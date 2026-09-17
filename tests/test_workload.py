import sys,pathlib,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from workload import task,verify,execute
class OracleTests(unittest.TestCase):
 def test_correct_queries_and_mutants(self):
  for seed in range(100,112):
   t=task(seed);a,c,r,e,i,b=(t['names'][k] for k in t['names'])
   if t['family']=='aggregate':
    good=f'SELECT a.id, COALESCE((SELECT SUM(amount) FROM {c} WHERE account_id=a.id AND settled=1),0)-COALESCE((SELECT SUM(amount) FROM {r} WHERE account_id=a.id AND approved=1),0) FROM {a} a WHERE active=1 ORDER BY a.id'
    bad=f'SELECT a.id,SUM(c.amount)-SUM(r.amount) FROM {a} a LEFT JOIN {c} c ON c.account_id=a.id LEFT JOIN {r} r ON r.account_id=a.id WHERE active=1 GROUP BY a.id ORDER BY a.id'
   elif t['family']=='temporal':
    good=f"SELECT a.id,COALESCE((SELECT state FROM {e} WHERE account_id=a.id AND at<={t['cutoff']} ORDER BY at DESC,id DESC LIMIT 1),'NONE') FROM {a} a WHERE active=1 ORDER BY a.id"
    bad=good.replace('id DESC','id ASC')
   else:
    good=f"SELECT a.id,(SELECT COUNT(*) FROM {i} WHERE account_id=a.id) FROM {a} a WHERE active=1 AND EXISTS(SELECT 1 FROM {i} WHERE account_id=a.id) AND NOT EXISTS(SELECT 1 FROM {i} WHERE account_id=a.id AND (status IS NULL OR status<>'ok' OR amount IS NULL OR amount<{t['threshold']})) AND NOT EXISTS(SELECT 1 FROM {b} WHERE account_id=a.id) ORDER BY a.id"
    bad=good.replace(f'NOT EXISTS(SELECT 1 FROM {b} WHERE account_id=a.id)',f'a.id NOT IN (SELECT account_id FROM {b})')
   self.assertTrue(verify(t,good)['success'],(t,verify(t,good)))
   self.assertFalse(verify(t,bad)['success'])
 def test_read_only_and_bad_sql(self):
  t=task(100)
  self.assertFalse(execute(t,'DROP TABLE accounts_100',0)['ok'])
  self.assertFalse(execute(t,'garbage',0)['ok'])
if __name__=='__main__':unittest.main()
