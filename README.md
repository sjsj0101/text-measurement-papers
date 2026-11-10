<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->

<div align="center">

# Text Measurement Papers

研究定义驱动的文本变量构建与测量验证

Constructs → Text Variables → Measurement Validation

**51 篇主目录 · 13 篇补充 · 0 条待核验 · 基线检索日期 2026-11-09**

</div>

## Scope

围绕研究者给定的构念定义、编码规则和文本语料，整理从标注与小模型适配到独立验证及下游推断的方法。面向IS、营销与社会科学实证研究者，保留专门的CS方法入口。

优先关注2022年以来的方法，并保留必要的早期测量基础；当前已收录年份为 **1991–2026**。期刊按首次正式在线发表年归档，卷期差异在条目中说明；会议按会议年。

**纳入：** 构念操作化、文本标注与分歧、合成训练和轻量适配、测量效度与等值、误分类修正、与测量任务直接相关的人机协作。正式期刊、主会、Findings、Industry及Demo可进主目录；官方已接收稿单独标明状态。Workshop、预印本／工作论文与辅助背景单列补充，证据不足单列待核验。

**排除：** 仅展示通用预测性能、模型压缩或分类榜单且无法说明测量相关性的研究；普通AI采用效果、完整科研Agent系统和无方法贡献的应用。金融或ESG文本只是可用场景，不作为独立收录理由。

后续定向增补见主数据incremental_updates及逐篇核验日期，不代表全库重新核验。精选文献目录，不声称系统综述或完整venue-year覆盖。仅发布元数据、原创短评与来源链接；阅读摘要、部分正文和全文分别记录，未独立复现实验。

## At a Glance

| 统计口径 | 数量 |
| --- | ---: |
| 主目录 | 51 |
| 补充 | 13 |
| 待核验（不计入收录） | 0 |
| 去重收录总数 | 64 |
| EDITH基线检索返回的唯一库记录 | 180 |
| EDITH命中后累计收录的研究 | 27 |

## How to Use

- [中文研究地图](docs/research-map.zh.md) · [建议阅读路线](docs/reading-routes.md)
- [CS Related Work](docs/cs-related-work.md) · [20个研究候选与文献对应](docs/candidate-map.md)
- [补充文献](docs/supplementary.md) · [待核验候选](docs/pending.md) · [与现有repos的关系](docs/related-repositories.md)
- [来源与检索边界](docs/sources.md) · [数据字段](docs/metadata.md)
- [JSON主数据](data/papers.json) · [CSV](exports/papers.csv) · [BibTeX](exports/references.bib)

## Browse by Topic

每篇仅有一个主展示主题，以下主目录与补充数分别可相加；交叉标签和阅读路线不重复计数。

| 研究主题 | 主目录 | 补充 |
| --- | ---: | ---: |
| [构念定义与操作化](topics/construct-operationalization.md) | 16 | 0 |
| [文本标注与人工判断](topics/annotation-and-judgment.md) | 6 | 2 |
| [合成数据与小模型适配](topics/synthetic-data-and-adaptation.md) | 13 | 4 |
| [测量验证与可比性](topics/validation-and-comparability.md) | 9 | 2 |
| [测量误差与下游推断](topics/measurement-error-and-inference.md) | 5 | 1 |
| [人机协作与使用条件](topics/human-ai-workflows.md) | 2 | 4 |

## Paper Index

主目录简表；完整作者、方法、适用条件和本轮核验来源在主题详情中。

