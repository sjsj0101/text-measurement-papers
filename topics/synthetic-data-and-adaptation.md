<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->

# 合成数据与小模型适配

[返回目录](../README.md) · [阅读路线](../docs/reading-routes.md)

比较合成与真实标注、蒸馏与少样本学习，以及错误反馈带来的收益与偏差。

## 主目录（13 篇）

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


<a id="pecher-2026-generators-classifiers"></a>
### Better as Generators Than Classifiers: Leveraging LLMs and Synthetic Data for Low-Resource Multilingual Classification

**2026 · EACL Findings · Findings** · 会议论文 · 主目录

**作者：** Branislav Pecher; Jan Cegin; Robert Belanec; Ivan Srba; Jakub Simko; Maria Bielikova

**研究内容：** 用多语言 LLM 生成分类数据，再比较小模型微调、指令调优和合成上下文示例等使用方式。作者跨语言与任务评估，报告在部分低资源情境下小模型可超过生成教师的直接分类表现。

**为什么读：** 连接低资源语言的文本变量构造与小模型部署，也为跨语言测量流程选择提供方法证据。

**适用条件与限制：** 分类准确率的跨语言比较不能单独确认构念含义相同；生成语料可能延续教师对语言或群体的偏差，仍需各语言独立参照。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2026.findings-eacl.148/)：已访问官方页面，核对题名、作者、年份、发表身份与摘要。（2026-11-09）

**主题：** 合成数据与小模型适配 · 测量验证与可比性

<a id="suntwal-2026-rad"></a>
### Reference Aware Delexicalization (RAD) Framework: Theory Driven Artificial Intelligence Modeling for Domain Generalization

**2026 · Information Systems Research · 期刊** · 期刊研究 · 主目录

**作者：** Sandeep Suntwal; Susan A. Brown

**研究内容：** 以指称理论指导去词汇化增强，识别容易依赖领域词汇的线索并构造保持语境含义的替代表达，在推断类NLP任务中评价跨域表现。

**为什么读：** 为理论知识如何进入训练数据设计提供直接方法近邻，可用于比较语义约束增强与单纯扩充数据的差别。

**适用条件与限制：** 核心评价是NLI、文本蕴含和事实核验的跨域表现；改善这些基准不自动证明研究构念的等值或下游估计有效。

**本轮证据：** 部分正文；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://pubsonline.informs.org/doi/10.1287/isre.2023.0457)：读取正式出版页、完整摘要及2026-03-05在线日期；本轮另阅读库内正文引言。（2026-11-09）

**年份与版本说明：** 首次在线：2026-03-05；卷期年：2026

**主题：** 合成数据与小模型适配

<a id="gandhi-2024-datatune"></a>
### Better Synthetic Data by Retrieving and Transforming Existing Datasets

**2024 · ACL Findings · Findings** · 会议论文 · 主目录

**作者：** Saumya Gandhi; Ritu Gala; Vijay Viswanathan; Tongshuang Wu; Graham Neubig

**研究内容：** DataTune 先检索现有公开数据，再利用语言模型把它们改造成目标任务所需格式。作者在语言任务上比较直接合成和检索训练，报告数据改造可增加生成样本的多样性与难度。

**为什么读：** 为避免从空白提示生成单调样本提供替代路径，也适合讨论既有语料如何转化为新编码任务的训练材料。

**适用条件与限制：** 改造后的任务格式不保证原始内容与目标构念一致；公开基准的增益不能替代目标语料的独立标注与分布检查。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2024.findings-acl.385/)：从种子 arXiv 更新为 ACL Findings 2024 正式发表版本；保留 arXiv 标识，计为同一研究。（2026-11-09）

**主题：** 合成数据与小模型适配

<a id="casula-2024-rewrite-abusive-language"></a>
### Don’t Augment, Rewrite? Assessing Abusive Language Detection with Synthetic Data

**2024 · ACL Findings · Findings** · 会议论文 · 主目录

**作者：** Camilla Casula; Elisa Leonardelli; Sara Tonelli

**研究内容：** 用指令模型重写英语辱骂检测语料，再训练分类器并检查跨数据集表现。作者考察以重写文本替代原始数据的可行性，同时人工检查文本能否被网络搜索回溯。

**为什么读：** 展示保留任务含义同时改变文本表面的数据改造策略，可用于讨论共享困难下的分类器训练和外部验证。

