"""Deployment accounting for a frozen policy on a fresh evaluation run."""
import argparse,json
from experiment import ROOT
p=argparse.ArgumentParser();p.add_argument('--evaluation',required=True);p.add_argument('--policy',default='policy-v1.json');p.add_argument('--reconstruction',default='reconstruction-v1');a=p.parse_args()
policy=json.loads((ROOT/'artifacts'/a.policy).read_text())
def outcomes(run):return [(p.parent.name.split('-')[-1],json.loads(p.read_text())) for p in sorted((ROOT/'runs'/run).glob('*/outcome.json'))]
def cost(run):
 result={'calls':0,'tokens':0,'seconds':0,'unknown_usage_calls':0}
 for p in (ROOT/'runs'/run).rglob('*.json'):
  d=json.loads(p.read_text())
  if 'request' not in d:continue
  result['calls']+=1;result['seconds']+=d['seconds'];usage=d.get('response',{}).get('usage')
  if usage is None:result['unknown_usage_calls']+=1
  else:result['tokens']+=usage['total_tokens']
 return result
rows=outcomes(a.evaluation);n=len(rows)//3
assert len(rows)==3*n and n>0
chosen=[d for arm,d in rows if policy['choices'][d['task']['family']]==arm]
assert len(chosen)==n
summary={}
for arm in ['none','inherit','reconstruct','policy']:
 ds=chosen if arm=='policy' else [d for k,d in rows if k==arm]
 summary[arm]={'tasks':len(ds),'successes':sum(d['success'] for d in ds),'use_tokens':sum(d['usage']['total_tokens'] for d in ds),'model_seconds':sum(d['model_seconds'] for d in ds)}
reconstruction=cost(a.reconstruction);calibration=cost(policy['calibration_run'])
for arm,d in summary.items():
 d['incremental_setup_tokens']=(reconstruction['tokens'] if arm in ['reconstruct','policy'] else 0)+(calibration['tokens'] if arm=='policy' else 0)
 d['setup_plus_use_tokens']=d['incremental_setup_tokens']+d['use_tokens']
projections={}
for arm in ['none','inherit','reconstruct']:
 saving=(summary[arm]['use_tokens']-summary['policy']['use_tokens'])/n
 overhead=summary['policy']['incremental_setup_tokens']-summary[arm]['incremental_setup_tokens']
 projections[arm]={'tokens_saved_per_future_task':saving,'extra_setup_tokens':overhead,'break_even_task_count':overhead/saving if saving>0 else None,'quality_difference_in_evaluation':summary['policy']['successes']-summary[arm]['successes']}
print(json.dumps({'choices':policy['choices'],'evaluation':a.evaluation,'arms':summary,'reconstruction_cost':reconstruction,'calibration_cost':calibration,'linear_token_only_projections':projections,'limitations':'Projection is descriptive, assumes future task mix and means recur, and does not equate quality or tokens to money. Source construction is common and must be added for lifetime totals. Policy reuses selected static-arm outcomes; it is not another stochastic run.'},indent=2))
