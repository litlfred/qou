exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'genus4_connected_sum_triangulation.py')).read().replace("print(K)",""))
F=K
E=sorted({tuple(sorted(e)) for e in [ (f[a],f[b]) for f in F for a,b in [(0,1),(1,2),(0,2)]]})
eidx={e:i for i,e in enumerate(E)}
def D(f,e):
    a,b,c=F[f]; s=0
    for (x,y),sg in [((a,b),1),((b,c),1),((a,c),-1)]:
        if (x,y)==E[e]: s+=sg
        if (y,x)==E[e]: s-=sg
    return s
# dual graph BFS tree from face 0
adj={}
for e in range(len(E)):
    fs=[f for f in range(len(F)) if D(f,e)!=0]; assert len(fs)==2
    adj.setdefault(fs[0],[]).append((fs[1],e)); adj.setdefault(fs[1],[]).append((fs[0],e))
par={0:None}; q=[0]
while q:
    f=q.pop(0)
    for g,e in adj[f]:
        if g not in par: par[g]=(f,e); q.append(g)
# path vector for g: want D*m = e_g - e_0. Build by walking up: for step g->p via edge e, D(.,e)*s has +1 at g?
paths={}
for g in range(len(F)):
    m={}; cur=g
    while par[cur] is not None:
        p,e=par[cur]; s=D(cur,e)  # D(cur,e)*s = 1 ; D(p,e)*s = -1 (opposite orientations)
        assert D(p,e)==-s
        m[e]=m.get(e,0)+s; cur=p
    paths[g]=m
# verify
for g in range(len(F)):
    for f in range(len(F)):
        v=sum(s*D(f,e) for e,s in paths[g].items())
        assert v==(1 if f==g else 0)-(1 if f==0 else 0)
print(len(E), max(len(p) for p in paths.values()))
import json; json.dump({'F':F,'E':E,'paths':{g:list(paths[g].items()) for g in paths}},open('cert.json','w'))
