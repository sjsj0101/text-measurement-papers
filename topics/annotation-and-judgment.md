<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->

# 文本标注与人工判断

[返回目录](../README.md) · [阅读路线](../docs/reading-routes.md)

比较教师标签、独立人工判断及分歧来源，区分复制教师和测量目标构念。

## 主目录（6 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2025 · MIS Quarterly · 期刊 | [Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning](https://aisel.aisnet.org/misq/vol49/iss3/12/)<br>[解读与来源](../topics/annotation-and-judgment.md#liu-2025-fastsr) | 为高专业知识、少量标签场景的文本变量提取提供专家参与和多任务设计案例。 |
| 2025 · MIS Quarterly · 期刊 | [Mitigating Bias in Hate Speech Detection with a Small Number of Expert Annotations: A Prompt-Based Learning Approach](https://aisel.aisnet.org/misq/vol49/iss4/14/)<br>[解读与来源](../topics/annotation-and-judgment.md#wei-2025-expert-hate-speech) | 说明标注者知识与群体语言背景会改变标签含义，适合讨论如何建立可靠测量参照。 |
| 2024 · ACL · 主会 | [VariErr NLI: Separating Annotation Error from Human Label Variation](https://aclanthology.org/2024.acl-long.123/)<br>[解读与来源](../topics/annotation-and-judgment.md#weber-genzel-2024-varierr) | 提供把低一致性拆成标注错误与有效观点差异的可操作程序，适用于构建更可靠的测量参照。 |
| 2022 · TACL · 期刊 | [Investigating Reasons for Disagreement in Natural Language Inference](https://aclanthology.org/2022.tacl-1.78/)<br>[解读与来源](../topics/annotation-and-judgment.md#jiang-2022-nli-disagreement) | 提醒文本测量先诊断不一致来源，再决定修订规则、清洗错误或保留多种判断。 |
| 2022 · EMNLP · 主会 | [The “Problem” of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation](https://aclanthology.org/2022.emnlp-main.731/)<br>[解读与来源](../topics/annotation-and-judgment.md#plank-2022-human-label-variation) | 为主观文本测量为何保留分歧、如何选择标签聚合与评价目标提供概念框架。 |
| 1991 · Journal of Consumer Research · 期刊 | [Content-Analysis Research: An Examination of Applications with Directives for Improving Research Reliability and Objectivity](https://academic.oup.com/jcr/article/18/2/243/1786851)<br>[解读与来源](../topics/annotation-and-judgment.md#kolbe-1991-content-analysis) | 为人工标注基准和编码流程的质量控制提供基础，提醒自动化测量也不能忽略参照标签的形成过程。 |


<a id="liu-2025-fastsr"></a>
### Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning

**2025 · MIS Quarterly · 期刊** · 期刊研究 · 主目录

**作者：** Rong Liu; Jingjing Li; Marko Zivkovic; Ahmed Abbasi

**研究内容：** FastSR 将医学系统综述专家的标注逻辑融入少样本框架，联合句子分类和序列标注，并在医学文章及临床试验摘要上评估。

**为什么读：** 为高专业知识、少量标签场景的文本变量提取提供专家参与和多任务设计案例。

**适用条件与限制：** 评估集中于医学系统综述任务，不能将自动提取表现视为医学结论有效或其他学科构念测量已验证。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aisel.aisnet.org/misq/vol49/iss3/12/)：已打开官方期刊存档/出版页面，核读题名、作者、期刊记录与摘要。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.25300/MISQ/2024/18573)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 文本标注与人工判断 · 合成数据与小模型适配 · 人机协作与使用条件

<a id="wei-2025-expert-hate-speech"></a>
### Mitigating Bias in Hate Speech Detection with a Small Number of Expert Annotations: A Prompt-Based Learning Approach

**2025 · MIS Quarterly · 期刊** · 期刊研究 · 主目录

**作者：** Dongjun Wei; Michael Chau; Zhepeng (Lionel) Li

**研究内容：** 针对通用标注者忽略语言群体差异造成的仇恨言论标签偏差，结合少量专家标注、对比学习与提示学习，在特定社群文本上评估偏差缓解。

**为什么读：** 说明标注者知识与群体语言背景会改变标签含义，适合讨论如何建立可靠测量参照。

**适用条件与限制：** 专家标签仍需说明其规范与适用社群；所考察英语变体及 LGBTQ+ 数据不能直接代表其他语言和群体。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aisel.aisnet.org/misq/vol49/iss4/14/)：已打开官方期刊存档/出版页面，核读题名、作者、期刊记录与摘要。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.25300/MISQ/2025/18416)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 文本标注与人工判断 · 合成数据与小模型适配 · 测量验证与可比性

<a id="weber-genzel-2024-varierr"></a>
### VariErr NLI: Separating Annotation Error from Human Label Variation

**2024 · ACL · 主会** · 会议论文 · 主目录

**作者：** Leon Weber-Genzel; Siyao Peng; Marie-Catherine de Marneffe; Barbara Plank

**研究内容：** 提出先为标签写解释、再判断标签与解释是否有效的两轮标注程序，构造区分错误和合理分歧的数据。作者在英文 NLI 上比较自动错误检测、GPT 和人工判断，展示自动检测仍有不足。

**为什么读：** 提供把低一致性拆成标注错误与有效观点差异的可操作程序，适用于构建更可靠的测量参照。

**适用条件与限制：** 核心验证对象是有限的英文 NLI 样本；解释有效性本身也需判断，不能把二轮裁决当作不受语境影响的绝对真值。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2024.acl-long.123/)：已读正式摘要；网页显示 De Marneffe，PDF 署名 de Marneffe，按 PDF。（2026-11-09）
- [metadata](https://aclanthology.org/2024.acl-long.123.pdf)：已对照 PDF 首页实际署名，优先于网页作者目录显示名。（2026-11-09）

**主题：** 文本标注与人工判断 · 测量验证与可比性

<a id="jiang-2022-nli-disagreement"></a>
### Investigating Reasons for Disagreement in Natural Language Inference

**2022 · TACL · 期刊** · 期刊研究 · 主目录

**作者：** Nan-Jiang Jiang; Marie-Catherine de Marneffe

**研究内容：** 建立自然语言推断标注分歧的来源分类，区分句意不确定、标注者偏差及任务设计因素，并比较增加复杂类别和允许多标签两种建模方式。作者发现标签分布可能对应不同类型的解释分歧。

**为什么读：** 提醒文本测量先诊断不一致来源，再决定修订规则、清洗错误或保留多种判断。

**适用条件与限制：** 框架基于自然语言推断，迁移到组织或消费者构念需要重新定义分歧类别；多标签覆盖更多解释也不直接解决下游统计推断。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2022.tacl-1.78/)：已访问官方页面，核对题名、作者、年份、发表身份与摘要。（2026-11-09）

