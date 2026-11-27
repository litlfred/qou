import json,subprocess,sys
S=sys.argv[1]; out=[]
for page in range(1,200):
    r=subprocess.run(['gh','api',f'repos/litlfred/qou/pulls?state=all&sort=created&direction=desc&per_page=100&page={page}'],capture_output=True,text=True)
    if r.returncode: print('err',page,r.stderr[:200],flush=True); break
    d=json.loads(r.stdout)
    if not d: break
    for p in d:
        out.append({k:p.get(k) for k in ['number','title','state','created_at','closed_at','merged_at','body']}|{'head':p['head']['ref'],'head_sha':p['head']['sha'],'draft':p.get('draft'),'labels':[l['name'] for l in p['labels']]})
    print(page,d[-1]['created_at'],flush=True)
    if d[-1]['created_at']<'2026-06-01': break
json.dump(out,open(S+'/prs.json','w'))
print('done',len(out))
