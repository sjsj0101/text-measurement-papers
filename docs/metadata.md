# 数据字段与统计口径

[返回目录](../README.md) · [维护说明](../CONTRIBUTING.md)

`data/papers.json`是唯一主数据；`schema_version`为1。日期采用ISO格式，检索日期按Asia/Hong_Kong记录。

| 顶层字段 | 用途 |
| --- | --- |
| `snapshot_date` | 本轮检索与核验截止日，不表示所有venue-year已覆盖 |
| `papers` | 主目录、补充及待核验研究，一项研究只出现一次 |
| `reading_routes` | 用稳定ID组织有顺序的阅读路线 |
| `candidates` | 20个探索方向的主题和文献映射，不等于已确认贡献 |
| `search_summary` | 本轮EDITH查询、命中、返回、截断和最终收录统计 |

| 论文字段 | 含义与约束 |
| --- | --- |
| `id` | 稳定英文标识；历史年份出现在ID中时，不随书目修正而强制重命名 |
| `title`、`authors`、`authors_complete` | 原文题名、核验的作者顺序、作者是否完整；不猜补姓名 |
| `year`、`venue` | 正式首次在线年／会议年／预印本首发年和来源；无法确认年份时为null且待核验 |
| `publication_type` | `journal-article`、`conference-paper`、`review`、`perspective`、`preprint` |
| `track` | `journal`、`main`、`findings`、`industry`、`demo`、`workshop`、`preprint` |
| `publication_status` | `published`、`accepted`、`preprint`、`unknown`；accepted必须有官方证据 |
| `collection` | `main`、`supplement`、`pending`；独立于论文的发表状态 |
| `primary_topic`、`topics` | 一个主展示主题与多个交叉主题，见首页六主题 |
| `discipline` | `is`、`cs`、`marketing`、`social-science`、`statistics`、`economics`、`hci`，用于阅读入口 |
| `summary_zh`、`relevance_zh`、`limitations_zh` | 原创研究概要、本目录相关性与具体适用限制 |
| `evidence_level` | `abstract`、`selected-full-text`、`full-text`、`metadata-only`；仅书目不足以正式收录 |
| `official_url`、`paper_url` | 官方身份入口与论文阅读入口；可以不同 |
| `doi`、`arxiv_id` | 规范标识，未知为null；有正式版后保留预印本关联 |
| `verified_on` | 本轮真正核验的日期；尚未完成为null |
| `sources` | URL、用途`publication/content/metadata`、检查日期及原始来源/访问/版本说明 |
| `seed_numbers`、`discovered_via` | 初始种子对应编号与发现途径；发现途径不替代核验证据 |
| `related_repos` | 对方repo名、稳定ID与公开链接；不在本库再次计数 |
| `publication_dates`、`version_note_zh` | 可选的在线／卷期日期与版本冲突说明 |

主目录数只含`main`；总收录数为`main + supplement`；`pending`独立报告。CSV和BibTeX只导出已收录研究，两者均保留分层、track和发表状态；BibTeX在note中标明。每个主题页只保存其主归属论文的完整条目，其他主题通过链接关联。

校验器检查结构、受控值、唯一ID/DOI/arXiv/题名/主链接、日期、阅读引用、相对链接与锚点、统计与派生文件一致性。它不证明外部链接永远可访问，也不进行论文复现。
