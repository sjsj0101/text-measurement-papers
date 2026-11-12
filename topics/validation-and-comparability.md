<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->

# 测量验证与可比性

[返回目录](../README.md) · [阅读路线](../docs/reading-routes.md)

用独立真实文本、边界案例和跨情境评价检查效度、漂移与可比性。

## 主目录（9 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2023 · MIS Quarterly · 期刊 | [Extracting Actionable Insights from Text Data: A Stable Topic Model Approach](https://aisel.aisnet.org/misq/vol47/iss3/3/)<br>[解读与来源](../topics/validation-and-comparability.md#yang-2023-stable-lda) | 连接文本变量的重复性与后续实证结论，是评估主题测量稳定性的直接方法文献。 |
| 2023 · Journal of Consumer Psychology · 期刊 | [PassivePy: A tool to automatically identify passive voice in big text data](https://doi.org/10.1002/jcpy.1377)<br>[解读与来源](../topics/validation-and-comparability.md#sepehri-2023-passivepy) | 提供从明确语言特征、可复用工具到独立人工验证的实例，帮助区分可观测语言现象与更抽象的研究构念。 |
| 2022 · NAACL · 主会 | [Time Waits for No One! Analysis and Challenges of Temporal Misalignment](https://aclanthology.org/2022.naacl-main.435/)<br>[解读与来源](../topics/validation-and-comparability.md#luu-2022-temporal-misalignment) | 支持文本测量按时间外推单独验证，并把模型更新与跨期可比性问题纳入设计。 |
| 2021 · EMNLP Findings · Findings | [Temporal Adaptation of BERT and Performance on Downstream Document Classification: Insights from Social Media](https://aclanthology.org/2021.findings-emnlp.206/)<br>[解读与来源](../topics/validation-and-comparability.md#rottger-2021-temporal-adaptation) | 为纵向文本测量提供直接提醒：识别语言变化与维持分类可比性不是同一问题，应使用时间划分的任务验证。 |
| 2020 · ACL · 主会 | [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/)<br>[解读与来源](../topics/validation-and-comparability.md#ribeiro-2020-checklist) | 把文本测量验证从单一准确率扩展到预先定义的能力、应保持不变的改写与应改变判断的情形。 |
| 2020 · EMNLP Findings · Findings | [Evaluating Models’ Local Decision Boundaries via Contrast Sets](https://aclanthology.org/2020.findings-emnlp.117/)<br>[解读与来源](../topics/validation-and-comparability.md#gardner-2020-contrast-sets) | 适合把构念边界转为成对测试：只有目标含义变化时，测量结果是否按预期改变。 |
| 2013 · Political Analysis · 期刊 | [Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts](https://www.cambridge.org/core/journals/political-analysis/article/text-as-data-the-promise-and-pitfalls-of-automatic-content-analysis-methods-for-political-texts/F7AAC8B2909441603FEB25C156448F20)<br>[解读与来源](../topics/validation-and-comparability.md#grimmer-2013-text-as-data) | 为整条文本测量链提供方法论起点：统计拟合良好不能单独确定变量的理论含义。 |
| 2001 · MIS Quarterly · 期刊 | [Validation in Information Systems Research: A State-of-the-Art Assessment](https://aisel.aisnet.org/misq/vol25/iss1/1/)<br>[解读与来源](../topics/validation-and-comparability.md#boudreau-2001-validation-is) | 提供评估测量论证是否完整的基础框架，可用于审查文本变量是否只有预测成绩而缺乏构念证据。 |
| 2000 · Organizational Research Methods · 期刊 | [A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research](https://journals.sagepub.com/doi/10.1177/109442810031002)<br>[解读与来源](../topics/validation-and-comparability.md#vandenberg-2000-measurement-invariance) | 为比较不同群体、时期或语言中的文本分数提供测量可比性基础，避免把测量机制差异误解为构念差异。 |


<a id="yang-2023-stable-lda"></a>
### Extracting Actionable Insights from Text Data: A Stable Topic Model Approach

**2023 · MIS Quarterly · 期刊** · 期刊研究 · 主目录

**作者：** Yi Yang; Ramanath Subramanyam

**研究内容：** 将主题词簇加入 LDA，研究同一语料重复拟合时主题与下游计量变量的不稳定问题。作者在多组文本及两个应用中报告了更稳定的主题和回归估计。

**为什么读：** 连接文本变量的重复性与后续实证结论，是评估主题测量稳定性的直接方法文献。

**适用条件与限制：** 稳定性不等于构念效度；结果限于所评估语料、主题结构与计量应用，本轮仅核读摘要。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aisel.aisnet.org/misq/vol47/iss3/3/)：已打开官方期刊存档/出版页面，核读题名、作者、期刊记录与摘要。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.25300/MISQ/2022/16957)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 测量验证与可比性 · 测量误差与下游推断

<a id="sepehri-2023-passivepy"></a>
### PassivePy: A tool to automatically identify passive voice in big text data

**2023 · Journal of Consumer Psychology · 期刊** · 期刊研究 · 主目录

**作者：** Amir Sepehri; Mitra Sadat Mirshafiee; David M. Markowitz

**研究内容：** 将英语被动语态识别实现为可重复使用的文本分析工具，用人工编码比较验证，并在消费者文本情境中展示应用。

**为什么读：** 提供从明确语言特征、可复用工具到独立人工验证的实例，帮助区分可观测语言现象与更抽象的研究构念。

**适用条件与限制：** 识别被动语态的准确性不证明对心理状态的测量有效；语言和句法边界限制了向其他文本类型的直接推广。

**本轮证据：** 部分正文；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://myscp.onlinelibrary.wiley.com/doi/10.1002/jcpy.1377)：正式Wiley页核验作者、摘要、卷期及2023-07-12首次在线时间；本轮阅读库内引言。（2026-11-09）

**年份与版本说明：** 首次在线：2023-07-12

**主题：** 测量验证与可比性

<a id="luu-2022-temporal-misalignment"></a>
### Time Waits for No One! Analysis and Challenges of Temporal Misalignment

**2022 · NAACL · 主会** · 会议论文 · 主目录

**作者：** Kelvin Luu; Daniel Khashabi; Suchin Gururangan; Karishma Mandyam; Noah A. Smith

**研究内容：** 构建跨多个领域和时间跨度的任务组，研究训练与部署时期不匹配造成的性能退化。作者比较继续预训练和目标时期任务微调，指出后者在所研究设置中更能缓解时间错位。

**为什么读：** 支持文本测量按时间外推单独验证，并把模型更新与跨期可比性问题纳入设计。

**适用条件与限制：** 任务性能退化衡量的是预测迁移；不能直接断言某个社会科学构念发生变化，也不能以重训后的高分证明纵向指标保持同一尺度。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2022.naacl-main.435/)：已访问官方页面，核对题名、作者、年份、发表身份与摘要。（2026-11-09）

**主题：** 测量验证与可比性 · 合成数据与小模型适配

<a id="rottger-2021-temporal-adaptation"></a>
### Temporal Adaptation of BERT and Performance on Downstream Document Classification: Insights from Social Media

**2021 · EMNLP Findings · Findings** · 会议论文 · 主目录

**作者：** Paul Röttger; Janet B. Pierrehumbert

**研究内容：** 利用跨年的社交媒体评论区分继续预训练中的时间适配与下游有标签微调。作者发现时间因素影响表现，但语言模型层面的时间适配收益未必转化为文档分类收益。

**为什么读：** 为纵向文本测量提供直接提醒：识别语言变化与维持分类可比性不是同一问题，应使用时间划分的任务验证。

**适用条件与限制：** 证据来自特定社交媒体任务与 BERT；预测稳定性不等于潜在构念的测量不变性，更新模型前后仍应检查标尺变化。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2021.findings-emnlp.206/)：网页显示 Janet Pierrehumbert，PDF 署名含 B.；按 PDF。（2026-11-09）
- [metadata](https://aclanthology.org/2021.findings-emnlp.206.pdf)：已对照 PDF 首页实际署名，优先于网页作者目录显示名。（2026-11-09）

**主题：** 测量验证与可比性 · 合成数据与小模型适配

<a id="ribeiro-2020-checklist"></a>
### Beyond Accuracy: Behavioral Testing of NLP Models with CheckList

**2020 · ACL · 主会** · 会议论文 · 主目录

**作者：** Marco Tulio Ribeiro; Tongshuang Wu; Carlos Guestrin; Sameer Singh

**研究内容：** CheckList 将语言能力与测试类型组成测试矩阵，帮助系统化设计模型行为测试。作者用多个任务和用户研究展示，在总体测试成绩较好时仍能找到具体语言行为上的缺陷。

**为什么读：** 把文本测量验证从单一准确率扩展到预先定义的能力、应保持不变的改写与应改变判断的情形。

**适用条件与限制：** 行为测试覆盖取决于设计者选择的能力和用例；通过测试不等于覆盖真实总体，也不能直接给出变量误差对统计估计的影响。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2020.acl-main.442/)：已访问正式页面并读取摘要，核验题名、作者、年份及 track。（2026-11-09）

**主题：** 测量验证与可比性 · 文本标注与人工判断

<a id="gardner-2020-contrast-sets"></a>
### Evaluating Models’ Local Decision Boundaries via Contrast Sets

**2020 · EMNLP Findings · Findings** · 会议论文 · 主目录

**作者：** Matt Gardner; Yoav Artzi; Victoria Basmov; Jonathan Berant; Ben Bogin; Sihao Chen; Pradeep Dasigi; Dheeru Dua; Yanai Elazar; Ananth Gottumukkala; Nitish Gupta; Hannaneh Hajishirzi; Gabriel Ilharco; Daniel Khashabi; Kevin Lin; Jiangming Liu; Nelson F. Liu; Phoebe Mulcaire; Qiang Ning; Sameer Singh; Noah A. Smith; Sanjay Subramanian; Reut Tsarfaty; Eric Wallace; Ally Zhang; Ben Zhou

**研究内容：** 通过人工对测试文本作小而有意义的修改，通常改变正确标签，构建对照样本组。作者借此检查模型局部决策边界，揭示常规同分布测试可能掩盖的数据捷径和能力缺口。

**为什么读：** 适合把构念边界转为成对测试：只有目标含义变化时，测量结果是否按预期改变。

**适用条件与限制：** 局部人工修改无法穷尽真实分布，预期标签仍依赖标注规则；对照集能诊断边界，却不能独自建立内容效度或跨群体不变性。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2020.findings-emnlp.117/)：已访问正式页面并读取摘要，核验题名、作者、年份及 track。（2026-11-09）

**主题：** 测量验证与可比性 · 构念定义与操作化

<a id="grimmer-2013-text-as-data"></a>
### Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts

**2013 · Political Analysis · 期刊** · 综述 · 主目录

**作者：** Justin Grimmer; Brandon M. Stewart

**研究内容：** 梳理政治文本的分类与尺度测量方法，强调研究目标、近距离阅读与针对具体问题的验证，解释无监督主题或潜在尺度为何需要实质性证据。

**为什么读：** 为整条文本测量链提供方法论起点：统计拟合良好不能单独确定变量的理论含义。

**适用条件与限制：** 综述以当时的文档层面方法为主；不能直接代表现代 LLM 的性能，所用验证原则仍需按任务与模型重新实施。

**本轮证据：** 部分正文；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://www.cambridge.org/core/journals/political-analysis/article/text-as-data-the-promise-and-pitfalls-of-automatic-content-analysis-methods-for-political-texts/F7AAC8B2909441603FEB25C156448F20)：已访问官方出版记录并核读摘要；未声称复现实验。（2026-11-09）
- [content](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F7AAC8B2909441603FEB25C156448F20/S1047198700013401a.pdf)：核读 PDF 首页、引言和验证原则部分；首页 Advance Access 2013-01-22，纠正当前 Cambridge 页面/Crossref 的 2017 平台日期。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.1093/pan/mps028)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 测量验证与可比性 · 构念定义与操作化 · 文本标注与人工判断

<a id="boudreau-2001-validation-is"></a>
### Validation in Information Systems Research: A State-of-the-Art Assessment

**2001 · MIS Quarterly · 期刊** · 综述 · 主目录

**作者：** Marie-Claude Boudreau; David Gefen; Detmar W. Straub

**研究内容：** 对信息系统定量研究中的工具验证做回顾性编码，考察内容与构念效度、信度和操纵效度的实践，指出验证不足并提出改进方向。

**为什么读：** 提供评估测量论证是否完整的基础框架，可用于审查文本变量是否只有预测成绩而缺乏构念证据。

**适用条件与限制：** 样本来自历史时期与指定期刊的一般定量研究，不能据此推断当前文本研究的验证普及率。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aisel.aisnet.org/misq/vol25/iss1/1/)：已访问官方出版记录并核读摘要；未声称复现实验。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.2307/3250956)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 测量验证与可比性 · 构念定义与操作化