**适用条件与限制：** 改写可能改变辱骂强度、语用线索或群体表达；搜索不到原文不等于形式隐私保证，分类成绩相近也不证明测量含义完全保留。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2024.findings-acl.669/)：已访问正式页面并读取摘要，核验题名、作者、年份及 track。（2026-11-09）

**主题：** 合成数据与小模型适配 · 测量验证与可比性

<a id="gholami-2024-gold"></a>
### GOLD: Generalized Knowledge Distillation via Out-of-Distribution-Guided Language Data Generation

**2024 · NAACL Findings · Findings** · 会议论文 · 主目录

**作者：** Mohsen Gholami; Mohammad Akbari; Cindy Hu; Vaden Masrani; Z. Jane Wang; Yong Zhang

**研究内容：** GOLD 根据学生模型对分布外样本的反馈迭代生成语言数据，并用能量评分处理生成噪声。其动机是避免生成样本集中在常见模式，使蒸馏训练更能覆盖分布尾部。

**为什么读：** 为稀有或边界文本类别的合成采样提供机制，可用于检验生成数据是否只覆盖容易样本。

**适用条件与限制：** 基准上的泛化收益不证明尾部样本代表真实研究总体；分布外检测也可能把有意义的少数群体表达误判为噪声。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2024.findings-naacl.272/)：网页显示 Tianxi Hu 和 Z. Wang，但 PDF 署名为 Cindy Hu 和 Z. Jane Wang；按 PDF，种子署名此处无需改动。（2026-11-09）
- [metadata](https://aclanthology.org/2024.findings-naacl.272.pdf)：已对照 PDF 首页实际署名，优先于网页作者目录显示名。（2026-11-09）

**主题：** 合成数据与小模型适配

<a id="moller-2024-parrot-dilemma"></a>
### The Parrot Dilemma: Human-Labeled vs. LLM-augmented Data in Classification Tasks

**2024 · EACL · 主会** · 会议论文 · 主目录

**作者：** Anders Giovanni Møller; Arianna Pera; Jacob Aarup Dalsgaard; Luca Maria Aiello

**研究内容：** 在计算社会科学分类任务中比较人工数据、LLM 合成增强和直接零样本分类，并考察训练集规模。作者报告人工数据总体更稳健，合成增强在部分稀有类别上有帮助。

**为什么读：** 为研究者选择人工标注、合成补样或直接 LLM 编码提供任务层面的对照，而非仅看生成成本。

**适用条件与限制：** 稀有类别受益不代表整体标签分布或群体偏差被修复；比较依赖任务、生成模型与训练规模，不能据此给出统一替代比例。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2024.eacl-short.17/)：已读正式摘要；网页省略 Aarup 和 Maria，但 PDF 完整署名包含两者，按 PDF。（2026-11-09）
- [metadata](https://aclanthology.org/2024.eacl-short.17.pdf)：已对照 PDF 首页实际署名，优先于网页作者目录显示名。（2026-11-09）

**主题：** 合成数据与小模型适配 · 文本标注与人工判断

<a id="hsieh-2023-distilling-step-by-step"></a>
### Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes

**2023 · ACL Findings · Findings** · 会议论文 · 主目录

**作者：** Cheng-Yu Hsieh; Chun-Liang Li; Chih-kuan Yeh; Hootan Nakhost; Yasuhisa Fujii; Alex Ratner; Ranjay Krishna; Chen-Yu Lee; Tomas Pfister

**研究内容：** 将大模型解释作为额外监督信号，让小模型在多任务训练中同时学习任务输出和推理理由。作者在 NLP 基准上比较普通微调、标签蒸馏和理由蒸馏，报告后者可降低所需训练数据与模型规模。

**为什么读：** 为将研究者定义的判断任务压缩为可部署分类器提供训练方法，并提示保留判断理由可能有助于学习。

**适用条件与限制：** 大模型生成的理由可能带有系统性错误，预测提升不证明理由真实或具有构念效度；跨域和主观测量任务仍须独立人工校验。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2023.findings-acl.507/)：已访问官方页面，核对题名、作者、年份、发表身份与摘要。（2026-11-09）

**主题：** 合成数据与小模型适配 · 文本标注与人工判断

<a id="viswanathan-2023-prompt2model"></a>
### Prompt2Model: Generating Deployable Models from Natural Language Instructions

