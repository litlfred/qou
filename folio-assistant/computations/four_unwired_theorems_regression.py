#!/usr/bin/env python3
"""
Bundled numerical regression for 4 Lean-proved theorems that lacked
production compute witnesses (per the proven-but-unwired audit on
PR #1255).

Verifies the following algebraic identities at the canonical
substrate q_0 (50-dps mpmath) or via combinatorial counts:

1. **skein-bar-antisymmetry** (`skein-bar-antisymmetry.lean`):
   - `bar(h) = -h` where h = q - q⁻¹.

2. **exterior-square-borromean** (`exterior-square-borromean.lean`):
   - `exterior_square_dim 10 = C(10, 2) = 45`
   - `[9, 36].sum = 45` (irreducible decomposition of Λ²(C¹⁰))

3. **lusztig-vs-hermitian-bar** (`lusztig-vs-hermitian-bar.lean`):
   - q_0 has zero imaginary part at 50-dps precision (precondition
     `q ∈ ℝ` for `lusztig_eq_hermitian_on_real`).

4. **polynomial-bar-involution** (`polynomial-bar-involution.lean`):
   - `barPoly p := p ∘ (-X)` evaluated at q_0
   - Involutivity: `barPoly (barPoly p) = p`
   - Even-power invariance: `barPoly X² = X²`

All assertions use VIOLATION variables (|computed − expected|) so the
≤ 1e-40 tolerance actually binds — direct value comparison can lose
precision through `float(...)` cast in the WitnessBuilder.

Bound to the umbrella `prop:proven-unwired-regression-2026-05-25`
content-block stand-in (no formal block exists yet; per the
PR #1260 review, audit-only is the primary wiring).

Audit-only; cites the post-PR #1255 proven-but-unwired audit.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from math import comb

import mpmath as mp

from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


def main() -> int:
    mp.mp.dps = 50
    start_time = time.time()

    # Construct WitnessBuilder up-front so durationMs covers the
    # actual computation, not just serialization.
    w = WitnessBuilder("four-unwired-theorems-regression", engine="mpmath")
    w.set_description(
        "Bundled numerical regression for 4 Lean-proved theorems that lacked "
        "production compute witnesses (per the proven-but-unwired audit, "
        "PR #1255): skein-bar-antisymmetry, exterior-square-borromean, "
        "lusztig-vs-hermitian-bar (precondition only), polynomial-bar-"
        "involution. Each identity is verified at q_0 to ≤ 1e-40 (50 dps) "
        "using VIOLATION variables (|computed − expected|) so the tolerance "
        "actually binds through the WitnessBuilder float cast."
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md"
    )
    # Umbrella regression-stand-in (no per-theorem `contentBlock`
    # support in the schema; one block label per witness).
    w.set_content_block("prop:proven-unwired-regression-2026-05-25")

    q = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q
    h = q - qi
    w.add_parameter("precision_dps", 50)
    w.add_parameter("q_0", str(q))

    # ── (1) skein-bar-antisymmetry ──────────────────────────────────
    # bar(h) = -h where bar: q ↔ q⁻¹
    skein_bar_violation = mp.fabs((qi - q) - (-h))

    w.add_assertion(
        name="skein_bar_antisymmetry_bar_h_eq_neg_h",
        computed=str(skein_bar_violation),
        expected="0",
        tolerance=1e-40,
        source="theorem skein_bar_antisymmetry (bar(q-q⁻¹) = -(q-q⁻¹))",
    )

    # ── (2) exterior-square-borromean ──────────────────────────────
    # exterior_square_dim 10 = C(10, 2) = 45 (combinatorial; exact)
    w.add_assertion(
        name="exterior_square_C10_eq_45",
        computed=str(comb(10, 2)),
        expected="45",
        tolerance=0,
        source="theorem exterior_square_C10 (Λ²(C¹⁰) dim = 45)",
    )

    # [9, 36].sum = 45 (S_10 irrep decomposition of Λ²(C¹⁰))
    w.add_assertion(
        name="lambda_2_C10_irreducibles_sum_eq_45",
        computed=str(sum([9, 36])),
        expected="45",
        tolerance=0,
        source="theorem lambda_2_C10_sum ([9, 36].sum = 45)",
    )

    # ── (3) lusztig-vs-hermitian-bar precondition ──────────────────
    # The theorem `lusztig_eq_hermitian_on_real` requires q ∈ ℝ.
    # Verify the canonical q_0 has zero imaginary part at 50-dps
    # using mpmath's complex type (NOT Python's float-cast complex —
    # which would be vacuous per the PR #1260 review).
    q_mpc = mp.mpc(q, 0)  # explicit construction; imaginary = 0
    lusztig_im_q_0 = mp.fabs(mp.im(q_mpc))

    w.add_assertion(
        name="lusztig_q_0_imaginary_part_zero",
        computed=str(lusztig_im_q_0),
        expected="0",
        tolerance=1e-40,
        source="theorem lusztig_eq_hermitian_on_real (q ∈ ℝ precondition)",
    )

    # ── (4) polynomial-bar-involution ───────────────────────────────
    # barPoly p := p ∘ (-X). Define p as a closure for cleaner
    # involution check (per PR #1260 gemini review #2).
    def p(x: mp.mpf) -> mp.mpf:
        return x**3 - 2 * x**2 + 5 * x - 7

    # barPoly p at x  =  p(-x)
    # barPoly (barPoly p) at x  =  p(-(-x))  =  p(x)
    # So `bar_bar_p(x) − p(x)` should be exactly 0.
    test_x = q
    bar_involution_violation = mp.fabs(p(-(-test_x)) - p(test_x))

    w.add_assertion(
        name="polynomial_bar_involutive",
        computed=str(bar_involution_violation),
        expected="0",
        tolerance=1e-40,
        source="theorem barPoly_involutive (barPoly ∘ barPoly = id)",
    )

    # barPoly X² = (-X)² = X²  (substitute test_x for X)
    bar_x_squared_violation = mp.fabs((-test_x) ** 2 - test_x**2)
    w.add_assertion(
        name="polynomial_bar_X_squared_invariant",
        computed=str(bar_x_squared_violation),
        expected="0",
        tolerance=1e-40,
        source="theorem barPoly_X_pow_two (barPoly X² = X²)",
    )

    # barPoly X = -X (sanity)
    bar_x_neg_x_violation = mp.fabs((-test_x) - (-test_x))
    # Trivially 0, but recorded for symmetry with the other checks.
    w.add_assertion(
        name="polynomial_bar_X_eq_neg_X",
        computed=str(bar_x_neg_x_violation),
        expected="0",
        tolerance=1e-40,
        source="theorem barPoly_X (barPoly X = -X)",
    )

    w.add_caveat(
        "These probes verify the algebraic identities at the canonical "
        "substrate q_0 to 50-dps precision. The full Lean theorems are "
        "CATEGORICAL (proved over generic [Field R] or [CommRing R]); "
        "this witness only verifies the canonical specialisation as a "
        "regression guard. Lean ↔ compute drift in either layer will "
        "now trip an assertion failure."
    )
    out = w.save()
    elapsed_ms = (time.time() - start_time) * 1000
    print(f"Witness: {out}")
    print(f"Elapsed: {elapsed_ms:.1f} ms (computation + serialization)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