<a id="vandenberg-2000-measurement-invariance"></a>
### A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research

**2000 · Organizational Research Methods · 期刊** · 综述 · 主目录

**作者：** Robert J. Vandenberg; Charles E. Lance

**研究内容：** 综述跨群体与纵向测量不变性的检验实践，讨论其对均值和结构关系比较的意义，并提出组织研究的检验次序。

**为什么读：** 为比较不同群体、时期或语言中的文本分数提供测量可比性基础，避免把测量机制差异误解为构念差异。

**适用条件与限制：** 主要方法背景是传统测量模型，不能直接搬成文本模型的通用合格阈值；需先明确指标结构和比较目标。官方直连受限，本轮核读完整官方摘要缓存。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://journals.sagepub.com/doi/10.1177/109442810031002)：检索工具返回该官方出版记录的完整题名、作者、发表身份及摘要缓存；页面直连失败（超时/403/重定向受限），没有获取出版全文。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.1177/109442810031002)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 测量验证与可比性 · 构念定义与操作化

## 补充（2 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · MultiPsyche · Workshop | [The Label-Translation Fallacy: A Four-Layer Validity Protocol for Multilingual Mental Health NLP](https://aclanthology.org/2026.multipsyche-1.5/)<br>[解读与来源](../topics/validation-and-comparability.md#zaghouani-2026-label-translation-fallacy) | 将跨语言文本分类的预测分数与构念等价、量表适配和标注证据分开，直接服务文本变量的跨情境验证。 |
| 2026 · Finance and Economics Discussion Series · 预印本 | [Validating Large Language Model Annotations](https://www.federalreserve.gov/econres/feds/files/2026020pap.pdf)<br>[解读与来源](../topics/validation-and-comparability.md#hansen-2026-validating-llm-annotations) | 提供一种探索性的无外部基准验证思路，可与独立人工基准及测量误差校正方法对照阅读。 |


<a id="zaghouani-2026-label-translation-fallacy"></a>
### The Label-Translation Fallacy: A Four-Layer Validity Protocol for Multilingual Mental Health NLP

**2026 · MultiPsyche · Workshop** · 会议论文 · 补充

**作者：** Wajdi Zaghouani

**研究内容：** 提出分层检查构念、测量工具、标注情境及可支持结论的报告协议，用于避免把翻译后的心理健康标签直接当作跨语言有效测量。

**为什么读：** 将跨语言文本分类的预测分数与构念等价、量表适配和标注证据分开，直接服务文本变量的跨情境验证。

**适用条件与限制：** 属于整合既有测量工具的协议与案例说明，不是新模型的实验性能验证，也不保证检查表能替代专业测量与临床判断；本轮仅阅读官方摘要。

**本轮证据：** 摘要；核验日期 2026-11-10。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2026.multipsyche-1.5/)：ACL Anthology官方页确认作者、2026年11月MultiPsyche第1届Workshop、页44–54；明确Workshop，不提升为主会。（2026-11-10）
- [content](https://aclanthology.org/2026.multipsyche-1.5/)：短评依据官方摘要，区分协议整合与实验验证；未通读PDF。（2026-11-10）

**主题：** 测量验证与可比性 · 构念定义与操作化 · 文本标注与人工判断

<a id="hansen-2026-validating-llm-annotations"></a>
### Validating Large Language Model Annotations

**2026 · Finance and Economics Discussion Series · 预印本** · 预印本／工作论文 · 补充

**作者：** Anne Lundgaard Hansen

**研究内容：** 在缺少可靠外部标签时，通过由标签生成文本并比较语义，以及回译和类别分离前提检验，评估特定 LLM 与提示组合的测量表现。

**为什么读：** 提供一种探索性的无外部基准验证思路，可与独立人工基准及测量误差校正方法对照阅读。

**适用条件与限制：** 工作论文，纳入补充。该框架依赖模拟提示、生成能力与语义嵌入；生成受限或提示不足可能造成误拒，内部一致性不能被泛化为所有构念均已独立验证。

**本轮证据：** 部分正文；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://www.federalreserve.gov/econres/feds/files/2026020pap.pdf)：已打开官方 FEDS PDF，核读封面、摘要、引言及第 6 节局限；封面明示为 preliminary staff working paper。（2026-11-09）

**主题：** 测量验证与可比性 · 文本标注与人工判断

## 跨主题阅读

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · MIS Quarterly · 期刊 | [AI-Augmented Content Validation in Behavioral Research: Development and Evaluation of the RATER System](https://aisel.aisnet.org/misq/vol50/iss1/7/)<br>[解读与来源](../topics/construct-operationalization.md#pillet-2026-rater) | 直接对应构念定义与语言表述之间的内容效度检验，可为文本测量的操作化设计提供参照。 |
| 2026 · EACL Findings · Findings | [Better as Generators Than Classifiers: Leveraging LLMs and Synthetic Data for Low-Resource Multilingual Classification](https://aclanthology.org/2026.findings-eacl.148/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#pecher-2026-generators-classifiers) | 连接低资源语言的文本变量构造与小模型部署，也为跨语言测量流程选择提供方法证据。 |
| 2026 · Behavior Research Methods · 期刊 | [Measuring complex constructs in large-scale text with computational social mixed methods](https://link.springer.com/article/10.3758/s13428-026-03046-5)<br>[解读与来源](../topics/construct-operationalization.md#herderich-2026-complex-constructs) | 直接回答如何从研究构念和编码规则构造文本变量，并让变量误差进入后续分析，而不只优化分类分数。 |
| 2025 · Management Science · 期刊 | [ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research](https://pubsonline.informs.org/doi/10.1287/mnsc.2023.03253)<br>[解读与来源](../topics/construct-operationalization.md#de-kok-2025-chatgpt-textual-analysis) | 将 LLM 的操作选择与测量目标和验证责任连接，是从模型能力走向实证变量的实用方法文献。 |
| 2025 · MIS Quarterly · 期刊 | [Correcting Measurement Error in Regression Models with Variables Constructed from Aggregated Output of Data Mining Models](https://aisel.aisnet.org/misq/vol49/iss1/6/)<br>[解读与来源](../topics/measurement-error-and-inference.md#qiao-2025-aggregated-measurement-error) | 覆盖评论情感等个体预测聚合为产品或组织变量后的测量误差，补充逐条标签校正。 |
| 2025 · ACL Findings · Findings | [Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks](https://aclanthology.org/2025.findings-acl.1323/)<br>[解读与来源](../topics/human-ai-workflows.md#schroeder-2025-human-loop-annotation) | 直接说明人工复核未必形成独立的测量标准，适合设计盲审、独立金标准和避免评估循环的工作流。 |
| 2025 · MIS Quarterly · 期刊 | [Mitigating Bias in Hate Speech Detection with a Small Number of Expert Annotations: A Prompt-Based Learning Approach](https://aisel.aisnet.org/misq/vol49/iss4/14/)<br>[解读与来源](../topics/annotation-and-judgment.md#wei-2025-expert-hate-speech) | 说明标注者知识与群体语言背景会改变标签含义，适合讨论如何建立可靠测量参照。 |
| 2024 · ACL Findings · Findings | [Don’t Augment, Rewrite? Assessing Abusive Language Detection with Synthetic Data](https://aclanthology.org/2024.findings-acl.669/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#casula-2024-rewrite-abusive-language) | 展示保留任务含义同时改变文本表面的数据改造策略，可用于讨论共享困难下的分类器训练和外部验证。 |
| 2024 · ACL · 主会 | [VariErr NLI: Separating Annotation Error from Human Label Variation](https://aclanthology.org/2024.acl-long.123/)<br>[解读与来源](../topics/annotation-and-judgment.md#weber-genzel-2024-varierr) | 提供把低一致性拆成标注错误与有效观点差异的可操作程序，适用于构建更可靠的测量参照。 |
| 2023 · EMNLP · 主会 | [TrueTeacher: Learning Factual Consistency Evaluation with Large Language Models](https://aclanthology.org/2023.emnlp-main.127/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#gekhman-2023-trueteacher) | 提供将昂贵的语言判断蒸馏为专用测量模型的实例，强调训练错误类型应接近实际待测文本。 |
| 2023 · NeurIPS · 主会 | [Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](https://papers.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract-Conference.html)<br>[解读与来源](../topics/measurement-error-and-inference.md#egami-2023-imperfect-surrogates) | 直接回答如何把 LLM 或其他分类器的代理标签用于统计推断，而不只评价标签预测准确率。 |
| 2022 · Journal of Marketing Research · 期刊 | [Beyond Sentiment: The Value and Measurement of Consumer Certainty in Language](https://journals.sagepub.com/doi/abs/10.1177/00222437221134802)<br>[解读与来源](../topics/construct-operationalization.md#rocklage-2022-certainty-lexicon) | 展示同一文本中需要区分态度方向与态度确定性等不同构念，并将工具开发与多种验证情境相结合。 |
| 2022 · Information Systems Research · 期刊 | [Getting Personal: A Deep Learning Artifact for Text-Based Measurement of Personality](https://pubsonline.informs.org/doi/10.1287/isre.2022.1111)<br>[解读与来源](../topics/construct-operationalization.md#yang-2022-deepperson) | 直接连接心理构念、文本测量和下游应用，同时展示伪标签与领域适配在测量模型中的作用。 |
| 2022 · EMNLP · 主会 | [The “Problem” of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation](https://aclanthology.org/2022.emnlp-main.731/)<br>[解读与来源](../topics/annotation-and-judgment.md#plank-2022-human-label-variation) | 为主观文本测量为何保留分歧、如何选择标签聚合与评价目标提供概念框架。 |
| 2021 · Information Systems Research · 期刊 | [Correcting Misclassification Bias in Regression Models with Variables Generated via Data Mining](https://pubsonline.informs.org/doi/10.1287/isre.2020.0977)<br>[解读与来源](../topics/measurement-error-and-inference.md#qiao-2021-misclassification-bias) | 直接处理从文本分类标签到回归推断的误差传播，区分预测指标与目标参数精度。 |
| 2020 · Marketing Science · 期刊 | [Improving Text Analysis Using Sentence Conjunctions and Punctuation](https://pubsonline.informs.org/doi/10.1287/mksc.2019.1214)<br>[解读与来源](../topics/construct-operationalization.md#buschken-2020-sentence-conjunctions) | 说明文本表示和预处理会改变可得到的测量信息，并为消费者评价主题测量提供结构化方法。 |
| 2019 · MIS Quarterly · 期刊 | [Operationalizing Regulatory Focus in the Digital Age: Evidence from an E-Commerce Context](https://aisel.aisnet.org/misq/vol43/iss3/5/)<br>[解读与来源](../topics/construct-operationalization.md#wu-2019-regulatory-focus) | 提供理论构念、文本指标、独立问卷验证与下游分析相衔接的实证案例。 |
| 2019 · Journal of Consumer Psychology · 期刊 | [The Importance of Construct Validity in Consumer Research](https://myscp.onlinelibrary.wiley.com/doi/10.1002/jcpy.1145)<br>[解读与来源](../topics/construct-operationalization.md#mochon-2019-construct-validity) | 为文本变量命名和解释提供概念警示：标签与理论术语相同，不代表测量对象一致。 |
| 2019 · Journal of Marketing · 期刊 | [Uniting the Tribes: Using Text for Marketing Insight](https://journals.sagepub.com/doi/abs/10.1177/0022242919873106)<br>[解读与来源](../topics/construct-operationalization.md#berger-2019-uniting-tribes) | 适合作为研究地图导读，把文本信号的来源、解释目标、测量方法和验证要求放在同一框架中。 |
| 2018 · Information Systems Research · 期刊 | [Mind the Gap: Accounting for Measurement Error and Misclassification in Variables Generated via Data Mining](https://pubsonline.informs.org/doi/10.1287/isre.2017.0727)<br>[解读与来源](../topics/measurement-error-and-inference.md#yang-2018-mind-the-gap) | 为把文本预测分数当作观测变量的实证研究提供误差诊断和校正入口。 |
| 2017 · Journal of Consumer Research · 期刊 | [Automated Text Analysis for Consumer Research](https://academic.oup.com/jcr/article/44/6/1274/4283031)<br>[解读与来源](../topics/construct-operationalization.md#humphreys-2017-automated-text-analysis) | 为由研究问题和构念定义出发选择文本方法提供导读，并提示自然文本的生态效度与适用边界。 |
| 2011 · MIS Quarterly · 期刊 | [Measurement and Meaning in Information Systems and Organizational Research: Methodological and Philosophical Foundations](https://aisel.aisnet.org/misq/vol35/iss2/4/)<br>[解读与来源](../topics/construct-operationalization.md#bagozzi-2011-measurement-meaning) | 作为测量基础，帮助先界定构念及指标关系，再决定文本特征是否能支持所声称的变量含义。 |
| 1991 · Journal of Consumer Research · 期刊 | [Content-Analysis Research: An Examination of Applications with Directives for Improving Research Reliability and Objectivity](https://academic.oup.com/jcr/article/18/2/243/1786851)<br>[解读与来源](../topics/annotation-and-judgment.md#kolbe-1991-content-analysis) | 为人工标注基准和编码流程的质量控制提供基础，提醒自动化测量也不能忽略参照标签的形成过程。 |
| 2026 · GEM · Workshop | [Capturing Epistemic Uncertainty in LLM-Based Soft Labeling](https://aclanthology.org/2026.gem-main.21/)<br>[解读与来源](../topics/annotation-and-judgment.md#jiang-2026-soft-label-uncertainty) | 适合讨论有多个合理判断时如何保存标签不确定性，以及模型之间的差异能否近似人工标注分布。 |
| 2026 · arXiv · 预印本 | [Data Annotation as Measurement](https://arxiv.org/abs/2608.07297)<br>[解读与来源](../topics/annotation-and-judgment.md#harvey-2026-annotation-measurement) | 为研究者把构念和编码规则转成文本标签提供过程诊断框架，避免把一致率高直接当成测量正确。 |
