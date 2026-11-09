<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->

# 人机协作与使用条件

[返回目录](../README.md) · [阅读路线](../docs/reading-routes.md)

说明人类判断、解释与验证报告如何进入工作流，并评价成本、适当依赖和可复用性。

## 主目录（2 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2025 · ACL Findings · Findings | [Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks](https://aclanthology.org/2025.findings-acl.1323/)<br>[解读与来源](../topics/human-ai-workflows.md#schroeder-2025-human-loop-annotation) | 直接说明人工复核未必形成独立的测量标准，适合设计盲审、独立金标准和避免评估循环的工作流。 |
| 2023 · Management Science · 期刊 | [Reciprocal Human-Machine Learning: A Theory and an Instantiation for the Case of Message Classification](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03518)<br>[解读与来源](../topics/human-ai-workflows.md#teeni-2023-reciprocal-learning) | 将专家概念化、模型分类与反馈修订置于同一流程，可用于理解人工判断如何参与测量工具开发。 |


<a id="schroeder-2025-human-loop-annotation"></a>
### Just Put a Human in the Loop? Investigating LLM-Assisted Annotation for Subjective Tasks

**2025 · ACL Findings · Findings** · 会议论文 · 主目录

**作者：** Hope Schroeder; Deb Roy; Jad Kabbara

**研究内容：** 预注册实验考察主观任务中展示 LLM 标注建议的后果。作者发现标注者会明显接受建议，改变标签分布；以这些经人工确认的标签评测模型时，模型成绩也会随之改变。

**为什么读：** 直接说明人工复核未必形成独立的测量标准，适合设计盲审、独立金标准和避免评估循环的工作流。

**适用条件与限制：** 结论受实验任务、模型和建议呈现方式约束，不能推为所有人机协作都无效；研究强调的是参照标签可能受辅助系统影响。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://aclanthology.org/2025.findings-acl.1323/)：已访问官方页面，核对题名、作者、年份、发表身份与摘要。（2026-11-09）

**主题：** 人机协作与使用条件 · 文本标注与人工判断 · 测量验证与可比性

<a id="teeni-2023-reciprocal-learning"></a>
### Reciprocal Human-Machine Learning: A Theory and an Instantiation for the Case of Message Classification

**2023 · Management Science · 期刊** · 期刊研究 · 主目录

**作者：** Dov Te’eni; Inbal Yahav; Alexely Zagalsky; David Schwartz; Gahl Silverman; Daniel Cohen; Yossi Mann; Dafna Lewinsky

**研究内容：** 提出人和机器围绕文本分类循环交换反馈、修订知识表示的学习配置，并以 Fusion 系统和网络安全论坛案例考察双方学习。

**为什么读：** 将专家概念化、模型分类与反馈修订置于同一流程，可用于理解人工判断如何参与测量工具开发。

**适用条件与限制：** 证据来自特定论坛任务及有限学习轮次；共同学习不等于标签获得独立验证，也不能保证任意任务的人机协作都更好。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03518)：已访问官方出版记录并核读摘要；未声称复现实验。 首次 online 2023-11-14；2026 是卷期年份。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.1287/mnsc.2022.03518)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 人机协作与使用条件 · 文本标注与人工判断 · 构念定义与操作化

