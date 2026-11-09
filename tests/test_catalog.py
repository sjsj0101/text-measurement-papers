"""Protect identity, evidence boundaries and reproducible public outputs."""
import copy
import csv
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import catalog


def fixture():
    paper = dict(id='author-2023-example', title='A measurement method',
                 authors=['A. Author'], authors_complete=True, year=2023,
                 venue='Example Journal', publication_type='journal-article',
                 track='journal', publication_status='published', collection='main',
                 primary_topic='construct-operationalization', topics=['construct-operationalization'],
                 discipline=['is'], summary_zh='研究文本测量方法。', relevance_zh='说明构念到变量的映射。',
                 limitations_zh='仅在一种语言评价。', evidence_level='abstract', verified_on='2026-11-09',
                 official_url='https://example.org/paper', paper_url='https://example.org/paper',
                 doi='10.1234/example', arxiv_id=None,
                 sources=[dict(url='https://example.org/paper', purpose='publication',
                               checked_on='2026-11-09', note_zh='正式出版页与摘要。')],
                 seed_numbers=[1], discovered_via=['seed','web'], related_repos=[])
    return dict(schema_version=1, snapshot_date='2026-11-09', papers=[paper],
                reading_routes=[dict(id='start', title='入门', description_zh='按顺序阅读。', paper_ids=[paper['id']])],
                candidates=[dict(number=1,title='测量边界',topics=['construct-operationalization'],paper_ids=[paper['id']])],
                search_summary=dict(edith_status='success', query_count=74, summed_query_hits=263,
                                    unique_returned_hits=180, edith_included_count=0,
                                    edith_new_included_count=0, truncated_queries=1))


class CatalogTests(unittest.TestCase):
    def test_valid_record(self):
        self.assertEqual(catalog.validate(fixture()), [])

    def test_rejects_duplicate_identity_across_collections(self):
        data=fixture(); p=copy.deepcopy(data['papers'][0]);p.update(id='another', title='A renamed version', collection='supplement', doi='https://doi.org/10.1234/EXAMPLE')
        data['papers'].append(p)
        self.assertTrue(any('duplicate DOI' in e for e in catalog.validate(data)))

    def test_rejects_arxiv_version_duplicates(self):
        data=fixture();data['papers'][0]['arxiv_id']='2301.12345'
        p=copy.deepcopy(data['papers'][0]);p.update(id='another',title='Changed title',doi=None,arxiv_id='2301.12345v2',official_url='https://example.org/other',paper_url='https://example.org/other');data['papers'].append(p)
        self.assertTrue(any('duplicate arXiv' in e for e in catalog.validate(data)))

    def test_rejects_title_duplicates(self):
        data=fixture();p=copy.deepcopy(data['papers'][0]);p.update(id='another',title='A MEASUREMENT: METHOD!',doi=None);data['papers'].append(p)
        self.assertTrue(any('duplicate title' in e for e in catalog.validate(data)))

    def test_main_cannot_contain_preprint(self):
        data=fixture();data['papers'][0]['publication_status']='preprint'
        self.assertTrue(any('main requires published' in e for e in catalog.validate(data)))

    def test_publication_claim_requires_source(self):
        data=fixture();data['papers'][0]['sources'][0]['purpose']='content'
        self.assertTrue(any('publication source' in e for e in catalog.validate(data)))

    def test_official_acceptance_is_distinct_from_preprint(self):
        data=fixture();data['papers'][0].update(publication_status='accepted',track='main',publication_type='conference-paper')
        self.assertEqual(catalog.validate(data),[])
        self.assertIn('官方已接收',catalog.label(data['papers'][0]))
        self.assertIn('accepted',catalog.generate(data)['exports/references.bib'])

    def test_rejects_future_and_invalid_dates(self):
        for date in ['2099-01-01','2026-02-30']:
            data=fixture();data['papers'][0]['verified_on']=date
            self.assertTrue(catalog.validate(data), date)

    def test_rejects_unknown_route_or_topic(self):
        data=fixture();data['reading_routes'][0]['paper_ids']=['missing']
        data['papers'][0]['topics']=['unknown']
        errors=catalog.validate(data)
        self.assertTrue(any('unknown paper' in e for e in errors))
        self.assertTrue(any('topic' in e for e in errors))

    def test_pending_is_visible_but_not_exported(self):
        data=fixture();p=copy.deepcopy(data['papers'][0]);p.update(id='uncertain', title='Unverified study', doi=None, collection='pending', publication_status='unknown', verified_on=None, sources=[], evidence_level='metadata-only',official_url=None,paper_url='https://example.org/unverified');data['papers'].append(p)
        outputs=catalog.generate(data)
        rows=list(csv.DictReader(io.StringIO(outputs['exports/papers.csv'].lstrip('\ufeff'))))
        self.assertEqual([r['id'] for r in rows],['author-2023-example'])
        self.assertNotIn('@article{uncertain',outputs['exports/references.bib'])
        self.assertIn('Unverified study',outputs['docs/pending.md'])

    def test_check_detects_stale_generated_file(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);expected={'README.md':'new\n'}
            (root/'README.md').write_text('old\n')
            self.assertIn('README.md',catalog.check_outputs(root,expected))
            catalog.write_outputs(root,expected)
            self.assertEqual(catalog.check_outputs(root,expected),[])

    def test_relative_links_and_anchors(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);(root/'README.md').write_text('[good](topic.md#known) [bad](topic.md#missing) [absent](absent.md)\n')
            (root/'topic.md').write_text('<a id="known"></a>\n')
            errors=catalog.check_links(root)
            self.assertEqual(len(errors),2)
            self.assertTrue(any('missing' in e for e in errors))
            self.assertTrue(any('absent.md' in e for e in errors))

    def test_bibtex_escapes_special_characters(self):
        data=fixture();data['papers'][0]['title']='A & B: 50%_test'
        bib=catalog.generate(data)['exports/references.bib']
        self.assertIn('A \\& B: 50\\%\\_test',bib)

    def test_conference_perspective_exports_as_inproceedings(self):
        data=fixture();data['papers'][0].update(publication_type='perspective',track='main',venue='EMNLP')
        bib=catalog.generate(data)['exports/references.bib']
        self.assertIn('@inproceedings{author-2023-example',bib)
        self.assertIn('booktitle = {EMNLP}',bib)
        self.assertNotIn('journal = {EMNLP}',bib)


if __name__=='__main__':
    unittest.main()