### 构念定义与操作化

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · MIS Quarterly · 期刊 | [AI-Augmented Content Validation in Behavioral Research: Development and Evaluation of the RATER System](https://aisel.aisnet.org/misq/vol50/iss1/7/)<br>[解读与来源](topics/construct-operationalization.md#pillet-2026-rater) | 直接对应构念定义与语言表述之间的内容效度检验，可为文本测量的操作化设计提供参照。 |
| 2026 · ACL · Industry | [Beyond Instruction Optimization: Multi-Agent Error-Driven Class Description Refinement for LLM-Based Classification](https://aclanthology.org/2026.acl-industry.137/)<br>[解读与来源](topics/construct-operationalization.md#dev-2026-class-description-refinement) | 直接连接概念定义、标签规则和分类误差，适合讨论编码手册如何转为模型可执行的测量规则。 |
| 2025 · Management Science · 期刊 | [ChatGPT for Textual Analysis? How to Use Generative LLMs in Accounting Research](https://pubsonline.informs.org/doi/10.1287/mnsc.2023.03253)<br>[解读与来源](topics/construct-operationalization.md#de-kok-2025-chatgpt-textual-analysis) | 将 LLM 的操作选择与测量目标和验证责任连接，是从模型能力走向实证变量的实用方法文献。 |
| 2025 · Information Systems Research · 期刊 | [The ITEM Ontology: A Tool to Elucidate the Anatomy of Psychometric Indicators](https://doi.org/10.1287/isre.2023.0257)<br>[解读与来源](topics/construct-operationalization.md#larsen-2025-item-ontology) | 为构念定义与编码指南的语义拆解提供基础：先说明文本要支持什么判断，再评价分类器能否保留这些条件。 |
| 2023 · MIS Quarterly · 期刊 | [Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method](https://aisel.aisnet.org/misq/vol47/iss3/10/)<br>[解读与来源](topics/construct-operationalization.md#zhao-2023-expert-industry-assignment) | 示范如何把显式类别定义、分类体系和专家标签同时纳入文本变量构建。 |
| 2022 · Journal of Marketing Research · 期刊 | [Beyond Sentiment: The Value and Measurement of Consumer Certainty in Language](https://journals.sagepub.com/doi/abs/10.1177/00222437221134802)<br>[解读与来源](topics/construct-operationalization.md#rocklage-2022-certainty-lexicon) | 展示同一文本中需要区分态度方向与态度确定性等不同构念，并将工具开发与多种验证情境相结合。 |
| 2022 · Information Systems Research · 期刊 | [Getting Personal: A Deep Learning Artifact for Text-Based Measurement of Personality](https://pubsonline.informs.org/doi/10.1287/isre.2022.1111)<br>[解读与来源](topics/construct-operationalization.md#yang-2022-deepperson) | 直接连接心理构念、文本测量和下游应用，同时展示伪标签与领域适配在测量模型中的作用。 |
| 2020 · Marketing Science · 期刊 | [Improving Text Analysis Using Sentence Conjunctions and Punctuation](https://pubsonline.informs.org/doi/10.1287/mksc.2019.1214)<br>[解读与来源](topics/construct-operationalization.md#buschken-2020-sentence-conjunctions) | 说明文本表示和预处理会改变可得到的测量信息，并为消费者评价主题测量提供结构化方法。 |
| 2019 · MIS Quarterly · 期刊 | [Operationalizing Regulatory Focus in the Digital Age: Evidence from an E-Commerce Context](https://aisel.aisnet.org/misq/vol43/iss3/5/)<br>[解读与来源](topics/construct-operationalization.md#wu-2019-regulatory-focus) | 提供理论构念、文本指标、独立问卷验证与下游分析相衔接的实证案例。 |
| 2019 · Journal of Consumer Psychology · 期刊 | [The Importance of Construct Validity in Consumer Research](https://myscp.onlinelibrary.wiley.com/doi/10.1002/jcpy.1145)<br>[解读与来源](topics/construct-operationalization.md#mochon-2019-construct-validity) | 为文本变量命名和解释提供概念警示：标签与理论术语相同，不代表测量对象一致。 |
| 2019 · Journal of Marketing · 期刊 | [Uniting the Tribes: Using Text for Marketing Insight](https://journals.sagepub.com/doi/abs/10.1177/0022242919873106)<br>[解读与来源](topics/construct-operationalization.md#berger-2019-uniting-tribes) | 适合作为研究地图导读，把文本信号的来源、解释目标、测量方法和验证要求放在同一框架中。 |
| 2018 · MIS Quarterly · 期刊 | [Text Analytics to Support Sense-Making in Social Media: A Language-Action Perspective](https://aisel.aisnet.org/misq/vol42/iss2/6/)<br>[解读与来源](topics/construct-operationalization.md#abbasi-2018-language-action) | 说明应依据理论明确文本要表达的行动或意图维度，再设计特征及验证任务，超越单纯词义归类。 |
| 2018 · Journal of Consumer Research · 期刊 | [What Happens in Vegas Stays on TripAdvisor? A Theory and Technique to Understand Narrativity in Consumer Reviews](https://doi.org/10.1093/jcr/ucy067)<br>[解读与来源](topics/construct-operationalization.md#van-laer-2018-narrativity) | 展示理论概念、可编码特征、计算测量及外部验证之间的对应，适合作为构念操作化案例。 |
| 2017 · Journal of Consumer Research · 期刊 | [Automated Text Analysis for Consumer Research](https://academic.oup.com/jcr/article/44/6/1274/4283031)<br>[解读与来源](topics/construct-operationalization.md#humphreys-2017-automated-text-analysis) | 为由研究问题和构念定义出发选择文本方法提供导读，并提示自然文本的生态效度与适用边界。 |
| 2011 · MIS Quarterly · 期刊 | [Measurement and Meaning in Information Systems and Organizational Research: Methodological and Philosophical Foundations](https://aisel.aisnet.org/misq/vol35/iss2/4/)<br>[解读与来源](topics/construct-operationalization.md#bagozzi-2011-measurement-meaning) | 作为测量基础，帮助先界定构念及指标关系，再决定文本特征是否能支持所声称的变量含义。 |
| 2011 · The Journal of Finance · 期刊 | [When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks](https://doi.org/10.1111/j.1540-6261.2010.01625.x)<br>[解读与来源](topics/construct-operationalization.md#loughran-2011-financial-dictionaries) | 以领域语义说明同一词语的含义不能直接跨情境迁移，是制定编码规则和检验文本测量边界的基础案例。 |


### 文本标注与人工判断

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2025 · MIS Quarterly · 期刊 | [Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning](https://aisel.aisnet.org/misq/vol49/iss3/12/)<br>[解读与来源](topics/annotation-and-judgment.md#liu-2025-fastsr) | 为高专业知识、少量标签场景的文本变量提取提供专家参与和多任务设计案例。 |
| 2025 · MIS Quarterly · 期刊 | [Mitigating Bias in Hate Speech Detection with a Small Number of Expert Annotations: A Prompt-Based Learning Approach](https://aisel.aisnet.org/misq/vol49/iss4/14/)<br>[解读与来源](topics/annotation-and-judgment.md#wei-2025-expert-hate-speech) | 说明标注者知识与群体语言背景会改变标签含义，适合讨论如何建立可靠测量参照。 |
| 2024 · ACL · 主会 | [VariErr NLI: Separating Annotation Error from Human Label Variation](https://aclanthology.org/2024.acl-long.123/)<br>[解读与来源](topics/annotation-and-judgment.md#weber-genzel-2024-varierr) | 提供把低一致性拆成标注错误与有效观点差异的可操作程序，适用于构建更可靠的测量参照。 |
| 2022 · TACL · 期刊 | [Investigating Reasons for Disagreement in Natural Language Inference](https://aclanthology.org/2022.tacl-1.78/)<br>[解读与来源](topics/annotation-and-judgment.md#jiang-2022-nli-disagreement) | 提醒文本测量先诊断不一致来源，再决定修订规则、清洗错误或保留多种判断。 |
| 2022 · EMNLP · 主会 | [The “Problem” of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation](https://aclanthology.org/2022.emnlp-main.731/)<br>[解读与来源](topics/annotation-and-judgment.md#plank-2022-human-label-variation) | 为主观文本测量为何保留分歧、如何选择标签聚合与评价目标提供概念框架。 |
| 1991 · Journal of Consumer Research · 期刊 | [Content-Analysis Research: An Examination of Applications with Directives for Improving Research Reliability and Objectivity](https://academic.oup.com/jcr/article/18/2/243/1786851)<br>[解读与来源](topics/annotation-and-judgment.md#kolbe-1991-content-analysis) | 为人工标注基准和编码流程的质量控制提供基础，提醒自动化测量也不能忽略参照标签的形成过程。 |


### 合成数据与小模型适配

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · EACL Findings · Findings | [Better as Generators Than Classifiers: Leveraging LLMs and Synthetic Data for Low-Resource Multilingual Classification](https://aclanthology.org/2026.findings-eacl.148/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#pecher-2026-generators-classifiers) | 连接低资源语言的文本变量构造与小模型部署，也为跨语言测量流程选择提供方法证据。 |
| 2026 · Information Systems Research · 期刊 | [Reference Aware Delexicalization (RAD) Framework: Theory Driven Artificial Intelligence Modeling for Domain Generalization](https://doi.org/10.1287/isre.2023.0457)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#suntwal-2026-rad) | 为理论知识如何进入训练数据设计提供直接方法近邻，可用于比较语义约束增强与单纯扩充数据的差别。 |
| 2024 · ACL Findings · Findings | [Better Synthetic Data by Retrieving and Transforming Existing Datasets](https://aclanthology.org/2024.findings-acl.385/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#gandhi-2024-datatune) | 为避免从空白提示生成单调样本提供替代路径，也适合讨论既有语料如何转化为新编码任务的训练材料。 |
| 2024 · ACL Findings · Findings | [Don’t Augment, Rewrite? Assessing Abusive Language Detection with Synthetic Data](https://aclanthology.org/2024.findings-acl.669/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#casula-2024-rewrite-abusive-language) | 展示保留任务含义同时改变文本表面的数据改造策略，可用于讨论共享困难下的分类器训练和外部验证。 |
| 2024 · NAACL Findings · Findings | [GOLD: Generalized Knowledge Distillation via Out-of-Distribution-Guided Language Data Generation](https://aclanthology.org/2024.findings-naacl.272/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#gholami-2024-gold) | 为稀有或边界文本类别的合成采样提供机制，可用于检验生成数据是否只覆盖容易样本。 |
| 2024 · EACL · 主会 | [The Parrot Dilemma: Human-Labeled vs. LLM-augmented Data in Classification Tasks](https://aclanthology.org/2024.eacl-short.17/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#moller-2024-parrot-dilemma) | 为研究者选择人工标注、合成补样或直接 LLM 编码提供任务层面的对照，而非仅看生成成本。 |
| 2023 · ACL Findings · Findings | [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://aclanthology.org/2023.findings-acl.507/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#hsieh-2023-distilling-step-by-step) | 为将研究者定义的判断任务压缩为可部署分类器提供训练方法，并提示保留判断理由可能有助于学习。 |
| 2023 · EMNLP System Demonstrations · System Demonstrations | [Prompt2Model: Generating Deployable Models from Natural Language Instructions](https://aclanthology.org/2023.emnlp-demo.38/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#viswanathan-2023-prompt2model) | 可作为把编码规则实现为小模型的系统入口，也便于讨论生成训练集和验证集的职责。 |
| 2023 · EMNLP · 主会 | [Synthetic Data Generation with Large Language Models for Text Classification: Potential and Limitations](https://aclanthology.org/2023.emnlp-main.647/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#li-2023-synthetic-data-limitations) | 帮助判断哪些文本变量适合用合成样本构建，以及哪些主观构念更需要独立人工参照。 |
| 2023 · EMNLP · 主会 | [TrueTeacher: Learning Factual Consistency Evaluation with Large Language Models](https://aclanthology.org/2023.emnlp-main.127/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#gekhman-2023-trueteacher) | 提供将昂贵的语言判断蒸馏为专用测量模型的实例，强调训练错误类型应接近实际待测文本。 |
| 2022 · TACL · 期刊 | [Generate, Annotate, and Learn: NLP with Synthetic Text](https://aclanthology.org/2022.tacl-1.48/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#he-2022-generate-annotate-learn) | 帮助区分生成分布与标注规则两个误差来源，并为自动标注训练流程提供清晰的模块划分。 |
| 2022 · EMNLP Findings · Findings | [ProGen: Progressive Zero-shot Dataset Generation via In-context Feedback](https://aclanthology.org/2022.findings-emnlp.269/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#ye-2022-progen) | 直接提供按学生模型反馈改进合成分类语料的早期方法入口，适合与随机扩充和主动标注比较。 |
| 2022 · EMNLP · 主会 | [ZeroGen: Efficient Zero-shot Learning via Dataset Generation](https://aclanthology.org/2022.emnlp-main.801/)<br>[解读与来源](topics/synthetic-data-and-adaptation.md#ye-2022-zerogen) | 提供从零样本任务定义到小分类器的基本路径，是后续反馈式生成和数据改造研究的比较基线。 |


### 测量验证与可比性

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2023 · MIS Quarterly · 期刊 | [Extracting Actionable Insights from Text Data: A Stable Topic Model Approach](https://aisel.aisnet.org/misq/vol47/iss3/3/)<br>[解读与来源](topics/validation-and-comparability.md#yang-2023-stable-lda) | 连接文本变量的重复性与后续实证结论，是评估主题测量稳定性的直接方法文献。 |
| 2023 · Journal of Consumer Psychology · 期刊 | [PassivePy: A tool to automatically identify passive voice in big text data](https://doi.org/10.1002/jcpy.1377)<br>[解读与来源](topics/validation-and-comparability.md#sepehri-2023-passivepy) | 提供从明确语言特征、可复用工具到独立人工验证的实例，帮助区分可观测语言现象与更抽象的研究构念。 |
| 2022 · NAACL · 主会 | [Time Waits for No One! Analysis and Challenges of Temporal Misalignment](https://aclanthology.org/2022.naacl-main.435/)<br>[解读与来源](topics/validation-and-comparability.md#luu-2022-temporal-misalignment) | 支持文本测量按时间外推单独验证，并把模型更新与跨期可比性问题纳入设计。 |
| 2021 · EMNLP Findings · Findings | [Temporal Adaptation of BERT and Performance on Downstream Document Classification: Insights from Social Media](https://aclanthology.org/2021.findings-emnlp.206/)<br>[解读与来源](topics/validation-and-comparability.md#rottger-2021-temporal-adaptation) | 为纵向文本测量提供直接提醒：识别语言变化与维持分类可比性不是同一问题，应使用时间划分的任务验证。 |
| 2020 · ACL · 主会 | [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/)<br>[解读与来源](topics/validation-and-comparability.md#ribeiro-2020-checklist) | 把文本测量验证从单一准确率扩展到预先定义的能力、应保持不变的改写与应改变判断的情形。 |
| 2020 · EMNLP Findings · Findings | [Evaluating Models’ Local Decision Boundaries via Contrast Sets](https://aclanthology.org/2020.findings-emnlp.117/)<br>[解读与来源](topics/validation-and-comparability.md#gardner-2020-contrast-sets) | 适合把构念边界转为成对测试：只有目标含义变化时，测量结果是否按预期改变。 |
| 2013 · Political Analysis · 期刊 | [Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts](https://www.cambridge.org/core/journals/political-analysis/article/text-as-data-the-promise-and-pitfalls-of-automatic-content-analysis-methods-for-political-texts/F7AAC8B2909441603FEB25C156448F20)<br>[解读与来源](topics/validation-and-comparability.md#grimmer-2013-text-as-data) | 为整条文本测量链提供方法论起点：统计拟合良好不能单独确定变量的理论含义。 |
| 2001 · MIS Quarterly · 期刊 | [Validation in Information Systems Research: A State-of-the-Art Assessment](https://aisel.aisnet.org/misq/vol25/iss1/1/)<br>[解读与来源](topics/validation-and-comparability.md#boudreau-2001-validation-is) | 提供评估测量论证是否完整的基础框架，可用于审查文本变量是否只有预测成绩而缺乏构念证据。 |
| 2000 · Organizational Research Methods · 期刊 | [A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research](https://journals.sagepub.com/doi/10.1177/109442810031002)<br>[解读与来源](topics/validation-and-comparability.md#vandenberg-2000-measurement-invariance) | 为比较不同群体、时期或语言中的文本分数提供测量可比性基础，避免把测量机制差异误解为构念差异。 |


### 测量误差与下游推断

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2025 · MIS Quarterly · 期刊 | [Correcting Measurement Error in Regression Models with Variables Constructed from Aggregated Output of Data Mining Models](https://aisel.aisnet.org/misq/vol49/iss1/6/)<br>[解读与来源](topics/measurement-error-and-inference.md#qiao-2025-aggregated-measurement-error) | 覆盖评论情感等个体预测聚合为产品或组织变量后的测量误差，补充逐条标签校正。 |
| 2023 · Science · 期刊 | [Prediction-powered inference](https://doi.org/10.1126/science.adi6000)<br>[解读与来源](topics/measurement-error-and-inference.md#angelopoulos-2023-prediction-powered-inference) | 为文本变量的验证预算提供推断起点：独立标签既用于检查分类质量，也可用于校正估计。 |
| 2023 · NeurIPS · 主会 | [Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](https://papers.neurips.cc/paper_files/paper/2023/hash/d862f7f5445255090de13b825b880d59-Abstract-Conference.html)<br>[解读与来源](topics/measurement-error-and-inference.md#egami-2023-imperfect-surrogates) | 直接回答如何把 LLM 或其他分类器的代理标签用于统计推断，而不只评价标签预测准确率。 |
| 2021 · Information Systems Research · 期刊 | [Correcting Misclassification Bias in Regression Models with Variables Generated via Data Mining](https://pubsonline.informs.org/doi/10.1287/isre.2020.0977)<br>[解读与来源](topics/measurement-error-and-inference.md#qiao-2021-misclassification-bias) | 直接处理从文本分类标签到回归推断的误差传播，区分预测指标与目标参数精度。 |
| 2018 · Information Systems Research · 期刊 | [Mind the Gap: Accounting for Measurement Error and Misclassification in Variables Generated via Data Mining](https://pubsonline.informs.org/doi/10.1287/isre.2017.0727)<br>[解读与来源](topics/measurement-error-and-inference.md#yang-2018-mind-the-gap) | 为把文本预测分数当作观测变量的实证研究提供误差诊断和校正入口。 |


### 人机协作与使用条件

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2025 · ACL Findings · Findings | [Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks](https://aclanthology.org/2025.findings-acl.1323/)<br>[解读与来源](topics/human-ai-workflows.md#schroeder-2025-human-loop-annotation) | 直接说明人工复核未必形成独立的测量标准，适合设计盲审、独立金标准和避免评估循环的工作流。 |
| 2023 · Management Science · 期刊 | [Reciprocal Human-Machine Learning: A Theory and an Instantiation for the Case of Message Classification](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03518)<br>[解读与来源](topics/human-ai-workflows.md#teeni-2023-reciprocal-learning) | 将专家概念化、模型分类与反馈修订置于同一流程，可用于理解人工判断如何参与测量工具开发。 |


## Sources and Known Gaps

本轮EDITH检索成功：74个查询，合计263次命中，返回180条唯一库记录；其中1个宽查询有返回上限。命中不自动证明发表或贡献，最终按官方来源与研究范围筛选。

种子引用已逐条筛选；部分出版页受访问限制时，通过作者原稿、机构存档及出版注册信息交叉核对并记录证据层次。宽查询之外未全量筛查、后续版本变化及语言／领域代表性仍是缺口。具体查询与未收录理由见[来源说明](docs/sources.md)。

## Contributing

编辑唯一主数据后生成并检查：

```sh
python3 scripts/catalog.py --write
python3 scripts/catalog.py --check
python3 -m unittest discover -s tests -v
git diff --check
```

使用Python 3.9或以上，无第三方运行依赖。详见[维护说明](CONTRIBUTING.md)。

## Acknowledgements and License

主要参考 [good_llm_stats_papers](https://github.com/sjsj0101/good_llm_stats_papers) 的章节、中文导读、主题导航和引用导出；采用单一JSON与标准库生成器，按本主题重新制定年份与track边界。原创目录说明适用[CC BY 4.0](LICENSE)；外链论文、代码和数据遵循各自许可。
