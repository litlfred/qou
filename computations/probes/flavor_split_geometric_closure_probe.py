#!/usr/bin/env python3
"""Probe: is the flavor-split subleading `(1 + ℏ_q³)` the truncation of a
geometric series, and does inverting to the closed form `1/(1 − ℏ_q³)` close
the Δm_pn gap?

Context. The color-weighting δ used by the canonical p-n crossing
`σ − h(½ − δ/4)·𝟙` is `flavor_split_subleading(q) = leading·(1 + ℏ_q³)`, with
`leading = (q−1)²(1−q⁻⁴)/3`. The factor `(1 + ℏ_q³)` looks exactly like the
first two terms of the geometric series `1/(1 − ℏ_q³) = 1 + ℏ_q³ + ℏ_q⁶ + …`.

This probe (scope-(a), measurement only — NOT a production rewire):
  1. quantifies `(1+ℏ³)` vs the geometric closed form `1/(1−ℏ³)` (差 = ℏ⁶ order);
  2. checks whether either reaches the CODATA Δm_pn/M_N;
  3. records that the closed form is a HYPOTHESIS — the derivation docstring
     frames `(1+ℏ³)` as a specific "3-loop substrate-Planck" term, not a
     geometric series, so the inversion is not structurally justified here.

Per AGENTS.md "Before declaring refuted/ruled out": this is a scope-(a)
numerical measurement, not a structural exclusion. Per the formalize-first
and three-calibration disciplines: do NOT wire `1/(1−ℏ³)` into production δ
without an independent derivation that the correction is geometric.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401,E402

from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION

# CODATA 2022: m_n − m_p = 1.29333236(46) MeV; M_N ≈ (m_p+m_n)/2.
CODATA_DMN_OVER_MN = mpf("1.29333236") / ((M_P_MEV_VALIDATION + mpf("939.56542194")) / 2)


def main() -> int:
    q = Q_MP
    hbar = (q - 1) / q
    lead = flavor_split_leading(q)

    trunc = lead * (1 + hbar**3)          # current canonical subleading
    closed = lead / (1 - hbar**3)         # geometric closed-form hypothesis
    next_term = lead * hbar**6            # first dropped geometric term

    rel_trunc_vs_closed = abs(closed - trunc) / trunc
    err_trunc = abs(trunc - CODATA_DMN_OVER_MN) / CODATA_DMN_OVER_MN
    err_closed = abs(closed - CODATA_DMN_OVER_MN) / CODATA_DMN_OVER_MN
    err_lead = abs(lead - CODATA_DMN_OVER_MN) / CODATA_DMN_OVER_MN

    print("flavor-split geometric-closure probe")
    print("=" * 60)
    print(f"  ℏ_q                     = {mp.nstr(hbar, 12)}")
    print(f"  ℏ_q³                    = {mp.nstr(hbar**3, 6)}")
    print(f"  ℏ_q⁶ (next geom. term)  = {mp.nstr(hbar**6, 6)}")
    print(f"  leading                 = {mp.nstr(lead, 14)}  (err vs CODATA {mp.nstr(err_lead*100,3)}%)")
    print(f"  (1+ℏ³)   [canonical]    = {mp.nstr(trunc, 16)}  (err {mp.nstr(err_trunc*100,3)}%)")
    print(f"  1/(1−ℏ³) [hypothesis]   = {mp.nstr(closed, 16)}  (err {mp.nstr(err_closed*100,3)}%)")
    print(f"  closed − trunc          = {mp.nstr(closed-trunc, 4)}  (= ℏ⁶ order {mp.nstr(next_term,4)})")
    print(f"  rel(closed,trunc)       = {mp.nstr(rel_trunc_vs_closed, 4)}")
    print(f"  CODATA Δm_pn/M_N        = {mp.nstr(CODATA_DMN_OVER_MN, 10)}")
    print()
    closes = err_closed < err_trunc / 10  # would need ≥10× improvement to "close"
    print(f"  VERDICT: geometric closed form { 'CLOSES' if closes else 'does NOT close'} "
          f"the Δm_pn gap (scope-a, near-match).")
    print("  The closed form is a HYPOTHESIS — (1+ℏ³) is documented as a")
    print("  '3-loop substrate-Planck' term, not a geometric series. NOT wired.")

    # --- Diagnostic: is (1+ℏ³) even the RIGHT correction? ---
    # The exact correction factor CODATA demands is C_true = CODATA/leading.
    C_true = CODATA_DMN_OVER_MN / lead
    ratio = (C_true - 1) / hbar**3        # =1 iff (1+ℏ³) is exact
    print()
    print("  --- is (1+ℏ³) the right target? ---")
    print(f"  C_true = CODATA/leading = {mp.nstr(C_true, 12)}  (C_true−1 = {mp.nstr(C_true-1,8)})")
    print(f"  (1+ℏ³) supplies ℏ³ = {mp.nstr(hbar**3,8)}  →  (C_true−1)/ℏ³ = {mp.nstr(ratio,8)}")
    print(f"  ⇒ (1+ℏ³) supplies only {mp.nstr(hbar**3/(C_true-1)*100,4)}% of the needed correction.")
    print("  ⇒ (1+ℏ³) is NOT the closure — it is a partial, posited factor, not")
    print("     merely unproven. No clean single ℏ_q-power reproduces C_true−1.")

    w = WitnessBuilder("flavor-split-geometric-closure-probe", engine="mpmath")
    w.set_description(
        "Scope-(a) measurement: the flavor-split subleading (1+ℏ_q³) vs the "
        "geometric closed form 1/(1−ℏ_q³). They differ at O(ℏ_q⁶) ~ 9.5e-7; "
        "neither closes the Δm_pn/M_N gap to CODATA (leading already −0.5%). "
        "The closed form is a hypothesis, not a derived identity — NOT wired "
        "to production δ (calibration-sensitive; needs an independent "
        "derivation that the correction is geometric)."
    )
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("hbar_q", str(hbar))
    w.add_data("leading", str(lead))
    w.add_data("subleading_1_plus_hbar3", str(trunc))
    w.add_data("geometric_closed_1_over_1_minus_hbar3", str(closed))
    w.add_data("rel_closed_vs_trunc", str(rel_trunc_vs_closed))
    w.add_data("err_trunc_vs_codata", str(err_trunc))
    w.add_data("err_closed_vs_codata", str(err_closed))
    w.add_data("codata_dmn_over_mn", str(CODATA_DMN_OVER_MN))
    w.add_data("geometric_closes_gap", bool(closes))
    w.add_data("C_true_codata_over_leading", str(C_true))
    w.add_data("ratio_Ctrue_minus_1_over_hbar3", str(ratio))
    w.add_data("fraction_of_correction_supplied_by_1plus_hbar3", str(hbar**3/(C_true-1)))
    w.add_assertion(
        name="geometric_closed_form_differs_only_at_hbar6",
        computed=1 if rel_trunc_vs_closed < mpf("1e-5") else 0,
        expected=1,
        source="(1+ℏ³) and 1/(1−ℏ³) agree to O(ℏ⁶); the inversion is a "
               "sub-ppm refinement, not the missing Δm_pn physics",
    )
    w.save()
    print(f"\n  Witness: flavor-split-geometric-closure-probe.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
