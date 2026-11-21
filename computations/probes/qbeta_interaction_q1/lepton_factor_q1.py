#!/usr/bin/env python3
"""Addendum 5-6 of PREREGISTRATION.md: K-conservation and the q = 1 value of one-sided lepton factors."""
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[3]
for _p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))
import itertools, mpmath as mp, sympy as sp
import qou_substrate.constants as C
mp.mp.dps = 50
q = sp.symbols("q", positive=True); h = q - 1/q; D2 = q + 1/q
R2 = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]); I2 = sp.eye(2)
S1 = sp.kronecker_product(R2, I2); S2 = sp.kronecker_product(I2, R2)
Delta = S1*S2*S1
print("5. K-conservation: K(n)=q^-1 = K(p) K(e) K(nubar), K(p)=q, K(e)=q^(3-2b)")
for nub in (None, 1, -1):
    sols = [b for b in range(4) if -1 == 1 + (3 - 2*b) + (0 if nub is None else nub)]
    print(f"   nubar weight {'absent' if nub is None else 'q^%+d' % nub}: allowed b = {sols}")
secs = {b: [i for i in range(8) if bin(i).count('1') == b] for b in range(4)}
tr = {b: sp.simplify(sum(Delta[i, i] for i in secs[b])) for b in range(4)}
print("   plain sector traces of Delta:", {b: sp.factor(v) for b, v in tr.items()})
epsp1 = sp.Rational(3, 8)
fac = {}
fac["nucleon rule, b=2, with nubar (K=q^-1)/[2]"] = (q**-1 * tr[2] / D2**3) * (q**-1 / D2)
fac["nucleon rule, b=3, with nubar (K=q^+1)/[2]"] = (q**-3 * tr[3] / D2**3) * (q / D2)
fac["nucleon rule, b=2, no nubar factor"] = q**-1 * tr[2] / D2**3
fac["Markov t(Delta) = q^3(q^4+1)/(q^2+1)^2"] = q**3*(q**4+1)/(q**2+1)**2
fac["plain per-sector trace, b=2 (tr/3)"] = tr[2] / 3
q0 = mp.mpf(C.Q_50_DIGIT_STR)
E0full = 1/(q*(q-1))/(1-(1-1/q)**2); me = mp.mpf(str(C.M_E_MEV))
epsP = q * (-(q**12-3*q**10+3*q**8-5*q**6+3*q**4-3*q**2+1)/q**6) / D2**3
epsN = epsP / q**2
print("\n6. one-sided factor on the final state: F = eps_n - eps_p * f")
rows = []
for k, f in fac.items():
    f1 = sp.limit(f, q, 1)
    F1 = epsp1 * (1 - f1)
    Fq0 = sp.lambdify(q, epsN - epsP * f, "mpmath")(q0)
    Qb = me * sp.lambdify(q, E0full, "mpmath")(q0) * abs(Fq0)
    rows.append((k, f1, F1, Qb))
    print(f"   {k:45s} f(1) = {str(f1):5s} F(1) = {str(F1):7s} E0full*|F| at q0 = {mp.nstr(Qb, 9)} MeV")
print("\nComparison (CODATA, outside any proof): Q_beta = 0.78233341 MeV; needs F(1)*(O(h) shape) ~ 0.185")
