from pathlib import Path
import json, subprocess,sys
from jsonschema import Draft202012Validator
R=Path(__file__).resolve().parents[1];A=R/'agents/adoption_agent'
def run(*a):subprocess.run([sys.executable,*a],cwd=R,check=True)
run('tools/check_frozen_core.py')
s=json.loads((R/'core/output_schema.json').read_text());i=json.loads((R/'core/input_schema.json').read_text());results={}
for c in sorted((A/'cases').glob('*.json')):
 Draft202012Validator(i).validate(json.loads(c.read_text()))
 r=A/'responses'/f'{c.stem}_response.json';o=json.loads(r.read_text());Draft202012Validator(s).validate(o)
 assert set(o)==set(s['required']);assert o['agent']['version']=='1.0-team-review'
 for k,v in o.items():assert v,(c.stem,k)
 run('tools/build_prompt.py','--agent','agents/adoption_agent','--case',str(c))
 run('tools/validate_response.py',str(r));results[c.stem]=o
p=json.loads((A/'cases/primary.json').read_text());c=json.loads((A/'cases/contrast_1.json').read_text())
assert [k for k in p if p[k]!=c[k]]==['adoption_posture']
for f in ['general_et_finding','application_finding']:assert results['primary'][f]==results['contrast_1'][f]
for k,v in {'primary':'BOUNDED_EXPERIMENT:','contrast_1':'MONITOR:','contrast_2':'DEFER:','qualified':'DEFER:'}.items():assert results[k]['recommendation_management_implication'].startswith(v)
def protocol(o):return all(t in o['recommendation_management_implication'].lower() for t in ['four-week','category manager','2000','30','20%','95%','stop','day 28'])
assert protocol(results['primary'])
w=json.loads((A/'records/weak_response.json').read_text());Draft202012Validator(s).validate(w);assert not protocol(w)
m=dict(results['primary']);m['recommendation_management_implication']='ADOPT: deploy immediately';assert not protocol(m)
assert 'pause' in results['qualified']['recommendation_management_implication'].lower()
assert 'independent' in str(results['qualified']['change_monitoring_triggers']).lower()
for owner in ['Harry-max264','yicrry777','mp7240-sudo','yanisimova']:
 for name in ['primary','contrast_1','contrast_2','qualified']:run('tools/build_prompt.py','--agent',f'provenance/{owner}','--case',f'agents/adoption_agent/cases/{name}.json','--out',f'work/candidate_{owner}_{name}.txt')
print('PASS: frozen core; 4 input/output schema pairs; exact output fields; 4 team + 16 candidate packets; posture isolation; stable findings; action prefixes; bounded protocol; qualified stop/retest; 2 negative semantic checks.')
print('LIMITS: fixture/rule verification only; independent model evaluation, business pilot, team approval and workshop attendance not verified.')
