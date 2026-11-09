<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->

# 建议阅读路线

[返回目录](../README.md) · [研究地图](research-map.zh.md)

顺序用于建立问题理解，不是论文质量排名。

<a id="measurement-start"></a>
## 先建立测量问题

从内容分析与操作化规范进入文本变量，再连接误差、独立标注和推断。

1. [Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts](../topics/validation-and-comparability.md#grimmer-2013-text-as-data) — 为整条文本测量链提供方法论起点：统计拟合良好不能单独确定变量的理论含义。
2. [Automated Text Analysis for Consumer Research](../topics/construct-operationalization.md#humphreys-2017-automated-text-analysis) — 为由研究问题和构念定义出发选择文本方法提供导读，并提示自然文本的生态效度与适用边界。
3. [Measurement and Meaning in Information Systems and Organizational Research: Methodological and Philosophical Foundations](../topics/construct-operationalization.md#bagozzi-2011-measurement-meaning) — 作为测量基础，帮助先界定构念及指标关系，再决定文本特征是否能支持所声称的变量含义。
4. [Mind the Gap: Accounting for Measurement Error and Misclassification in Variables Generated via Data Mining](../topics/measurement-error-and-inference.md#yang-2018-mind-the-gap) — 为把文本预测分数当作观测变量的实证研究提供误差诊断和校正入口。
5. [Correcting Misclassification Bias in Regression Models with Variables Generated via Data Mining](../topics/measurement-error-and-inference.md#qiao-2021-misclassification-bias) — 直接处理从文本分类标签到回归推断的误差传播，区分预测指标与目标参数精度。
6. [Prediction-powered inference](../topics/measurement-error-and-inference.md#angelopoulos-2023-prediction-powered-inference) — 为文本变量的验证预算提供推断起点：独立标签既用于检查分类质量，也可用于校正估计。

<a id="cs-adaptation"></a>
## CS：从任务描述到可复用模型

先比较数据生成和反馈，再看部署、理由蒸馏与轻量分类；预印本身份与正式track始终保留。

1. [ZeroGen: Efficient Zero-shot Learning via Dataset Generation](../topics/synthetic-data-and-adaptation.md#ye-2022-zerogen) — 提供从零样本任务定义到小分类器的基本路径，是后续反馈式生成和数据改造研究的比较基线。
2. [ProGen: Progressive Zero-shot Dataset Generation via In-context Feedback](../topics/synthetic-data-and-adaptation.md#ye-2022-progen) — 直接提供按学生模型反馈改进合成分类语料的早期方法入口，适合与随机扩充和主动标注比较。
3. [Prompt2Model: Generating Deployable Models from Natural Language Instructions](../topics/synthetic-data-and-adaptation.md#viswanathan-2023-prompt2model) — 可作为把编码规则实现为小模型的系统入口，也便于讨论生成训练集和验证集的职责。
4. [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](../topics/synthetic-data-and-adaptation.md#hsieh-2023-distilling-step-by-step) — 为将研究者定义的判断任务压缩为可部署分类器提供训练方法，并提示保留判断理由可能有助于学习。
5. [Knowledge Distillation in Automated Annotation: Supervised Text Classification with LLM-Generated Training Labels](../topics/annotation-and-judgment.md#pangakis-2024-annotation-distillation) — 紧贴从自动标注到可规模化文本变量的流程，也能帮助区分教师标签质量和学生分类器表现。
6. [Efficient Few-Shot Learning Without Prompts](../topics/synthetic-data-and-adaptation.md#tunstall-2022-setfit) — 作为有少量人工标注时的轻量分类基线，可与直接调用 LLM 或使用合成数据的方案比较。
7. [GLiClass: Generalist Lightweight Model for Sequence Classification Tasks](../topics/synthetic-data-and-adaptation.md#stepanov-2025-gliclass) — 可作为动态标签和低成本批量文本编码的候选实现，连接轻量分类与反馈学习。

<a id="validation"></a>
## 独立验证、分歧与可比性

把构念有效性、人类判断差异、边界测试和时间变化分开检查。

1. [The Importance of Construct Validity in Consumer Research](../topics/construct-operationalization.md#mochon-2019-construct-validity) — 为文本变量命名和解释提供概念警示：标签与理论术语相同，不代表测量对象一致。
2. [The “Problem” of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation](../topics/annotation-and-judgment.md#plank-2022-human-label-variation) — 为主观文本测量为何保留分歧、如何选择标签聚合与评价目标提供概念框架。
3. [VariErr NLI: Separating Annotation Error from Human Label Variation](../topics/annotation-and-judgment.md#weber-genzel-2024-varierr) — 提供把低一致性拆成标注错误与有效观点差异的可操作程序，适用于构建更可靠的测量参照。
4. [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](../topics/validation-and-comparability.md#ribeiro-2020-checklist) — 把文本测量验证从单一准确率扩展到预先定义的能力、应保持不变的改写与应改变判断的情形。
5. [Evaluating Models’ Local Decision Boundaries via Contrast Sets](../topics/validation-and-comparability.md#gardner-2020-contrast-sets) — 适合把构念边界转为成对测试：只有目标含义变化时，测量结果是否按预期改变。
6. [A Review and Synthesis of the Measurement Invariance Literature: Suggestions, Practices, and Recommendations for Organizational Research](../topics/validation-and-comparability.md#vandenberg-2000-measurement-invariance) — 为比较不同群体、时期或语言中的文本分数提供测量可比性基础，避免把测量机制差异误解为构念差异。
7. [Temporal Adaptation of BERT and Performance on Downstream Document Classification: Insights from Social Media](../topics/validation-and-comparability.md#rottger-2021-temporal-adaptation) — 为纵向文本测量提供直接提醒：识别语言变化与维持分类可比性不是同一问题，应使用时间划分的任务验证。
8. [Time Waits for No One! Analysis and Challenges of Temporal Misalignment](../topics/validation-and-comparability.md#luu-2022-temporal-misalignment) — 支持文本测量按时间外推单独验证，并把模型更新与跨期可比性问题纳入设计。
9. [Validating Large Language Model Annotations](../topics/validation-and-comparability.md#hansen-2026-validating-llm-annotations) — 提供一种探索性的无外部基准验证思路，可与独立人工基准及测量误差校正方法对照阅读。

<a id="inference"></a>
## 从生成变量到回归推断

沿个体误分类、聚合误差和验证标签的推断用途阅读；再回到任务特有假设。

1. [Mind the Gap: Accounting for Measurement Error and Misclassification in Variables Generated via Data Mining](../topics/measurement-error-and-inference.md#yang-2018-mind-the-gap) — 为把文本预测分数当作观测变量的实证研究提供误差诊断和校正入口。
2. [Correcting Misclassification Bias in Regression Models with Variables Generated via Data Mining](../topics/measurement-error-and-inference.md#qiao-2021-misclassification-bias) — 直接处理从文本分类标签到回归推断的误差传播，区分预测指标与目标参数精度。
3. [Correcting Measurement Error in Regression Models with Variables Constructed from Aggregated Output of Data Mining Models](../topics/measurement-error-and-inference.md#qiao-2025-aggregated-measurement-error) — 覆盖评论情感等个体预测聚合为产品或组织变量后的测量误差，补充逐条标签校正。
4. [Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models](../topics/measurement-error-and-inference.md#egami-2023-imperfect-surrogates) — 直接回答如何把 LLM 或其他分类器的代理标签用于统计推断，而不只评价标签预测准确率。
5. [Prediction-powered inference](../topics/measurement-error-and-inference.md#angelopoulos-2023-prediction-powered-inference) — 为文本变量的验证预算提供推断起点：独立标签既用于检查分类质量，也可用于校正估计。

<a id="human-workflow"></a>
## 人工判断与验证报告

先读直接标注与人机学习，再比较信任和透明度的辅助背景，避免把信任提升等同于测量改善。

1. [Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks](../topics/human-ai-workflows.md#schroeder-2025-human-loop-annotation) — 直接说明人工复核未必形成独立的测量标准，适合设计盲审、独立金标准和避免评估循环的工作流。
2. [Reciprocal Human-Machine Learning: A Theory and an Instantiation for the Case of Message Classification](../topics/human-ai-workflows.md#teeni-2023-reciprocal-learning) — 将专家概念化、模型分类与反馈修订置于同一流程，可用于理解人工判断如何参与测量工具开发。
3. [AI-Augmented Content Validation in Behavioral Research: Development and Evaluation of the RATER System](../topics/construct-operationalization.md#pillet-2026-rater) — 直接对应构念定义与语言表述之间的内容效度检验，可为文本测量的操作化设计提供参照。
4. [To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making](../topics/human-ai-workflows.md#bucinca-2021-cognitive-forcing) — 为文本测量报告和人工复核流程提供辅助设计背景：解释的存在与用户是否核查证据应分别评价。
5. [How Much Information? Effects of Transparency on Trust in an Algorithmic Interface](../topics/human-ai-workflows.md#kizilcec-2016-transparency-trust) — 为测量验证报告提供辅助阅读：报告应说明有助于判断用途的信息，并独立检验理解与正确使用。
6. [Recommendation Agents for Electronic Commerce: Effects of Explanation Facilities on Trusting Beliefs](../topics/human-ai-workflows.md#wang-2007-explanation-trusting-beliefs) — 作为验证报告设计的辅助背景，提示分别衡量解释带来的信任与研究者实际识别错误的能力。
