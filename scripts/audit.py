"""Offline integrity checks beyond SQL replay; no model calls."""
import datetime,hashlib,json,pathlib,subprocess
from experiment import ROOT,archive
banks=['bank-v1','bank-v2','reconstruction-v2']
common=hashlib.sha256(json.dumps(archive('source-v1'),sort_keys=True).encode()).hexdigest()
for bank in banks:
 d=json.loads((ROOT/'runs'/bank/'bank.json').read_text());assert d['source_archive_sha256']==common,bank
 for p in (ROOT/'runs'/bank).glob('*.json'):
  r=json.loads(p.read_text())
  if 'request' in r:
   content=json.dumps(r['request'])
   for seed in list(range(200,206))+list(range(300,306))+list(range(400,412))+list(range(500,506)):
    for family in ['aggregate','temporal','exclusion']:assert f'{family}-{seed}' not in content,(bank,seed)
ids={'docker.io/ai/qwen3.8:27b-q4_K_M':'f04d0a543b642a6f0d06590973b124bc4e8700ddf7e99b669ec6c4ab1ef561ef','docker.io/ai/qwen3:8B-Q4_K_M':'79fa56c07429f64f41950fe2f524937cf3ae9ea9bd3d7ada72170b036ea3cc85'}
calls=0
for p in (ROOT/'runs').rglob('*.json'):
 d=json.loads(p.read_text())
 if 'request' not in d:continue
 calls+=1
 if 'response' in d:assert ids[d['request']['model']] in d['response']['model'],str(p)
policy=json.loads((ROOT/'artifacts/policy-v2.json').read_text())
locked=json.loads(subprocess.check_output(['git','show','092ae7d:artifacts/policy-v2.json'],cwd=ROOT))
assert policy==locked
locktime=datetime.datetime.fromisoformat(subprocess.check_output(['git','show','-s','--format=%cI','092ae7d'],cwd=ROOT,text=True).strip())
for p in (ROOT/'runs/evaluation-recipient-v2').rglob('turn-*.json'):
 assert datetime.datetime.fromisoformat(json.loads(p.read_text())['started'])>=locktime
for family,stats in policy['statistics'].items():
 chosen=min(stats,key=lambda arm:(-stats[arm]['successes'],stats[arm]['tokens'],['none','inherit','reconstruct'].index(arm)))
 assert chosen==policy['choices'][family]
for seed in range(400,412):
 records=[]
 for run,arms in [('evaluation-recipient-v2',['none','inherit','reconstruct']),('evaluation-source-v2',['none','inherit'])]:
  for arm in arms:
   p=ROOT/'runs'/run/f'{seed}-{arm}'/'outcome.json';assert p.exists(),str(p);records.append(json.loads(p.read_text()))
 assert all(d['task']==records[0]['task'] for d in records),seed
 assert records[1]['memory']==records[4]['memory'],seed
print(f'Audited {calls} model calls: pinned weights, same source archive, no held-out build tasks, frozen pre-evaluation policy, and matched final task facts/artifact.')
