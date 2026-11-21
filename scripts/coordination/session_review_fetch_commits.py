import json,subprocess,sys,re
from concurrent.futures import ThreadPoolExecutor
S=sys.argv[1]
p=json.load(open(S+'/prs.json'))
todo=[x['number'] for x in p if not x['merged_at']]
def get(n):
    r=subprocess.run(['gh','api',f'repos/litlfred/qou/pulls/{n}/commits?per_page=100'],capture_output=True,text=True)
    if r.returncode: return n,None
    d=json.loads(r.stdout)
    ids=set(); last=None
    for c in d:
        ids|=set(re.findall(r'claude\.ai/code/(session_[A-Za-z0-9]+)',c['commit']['message']))
        last=c['commit']['committer']['date']
    return n,{'sessions':sorted(ids),'ncommits':len(d),'last_commit':last}
res={}
with ThreadPoolExecutor(4) as ex:
    for i,(n,v) in enumerate(ex.map(get,todo)):
        res[n]=v
        if i%50==0: print(i,flush=True)
json.dump(res,open(S+'/pr_commits.json','w')); print('done',len(res))