**2023 · EMNLP System Demonstrations · System Demonstrations** · 会议论文 · 主目录

**作者：** Vijay Viswanathan; Chenyang Zhao; Amanda Bertsch; Tongshuang Wu; Graham Neubig

**研究内容：** 将自然语言任务描述转成专用模型：检索相关数据集与预训练模型，生成补充数据，再监督微调。作者展示从提示到可部署模型的集成流程，并讨论利用所得数据估计性能。

**为什么读：** 可作为把编码规则实现为小模型的系统入口，也便于讨论生成训练集和验证集的职责。

**适用条件与限制：** 演示任务数量有限；如果评估数据与训练数据共享生成源或任务误解，性能估计不能代替独立真实样本上的测量验证。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2023.emnlp-demo.38/)：已读正式 EMNLP 2023 System Demonstrations 页面；由种子 arXiv 升级为正式 demo，独立 track=demo。（2026-11-09）

**主题：** 合成数据与小模型适配 · 构念定义与操作化

<a id="li-2023-synthetic-data-limitations"></a>
### Synthetic Data Generation with Large Language Models for Text Classification: Potential and Limitations

**2023 · EMNLP · 主会** · 会议论文 · 主目录

**作者：** Zhuoyan Li; Hangxiao Zhu; Zhuoran Lu; Ming Yin

**研究内容：** 比较合成训练数据在不同文本分类任务中的效果，重点考察任务及样本的主观性。作者发现主观性越强，合成数据训练分类器的表现越弱，提示数据生成效果依赖判断性质。

**为什么读：** 帮助判断哪些文本变量适合用合成样本构建，以及哪些主观构念更需要独立人工参照。

**适用条件与限制：** 结果是所研究任务中主观性与表现的关联，不能视为主观性导致退化的通用因果结论；分类效果也不等于构念效度。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2023.emnlp-main.647/)：已访问官方页面，核对题名、作者、年份、发表身份与摘要。（2026-11-09）

**主题：** 合成数据与小模型适配 · 文本标注与人工判断

<a id="gekhman-2023-trueteacher"></a>
### TrueTeacher: Learning Factual Consistency Evaluation with Large Language Models

**2023 · EMNLP · 主会** · 会议论文 · 主目录

**作者：** Zorik Gekhman; Jonathan Herzig; Roee Aharoni; Chen Elkind; Idan Szpektor

**研究内容：** TrueTeacher 让 LLM 为多种模型生成的摘要标注事实一致性，再用合成监督训练较小的评价模型。作者将其与依靠扰动人工摘要的方法比较，并考察领域变化和多语言场景。

**为什么读：** 提供将昂贵的语言判断蒸馏为专用测量模型的实例，强调训练错误类型应接近实际待测文本。

