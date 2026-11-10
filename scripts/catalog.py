"""Validate and render the catalog using only the Python standard library."""
from __future__ import annotations
import argparse
from collections import Counter
import csv
from datetime import date, datetime
import html
import io
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
NOTICE = '<!-- Generated from data/papers.json by scripts/catalog.py. Do not edit directly. -->\n\n'
TOPICS = {
    'construct-operationalization': ('构念定义与操作化', '把理论构念转成可辨认的文本证据，明确包含条件、排除条件和观察单位。'),
    'annotation-and-judgment': ('文本标注与人工判断', '比较教师标签、独立人工判断及分歧来源，区分复制教师和测量目标构念。'),
    'synthetic-data-and-adaptation': ('合成数据与小模型适配', '比较合成与真实标注、蒸馏与少样本学习，以及错误反馈带来的收益与偏差。'),
    'validation-and-comparability': ('测量验证与可比性', '用独立真实文本、边界案例和跨情境评价检查效度、漂移与可比性。'),
    'measurement-error-and-inference': ('测量误差与下游推断', '研究生成变量的误分类、聚合误差及其对估计和不确定性的影响。'),
    'human-ai-workflows': ('人机协作与使用条件', '说明人类判断、解释与验证报告如何进入工作流，并评价成本、适当依赖和可复用性。'),
}
COLLECTIONS = {'main':'主目录', 'supplement':'补充', 'pending':'待核验'}
TRACKS = {'journal':'期刊', 'main':'主会', 'findings':'Findings', 'industry':'Industry', 'demo':'System Demonstrations', 'workshop':'Workshop', 'preprint':'预印本'}
TYPES = {'journal-article':'期刊研究', 'conference-paper':'会议论文', 'review':'综述', 'perspective':'观点／方法评论', 'preprint':'预印本／工作论文'}
LEVELS = {'abstract':'摘要', 'selected-full-text':'部分正文', 'full-text':'全文', 'metadata-only':'仅书目'}

def normalized_title(value):
    return ''.join(c for c in unicodedata.normalize('NFKD', value).casefold() if c.isalnum())

def normalized_doi(value):
    return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', (value or '').strip(), flags=re.I).casefold().rstrip('/')

def normalized_arxiv(value):
    match = re.search(r'(\d{4}\.\d{4,5})(?:v\d+)?', value or '')
    return match[1] if match else (value or '').strip().casefold()

def valid_url(value):
    return isinstance(value, str) and urlsplit(value).scheme in {'https','http'} and bool(urlsplit(value).netloc) and not re.search(r'\s',value)

