#!/usr/bin/env python3
"""Addendum 2 of PREREGISTRATION.md: nucleon vs Markov lepton factor, one-sided vs shared."""
import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[3]
for _p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))
import mpmath as mp, sympy as sp
import qou_substrate.constants as C
mp.mp.dps = 50
q = sp.symbols("q", positive=True); D2 = q + 1/q
P = q**12-3*q**10+3*q**8-5*q**6+3*q**4-3*q**2+1
epsP = q*(-P/q**6)/D2**3; epsN = epsP/q**2
rules = {"nucleon rule f=q/[2]^4 (K-sector x nubar)": (q/D2**4, "restricted to the K-allowed sector"),
         "Markov f=t(Delta)=q^3(q^4+1)/(q^2+1)^2": (q**3*(q**4+1)/(q**2+1)**2, "sums all four sectors, incl. K-forbidden")}
E0 = {"order-zero": 1/(q*(q-1)), "tower": 1/(q*(q-1))/(1-(1-1/q)**2)}
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(str(C.M_E_MEV))
ev = lambda e: sp.lambdify(q, e, "mpmath")(q0)
QB, NP = mp.mpf("0.78233341"), mp.mpf("1.29333251")
for name, (f, kc) in rules.items():
    for place, F in (("one-sided", epsN - epsP*f), ("shared", (epsN - epsP)*f)):
        Fq = ev(F); F1 = sp.limit(F, q, 1); c = sp.limit(F/(q-1), q, 1) if F1 == 0 else "~E0 (order 0)"
        vals = {k: me*ev(e)*Fq for k, e in E0.items()}
        print(f"{name} | {place}\n   K: {kc}\n   sign F(q0) = {'+ (neutron heavier)' if Fq > 0 else '- (neutron lighter)'};  F(1) = {F1};  q->1: {c}")
        print("   Q (order-zero E0) = %s MeV, Q (tower E0) = %s MeV" % (mp.nstr(vals['order-zero'], 9), mp.nstr(vals['tower'], 9)))
        t = vals['tower']
        print("   vs Q_beta %+.2f %%, vs m_n-m_p %+.2f %%" % (float((abs(t)/QB-1)*100), float((abs(t)/NP-1)*100)))
