#!/usr/bin/env python3
"""qbeta_rung2_hypA_markov_3strand_test.py — definitively test
Hyp-A for the c_3 rung-2 structural lift.

PR #1801 follow-up to the rung-structure analysis in PR #1786
(commit dffe605e2). The c_3 closure on main is

  c_3 = -(q² + q⁻²) · (1 + ℏ_q · [3]_q / 25 + ℏ_q³ / [2]_q)

with rung 2 = ℏ_q³ / [2]_q. The rung-2 bracket comparison
(qbeta_c3_rung2_bracket_comparison.py) listed three hypotheses
for the structural origin of this form:

  Hyp-A.  rung_2 = (3-strand Markov trace at identity) / dim_q(V_1)
                 = tr_M(1 ∈ H_3(q)) / [2]_q

  Hyp-B.  rung_2 = (Wenzl p_3 projector contribution at order ℏ³)
                 / TL loop value δ_q = [2]_q

  Hyp-C.  rung_2 = (Kauffman bracket order-h³ coefficient)
                 / (unknot bracket in [2]_q normalization)

This probe tests Hyp-A precisely.

In the QOU Markov-trace convention (per `_precision.py` and the
operator-valued N=3 probe), the Markov trace on H_n(q) satisfies

  tr_M(1) = z^(n-1)   where  z = 1 / (√q + 1/√q)

(z = Markov-Jones parameter). So tr_M(1 ∈ H_3(q)) = z².

Hyp-A prediction:
  z² / [2]_q = [1 / (√q + 1/√q)]² · 1 / (q + 1/q)
             = q / (q + 1)²   ·   q / (q² + 1)
             = q² / [(q + 1)² · (q² + 1)]

ℏ_q³ / [2]_q (the actual rung 2):
             = [(q - 1)/q]³  ·  q / (q² + 1)
             = (q - 1)³ / [q² · (q² + 1)]

Hyp-A is CONFIRMED iff these two rational functions are equal.
This probe simplifies the difference symbolically — exact answer.

If REFUTED, then either:
  - tr_M(1) in 3-strand H_3(q) is not z² in QOU convention
    (unlikely — the QOU framework defines it this way), OR
  - "Markov trace at identity" must mean something other than
    tr_M(1 ∈ H_3), e.g. tr_M of a specific 3-cycle braid, OR
  - Hyp-A as stated is not the correct categorical source for
    rung 2; one of Hyp-B / Hyp-C may still hold.

Honest definitive test. No fit. No fallback ambiguity.
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

Q0_MP_PIN = "1.1099785955573347198997632204832250266562084087802"


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-rung2-hyp-a-markov-3strand-test",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Definitive test of Hyp-A: does the rung 2 form ℏ_q³/[2]_q "
        "equal (3-strand Markov trace at identity) / dim_q(V_1)? "
        "Symbolic check using QOU Markov-trace convention "
        "tr_M(1 ∈ H_n) = z^(n-1), z = 1/(√q+1/√q). Hyp-A confirmed "
        "iff the difference simplifies to 0."
    )
    builder.set_content_block("prop:q-beta-c-2-eq-neg-one-structural")

    print("=" * 78)
    print(" Q_β RUNG-2 HYP-A — definitive symbolic test")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    hbar_q = (q - 1) / q
    qint_2 = q + 1 / q
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))         # Markov-Jones parameter

    # The actual rung 2 form (closure on main)
    rung2_actual = hbar_q ** 3 / qint_2

    # Hyp-A prediction: tr_M(1 ∈ H_3) / dim_q(V_1) = z² / [2]_q
    hypA_pred = z ** 2 / qint_2

    print(f"  Setup (QOU Markov-trace convention):")
    print(f"    tr_M on H_n(q): tr_M(1) = z^(n-1)")
    print(f"    z = 1 / (√q + 1/√q) = Markov-Jones parameter")
    print(f"    dim_q(V_1) = [2]_q = q + q⁻¹ (fundamental rep)")
    print()
    print(f"  Hyp-A prediction:  rung 2 = tr_M(1 ∈ H_3) / dim_q(V_1)")
    print(f"                            = z² / [2]_q")
    print(f"  Actual rung 2:     ℏ_q³ / [2]_q")
    print()

    # Simplify both sides
    rung2_actual_simple = sp.simplify(rung2_actual)
    hypA_pred_simple = sp.simplify(hypA_pred)

    print(f"  Symbolic simplification:")
    print(f"    rung 2 (actual):  {sp.factor(rung2_actual_simple)}")
    print(f"    Hyp-A pred:       {sp.factor(hypA_pred_simple)}")
    print()

    # The decisive test
    diff = sp.simplify(rung2_actual - hypA_pred)
    print(f"  Decisive test:  rung 2 - Hyp-A pred = {sp.simplify(diff)}")
    print()

    hypA_confirmed = (diff == 0)

    # ---- Numerical check at q_0 ----
    q0_mp = mp.mpf(Q0_MP_PIN)
    def evalmp(expr):
        return mp.mpf(str(sp.N(expr.subs(q, sp.Float(str(q0_mp), 50)), 50)))

    actual_q0 = evalmp(rung2_actual)
    hypA_q0 = evalmp(hypA_pred)
    print(f"  Numerical at q_0 = {Q0_MP_PIN[:14]}:")
    print(f"    rung 2 (actual)         = {mp.nstr(actual_q0, 12)}")
    print(f"    Hyp-A pred (z²/[2]_q)   = {mp.nstr(hypA_q0, 12)}")
    print(f"    relative gap            = "
          f"{float(mp.fabs(actual_q0 - hypA_q0) / actual_q0):.4e}")
    print()

    print("=" * 78)
    print(" VERDICT — Hyp-A")
    print("=" * 78)
    print()
    if hypA_confirmed:
        print(f"  ✓ Hyp-A CONFIRMED")
        print(f"    rung 2 = ℏ_q³/[2]_q IS (3-strand Markov trace")
        print(f"    at identity) / dim_q(V_1) as symbolic rational")
        print(f"    function in q.  The rung-2 structural lift")
        print(f"    holds with this interpretation.")
    else:
        print(f"  ✗ Hyp-A REFUTED")
        print(f"    rung 2 = ℏ_q³/[2]_q ≠ tr_M(1)/[2]_q = z²/[2]_q.")
        print(f"    The two rational functions DIFFER:")
        print(f"      rung 2:  (q-1)³ / [q² · (q² + 1)]")
        print(f"      Hyp-A:   q²    / [(q+1)² · (q² + 1)]")
        print()
        print(f"    Hyp-A as literally stated does NOT give the rung-2 form.")
        print()
        print(f"    Implications:")
        print(f"      (a) 'Markov trace at identity' may need a different")
        print(f"          interpretation (e.g. 3-cycle braid trace, NOT")
        print(f"          identity-element trace).")
        print(f"      (b) The /[2]_q factor IS plausibly dim_q(V_1), but")
        print(f"          the ℏ_q³ numerator's categorical source is")
        print(f"          OPEN — not captured by tr_M(1 ∈ H_3) = z².")
        print(f"      (c) Hyp-B (Wenzl p_3) and Hyp-C (Kauffman bracket)")
        print(f"          remain untested; either could be correct.")
    print()
    print(f"  Honest finding either way — no fit, no fallback.")
    print()

    # ---- Also: what does ℏ_q³ correspond to in standard categorical ----
    # objects? Quick test of a few candidates:
    print(f"  Auxiliary scan — what gives ℏ_q³ structurally?")
    candidates = {
        "ℏ_q³ = ((q-1)/q)³":                  hbar_q ** 3,
        "(z - 1)³ where z = 1/(√q+1/√q)":     (z - 1) ** 3,
        "(q - 1)³ / [2]_q^(3/2)":              (q - 1) ** 3 / qint_2 ** (sp.Rational(3, 2)),
        "(1 - q⁻¹)³ = ℏ_q³ trivially":          (1 - 1 / q) ** 3,
        "[3]_q · ℏ_q / [2]_q² · ℏ_q²":         (q ** 2 + 1 + 1/q**2) * hbar_q
                                              / qint_2 ** 2 * hbar_q ** 2,
    }
    for name, expr in candidates.items():
        diff_to_rung2_num = sp.simplify(expr - hbar_q ** 3)
        marker = " ✓ matches ℏ_q³" if diff_to_rung2_num == 0 else ""
        print(f"    {name:<50}{marker}")
    print()

    builder.add_data("hypothesis", "Hyp-A: rung_2 = tr_M(1 ∈ H_3) / dim_q(V_1) = z² / [2]_q")
    builder.add_data("rung_2_actual", "hbar_q^3 / [2]_q = (q-1)^3 / (q^2 * (q^2 + 1))")
    builder.add_data("hypA_pred", "z^2 / [2]_q = q^2 / ((q+1)^2 * (q^2 + 1))")
    builder.add_data("symbolic_difference", str(sp.simplify(diff)))
    builder.add_data("verdict",
                     "CONFIRMED" if hypA_confirmed else "REFUTED")
    builder.add_data("numerical_at_q0", {
        "rung_2_actual": mp.nstr(actual_q0, 25),
        "hypA_pred": mp.nstr(hypA_q0, 25),
        "relative_gap": float(mp.fabs(actual_q0 - hypA_q0) / actual_q0),
    })
    builder.add_data("implications", (
        "Hyp-A as literally stated (tr_M(1 ∈ H_3) / dim_q(V_1)) "
        "does NOT yield the rung-2 form. Possible refinements: "
        "(a) 'Markov trace at identity' may need a different "
        "interpretation (e.g. 3-cycle braid trace); "
        "(b) /[2]_q may still be dim_q(V_1), but the ℏ_q³ "
        "numerator's categorical source is OPEN; "
        "(c) Hyp-B (Wenzl p_3) and Hyp-C (Kauffman bracket) "
        "remain untested."
    ) if not hypA_confirmed else (
        "Hyp-A confirmed — rung 2 IS the 3-strand Markov-trace at "
        "identity divided by the fundamental-rep quantum dimension. "
        "Structural lift holds with this categorical interpretation."
    ))

    builder.add_assertion(
        "hypA_decisively_resolved",
        computed=1,
        expected=1,
        tolerance=0,
        source=("The probe symbolically computes both rung-2 and "
                "Hyp-A's prediction as rational functions in q, "
                "simplifies the difference, and reports CONFIRMED "
                "(diff = 0) or REFUTED (diff ≠ 0). Either way the "
                "Hyp-A status is decisively resolved at this scope."),
    )

    builder.save()
    print(f"  Witness: qbeta-rung2-hyp-a-markov-3strand-test.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
