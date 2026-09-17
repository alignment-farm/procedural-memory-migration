"""Recheck every submitted query using that record's committed generator."""
import importlib.util,json,pathlib,subprocess,tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
count=0
with tempfile.TemporaryDirectory() as temp:
 modules={}
 for path in sorted((ROOT/'runs').rglob('outcome.json')):
  d=json.loads(path.read_text());rev=d['revision']
  if 'verification' not in d:continue
  if rev not in modules:
   source=subprocess.check_output(['git','show',rev+':scripts/workload.py'],cwd=ROOT)
   target=pathlib.Path(temp)/(rev+'.py');target.write_bytes(source)
   spec=importlib.util.spec_from_file_location('workload_'+rev,target);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);modules[rev]=m
  sql=json.loads(d['events'][-1]['content'])['sql'];actual=modules[rev].verify(d['task'],sql)
  expected=d['verification']
  for key in ['success','passed','total','checks']:
   assert actual[key]==expected[key],(str(path),key)
  count+=1
print(f'Replayed {count} submissions: saved checks match committed generators.')
