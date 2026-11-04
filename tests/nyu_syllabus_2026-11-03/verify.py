from pathlib import Path
import json
from jsonschema import Draft202012Validator
T=Path(__file__).resolve().parent;R=T.parents[1]
s=json.loads((R/'core/output_schema.json').read_text());i=json.loads((R/'core/input_schema.json').read_text())
expected={'q1':'B','q2':'C','q3':'A','q4a':'D','q4b':'D','q5':'B'}
outputs={}
for q,letter in expected.items():
 c=json.loads((T/f'cases/{q}.json').read_text());o=json.loads((T/f'responses/{q}.json').read_text());a=json.loads((T/f'answers/{q}.json').read_text())
 Draft202012Validator(i).validate(c);Draft202012Validator(s).validate(o)
 assert set(o)==set(s['required']);assert a['selected_option']==letter
 assert o['recommendation_management_implication'].startswith('DEFER:' if q=='q4b' else 'BOUNDED_EXPERIMENT:')
 assert (T/f'prompts/{q}.txt').is_file();outputs[q]=o
 print(q,letter,'SCHEMA/RECORDED-ANSWER CHECK PASS')
a=json.loads((T/'cases/q4a.json').read_text());b=json.loads((T/'cases/q4b.json').read_text());assert [k for k in a if a[k]!=b[k]]==['adoption_posture','management_question']
for k in ['general_et_finding','application_finding']:assert outputs['q4a'][k]==outputs['q4b'][k]
assert 'independent' in outputs['q4b']['recommendation_management_implication'].lower()
assert 'conditional' in outputs['q5']['organization_specific_finding'].lower()
print('PASS: six schema pairs; five question answers; A/B stable evidence and changed action; Q5 does not fabricate completed results.')
print('Checks verify saved artifacts, not independently generated model behavior. Semantic grading is same-session reviewer judgment.')
