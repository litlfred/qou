#!/usr/bin/env python3
"""Reflection parity on the Bring map (exact, integers). Bean qou-u81q, 2026-11-28.

Darts = S5, sigma x = x S, alpha x = x A, faces = cosets of <A S>. T = (2 4) is the unique t
with t S t^-1 = S^-1, t A t^-1 = A, t^2 = 1; (g, c): x -> g x T are the orientation-reversing
isometries. Prints fixed cells of (g, c) per S5 class and the Hopf trace on H^1 (expected 0).
Lean twin: QOU/BringsSurface/BringReflectionParity.lean.
"""
from itertools import permutations
G=list(permutations(range(5)))
def m(p,q): return tuple(p[q[i]] for i in range(5))  # (p*q)(i)=p(q(i))
def inv(p):
    r=[0]*5
    for i,x in enumerate(p): r[x]=i
    return tuple(r)
e=tuple(range(5))
def swap(a,b):
    l=list(range(5)); l[a],l[b]=l[b],l[a]; return tuple(l)
S=m(m(swap(1,2),swap(2,3)),swap(3,4)); A=swap(0,1); SA=m(S,A)
def sgn(p):
    s=1;seen=set()
    for i in range(5):
        if i in seen: continue
        j=i;l=0
        while j not in seen: seen.add(j); j=p[j]; l+=1
        if l%2==0: s=-s
    return s
Ts=[t for t in G if m(m(t,S),inv(t))==inv(S) and m(m(t,A),inv(t))==A and m(t,t)==e]
print("T candidates",Ts,[sgn(t) for t in Ts])
T=Ts[0]
def cyc(g):
    H=[e];x=g
    while x!=e: H.append(x); x=m(x,g)
    return set(H)
HS,HA,HF=cyc(S),cyc(A),cyc(SA)
def ctype(p):
    seen=set();t=[]
    for i in range(5):
        if i in seen: continue
        j=i;l=0
        while j not in seen: seen.add(j); j=p[j]; l+=1
        t.append(l)
    return tuple(sorted(t,reverse=True))
order=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
reps={}
for g in G: reps.setdefault(ctype(g),g)
# reps as in Lean: 1,(01),(01)(23),(01)(12),(01)(12)(34),(01)(12)(23),(01)(12)(23)(34)
def M(*ps):
    r=e
    for p in ps: r=m(r,p)
    return r
L=[e,swap(0,1),M(swap(0,1),swap(2,3)),M(swap(0,1),swap(1,2)),M(swap(0,1),swap(1,2),swap(3,4)),M(swap(0,1),swap(1,2),swap(2,3)),M(swap(0,1),swap(1,2),swap(2,3),swap(3,4))]
assert [ctype(x) for x in L]==order
AS=m(A,S); HAS=cyc(AS)
for g in L:
    act=lambda x: m(m(g,x),T)
    v=sum(1 for x in G if m(inv(x),act(x)) in HS)//4
    ep=sum(1 for x in G if act(x)==x)//2; em=sum(1 for x in G if act(x)==m(x,A))//2
    f=sum(1 for x in G if m(m(inv(x),act(x)),A) in HAS)//5
    print(ctype(g),"V",v,"E kept",ep,"E reversed",em,"F",f,"tr H1",1-1-(v-(ep-em)-f))