**主题：** 文本标注与人工判断 · 构念定义与操作化

<a id="plank-2022-human-label-variation"></a>
### The “Problem” of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation

**2022 · EMNLP · 主会** · 观点／方法评论 · 主目录

**作者：** Barbara Plank

**研究内容：** 观点文章梳理人工标签差异在数据、建模和评价中的位置，主张区分噪声与多个合理答案。文章汇合保留未聚合标签的数据及相关方法，指出单一金标准假设可能遮蔽真实判断差异。

**为什么读：** 为主观文本测量为何保留分歧、如何选择标签聚合与评价目标提供概念框架。

**适用条件与限制：** 这是立场与研究综述式论证，并非所有差异都应保留的经验保证；实际项目仍要识别粗心标注、规则误解与合理差异。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2022.emnlp-main.731/)：已访问官方页面，核对题名、作者、年份、发表身份与摘要。（2026-11-09）

**主题：** 文本标注与人工判断 · 测量验证与可比性

<a id="kolbe-1991-content-analysis"></a>
### Content-Analysis Research: An Examination of Applications with Directives for Improving Research Reliability and Objectivity

**1991 · Journal of Consumer Research · 期刊** · 综述 · 主目录

**作者：** Richard H. Kolbe; Melissa S. Burnett

**研究内容：** 回顾内容分析研究的实施方法，评估客观性、可复现性与评判者间信度的报告，并讨论如何改进编码及信度计算。

**为什么读：** 为人工标注基准和编码流程的质量控制提供基础，提醒自动化测量也不能忽略参照标签的形成过程。

**适用条件与限制：** 面向人工内容分析的历史样本；信度并不等于构念效度，现代主观标签或多样化解释任务还需额外处理分歧。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://academic.oup.com/jcr/article/18/2/243/1786851)：已访问官方出版记录并核读摘要；未声称复现实验。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.1086/209256)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 文本标注与人工判断 · 测量验证与可比性

