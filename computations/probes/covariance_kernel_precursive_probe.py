"""Pre-registered probe for bean qou-085a (covariance-kernel conjecture), 2026-11-21.

Object: a(k) = Σ_{λ⊢k} (f^λ)^2 χ^λ(3-cycle) = kernelValue(k)/|C_3|, |C_3| = k(k-1)(k-2)/3 (exact integers).
Hypothesis H: a(k) is P-recursive with a recurrence of order r ≤ 3 and polynomial coefficient degree d ≤ 3,
guessed from k = 3..K_fit and checked on held-out k = K_fit+1..40.
PASS: some (r,d) recurrence fitted (exact rational nullspace) on the fit range predicts every held-out term exactly.
FAIL: no (r,d) in range survives held-out terms. A FAIL is scope-limited (a): says nothing about larger r,d.
Arithmetic: Python int / Fraction only, no floats.

Result (run 2026-11-21): FAIL for all 12 (r, d) pairs; the fitted nullspace is empty.
Scope (a): rules out only a low-order holonomic closed form; says nothing about the sign.
"""
from fractions import Fraction
from math import factorial
import sympy as sp
def parts(n,m=None):
    if m is None: m=n
    if n==0: yield (); return
    for i in range(min(n,m),0,-1):
        for p in parts(n-i,i): yield (i,)+p
def f(l):
    n=sum(l); conj=[sum(1 for x in l if x>j) for j in range(l[0])] if l else []
    h=1
    for i,r in enumerate(l):
        for j in range(r): h*= (r-j-1)+(conj[j]-i-1)+1
    return factorial(n)//h
def c2(l): return sum((j-i)**2 for i,r in enumerate(l) for j in range(r))
K=40
a={}
for k in range(3,K+1):
    C3=k*(k-1)*(k-2)//3; s=0
    for l in parts(k):
        fl=f(l); s+=fl**3*(c2(l)-k*(k-1)//2)
    assert s% C3==0; a[k]=s//C3
print({k:a[k] for k in range(3,12)})
import itertools
res=[]
for r in range(1,4):
  for d in range(0,4):
    nunk=(r+1)*(d+1); ks=[k for k in range(3+r,K+1)]
    fit=ks[:nunk+4]; hold=ks[nunk+4:]
    if len(hold)<3: continue
    M=sp.Matrix([[sp.Integer(k)**e*a[k-j] for j in range(r+1) for e in range(d+1)] for k in fit])
    ns=M.nullspace()
    ok=False
    for v in ns:
        if all(sum(v[j*(d+1)+e]*k**e*a[k-j] for j in range(r+1) for e in range(d+1))==0 for k in hold): ok=True
    res.append((r,d,len(ns),ok))
print(res)
