"""Three static alternatives, and a frozen paid family-wise selection rule."""
import argparse,json,pathlib
from experiment import ROOT,SOURCE,dump,run_task,revision
from workload import task,FAMILIES

def compare(run,model,start,count,inherit,reconstruct):
    banks={name:json.loads((ROOT/'runs'/bank/'bank.json').read_text())['cards'] for name,bank in [('inherit',inherit),('reconstruct',reconstruct)]}
    for seed in range(start,start+count):
        t=task(seed);arms=['none','inherit','reconstruct']; shift=((seed-start)//3)%3;arms=arms[shift:]+arms[:shift]
        for arm in arms:run_task(t,model,'' if arm=='none' else banks[arm][t['family']],ROOT/'runs'/run/f'{seed}-{arm}')

def select(calibration,output):
    data=[(p.parent.name.split('-')[-1],json.loads(p.read_text())) for p in sorted((ROOT/'runs'/calibration).glob('*/outcome.json'))]
    choices={};statistics={}
    for family in FAMILIES:
        stats={}
        for arm in ['none','inherit','reconstruct']:
            rows=[d for a,d in data if a==arm and d['task']['family']==family]
            if len(rows)!=2:raise ValueError('Expected two complete calibration records per family and arm')
            stats[arm]={'successes':sum(d['success'] for d in rows),'tokens':sum(d['usage']['total_tokens'] for d in rows)}
        choices[family]=min(stats,key=lambda arm:(-stats[arm]['successes'],stats[arm]['tokens'],['none','inherit','reconstruct'].index(arm)))
        statistics[family]=stats
    dump(ROOT/'artifacts'/output,{'calibration_run':calibration,'choices':choices,'statistics':statistics,'revision':revision(),'rule':'Max successes, min tokens, then none/inherit/reconstruct. All calibration and reconstruction is charged.'})
    print(json.dumps(choices),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['compare','select']);p.add_argument('--run',required=True);p.add_argument('--model');p.add_argument('--start',type=int,default=300);p.add_argument('--count',type=int,default=6);p.add_argument('--inherit',default='bank-v1');p.add_argument('--reconstruct',default='reconstruction-v1');p.add_argument('--output',default='policy-v1.json');a=p.parse_args()
    if a.mode=='compare':compare(a.run,a.model,a.start,a.count,a.inherit,a.reconstruct)
    else:select(a.run,a.output)
