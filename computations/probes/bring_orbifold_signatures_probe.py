#!/usr/bin/env python3
"""Orbifold signatures of B/H and B/(H x <c>) for the 19 subgroup classes H <= S5 (exact).

Bean qou-u81q, 2026-11-28. Barycentric (2,4,5) triangulation of the Bring map: triangles = S5 x C2
(simply transitive), base side reflections (T,c), (ST,c), (AT,c). For K <= S5 x C2 the quotient
complex gives the underlying surface (chi, orientability by 2-colouring, boundary curves from
mirror edges), cone points (rotation-only stabilisers) and corner reflectors (dihedral ones).
Lean twin: QOU/BringsSurface/BringOrbifoldSignatures.lean. Integers only.
"""
from itertools import permutations
G=list(permutations(range(5)))
def m(p,q): return tuple(p[q[i]] for i in range(5))
def inv(p):
    r=[0]*5
    for i,x in enumerate(p): r[x]=i
    return tuple(r)
e=tuple(range(5))
def swap(a,b):
    l=list(range(5)); l[a],l[b]=l[b],l[a]; return tuple(l)
S=m(m(swap(1,2),swap(2,3)),swap(3,4)); A=swap(0,1); T=swap(2,4)
def ctype(p):
    seen=set();t=[]
    for i in range(5):
        if i in seen: continue
        j=i;l=0
        while j not in seen: seen.add(j); j=p[j]; l+=1
        t.append(l)
    return tuple(sorted(t,reverse=True))
order=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
# Gamma elements (g,eps): isometry x -> g x T^eps ; composition (g,a)(h,b) = (gh, a^b) since T commutes with left mult and T^2=1 (c central)
def gm(a,b): return (m(a[0],b[0]), a[1]^b[1])
def gen(gens):
    H={(e,0)}; frontier=list(H)
    while frontier:
        new=[]
        for x in frontier:
            for g in gens:
                y=gm(x,g)
                if y not in H: H.add(y); new.append(y)
        frontier=new
    return frozenset(H)
Gam=[(g,a) for g in G for a in (0,1)]
# base reflections, as isometries x -> g x T  i.e. (g,1)
rVE=(T,1); rVF=(m(S,T),1); rEF=(m(A,T),1)
# But careful: these are maps on darts x -> g x T; the triangle group acts on the LEFT of triangles.
# Triangles <-> Gamma (regular action). Stabilisers of base cells:
DV=gen([rVE,rVF]); DE=gen([rVE,rEF]); DF=gen([rVF,rEF])
print(len(DV),len(DE),len(DF))
SVE=gen([rVE]); SVF=gen([rVF]); SEF=gen([rEF])
def cosets(D):
    idx={}
    for g in Gam:
        k=frozenset(gm(g,d) for d in D)
        idx.setdefault(k,len(idx))
    return {g:idx[frozenset(gm(g,d) for d in D)] for g in Gam}, len(idx)
cellmaps={nm:cosets(D) for nm,D in [('V',DV),('E',DE),('F',DF),('ve',SVE),('vf',SVF),('ef',SEF),('t',gen([]))]}
print({k:v[1] for k,v in cellmaps.items()})
def orbits(K,nm):
    cm,_=cellmaps[nm]
    seen={};reps=[]
    for g in Gam:
        c=cm[g]
        if c in seen: continue
        orb=set(cm[gm(k,g)] for k in K)
        for o in orb: seen[o]=len(reps)
        reps.append(g)
    return seen,reps
