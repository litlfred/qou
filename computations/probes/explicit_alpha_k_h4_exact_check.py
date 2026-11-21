#!/usr/bin/env python3
"""Exact check of the H_4 Wedderburn-orthogonal table (prop:explicit-alpha-k-h4).

Builds the Hoefsmit seminormal representations of H_4(q) over Q(q) with
sigma_i^2 = (q - q^-1) sigma_i + 1, computes the characters on the five
minimal-length class representatives e, s1, s1s3, s1s2, s1s2s3, and checks
symbolically that each row r_lambda of the published table satisfies
chi_mu(r_lambda) = 0 for every mu != lambda and chi_lambda(r_lambda) != 0.
Exact arithmetic in sympy throughout; no floating point.
"""
import sympy as sp
q=sp.symbols('q',positive=True)
def qi(d): return (q**d-q**-d)/(q-1/q)
def tableaux(shape):
    n=sum(shape); res=[]
    def rec(T,k):
        if k>n: res.append({v:pos for pos,v in T.items()} if False else dict(T)); return
        for r,l in enumerate(shape):
            row=[c for (rr,c) in T if rr==r]; c=len(row)
            if c<l and (r==0 or (r-1,c) in T): T[(r,c)]=k; rec(T,k+1); del T[(r,c)]
    rec({},1); return [ {v:k for k,v in t.items()} for t in res]  # value->pos
def rep(shape):
    Ts=tableaux(shape); idx={tuple(sorted(t.items())):i for i,t in enumerate(Ts)}; N=len(Ts)
    gens=[]
    for i in range(1,sum(shape)):
        M=sp.zeros(N)
        for j,t in enumerate(Ts):
            (r1,c1),(r2,c2)=t[i],t[i+1]; d=(c2-r2)-(c1-r1)
            M[j,j]=q**d/qi(d)
            if abs(d)>1:
                s=dict(t); s[i],s[i+1]=t[i+1],t[i]; k=idx[tuple(sorted(s.items()))]
                # pair: choose b=1 on (k,j) when j<k, c on other
                M[k,j]= 1 if j<k else 1-1/qi(d)**2
        gens.append(M)
    return gens
parts=[(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]
words=[[],[1],[1,3],[1,2],[1,2,3]]
chi={}
for p in parts:
    g=rep(p); N=g[0].shape[0]
    for a in g: assert sp.simplify(a*a-(q-1/q)*a-sp.eye(N))==sp.zeros(N)
    chi[p]=[sp.simplify(sp.prod([g[w-1] for w in W],start=sp.eye(N)).trace()) if W else N for W in words]
    print(p,chi[p])
P=lambda x:x
Phi=q**6+2*q**4+2*q**2+1
table={
(4,):[1/(q**3*Phi),(q**4+2*q**2+3)/(q**2*Phi),1/(q*(q**2+1)),(q**4+q**2+2)/(q*(q**4+q**2+1)),1],
(3,1):[-1/(q*(q**2+1)),(1-2*q**2-q**4)/(q**2*(q**2+1)),1/(q*(q**2+1)),(1-q**2)/q,1],
(2,2):[-q**2/(q**2+1)**2,q*(1-q**2)/(q**2+1)**2,-(q**4+q**2+1)/(q**2+1)**2,1,0],
(2,1,1):[q**3/(q**2+1),(q**4-2*q**2-1)/(q**2+1),-q**3/(q**2+1),(1-q**2)/q,1],
(1,1,1,1):[-q**9/Phi,q**4*(3*q**4+2*q**2+1)/Phi,-q**3/(q**2+1),q*(-2*q**4-q**2-1)/(q**4+q**2+1),1]}
for lam,c in table.items():
    vals=[sp.factor(sum(ci*x for ci,x in zip(c,chi[mu]))) for mu in parts]
    for mu,v in zip(parts,vals):
        assert (v==0)==(mu!=lam), (lam,mu,v)
    print(lam,'dual to chi_'+str(lam),': PASS')
print('all 5 rows exact: PASS')
