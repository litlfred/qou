#!/usr/bin/env python3
"""²H, ³H, ³He on the ruled γγ bond, exact (issue #9039; preregistration.md).

Ruling 2026-11-22: vertex σ_iσ_{i+1}⁻¹ (reading A), closure on the right, so a bond
enters the newer nucleon ("left entry" of ../he4_sign_conventions). Chain law
(towerTr_ggChain, proved): tr_atom = tr(N₀) · ∏_{j≥1} tr(V³ · N_j↑¹).

1. Symbolic ℚ(q): tr(x), bond factor b(x) = tr(V³ · x↑¹), μ_x = b(x)/tr(x) for x ∈ {p, n},
   and the sign of μ_x − 1 for every q > 1 via positive coefficients in y = q² − 1.
2. Exact Fractions at the proton 50-digit pin: every order of ²H, ³H, ³He (and ⁴He ppnn as
   control), B_diff = E₀(tr_free − tr_atom), B_log = E₀ ln(tr_free/tr_atom).
3. Control: one chain evaluated from the full word, not from the chain law.
No float in any computed quantity; mpmath only formats. AME is comparison only.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "he4_closed_form"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools", "qou-substrate", "python"))
from hecke_exact import Ring  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

mp.mp.dps = 40
E0_MEV = Fraction("4.227483355629030550268056026587211153615")  # he4-gg-all-pairs.witness.json
AME_KEV = {"2H": Fraction("2224.566"), "3H": Fraction("8481.798"),
           "3He": Fraction("7718.043"), "4He": Fraction("28295.673")}  # AME2020, comparison only


def sh(L, k):
    return [(a, b, i + k) for a, b, i in L]


def fx(x):
    return mp.mpf(x.numerator) / x.denominator


# ---- 1. symbolic ----------------------------------------------------------------
RS = Ring()
qq, yy = sp.symbols("q y")
sym = {}
for name, blk in (("p", RS.proton()), ("n", RS.neutron())):
    t = RS.tr(3, blk)
    b = RS.tr(4, RS.V3(0) + sh(blk, 1))
    m1 = sp.factor(sp.sympify(str((b / t - 1).as_expr())).subs("q", qq))
    # m1 = (q² − 1)^k · F(q²); write F in y = q² − 1 and require every coefficient of its
    # numerator and denominator to be ≥ 0 with a positive constant term (so F > 0 for y > 0).
    k = 0
    F = m1
    while sp.cancel(F).subs(qq, 1) == 0:
        F = sp.cancel(F / (qq**2 - 1))
        k += 1
    assert sp.simplify(F - F.subs(qq, -qq)) == 0, "F not even in q"
    Fy = sp.cancel(F.subs(qq, sp.sqrt(yy + 1)))
    nF, dF = (sp.Poly(sp.expand(e), yy) for e in sp.fraction(Fy))
    pos = (all(c >= 0 for c in nF.all_coeffs()) and nF.eval(0) != 0
           and all(c >= 0 for c in dF.all_coeffs()) and dF.eval(0) != 0
           and (nF.eval(0) > 0) == (dF.eval(0) > 0))
    y_pow = k
    pieces = {"num_rest": pos, "den": pos}
    sym_y = {"num_coeffs_in_y": [str(c) for c in nF.all_coeffs()[::-1]],
             "den_coeffs_in_y": [str(c) for c in dF.all_coeffs()[::-1]]}
    sym[name] = {"tr": str(sp.factor(sp.sympify(str(t.as_expr())))),
                 "bond_factor": str(sp.factor(sp.sympify(str(b.as_expr())))),
                 "mu_minus_1": str(m1), "y_power": int(y_pow),
                 "positive_for_q_gt_1": bool(pos), **sym_y}
    print(name, "mu-1 =", m1, "| y-power", y_pow, "| positive for q>1:", sym[name]["positive_for_q_gt_1"])

# ---- 2. exact at the pin ----------------------------------------------------------
R = Ring(Fraction(Q_50_DIGIT_STR))
N = {"p": R.proton(), "n": R.neutron()}
t = {k: R.tr(3, v) for k, v in N.items()}
bL = {k: R.tr(4, R.V3(0) + sh(v, 1)) for k, v in N.items()}
mu = {k: bL[k] / t[k] for k in N}

checks = {"chain_law_vs_full_word_2H_pn": R.tr(6, N["p"] + sh(N["n"], 3) + R.V3(2)) == t["p"] * bL["n"],
          "mu_p_gt_1": mu["p"] > 1, "mu_n_gt_1": mu["n"] > 1}
NUCLEI = {"2H": "pn", "3H": "pnn", "3He": "ppn", "4He": "ppnn"}
rows = []
for iso, comp in NUCLEI.items():
    orders = sorted(set("".join(o) for o in itertools.permutations(comp)))
    if iso == "4He":
        orders = ["ppnn"]
    for order in orders:
        free = Fraction(1)
        for x in order:
            free *= t[x]
        atom = t[order[0]]
        for x in order[1:]:
            atom *= bL[x]
        Bd = E0_MEV * 1000 * (free - atom)
        Bl = fx(E0_MEV) * 1000 * mp.log(fx(free) / fx(atom))
        rows.append({"nucleus": iso, "order": order, "bonds_enter": order[1:],
                     "tr_free": mp.nstr(fx(free), 30), "tr_atom": mp.nstr(fx(atom), 30),
                     "ratio_atom_over_free": mp.nstr(fx(atom / free), 30),
                     "B_diff_keV": mp.nstr(fx(Bd), 15), "B_log_keV": mp.nstr(Bl, 15),
                     "AME_keV_comparison_only": mp.nstr(fx(AME_KEV[iso]), 10)})
        print(f"{iso:4s} {order:5s} ratio={mp.nstr(fx(atom / free), 15)}  "
              f"B_diff={mp.nstr(fx(Bd), 8)} keV  B_log={mp.nstr(Bl, 8)} keV")
checks["all_rows_unbind"] = all(mp.mpf(r["B_diff_keV"]) < 0 for r in rows)
print(checks)
assert all(checks.values())

out = {"q0Anchor": "proton", "q0AnchorReason": "exact Fractions at the proton 50-digit pin",
       "issue": 9039, "preregistration": "preregistration.md",
       "rulings": "owner-rulings 2026-11-22: reading A, right-hand closure (bond enters newer nucleon)",
       "E0_MeV": str(E0_MEV), "symbolic": sym,
       "mu_minus_1_at_pin": {k: mp.nstr(fx(mu[k] - 1), 30) for k in N},
       "rows": rows, "checks": checks,
       "note": "PROBE, adopts nothing. AME values are comparison fields only."}
with open(os.path.join(HERE, "light-nuclei-a2-a3.witness.json"), "w") as fh:
    json.dump(out, fh, indent=1, ensure_ascii=False)
