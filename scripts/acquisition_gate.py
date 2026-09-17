"""Apply the prospective screening gate; requires six paired completed tasks."""
import argparse,json
from experiment import ROOT,dump,revision
p=argparse.ArgumentParser();p.add_argument('run');p.add_argument('--output',required=True);a=p.parse_args()
rows=[(q.parent.name.split('-')[-1],json.loads(q.read_text())) for q in sorted((ROOT/'runs'/a.run).glob('*/outcome.json'))]
stats={}
for arm in ['none','inherit']:
 ds=[d for key,d in rows if key==arm]
 assert len(ds)==6,'Gate requires all six tasks per arm, including failures'
 stats[arm]={'successes':sum(d['success'] for d in ds),'tokens':sum(d['usage']['total_tokens'] for d in ds),'ids':sorted(d['task']['id'] for d in ds)}
assert stats['none']['ids']==stats['inherit']['ids']
a0,b=stats['none'],stats['inherit']
quality=b['successes']-a0['successes']>=2
cost=b['successes']>=a0['successes'] and b['tokens']<=.85*a0['tokens']
result={'run':a.run,'pass':quality or cost,'quality_gate':quality,'cost_gate':cost,'stats':stats,'revision':revision(),'interpretation':'Screening only, not statistical significance. Failed gate is acquisition evidence, not transfer failure.'}
dump(ROOT/'artifacts'/a.output,result);print(json.dumps(result,indent=2))
