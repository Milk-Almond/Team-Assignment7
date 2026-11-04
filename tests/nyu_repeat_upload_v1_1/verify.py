from pathlib import Path
import json
from jsonschema import Draft202012Validator
T=Path(__file__).resolve().parent; R=T.parents[1]
o=json.loads((T/'response.json').read_text());c=json.loads((T/'case.json').read_text())
for f,obj in [('output_schema.json',o),('input_schema.json',c)]: Draft202012Validator(json.loads((R/'core'/f).read_text())).validate(obj)
assert set(o)==set(json.loads((R/'core/output_schema.json').read_text())['required'])
assert o['agent']['version']=='1.1-team-review'
a=json.loads((T/'answers.json').read_text());assert [x['answer'] for x in a]==['B','C','A','D','B']
assert 'Program B: DEFER' in o['recommendation_management_implication']
assert 'hypothetical evidence criterion' in o['value_opportunity_implication']
print('PASS: input/output schema; exact output fields; recorded B/C/A/D/B answers; B trial deferral; no fabricated Q5 outcomes.')
print('QUALIFIED: Q4 MONITOR/DEFER instruction conflict remains. Same-session, nonblind self-review; no independent performance claim.')