## 补充（4 篇）

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2021 · Proceedings of the ACM on Human-Computer Interaction · 期刊 | [To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making](https://doi.org/10.1145/3449287)<br>[解读与来源](../topics/human-ai-workflows.md#bucinca-2021-cognitive-forcing) | 为文本测量报告和人工复核流程提供辅助设计背景：解释的存在与用户是否核查证据应分别评价。 |
| 2016 · CHI · 主会 | [How Much Information? Effects of Transparency on Trust in an Algorithmic Interface](https://doi.org/10.1145/2858036.2858402)<br>[解读与来源](../topics/human-ai-workflows.md#kizilcec-2016-transparency-trust) | 为测量验证报告提供辅助阅读：报告应说明有助于判断用途的信息，并独立检验理解与正确使用。 |
| 2007 · Information Systems Research · 期刊 | [Decision-Centric Active Learning of Binary-Outcome Models](https://pubsonline.informs.org/doi/10.1287/isre.1070.0111)<br>[解读与来源](../topics/human-ai-workflows.md#saar-tsechansky-2007-decision-centric) | 作为补充方法背景，提醒有限标注预算的分配应围绕实际研究或决策目标，而非只追求统一准确率。 |
| 2007 · Journal of Management Information Systems · 期刊 | [Recommendation Agents for Electronic Commerce: Effects of Explanation Facilities on Trusting Beliefs](https://doi.org/10.2753/MIS0742-1222230410)<br>[解读与来源](../topics/human-ai-workflows.md#wang-2007-explanation-trusting-beliefs) | 作为验证报告设计的辅助背景，提示分别衡量解释带来的信任与研究者实际识别错误的能力。 |


<a id="bucinca-2021-cognitive-forcing"></a>
### To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making

**2021 · Proceedings of the ACM on Human-Computer Interaction · 期刊** · 期刊研究 · 补充

**作者：** Zana Buçinca; Maja Barbara Malaya; Krzysztof Z. Gajos

**研究内容：** 比较促使用户主动思考的交互干预与直接解释，在受测决策任务中考察对错误AI建议的依赖及使用体验。

**为什么读：** 为文本测量报告和人工复核流程提供辅助设计背景：解释的存在与用户是否核查证据应分别评价。

**适用条件与限制：** 受测决策任务不是研究者的文本编码或构念判断；降低依赖伴随体验成本，不能直接推断专业研究场景的净收益。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://scholar.harvard.edu/files/zbucinca/files/bucinca2021trust.pdf)：检索工具读取作者机构所存排印稿的标题与正文索引，含PACMHCI 5(CSCW1)、Article188及April2021页脚；直接打开超时，ACM入口403。（2026-11-09）
- [content](https://arxiv.org/abs/2102.09692)：本轮读取作者预印本摘要，支持干预比较与适用边界。（2026-11-09）

**主题：** 人机协作与使用条件

<a id="kizilcec-2016-transparency-trust"></a>
### How Much Information? Effects of Transparency on Trust in an Algorithmic Interface

**2016 · CHI · 主会** · 会议论文 · 补充

**作者：** René F. Kizilcec

**研究内容：** 在同伴评分场景比较不同程度的算法透明度，考察解释信息与期望落差如何共同影响信任。

**为什么读：** 为测量验证报告提供辅助阅读：报告应说明有助于判断用途的信息，并独立检验理解与正确使用。

**适用条件与限制：** 研究围绕教育评分系统的信任，并非测量效度或研究者审计表现；更多透明信息是否改善判断需要在新任务中验证。

**本轮证据：** 部分正文；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://rene.kizilcec.com/wp-content/uploads/2016/01/kizilcec2016information.pdf)：读取作者保存的正式CHI排印稿摘要、首页会议与DOI、研究设计部分。（2026-11-09）

**主题：** 人机协作与使用条件

<a id="saar-tsechansky-2007-decision-centric"></a>
### Decision-Centric Active Learning of Binary-Outcome Models

**2007 · Information Systems Research · 期刊** · 期刊研究 · 补充

**作者：** Maytal Saar-Tsechansky; Foster Provost

**研究内容：** 将主动数据获取的目标从降低预测误差转向改善最终决策，利用直接营销数据比较不同获取策略，并考虑获取成本和效用估计质量。

**为什么读：** 作为补充方法背景，提醒有限标注预算的分配应围绕实际研究或决策目标，而非只追求统一准确率。

**适用条件与限制：** 一般二元决策和主动学习研究，未直接建立文本构念或推断校正方法；决策效用的估计与应用语境是其边界。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://pubsonline.informs.org/doi/10.1287/isre.1070.0111)：已访问官方出版记录并核读摘要；未声称复现实验。（2026-11-09）
- [metadata](https://api.crossref.org/works/10.1287/isre.1070.0111)：实际读取 Crossref 官方注册记录，用于核对 DOI、题名、作者及发表日期；未作为全文阅读证据。（2026-11-09）

**主题：** 人机协作与使用条件 · 文本标注与人工判断

<a id="wang-2007-explanation-trusting-beliefs"></a>
### Recommendation Agents for Electronic Commerce: Effects of Explanation Facilities on Trusting Beliefs

**2007 · Journal of Management Information Systems · 期刊** · 期刊研究 · 补充

**作者：** Weiquan Wang; Izak Benbasat

**研究内容：** 在推荐代理实验中比较不同解释设施，研究它们对能力、善意与正直等初始信任判断的影响。

**为什么读：** 作为验证报告设计的辅助背景，提示分别衡量解释带来的信任与研究者实际识别错误的能力。

**适用条件与限制：** 研究对象是消费者与推荐代理的初始信任，未检验文本变量质量、专业编码或下游推断；不作为测量工具有效性的直接证据。

**本轮证据：** 摘要；核验日期 2026-11-09。未独立复现实验。

**来源：**

- [publication](https://jmis-web.org/articles/1020)：期刊官方页明确23(4)、2007、217–246并提供摘要。（2026-11-09）
- [metadata](https://www.tandfonline.com/doi/abs/10.2753/MIS0742-1222230410)：当前承载页显示2014上线日期，但期刊原卷期为2007；不将后续数字化日期作为首发年。（2026-11-09）

**年份与版本说明：** 卷期年：2007；日期说明：当前出版社平台2014上线晚于原刊2007，采用原刊年份。

**主题：** 人机协作与使用条件

## 跨主题阅读

| 年份 / 来源 | 论文 | 阅读价值 |
| --- | --- | --- |
| 2026 · MIS Quarterly · 期刊 | [AI-Augmented Content Validation in Behavioral Research: Development and Evaluation of the RATER System](https://aisel.aisnet.org/misq/vol50/iss1/7/)<br>[解读与来源](../topics/construct-operationalization.md#pillet-2026-rater) | 直接对应构念定义与语言表述之间的内容效度检验，可为文本测量的操作化设计提供参照。 |
| 2025 · MIS Quarterly · 期刊 | [Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning](https://aisel.aisnet.org/misq/vol49/iss3/12/)<br>[解读与来源](../topics/annotation-and-judgment.md#liu-2025-fastsr) | 为高专业知识、少量标签场景的文本变量提取提供专家参与和多任务设计案例。 |
| 2018 · MIS Quarterly · 期刊 | [Text Analytics to Support Sense-Making in Social Media: A Language-Action Perspective](https://aisel.aisnet.org/misq/vol42/iss2/6/)<br>[解读与来源](../topics/construct-operationalization.md#abbasi-2018-language-action) | 说明应依据理论明确文本要表达的行动或意图维度，再设计特征及验证任务，超越单纯词义归类。 |
