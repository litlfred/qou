#!/usr/bin/env python3
"""Exact discrete sunset on the vertex graph of the Bring map, by S5 x C2 type. Bean qou-u81q.

Vertices = cosets x<S> (30), edges {x, xA}; Laplacian 4I - Adj; Green G = (L + J/30)^-1 - J/30.
Typed projectors P = (d/120) sum chi(g) g * (1 +- c)/2. Checks: each type is one eigenspace,
forbidden typed triples give zero partial sunset, and sum G^3 = 18364201/22680000.
Exact rationals (sympy). Lean twin: QOU/BringsSurface/BringDiscreteSunset.lean.
"""
from itertools import permutations
from fractions import Fraction as F
import sympy as sp
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
def cyc(g):
    H=[e];x=g
    while x!=e: H.append(x); x=m(x,g)
    return H
HS=cyc(S)
cos={}
V=[]
for x in G:
    k=frozenset(m(x,h) for h in HS)
    if k not in cos: cos[k]=len(V); V.append(k)
vid={x:cos[frozenset(m(x,h) for h in HS)] for x in G}
n=len(V); print("V",n)
Adj=[[0]*n for _ in range(n)]
for x in G: Adj[vid[x]][vid[m(x,A)]]+=1
print("deg",set(sum(r) for r in Adj), "loops",sum(Adj[i][i] for i in range(n)), "maxmult",max(max(r) for r in Adj))
L=sp.Matrix(n,n,lambda i,j:(4 if i==j else 0)-Adj[i][j])
J=sp.ones(n,n)/n
Gr=(L+J).inv()-J
assert L*Gr==sp.eye(n)-J
def perm_mat(f):
    P=sp.zeros(n,n)
    for x in G: P[vid[f(x)],vid[x]]=1
    return P
def ctype(p):
    seen=set();t=[]
    for i in range(5):
        if i in seen: continue
        j=i;l=0
        while j not in seen: seen.add(j); j=p[j]; l+=1
        t.append(l)
    return tuple(sorted(t,reverse=True))
order=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
chars=[[1,1,1,1,1,1,1],[1,-1,1,1,-1,-1,1],[4,2,0,1,-1,0,-1],[4,-2,0,1,1,0,-1],[5,1,1,-1,1,-1,0],[5,-1,1,-1,-1,1,0],[6,0,-2,0,0,0,1]]
names=["triv","sgn","std","2111","32","221","311"]
Pg={g:perm_mat(lambda x,g=g:m(g,x)) for g in G}
C=perm_mat(lambda x:m(x,T))
assert all(C*Pg[g]==Pg[g]*C for g in G[:10])
Proj={}
for r in range(7):
    P=sp.zeros(n,n)
    for g in G: P+=chars[r][order.index(ctype(g))]*Pg[g]
    P=P*chars[r][0]/120
    for par,s in ((False,1),(True,-1)):
        Q=P*(sp.eye(n)+s*C)/2
        rk=Q.rank()
        if rk: Proj[(r,par)]=Q
print({(names[k[0]],'-' if k[1] else '+'):Proj[k].rank() for k in Proj})
Gt={k:Gr*Proj[k] for k in Proj}
keys=list(Proj)
total=sum(Gr[i,j]**3 for i in range(n) for j in range(n))
print("sunset",total)
import json
res={}
for a in keys:
  for b in keys:
    for c in keys:
      s=sum(Gt[a][i,j]*Gt[b][i,j]*Gt[c][i,j] for i in range(n) for j in range(n))
      res[(a,b,c)]=s
print("sum check",sum(res.values())==total)

for k,P in Proj.items():
    LP=L*P
    # find scalar
    lam=None
    for i in range(n):
        for j in range(n):
            if P[i,j]!=0: lam=LP[i,j]/P[i,j]; break
        if lam is not None: break
    print(names[k[0]],'-' if k[1] else '+', "lambda",lam, LP==lam*P, "denoms", sp.ilcm(*[x.q for x in P]))
print("G denom", sp.ilcm(*[x.q for x in Gr]))
cs=[1,10,15,20,20,30,24]
def N(a,b,c): return sum(cs[i]*chars[a][i]*chars[b][i]*chars[c][i] for i in range(7))//120
bad=sum(1 for (a,b,c),v in res.items() if v!=0 and not (N(a[0],b[0],c[0]) and not (a[1]^b[1]^c[1])))
print("forbidden triples with nonzero partial sunset:",bad)
print("std+ std+ 32+ partial sunset:",res[((2,False),(2,False),(4,False))])
