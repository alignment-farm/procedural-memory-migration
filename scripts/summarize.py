"""Summarize saved outcomes only; no model calls and no silent exclusions."""
import collections,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
rows=[];calls=[]
for p in sorted((ROOT/'runs').rglob('*.json')):
 d=json.loads(p.read_text())
 if p.name=='outcome.json':rows.append((p,d))
 elif 'request' in d and ('response' in d or 'error' in d):calls.append((p,d))
groups=collections.defaultdict(list)
for p,d in rows:groups[(p.relative_to(ROOT/'runs').parts[0],p.parent.name.split('-')[-1])].append(d)
summary={}
for (run,arm),ds in groups.items():
 summary[run+'/'+arm]={'tasks':len(ds),'successes':sum(d['success'] for d in ds),'failures':sum(not d['success'] for d in ds),'tokens':sum(d['usage']['total_tokens'] for d in ds),'prompt_tokens':sum(d['usage']['prompt_tokens'] for d in ds),'completion_tokens':sum(d['usage']['completion_tokens'] for d in ds),'model_seconds':sum(d['model_seconds'] for d in ds),'checker_seconds':sum(d['checker_seconds'] for d in ds),'actions':sum(len(d['events']) for d in ds)}
phase_cost=collections.defaultdict(lambda:{'calls':0,'failed_calls':0,'total_tokens':0,'seconds':0})
for p,d in calls:
 g=phase_cost[p.relative_to(ROOT/'runs').parts[0]];g['calls']+=1;g['failed_calls']+=int('error' in d);g['total_tokens']+=d.get('response',{}).get('usage',{}).get('total_tokens',0);g['seconds']+=d['seconds']
print(json.dumps({'outcomes':summary,'all_call_costs':dict(phase_cost),'caveat':'Missing provider usage on a failed request is unknown, not zero cost; latency is descriptive.'},indent=2))