def validate(data):
    errors=[]
    today=datetime.now(ZoneInfo('Asia/Hong_Kong')).date()
    def fail(message): errors.append(message)
    def check_date(value,label,required=True):
        if value is None and not required: return
        try:
            parsed=date.fromisoformat(value)
            if parsed>today: fail(label+': future date')
            if parsed.isoformat()!=value: fail(label+': non-ISO date')
        except (ValueError,TypeError): fail(label+': invalid date')
    if data.get('schema_version')!=1: fail('unsupported schema_version')
    check_date(data.get('snapshot_date'),'snapshot_date')
    papers=data.get('papers',[])
    if not isinstance(papers,list) or not papers: return errors+['papers must be a nonempty list']
    seen={name:{} for name in ['id','DOI','arXiv','title','URL','seed']}
    required=['id','title','authors','authors_complete','year','venue','publication_type','track','publication_status',
              'collection','primary_topic','topics','discipline','summary_zh','relevance_zh','limitations_zh',
              'evidence_level','verified_on','official_url','paper_url','doi','arxiv_id','sources','seed_numbers','discovered_via']
    def unique(kind,key,pid):
        if not key: return
        if key in seen[kind]: fail(f'{pid}: duplicate {kind} with {seen[kind][key]}')
        seen[kind][key]=pid
    for p in papers:
        pid=p.get('id','<missing>')
        for key in required:
            if key not in p: fail(f'{pid}: missing {key}')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',pid): fail(f'{pid}: invalid id')
        unique('id',pid,pid)
        unique('title',normalized_title(p.get('title','')),pid)
        unique('DOI',normalized_doi(p.get('doi')),pid)
        unique('arXiv',normalized_arxiv(p.get('arxiv_id')),pid)
        unique('URL',(p.get('paper_url') or '').rstrip('/'),pid)
        for seed in p.get('seed_numbers',[]): unique('seed',seed,pid)
        for key in ['title','venue','summary_zh','relevance_zh','limitations_zh']:
            if not isinstance(p.get(key),str) or not p[key].strip(): fail(f'{pid}: empty {key}')
        if p.get('collection') not in COLLECTIONS: fail(f'{pid}: invalid collection')
        if p.get('track') not in TRACKS: fail(f'{pid}: invalid track')
        if p.get('publication_type') not in TYPES: fail(f'{pid}: invalid publication_type')
        if p.get('publication_status') not in {'published','accepted','preprint','unknown'}: fail(f'{pid}: invalid publication_status')
        if p.get('evidence_level') not in LEVELS: fail(f'{pid}: invalid evidence_level')
        if not isinstance(p.get('authors'),list) or any(not isinstance(a,str) or not a.strip() for a in p.get('authors',[])): fail(f'{pid}: invalid authors')
        if not isinstance(p.get('authors_complete'),bool): fail(f'{pid}: invalid authors_complete')
        topics=p.get('topics',[])
        if not topics or len(topics)!=len(set(topics)) or any(t not in TOPICS for t in topics): fail(f'{pid}: invalid topics')
        if p.get('primary_topic') not in topics or p.get('primary_topic') not in TOPICS: fail(f'{pid}: invalid primary topic')
        if not p.get('discipline') or any(d not in {'is','cs','marketing','social-science','statistics','economics','hci'} for d in p.get('discipline',[])): fail(f'{pid}: invalid discipline')
        year=p.get('year')
        if year is not None and (type(year)!=int or not 1900<=year<=today.year): fail(f'{pid}: invalid year')
        included=p.get('collection')!='pending'
        check_date(p.get('verified_on'),pid+': verified_on',required=included)
        if included and (not p.get('authors') or year is None or p.get('evidence_level')=='metadata-only'): fail(f'{pid}: included record needs authors, year and content evidence')
        if included and not valid_url(p.get('official_url')): fail(f'{pid}: missing official URL')
        if not valid_url(p.get('paper_url')): fail(f'{pid}: invalid paper URL')
        if p.get('collection')=='main' and p.get('publication_status') not in {'published','accepted'}: fail(f'{pid}: main requires published or officially accepted status')
        if p.get('collection')=='main' and p.get('track') in {'workshop','preprint'}: fail(f'{pid}: workshop/preprint belongs in supplement')
        if p.get('publication_status')=='preprint' and p.get('track')!='preprint': fail(f'{pid}: inconsistent preprint track')
        sources=p.get('sources',[])
        if included and not sources: fail(f'{pid}: missing sources')
        if p.get('publication_status') in {'published','accepted'} and not any(s.get('purpose')=='publication' for s in sources): fail(f'{pid}: missing publication source')
        for s in sources:
            if not valid_url(s.get('url')) or s.get('purpose') not in {'publication','content','metadata'} or not s.get('note_zh'): fail(f'{pid}: invalid source')
            check_date(s.get('checked_on'),pid+': source date')
        for key,value in p.get('publication_dates',{}).items():
            if value is not None and key.endswith('_date'): check_date(value,pid+': '+key)
        if p.get('doi') and not re.fullmatch(r'10\.\d{4,9}/\S+',normalized_doi(p['doi'])): fail(f'{pid}: invalid DOI')
        if not p.get('discovered_via') or any(v not in {'seed','web','edith','existing-repo'} for v in p.get('discovered_via',[])): fail(f'{pid}: invalid discovery source')
        for other in p.get('related_repos',[]):
            if not other.get('repo') or not other.get('id') or not valid_url(other.get('url')): fail(f'{pid}: invalid cross-repo reference')
    ids=set(seen['id'])
    included_ids={p['id'] for p in papers if p['collection']!='pending'}
    for r in data.get('reading_routes',[]):
        if not re.fullmatch(r'[a-z0-9-]+',r.get('id','')): fail('invalid reading route id')
        if len(r.get('paper_ids',[]))!=len(set(r.get('paper_ids',[]))): fail('duplicate reading route reference')
        for pid in r.get('paper_ids',[]):
            if pid not in included_ids: fail(f'reading route {r.get("id")}: unknown paper or pending {pid}')
    nums=[]
    for c in data.get('candidates',[]):
        nums.append(c.get('number'))
        if any(t not in TOPICS for t in c.get('topics',[])): fail('candidate: unknown topic')
        for pid in c.get('paper_ids',[]):
            if pid not in included_ids: fail(f'candidate: unknown paper or pending {pid}')
    if len(nums)!=len(set(nums)): fail('duplicate candidate number')
    search=data.get('search_summary',{})
    if search.get('edith_status')!='success': fail('EDITH search not complete')
    if search.get('edith_included_count')!=sum('edith' in p['discovered_via'] for p in papers if p['collection']!='pending'): fail('EDITH included count mismatch')
    if re.search(r'/Users/|codex://threads/|papers_raw/|literature\.db',json.dumps(data,ensure_ascii=False)): fail('private material in public data')
    return errors

