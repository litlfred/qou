#!/usr/bin/env python3
"""Addendum 5: the window a non-product final-state trace must land in."""
import json, sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_ROOT / "tools/qou-substrate/python"))
import mpmath as mp
import qou_substrate.constants as C
mp.mp.dps = 50
q = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(str(C.M_E_MEV))
P = q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1
d2 = q + 1/q
eP = q*(-P/q**6)/d2**3; eN = eP/q**2; f = q/d2**4; prod = eP*f
E0 = me/(q*(q-1))/(1-(1-1/q)**2)
out = {"eps_p": mp.nstr(eP, 15), "eps_n": mp.nstr(eN, 15), "product": mp.nstr(prod, 15),
       "window": [mp.nstr(eN, 15), mp.nstr(eP, 15)],
       "lift_needed_min": mp.nstr(eN - prod, 15), "lift_needed_max": mp.nstr(eP - prod, 15),
       "lift_min_over_product": mp.nstr((eN - prod)/prod, 10), "maps": {}}
maps = {"-log": (lambda x: -E0*mp.log(x), lambda e: lambda E: e*mp.e**(-E/E0)),
        "1/x": (lambda x: E0/x, None)}
for name, (g, _) in maps.items():
    np_ = g(eN) - g(eP)
    if name == "-log":
        x = eP*mp.e**(-me/E0)          # g(x) - g(eP) = m_e
    else:
        x = 1/(me/E0 + 1/eP)
    Q = g(eN) - g(x)
    out["maps"][name] = {"E(n)-E(p)_MeV": mp.nstr(np_, 12), "x_for_pair_eq_me": mp.nstr(x, 15),
                         "x_in_window": bool(eN < x < eP), "Q_then_MeV": mp.nstr(Q, 12),
                         "cross_term_needed": mp.nstr(x - prod, 15)}
print(json.dumps(out, indent=1))
print("CODATA (printed only): Q_beta 0.78233 MeV, m_n-m_p 1.29333 MeV")
(Path(__file__).parent / "qbeta-nonproduct-window.witness.json").write_text(
    json.dumps({"description": "Addendum 5: window for a non-product final-state trace", "q0Anchor": "proton", **out}, indent=2) + "\n")
