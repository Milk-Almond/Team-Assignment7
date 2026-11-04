from pathlib import Path
import json
from jsonschema import Draft202012Validator
T=Path(__file__).resolve().parent;R=T.parents[1]
o=json.loads((T/'nyu_program_b_reference.json').read_text())
Draft202012Validator(json.loads((R/'core/output_schema.json').read_text())).validate(o)
assert o['agent']['version']=='1.2-team-review'
assert o['recommendation_management_implication'].startswith('DEFER:')
assert 'monitoring' in o['recommendation_management_implication'].lower()
s=(R/'agents/adoption_agent/specialist_instructions.md').read_text()
assert 'pending external evidence, MONITOR is appropriate' not in s
assert 'Prefer when learning is not currently sponsored' not in s
print('PASS: NYU Program B remains DEFER; monitoring is supporting work; active conflicting clauses absent.')
print('Reference-fixture regression only; historical v1.1 qualified records remain valid for that version.')
