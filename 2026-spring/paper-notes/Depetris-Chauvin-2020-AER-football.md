# 中文精要：Depetris-Chauvin-2020-AER


> Depetris-Chauvin, E., Durante, R., & Campante, F. (**2020**). Building Nations through Shared Experiences: Evidence from African Football. **American Economic Review**, 110(5), 1572–1602. [Link](https://doi.org/10.1257/aer.20180805), [PDF](http://sci-hub.ren/10.1257/aer.20180805), [-PDF2-](https://filipecampante.org/wp-content/uploads/2021/07/campante_BuildingNations_May2020.pdf), [Appendix](https://www.aeaweb.org/doi/10.1257/aer.20180805.appx), [-cited-](https://scholar.google.com/scholar?cites=2247119565205502563&as_sdt=2005&sciodt=0,5&hl=zh-CN), [-Replication-](http://doi.org/10.3886/E115011V1), [Google](<https://scholar.google.com/scholar?q=Building Nations through Shared Experiences: Evidence from African Football>), [Correction 2024](https://www.aeaweb.org/content/file?id=21819).
  - **复现报告**：Delpeyrou, L., S. Bertoli. (2024). "——": a Replication of Depetris-Chauvin, Durante and Campante (2020). [-Link-](https://www.econstor.eu/handle/10419/307961), [-PDF-](https://www.econstor.eu/bitstream/10419/307961/1/I4R-DP193.pdf), [-Replication codes and data-](https://www.dropbox.com/scl/fo/lk7akxuy82rpews8b8jq2/AFuSJm69qeI1Jq585_qwm64?rlkey=j0tjju8iu1botoslymr9m1jbx&e=1&st=4adnj4v4&dl=0). 
  - **原作者回应**：Filipe Campante, F., Depetris-Chauvin E., Durante R. (2024). "——": A Reply to Delpeyrou and Bertoli (2024). I4R working paper. [-Link-](https://www.rwi-essen.de/i4r-discussion-paper-series/1/building-nations-through-shared-experiences-evidence-from-25010605), [-PDF-](https://www.econstor.eu/bitstream/10419/307962/1/I4R-DP194.pdf).


---


## 1. 简介

这篇论文回答一个看似「软」、但在发展经济学与政治经济学中很「硬」的问题：共享的集体经历(collective experiences)能否帮助塑造民族国家意义上的国家认同(national identity)，并进一步缓和族群冲突(ethnic conflict)？

作者用撒哈拉以南非洲国家队足球成绩作为「集体经历」的可观测冲击，做了两条并行、相互支撑的证据链：

* 个体层面：把 Afrobarometer 访谈日期与国家队重要比赛的胜负「对齐」，比较「比赛前几天被访谈的人」与「比赛后几天被访谈的人」在族群认同、跨族群信任等指标上的差异。核心发现是：重要胜利后，受访者「主要认同族群而非国家」的概率显著下降，同时跨族群信任上升。
* 国家层面：利用非洲国家杯(Africa Cup of Nations, AFCON)预选赛中「险胜晋级」与「险负出局」的近邻对比(close qualification)，考察晋级带来的国家荣誉冲击，是否会在随后几个月降低国内冲突事件。作者发现：险胜晋级的国家在接下来约半年内的内战/冲突事件更少(大约减少 9%)。

这两条证据链的共同点是：都把体育成绩处理为一种「可预期但结果不完全可控」的全国性共同经历，并强调其短期内对身份凸显(salience)与社会互信的影响，进而可能打开降低暴力冲突的「窗口期」。论文摘要给出的量级描述是：重要胜利后，族群优先认同显著下降(相对幅度约 37%)，跨族群信任上升(约 30%)，而险胜晋级 AFCON 的国家随后冲突事件更少(约 9%)。

## 2. 研究问题与理论直觉

论文背后的直觉并不神秘：身份认同具有情境性。很多时候，人们并非「没有国家认同」，而是「在特定场景下，族群身份更被激活」。足球国家队比赛恰好是一个强烈、同步、可共同体验的全国事件，它可能通过两条相对不同的通道改变行为与态度：

第一条通道是「身份凸显与共同命运」。当国家队取胜时，个体更容易把「我们」理解为国家共同体，而非仅仅是族群共同体。于是，在问卷中「我更接近族群还是国家」的回答会向国家侧移动。论文把这种变化理解为一种短期的 priming 效应：不是永久改造身份结构，而是改变当下做判断时最显著的身份标签。

第二条通道是「角色示范(role modeling)」。如果国家队阵容本身跨族群协作明显，那么胜利不仅仅是「国家赢了」，更是「不同族群一起赢了」，从而降低对外群体(out-group)的不信任。这也解释了作者为什么特别去构造了「国家队内部族群多样性(team diversity)」并做异质性检验：队伍越多元，胜利的「融合作用」应越强。

## 3. 数据来源和变量界定

### 3.1 足球比赛数据 (「冲击」如何定义)

作者收集了撒哈拉以南非洲国家队在主要国际赛事中的官方比赛信息，并区分「重要比赛」(例如正式赛事/预选赛)与「友谊赛」等低 stakes 情形。重要性区分在识别上很关键：如果效果主要来自「全国性共同关注」，那么低关注度的友谊赛不应产生同样的身份变化。论文的异质性结果也确实把这一点作为识别的「对照」。

### 3.2 Afrobarometer 个体数据与核心变量

个体层面核心因变量是一个二元指标：受访者是否「主要认同族群而非国家」(文中称为 ethnic over national identity)。它来自 Afrobarometer 关于身份归属的标准题项，并把回答映射为 $y_{icm}\in{0,1}$。

关键解释变量是 Post-victory：受访者是否在「国家队一场重要胜利之后」的短窗口内被访谈。论文主要使用「赛后 15 天内」的窗口，并将样本限制在「比赛前 15 天到比赛后 15 天」的受访者，以强化时间可比性。

作者还构造了一系列「态度与信任」类因变量，用于验证机制与外推：例如对其他族群的信任(interethnic trust)、是否愿意与其他族群做邻居等。

### 3.3 冲突数据与「险胜晋级」样本

国家层面的冲突结果来自 ACLED(Armed Conflict Location & Event Data)，以国家-周为单位构造冲突事件数量，并使用 $\ln(1+\text{events})$ 作为主要因变量，以降低极端值影响。
(ACLED 数据集的基准介绍见 Raleigh et al. 2010，DOI: 10.1177/0022343310378914。

「险胜晋级」设计围绕 AFCON 预选赛：把那些在预选赛最后阶段「仍有晋级可能」且最终以极小差距晋级/出局的国家，视为近似随机地落在胜负两侧，从而得到一个更接近准实验的国家层面冲击。

## 4. 研究设计和识别策略

### 4.1 个体层面：Event × Survey 的「几乎随机访问顺序」设计

作者的核心回归可以概括为：

$$
y_{icm}=\alpha+\beta ,\text{PostVictory}*{icm}+\gamma X_i+\mu*{cm}+\lambda_{g(i)t}+\varepsilon_{icm}
$$

其中 $i$ 是个体，$c$ 是国家，$m$ 是比赛(或与比赛相关的事件窗口)。$\mu_{cm}$ 是 country × match 固定效应，意味着比较发生在「同一场比赛、同一国家」的受访者之间；$\lambda_{g(i)t}$ 是语言/族群组别 × 年份等高维控制，用于吸收慢变的组别差异。论文强调的识别逻辑是：在控制这些固定效应后，访谈日期相对比赛日的前后更接近「调研物流导致的近似随机」。

这一设计的关键优势是：它把「国家间差异」(更民族主义的国家可能更常赢球)与「比赛选择偏误」(强队更易赢)尽可能压缩到固定效应里，让 $\beta$ 主要由「同一场比赛前后几天的受访者差异」识别。

识别假设在课堂上可以讲成三句话：

* 受访者在赛前/赛后被访问的概率不应系统性相关于其未观测的族群主义倾向；
* 赛后窗口内除了比赛胜利，不应有同时发生且同向影响身份认同的全国性冲击；
* 即便存在一些全国性新闻，只有「重要胜利」才应产生系统性变化，而友谊赛等低关注事件不应同样显著。

论文用「友谊赛无效应」「重要胜利更强」「意外胜利更强」等模式去支撑这些假设的可信度。

### 4.2 国家层面：Close Qualification 的准实验

国家-周层面作者估计的结构可写为：

$$
\ln(1+\text{conflict}*{cqw})=\alpha+\beta,\text{PostQual}*{cqw}+\theta_c+\rho_q+\delta_w+\tau_{cq}+\varepsilon_{cqw}
$$

其中 $c$ 为国家，$q$ 为预选赛 campaign，$w$ 为周。$\tau_{cq}$ 表示国家 × campaign 固定效应，吸收一国在某次预选赛阶段的总体水平；$\delta_w$ 等时间固定效应吸收共同时间冲击。PostQual 表示在「预选赛结束后 25 周」内，且只在 close qualification 样本中比较「险胜晋级」与「险负出局」。

这一步的识别要点是：把「晋级」当作国家层面的共同经历冲击，而 close qualification 让晋级与否更接近「不可精确操控的边缘结果」。在此框架下，$\beta<0$ 可以解释为：晋级带来的短期国家认同与社会凝聚提升，使得冲突事件在随后一段时间内下降。

## 5. 主要实证结果与解释

### 5.1 个体层面主结果：族群优先认同下降

论文最核心的表格之一是 Table 2：在控制 country × match 固定效应、个体控制变量等后，Post-victory 的系数大约在 -0.06 左右，意味着「重要胜利后 15 天内被访谈」的人，更不容易回答「我主要认同族群而非国家」。

从量级上看，Table 2 报告的基准列中 Post-victory 系数约为 -0.064，样本均值约为 0.173。直观解读是：重要胜利与族群优先认同的下降相关，且相对均值变动幅度不小。

【插入图表 Table 2】
说明：把 Table 2 的不同列当作「逐步锁死的对照实验」，课堂上可逐列解释控制集与固定效应如何强化「同场比赛前后对比」的识别逻辑。

### 5.2 态度结果：跨族群信任上升，但对外群体可能更复杂

Table 4 显示，重要胜利后受访者对「同胞」的信任上升，对「其他族群」的信任也上升(例如 interethnic trust 的系数约 0.04)，并且与「愿意与其他族群做邻居」类指标一致。

同时，论文也提醒一种可能的张力：更强的国家认同未必总是「温和的」，它在某些语境下也可能与「对外部者的排斥」并存。作者在文本中讨论了相关文献并做了部分检验，整体结论更偏向「对内整合显著」，而对外排斥并非主要驱动。

【插入图表 Table 4】
说明：这张表适合用来训练学生区分「认同变化」和「社会偏好变化」：前者是身份标签的凸显，后者是对 out-group 行为倾向的改变。

### 5.3 异质性与机制：何时效果更强

论文的 Table 3 提供了一组非常「教学友好」的异质性结果，它们共同指向「共同经历必须足够重要、足够出乎意料、且具有跨族群协作可见性」：

* 友谊赛胜利基本不产生同样的认同变化(低 stakes 对照)。
* 如果胜利是「意外的」(upset)，效果更强，符合「情绪冲击/注意力」机制。
* 当国家队内部族群多样性更高时，胜利带来的认同变化更强，支持「角色示范(role modeling)」解释。
* 当地方国家能力(公共品供给)更强时，胜利的边际效应反而更弱，暗示「常规国家建构手段」与「共享经历」可能是替代关系：国家认同本来就更稳固的地方，体育胜利可「再提升」的空间更小。

【插入图表 Table 3】
说明：Table 3 很适合在博士生写作课中作为「机制检验与边界条件」的示范：每一个交互项都在回答「如果机制为真，在哪些情形下效应应更大或更小」。

### 5.4 国家层面：险胜晋级降低后续冲突

Table 6 报告了 close qualification 设计的核心结果：Post-qualification 的系数约为 -0.090。由于因变量是 $\ln(1+\text{events})$，论文将其解释为冲突事件数量在数量级上下降约 $e^{-0.090}-1\approx -8.6%$，与摘要中的「约 9% 更少冲突事件」一致。

【插入图表 Table 6】
说明：课堂上可以让学生练习「半弹性(semielasticity)」的读法：当因变量取对数时，系数如何转换成百分比变化。

### 5.5 稳健性与多重检验

这篇论文的稳健性讨论有两点特别值得在方法课强调：

* 多重结果与多重假设：作者面对「身份、信任、邻里偏好、冲突」等一组相关但不同的因变量，强调不能只挑显著结果，而需要考虑 multiple inference 的问题，并引用 Anderson (2008) 的修正思路(基于 FDR 或 family-wise 的校正)。
* 「验证识别而非堆砌控制」：个体层面的关键并不是把 $X_i$ 加到无穷多，而是用 country × match 固定效应把比较锁定在同一场比赛前后，并通过友谊赛、意外胜利、时间窗口多种方式验证「结果模式」与机制一致。

## 6. 写作与研究设计

如果把这篇论文当作「研究设计练习题」，它最可学的不是「足球很重要」，而是作者如何把一个很难测量的概念(国家认同、族群裂痕)分解成可识别的经验对象：

第一步，把理论概念落在可重复测量的问卷题项上。作者用 Afrobarometer 的身份归属题构造二元指标，并用信任、邻里偏好等多维结果去交叉验证，这避免了「单一指标解释过度」。

第二步，把「冲击」设计成尽可能外生的时间错位。个体层面的关键是「比赛日是全国共同节点，而访问顺序较难被受访者操控」，于是形成 event × survey 的准实验结构。

第三步，用第二条证据链做外部效度与行为后果。很多关于身份的论文会停留在态度指标，作者进一步用 close qualification 连接到真实冲突事件，构成「从认同到暴力」的行为链条，这对论文说服力非常关键。

第四步，机制检验写成「可证伪的异质性预测」。例如「队伍越多元 → role modeling 越强 → 效果越大」，这类检验不是装饰，而是在告诉读者：如果你不相信我的故事，你至少要解释为什么这些交互项呈现出这样的符号与梯度。

## 7. 预留插图与表格位置(便于你随后截图插入)

* 插入图表 Table 1：样本描述与平衡性检验

  * 说明：用来解释「赛前/赛后访问样本」在可观测特征上是否接近可比。

* 插入图表 Table 2：个体层面主回归(族群优先认同)

  * 说明：逐列讲清固定效应、控制变量与标准误处理是如何把识别锁定在「同一场比赛前后」。

* 插入图表 Table 3：异质性与机制(重要性、意外性、国家能力、队伍多样性)

  * 说明：把每个交互项都当作一个「机制的可证伪预测」。

* 插入图表 Table 4：信任与偏好结果

  * 说明：展示「认同变化」是否伴随「跨族群信任与互动意愿」的变化。

* 插入图表 Table 6：close qualification 与冲突事件

  * 说明：训练对数因变量的系数解读，并讨论国家层面识别假设。

## 8. 引文信息
- Depetris-Chauvin, E., Durante, R., & Campante, F. (2020). Building Nations through Shared Experiences: Evidence from African Football. *American Economic Review*, 110(5), 1572–1602. [Link](https://doi.org/10.1257/aer.20180805), [PDF](https://filipecampante.org/wp-content/uploads/2021/07/campante_BuildingNations_May2020.pdf), [Replication](https://doi.org/10.3886/E115011V1), [Google](https://scholar.google.com/scholar?q=Building%20Nations%20through%20Shared%20Experiences%3A%20Evidence%20from%20African%20Football)。 
- Anderson, M. L. (2008). Multiple Inference and Gender Differences in the Effects of Early Intervention: A Reevaluation of the Abecedarian, Perry Preschool, and Early Training Projects. Journal of the American Statistical Association, 103(484), 1481–1495. [Link](https://doi.org/10.1198/016214508000000841), [PDF](http://sci-hub.ren/10.1198/016214508000000841), [Google](<https://scholar.google.com/scholar?q=Multiple Inference and Gender Differences in the Effects of Early Intervention: A Reevaluation of the Abecedarian, Perry Preschool, and Early Training Projects>).
- Raleigh, C., Linke,  Rew, Hegre, H., & Karlsen, J. (2010). Introducing ACLED: An Armed Conflict Location and Event Dataset. Journal of Peace Research, 47(5), 651–660. [Link](https://doi.org/10.1177/0022343310378914), [PDF](http://sci-hub.ren/10.1177/0022343310378914), [Google](<https://scholar.google.com/scholar?q=Introducing ACLED: An Armed Conflict Location and Event Dataset>). 
- Cederman, L.-E., Wimmer, A., & Min, B. (2009). Why Do Ethnic Groups Rebel? New Data and Analysis. World Politics, 62(1), 87–119. [Link](https://doi.org/10.1017/S0043887109990219), [PDF](http://sci-hub.ren/10.1017/S0043887109990219), [Google](<https://scholar.google.com/scholar?q=Why Do Ethnic Groups Rebel? New Data and Analysis>).
- Fearon, J. D., & Laitin, D. D. (2003). Ethnicity, Insurgency, and Civil War. American Political Science Review, 97(01), 75–90. [Link](https://doi.org/10.1017/S0003055403000534), [PDF](http://sci-hub.ren/10.1017/S0003055403000534), [Google](<https://scholar.google.com/scholar?q=Ethnicity, Insurgency, and Civil War>). 
- Miguel, E. (2004). Tribe or Nation? Nation Building and Public Goods in Kenya versus Tanzania. World Politics, 56(3), 327–362. [Link](https://doi.org/10.1017/S0043887100004330), [PDF](http://sci-hub.ren/10.1017/S0043887100004330), [Google](<https://scholar.google.com/scholar?q=Tribe or Nation? Nation Building and Public Goods in Kenya versus Tanzania>). 
- Card, D., & Dahl, G. B. (2011). Family Violence and Football: The Effect of Unexpected Emotional Cues on Violent Behavior*. The Quarterly Journal of Economics, 126(1), 103–143. [Link](https://doi.org/10.1093/qje/qjr001) (rep), [PDF](http://sci-hub.ren/10.1093/qje/qjr001), [Google](<https://scholar.google.com/scholar?q=Family Violence and Football: The Effect of Unexpected Emotional Cues on Violent Behavior*>). 
- Easterly, W., & Levine, R. (1997). Africa’s Growth Tragedy: Policies and Ethnic Divisions. The Quarterly Journal of Economics, 112(4), 1203–1250. [Link](https://doi.org/10.1162/003355300555466), [PDF](http://sci-hub.ren/10.1162/003355300555466), [Google](<https://scholar.google.com/scholar?q=Africa’s Growth Tragedy: Policies and Ethnic Divisions>).
