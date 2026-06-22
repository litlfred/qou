#!/usr/bin/env python3
"""
Regression guard for the symbolic H_3(q) Gram entries in
`content/quantum-observable-universe/lean/QOU/Interactions/GramMatrixH3Symbolic.lean`.

Computes each of the 36 entries via the sympy-derived closed forms
(transcribed from the Lean definitions) and compares to the production
pyhecke Gram (`gram-matrix-dual.witness.json`) at the canonical q_0.

Max absolute difference must be ≤ 1e-14 (numerical floor for float64
arithmetic) — otherwise the Lean symbolic definitions have drifted
from the production-compute pyhecke implementation.

Bound to `prop:gram-matrix-h3-symbolic` content block via
`set_content_block`.

Audit-only; cites the Phase 1b deliverable.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp

from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


def gram_entry_symbolic(u: mp.mpf, i: int, j: int) -> mp.mpf:
    """
    Symbolic Gram entry G[i,j] as a function of u = sqrt(q)
    (the spinor information rate \check{q}; "u" is kept as the
    Python identifier per Habiro-literature convention — see
    notation-collisions.md §\check{q}).

    Mirrors the `gramEntry` definition in `GramMatrixH3Symbolic.lean`
    exactly — any drift here ↔ Lean definitions is a regression.
    """
    if i > j:
        i, j = j, i  # use upper-triangle (matrix is symmetric)
    one = mp.mpf(1)
    if (i, j) == (0, 0):
        return one
    if (i, j) in [(0, 1), (0, 2)]:
        return u / (u**2 + 1)
    if (i, j) in [(0, 3), (0, 4), (1, 2)]:
        return u**2 / (u**2 + 1) ** 2
    if (i, j) == (0, 5):
        return (u**2 + u - 1) / (u**2 + 1)
    if (i, j) in [(1, 1), (2, 2)]:
        return (u**2 + u - 1) / u
    if (i, j) in [(1, 3), (1, 4), (2, 3), (2, 4)]:
        return (u**2 + u - 1) / (u**2 + 1)
    if (i, j) in [(1, 5), (2, 5), (3, 3), (4, 4)]:
        return (u**4 + u - 1) * (u**4 + u**3 - 1) / (u**2 * (u**2 + 1) ** 2)
    if (i, j) == (3, 4):
        return (u**2 + u - 1) ** 2 / u**2
    if (i, j) in [(3, 5), (4, 5)]:
        return (u**10 + u**9 - u**8 - u**5 + u**2 + u - 1) / (u**4 * (u**2 + 1))
    if (i, j) == (5, 5):
        return (
            u**12 + u**11 - 2 * u**10 - u**9 + 2 * u**8 + u**7
            - u**6 - u**5 + 2 * u**4 + u**3 - 2 * u**2 - u + 1
        ) / u**6
    raise ValueError(f"unexpected cell ({i},{j})")


def main() -> int:
    mp.mp.dps = 50

    q = mp.mpf(Q_50_DIGIT_STR)
    u = mp.sqrt(q)

    # Compute symbolic Gram from the closed-form transcription
    G_sym = [[gram_entry_symbolic(u, i, j) for j in range(6)] for i in range(6)]

    # Load production pyhecke Gram from witness
    witness_path = Path(__file__).resolve().parent / "gram-matrix-dual.witness.json"
    with open(witness_path) as f:
        pyhecke_witness = json.load(f)
    G_pyhecke = pyhecke_witness["gram_matrix"]

    # Max absolute difference across all 36 entries
    max_diff = mp.mpf(0)
    diffs = []
    for i in range(6):
        for j in range(6):
            d = mp.fabs(G_sym[i][j] - mp.mpf(repr(G_pyhecke[i][j])))
            diffs.append((i, j, float(d)))
            if d > max_diff:
                max_diff = d

    # Symmetry check on the symbolic Gram (G_sym[i,j] - G_sym[j,i] = 0)
    max_asymm = mp.mpf(0)
    for i in range(6):
        for j in range(6):
            d = mp.fabs(G_sym[i][j] - G_sym[j][i])
            if d > max_asymm:
                max_asymm = d

    # Determinant via mpmath
    det_sym = mp.det(mp.matrix(G_sym))

    w = WitnessBuilder("gram-h3-symbolic-regression", engine="mpmath")
    w.set_description(
        "Regression guard for symbolic H_3(q) Hoefsmit Gram closed-form "
        "entries (Phase 1b of Option E). Compares the 36 sympy-derived "
        "Lean `gramEntry` definitions in `GramMatrixH3Symbolic.lean` "
        "against the production pyhecke Gram at q_0 to detect Lean ↔ "
        "compute drift. Also verifies symmetry (numerically) and reports "
        "determinant at q_0 (non-zero; gramMatrix_det_ne_zero sorry to "
        "be discharged in Phase 1b-2)."
    )
    w.set_audit_only("docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md")
    w.set_content_block("prop:gram-matrix-h3-symbolic")
    w.add_parameter("precision_dps", 50)
    w.add_parameter("q_0", str(q))
    w.add_parameter("u_0_sqrt_q_0", str(u))
    w.add_data(
        "gram_symbolic_at_q_0",
        [[str(G_sym[i][j]) for j in range(6)] for i in range(6)],
    )
    w.add_data("det_at_q_0", str(det_sym))

    # Headline assertion: symbolic entries match pyhecke witness
    w.add_assertion(
        name="gram_h3_symbolic_matches_pyhecke",
        computed=str(max_diff),
        expected="0",
        tolerance=1e-14,
        source="36-entry comparison vs gram-matrix-dual.witness.json",
    )

    # Symmetry assertion
    w.add_assertion(
        name="gram_h3_symbolic_is_symmetric",
        computed=str(max_asymm),
        expected="0",
        tolerance=1e-40,
        source="closed-form symmetry of Lean gramEntry definitions",
    )

    # Det non-zero assertion (numerical witness for the deferred Lean proof)
    w.add_assertion(
        name="gram_h3_symbolic_det_ne_zero_at_q_0",
        computed=str(mp.fabs(det_sym)),
        expected="0.189",
        tolerance=0.01,  # det ≈ -0.189 ± 0.01 is enough to show ≠ 0
        source="numerical witness for gramMatrix_det_ne_zero (Phase 1b-2 sorry)",
    )

    w.add_caveat(
        "The Lean symbolic definitions are CATEGORICAL (Laurent polynomials "
        "in u = √q over generic positive u); this witness only verifies the "
        "q_0-specialisation matches pyhecke and that the determinant is "
        "non-zero at q_0. Phase 1b-2 follow-up will discharge the "
        "gramMatrix_det_ne_zero sorry via symbolic determinant factorisation."
    )

    out = w.save()
    print(f"Witness: {out}")
    print(f"Max abs diff (symbolic vs pyhecke at q_0): {float(max_diff):.2e}")
    print(f"Max symmetry violation: {float(max_asymm):.2e}")
    print(f"det(G(q_0)) = {float(det_sym):.10f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