def label(p):
    status=' · 官方已接收' if p['publication_status']=='accepted' else ''
    return f"{p.get('year') or '年份待核验'} · {p['venue']} · {TRACKS[p['track']]}"+status

def escape(text):
    return str(text).replace('|','\\|').replace('\n',' ')

def detail_link(p,prefix='../'):
    if p['collection']=='pending': return prefix+'docs/pending.md#'+p['id']
    return prefix+'topics/'+p['primary_topic']+'.md#'+p['id']

def table(papers,prefix='../'):
    lines=['| 年份 / 来源 | 论文 | 阅读价值 |','| --- | --- | --- |']
    for p in papers:
        url=p.get('official_url') or p['paper_url']
        lines.append(f"| {escape(label(p))} | [{escape(p['title'])}]({url})<br>[解读与来源]({detail_link(p,prefix)}) | {escape(p['relevance_zh'])} |")
    return '\n'.join(lines)+'\n'

def detail(p):
    out=[f'<a id="{p["id"]}"></a>',f'### {p["title"]}', '',
         f"**{label(p)}** · {TYPES[p['publication_type']]} · {COLLECTIONS[p['collection']]}", '',
         '**作者：** '+('; '.join(p['authors']) or '待核验')+('' if p['authors_complete'] else '（名单尚未完整核验）'), '',
         '**研究内容：** '+p['summary_zh'], '', '**为什么读：** '+p['relevance_zh'], '',
         '**适用条件与限制：** '+p['limitations_zh'], '',
         f"**本轮证据：** {LEVELS[p['evidence_level']]}；核验日期 {p.get('verified_on') or '尚未完成'}。未独立复现实验。", '',
         '**来源：**', '']
    for s in p['sources']:
        out.append(f"- [{s['purpose']}]({s['url']})：{s['note_zh']}（{s['checked_on']}）")
    if not p['sources']: out.append(f"- [候选入口]({p['paper_url']})：尚无充分的本轮核验证据。")
    if p.get('publication_dates'):
        dates=p['publication_dates']
        names={'online_date':'首次在线','first_online':'首次在线','issue_year':'卷期年','date_note_zh':'日期说明','print_year':'卷期年','first_online_date':'首次在线','conference_year':'会议年','preprint_date':'预印本首发'}
        out+=['','**年份与版本说明：** '+'；'.join(f'{names.get(k,k)}：{v}' for k,v in dates.items() if v is not None)]
    if p.get('version_note_zh'):out+=['','**版本说明：** '+p['version_note_zh']]
    if p.get('related_repos'):
        out+=['','**其他目录：** '+' · '.join(f"[{r['repo']}]({r['url']})" for r in p['related_repos'])]
    out+=['','**主题：** '+' · '.join(TOPICS[t][0] for t in p['topics']),'']
    return '\n'.join(out)