## 补充（2 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · GEM · Workshop | [Capturing Epistemic Uncertainty in LLM-Based Soft Labeling](https://aclanthology.org/2026.gem-main.21/)<br>[解读与来源](../topics/annotation-and-judgment.md#jiang-2026-soft-label-uncertainty) | 适合讨论有多个合理判断时如何保存标签不确定性，以及模型之间的差异能否近似人工标注分布。 |
| 2024 · NLP+CSS · Workshop | [Knowledge Distillation in Automated Annotation: Supervised Text Classification with LLM-Generated Training Labels](https://aclanthology.org/2024.nlpcss-1.9/)<br>[解读与来源](../topics/annotation-and-judgment.md#pangakis-2024-annotation-distillation) | 紧贴从自动标注到可规模化文本变量的流程，也能帮助区分教师标签质量和学生分类器表现。 |


<a id="jiang-2026-soft-label-uncertainty"></a>
### Capturing Epistemic Uncertainty in LLM-Based Soft Labeling

**2026 · GEM · Workshop** · 会议论文 · 补充

**作者：** Yanru Jiang; Siyu Liang

**研究内容：** 将 LLM 标注表示为分布而非多数标签，并比较随机解码、模型集合、角色提示和经人类示例校准等变异来源。作者在仇恨与情绪数据上考察对人类分歧的近似及其分类用途。

**为什么读：** 适合讨论有多个合理判断时如何保存标签不确定性，以及模型之间的差异能否近似人工标注分布。

**适用条件与限制：** 研究在特定仇恨与情绪数据上验证；模型变异不自动等于人群真实分歧，软标签训练效果也不能证明跨群体测量一致。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2026.gem-main.21/)：已核验 Proceedings of the Fifth Workshop on Generation, Evaluation and Metrics；标识中的 gem-main 不表示 ACL 主会。（2026-11-09）

**主题：** 文本标注与人工判断 · 测量验证与可比性

<a id="pangakis-2024-annotation-distillation"></a>
### Knowledge Distillation in Automated Annotation: Supervised Text Classification with LLM-Generated Training Labels

**2024 · NLP+CSS · Workshop** · 会议论文 · 补充

**作者：** Nicholas Pangakis; Samuel Wolken

**研究内容：** 将 LLM 产生的训练标签用于微调监督式分类器，并与人工标签训练及直接提示 LLM 比较。作者以计算社会科学的英文分类任务复核这种工作流，报告其在所研究任务上的可用性。

**为什么读：** 紧贴从自动标注到可规模化文本变量的流程，也能帮助区分教师标签质量和学生分类器表现。

