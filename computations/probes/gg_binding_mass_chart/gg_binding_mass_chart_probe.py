#!/usr/bin/env python3
"""
gg_binding_mass_chart_probe.py -- owner card 2026-11-27, "Look for the missing gg piece".

QUESTION. On the ruled gamma-gamma chain (docs/audits/2026-11-22-light-nuclei-a2-a3-gg-chain.md),
every light nucleus unbinds in the log chart, B = -E0 ln R with R = tr_atom/tr_free.
Does the energy reading of the ring mass (PR #9789, U = -q d/dq log m) change that,
and by how much?

INPUTS. No new choice is made. R = prod over bonds of mu_x, with the exact Q(q) block
traces and bond factors from light-nuclei-a2-a3.witness.json (chain law towerTr_ggChain).
The ring framing factor [2]^n q^(-n-2w) cancels in R: the strand count is the same bound
and free, and the gamma-gamma vertex s_i s_{i+1}^-1 has writhe 0. So the ring ratio
equals the raw ratio.

READINGS
  log chart:   B_log  = -E0 ln R                 (E0 = 4.2274833556 MeV, as in the audit)
  mass chart:  B_mass = U_free - U_bound = q d/dq ln R, in electron units
               m_e / U_e with U_e = 3 - D[4]/[4] (PR #9789)

STRUCTURE. The bond V^3 = gamma(0,0,qh) gamma(0,0,-h/q) (CLAUDE.md photon ruling).
At h = 0 each factor is the bare photon, which equals 1 (QOU.StandardModel.photon_bare).
So R(1) = 1 and every bond effect vanishes at q = 1. The audit measures the order: y^4,
with y = q^2 - 1. Then B_log = O(y^4) and B_mass = O(y^3). At q0 these are 1e-3 to 1e-2
of a per-bond unit, whatever the unit is.

AME is used only in a comparison column. Scope (a).
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path[:0] = [str(COMP / "substrate"), str(COMP)]
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

mp.mp.dps = 50
QR = sp.Rational(Q_50_DIGIT_STR)
M_E = mp.mpf("0.51099895069")
E0 = mp.mpf("4.2274833556")
AME_KEV = {k: mp.mpf(v) for k, v in {"2H": "2224.566", "3H": "8481.798", "3He": "7718.043", "4He": "28295.673"}.items()}  # comparison only

q = sp.symbols("q", positive=True)


def ev(expr):
    return mp.mpf(str(sp.N(expr.subs(q, QR), 45)))


def main() -> int:
    sym = json.loads((COMP / "probes/light_nuclei_a2_a3/light-nuclei-a2-a3.witness.json").read_text())["symbolic"]
    mu = {k: sp.sympify(sym[k]["bond_factor"], locals={"q": q}) / sp.sympify(sym[k]["tr"], locals={"q": q}) for k in "pn"}
    i4 = q**3 + q + 1 / q + q**-3
    U_e = ev(3 - q * sp.diff(i4, q) / i4)

    cells = {"2H": mu["n"], "3H": mu["n"] ** 2, "3He": mu["p"] * mu["n"], "4He": mu["p"] * mu["n"] ** 2}
    out, checks = {}, {}
    for name, R in cells.items():
        w = q * sp.diff(sp.log(R), q)
        Rv, wv = ev(R), ev(w)
        b_log = -E0 * mp.log(Rv) * 1000
        b_mass = M_E * wv / U_e * 1000
        out[name] = {"R": mp.nstr(Rv, 20), "B_log_keV": mp.nstr(b_log, 8), "B_mass_keV": mp.nstr(b_mass, 8),
                     "AME_keV": mp.nstr(AME_KEV[name], 10), "AME_over_B_mass": mp.nstr(AME_KEV[name] / b_mass, 6)}
        checks[f"{name}_R_at_q1_is_1"] = sp.simplify(R.subs(q, 1) - 1) == 0
        checks[f"{name}_log_unbinds"] = b_log < 0
        checks[f"{name}_mass_binds"] = b_mass > 0
        print(f"{name:4s} R={mp.nstr(Rv, 12)}  B_log={mp.nstr(b_log, 6):>9} keV  "
              f"B_mass={mp.nstr(b_mass, 6):>8} keV  AME/B_mass={mp.nstr(AME_KEV[name] / b_mass, 5)}")
    # observed order is the opposite (3H more bound); recorded, not a pass of the model
    checks["mass_chart_mirror_order_3He_gt_3H"] = mp.mpf(out["3He"]["B_mass_keV"]) > mp.mpf(out["3H"]["B_mass_keV"])
    print(f"U_e = {mp.nstr(U_e, 12)}; unit m_e/U_e = {mp.nstr(M_E / U_e * 1000, 8)} keV")
    for k, v in checks.items():
        print(("PASS " if v else "FAIL ") + k)

    if WitnessBuilder is not None:
        wb = WitnessBuilder("gg-binding-mass-chart", engine="mpmath+sympy")
        wb.set_description("Light-nucleus binding on the ruled gamma-gamma chain in the log and mass "
                           "(ring-energy) charts; AME only for comparison.")
        for k, v in checks.items():
            wb.add_assertion(k, computed=str(bool(v)), expected="True", tolerance="0")
        wb.add_data("U_e", mp.nstr(U_e, 20))
        wb.add_data("E0_MeV", mp.nstr(E0, 12))
        wb.add_data("cells", out)
        wb.save()
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