**适用条件与限制：** 事实一致性是摘要与源文档之间的特定关系，不能直接泛化到主观社会构念；教师标签和生成摘要分布可能共同限制评价器覆盖。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2023.emnlp-main.127/)：正式页面及 PDF 题名为 Learning Factual Consistency Evaluation with Large Language Models；种子 Google Research 页保留 Generating Synthetic Data… 旧题。正式第四作者为 Chen Elkind，不是 Chenel Elkind。版本合并计一篇。（2026-11-09）
- [metadata](https://aclanthology.org/2023.emnlp-main.127.pdf)：PDF 首页确认正式标题和 Chen Elkind 署名。（2026-11-09）
- [metadata](https://research.google/pubs/trueteacher-generating-synthetic-data-for-factual-consistency-evaluation-using-large-language-models/)：原始种子来源保留旧题名及 Chenel Elkind 写法，且链接 ACL 正式论文。采用 ACL PDF 的正式题名和 Chen Elkind，两个入口归为同一研究。（2026-11-09）

**主题：** 合成数据与小模型适配 · 测量验证与可比性

<a id="he-2022-generate-annotate-learn"></a>
### Generate, Annotate, and Learn: NLP with Synthetic Text

**2022 · TACL · 期刊** · 期刊研究 · 主目录

**作者：** Xuanli He; Islam Nassar; Jamie Kiros; Gholamreza Haffari; Mohammad Norouzi

**研究内容：** GAL 将文本生成、伪标签标注与学习分开：先产生任务相关的无标签文本，再由可用分类器或语言模型标注，最后与原始数据联合训练。文章把这一流程用于蒸馏、自训练和少样本学习。

**为什么读：** 帮助区分生成分布与标注规则两个误差来源，并为自动标注训练流程提供清晰的模块划分。

**适用条件与限制：** 伪标签仍依赖教师质量，生成文本也可能偏离目标总体；训练收益不说明构念定义、少数群体表示或测量误差已得到独立验证。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2022.tacl-1.48/)：已访问正式页面并读取摘要，核验题名、作者、年份及 track。（2026-11-09）

**主题：** 合成数据与小模型适配 · 文本标注与人工判断

<a id="ye-2022-progen"></a>
### ProGen: Progressive Zero-shot Dataset Generation via In-context Feedback

**2022 · EMNLP Findings · Findings** · 会议论文 · 主目录

**作者：** Jiacheng Ye; Jiahui Gao; Jiangtao Feng; Zhiyong Wu; Tao Yu; Lingpeng Kong

**研究内容：** ProGen 利用任务模型反馈挑选上下文示例，逐步引导预训练语言模型产生新的训练数据。作者在文本分类任务上评估这种生成与学习交替进行的流程，针对静态合成集的信息不足和冗余问题。

**为什么读：** 直接提供按学生模型反馈改进合成分类语料的早期方法入口，适合与随机扩充和主动标注比较。

**适用条件与限制：** 模型反馈可能强化现有错误，任务基准的预测改善也不保证覆盖构念边界；应使用独立真实文本检查反馈闭环是否偏离编码目标。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2022.findings-emnlp.269/)：已读摘要。网页作者顺序为 Zhiyong Wu 在 Jiangtao Feng 之前；正式 PDF 首页相反，按 PDF 采用 Jiangtao Feng、Zhiyong Wu。（2026-11-09）
- [metadata](https://aclanthology.org/2022.findings-emnlp.269.pdf)：PDF 首页确认作者顺序，Jiangtao Feng 在 Zhiyong Wu 前。（2026-11-09）

**主题：** 合成数据与小模型适配

<a id="ye-2022-zerogen"></a>
### ZeroGen: Efficient Zero-shot Learning via Dataset Generation

**2022 · EMNLP · 主会** · 会议论文 · 主目录

**作者：** Jiacheng Ye; Jiahui Gao; Qintong Li; Hang Xu; Jiangtao Feng; Zhiyong Wu; Tao Yu; Lingpeng Kong

**研究内容：** ZeroGen 用预训练语言模型从任务描述生成数据，再训练小型专用模型，将昂贵生成集中在训练阶段。作者在分类、问答和自然语言推断中考察这种零样本数据生成式蒸馏。

**为什么读：** 提供从零样本任务定义到小分类器的基本路径，是后续反馈式生成和数据改造研究的比较基线。

**适用条件与限制：** 无需人工训练标签不代表无需人工测量验证；生成器可能错误理解类别或遗漏真实语言分布，部署时仍需独立目标样本。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2022.emnlp-main.801/)：已访问正式页面并读取摘要，核验题名、作者、年份及 track。（2026-11-09）

**主题：** 合成数据与小模型适配

