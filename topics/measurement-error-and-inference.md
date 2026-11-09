<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->

# 测量误差与下游推断

[返回目录](../README.md) · [阅读路线](../docs/reading-routes.md)

研究生成变量的误分类、聚合误差及其对估计和不确定性的影响。

## 主目录（5 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2025 · MIS Quarterly · 期刊 | [Correcting Measurement Error in Regression Models with Variables Constructed from Aggregated Output of Data Mining Models](https://aisel.aisnet.org/misq/vol49/iss1/6/)<br>[解读与来源](../topics/measurement-error-and-inference.md#qiao-2025-aggregated-measurement-error) | 覆盖评论情感等个体预测聚合为产品或组织变量后的测量误差，补充逐条标签校正。 |
| 2023 · Science · 期刊 | [Prediction-powered inference](https://doi.org/10.1126/science.adi6000)<br>[解读与来源](../topics/measurement-error-and-inference.md#angelopoulos-2023-prediction-powered-inference) | 为文本变量的验证预算提供推断起点：独立标签既用于检查分类质量，也可用于校正估计。 |
| 2023 · NeurIPS · 主会 | [Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](https://papers.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract-Conference.html)<br>[解读与来源](../topics/measurement-error-and-inference.md#egami-2023-imperfect-surrogates) | 直接回答如何把 LLM 或其他分类器的代理标签用于统计推断，而不只评价标签预测准确率。 |
| 2021 · Information Systems Research · 期刊 | [Correcting Misclassification Bias in Regression Models with Variables Generated via Data Mining](https://pubsonline.informs.org/doi/10.1287/isre.2020.0977)<br>[解读与来源](../topics/measurement-error-and-inference.md#qiao-2021-misclassification-bias) | 直接处理从文本分类标签到回归推断的误差传播，区分预测指标与目标参数精度。 |
| 2018 · Information Systems Research · 期刊 | [Mind the Gap: Accounting for Measurement Error and Misclassification in Variables Generated via Data Mining](https://pubsonline.informs.org/doi/10.1287/isre.2017.0727)<br>[解读与来源](../topics/measurement-error-and-inference.md#yang-2018-mind-the-gap) | 为把文本预测分数当作观测变量的实证研究提供误差诊断和校正入口。 |


<a id="qiao-2025-aggregated-measurement-error"></a>
### Correcting Measurement Error in Regression Models with Variables Constructed from Aggregated Output of Data Mining Models

**2025 · MIS Quarterly · 期刊** · 期刊研究 · 主目录

**作者：** Mengke Qiao; Ke-Wei Huang

**研究内容：** 研究先分类个体文本、再聚合为群体变量进入回归的两阶段设计，提出精确校正及基于中心极限定理和大数定律的近似校正。

**为什么读：** 覆盖评论情感等个体预测聚合为产品或组织变量后的测量误差，补充逐条标签校正。

**适用条件与限制：** 近似方法的适用性与计算优势取决于聚合规模和相应渐近条件；摘要报告的结论只限论文检验情形。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aisel.aisnet.org/misq/vol49/iss1/6/)：已打开官方期刊存档/出版页面，核读题名、作者、期刊记录与摘要。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.25300/MISQ/2024/18026)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 测量误差与下游推断 · 测量验证与可比性

<a id="angelopoulos-2023-prediction-powered-inference"></a>
### Prediction-powered inference

**2023 · Science · 期刊** · 期刊研究 · 主目录

**作者：** Anastasios N. Angelopoulos; Stephen Bates; Clara Fannjiang; Michael I. Jordan; Tijana Zrnic

**研究内容：** 将少量带真实标签的观测与大量模型预测结合，用标签样本校正预测误差并构造目标总体参数的置信区间。

**为什么读：** 为文本变量的验证预算提供推断起点：独立标签既用于检查分类质量，也可用于校正估计。

**适用条件与限制：** 有效性依赖具体抽样和推断条件；不能把方便取得的标签当作代表性验证样本。校正统计估计不自动证明构念的内容效度。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://www.stat.ubc.ca/~john/papers/AngelopoulosScience2023.pdf)：机构保存的Science正式排印稿首页与刊期支持发表身份；出版社入口返回403。（2026-11-09）
- [content](https://arxiv.org/abs/2301.09633)：读取作者预印本摘要；与正式题名及作者对应，不以arXiv单独证明发表。（2026-11-09）

**其他目录：** [good_llm_stats_papers](https://github.com/sjsj0101/good_llm_stats_papers/blob/main/data/supplementary.yaml)

**主题：** 测量误差与下游推断

<a id="egami-2023-imperfect-surrogates"></a>
### Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models

**2023 · NeurIPS · 主会** · 会议论文 · 主目录

**作者：** Naoki Egami; Musashi Hinck; Brandon M. Stewart; Hanying Wei

**研究内容：** 将有偏的自动标签与较小的高质量人工标签样本结合，提出设计型监督学习估计量，以控制金标准抽样概率来支持下游回归推断。

**为什么读：** 直接回答如何把 LLM 或其他分类器的代理标签用于统计推断，而不只评价标签预测准确率。

**适用条件与限制：** 推断保证依赖金标准标签及其抽样设计，并有相应渐近条件；它校正代理误差，不替代目标构念和金标准本身的有效性论证。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://papers.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract-Conference.html)：检索工具返回该官方出版记录的完整题名、作者、发表身份及摘要缓存；页面直连失败（超时/403/重定向受限），没有获取出版全文。（2026-11-09）
- [content](https://arxiv.org/abs/2306.04746)：已打开 arXiv 记录并核读摘要，与官方 NeurIPS 2023 main-track 索引同题同作者；保留预印本版本关联。（2026-11-09）

**主题：** 测量误差与下游推断 · 文本标注与人工判断 · 测量验证与可比性

<a id="qiao-2021-misclassification-bias"></a>
### Correcting Misclassification Bias in Regression Models with Variables Generated via Data Mining

**2021 · Information Systems Research · 期刊** · 期刊研究 · 主目录

**作者：** Mengke Qiao; Ke-Wei Huang

**研究内容：** 分析数据挖掘生成的分类变量进入线性与非线性回归时的误分类偏差，推导所研究模型的校正式，并据校正后目标系数的精度选择分类模型。

**为什么读：** 直接处理从文本分类标签到回归推断的误差传播，区分预测指标与目标参数精度。

**适用条件与限制：** 一致性与精度结论依赖论文模型、误分类机制和可估计的校正量，不能从低分类准确率推得任意应用仍可可靠推断。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://pubsonline.informs.org/doi/10.1287/isre.2020.0977)：已打开官方期刊存档/出版页面，核读题名、作者、期刊记录与摘要。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.1287/isre.2020.0977)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 测量误差与下游推断 · 测量验证与可比性

<a id="yang-2018-mind-the-gap"></a>
### Mind the Gap: Accounting for Measurement Error and Misclassification in Variables Generated via Data Mining

**2018 · Information Systems Research · 期刊** · 观点／方法评论 · 主目录

**作者：** Mochen Yang; Gediminas Adomavicius; Gordon Burtch; Yuqing Ren

**研究内容：** 展示数据挖掘产生的回归变量即使预测表现较好，也可能引入系统估计偏差；讨论并通过模拟及案例演示 SIMEX 与 MC-SIMEX 的误差校正。

**为什么读：** 为把文本预测分数当作观测变量的实证研究提供误差诊断和校正入口。

**适用条件与限制：** 校正依赖误差方差或混淆矩阵等信息及其与分析样本的相容性；复杂误差与模型设定下不能将示例效果视为普遍保证。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://pubsonline.informs.org/doi/10.1287/isre.2017.0727)：已打开官方期刊存档/出版页面，核读题名、作者、期刊记录与摘要。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.1287/isre.2017.0727)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 测量误差与下游推断 · 测量验证与可比性

## 补充（1 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2018 · The Annals of Applied Statistics · 期刊 | [Statistical paradises and paradoxes in big data (I): Law of large populations, big data paradox, and the 2016 US presidential election](https://doi.org/10.1214/18-AOAS1161SF)<br>[解读与来源](../topics/measurement-error-and-inference.md#meng-2018-big-data-paradox) | 作为辅助统计背景，帮助区分增加可编码文本数量与改善目标总体覆盖；低标注成本本身不是代表性证据。 |


<a id="meng-2018-big-data-paradox"></a>
### Statistical paradises and paradoxes in big data (I): Law of large populations, big data paradox, and the 2016 US presidential election

**2018 · The Annals of Applied Statistics · 期刊** · 期刊研究 · 补充

**作者：** Xiao-Li Meng

**研究内容：** 将总体均值误差分解为数据质量、数据量和问题难度，解释带选择偏差的大样本为何仍可能产生很有把握的错误结论。

**为什么读：** 作为辅助统计背景，帮助区分增加可编码文本数量与改善目标总体覆盖；低标注成本本身不是代表性证据。

**适用条件与限制：** 主要讨论选择与记录机制引起的总体推断问题，不是LLM标注误差修正或构念效度方法。

**本轮证据：** 部分正文；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://statistics.fas.harvard.edu/sites/g/files/omnuum10116/files/statistics-2/files/statistical_paradises_and_paradoxes.pdf)：作者机构保存的正式排印稿首页列出刊名、2018卷期与DOI；读取摘要和误差分解引言。Project Euclid直接页面未返回正文。（2026-11-09）

**主题：** 测量误差与下游推断

## 跨主题阅读

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2023 · MIS Quarterly · 期刊 | [Extracting Actionable Insights from Text Data: A Stable Topic Model Approach](https://aisel.aisnet.org/misq/vol47/iss3/3/)<br>[解读与来源](../topics/validation-and-comparability.md#yang-2023-stable-lda) | 连接文本变量的重复性与后续实证结论，是评估主题测量稳定性的直接方法文献。 |
