#!/usr/bin/env python3
"""qbeta_c3_rung2_bracket_comparison.py — symbolic comparison of the
3 distinct rung-2 candidates in the c_3 closure bracket.

PR #1786 follow-up to qbeta_c3_rung_structure_analysis.py. The c_3
closure on main (commit 305c08a91) lists 4 PASS candidates at
≤ 10 ppm for the rung-2 form, of which 2 are algebraically identical:

  T1.       ℏ_q³ / 2                  → 5.25 ppm
  T3 = T8.  ℏ_q³ · [2]_q / 4          → 7.87 ppm
  T7.       ℏ_q³ / [2]_q              → 2.65 ppm  ★ cleanest

(T3 and T8 are written differently — `ℏ_q³·[2]_q/4` vs
`ℏ_q³·(q+q⁻¹)/4` — but [2]_q = q+q⁻¹, so they are identical
expressions; this probe verifies that symbolically.)

The audit doc calls T7 'cleanest categorical' on the grounds that
it has no empirical numerical denominator (just a q-integer in the
denominator). This probe makes that structural argument precise:

  T1, T3 denominators: 2, 4 — empirical, no q-content
  T7 denominator:      [2]_q — quantum integer, full q-content

The substantive open question — *why is the denominator forced to
be a quantum dimension* — is the rung-2 structural-derivation
target. Candidate categorical sources (each unproven):

  Hyp-A. T7 = (3-strand Markov trace at identity) /
                 (quantum dimension of fundamental rep V_1).
         ℏ_q³ from 3-strand element, [2]_q from dim_q(V_1).

  Hyp-B. T7 = Wenzl 3-cell projector contribution to Q_β at
         order ℏ³, with normalization by the Temperley-Lieb
         loop value δ_q = [2]_q.

  Hyp-C. T7 = (Bracket polynomial value at order h³) /
                 (Kauffman bracket of unknot in standard norm).

This probe reports the precision of each candidate + flags the
unique structural property of T7. Does NOT prove the rung-2
structural lift. Honest scoping.
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
        "qbeta-c3-rung2-bracket-comparison",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Symbolic comparison of the 3 distinct rung-2 candidates "
        "in the c_3 closure bracket. Verifies T3 = T8 algebraically, "
        "compares T1/T3/T7 by structural cleanliness (T7 alone has "
        "a q-integer denominator), lists 3 candidate categorical "
        "sources for the structural lift. Does NOT prove lift."
    )
    builder.set_content_block("prop:q-beta-c-2-eq-neg-one-structural")

    print("=" * 78)
    print(" Q_β c_3 RUNG-2 BRACKET — T1 vs T3=T8 vs T7")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    hbar_q = (q - 1) / q
    qint_2 = q + 1 / q

    T1 = hbar_q ** 3 / 2
    T3 = hbar_q ** 3 * qint_2 / 4
    T7 = hbar_q ** 3 / qint_2
    T8 = hbar_q ** 3 * (q + 1 / q) / 4   # written differently

    # Verify T3 = T8 algebraically
    T3_minus_T8 = sp.simplify(T3 - T8)
    print(f"  Algebraic identity check:")
    print(f"    T3 = ℏ_q³ · [2]_q / 4")
    print(f"    T8 = ℏ_q³ · (q + q⁻¹) / 4")
    print(f"    T3 - T8 = {T3_minus_T8}   ← {'IDENTICAL ✓' if T3_minus_T8 == 0 else 'DIFFER'}")
    print(f"    (since [2]_q ≡ q + q⁻¹, T3 ≡ T8 as Laurent")
    print(f"     polynomials in q.  Bracket has 3 distinct candidates,")
    print(f"     not 4.)")
    print()

    print(f"  Structural-cleanliness ranking:")
    print(f"    {'Candidate':<10} {'Form':<30} {'Denominator':<18} "
          f"{'q-content?':<12}")
    print(f"    {'-'*10} {'-'*30} {'-'*18} {'-'*12}")
    print(f"    {'T1':<10} {'ℏ_q³ / 2':<30} {'2':<18} {'NO':<12}")
    print(f"    {'T3 = T8':<10} {'ℏ_q³ · [2]_q / 4':<30} "
          f"{'4':<18} {'NO':<12}")
    print(f"    {'T7':<10} {'ℏ_q³ / [2]_q':<30} {'[2]_q':<18} "
          f"{'YES ★':<12}")
    print()
    print(f"  → T7 is the only candidate whose denominator carries")
    print(f"    full q-content (a quantum integer). T1, T3 use plain")
    print(f"    integer denominators that don't deform with q. By the")
    print(f"    'minimize empirical content' criterion, T7 wins.")
    print()

    # ---- Numerical precision vs target -------------------------------
    q0_mp = mp.mpf(Q0_MP_PIN)
    def evalmp(expr):
        return mp.mpf(str(sp.N(expr.subs(q, sp.Float(str(q0_mp), 50)), 50)))

    T1_q0 = evalmp(T1)
    T3_q0 = evalmp(T3)
    T7_q0 = evalmp(T7)
    print(f"  Numerical at q_0:")
    print(f"    T1 = {mp.nstr(T1_q0, 12)}")
    print(f"    T3 = {mp.nstr(T3_q0, 12)}")
    print(f"    T7 = {mp.nstr(T7_q0, 12)}")
    print(f"  Each rung gives c_3 = -(q²+q⁻²)·(1 + ℏ_q·[3]_q/25 + T_k).")
    print(f"  Per audit doc 2026-06-03-l2-closure-habiro-3-q-25-...,")
    print(f"  ε_ppm vs cal-anchored c_3 target:")
    print(f"    T1: 5.25 ppm")
    print(f"    T3 = T8: 7.87 ppm")
    print(f"    T7: 2.65 ppm  ★ cleanest categorical AND best ε")
    print()

    print("=" * 78)
    print(" RUNG-2 STRUCTURAL-LIFT CANDIDATE HYPOTHESES")
    print("=" * 78)
    print()
    print(f"  Hyp-A.  T7 = (3-strand Markov-trace component at identity)")
    print(f"               / (quantum dimension dim_q V_1 = [2]_q)")
    print(f"          The ℏ_q³ would arise from the cube-of-substrate")
    print(f"          element in the 3-strand contribution; the [2]_q")
    print(f"          would be the Markov-trace normalization on one")
    print(f"          fundamental-rep strand.")
    print()
    print(f"  Hyp-B.  T7 = Wenzl projector p_3 contribution at order")
    print(f"               ℏ³ / Temperley-Lieb loop value δ_q = [2]_q.")
    print(f"          The 3-cell Wenzl projector p_3 carries an")
    print(f"          inherent /[2]_q normalization from the TL")
    print(f"          algebra structure.")
    print()
    print(f"  Hyp-C.  T7 = (Kauffman bracket order-h³ coefficient) /")
    print(f"               (unknot Kauffman bracket in standard norm)")
    print(f"          The unknot bracket = [2]_q in standard")
    print(f"          normalization, so the ratio carries 1/[2]_q.")
    print()
    print(f"  All three hypotheses predict the same FORM (ℏ_q³/[2]_q)")
    print(f"  with different categorical justification. Discriminating")
    print(f"  between them — or finding a single unifying structural")
    print(f"  argument — is the rung-2 structural-lift open question.")
    print()
    print(f"  Until any of A, B, C is proven, c_3 = NEAR-MATCH (2.65 ppm).")
    print()

    builder.add_data("bracket_candidates", {
        "T1": "hbar_q^3 / 2",
        "T3_equals_T8": "hbar_q^3 * [2]_q / 4  (T3 and T8 algebraically identical)",
        "T7": "hbar_q^3 / [2]_q  ★ cleanest categorical",
    })
    builder.add_data("T3_minus_T8_symbolic_difference", str(T3_minus_T8))
    builder.add_data("structural_cleanliness_ranking", {
        "T1_denominator": "2 (empirical, no q-content)",
        "T3_T8_denominator": "4 (empirical, no q-content)",
        "T7_denominator": "[2]_q (quantum integer, full q-content) ★",
        "principle": "minimize empirical content",
        "winner": "T7",
    })
    builder.add_data("numerical_at_q0", {
        "T1": mp.nstr(T1_q0, 25),
        "T3": mp.nstr(T3_q0, 25),
        "T7": mp.nstr(T7_q0, 25),
    })
    builder.add_data("eps_ppm_per_audit_doc", {
        "T1": "5.25 ppm",
        "T3_equals_T8": "7.87 ppm",
        "T7": "2.65 ppm",
    })
    builder.add_data("structural_lift_hypotheses", [
        ("Hyp-A: T7 = (3-strand Markov-trace at identity) / dim_q(V_1) "
         "= (3-strand component) / [2]_q"),
        ("Hyp-B: T7 = Wenzl projector p_3 contribution at order h^3 / "
         "Temperley-Lieb loop value [2]_q"),
        ("Hyp-C: T7 = (Kauffman bracket order-h^3 coefficient) / "
         "(unknot Kauffman bracket in [2]_q normalization)"),
    ])
    builder.add_data("status", "All 3 hypotheses unproven; c_3 remains NEAR-MATCH (2.65 ppm)")

    # Sanity assertion: T3 and T8 are algebraically identical
    builder.add_assertion(
        "T3_equals_T8_symbolically",
        computed=int(T3_minus_T8 == 0),
        expected=1,
        tolerance=0,
        source=("T3 = ℏ_q³ · [2]_q / 4 and T8 = ℏ_q³ · (q+q⁻¹) / 4 "
                "are identical Laurent polynomials in q because "
                "[2]_q ≡ q + q⁻¹.  Sympy.simplify of the difference "
                "equals 0.  Confirms the audit doc's 4-candidate "
                "bracket is structurally a 3-candidate bracket."),
    )

    builder.save()
    print(f"  Witness: qbeta-c3-rung2-bracket-comparison.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
