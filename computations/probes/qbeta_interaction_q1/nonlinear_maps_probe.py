#!/usr/bin/env python3
"""Addendum 4 of PREREGISTRATION.md: nonlinear energy maps for the one-sided lepton factor."""
import json, sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[3]
for _p in ("computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))
import mpmath as mp
import qou_substrate.constants as C
mp.mp.dps = 50
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(str(C.M_E_MEV))

def eps(q):
    P = q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1
    d2 = q + 1/q
    eP = q*(-P/q**6)/d2**3
    return eP, eP/q**2, q/d2**4
E0 = me/(q0*(q0-1))/(1-(1-1/q0)**2)
eP, eN, f = eps(q0)
eP1, eN1, f1 = eps(mp.mpf(1))
checks, rows = [], {}
checks.append(("ordering eps_p f < eps_n < eps_p", eP*f < eN < eP))
maps = {"linear": lambda x: x, "abs": abs, "+log": mp.log, "-log": lambda x: -mp.log(x),
        "1/x (hbar/D)": lambda x: 1/x}
for k in (2, -2, mp.mpf(1)/2, -mp.mpf(1)/2):
    maps[f"x^{mp.nstr(k,3)}"] = (lambda kk: (lambda x: x**kk))(k)
for name, g in maps.items():
    pair, Q = E0*(g(eP*f) - g(eP)), E0*(g(eN) - g(eP*f))
    rows[name] = {"lepton_pair_MeV": mp.nstr(pair, 12), "Q_MeV": mp.nstr(Q, 12), "both_positive": bool(pair > 0 and Q > 0)}
    checks.append((f"{name}: not both positive", not (pair > 0 and Q > 0)))
# proton-style affine: subtract each state's q=1 value
pair = E0*((eP*f - eP1*f1) - (eP - eP1)); Q = E0*((eN - eN1) - (eP*f - eP1*f1))
rows["affine, q=1 subtracted"] = {"lepton_pair_MeV": mp.nstr(pair, 12), "Q_MeV": mp.nstr(Q, 12), "both_positive": bool(pair > 0 and Q > 0)}
checks.append(("affine q=1-subtracted: not both positive", not (pair > 0 and Q > 0)))
jump = 1/f
rows["rho-weighted"] = {"needed_rho_final_over_rho_p_gt": mp.nstr(jump, 12), "[2]^4/q": mp.nstr((q0+1/q0)**4/q0, 12)}
for k, v in rows.items():
    print(f"{k:28s} {v}")
print(f"\nm_e = {mp.nstr(me, 12)} MeV (printed only)")
ok = sum(c for _, c in checks)
for d, c in checks:
    print(("PASS " if c else "FAIL ") + d)
print(f"{ok}/{len(checks)}")
out = {"description": "Addendum 4: arbitrary energy maps g(eps) for the one-sided nucleon-rule lepton factor.",
       "q0Anchor": "proton", "q0": mp.nstr(q0, 20), "eps_p": mp.nstr(eP, 20), "eps_n": mp.nstr(eN, 20),
       "f": mp.nstr(f, 20), "maps": rows, "checks": [{"check": d, "pass": bool(c)} for d, c in checks]}
(Path(__file__).parent / "qbeta-one-sided-nonlinear-maps.witness.json").write_text(json.dumps(out, indent=2) + "\n")
sys.exit(0 if ok == len(checks) else 1)
