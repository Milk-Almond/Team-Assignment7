from pathlib import Path
import json,subprocess,sys,hashlib
from jsonschema import Draft202012Validator
T=Path(__file__).resolve().parent; R=T.parents[1]; A=R/'agents/adoption_agent'
outputs={}
for name,category in [('primary','BOUNDED_EXPERIMENT'),('contrast_1','DEFER'),('qualified','DEFER')]:
 case=json.loads((T/f'cases/{name}.json').read_text()); original=json.loads((A/f'cases/{name}.json').read_text());assert case==original
 Draft202012Validator(json.loads((R/'core/input_schema.json').read_text())).validate(case)
 out=json.loads((T/f'responses/{name}.json').read_text());Draft202012Validator(json.loads((R/'core/output_schema.json').read_text())).validate(out)
 assert out['agent']==json.loads((A/'agent_metadata.json').read_text())
 assert out['recommendation_management_implication'].startswith(category+':')
 assert out['change_monitoring_triggers'] and out['abstention_or_more_information_needed']
 subprocess.run([sys.executable,str(R/'tools/validate_response.py'),str(T/f'responses/{name}.json')],check=True)
 outputs[name]=out
 print('PASS original case, full contracts, exact agent version and category:',name,category)
p=json.loads((T/'cases/primary.json').read_text());c=json.loads((T/'cases/contrast_1.json').read_text())
assert [k for k in p if p[k]!=c[k]]==['adoption_posture']
for field in ['general_et_finding','application_finding']:assert outputs['primary'][field]==outputs['contrast_1'][field]
assert 'Pause' in outputs['qualified']['recommendation_management_implication']
assert 'independent' in str(outputs['qualified']['change_monitoring_triggers']).lower()
for term in ['four-week','category manager','2000','30','20%','95%','Stop','day 28']:
 assert term.lower() in outputs['primary']['recommendation_management_implication'].lower(),term
for line in (T/'SHA256.txt').read_text().splitlines():
 digest,path=line.split('  ',1);assert hashlib.sha256((T/path).read_bytes()).hexdigest()==digest,path
print('PASS unchanged matched context, invariant findings, bounded protocol, qualified pause/retest and saved artifact hashes')
print('LIMIT: same-conversation AI qualitative analyses; no independent inference or operational trial claimed.')
