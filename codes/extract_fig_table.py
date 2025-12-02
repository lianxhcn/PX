# -*- coding: utf-8 -*-
"""
从指定文件夹中，找到文件名包含 title_keywords 的 PDF，
并基于 "Figure/Fig./Table + number" 的 caption 位置，截图导出 Figures 和 Tables。

依赖：
    pip install pymupdf

用法示例：
    python extract_fig_table.py --folder "." --title_keywords "Guo-2020-JDE"
"""

import argparse
import os
import re
import shutil
from pathlib import Path

import fitz  # PyMuPDF


# -----------------------------
# 文本与编号解析
# -----------------------------
FIG_PATTERN = re.compile(r"^\s*(figure|fig\.?)\s*([0-9]+)\b", re.IGNORECASE)
TAB_PATTERN = re.compile(r"^\s*(table)\s*([0-9]+)\b", re.IGNORECASE)


def _iter_caption_lines(page: fitz.Page):
    """
    逐行产出 (line_text, line_rect)。
    使用 get_text("dict") 获取更细粒度的行与坐标信息。
    """
    d = page.get_text("dict")
    for block in d.get("blocks", []):
        if block.get("type", 1) != 0:
            # type=0 为文本；其他类型（如图片）先跳过
            continue
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            if not spans:
                continue

            # 拼接该行文本，并合并该行的 bbox
            line_text = "".join(s.get("text", "") for s in spans).strip()
            x0 = min(s["bbox"][0] for s in spans)
            y0 = min(s["bbox"][1] for s in spans)
            x1 = max(s["bbox"][2] for s in spans)
            y1 = max(s["bbox"][3] for s in spans)
            yield line_text, fitz.Rect(x0, y0, x1, y1)


def _find_captions_on_page(page: fitz.Page):
    """
    返回该页所有 caption：
        [{"kind": "Figure"/"Table", "num": int|None, "rect": fitz.Rect, "text": str}, ...]
    说明：
        - 只匹配行首出现 Figure/Fig./Table 的 caption（更稳健，误报更少）。
        - caption 可能跨行：这里做一个简单合并（相邻行 y 距离很近且缩进相近）。
    """
    lines = list(_iter_caption_lines(page))
    caps = []

    i = 0
    while i < len(lines):
        text, rect = lines[i]

        m_fig = FIG_PATTERN.match(text)
        m_tab = TAB_PATTERN.match(text)

        if not (m_fig or m_tab):
            i += 1
            continue

        if m_fig:
            kind = "Figure"
            num = int(m_fig.group(2))
        else:
            kind = "Table"
            num = int(m_tab.group(2))

        # 尝试合并 caption 后续行：常见情形是 caption 换行
        merged_text = text
        merged_rect = fitz.Rect(rect)

        j = i + 1
        while j < len(lines):
            nxt_text, nxt_rect = lines[j]

            # 合并条件（启发式）：
            # 1) 行间距较小（例如 <= 12pt）
            # 2) 下一行不再以 Figure/Table 开头（避免把下一个 caption 吃进来）
            # 3) x0 相近（缩进相近）
            if (nxt_rect.y0 - merged_rect.y1) <= 12 and \
               not (FIG_PATTERN.match(nxt_text) or TAB_PATTERN.match(nxt_text)) and \
               abs(nxt_rect.x0 - merged_rect.x0) <= 30:
                merged_text = (merged_text + " " + nxt_text).strip()
                merged_rect |= nxt_rect
                j += 1
            else:
                break

        caps.append({
            "kind": kind,
            "num": num,
            "rect": merged_rect,
            "text": merged_text
        })
        i = j

    return caps


