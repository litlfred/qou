"""Joint ranks of the eight electroweak projectors E_abc in H_6(q).

Supports prop:weak-spectral-completeness (item on joint ranks). Builds
Young's seminormal representations of H_6(q) for every partition of 6,
checks the Hecke and braid relations symbolically, and sums over all
irreducibles the trace of E_abc = e_a(sigma_1) e_b(sigma_3) e_c(sigma_5),
where e_+ / e_- are the two primitive idempotents of the slot H_2(q).

Exact arithmetic only (sympy rationals / rational functions; no float):
at symbolic q the summed trace of an idempotent over Q(q) equals its rank.
Expected: 11, 9 (x6), 11; total 76 = sum_lambda f^lambda for n = 6.
Spot checks at q = 3 and q = 5/7 use exact matrix rank.
No witness is written.

-- Ref: [leitner2026] mass-theory/weak-spectral-completeness
"""
from fractions import Fraction as F
import itertools, sympy as sp
def partitions(n,m=None):
    if m is None: m=n
    if n==0: yield (); return
    for k in range(min(n,m),0,-1):
        for p in partitions(n-k,k): yield (k,)+p
def syt(lam):
    n=sum(lam); res=[]
    def rec(T,filled,k):
        if k>n: res.append(dict(T)); return
        for r in range(len(lam)):
            c=filled[r]
            if c<lam[r] and (r==0 or filled[r-1]>c):
                filled[r]+=1; T[k]=(r,c); rec(T,filled,k+1); filled[r]-=1; del T[k]
    rec({},[0]*len(lam),1); return res
def gens(lam,q):
    Ts=syt(lam); key=[tuple(sorted(T.items())) for T in Ts]; idx={k:i for i,k in enumerate(key)}
    N=len(Ts); G={}
    for i in range(1,6):
        M=sp.zeros(N,N)
        for a,T in enumerate(Ts):
            (r1,c1),(r2,c2)=T[i],T[i+1]
            r=(c2-r2)-(c1-r1)
            ar=q**r*(q-1/q)/(q**r-q**(-r)); M[a,a]=ar
            if abs(r)>1:
                T2=dict(T); T2[i],T2[i+1]=T[i+1],T[i]
                b=idx[tuple(sorted(T2.items()))]
                amr=q**(-r)*(q-1/q)/(q**(-r)-q**(r))
                if r>0: M[b,a]=1
                else: M[b,a]=ar*amr+1
        G[i]=M
    return G,N
for q in [sp.Integer(3), sp.Rational(5,7), sp.Symbol('q')]:
    tot={p:0 for p in itertools.product([1,0],repeat=3)}; sym=q.is_Symbol
    for lam in partitions(6):
        G,N=gens(lam,q); I=sp.eye(N); d=1/(q+1/q)
        # check relations
        for i in range(1,6):
            assert sp.simplify(G[i]*G[i]-(q-1/q)*G[i]-I)==sp.zeros(N,N)
        for i in range(1,5):
            assert sp.simplify(G[i]*G[i+1]*G[i]-G[i+1]*G[i]*G[i+1])==sp.zeros(N,N)
        e=lambda s,a: d*(s+(1/q)*I) if a else d*(q*I-s)
        for p in tot:
            E=e(G[1],p[0])*e(G[3],p[1])*e(G[5],p[2])
            tot[p]+= sp.simplify(E.trace()) if sym else E.rank()
    print(q,tot,sum(tot.values()))
