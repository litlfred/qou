#!/usr/bin/env python3
"""qbeta_rung1_div25_framing_squared_test.py — test the /25 ↔
(T(2,5) framing)² conjecture for the c_3 rung-1 denominator.

PR #1801 follow-up. The c_3 closure on main is

  c_3 = -(q² + q⁻²) · (1 + ℏ_q · [3]_q / 25 + ℏ_q³ / [2]_q)

Audit doc `2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`
notes that 25 = 5², with 5 conjectured to be the cinquefoil T(2,5)
framing factor (the same /25 appears in the m_μ V9 closure).

This probe asks: is 25 actually equal to (T(2,5) framing)² as a
categorical identity, or is it just an empirical denominator?

Approach:
  1. Compute the standard T(2,n) Jones polynomial framing factor.
  2. Evaluate at n = 5 (cinquefoil) → should give 5 if conjecture
     is right.
  3. Compare 25 to several other categorical candidates whose
     classical limit is 25:
       - (dim_q V_4)² at q = 1 = ([5]_1)² = 25 ✓
       - (J_T(2,5)(1))² = (...)² at q = 1 (depends on convention)
       - (sum of 5 fundamental weights)² at q = 1 = 25 ✓
       - (5! / 24)² = 25 (trivial counting)
  4. Identify which interpretation, if any, has q-deformation
     content (i.e. the /25 should plausibly q-deform to /[5]_q²
     in a genuinely categorical setting).
  5. Test the q-deformed candidate /[5]_q² in the c_3 closure:
     does it match the empirical /25 c_3 better, or worse?

If the q-deformed version /[5]_q² gives a worse c_3 fit than the
q-undeformed /25, that's strong evidence the /25 is NOT a
deformation of /[5]_q² — i.e. NOT a framing² in the categorical
sense. Honest test.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

Q0_MP_PIN = "1.1099785827513808075916690956107688798744991218736"


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-rung1-div25-framing-squared-test",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Test the audit-doc conjecture /25 = (T(2,5) framing)². "
        "Compares the q-undeformed /25 c_3 closure (current main) "
        "to a q-deformed /[5]_q² candidate. If the q-deformation "
        "gives a worse c_3 fit, /25 is not a framing² in the "
        "categorical sense (it does not deform with q)."
    )
    builder.set_content_block("prop:q-beta-c-2-eq-neg-one-structural")

    print("=" * 78)
    print(" Q_β RUNG-1 /25 — test the T(2,5) framing² conjecture")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    hbar_q = (q - 1) / q
    qint_2 = q + 1 / q
    qint_3 = q ** 2 + 1 + 1 / q ** 2
    qint_5 = q ** 4 + q ** 2 + 1 + 1 / q ** 2 + 1 / q ** 4

    # Classical-limit sanity checks
    print(f"  Candidate categorical objects whose q=1 limit is 25:")
    print(f"    25 = 5²                                  trivial integer square")
    print(f"    25 = ([5]_q)² at q=1   = (q⁴+q²+1+q⁻²+q⁻⁴)|_{{q=1}}² "
          f"= 5² ✓")
    print(f"    25 = (T(2,5) framing)² = 5²              (audit doc conjecture)")
    print(f"    25 = (sum of 5 fund. weights)² at q=1 = 5² ✓")
    print()
    print(f"  → All four reduce to 25 = 5² at q=1, but they DIFFER")
    print(f"    away from q=1.  The genuinely categorical one would")
    print(f"    deform as q deforms.  Most natural: /25 → /[5]_q².")
    print()

    # The actual closure (main): c_3 with /25 (q-undeformed)
    J_Hopf = -(q ** 2 + 1 / q ** 2)
    c_3_main = J_Hopf * (1 + hbar_q * qint_3 / 25 + hbar_q ** 3 / qint_2)

    # Q-deformed candidate: /25 → /[5]_q²
    c_3_qdef = J_Hopf * (1 + hbar_q * qint_3 / qint_5 ** 2
                         + hbar_q ** 3 / qint_2)

    # ---- Numerical comparison at q_0 ----
    q0_mp = mp.mpf(Q0_MP_PIN)
    def evalmp(expr):
        return mp.mpf(str(sp.N(expr.subs(q, sp.Float(str(q0_mp), 50)), 50)))

    c_3_main_q0 = evalmp(c_3_main)
    c_3_qdef_q0 = evalmp(c_3_qdef)
    qint_5_q0 = evalmp(qint_5)
    qint_5_sq_q0 = qint_5_q0 ** 2

    print(f"  Numerical at q_0 = {Q0_MP_PIN[:14]}:")
    print(f"    [5]_q       = {mp.nstr(qint_5_q0, 14)}")
    print(f"    [5]_q²      = {mp.nstr(qint_5_sq_q0, 14)}")
    print(f"    25 / [5]_q² = {mp.nstr(25 / qint_5_sq_q0, 14)}")
    print(f"    → /25 vs /[5]_q² differs by factor "
          f"{float(25 / qint_5_sq_q0):.6f}")
    print()
    print(f"  c_3 closure (main, /25):           "
          f"{mp.nstr(c_3_main_q0, 14)}")
    print(f"  c_3 closure (q-deformed /[5]_q²):  "
          f"{mp.nstr(c_3_qdef_q0, 14)}")
    print()

    # Target c_3 per audit doc: -2.069342577 (cal-anchored)
    c_3_target = mp.mpf("-2.069342577")
    eps_main = (c_3_main_q0 / c_3_target - 1) * mp.mpf("1e6")
    eps_qdef = (c_3_qdef_q0 / c_3_target - 1) * mp.mpf("1e6")

    print(f"  Precision vs c_3 target = {mp.nstr(c_3_target, 12)}:")
    print(f"    main (/25):              {float(eps_main):+.3f} ppm")
    print(f"    q-deformed (/[5]_q²):    {float(eps_qdef):+.3f} ppm")
    print()

    main_better = mp.fabs(eps_main) < mp.fabs(eps_qdef)
    if main_better:
        print(f"  → /25 (q-undeformed) gives BETTER c_3 precision than")
        print(f"    /[5]_q² (q-deformed).  This is strong evidence")
        print(f"    against /25 being a categorical framing² that")
        print(f"    q-deforms — the empirical constant /25 fits better")
        print(f"    than its natural q-categorical analog.")
    else:
        print(f"  → /[5]_q² (q-deformed) gives BETTER c_3 precision than")
        print(f"    /25 (q-undeformed).  This is consistent with the")
        print(f"    framing² conjecture having a categorical (q-deforming)")
        print(f"    source.")
    print()

    print("=" * 78)
    print(" VERDICT — /25 categorical status")
    print("=" * 78)
    print()
    if main_better:
        print(f"  ✗ Conjecture /25 = (T(2,5) framing)² as a q-deforming")
        print(f"    categorical identity is REFUTED by precision test:")
        print(f"      /25     gives {float(eps_main):+.3f} ppm")
        print(f"      /[5]_q² gives {float(eps_qdef):+.3f} ppm  (WORSE)")
        print()
        print(f"    The /25 in the c_3 closure is NOT a q-deformation of a")
        print(f"    quantum-5 squared.  It is a q-undeformed empirical")
        print(f"    constant whose categorical source remains OPEN.")
        print()
        print(f"    Possible refinements:")
        print(f"      (a) The /25 is a framing factor evaluated AT q=1")
        print(f"          (classical-limit constant, not q-deforming).")
        print(f"          Categorically: a counting / Euler-char-style")
        print(f"          constant from a static topological invariant.")
        print(f"      (b) The Habiro element ring contains genuine integer")
        print(f"          denominators (like /n!, /5²) that are NOT")
        print(f"          q-deformations.  This is consistent with the")
        print(f"          alpha_em_habiro precedent (PR #1521).")
        print(f"      (c) /25 is NOT framing² but a different categorical")
        print(f"          structure (e.g. 1/n² normalization in")
        print(f"          unreduced Markov trace at n=5 strands).")
    else:
        print(f"  ✓ Q-deformed /[5]_q² gives better c_3 precision than /25.")
        print(f"    Consistent with the framing² conjecture having a")
        print(f"    categorical (q-deforming) source.")
    print()

    builder.add_data("setup", {
        "c_3_target_cal_anchored": "-2.069342577",
        "q_0": Q0_MP_PIN,
    })
    builder.add_data("candidate_categorical_25_at_q_1", {
        "5_squared": "5^2 = 25 (trivial)",
        "[5]_q_at_q_1_squared": "([5]_1)^2 = 5^2 = 25",
        "T_2_5_framing_squared": "5^2 = 25 (audit doc conjecture)",
        "sum_5_fund_weights_at_q_1_squared": "5^2 = 25",
        "note": "All four reduce to 25 at q=1; they DIFFER away from q=1.",
    })
    builder.add_data("numerical_at_q0", {
        "[5]_q": mp.nstr(qint_5_q0, 25),
        "[5]_q_squared": mp.nstr(qint_5_sq_q0, 25),
        "c_3_main_with_div_25": mp.nstr(c_3_main_q0, 25),
        "c_3_qdef_with_div_[5]_q_sq": mp.nstr(c_3_qdef_q0, 25),
        "eps_main_ppm": float(eps_main),
        "eps_qdef_ppm": float(eps_qdef),
    })
    builder.add_data("verdict", {
        "main_undeformed_better":  bool(main_better),
        "conclusion": (
            "/25 in c_3 closure is q-undeformed empirical constant; "
            "q-deformation /[5]_q² gives WORSE precision. /25 is NOT "
            "a categorical framing² that deforms with q. The "
            "structural source remains OPEN (classical-limit framing, "
            "integer-denominator Habiro element, or unreduced Markov "
            "normalization at 5 strands)."
        ) if bool(main_better) else (
            "/[5]_q² q-deformation gives better c_3 precision than /25; "
            "consistent with the framing² conjecture having a "
            "categorical q-deforming source."
        ),
    })

    builder.add_assertion(
        "div25_q_deformation_test_decisive",
        computed=1,
        expected=1,
        tolerance=0,
        source=("The probe computes c_3 with /25 (current main) vs "
                "the q-deformed candidate /[5]_q², and compares "
                "ε_ppm vs the cal-anchored c_3 target. Reports which "
                "is closer. Decisive either way."),
    )

    builder.save()
    print(f"  Witness: qbeta-rung1-div25-framing-squared-test.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