# -----------------------------
# 裁剪与渲染
# -----------------------------
def _clip_by_caption(page: fitz.Page, cap: dict):
    """
    基于 caption 的 bbox 生成截图区域 clip。
    说明：纯启发式，力求“尽量截图到图/表 + caption”。
    """
    r = cap["rect"]
    page_rect = page.rect
    H = page_rect.height

    # 一些通用边距（单位：pt）
    margin_x = 20
    margin_y = 10

    if cap["kind"] == "Figure":
        # 常见布局：Figure 在上，caption 在下
        y0 = max(page_rect.y0, r.y0 - 0.55 * H)
        y1 = min(page_rect.y1, r.y1 + 0.10 * H)
    else:
        # 常见布局：Table caption 在上，表格内容在下
        y0 = max(page_rect.y0, r.y0 - 0.10 * H)
        y1 = min(page_rect.y1, r.y1 + 0.55 * H)

    x0 = max(page_rect.x0, r.x0 - margin_x)
    x1 = min(page_rect.x1, r.x1 + (page_rect.width * 0.90))  # 倾向抓到更完整的图/表宽度

    # 如果 x1 没扩到足够宽，直接扩到页面近乎全宽（论文图表通常比较宽）
    if (x1 - x0) < 0.60 * page_rect.width:
        x0 = max(page_rect.x0, page_rect.x0 + 10)
        x1 = min(page_rect.x1, page_rect.x1 - 10)

    clip = fitz.Rect(x0, y0 - margin_y, x1, y1 + margin_y)
    clip = clip & page_rect  # 截断到页面范围内
    return clip


def _render_clip_to_png(page: fitz.Page, clip: fitz.Rect, out_png: Path, target_width_px: int = 1000):
    """
    将 clip 区域渲染为 PNG：
        - 宽度固定 target_width_px
        - 高度自适应
    """
    rect_w = max(1.0, clip.width)

    # 计算缩放：让输出宽度接近 target_width_px
    zoom = target_width_px / rect_w

    # 防止过大/过小：过大可能很慢，过小会糊
    zoom = max(1.0, min(zoom, 6.0))

    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
    pix.save(str(out_png))


# -----------------------------
# 主过程
# -----------------------------
def extract_figures_tables(folder: str, title_keywords: str):
    base = Path(folder).expanduser().resolve()
    if not base.exists():
        raise FileNotFoundError(f"folder 不存在：{base}")

    # 搜索 PDF：文件名包含 title_keywords（不区分大小写）
    kw_lower = title_keywords.lower()
    pdf_files = sorted([p for p in base.glob("*.pdf") if kw_lower in p.name.lower()])

    if not pdf_files:
        print(f"未找到匹配的 PDF：folder={base}, title_keywords={title_keywords}")
        return

    # 输出目录：在当前工作路径下创建
    output_folder = Path.cwd() / f"{title_keywords}-out"
    if output_folder.exists():
        shutil.rmtree(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    fig_seen = set()   # (pdf_name, fig_num, page_index, y0) 去重
    tab_seen = set()

    for pdf_path in pdf_files:
        doc = fitz.open(str(pdf_path))
        try:
            for page_index in range(doc.page_count):
                page = doc.load_page(page_index)
                caps = _find_captions_on_page(page)

                for cap in caps:
                    clip = _clip_by_caption(page, cap)

                    # 去重 key（避免同一 caption 多次匹配或跨行重复）
                    key = (pdf_path.name, cap["num"], page_index, round(cap["rect"].y0, 1))
                    if cap["kind"] == "Figure":
                        if key in fig_seen:
                            continue
                        fig_seen.add(key)
                        out_name = f"{title_keywords}-Figure{cap['num']}.png"
                    else:
                        if key in tab_seen:
                            continue
                        tab_seen.add(key)
                        out_name = f"{title_keywords}-Table{cap['num']}.png"

                    out_png = output_folder / out_name

                    # 若同名已存在（例如不同 PDF 都有 Figure 1），则追加后缀避免覆盖
                    if out_png.exists():
                        stem = out_png.stem
                        suffix = out_png.suffix
                        k = 2
                        while True:
                            cand = output_folder / f"{stem}-{k}{suffix}"
                            if not cand.exists():
                                out_png = cand
                                break
                            k += 1

                    _render_clip_to_png(page, clip, out_png, target_width_px=1000)

        finally:
            doc.close()

    print(f"完成。输出目录：{output_folder}")


def main():
    parser = argparse.ArgumentParser(description="Extract Figures and Tables screenshots from PDFs.")
    parser.add_argument("--folder", type=str, default=".", help="包含 PDF 文件的文件夹路径，默认当前路径")
    parser.add_argument("--title_keywords", type=str, required=True, help="用于匹配 PDF 文件名的关键词字符串")
    args = parser.parse_args()

    extract_figures_tables(args.folder, args.title_keywords)


if __name__ == "__main__":
    main()
