"""Original deterministic SQLite tasks; standard library only."""
import json,random,sqlite3,time
FAMILIES=('aggregate','temporal','exclusion')

def task(seed):
    family=FAMILIES[(seed%100)%3]
    suffix=str(seed)
    names={k:k+'_'+suffix for k in ('accounts','charges','refunds','events','items','blocks')}
    a,c,r,e,i,b=(names[k] for k in names)
    rng=random.Random(seed); threshold=rng.randrange(15,65); cutoff=rng.randrange(4,9)
    if family=='aggregate':
        schema=f'CREATE TABLE {a}(id INTEGER PRIMARY KEY, active INTEGER); CREATE TABLE {c}(id INTEGER PRIMARY KEY, account_id INTEGER, amount INTEGER, settled INTEGER); CREATE TABLE {r}(id INTEGER PRIMARY KEY, account_id INTEGER, amount INTEGER, approved INTEGER);'
        ask=f'Return one row for EVERY active account: id, net. Net is total settled charges minus total approved refunds, treating missing totals as zero. Include negative and zero net accounts. Multiple charges and refunds can belong to the same account. Order by id.'
    elif family=='temporal':
        schema=f'CREATE TABLE {a}(id INTEGER PRIMARY KEY, active INTEGER); CREATE TABLE {e}(id INTEGER PRIMARY KEY, account_id INTEGER, at INTEGER, state TEXT);'
        ask=f'For EVERY active account, return id and the state of its latest event with at <= {cutoff}; ties in at are broken by the greatest event id. If it has no eligible event use the text NONE. Inactive accounts are excluded. Events after the cutoff must not affect selection. Order by account id.'
    else:
        schema=f'CREATE TABLE {a}(id INTEGER PRIMARY KEY, active INTEGER); CREATE TABLE {i}(id INTEGER PRIMARY KEY, account_id INTEGER, amount INTEGER, status TEXT); CREATE TABLE {b}(account_id INTEGER);'
        ask=f'Return id, qualifying_count for active accounts that have at least one item, have NO item whose status is NULL or differs from ok, have NO item with NULL amount or amount < {threshold}, and are not blocked. Each block with a non-NULL account_id blocks that account; NULL block entries block nobody. qualifying_count counts all items for each qualifying account. Order by id.'
    return dict(id=f'{family}-{seed}',seed=seed,family=family,names=names,schema=schema,ask=ask,threshold=threshold,cutoff=cutoff)

def fixture(t,index):
    rng=random.Random(t['seed']*1000+index); a,c,r,e,i,b=(t['names'][k] for k in t['names'])
    accounts=[(x,0 if x==8 else 1) for x in range(1,10)]
    rows={a:accounts}; expected=[]
    if t['family']=='aggregate':
        charges=[]; refunds=[]
        for x,_ in accounts:
            for j in range(0 if x==1 else rng.randrange(1,5)):
                charges.append((len(charges)+1,x,rng.randrange(1,40),int(j!=1)))
            for j in range(0 if x==2 else rng.randrange(1,5)):
                refunds.append((len(refunds)+1,x,rng.randrange(1,40),int(j!=1)))
        rows[c]=charges;rows[r]=refunds
        for x,active in accounts:
            if active: expected.append([x,sum(z[2] for z in charges if z[1]==x and z[3])-sum(z[2] for z in refunds if z[1]==x and z[3])])
    elif t['family']=='temporal':
        events=[]
        for x,_ in accounts:
            if x==1: continue
            for at in [1,t['cutoff'],t['cutoff'],t['cutoff']+1]:
                events.append((len(events)+1,x,at,rng.choice(['open','closed','paused'])))
        rows[e]=events
        for x,active in accounts:
            if active:
                eligible=[z for z in events if z[1]==x and z[2]<=t['cutoff']]
                expected.append([x,max(eligible,key=lambda z:(z[2],z[0]))[3] if eligible else 'NONE'])
    else:
        items=[]; blocks=[(None,),(6,),(6,)]
        for x,_ in accounts:
            if x==1: continue
            for j in range(2+index%3):
                amount=t['threshold']+rng.randrange(1,20); status='ok'
                if j==0 and x==2: status=None
                if j==0 and x==3: status='bad'
                if j==0 and x==4: amount=None
                if j==0 and x==5: amount=t['threshold']-1
                if j==0 and x==9: amount=t['threshold']
                items.append((len(items)+1,x,amount,status))
        rows[i]=items;rows[b]=blocks
        for x,active in accounts:
            its=[z for z in items if z[1]==x]
            if active and its and (x,) not in blocks and all(z[2] is not None and z[2]>=t['threshold'] and z[3]=='ok' for z in its):expected.append([x,len(its)])
    return rows,expected

def execute(t,sql,index):
    con=sqlite3.connect(':memory:'); con.executescript(t['schema']); rows,expected=fixture(t,index)
    for table,data in rows.items():
        if data:con.executemany(f'INSERT INTO {table} VALUES ({",".join("?" for _ in data[0])})',data)
    con.execute('PRAGMA query_only=ON')
    budget=[0]
    def progress():
        budget[0]+=1
        return int(budget[0]>1000)
    con.set_progress_handler(progress,1000)
    try:
        actual=[list(r) for r in con.execute(sql).fetchmany(101)]
        return {'ok':actual==expected,'actual':actual,'expected':expected}
    except sqlite3.Error as error:return {'ok':False,'error':str(error),'expected':expected}
    finally:con.close()

def verify(t,sql):
    start=time.perf_counter(); checks=[execute(t,sql,k) for k in range(1,13)]
    return {'success':all(x['ok'] for x in checks),'passed':sum(x['ok'] for x in checks),'total':12,'checks':checks,'seconds':time.perf_counter()-start}

def prompt(t):
    rows,_=fixture(t,0)
    return f"Task {t['id']}\nSQLite schema:\n{t['schema']}\nObligations: {t['ask']}\nPublic example data: {json.dumps(rows)}\nWrite a reusable SQL query valid for all databases satisfying this schema and obligations, not just these example rows."
