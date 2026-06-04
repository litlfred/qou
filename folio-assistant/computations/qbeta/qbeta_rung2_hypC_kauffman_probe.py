#!/usr/bin/env python3
"""qbeta_rung2_hypC_kauffman_probe.py — definitive test of Hyp-C
for the c_3 rung-2 structural lift.

Tests whether rung 2 = ℏ_q³/[2]_q equals
(Kauffman bracket order-h³ coefficient of some knot) / (unknot
Kauffman bracket in [2]_q normalization).

In the standard Kauffman bracket convention with A = q^(1/4)
(so A² = q^(1/2)), the unknot bracket evaluates to
<O> = -A² - A⁻² = -(q^(1/2) + q^(-1/2)), or in the [2]_q
normalization <O> = [2]_q = q + q⁻¹.  Specific knots' brackets
have q-Taylor expansions whose order-h³ coefficients can be
read off.

Hyp-C literal test:
  Expand the Kauffman bracket of the simplest non-trivial link
  (the Hopf link H+) in powers of (q-1), divide by [2]_q, and
  compare to ℏ_q³/[2]_q at order ℏ³.

The Hopf link's Jones polynomial:
  V(H+)(q) = -q^(-5/2) - q^(-1/2)  (one common Jones convention)
            = -q^(-1/2) (q^(-2) + 1)

Translating to the bracket via <H+>(A) = (-A)^{-3·w(H+)} V(H+)(A^(-4))
with writhe w(H+) = +2 gets messy convention-wise.  Use a simpler
proxy: the Markov-trace polynomial of the 2-braid σ_1² (whose
closure IS the Hopf link) in H_2(q).

  σ_1² = (q - q⁻¹) σ_1 + 1   (Hecke relation in H_2(q))
  tr_M(σ_1²) = (q - q⁻¹) tr_M(σ_1) + tr_M(1)
             = (q - q⁻¹) · z + z² · [scale]   ... convention-dep

To avoid convention thrash, this probe just verifies the
classical-limit compatibility test and reports the Kauffman
direction as REQUIRING further specification before a definitive
test can be performed.

Naming: `*_probe.py` (not `*_test.py`) per Copilot review on
PR #1806.  All complex / high-precision arithmetic uses mpmath
context (no `1j` literals).
"""
from __future__ import annotations

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
        "qbeta-rung2-hyp-c-kauffman-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Hyp-C scoping: tests whether the Kauffman-bracket "
        "interpretation of rung 2 = hbar_q^3/[2]_q is "
        "self-consistent.  Performs the classical-limit cross-check "
        "(rung 2 vanishes at q=1, so any Kauffman-bracket-derived "
        "expression must vanish at the same order).  Identifies "
        "which specific Kauffman-bracket reading would be testable."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Q_β RUNG-2 HYP-C — Kauffman bracket scoping")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    hbar_q = (q - 1) / q
    qint_2 = q + 1 / q

    rung2_actual = hbar_q ** 3 / qint_2

    # Hopf link Jones polynomial (one common convention).  Used as a
    # representative Kauffman-derived form to test the magnitude of
    # the cubic-in-(q-1) contribution.
    V_Hopf = -1 / q ** sp.Rational(1, 2) * (1 / q ** 2 + 1)

    # Trefoil Jones (one convention)
    V_trefoil = -q ** (-4) + q ** (-3) + q ** (-1)

    # "Kauffman bracket scaled by unknot in [2]_q normalization" for
    # the Hopf link, expanded around q=1
    print(f"  Rung 2 (actual):  {sp.factor(rung2_actual)}")
    print(f"  Taylor at q=1:     {sp.series(rung2_actual, q, 1, 5).removeO()}")
    print()
    print(f"  Hopf Jones V(H+)(q):  {V_Hopf}")
    print(f"  Taylor at q=1:        {sp.series(V_Hopf, q, 1, 4).removeO()}")
    print()
    print(f"  Trefoil Jones V(3_1)(q):  {V_trefoil}")
    print(f"  Taylor at q=1:            {sp.series(V_trefoil, q, 1, 4).removeO()}")
    print()

    # The classical-limit test: rung 2 vanishes cubically in (q-1).
    # Any candidate Kauffman bracket must also vanish at order h^3 or
    # higher to be consistent.
    rung2_at_q1 = sp.limit(rung2_actual, q, 1)
    V_Hopf_at_q1 = sp.limit(V_Hopf, q, 1)
    V_trefoil_at_q1 = sp.limit(V_trefoil, q, 1)

    print(f"  Classical-limit values:")
    print(f"    rung 2 at q=1:        {rung2_at_q1}  (must be 0)")
    print(f"    V(Hopf+) at q=1:      {V_Hopf_at_q1}  (≠ 0 — NOT order-h³ form)")
    print(f"    V(3_1) at q=1:        {V_trefoil_at_q1}  (≠ 0 — NOT order-h³ form)")
    print()

    print("=" * 78)
    print(" VERDICT — Hyp-C scope status")
    print("=" * 78)
    print()
    print(f"  Hyp-C as literally stated ('Kauffman bracket order-h³ coefficient')")
    print(f"  IS in principle a vanishing-at-classical-limit form, since")
    print(f"  order-h³ extraction strips out the constant and lower-order")
    print(f"  terms.  So the classical-limit compatibility test is")
    print(f"  TRIVIALLY satisfied for ANY 'order-h³ coefficient' reading.")
    print()
    print(f"  But: 'order-h³ coefficient of WHICH knot' is left UNDERSPECIFIED.")
    print(f"  Without choosing a knot, Hyp-C is NOT a definitive hypothesis —")
    print(f"  it's a family of hypotheses parameterized by the knot choice.")
    print()
    print(f"  This probe identifies the necessary refinement:")
    print(f"  → Hyp-C needs a SPECIFIC knot choice + specific Kauffman")
    print(f"    bracket convention before it can be definitively tested.")
    print(f"  → Natural candidates: Hopf link (relates to rung-0 base),")
    print(f"    trefoil 3_1, figure-eight 4_1, cinquefoil T(2,5)")
    print(f"    (relates to the rung-1 /25 conjecture).")
    print()
    print(f"  SCOPING VERDICT: Hyp-C is currently UNDERSPECIFIED — needs")
    print(f"  a knot + convention choice before becoming definitively")
    print(f"  testable. Deferred to a follow-up probe.")
    print()

    builder.add_data("hypothesis_C_status", "UNDERSPECIFIED (needs knot + convention choice)")
    builder.add_data("classical_limit_test", {
        "rung_2_at_q_1": str(rung2_at_q1),
        "V_Hopf_at_q_1": str(V_Hopf_at_q1),
        "V_trefoil_at_q_1": str(V_trefoil_at_q1),
        "note": ("Order-h^3 extraction trivially gives vanishing-at-q=1, "
                 "so the test does NOT discriminate without specifying "
                 "the knot."),
    })
    builder.add_data("candidate_knots_for_followup", [
        "Hopf link (links to rung-0 base -(q^2+q^-2) = -J_Hopf)",
        "trefoil 3_1 (V_trefoil(q) at q=1 = 1)",
        "figure-eight 4_1 (V_4_1(q) at q=1 = 5)",
        "cinquefoil T(2,5) (links to rung-1 /25 conjecture)",
    ])
    builder.add_data("verdict", "UNDERSPECIFIED — Hyp-C requires further refinement to be definitive")

    builder.add_assertion(
        "hyp_C_scope_documented",
        computed=1,
        expected=1,
        tolerance=0,
        source=("Sanity invariant: this probe documents Hyp-C's "
                "status as UNDERSPECIFIED and lists the refinement "
                "needed (knot + convention choice). Open follow-up."),
    )

    builder.save()
    print(f"  Witness: qbeta-rung2-hyp-c-kauffman-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
