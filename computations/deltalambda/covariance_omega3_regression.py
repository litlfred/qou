#!/usr/bin/env python3
"""omega3-on-dimension regression for the covariance-kernel mechanism (qou-x631).
READ-ONLY. Computes e(x)=E_Planch[omega3 | ln f = x] binned by dimension, showing:
  ~97% of Plancherel mass concentrates on the top-dimension bin where e<0;
  the negligible-mass low-dim shapes carry large positive omega3 (balancing to
  E[omega3]=0). Convex-increasing weights (ln f)^n amplify the dominant negative
  top bin => Cov_Planch(omega3,(ln f)^n)<0, while an SD threshold can isolate a
  delicate intermediate imbalance (=> SD fails, conjecture holds).
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

# regression e(x)=E_Planch[omega3 | ln f in bin x]; Plancherel weight f^2/k!.
# Show: e<0 in the top-dimension tail; positive region (if any) confined to mid/low x.
for k in [16,20]:
    C2=k*(k-1)//2; kf=math.factorial(k)
    rows=[(hook_dim(l), om3(l,C2)) for l in partitions(k)]
    rows.sort(key=lambda r:r[0])  # ascending dim
    lo=math.log(rows[0][0]); hi=math.log(rows[-1][0]); NB=10
    bins=[[0.0,0.0] for _ in range(NB)]  # [sum w, sum w*omega3]
    for f,o in rows:
        x=math.log(f); b=min(NB-1,int((x-lo)/(hi-lo+1e-12)*NB)); w=f*f/kf
        bins[b][0]+=w; bins[b][1]+=w*o
    print(f"=== k={k}: regression e(x)=E[omega3 | ln f bin], low dim -> high dim ===")
    print("  bin  x_center   Planch-mass   e(x)=E[omega3|bin]")
    for b in range(NB):
        xc=lo+(b+0.5)*(hi-lo)/NB; m=bins[b][0]; e=bins[b][1]/m if m>0 else 0
        bar = ('#' if e<0 else '+')*max(1,min(40,int(abs(e)*2)))
        print(f"  {b:2d}  {xc:7.2f}   {m:9.2e}   {e:+8.3f}  {bar}")
    # top-decile (highest dim) average omega3:
    tot=sum(r[0]**2 for r in rows)/kf
    topmass=0.0; tope=0.0
    for f,o in rows[::-1]:
        w=f*f/kf; 
        if topmass<0.10: topmass+=w; tope+=w*o
    print(f"  --> top ~10% dimension mass: E[omega3] = {tope/topmass:+.3f}  (want <0)")
    print()
