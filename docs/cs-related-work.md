<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->

# CS Related Work

[返回目录](../README.md) · [阅读路线](reading-routes.md)

按标注、适配、验证组织计算机科学方法，直接比较其在研究测量中的作用。正式会议、Findings、Industry、Demo、Workshop 和预印本逐条标注；本页不新增或重复计数。

## 构念定义与操作化

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · ACL · Industry | [Beyond Instruction Optimization: Multi-Agent Error-Driven Class Description Refinement for LLM-Based Classification](https://aclanthology.org/2026.acl-industry.137/)<br>[解读与来源](../topics/construct-operationalization.md#dev-2026-class-description-refinement) | 直接连接概念定义、标签规则和分类误差，适合讨论编码手册如何转为模型可执行的测量规则。 |


## 文本标注与人工判断

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2024 · ACL · 主会 | [VariErr NLI: Separating Annotation Error from Human Label Variation](https://aclanthology.org/2024.acl-long.123/)<br>[解读与来源](../topics/annotation-and-judgment.md#weber-genzel-2024-varierr) | 提供把低一致性拆成标注错误与有效观点差异的可操作程序，适用于构建更可靠的测量参照。 |
| 2022 · TACL · 期刊 | [Investigating Reasons for Disagreement in Natural Language Inference](https://aclanthology.org/2022.tacl-1.78/)<br>[解读与来源](../topics/annotation-and-judgment.md#jiang-2022-nli-disagreement) | 提醒文本测量先诊断不一致来源，再决定修订规则、清洗错误或保留多种判断。 |
| 2022 · EMNLP · 主会 | [The “Problem” of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation](https://aclanthology.org/2022.emnlp-main.731/)<br>[解读与来源](../topics/annotation-and-judgment.md#plank-2022-human-label-variation) | 为主观文本测量为何保留分歧、如何选择标签聚合与评价目标提供概念框架。 |
| 2026 · GEM · Workshop | [Capturing Epistemic Uncertainty in LLM-Based Soft Labeling](https://aclanthology.org/2026.gem-main.21/)<br>[解读与来源](../topics/annotation-and-judgment.md#jiang-2026-soft-label-uncertainty) | 适合讨论有多个合理判断时如何保存标签不确定性，以及模型之间的差异能否近似人工标注分布。 |
| 2024 · NLP+CSS · Workshop | [Knowledge Distillation in Automated Annotation: Supervised Text Classification with LLM-Generated Training Labels](https://aclanthology.org/2024.nlpcss-1.9/)<br>[解读与来源](../topics/annotation-and-judgment.md#pangakis-2024-annotation-distillation) | 紧贴从自动标注到可规模化文本变量的流程，也能帮助区分教师标签质量和学生分类器表现。 |


## 合成数据与小模型适配

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · EACL Findings · Findings | [Better as Generators Than Classifiers: Leveraging LLMs and Synthetic Data for Low-Resource Multilingual Classification](https://aclanthology.org/2026.findings-eacl.148/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#pecher-2026-generators-classifiers) | 连接低资源语言的文本变量构造与小模型部署，也为跨语言测量流程选择提供方法证据。 |
| 2026 · Information Systems Research · 期刊 | [Reference Aware Delexicalization (RAD) Framework: Theory Driven Artificial Intelligence Modeling for Domain Generalization](https://doi.org/10.1287/isre.2023.0457)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#suntwal-2026-rad) | 为理论知识如何进入训练数据设计提供直接方法近邻，可用于比较语义约束增强与单纯扩充数据的差别。 |
| 2024 · ACL Findings · Findings | [Better Synthetic Data by Retrieving and Transforming Existing Datasets](https://aclanthology.org/2024.findings-acl.385/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#gandhi-2024-datatune) | 为避免从空白提示生成单调样本提供替代路径，也适合讨论既有语料如何转化为新编码任务的训练材料。 |
| 2024 · ACL Findings · Findings | [Don’t Augment, Rewrite? Assessing Abusive Language Detection with Synthetic Data](https://aclanthology.org/2024.findings-acl.669/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#casula-2024-rewrite-abusive-language) | 展示保留任务含义同时改变文本表面的数据改造策略，可用于讨论共享困难下的分类器训练和外部验证。 |
| 2024 · NAACL Findings · Findings | [GOLD: Generalized Knowledge Distillation via Out-of-Distribution-Guided Language Data Generation](https://aclanthology.org/2024.findings-naacl.272/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#gholami-2024-gold) | 为稀有或边界文本类别的合成采样提供机制，可用于检验生成数据是否只覆盖容易样本。 |
| 2024 · EACL · 主会 | [The Parrot Dilemma: Human-Labeled vs. LLM-augmented Data in Classification Tasks](https://aclanthology.org/2024.eacl-short.17/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#moller-2024-parrot-dilemma) | 为研究者选择人工标注、合成补样或直接 LLM 编码提供任务层面的对照，而非仅看生成成本。 |
| 2023 · ACL Findings · Findings | [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://aclanthology.org/2023.findings-acl.507/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#hsieh-2023-distilling-step-by-step) | 为将研究者定义的判断任务压缩为可部署分类器提供训练方法，并提示保留判断理由可能有助于学习。 |
| 2023 · EMNLP System Demonstrations · System Demonstrations | [Prompt2Model: Generating Deployable Models from Natural Language Instructions](https://aclanthology.org/2023.emnlp-demo.38/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#viswanathan-2023-prompt2model) | 可作为把编码规则实现为小模型的系统入口，也便于讨论生成训练集和验证集的职责。 |
| 2023 · EMNLP · 主会 | [Synthetic Data Generation with Large Language Models for Text Classification: Potential and Limitations](https://aclanthology.org/2023.emnlp-main.647/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#li-2023-synthetic-data-limitations) | 帮助判断哪些文本变量适合用合成样本构建，以及哪些主观构念更需要独立人工参照。 |
| 2023 · EMNLP · 主会 | [TrueTeacher: Learning Factual Consistency Evaluation with Large Language Models](https://aclanthology.org/2023.emnlp-main.127/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#gekhman-2023-trueteacher) | 提供将昂贵的语言判断蒸馏为专用测量模型的实例，强调训练错误类型应接近实际待测文本。 |
| 2022 · TACL · 期刊 | [Generate, Annotate, and Learn: NLP with Synthetic Text](https://aclanthology.org/2022.tacl-1.48/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#he-2022-generate-annotate-learn) | 帮助区分生成分布与标注规则两个误差来源，并为自动标注训练流程提供清晰的模块划分。 |
| 2022 · EMNLP Findings · Findings | [ProGen: Progressive Zero-shot Dataset Generation via In-context Feedback](https://aclanthology.org/2022.findings-emnlp.269/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#ye-2022-progen) | 直接提供按学生模型反馈改进合成分类语料的早期方法入口，适合与随机扩充和主动标注比较。 |
| 2022 · EMNLP · 主会 | [ZeroGen: Efficient Zero-shot Learning via Dataset Generation](https://aclanthology.org/2022.emnlp-main.801/)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#ye-2022-zerogen) | 提供从零样本任务定义到小分类器的基本路径，是后续反馈式生成和数据改造研究的比较基线。 |
| 2026 · COLM · 主会 · 官方已接收 | [Towards Active Synthetic Data Generation for Finetuning Language Models](https://colm.eventhosts.cc/Conferences/2026/AcceptedPapers)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#kessler-2025-active-synthetic-data) | 为按分类器薄弱点组织合成数据提供邻近方法背景；实验并非社会科学文本构念测量，因此列入补充。 |
| 2025 · arXiv · 预印本 | [GLiClass: Generalist Lightweight Model for Sequence Classification Tasks](https://arxiv.org/abs/2508.07662)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#stepanov-2025-gliclass) | 可作为动态标签和低成本批量文本编码的候选实现，连接轻量分类与反馈学习。 |
| 2024 · arXiv · 预印本 | [Data Generation Using Large Language Models for Text Classification: An Empirical Case Study](https://arxiv.org/abs/2407.12813)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#li-2024-data-generation-case-study) | 为合成文本变量训练样本时的生成设置与诊断提供经验参照，避免仅以生成量评价数据质量。 |
| 2022 · arXiv · 预印本 | [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#tunstall-2022-setfit) | 作为有少量人工标注时的轻量分类基线，可与直接调用 LLM 或使用合成数据的方案比较。 |


## 测量验证与可比性

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2022 · NAACL · 主会 | [Time Waits for No One! Analysis and Challenges of Temporal Misalignment](https://aclanthology.org/2022.naacl-main.435/)<br>[解读与来源](../topics/validation-and-comparability.md#luu-2022-temporal-misalignment) | 支持文本测量按时间外推单独验证，并把模型更新与跨期可比性问题纳入设计。 |
| 2021 · EMNLP Findings · Findings | [Temporal Adaptation of BERT and Performance on Downstream Document Classification: Insights from Social Media](https://aclanthology.org/2021.findings-emnlp.206/)<br>[解读与来源](../topics/validation-and-comparability.md#rottger-2021-temporal-adaptation) | 为纵向文本测量提供直接提醒：识别语言变化与维持分类可比性不是同一问题，应使用时间划分的任务验证。 |
| 2020 · ACL · 主会 | [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/)<br>[解读与来源](../topics/validation-and-comparability.md#ribeiro-2020-checklist) | 把文本测量验证从单一准确率扩展到预先定义的能力、应保持不变的改写与应改变判断的情形。 |
| 2020 · EMNLP Findings · Findings | [Evaluating Models’ Local Decision Boundaries via Contrast Sets](https://aclanthology.org/2020.findings-emnlp.117/)<br>[解读与来源](../topics/validation-and-comparability.md#gardner-2020-contrast-sets) | 适合把构念边界转为成对测试：只有目标含义变化时，测量结果是否按预期改变。 |


## 测量误差与下游推断

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2023 · NeurIPS · 主会 | [Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](https://papers.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract-Conference.html)<br>[解读与来源](../topics/measurement-error-and-inference.md#egami-2023-imperfect-surrogates) | 直接回答如何把 LLM 或其他分类器的代理标签用于统计推断，而不只评价标签预测准确率。 |


## 人机协作与使用条件

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2025 · ACL Findings · Findings | [Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks](https://aclanthology.org/2025.findings-acl.1323/)<br>[解读与来源](../topics/human-ai-workflows.md#schroeder-2025-human-loop-annotation) | 直接说明人工复核未必形成独立的测量标准，适合设计盲审、独立金标准和避免评估循环的工作流。 |
