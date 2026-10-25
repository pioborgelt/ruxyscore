#!/usr/bin/env python3
"""Check recorded JSON, local links and copied values; no scientific compute."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads(path.read_text())

def main():
    checked = 0
    for path in [*ROOT.glob('configs/**/*.json'), *ROOT.glob('results/**/*.json')]:
        read(path)
        checked += 1
    links = 0
    for path in [ROOT / 'README.md', *ROOT.glob('docs/*.md')]:
        content = path.read_text()
        targets = re.findall(r'\]\(([^\s)]+)', content)
        for href in targets:
            parsed = urlsplit(href)
            if parsed.scheme or href.startswith('#'):
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            assert target.is_relative_to(ROOT) and target.exists(), (str(path), href)
            links += 1
    result = read(ROOT / 'results/benchmark-v4.1.json')
    cells = read(ROOT / 'results/recorded-cells.json')['cells']
    panel = read(ROOT / 'configs/reference-panel-summary.json')
    assert result['version'] == 'mixed-bank-corrected-original-4.1'
    assert result['canonical_view'] == 'mixed-original-contract'
    assert panel['executable'] is False and panel['self_source_allowed'] is False
    assert len(result['profiles']) == 40 and len(result['matrix']) == 160
    assert len(cells) == 3228 and len({c['id'] for c in cells}) == len(cells)
    cell_ids = {c['id'] for c in cells}
    for p in result['profiles']:
        assert p['view'] == result['canonical_view']
        assert p['model'] not in p['source_pool']
        if p['model'] == panel['full_panel_target']:
            assert p['source_pool'] == panel['sources'] and p['panel_id'] == panel['full_panel_id']
        if p['model'] == 'qwen3_8b_int8':
            assert p['native'] is None and p['incoming'] is None and p['composite'] is None
        for v in p['native_tasks'].values():
            if v:
                assert set(v.get('cell_ids', [])).issubset(cell_ids)
    with (ROOT/'results/native-profiles.csv').open(newline='') as f:
        for row in csv.DictReader(f):
            p = next(p for p in result['profiles'] if p['model']==row['model']
                     and p['recipe']=='ridge' and p['fraction']==1 and p['calibration']=='target_CAL')
            assert float(row['native_points']) == p['native']['point']
            for t in result['config']['task_weights']:
                assert float(row[t]) == p['native_tasks'][t]['point']
    # File/metadata equality checks only: scientific verification is recorded from Colab.
    source = ROOT / '_private/imports/v4.1-2026-10-22/source'
    compared = False
    if source.is_dir():
        original = read(source/'benchmark/BENCHMARK.json')
        assert result['profiles'] == [p for p in original['profiles'] if p['view']==result['canonical_view']]
        assert result['matrix'] == [p for p in original['matrix'] if p['view']==result['canonical_view']]
        old_cells = {c['id']: c for c in original['cells']}
        for c in cells:
            old = old_cells[c['id']]
            for k,v in c.items():
                if k != 'ranking':
                    assert v == old[k], (c['id'], k)
            for a,b in [('legacy_probability','old'), ('corrected_original_v4_1','numeric'), ('relative_link_v4_0','primary')]:
                if a in c['ranking']:
                    assert c['ranking'][a] == old['ranking'][b], (c['id'], a)
        provenance = read(ROOT/'results/provenance.json')
        for name,w in provenance['source_receipts'].items():
            p = source/name
            assert p.stat().st_size == w['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest() == w['sha256'], name
        compared = True
    print(json.dumps({'passed': True, 'json_files_checked': checked, 'local_links_checked': links,
                      'canonical_profiles': len(result['profiles']),
                      'directed_matrix_rows': len(result['matrix']),
                      'recorded_cells': len(cells),
                      'copied_values_equal_source_reports': compared,
                      'new_model_runs_or_fits': 0}, indent=2))

if __name__ == '__main__':
    main()