def generate(data):
    papers=sorted(data['papers'],key=lambda p:(-(p.get('year') or 0),p['title'].casefold()))
    main=[p for p in papers if p['collection']=='main'];supp=[p for p in papers if p['collection']=='supplement'];pending=[p for p in papers if p['collection']=='pending']
    included=main+supp;byid={p['id']:p for p in papers};output={};search=data['search_summary']
    for topic,(name,description) in TOPICS.items():
        own=[p for p in papers if p['primary_topic']==topic and p['collection']!='pending']
        lines=[NOTICE+f'# {name}', '', '[返回目录](../README.md) · [阅读路线](../docs/reading-routes.md)', '',description,'']
        for collection in ['main','supplement']:
            group=[p for p in own if p['collection']==collection]
            lines += [f'## {COLLECTIONS[collection]}（{len(group)} 篇）','',table(group) if group else '暂无已核验收录。','']
            lines += [detail(p) for p in group]
        related=[p for p in included if topic in p['topics'] and p['primary_topic']!=topic]
        lines+=['## 跨主题阅读','',table(related) if related else '暂无其他主主题下的交叉条目。','']
        output[f'topics/{topic}.md']='\n'.join(lines)
    output['docs/supplementary.md']=NOTICE+'# 补充文献\n\n[返回目录](../README.md)\n\n已核验的预印本、工作论文、Workshop 与辅助背景；不计入主目录数。每条的用途与限制见主题详情。\n\n'+table(supp)
    output['docs/pending.md']=NOTICE+'# 待核验候选\n\n[返回目录](../README.md)\n\n以下记录不计入收录数，也不导出为正式参考文献。\n\n'+('\n'.join(detail(p) for p in pending) if pending else '本版无待核验目录条目；尚未深入筛查的检索线索见检索说明。\n')
    lines=[NOTICE+'# 建议阅读路线','','[返回目录](../README.md) · [研究地图](research-map.zh.md)','','顺序用于建立问题理解，不是论文质量排名。','']
    for r in data['reading_routes']:
        lines += [f'<a id="{r["id"]}"></a>',f'## {r["title"]}','',r['description_zh'],'']
        lines += [f"{i}. [{byid[pid]['title']}]({detail_link(byid[pid])}) — {byid[pid]['relevance_zh']}" for i,pid in enumerate(r['paper_ids'],1)]+['']
    output['docs/reading-routes.md']='\n'.join(lines)
    cs=[p for p in included if 'cs' in p['discipline']]
    lines=[NOTICE+'# CS Related Work','','[返回目录](../README.md) · [阅读路线](reading-routes.md)','','按标注、适配、验证组织计算机科学方法，直接比较其在研究测量中的作用。正式会议、Findings、Industry、Demo、Workshop 和预印本逐条标注；本页不新增或重复计数。','']
    for topic,(name,_) in TOPICS.items():
        group=[p for p in cs if p['primary_topic']==topic]
        if group:lines += ['## '+name,'',table(group),'']
    output['docs/cs-related-work.md']='\n'.join(lines)
    lines=[NOTICE+'# 研究候选与文献的对应','','[返回目录](../README.md)','','保留20个探索方向，不以排列顺序选定主方向。下列文献用于检验已有解释与研究设计，不证明候选具有新颖性或贡献。','','| 候选问题 | 主题入口 | 起点文献 |','| --- | --- | --- |']
    for c in data['candidates']:
        topics=' · '.join(f'[{TOPICS[t][0]}](../topics/{t}.md)' for t in c['topics'])
        refs='<br>'.join(f"[{byid[pid]['title']}]({detail_link(byid[pid])})" for pid in c['paper_ids'])
        lines.append(f"| {c['number']}. {c['title']} | {topics} | {refs} |")
    output['docs/candidate-map.md']='\n'.join(lines)+'\n'
    overlaps=[p for p in included if p.get('related_repos')]
    lines=[NOTICE+'# 与现有目录的关系','','[返回目录](../README.md)','','本目录围绕构念、文本编码和测量验证组织文献；LLM统计目录侧重统计与因果方法，量化目录要求直接投资决策贡献，科研Agent目录侧重科研系统，Science of Science目录侧重科研行为与制度。允许同一论文服务于不同阅读问题。', '',f'本轮直接识别到 **{len(overlaps)} 篇已收录研究** 同时出现在其他目录。按DOI、arXiv ID、规范化标题匹配并检查版本；未直接匹配不等于主题不重叠。','','| 本目录条目 | 其他目录与稳定 ID |','| --- | --- |']
    for p in overlaps:
        links='<br>'.join(f"[{r['repo']} · {r['id']}]({r['url']})" for r in p['related_repos'])
        lines.append(f"| [{p['title']}]({detail_link(p)}) | {links} |")
    lines+=['','核对范围：四个现有仓库的主数据，另含LLM统计补充／待核验清单及量化金融期刊watchlist；以本次本机快照为准，未改变旧仓库的收录边界。','']
    output['docs/related-repositories.md']='\n'.join(lines)
    years=[p['year'] for p in included]
    lines=[NOTICE+'<div align="center">','','# Text Measurement Papers','','研究定义驱动的文本变量构建与测量验证','','Constructs → Text Variables → Measurement Validation', '',f'**{len(main)} 篇主目录 · {len(supp)} 篇补充 · {len(pending)} 条待核验 · 基线检索日期 {data["snapshot_date"]}**','','</div>','','## Scope','','围绕研究者给定的构念定义、编码规则和文本语料，整理从标注与小模型适配到独立验证及下游推断的方法。面向IS、营销与社会科学实证研究者，保留专门的CS方法入口。', '',f'优先关注2022年以来的方法，并保留必要的早期测量基础；当前已收录年份为 **{min(years)}–{max(years)}**。期刊按首次正式在线发表年归档，卷期差异在条目中说明；会议按会议年。', '',
        '**纳入：** 构念操作化、文本标注与分歧、合成训练和轻量适配、测量效度与等值、误分类修正、与测量任务直接相关的人机协作。正式期刊、主会、Findings、Industry及Demo可进主目录；官方已接收稿单独标明状态。Workshop、预印本／工作论文与辅助背景单列补充，证据不足单列待核验。', '',
        '**排除：** 仅展示通用预测性能、模型压缩或分类榜单且无法说明测量相关性的研究；普通AI采用效果、完整科研Agent系统和无方法贡献的应用。金融或ESG文本只是可用场景，不作为独立收录理由。', '',
        '后续定向增补见主数据incremental_updates及逐篇核验日期，不代表全库重新核验。精选文献目录，不声称系统综述或完整venue-year覆盖。仅发布元数据、原创短评与来源链接；阅读摘要、部分正文和全文分别记录，未独立复现实验。','','## At a Glance','','| 统计口径 | 数量 |','| --- | ---: |',f'| 主目录 | {len(main)} |',f'| 补充 | {len(supp)} |',f'| 待核验（不计入收录） | {len(pending)} |',f'| 去重收录总数 | {len(included)} |',f'| EDITH基线检索返回的唯一库记录 | {search["unique_returned_hits"]} |',f'| EDITH命中后累计收录的研究 | {search["edith_included_count"]} |','','## How to Use','','- [中文研究地图](docs/research-map.zh.md) · [建议阅读路线](docs/reading-routes.md)','- [CS Related Work](docs/cs-related-work.md) · [20个研究候选与文献对应](docs/candidate-map.md)','- [补充文献](docs/supplementary.md) · [待核验候选](docs/pending.md) · [与现有repos的关系](docs/related-repositories.md)','- [来源与检索边界](docs/sources.md) · [数据字段](docs/metadata.md)','- [JSON主数据](data/papers.json) · [CSV](exports/papers.csv) · [BibTeX](exports/references.bib)','','## Browse by Topic','','每篇仅有一个主展示主题，以下主目录与补充数分别可相加；交叉标签和阅读路线不重复计数。','','| 研究主题 | 主目录 | 补充 |','| --- | ---: | ---: |']
    for topic,(name,_) in TOPICS.items():lines.append(f'| [{name}](topics/{topic}.md) | {sum(p["primary_topic"]==topic for p in main)} | {sum(p["primary_topic"]==topic for p in supp)} |')
    lines+=['','## Paper Index','','主目录简表；完整作者、方法、适用条件和本轮核验来源在主题详情中。','']
    for topic,(name,_) in TOPICS.items():lines+=['### '+name,'',table([p for p in main if p['primary_topic']==topic],prefix=''),'']
    lines+=['## Sources and Known Gaps','',f'本轮EDITH检索成功：{search["query_count"]}个查询，合计{search["summed_query_hits"]}次命中，返回{search["unique_returned_hits"]}条唯一库记录；其中{search["truncated_queries"]}个宽查询有返回上限。命中不自动证明发表或贡献，最终按官方来源与研究范围筛选。', '',
        '种子引用已逐条筛选；部分出版页受访问限制时，通过作者原稿、机构存档及出版注册信息交叉核对并记录证据层次。宽查询之外未全量筛查、后续版本变化及语言／领域代表性仍是缺口。具体查询与未收录理由见[来源说明](docs/sources.md)。','','## Contributing','','编辑唯一主数据后生成并检查：','','```sh','python3 scripts/catalog.py --write','python3 scripts/catalog.py --check','python3 -m unittest discover -s tests -v','git diff --check','```','','使用Python 3.9或以上，无第三方运行依赖。详见[维护说明](CONTRIBUTING.md)。','','## Acknowledgements and License','','主要参考 [good_llm_stats_papers](https://github.com/sjsj0101/good_llm_stats_papers) 的章节、中文导读、主题导航和引用导出；采用单一JSON与标准库生成器，按本主题重新制定年份与track边界。原创目录说明适用[CC BY 4.0](LICENSE)；外链论文、代码和数据遵循各自许可。','']
    output['README.md']='\n'.join(lines)
    columns=['id','title','authors','year','venue','publication_type','track','publication_status','collection','primary_topic','topics','summary_zh','relevance_zh','limitations_zh','doi','arxiv_id','official_url','verified_on','evidence_level']
    stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=columns,lineterminator='\n');writer.writeheader()
    for p in included:writer.writerow({k:'; '.join(p[k]) if isinstance(p.get(k),list) else p.get(k) for k in columns})
    output['exports/papers.csv']='\ufeff'+stream.getvalue()
    def tex(value):
        replacements={'\\':'\\textbackslash{}','&':'\\&','%':'\\%','_':'\\_','#':'\\#','{':'\\{','}':'\\}','~':'\\textasciitilde{}','^':'\\textasciicircum{}'}
        return ''.join(replacements.get(c,c) for c in str(value))
    bib=[]
    for p in included:
        entry='misc' if p['publication_status']=='preprint' else ('inproceedings' if p['track'] in {'main','findings','industry','demo','workshop'} else 'article')
        fields={'title':'{'+tex(p['title'])+'}','author':' and '.join(tex(a) for a in p['authors']),'year':str(p['year']), 'url':p['official_url'], 'note':tex(COLLECTIONS[p['collection']]+'; '+TRACKS[p['track']]+'; '+p['publication_status'])}
        fields['booktitle' if entry=='inproceedings' else 'journal' if entry=='article' else 'howpublished']=tex(p['venue'])
        if p.get('doi'):fields['doi']=p['doi']
        if p.get('arxiv_id'):fields.update(eprint=p['arxiv_id'],archivePrefix='arXiv')
        bib.append('@'+entry+'{'+p['id']+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}\n')
    output['exports/references.bib']='\n'.join(bib)
    return {name: text.rstrip()+'\n' for name, text in output.items()}

