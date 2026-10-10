#!/usr/bin/env python3
"""The functional side of a convention-D correction on Delta_S has a ceiling below 2.

Bean `qou-cds1`. Numeric companion to
`folio/quantum-observable-universe/lean/QOU/QBeta/DFrameFunctionalFactorCeiling.lean`
(sorry-free). The Lean proves, for every q, that a positive normalised
convention-D admissible functional moves Q_beta off the ruled base by the single
scalar F = w3 / y3(z_D), with

    0 <= F <= ceiling(q) = (q^2+1)^2/(q^4+1) = 1 + 2q^2/(q^4+1) < 2,

and that F > 1  <=>  w21 < y21(z_D). This probe evaluates those objects at the
proton pin, calibrates against two corpus figures, and locates F_required.

WHAT IT FINDS, stated so it is not over-read. The ceiling at q0 is ~1.9786 and
F_required ~1.7592 sits STRICTLY INSIDE (1, ceiling). So magnitude does NOT
exclude a functional-side correction on Delta_S; this is a scope-(a) location,
not a refutation. The interior point corresponds to a (2,1) weight w21* that is
neither 0 (augmentation) nor y21(z_D) (ruled Markov trace) -- the only two
admissible Markov points -- so reaching it needs a free non-Markov weight: one
parameter against one anchor. This probe computes w21* ONLY to show where it
sits relative to the two derived points; it is not a proposed value, it is not
wired anywhere, and per AGENTS.md section NO FITTING it must not be adopted.

PRECISION. mpmath end to end at the substrate compute precision; the pin enters
as the 50-digit proton string. No float arithmetic; float() appears nowhere.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402

mp.mp.dps = 70

# Corpus calibration figures (AGENTS.md Q_beta scoping note 2026-09-14 table,
# recomputed at 70 dps in docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md
# section 5.1). Used ONLY as checks that this probe's base is the corpus's base.
CAL_Q_BASE_ZD = mp.mpf("0.444700408522")
CAL_F_REQ_ZD = mp.mpf("1.75923699418")
CAL_TOL = mp.mpf("1e-11")


def main() -> int:
    results: list[bool] = []

    def chk(name: str, ok: bool, detail: str) -> None:
        results.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    q = mp.mpf(Q_50_DIGIT_STR)
    # Same source as the sibling ruled-base probe (mpf, not the float64
    # mass-difference Q_NEUTRON_MEV).
    m_e = mp.mpf(M_E_MEV)
    q_codata = mp.mpf(Q_BETA_MEV)
    e0 = m_e / (q * (q - 1))                       # order-zero E0
    chi3_abs = (q**4 - 1) / (2 * q**2)            # |chi_(3)(Delta_S)|, exact over Q(q)

    y3d = (q**4 + 1) / (q**2 + 1) ** 2
    y21d = q**2 / (q**2 + 1) ** 2
    ceiling = (q**2 + 1) ** 2 / (q**4 + 1)

    q_base = y3d * chi3_abs * e0
    f_req = q_codata / q_base
    q_aug = chi3_abs * e0                           # w3 = 1, the augmentation

    print("Convention-D functional-factor ceiling on Delta_S, proton pin\n")
    chk("normalisation_y3D_plus_2y21D_is_1",
        abs(y3d + 2 * y21d - 1) < mp.mpf(10) ** (-60),
        f"y3D + 2*y21D - 1 = {mp.nstr(y3d + 2 * y21d - 1, 5)}")
    chk("ruled_base_reproduces_corpus",
        abs(q_base - CAL_Q_BASE_ZD) < CAL_TOL,
        f"Q_base(z_D) = {mp.nstr(q_base, 15)} MeV vs corpus {CAL_Q_BASE_ZD}")
    chk("F_required_reproduces_corpus",
        abs(f_req - CAL_F_REQ_ZD) < CAL_TOL,
        f"F_required = {mp.nstr(f_req, 15)} vs corpus {CAL_F_REQ_ZD}")
    chk("ceiling_equals_augmentation_over_ruled",
        abs(ceiling - q_aug / q_base) < mp.mpf(10) ** (-60),
        f"ceiling = {mp.nstr(ceiling, 15)} = Q_aug/Q_base "
        f"(Q_aug = {mp.nstr(q_aug, 12)} MeV)")
    chk("ceiling_strictly_between_1_and_2",
        1 < ceiling < 2,
        f"1 < {mp.nstr(ceiling, 15)} < 2 (Lean one_lt_ceiling, ceiling_lt_two)")
    chk("F_required_is_interior_not_excluded",
        1 < f_req < ceiling,
        f"1 < F_required = {mp.nstr(f_req, 12)} < ceiling = {mp.nstr(ceiling, 12)}"
        " -- scope (a): the functional side is NOT excluded by magnitude")

    # Where the interior point sits on the admissible line (location only).
    w3_star = f_req * y3d
    w21_star = (1 - w3_star) / 2
    chk("interior_point_is_neither_admissible_Markov_point",
        0 < w21_star < y21d,
        f"w21* = {mp.nstr(w21_star, 12)} strictly between 0 (augmentation) and "
        f"y21D = {mp.nstr(y21d, 12)} (ruled) -- reached only by a free "
        "non-Markov weight; NOT a proposed value")
    chk("lean_equivalence_F_gt_1_iff_w21_below_y21D",
        (f_req > 1) == (w21_star < y21d),
        "one_lt_factor_iff holds at the located point")

    n_ok = sum(results)
    print(f"\n{n_ok}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