## 补充（4 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · COLM · 主会 · 官方已接收 | [Towards Active Synthetic Data Generation for Finetuning Language Models](https://colm.eventhosts.cc/Conferences/2026/AcceptedPapers)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#kessler-2025-active-synthetic-data) | 为按分类器薄弱点组织合成数据提供邻近方法背景；实验并非社会科学文本构念测量，因此列入补充。 |
| 2025 · arXiv · 预印本 | [GLiClass: Generalist Lightweight Model for Sequence Classification Tasks](https://arxiv.org/abs/2508.07662)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#stepanov-2025-gliclass) | 可作为动态标签和低成本批量文本编码的候选实现，连接轻量分类与反馈学习。 |
| 2024 · arXiv · 预印本 | [Data Generation Using Large Language Models for Text Classification: An Empirical Case Study](https://arxiv.org/abs/2407.12813)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#li-2024-data-generation-case-study) | 为合成文本变量训练样本时的生成设置与诊断提供经验参照，避免仅以生成量评价数据质量。 |
| 2022 · arXiv · 预印本 | [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)<br>[解读与来源](../topics/synthetic-data-and-adaptation.md#tunstall-2022-setfit) | 作为有少量人工标注时的轻量分类基线，可与直接调用 LLM 或使用合成数据的方案比较。 |


<a id="kessler-2025-active-synthetic-data"></a>
### Towards Active Synthetic Data Generation for Finetuning Language Models

**2026 · COLM · 主会 · 官方已接收** · 会议论文 · 补充

**作者：** Samuel Kessler; Menglin Xia; Daniel Madrigal; Dongge Han; Helia Hashemi; Saravan Rajmohan; Victor Rühle; Jordan T Ash

**研究内容：** 研究让学生模型当前状态反馈到下一轮合成样本选择的闭环蒸馏。作者在数学与逻辑推理任务上比较静态生成和迭代生成，报告简单主动学习准则也能有效利用生成预算。

**为什么读：** 为按分类器薄弱点组织合成数据提供邻近方法背景；实验并非社会科学文本构念测量，因此列入补充。

**适用条件与限制：** 证据来自数学与逻辑推理任务，不能直接推断其能改善主观标签、构念效度或下游估计。官方名单确认 COLM 2026 接收；正式 OpenReview 页面及 PDF 被浏览器验证拦截，内容短评依 arXiv v2 摘要。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [content](https://arxiv.org/abs/2512.00884)：已读 arXiv 摘要与版本记录：首发 2025-11-30，v2 2026-02-09；内容证据来自此版本。后续查获 COLM 2026 官方接收记录，论文仅计一次。（2026-11-09）
- [publication](https://colm.eventhosts.cc/Conferences/2026/AcceptedPapers)：官方名单列出题名并链接 OpenReview c2pJvSu6Qo；作者按官方接收列表。该列表写 Daniel Madrigal、Helia Hashemi、Victor Rühle、Jordan T Ash，与 arXiv 拼写/姓名长度不同；保留来源差异。（2026-11-09）

**主题：** 合成数据与小模型适配

<a id="stepanov-2025-gliclass"></a>
### GLiClass: Generalist Lightweight Model for Sequence Classification Tasks

**2025 · arXiv · 预印本** · 预印本／工作论文 · 补充

**作者：** Ihor Stepanov; Mykhailo Shtopko; Dmytro Vodianytskyi; Oleksandr Lukashov; Alexander Yavorskyi; Mykyta Yaroshenko

**研究内容：** GLiClass 将 GLiNER 思路改为序列分类，以兼顾灵活标签与高效推断。文章面向零样本和少样本分类，并探索用 PPO 处理稀疏数据或人工反馈下的多标签训练。

**为什么读：** 可作为动态标签和低成本批量文本编码的候选实现，连接轻量分类与反馈学习。

**适用条件与限制：** 模型效率与分类基准表现不证明标签语义符合研究构念；复杂约束、长标签集及跨域使用仍须专门验证。本轮未找到可核验的正式发表版本。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [content](https://arxiv.org/abs/2508.07662)：已访问正式页面并读取摘要，核验题名、作者、年份及 track。（2026-11-09）

**主题：** 合成数据与小模型适配 · 文本标注与人工判断

<a id="li-2024-data-generation-case-study"></a>
### Data Generation Using Large Language Models for Text Classification: An Empirical Case Study

**2024 · arXiv · 预印本** · 预印本／工作论文 · 补充

**作者：** Yinheng Li; Rogerio Bonatti; Sara Abdali; Justin Wagle; Kazuhito Koishida

**研究内容：** 以合成数据训练的文本分类器为检验工具，研究提示方式、任务复杂度以及生成数据数量、质量和多样性对效果的影响。文章据此讨论面向分类任务的数据生成实践。

**为什么读：** 为合成文本变量训练样本时的生成设置与诊断提供经验参照，避免仅以生成量评价数据质量。

**适用条件与限制：** 分类器成绩是数据质量的间接指标，不证明合成样本代表研究总体或保持构念。arXiv 自述 DMLR@ICML 2024 接收，但本轮官方 workshop 页面未返回该文条目，暂按可核验预印本收录。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [content](https://arxiv.org/abs/2407.12813)：已读 arXiv v2 摘要、作者、版本记录及 DMLR 接收自述。dmlr.ai/program/ 未显示逐篇列表，OpenReview group 仅返回 Loading，未把作者自述或 ICML 页脚当主会发表证据。（2026-11-09）

**主题：** 合成数据与小模型适配

<a id="tunstall-2022-setfit"></a>
### Efficient Few-Shot Learning Without Prompts

**2022 · arXiv · 预印本** · 预印本／工作论文 · 补充

**作者：** Lewis Tunstall; Nils Reimers; Unso Eun Seo Jo; Luke Bates; Daniel Korat; Moshe Wasserblat; Oren Pereg

**研究内容：** SetFit 先用少量带标签文本形成配对样本，对句向量模型做对比式微调，再训练分类头。作者据此展示无需任务提示或标签词映射的少样本文本分类方法，并考察多语言使用。

**为什么读：** 作为有少量人工标注时的轻量分类基线，可与直接调用 LLM 或使用合成数据的方案比较。

**适用条件与限制：** 依赖预训练表示和有限标注覆盖；少样本分类表现不能替代对潜在构念、群体差异和时间迁移的测量验证。本轮未查到可核验的正式发表版本。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [content](https://arxiv.org/abs/2209.11055)：已访问官方页面，核对题名、作者、年份、发表身份与摘要。（2026-11-09）

**主题：** 合成数据与小模型适配

## 跨主题阅读

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · ACL · Industry | [Beyond Instruction Optimization: Multi-Agent Error-Driven Class Description Refinement for LLM-Based Classification](https://aclanthology.org/2026.acl-industry.137/)<br>[解读与来源](../topics/construct-operationalization.md#dev-2026-class-description-refinement) | 直接连接概念定义、标签规则和分类误差，适合讨论编码手册如何转为模型可执行的测量规则。 |
| 2025 · MIS Quarterly · 期刊 | [Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning](https://aisel.aisnet.org/misq/vol49/iss3/12/)<br>[解读与来源](../topics/annotation-and-judgment.md#liu-2025-fastsr) | 为高专业知识、少量标签场景的文本变量提取提供专家参与和多任务设计案例。 |
| 2025 · MIS Quarterly · 期刊 | [Mitigating Bias in Hate Speech Detection with a Small Number of Expert Annotations: A Prompt-Based Learning Approach](https://aisel.aisnet.org/misq/vol49/iss4/14/)<br>[解读与来源](../topics/annotation-and-judgment.md#wei-2025-expert-hate-speech) | 说明标注者知识与群体语言背景会改变标签含义，适合讨论如何建立可靠测量参照。 |
| 2023 · MIS Quarterly · 期刊 | [Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method](https://aisel.aisnet.org/misq/vol47/iss3/10/)<br>[解读与来源](../topics/construct-operationalization.md#zhao-2023-expert-industry-assignment) | 示范如何把显式类别定义、分类体系和专家标签同时纳入文本变量构建。 |
| 2022 · Information Systems Research · 期刊 | [Getting Personal: A Deep Learning Artifact for Text-Based Measurement of Personality](https://pubsonline.informs.org/doi/10.1287/isre.2022.1111)<br>[解读与来源](../topics/construct-operationalization.md#yang-2022-deepperson) | 直接连接心理构念、文本测量和下游应用，同时展示伪标签与领域适配在测量模型中的作用。 |
| 2022 · NAACL · 主会 | [Time Waits for No One! Analysis and Challenges of Temporal Misalignment](https://aclanthology.org/2022.naacl-main.435/)<br>[解读与来源](../topics/validation-and-comparability.md#luu-2022-temporal-misalignment) | 支持文本测量按时间外推单独验证，并把模型更新与跨期可比性问题纳入设计。 |
| 2021 · EMNLP Findings · Findings | [Temporal Adaptation of BERT and Performance on Downstream Document Classification: Insights from Social Media](https://aclanthology.org/2021.findings-emnlp.206/)<br>[解读与来源](../topics/validation-and-comparability.md#rottger-2021-temporal-adaptation) | 为纵向文本测量提供直接提醒：识别语言变化与维持分类可比性不是同一问题，应使用时间划分的任务验证。 |
| 2024 · NLP+CSS · Workshop | [Knowledge Distillation in Automated Annotation: Supervised Text Classification with LLM-Generated Training Labels](https://aclanthology.org/2024.nlpcss-1.9/)<br>[解读与来源](../topics/annotation-and-judgment.md#pangakis-2024-annotation-distillation) | 紧贴从自动标注到可规模化文本变量的流程，也能帮助区分教师标签质量和学生分类器表现。 |