def write_outputs(root,outputs):
    for name,text in outputs.items():
        p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')

def check_outputs(root,outputs):
    stale=[name for name,text in outputs.items() if not (root/name).is_file() or (root/name).read_text(encoding='utf-8')!=text]
    for directory in ['topics','exports']:
        for p in (root/directory).glob('*'):
            if p.is_file() and str(p.relative_to(root)) not in outputs:stale.append(str(p.relative_to(root)))
    return stale

def anchors(text):
    found=set(re.findall(r'<a\s+id="([^"]+)"',text))
    for heading in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        found.add(re.sub(r'[^\w\-\s]','',heading.lower()).replace(' ','-'))
    return found

def check_links(root):
    errors=[]
    for path in root.rglob('*.md'):
        if '.git' in path.parts or path.name=='HANDOFF.md':continue
        text=path.read_text()
        for target in re.findall(r'\]\(([^\s]+?)\)',text):
            if urlsplit(target).scheme or target.startswith('//'):continue
            rel,_,anchor=unquote(target).partition('#');dest=path.parent/rel if rel else path
            if not dest.exists():errors.append(f'{path.relative_to(root)}: missing file {target}')
            elif anchor and dest.suffix=='.md' and anchor not in anchors(dest.read_text()):errors.append(f'{path.relative_to(root)}: missing anchor {target}')
    return errors

def main():
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group(required=True);group.add_argument('--write',action='store_true');group.add_argument('--check',action='store_true');args=parser.parse_args()
    data=json.loads((ROOT/'data/papers.json').read_text());errors=validate(data)
    if errors:raise SystemExit('\n'.join(errors))
    outputs=generate(data)
    if args.write:write_outputs(ROOT,outputs)
    else:errors+=['Out of date: '+p for p in check_outputs(ROOT,outputs)]
    errors+=check_links(ROOT)
    for path in [ROOT/'README.md',ROOT/'CONTRIBUTING.md',*ROOT.glob('docs/*.md'),*ROOT.glob('topics/*.md')]:
        if path.exists() and re.search(r'/Users/|codex://threads/|papers_raw/|literature\.db',path.read_text()):errors.append('Private material: '+str(path.relative_to(ROOT)))
    if errors:raise SystemExit('\n'.join(errors))
    print(json.dumps({'status':'passed','action':'write' if args.write else 'check','collections':dict(Counter(p['collection'] for p in data['papers'])),'generated_files':len(outputs),'candidates':len(data['candidates']),'snapshot_date':data['snapshot_date']},ensure_ascii=False))

if __name__=='__main__':main()