def sig(K):
    Kset=set(K)
    def stab(g,D): return [k for k in K if gm(gm((inv(g[0]),g[1]),k),g) in D]
    # conjugate: g^-1 k g in D
    res={}
    out={'cone':[], 'corner':[]}
    orbV={}
    for nm,D,mm in [('V',DV,4),('E',DE,2),('F',DF,5)]:
        seen,reps=orbits(K,nm)
        for g in reps:
            st=stab(g,D)
            refl=[x for x in st if x[1]==1 and gm(x,x)==(e,0) and x!=(e,0)]
            # orientation-reversing elements of a corner dihedral group are reflections
            rot=[x for x in st if x[1]==0]
            if any(x[1]==1 for x in st):
                if len(rot)>1: out['corner'].append(len(rot))
            else:
                if len(rot)>1: out['cone'].append(len(rot))
        res[nm]=len(reps)
    mirror_edges=0
    for nm,D in [('ve',SVE),('vf',SVF),('ef',SEF)]:
        seen,reps=orbits(K,nm)
        res[nm]=len(reps)
        mirror_edges+=sum(1 for g in reps if len(stab(g,D))>1)
    tseen,treps=orbits(K,'t')
    nt=len(treps)
    chiX=res['V']+res['E']+res['F']-res['ve']-res['vf']-res['ef']+nt
    # orientability: bipartite graph on triangle orbits across non-mirror sides
    col={}
    ok=True
    tm,_=cellmaps['t']
    for start in range(nt):
        if start in col: continue
        col[start]=1; stack=[start]
        while stack:
            u=stack.pop(); g=treps[u]
            for r,D in [(rVE,SVE),(rVF,SVF),(rEF,SEF)]:
                if len(stab(g,D))>1: continue
                v=tseen[tm[gm(g,r)]]
                if v not in col: col[v]=-col[u]; stack.append(v)
                elif col[v]==col[u]: ok=False
    # boundary components: mirror edges form cycles; count via union-find on boundary vertices
    # simpler: number of boundary components = connected components of mirror-edge subgraph
    parent={}
    def f(x):
        while parent.setdefault(x,x)!=x: x=parent[x]
        return x
    nb_edges=[]
    for nm,D,a,b,Da,Db in [('ve',SVE,'V','E',DV,DE),('vf',SVF,'V','F',DV,DF),('ef',SEF,'E','F',DE,DF)]:
        seen,reps=orbits(K,nm)
        sa,_=orbits(K,a); sb,_=orbits(K,b)
        for g in reps:
            if len(stab(g,D))>1:
                u=(a,sa[cellmaps[a][0][g]]); v=(b,sb[cellmaps[b][0][g]])
                parent[f(u)]=f(v)
    comps=len({f(x) for x in list(parent)})
    return dict(chiX=chiX, orientable=ok, boundary=comps, cone=sorted(out['cone']), corner=sorted(out['corner']), triangles=nt)
# subgroups of S5 by conjugacy class
def genS(gs):
    H={e};fr=[e]
    while fr:
        nw=[]
        for x in fr:
            for g in gs:
                y=m(x,g)
                if y not in H: H.add(y); nw.append(y)
        fr=nw
    return frozenset(H)
subs=set()
for a in G:
    for b in G:
        subs.add(genS([a,b]))
def dist(H): 
    d=[0]*7
    for h in H: d[order.index(ctype(h))]+=1
    return tuple(d)
classes={}
for H in subs: classes.setdefault((len(H),dist(H)),H)
print(len(subs),len(classes))
table=[(1,[1,0,0,0,0,0,0],'1'),(2,[1,0,1,0,0,0,0],'<(01)(23)>'),(2,[1,1,0,0,0,0,0],'<(01)>'),(3,[1,0,0,2,0,0,0],'C3'),(4,[1,2,1,0,0,0,0],'<(01),(23)>'),(4,[1,0,3,0,0,0,0],'V4'),(4,[1,0,1,0,0,2,0],'C4'),(5,[1,0,0,0,0,0,4],'C5'),(6,[1,1,0,2,2,0,0],'C6'),(6,[1,3,0,2,0,0,0],'S3'),(6,[1,0,3,2,0,0,0],'S3tw'),(8,[1,2,3,0,0,2,0],'D4'),(10,[1,0,5,0,0,0,4],'D5'),(12,[1,4,3,2,2,0,0],'S3xS2'),(12,[1,0,3,8,0,0,0],'A4'),(20,[1,0,5,0,0,10,4],'F20'),(24,[1,6,3,8,0,6,0],'S4'),(60,[1,0,15,20,0,0,24],'A5'),(120,[1,10,15,20,20,30,24],'S5')]
import json
allres=[]
for o,dd,nm in table:
    H=classes[(o,tuple(dd))]
    K0=[(h,0) for h in H]; K1=K0+[(h,1) for h in H]
    s0=sig(K0); s1=sig(K1)
    allres.append((nm,s0,s1))
    print(nm.ljust(12), "B/H:",s0, "\n             B/(Hxc):",s1)