**适用条件与限制：** 英文任务与特定模型的结果不保证迁移到其他语言或主观构念；受保护语料降低污染风险但不等于完全排除。模型与人工标签相近不代表没有共同测量偏误。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2024.nlpcss-1.9/)：已核验正式 NLP+CSS workshop，网页显示 Sam Wolken，PDF 实际署名 Samuel Wolken；依 PDF 保留完整名。（2026-11-09）
- [metadata](https://aclanthology.org/2024.nlpcss-1.9.pdf)：已对照 PDF 首页实际署名，优先于网页作者目录显示名。（2026-11-09）

**主题：** 文本标注与人工判断 · 合成数据与小模型适配

## 跨主题阅读

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · ACL · Industry | [Beyond Instruction Optimization: Multi-Agent Error-Driven Class Description Refinement for LLM-Based Classification](https://aclanthology.org/2026.acl-industry.137/)<br>[解读与来源](../topics/construct-operationalization.md#dev-2026-class-description-refinement) | 直接连接概念定义、标签规则和分类误差，适合讨论编码手册如何转为模型可执行的测量规则。 |
| 2025 · Management Science · 期刊 | [ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research](https://pubsonline.informs.org/doi/10.1287/mnsc.2023.03253)<br>[解读与来源](../topics/construct-operationalization.md#de-kok-2025-chatgpt-textual-analysis) | 将 LLM 的操作选择与测量目标和验证责任连接，是从模型能力走向实证变量的实用方法文献。 |
| 2025 · ACL Findings · Findings | [Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks](https://aclanthology.org/2025.findings-acl.1323/)<br>[解读与来源](../topics/human-ai-workflows.md#schroeder-2025-human-loop-annotation) | 直接说明人工复核未必形成独立的测量标准，适合设计盲审、独立金标准和避免评估循环的工作流。 |
| 2024 · EACL · 主会 | [The Parrot Dilemma: Human-Labeled vs. LLM-augmented Data in Classification Tasks](https://aclanthology.org/2024.eacl-short.17/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#moller-2024-parrot-dilemma) | 为研究者选择人工标注、合成补样或直接 LLM 编码提供任务层面的对照，而非仅看生成成本。 |
| 2023 · ACL Findings · Findings | [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://aclanthology.org/2023.findings-acl.507/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#hsieh-2023-distilling-step-by-step) | 为将研究者定义的判断任务压缩为可部署分类器提供训练方法，并提示保留判断理由可能有助于学习。 |
| 2023 · MIS Quarterly · 期刊 | [Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method](https://aisel.aisnet.org/misq/vol47/iss3/10/)<br>[解读与来源](../topics/construct-operationalization.md#zhao-2023-expert-industry-assignment) | 示范如何把显式类别定义、分类体系和专家标签同时纳入文本变量构建。 |
| 2023 · Management Science · 期刊 | [Reciprocal Human-Machine Learning: A Theory and an Instantiation for the Case of Message Classification](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03518)<br>[解读与来源](../topics/human-ai-workflows.md#teeni-2023-reciprocal-learning) | 将专家概念化、模型分类与反馈修订置于同一流程，可用于理解人工判断如何参与测量工具开发。 |
| 2023 · EMNLP · 主会 | [Synthetic Data Generation with Large Language Models for Text Classification: Potential and Limitations](https://aclanthology.org/2023.emnlp-main.647/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#li-2023-synthetic-data-limitations) | 帮助判断哪些文本变量适合用合成样本构建，以及哪些主观构念更需要独立人工参照。 |
| 2023 · NeurIPS · 主会 | [Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](https://papers.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract-Conference.html)<br>[解读与来源](../topics/measurement-error-and-inference.md#egami-2023-imperfect-surrogates) | 直接回答如何把 LLM 或其他分类器的代理标签用于统计推断，而不只评价标签预测准确率。 |
| 2022 · TACL · 期刊 | [Generate, Annotate, and Learn: NLP with Synthetic Text](https://aclanthology.org/2022.tacl-1.48/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#he-2022-generate-annotate-learn) | 帮助区分生成分布与标注规则两个误差来源，并为自动标注训练流程提供清晰的模块划分。 |
| 2020 · ACL · 主会 | [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/)<br>[解读与来源](../topics/validation-and-comparability.md#ribeiro-2020-checklist) | 把文本测量验证从单一准确率扩展到预先定义的能力、应保持不变的改写与应改变判断的情形。 |
| 2013 · Political Analysis · 期刊 | [Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts](https://www.cambridge.org/core/journals/political-analysis/article/text-as-data-the-promise-and-pitfalls-of-automatic-content-analysis-methods-for-political-texts/F7AAC8B2909441603FEB25C156448F20)<br>[解读与来源](../topics/validation-and-comparability.md#grimmer-2013-text-as-data) | 为整条文本测量链提供方法论起点：统计拟合良好不能单独确定变量的理论含义。 |
| 2026 · MultiPsyche · Workshop | [The Label-Translation Fallacy: A Four-Layer Validity Protocol for Multilingual Mental Health NLP](https://aclanthology.org/2026.multipsyche-1.5/)<br>[解读与来源](../topics/validation-and-comparability.md#zaghouani-2026-label-translation-fallacy) | 将跨语言文本分类的预测分数与构念等价、量表适配和标注证据分开，直接服务文本变量的跨情境验证。 |
| 2026 · Finance and Economics Discussion Series · 预印本 | [Validating Large Language Model Annotations](https://www.federalreserve.gov/econres/feds/files/2026020pap.pdf)<br>[解读与来源](../topics/validation-and-comparability.md#hansen-2026-validating-llm-annotations) | 提供一种探索性的无外部基准验证思路，可与独立人工基准及测量误差校正方法对照阅读。 |
| 2025 · arXiv · 预印本 | [GLiClass: Generalist Lightweight Model for Sequence Classification Tasks](https://arxiv.org/abs/2508.07662)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#stepanov-2025-gliclass) | 可作为动态标签和低成本批量文本编码的候选实现，连接轻量分类与反馈学习。 |
| 2007 · Information Systems Research · 期刊 | [Decision-Centric Active Learning of Binary-Outcome Models](https://pubsonline.informs.org/doi/10.1287/isre.1070.0111)<br>[解读与来源](../topics/human-ai-workflows.md#saar-tsechansky-2007-decision-centric) | 作为补充方法背景，提醒有限标注预算的分配应围绕实际研究或决策目标，而非只追求统一准确率。 |
