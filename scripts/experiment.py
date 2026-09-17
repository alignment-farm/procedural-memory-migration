"""Serial, append-only procedural-memory pilot. Run via uv run python."""
import argparse,datetime,hashlib,json,pathlib,subprocess,time,urllib.request,urllib.error
from workload import task,prompt,execute,verify,FAMILIES
ROOT=pathlib.Path(__file__).resolve().parents[1]
ENDPOINT='https://mac-studio-7hr7.taile71f88.ts.net/engines/v1/chat/completions'
SOURCE='docker.io/ai/qwen3.8:27b-q4_K_M'
SYSTEM='''You solve SQLite query tasks. You have an ordinary SQL execution/check tool through this JSON protocol. On every turn output exactly one JSON object, no markdown: {"action":"check","sql":"..."} to run a candidate against the public example and see actual/expected rows, or {"action":"submit","sql":"..."} to finish with a reusable SQL query. You may check or directly submit; at most four turns including final submission. Hidden databases evaluate general correctness. Use the task obligations as authoritative. Any supplied memory is optional procedural advice; correct or ignore it if inappropriate.'''

def dump(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x') as f:json.dump(data,f,indent=2);f.write('\n')

def revision():return subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()

def call(messages,model,directory,label,max_tokens=1400):
    body={'model':model,'messages':messages,'temperature':0,'max_tokens':max_tokens,'chat_template_kwargs':{'enable_thinking':False}}
    dest=directory/(label+'.json'); record={'request':body,'endpoint':ENDPOINT,'revision':revision(),'started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    if dest.exists():raise RuntimeError(f'Refusing overwrite {dest}')
    start=time.perf_counter()
    try:
        req=urllib.request.Request(ENDPOINT,data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=180) as response:record['response']=json.load(response)
    except Exception as error:record['error']=repr(error)
    record['seconds']=time.perf_counter()-start;dump(dest,record)
    if 'error' in record:raise RuntimeError(record['error'])
    return record['response']['choices'][0]['message'].get('content',''),record

def run_task(t,model,memory,directory):
    directory.mkdir(parents=True,exist_ok=False)
    messages=[{'role':'system','content':SYSTEM},{'role':'user','content':prompt(t)+(('\nOptional procedural memory:\n'+memory) if memory else '')}]
    outcome={'task':t,'model':model,'memory':memory,'revision':revision(),'success':False,'events':[],'usage':{'prompt_tokens':0,'completion_tokens':0,'total_tokens':0},'model_seconds':0,'checker_seconds':0}
    for turn in range(4):
        try:
            content,record=call(messages,model,directory,f'turn-{turn}')
            outcome['model_seconds']+=record['seconds']
            for key in outcome['usage']:outcome['usage'][key]+=record['response'].get('usage',{}).get(key,0)
            event={'content':content,'finish_reason':record['response']['choices'][0].get('finish_reason')};outcome['events'].append(event)
            messages.append({'role':'assistant','content':content})
            try:
                action=json.loads(content)
                assert action['action'] in ('check','submit') and isinstance(action['sql'],str)
            except Exception:
                feedback={'error':'Invalid protocol. Output exactly one JSON object with action check or submit and sql string.'}
                event['feedback']=feedback; messages.append({'role':'user','content':json.dumps(feedback)});continue
            if action['action']=='submit':
                result=verify(t,action['sql']);outcome['checker_seconds']+=result['seconds'];outcome['verification']=result;outcome['success']=result['success'];break
            start=time.perf_counter();feedback=execute(t,action['sql'],0);outcome['checker_seconds']+=time.perf_counter()-start
            event['feedback']=feedback;messages.append({'role':'user','content':json.dumps(feedback)+f'\n{3-turn} turns remain. Submit when ready.'})
        except Exception as error:outcome['error']=repr(error);break
    else:outcome['error']='action_budget_exhausted'
    dump(directory/'outcome.json',outcome)
    print(json.dumps({'run':str(directory.relative_to(ROOT)),'success':outcome['success'],'tokens':outcome['usage']['total_tokens'],'actions':len(outcome['events'])}),flush=True)
    return outcome

def archive(run):
    return [json.loads(p.read_text()) for p in sorted((ROOT/'runs'/run).glob('*/outcome.json'))]

def build_bank(run,source_run,model,style="standard"):
    directory=ROOT/'runs'/run;directory.mkdir(parents=True,exist_ok=False)
    experiences=archive(source_run);cards={}
    for family in FAMILIES:
        evidence=[x for x in experiences if x['task']['family']==family]
        # Exact common archive, including final failures; no withheld evaluation records.
        content='From this complete source experience archive, derive concise reusable procedural guidance for future SQLite tasks in the same family. Explain an effective method, pitfalls, and when checking is useful. Do not retain task-specific identifiers or numeric answers. Return plain text, at most 400 words.\n'+json.dumps(evidence)
        if style=='compact':
            content='From this complete source experience archive, derive ONE compact procedural card for future SQLite tasks in this family. Use at most 100 words, no headings or recap. Retain the executable query structure and critical edge cases; omit background explanation and task-specific identifiers/answers. Recommend checks only when the experience indicates they resolve uncertainty, not as a blanket ritual. Ordinary checking remains available. Return only the card.\n'+json.dumps(evidence)
        text,record=call([{'role':'user','content':content}],model,directory,family,max_tokens=320 if style=='compact' else 700)
        cards[family]=text
    dump(directory/'bank.json',{'model':model,'style':style,'source_run':source_run,'source_archive_sha256':hashlib.sha256(json.dumps(experiences,sort_keys=True).encode()).hexdigest(),'cards':cards,'revision':revision()})

def batch(run,seeds,model,bank_run=None):
    cards=json.loads((ROOT/'runs'/bank_run/'bank.json').read_text())['cards'] if bank_run else None
    for seed in seeds:
        t=task(seed)
        arms=[('none',''),('inherit',cards[t['family']])] if cards else [('none','')]
        if seed%2:arms.reverse()
        for name,memory in arms:run_task(t,model,memory,ROOT/'runs'/run/f'{seed}-{name}')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['batch','build']);p.add_argument('--run',required=True);p.add_argument('--model',default=SOURCE);p.add_argument('--start',type=int,default=100);p.add_argument('--count',type=int,default=6);p.add_argument('--bank');p.add_argument('--source-run');p.add_argument('--style',choices=['standard','compact'],default='standard');a=p.parse_args()
    if a.mode=='batch':batch(a.run,range(a.start,a.start+a.count),a.model,a.bank)
    else:build_bank(a.run,a.source_run,a.model,a.style)
