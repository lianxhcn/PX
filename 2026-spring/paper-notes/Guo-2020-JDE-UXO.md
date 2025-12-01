
# 中文精要：Guo-2020-JDE

>**Guo, S.** (**2020**). The legacy effect of unexploded bombs on educational attainment in Laos. **Journal of Development Economics**, 147, 102527. [Link](https://doi.org/10.1016/j.jdeveco.2020.102527), [PDF](https://file-lianxh.oss-cn-shenzhen.aliyuncs.com/Refs/2026-Spring/Guo_2020_The_legacy_effect_of_unexploded_bombs_on_educational_attainment_in_Laos.pdf), [Google](<https://scholar.google.com/scholar?q=The legacy effect of unexploded bombs on educational attainment in Laos>). [背景介绍](https://storymaps.arcgis.com/stories/d11a4299f1b4462b88efcf7f2262afb6)

- 这篇论文研究了越战期间美国在老挝投下的未爆炸弹（UXO）对当地居民教育水平的长期影响。作者利用地理信息系统（GIS）数据，将未爆炸弹的密度与教育结果进行关联分析，发现未爆炸弹的存在显著降低了受影响地区儿童的入学率和完成学业的可能性。论文还探讨了未爆炸弹对家庭经济状况和社区发展的间接影响，强调了战争遗留问题对社会经济发展的深远影响。

[toc]

## 1. 简介

本文研究「战争遗留的未爆炸弹药 (unexploded ordnance, UXO)」如何在战后长期影响老挝的人力资本积累，核心关注教育年限 (years of education)。老挝在 1964–1973 年间遭受密集空袭，UXO 作为战争遗产持续污染农村与耕地，作者强调这种「遗留效应 (legacy effect)」不仅影响战争时期学龄儿童 (education interruption)，也会在战后很久仍然压低新出生队列的教育水平。

论文的主结论可以用一句话概括：在美国轰炸结束 20 年后，处于学龄阶段且暴露在「平均水平 UXO 污染」下的儿童，仍然少约 1.3 年受教育年限。 

机制上，作者排除了一批常见渠道(代际教育传递、学校可达性、健康、财富冲击、选择性迁移等)，转而给出一条更贴近农村生产结构的解释：UXO 进入农田后，农事操作需要「更慢、更谨慎」，导致耕作效率下降；在以自给农业为主的环境下，为维持生计就需要投入更多农业劳动，于是儿童更容易辍学补充家庭劳动力。 

## 2. 政策背景和研究问题

![20251201101344](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251201101344.png)

![20251201103600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251201103600.png)

> Source: Samuel Smith, 2021. The Plague of Unexploded Vietnam-Era Bombs in Southeast Asia. [-Link-](https://storymaps.arcgis.com/stories/d11a4299f1b4462b88efcf7f2262afb6)




### 2.1 冲突与轰炸：为何 UXO 会成为长期约束

老挝内战与越战外溢使其成为空袭重点区域。美国自 1964 年起在老挝发动空战，累计约 541,344 次轰炸任务，投放约 210 万吨弹药(超过二战时期美国用弹量)，并留下大量未爆炸的集束弹。 

作者强调两个事实，使「UXO → 教育」成为值得严肃识别的长期问题：

* 污染范围广：UXO 约污染 25% 的村庄、50% 的农业用地。 
* 清排缓慢且代价高：1996–2012 年间，污染土地清排不足 1%，意味着 UXO 的约束会跨队列持续存在。

### 2.2 研究问题与分解：exposure effect vs. legacy effect

论文把冲击分成两类、并分别用数据去识别：

* **Exposure effect**：战争期间「当期轰炸」对正在上学的队列造成直接中断。
* **Legacy effect**：战争结束后，UXO 作为「存量约束」继续通过生产与劳动需求机制影响后续出生队列的教育积累。

因此，识别目标不仅是「轰炸是否降低教育」，更关键是：在轰炸停止后，UXO 是否仍能在经济结构中产生持续性教育缺口，以及它通过何种可检验的机制发生。

## 3. 数据来源和变量界定

### 3.1 数据来源与样本构建

作者将多个村级与个体级数据合并：

* **UXO 污染(村级)**：2011 年老挝农业普查 (Agricultural Census) 调查村长「本村有多少农业地块受 UXO 影响」，形成更直接的 UXO incidences 指标。 
* **轰炸强度(村级)**：Theater History of Operations Reports 数据库记录每次空袭任务的目标坐标与武器类型，作者据此计算每村附近一定半径内的 bombing missions。
* **教育与个体特征(个体级)**：World Bank 的 Laos STEP Skills Measurement Household Survey 2012，合并后样本为 17 个省、182 个村、2,706 户、13,512 个个体。 

此外，作者使用人口普查与农业普查中的地理与自然条件变量(如到省会/县城通行时间、地形类型、灾害等)作为村级外生控制项。

### 3.2 关键变量

* 被解释变量：$EDU_{ivp}$，个体 $i$ 在村 $v$、省 $p$ 的受教育年限 (years of education)。
* 核心解释变量：$UXO_v$，村级 UXO 密度。作者将以村中心 (centroid) 为圆心、10 km 半径内「周边村落」的 UXO 与轰炸强度加总，构造：

  * $UXO(10km)$：10 km 内 UXO-affected plots 数量
  * $Bomb(10km)$：10 km 内 bombing missions 数量
    两者相关系数约 0.6，且样本村在 10 km 内的平均值分别约为 6.6 与 512.5(单位为 plots 与 missions)。
* 样本限制：作者将样本限制为在 1964–1973 轰炸期「处于或进入义务教育年龄 (9–15 岁)」的个体，并剔除 1949 年前出生者(约占 5%)。

![20251201111616](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251201111616.png)



## 4. 研究设计和识别策略

### 4.1 基准模型 (OLS/2SLS) 与控制结构

基准回归写为：

$$
EDU_{ivp}=\beta UXO_v+D_i'\alpha+X_v'\delta+c_i\theta_p+\mu_p+\varepsilon_{ivp}
$$

其中 $D_i$ 包含个体与家庭特征(性别、年龄、婚姻、家庭规模、户主年龄与性别等)，$X_v$ 为村庄地理与自然条件(城乡、到省会/县城通行时间、地形、灾害、降雨等)，$\mu_p$ 为省固定效应，$c_i\theta_p$ 表示省份特定的「随出生队列变化」趋势项；标准误在村级聚类。

### 4.2 内生性来源与工具变量设计

核心内生性担忧是：轰炸与 UXO 并非随机落点，若轰炸强度与长期发展潜力、地理通达性等不可观测因素相关，则 $UXO_v$ 与 $\varepsilon_{ivp}$ 相关，OLS 有偏。

作者的 IV 来自轰炸的地理结构：美国轰炸主要集中于两大区域，北部的 Plain of Jars (POJ) 与南部的 Ho Chi Minh Trail (HCMT)。作者用「每个村庄到 POJ 与 HCMT 的距离」作为工具变量 $DIST_v$，并指出靠近这两个中心的村庄，轰炸任务更多、UXO 密度更高。 

IV 的可信度，作者主要从三点支撑：

* **相关性 (first stage)**：距离到两大轰炸中心可显著预测 bombing missions 与 UXO 密度。
* **排除限制的讨论**：作者强调「炸弹是否未爆」带有较大随机性，从而削弱了「距离直接影响教育」的担忧，并以一系列排序/选择检验来反驳系统性迁移或村庄选择。
* **放松排除限制 (plausibly exogenous)**：作者进一步说明即使工具变量仅「近似外生」，负向 UXO 效应仍可被确认。

![20251201104326](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251201104326.png)

> **Figure 1**：全国 UXO-affected plots 与 bombing missions 的空间分布图。

![20251201111739](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251201111739.png)

![20251201111836](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251201111836.png)

### 4.3 队列分解：识别 legacy effect 的关键做法

文章在动机上强调：如果仅看战争当期队列，难以区分「轰炸中断」与「UXO 存量遗留」；因此作者用出生队列与 UXO 的交互项来分解不同阶段的效应，分别刻画 wartime 学龄暴露与战后学龄暴露所对应的 exposure effect 与 legacy effect。其核心识别逻辑是：同一村庄的 UXO 存量对不同出生队列的教育影响应呈现系统差异，且战后队列的负向效应若持续存在，就更支持「UXO → 农业劳动需求 → 辍学」这一长期机制。

## 5. 主要实证结果和结论

### 5.1 基准影响：UXO 显著压低教育年限

作者在摘要与引言中给出最具教学价值的量级表达：在美国轰炸结束 20 年后，学龄儿童若暴露于「平均水平」UXO 污染，教育年限仍然少约 1.3 年。 

在更一般的表述上，作者报告：UXO 密度(用 $UXO(10km)$ 与 $Bomb(10km)$ 两种口径分别测量)均会显著降低教育年限；平均暴露对应约 0.2–0.3 年的教育损失，1 个标准差上升对应约 0.6–0.9 年损失。



### 5.2 OLS 为什么会「低估」：把“方向正确”变成“可信识别”

作者明确指出 OLS 会低估 UXO 的负向影响，并通过「稳健得分检验」提示：若 $UXO_v$ 存在内生性，OLS 估计不一致，因此需要 2SLS 框架来将解释转移到更可信的外生变动上。 

课堂上更好的说法是：本文不是在告诉你「加点控制变量就行」，而是在展示一种研究流程——先承认轰炸地点可能内生，然后用轰炸地理结构构造 $DIST_v$，再用排序检验与 plausibly exogenous 去处理排除限制的担忧，逐步把结论从“相关”推进到“更接近因果”。 

> **Table 4**：对比 OLS 与 2SLS、两种 UXO 口径的一致性。 

![20251201112615](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251201112615.png)

### 5.3 队列结果：同时看到 exposure effect 与 legacy effect

作者强调 UXO 的影响不仅来自 wartime 学龄队列的直接中断，还会持续作用于 postwar birth cohorts，这一点在摘要中被反复强调，是论文标题「legacy effect」的实证含义。 

* 插入 Figure(队列效应图) 与对应回归表：建议你在讲解时把队列划分与国家历史时间线并排展示：轰炸期 (1964–1973)、战后前 10 年、战后 20 年，并解释为什么「战后 20 年仍然显著」更支持机制而非单纯的战争中断。

### 5.4 机制检验：为何是“农田 UXO → 劳动需求 → 辍学”

作者对机制的叙事是高度结构化的：

* 先「排除」：代际传递、学校可达性、健康、财富、迁移等不足以解释。
* 再「确认」：在 UXO 密度更高的村庄，农民耕作更慢更谨慎，农业劳动投入更长，农业部门吸纳更多劳动；且教育损失主要由拥有农业用地的家庭驱动。

你在课堂上可以把这条机制写成一条可检验的链条(并提示每一环对应什么数据)：

$$
UXO_v \rightarrow \text{(lower farm efficiency)} \rightarrow \text{(higher labor demand in subsistence farming)} \rightarrow \text{(school dropout)} \rightarrow EDU_{ivp}\downarrow
$$

* 插入“机制表”(农事投入、劳动配置、辍学/工作选择)：讲清楚每一列在验证链条的哪个环节，例如「劳动投入上升」是对效率下降的补偿，「年轻农业劳动力比例上升」与「儿童辍学」是对家庭劳动力约束的响应。

### 5.5 结果外溢：认知与劳动市场后果

作者将教育损失进一步连接到更广泛的发展结果：受教育更少的个体表现出更差的认知能力，更可能进入农业与家族经营，并拥有更低的劳动收入。更重要的是，作者用「循环陷阱」的语言强调：若 UXO 清排不足，低教育与低效率农业之间会形成代际循环。

* 插入“认知与收入”表：建议配合解释「教育年限损失」如何转化为技能与收入差距，并提示学生在自己研究中如何把教育效应延伸到劳动市场结果(avoid post-treatment controls 的讨论也可在此顺带提醒)。

## 6. 引文信息

- Guo, S. (2020). The legacy effect of unexploded bombs on educational attainment in Laos. Journal of Development Economics, 147, 102527. [Link](https://doi.org/10.1016/j.jdeveco.2020.102527), [PDF](http://sci-hub.ren/10.1016/j.jdeveco.2020.102527), [Google](<https://scholar.google.com/scholar?q=The legacy effect of unexploded bombs on educational attainment in Laos>).
- Conley, T. G., Hansen, C. B., & Rossi, P. E. (2012). Plausibly Exogenous. Review of Economics and Statistics, 94(1), 260–272. [Link](https://doi.org/10.1162/REST_a_00139), [PDF](http://sci-hub.ren/10.1162/REST_a_00139), [Google](<https://scholar.google.com/scholar?q=Plausibly Exogenous>).
- Miguel, E., & Roland, G. (2011). The long-run impact of bombing Vietnam. Journal of Development Economics, 96(1), 1–15. [Link](https://doi.org/10.1016/j.jdeveco.2010.07.004), [PDF](http://sci-hub.ren/10.1016/j.jdeveco.2010.07.004), [Google](<https://scholar.google.com/scholar?q=The long-run impact of bombing Vietnam>).
- Merrouche, O. (2011). The Long Term Educational Cost of War: Evidence from Landmine Contamination in Cambodia. Journal of Development Studies, 47(3), 399–416. [Link](https://doi.org/10.1080/00220388.2010.485633), [PDF](http://sci-hub.ren/10.1080/00220388.2010.485633), [Google](<https://scholar.google.com/scholar?q=The Long Term Educational Cost of War: Evidence from Landmine Contamination in Cambodia>).
- Blattman, C., & Miguel, E. (2010). Civil War. Journal of Economic Literature, 48(1), 3–57. [Link](https://doi.org/10.1257/jel.48.1.3) (rep), [PDF](http://sci-hub.ren/10.1257/jel.48.1.3), [Appendix](https://www.aeaweb.org/doi/10.1257/jel.48.1.3.appx), [Google](<https://scholar.google.com/scholar?q=Civil War>).

