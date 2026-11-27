#!/usr/bin/env python3
"""Genus of every symmetry quotient of Bring's surface (exact arithmetic, no float).

Thread "Audit the q-Bessel special-function dictionary", 2026-11-27. Companion of
folio/quantum-observable-universe/lean/QOU/BringsSurface/BringSymmetryQuotientGenus.lean.

Enumerates all subgroups of S5 (2-generated closures, 156 subgroups, 19 conjugacy classes),
finds a generating vector (a, b, c) of orders (2, 4, 5) with abc = 1, and computes for each
class the quotient genus two independent ways:
  * Riemann-Hurwitz with fixed points of each h from the generating vector;
  * Chevalley-Weil with the character of std (x) sgn, and (for contrast) of std.
The RH column equals the std (x) sgn column on every class and differs from std, which is
the numerical side of `h0K_character_forced`. Prints the class distributions used in the
Lean table `subgroupClasses`.
"""
from itertools import permutations, product
from fractions import Fraction as F
G=list(permutations(range(5)))
def m(p,q): return tuple(p[q[i]] for i in range(5))  # p∘q
e=tuple(range(5))
def inv(p):
    r=[0]*5
    for i,x in enumerate(p): r[x]=i
    return tuple(r)
def order(p):
    k,x=1,p
    while x!=e: x=m(x,p);k+=1
    return k
def gen(gs):
    S={e};fr=[e]
    while fr:
        n=[]
        for x in fr:
            for g in gs:
                y=m(x,g)
                if y not in S:S.add(y);n.append(y)
        fr=n
    return frozenset(S)
# find generating vector (a,b,c) orders (2,4,5), abc=1
vec=None
for a in G:
  if order(a)!=2: continue
  for b in G:
    if order(b)!=4: continue
    c=inv(m(a,b))
    if order(c)==5 and len(gen([a,b]))==120: vec=(a,b,c);break
  if vec:break
def conj(x,y): return any(m(m(g,x),inv(g))==y for g in G)
def cent(h): return sum(1 for g in G if m(g,h)==m(h,g))
def pw(p,k):
    x=e
    for _ in range(k): x=m(x,p)
    return x
def fix(h):
    if h==e: return None
    s=F(0)
    for c,mj in zip(vec,(2,4,5)):
        s+=F(sum(1 for k in range(1,mj) if conj(pw(c,k),h)),mj)
    return cent(h)*s
# all subgroups
subs=set()
for a in G:
  for b in G: subs.add(gen([a,b]))
def cls(H):
    return min(tuple(sorted(tuple(m(m(g,h),inv(g)) for h in H))) for g in G)
reps={}
for H in subs: reps.setdefault(cls(H),H)
def orbits(H):
    seen=set();n=0
    for i in range(5):
        if i not in seen:
            n+=1; seen|={h[i] for h in H}
    return n
def sgn(p):
    s=1;p=list(p)
    for i in range(5):
        for j in range(i+1,5):
            if p[i]>p[j]: s=-s
    return s
def fixpts(p): return sum(1 for i in range(5) if p[i]==i)
rows=[]
for H in reps.values():
    n=len(H)
    # RH: 2*4-2 = n(2g'-2) + sum_{h!=1} fix(h)
    tot=sum(fix(h) for h in H if h!=e)
    g2=(F(6)-tot)/n; gq=(g2+2)/2
    chi_std=F(sum(fixpts(h)-1 for h in H),n)
    chi_stds=F(sum((fixpts(h)-1)*sgn(h) for h in H),n)
    rows.append((n,gq,chi_std,chi_stds,orbits(H),sorted({order(h) for h in H})))
for r in sorted(rows): print(r)
print("----")
def ctype(p):
    seen=set();t=[]
    for i in range(5):
        if i in seen: continue
        j=i;l=0
        while j not in seen: seen.add(j); j=p[j]; l+=1
        t.append(l)
    return tuple(sorted(t,reverse=True))
order=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
for H in sorted(reps.values(), key=len):
    k=[0]*7
    for h in H: k[order.index(ctype(h))]+=1
    chi=[4,-2,0,1,1,0,-1]
    g=F(sum(a*b for a,b in zip(k,chi)),len(H))
    print(len(H), k, g, sorted({order[i] for i in range(7) if k[i]}))
