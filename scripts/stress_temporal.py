"""Post-hoc offline grader audit: event IDs no longer correlate with time.
No model calls, no changes to primary outcomes, banks, or selection.
"""
import collections,json,random
import workload
from experiment import ROOT
original=workload.fixture

def permuted(t,index):
 rows,_=original(t,index);n=t['names'];events=rows[n['events']]
 ids=random.Random(900000+t['seed']*100+index).sample(range(1000,9999),len(events))
 events=[(identifier,*row[1:]) for identifier,row in zip(ids,events)]
 rows[n['events']]=events;expected=[]
 for account,active in rows[n['accounts']]:
  if not active:continue
  candidates=[row for row in events if row[1]==account and row[2]<=t['cutoff']]
  expected.append([account,max(candidates,key=lambda row:(row[2],row[0]))[3] if candidates else 'NONE'])
 return rows,sorted(expected)

workload.fixture=permuted
# Establish that the supplemental fixtures catch the coverage gap they target.
t=workload.task(901);a=t['names']['accounts'];e=t['names']['events']
good=f"SELECT a.id, COALESCE((SELECT state FROM {e} WHERE account_id=a.id AND at<={t['cutoff']} ORDER BY at DESC,id DESC LIMIT 1),'NONE') FROM {a} a WHERE active=1 ORDER BY a.id"
assert workload.verify(t,good)['success']
assert not workload.verify(t,good.replace('ORDER BY at DESC,id DESC','ORDER BY id DESC'))['success']
summary=collections.defaultdict(lambda:{'tasks':0,'primary_successes':0,'stress_successes':0});changed=[]
for run in ['evaluation-recipient-v2','evaluation-source-v2']:
 for p in sorted((ROOT/'runs'/run).glob('*/outcome.json')):
  d=json.loads(p.read_text())
  if d['task']['family']!='temporal':continue
  if 'verification' not in d:ok=False
  else:ok=workload.verify(d['task'],json.loads(d['events'][-1]['content'])['sql'])['success']
  key=run+'/'+p.parent.name.split('-')[-1];s=summary[key];s['tasks']+=1;s['primary_successes']+=d['success'];s['stress_successes']+=ok
  if ok!=d['success']:changed.append({'run':str(p.relative_to(ROOT)),'primary':d['success'],'stress':ok})
assert sum(s['tasks'] for s in summary.values())==20,'Wait for all matched evaluation records'
print(json.dumps({'status':'post-hoc offline verifier audit, not an additional model evaluation or selection set','change':'Permute event IDs independently of timestamps; compute expected rows in Python with (at,id) ordering. 12 fixtures per query.','summary':dict(summary),'changed':changed},indent=2))
