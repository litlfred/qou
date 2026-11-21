# Build a genus-4 triangulation as a connected sum of four 7-vertex (Moebius/Csaszar) tori
# and verify: simplicial, every edge in exactly 2 faces, vertex links are single cycles,
# orientable (consistent orientation), chi = -6.
from itertools import combinations
torus=[(i,(i+1)%7,(i+3)%7) for i in range(7)]+[(i,(i+2)%7,(i+3)%7) for i in range(7)]
def check(F):
    F=[tuple(f) for f in F]; V=sorted({v for f in F for v in f})
    assert len({frozenset(f) for f in F})==len(F) and all(len(set(f))==3 for f in F)
    E={}
    for f in F:
        for a,b in [(f[0],f[1]),(f[1],f[2]),(f[2],f[0])]:
            E.setdefault(frozenset((a,b)),[]).append((a,b))
    assert all(len(x)==2 for x in E.values()), 'edge degree'
    for v in V:  # link is one cycle
        lk=[tuple(x for x in f if x!=v) for f in F if v in f]
        adj={}
        for a,b in lk: adj.setdefault(a,[]).append(b); adj.setdefault(b,[]).append(a)
        assert all(len(x)==2 for x in adj.values())
        start=next(iter(adj)); seen={start}; cur=start; prev=None
        while True:
            nx=[y for y in adj[cur] if y!=prev][0] if prev is not None else adj[cur][0]
            if nx==start: break
            seen.add(nx); prev,cur=cur,nx
        assert len(seen)==len(adj), f'link of {v} not connected'
    return V,E
def orient(F):
    # BFS to orient consistently
    F=[list(f) for f in F]; done={0}; queue=[0]
    def edges(f): return [(f[0],f[1]),(f[1],f[2]),(f[2],f[0])]
    while queue:
        i=queue.pop()
        for a,b in edges(F[i]):
            for j,g in enumerate(F):
                if j==i or not {a,b}<=set(g): continue
                if j in done:
                    assert (b,a) in edges(g), 'non-orientable'
                else:
                    if (a,b) in edges(g): g.reverse()
                    done.add(j); queue.append(j)
    assert len(done)==len(F)
    return [tuple(f) for f in F]
T=orient(torus); check(T)
def relabel(F,off): return [tuple(v+off for v in f) for f in F]
K=T
for k in range(1,4):
    T2=relabel(T,7*k)
    # remove face f1 from K (last face of previous block) and face T2[0], glue with orientation reversed
    f1=K[-1] if k>1 else K[0]
    f2=T2[0]
    # orientation-reversing identification: f2=(x,y,z) glued to reversed f1=(c,b,a)
    a,b,c=f1; x,y,z=f2
    m={x:c,y:b,z:a}
    K=[f for f in K if f!=f1]+[tuple(m.get(v,v) for v in f) for f in T2 if f!=f2]
V,E=check(K)
# compact labels
lab={v:i for i,v in enumerate(sorted(V))}
K=[tuple(lab[v] for v in f) for f in K]
K=orient(K); V,E=check(K)
print('V',len(V),'E',len(E),'F',len(K),'chi',len(V)-len(E)+len(K))
print(K)
