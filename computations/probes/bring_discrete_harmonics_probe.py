#!/usr/bin/env python3
"""Discrete harmonics on Bring's surface as the regular map {5,4} (exact arithmetic).

Thread "Audit the q-Bessel special-function dictionary", 2026-11-27. The owner asked for the
Maass (Laplace) harmonics on Bring's surface. The true Maass spectrum is transcendental; this
probe computes the exact, algebraic model the corpus already uses (QOU/BringsSurface/
BringRegularMap.lean: darts = S5, vertex rotation S=(1 2 3 4), edge flip A=(0 1)):

* the graph Laplacian on the 30 vertices: spectrum and the S5 type of each eigenspace;
* the Hodge Laplacian on the 60 edges: harmonic 1-cochains (dimension 2g = 8) and their
  S5 character.

Result (sympy, exact rationals):
  vertex Laplacian:  0 [triv], 2 [3,2]+[3,1,1] (dim 11), 4 [2,2,1], 5 [4,1], 6 [2,2,1],
                     7 [2,1,1,1]
  harmonic 1-cochains: character (8,-4,0,2,2,0,-2) = 2 x [2,1,1,1] = 2 x (std (x) sgn).

The second line independently confirms `h0K_character_forced` in
QOU/BringsSurface/BringSymmetryQuotientGenus.lean (H^1 = H^0(K) + conj = 2 x std(x)sgn) and
contradicts H^0(K) = std as modelled in BringPrymRiemannRochGenerations.lean (bean qou-efxy).
The discrete spectrum is a combinatorial model, not the Maass spectrum; no number here is a
prediction or a comparison.
"""
from itertools import permutations
import sympy as sp
G=list(permutations(range(5)))
def m(p,q): return tuple(p[q[i]] for i in range(5))
e=tuple(range(5))
def swap(a,b):
    l=list(range(5)); l[a],l[b]=l[b],l[a]; return tuple(l)
S=m(m(swap(1,2),swap(2,3)),swap(3,4)); A=swap(0,1)
def cyc(g):
    H={e};x=g
    while x!=e: H.add(x); x=m(x,g)
    return H
HS=cyc(S)
def coset(g,H): return frozenset(m(g,h) for h in H)
V=[];vi={}
for g in G:
    c=coset(g,HS)
    if c not in vi: vi[c]=len(V); V.append(c)
def vid(g): return vi[coset(g,HS)]
n=len(V); Adj=sp.zeros(n,n); seenE=set()
for g in G:
    c=coset(g,cyc(A))
    if c in seenE: continue
    seenE.add(c); a,b=vid(g),vid(m(g,A)); Adj[a,b]+=1; Adj[b,a]+=1
deg=[sum(Adj.row(i)) for i in range(n)]
Lap=sp.diag(*deg)-Adj
x=sp.symbols('x')
cp=Lap.charpoly(x).as_expr()
fl=sp.factor_list(cp)
print("V=",n,"deg",set(deg))
# class reps
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
chars={'triv':[1,1,1,1,1,1,1],'sgn':[1,-1,1,1,-1,-1,1],'std':[4,2,0,1,-1,0,-1],'std*sgn':[4,-2,0,1,1,0,-1],
 '32':[5,1,1,-1,1,-1,0],'221':[5,-1,1,-1,-1,1,0],'311':[6,0,-2,0,0,0,1]}
size=[1,10,15,20,20,30,24]
def permmat(g):
    P=sp.zeros(n,n)
    for i,c in enumerate(V):
        h=next(iter(c)); P[vid(m(g,h)),i]=1
    return P
PM={t:permmat(reps[t]) for t in order}
for f,mult in fl[1]:
    fx=sp.Poly(f,x)
    if fx.degree()==0: continue
    M=sp.zeros(n,n)
    for k,cf in enumerate(reversed(fx.all_coeffs())): M+=cf*Lap**k
    B=sp.Matrix.hstack(*M.nullspace())
    pinv=(B.T*B).inv()*B.T
    ch=[(pinv*PM[t]*B).trace() for t in order]
    dec={nm:sp.Rational(sum(s*a*b for s,a,b in zip(size,ch,cv)),120) for nm,cv in chars.items()}
    print(sp.factor(f), "mult",mult,"dim",B.shape[1], {k:v for k,v in dec.items() if v})
print("---- 1-cochains")
R=m(A,S)
Ed=[];eidx={}
for g in G:
    if g in eidx: continue
    eidx[g]=(len(Ed),1); eidx[m(g,A)]=(len(Ed),-1); Ed.append(g)
nE=len(Ed)
Fc=[];fseen=set()
for g in G:
    if g in fseen: continue
    cyc_=[];x=g
    while x not in fseen: fseen.add(x); cyc_.append(x); x=m(x,R)
    Fc.append(cyc_)
nF=len(Fc)
d0=sp.zeros(nE,n); d1=sp.zeros(nF,nE)
for j,g in enumerate(Ed):
    d0[j,vid(m(g,A))]+=1; d0[j,vid(g)]-=1
for i,cy in enumerate(Fc):
    for g in cy:
        j,s=eidx[g]; d1[i,j]+=s
print("nE nF",nE,nF,"d1d0=0:", (d1*d0).is_zero_matrix)
L1=d0*d0.T+d1.T*d1
K1=sp.Matrix.hstack(*L1.nullspace())
print("dim harmonic 1-cochains", K1.shape[1])
def edgemat(g):
    P=sp.zeros(nE,nE)
    for j,h in enumerate(Ed):
        k,s=eidx[m(g,h)]; P[k,j]=s
    return P
pinv=(K1.T*K1).inv()*K1.T
ch=[(pinv*edgemat(reps[t])*K1).trace() for t in order]
dec={nm:sp.Rational(sum(s*a*b for s,a,b in zip(size,ch,cv)),120) for nm,cv in chars.items()}
print("character",ch,{k:v for k,v in dec.items() if v})
