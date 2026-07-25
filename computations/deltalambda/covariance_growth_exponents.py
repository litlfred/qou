#!/usr/bin/env python3
"""Asymptotic growth exponents for the covariance-kernel reduction (qou-x631).
READ-ONLY. Measures growth (log-log slope, tail k>=16) of the Plancherel quantities
in the log-moment expansion M_n ~ n*muL^{n-1}*Cov(w3,ln f):
  muL=E[ln f]~k^1.5, |Cov1|~k^1.64, Var(ln f)~k^0.63 (concentration),
  E[w3 delta^2]~k^1.82, and r2=E[w3 d2]/(muL|Cov1|)~k^-1.33 -> 0.
=> the leading (cited n=1) term dominates by a full power of k; the correction
r2<=0.26 for all k>=6 and falls monotonically, so Cov(w3,(ln f)^n)<0 asymptotically.
Companion to docs/audits/2026-07-25-covariance-kernel-laplace-moment-reduction.md.
"""
import math
def partitions(n, mx=None):
    if mx is None: mx=n
    if n==0:
        yield (); return
    for f in range(min(n,mx),0,-1):
        for r in partitions(n-f,f): yield (f,)+r
def hook_dim(lam):
    lam=list(lam); n=sum(lam)
    conj=[sum(1 for r in lam if r>j) for j in range(lam[0])] if lam else []
    p=1
    for i,row in enumerate(lam):
        for j in range(row): p*=(row-1-j)+(conj[j]-1-i)+1
    return math.factorial(n)//p
def om3(lam,C2): return sum((j-i)**2 for i,row in enumerate(lam) for j in range(row))-C2

ks=list(range(6,29))
data={}
for k in ks:
    C2=k*(k-1)//2; kf=math.factorial(k)
    rows=[(om3(l,C2), hook_dim(l)**2/kf, math.log(hook_dim(l))) for l in partitions(k)]
    muL=sum(p*lf for _,p,lf in rows)
    Cov1=sum(p*o*lf for o,p,lf in rows)
    V=sum(p*(lf-muL)**2 for _,p,lf in rows)          # Var(ln f)
    d2=sum(p*o*(lf-muL)**2 for o,p,lf in rows)        # E[w3 delta^2]
    data[k]=(muL,Cov1,V,d2)

print(" k | muL      |Cov1|    Var(lnf)  E[w3 d^2]  | r2=E[w3d2]/(muL|Cov1|)")
for k in ks:
    muL,Cov1,V,d2=data[k]
    print(f"{k:2d} | {muL:7.2f}  {abs(Cov1):7.3f}  {V:8.3f}  {d2:8.3f}  | {d2/(muL*abs(Cov1)):.5f}")

def slope(xs,ys):  # log-log least squares slope
    lx=[math.log(x) for x in xs]; ly=[math.log(abs(y)) for y in ys]
    n=len(lx); sx=sum(lx); sy=sum(ly); sxx=sum(a*a for a in lx); sxy=sum(a*b for a,b in zip(lx,ly))
    return (n*sxy-sx*sy)/(n*sxx-sx*sx)
tail=[k for k in ks if k>=16]
print()
print("log-log slopes vs k (tail k>=16):")
print(f"  muL       ~ k^{slope(tail,[data[k][0] for k in tail]):.3f}   (expect ~ (k ln k)/2, slope slightly >1)")
print(f"  |Cov1|    ~ k^{slope(tail,[data[k][1] for k in tail]):.3f}")
print(f"  Var(lnf)  ~ k^{slope(tail,[data[k][2] for k in tail]):.3f}")
print(f"  E[w3 d^2] ~ k^{slope(tail,[data[k][3] for k in tail]):.3f}")
print(f"  r2=E[w3d2]/(muL|Cov1|) ~ k^{slope(tail,[data[k][3]/(data[k][0]*abs(data[k][1])) for k in tail]):.3f}  (want NEGATIVE -> resid=o(lead))")
