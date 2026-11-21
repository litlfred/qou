#!/usr/bin/env python3
"""Addendum 3 of PREREGISTRATION.md: which energy is E0*F for the one-sided nucleon rule?

Readings are judged by sign consistency with the energy map they use; the CODATA numbers are
printed last and are not used to decide anything.
"""
import json, sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[3]
for _p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))
import mpmath as mp
import sympy as sp
import qou_substrate.constants as C
mp.mp.dps = 50

q = sp.symbols("q", positive=True)
D2 = q + 1/q
P = q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1
epsP = q*(-P/q**6)/D2**3
epsN = epsP/q**2
f = q/D2**4
F = epsN - epsP*f
assert sp.simplify(F - ((epsN - epsP) + epsP*(1 - f))) == 0

q0 = mp.mpf(C.Q_50_DIGIT_STR)
me = mp.mpf(str(C.M_E_MEV))
ev = lambda e: sp.lambdify(q, e, "mpmath")(q0)
E0s = {"order-zero": me/(q0*(q0-1)), "tower": me/(q0*(q0-1))/(1-(1-1/q0)**2)}
eP, eN, fv = ev(epsP), ev(epsN), ev(f)
out = {"q0": mp.nstr(q0, 20), "eps_p": mp.nstr(eP, 20), "eps_n": mp.nstr(eN, 20),
       "f": mp.nstr(fv, 20), "readings": {}}
checks = []
for name, E0 in E0s.items():
    lin = {"E(n)": E0*eN, "E(p)": E0*eP, "E(p e nubar)": E0*eP*fv}
    lin_pair = lin["E(p e nubar)"] - lin["E(p)"]
    lin_np = lin["E(n)"] - lin["E(p)"]
    lin_Q = lin["E(n)"] - lin["E(p e nubar)"]
    rec = {"linear": {"lepton_pair_MeV": mp.nstr(lin_pair, 15), "E_n_minus_E_p_MeV": mp.nstr(lin_np, 15),
                      "E0F_MeV": mp.nstr(lin_Q, 15),
                      "Qbeta_reading_consistent": bool(lin_pair > 0),
                      "mn_mp_reading_consistent": bool(abs(lin_np - lin_Q) < mp.mpf(10)**-30)}}
    for sgn in (+1, -1):
        Ex = lambda e: sgn*E0*mp.log(e)
        pair = Ex(eP*fv) - Ex(eP)
        Q = Ex(eN) - Ex(eP*fv)
        np_ = Ex(eN) - Ex(eP)
        rec[f"log sign {sgn:+d}"] = {"lepton_pair_MeV": mp.nstr(pair, 15), "Q_MeV": mp.nstr(Q, 15),
                                    "E_n_minus_E_p_MeV": mp.nstr(np_, 15),
                                    "both_positive": bool(pair > 0 and Q > 0)}
        checks.append((f"{name} log {sgn:+d}: pair and Q not both positive", not (pair > 0 and Q > 0)))
    out["readings"][name] = rec
    checks.append((f"{name} linear: Q_beta reading inconsistent (pair < 0)", lin_pair < 0))
    checks.append((f"{name} linear: m_n-m_p reading inconsistent (E(n)-E(p) < 0 < E0F)",
                   lin_np < 0 < lin_Q))

for name, rec in out["readings"].items():
    print(f"== E0 {name}")
    for k, v in rec.items():
        print(f"   {k}: {v}")
print(f"\nm_e = {mp.nstr(me, 12)} MeV (CODATA, printed only)")
ok = sum(c for _, c in checks)
for d, c in checks:
    print(("PASS " if c else "FAIL ") + d)
print(f"{ok}/{len(checks)}")
out["checks"] = [{"check": d, "pass": bool(c)} for d, c in checks]
out["description"] = ("Addendum 3: reading of E0*F for the one-sided nucleon-rule lepton factor. "
                      "Linear and log energy maps; sign consistency decides, CODATA printed only.")
out["q0Anchor"] = "proton"
(Path(__file__).parent / "qbeta-one-sided-reading.witness.json").write_text(json.dumps(out, indent=2) + "\n")
sys.exit(0 if ok == len(checks) else 1)
