#!/usr/bin/env python3
"""
Regression guard for the symbolic H_3(q) Gram entries in
`content/quantum-observable-universe/lean/QOU/Interactions/GramMatrixH3Symbolic.lean`.

Transcribes the Lean `gramEntry*` definitions and compares them to the
production pyhecke Gram (`gram-matrix-dual.witness.json`) at the canonical q_0,
so that Lean ↔ compute drift is caught.

## The comparison this guard makes, and the one it used to make

Both sides carry a Markov weight `z`, and there are two:

  convention C   z = √q/(q+1)     excised 2026-08-09, re-affirmed 2026-08-15
  convention D   z = q³/(q²+1)    CANONICAL (owner ruling 2026-08-15)

Until 2026-08-23 this script transcribed the Lean **`gramEntry`** definitions,
which are convention C, and compared them to the reference witness — which was
regenerated under convention **D** on 2026-08-15. The headline assertion went
red at `0.17218519049094` against a `1e-14` tolerance and stayed red, reading
as though the Lean had drifted from the compute. It had not: both sides were
exact and internally consistent, and that number is precisely the C−D gap.

The guard now compares the **canonical** Lean entries `gramEntryD` against the
**canonical** reference, which is the drift check it was always meant to be.
The C-frame entries are still transcribed and still evaluated — the C−D gap is
reported as `data`, not as a failing assertion, so the number stays visible
without pretending to be a drift measurement.

Diagnosis, the determinant factorisation that makes D a root, and six
cross-checks: `computations/probes/gram_h3_convention_frame_probe.py`.

Bound to `prop:gram-matrix-h3-symbolic` content block via `set_content_block`.

Audit-only; cites the Phase 1b deliverable.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


def gram_entry_symbolic_C(u: mp.mpf, i: int, j: int) -> mp.mpf:
    """
    **Convention-C** Gram entry G[i,j] as a function of u = sqrt(q)
    (the spinor information rate \check{q}; "u" is kept as the
    Python identifier per Habiro-literature convention — see
    notation-collisions.md §\check{q}).

    Mirrors the `gramEntry` definition in `GramMatrixH3Symbolic.lean`
    exactly — any drift here ↔ Lean definitions is a regression.

    Convention C was excised 2026-08-09 / re-affirmed 2026-08-15. This stays
    to keep the C−D gap measurable; it is not the canonical frame.
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


def gram_entry_symbolic_D(q: mp.mpf, i: int, j: int) -> mp.mpf:
    """
    **Convention-D** (canonical) Gram entry G[i,j] as a function of q.

    Mirrors the `gramEntryD` definition in `GramMatrixH3Symbolic.lean`
    exactly — any drift here ↔ Lean definitions is a regression.

    Note there is no square root anywhere: `z_D = q³/(q²+1)` is rational in q,
    so every entry is a rational function with a power of `q² + 1` beneath it.
    That is why the D entries need no `u = √q` parametrisation and no `q ≠ 0`
    side condition, unlike the C entries above.
    """
    if i > j:
        i, j = j, i  # use upper-triangle (matrix is symmetric)
    one = mp.mpf(1)
    d1 = q**2 + 1
    d2 = d1**2
    if (i, j) == (0, 0):
        return one
    if (i, j) in [(0, 1), (0, 2)]:
        return q**3 / d1
    if (i, j) in [(0, 3), (0, 4), (1, 2)]:
        return q**6 / d2
    if (i, j) in [(0, 5), (1, 3), (1, 4), (2, 3), (2, 4)]:
        return (q**7 + q**3) / d2
    if (i, j) in [(1, 1), (2, 2)]:
        return (q**4 + 1) / d1
    if (i, j) in [(1, 5), (2, 5), (3, 3), (4, 4)]:
        return (q**8 + q**4 - q**2) / d2
    if (i, j) == (3, 4):
        return (q**8 + 2 * q**4 + 1) / d2
    if (i, j) in [(3, 5), (4, 5)]:
        return (q**9 + q**5 - q**3 + q) / d2
    if (i, j) == (5, 5):
        return (q**10 + q**6 + 2 * q**2) / d2
    raise ValueError(f"unexpected cell ({i},{j})")


def main() -> int:
    set_compute_dps()

    q = mp.mpf(Q_50_DIGIT_STR)
    u = mp.sqrt(q)

    # Canonical (D) and legacy (C) symbolic Grams from the Lean transcriptions
    G_D = [[gram_entry_symbolic_D(q, i, j) for j in range(6)] for i in range(6)]
    G_C = [[gram_entry_symbolic_C(u, i, j) for j in range(6)] for i in range(6)]

    # Load production pyhecke Gram from witness (convention D since 2026-08-15)
    witness_path = Path(__file__).resolve().parent / "gram-matrix-dual.witness.json"
    with open(witness_path) as f:
        pyhecke_witness = json.load(f)
    G_pyhecke = pyhecke_witness["gram_matrix"]

    def max_abs_diff(A, B):
        worst, cell = mp.mpf(0), None
        for i in range(6):
            for j in range(6):
                d = mp.fabs(A[i][j] - B[i][j])
                if d > worst:
                    worst, cell = d, (i, j)
        return worst, cell

    G_ref = [[mp.mpf(repr(G_pyhecke[i][j])) for j in range(6)] for i in range(6)]
    max_diff_D, cell_D = max_abs_diff(G_D, G_ref)
    max_diff_C, cell_C = max_abs_diff(G_C, G_ref)
    gap_CD, cell_CD = max_abs_diff(G_C, G_D)

    # Symmetry check on the canonical symbolic Gram
    max_asymm = mp.mpf(0)
    for i in range(6):
        for j in range(6):
            d = mp.fabs(G_D[i][j] - G_D[j][i])
            if d > max_asymm:
                max_asymm = d

    det_D = mp.det(mp.matrix(G_D))
    det_C = mp.det(mp.matrix(G_C))

    # The radical: G_D annihilates the three-strand q-antisymmetriser.
    radical = [-q**3, q**2, q**2, -q, -q, mp.mpf(1)]
    max_radical_residual = mp.mpf(0)
    for i in range(6):
        r = mp.fsum([G_D[i][j] * radical[j] for j in range(6)])
        if mp.fabs(r) > max_radical_residual:
            max_radical_residual = mp.fabs(r)

    w = WitnessBuilder("gram-h3-symbolic-regression", engine="mpmath")
    w.set_description(
        "Regression guard for the symbolic H_3(q) Hoefsmit Gram closed-form "
        "entries. Transcribes the Lean `gramEntryD` (convention D, canonical) "
        "definitions in `GramMatrixH3Symbolic.lean` and compares them against "
        "the production pyhecke Gram at q_0 to detect Lean <-> compute drift. "
        "Also transcribes the legacy `gramEntry` (convention C) definitions and "
        "reports the C-D gap as data. Until 2026-08-23 this guard compared C "
        "against the D reference and was red at 0.1721851904909 on that gap "
        "alone; see the module docstring."
    )
    w.set_audit_only("docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md")
    w.set_content_block("prop:gram-matrix-h3-symbolic")
    w.add_parameter("precision_dps", 50)
    w.add_parameter("q_0", str(q))
    w.add_parameter("u_0_sqrt_q_0", str(u))
    w.add_parameter("z_D_canonical", str(q**3 / (q**2 + 1)))
    w.add_parameter("z_C_excised", str(u / (q + 1)))
    w.add_data(
        "gram_symbolic_D_at_q_0",
        [[str(G_D[i][j]) for j in range(6)] for i in range(6)],
    )
    w.add_data(
        "gram_symbolic_C_at_q_0",
        [[str(G_C[i][j]) for j in range(6)] for i in range(6)],
    )
    w.add_data("det_D_at_q_0", str(det_D))
    w.add_data("det_C_at_q_0", str(det_C))
    w.add_data("convention_C_minus_D_max_abs", str(gap_CD))
    w.add_data("convention_C_minus_D_worst_cell", list(cell_CD))
    w.add_data("convention_C_vs_D_reference_max_abs", str(max_diff_C))
    w.add_data(
        "convention_gap_note",
        "convention_C_vs_D_reference_max_abs is NOT a drift measurement: it "
        "differences the excised-C Lean entries against the canonical-D "
        "reference, so it reports the convention gap. It is kept as data "
        "because it was this script's headline assertion until 2026-08-23.",
    )

    # Headline assertion: the CANONICAL symbolic entries match the CANONICAL
    # reference. Tolerance is the float64 floor of the strings the reference
    # stores, not a precision claim about either side.
    w.add_assertion(
        name="gram_h3_symbolic_matches_pyhecke",
        computed=str(max_diff_D),
        expected="0",
        tolerance="1e-14",  # string: keeps the value out of float64 (qou-t0rf)
        source="36-entry comparison, gramEntryD vs gram-matrix-dual.witness.json",
    )

    w.add_assertion(
        name="gram_h3_symbolic_is_symmetric",
        computed=str(max_asymm),
        expected="0",
        tolerance="1e-40",
        source="closed-form symmetry of the Lean gramEntryD definitions",
    )

    # Under D the determinant VANISHES — the canonical counterpart of the
    # C-frame `gramMatrix_det_ne_zero`. Tolerance is the numerical floor of a
    # 6x6 determinant of entries near 1 at this precision; the vanishing itself
    # is exact (`QOU...gramMatrixD_det_eq_zero`, sorry-free).
    w.add_assertion(
        name="gram_h3_symbolic_D_det_vanishes",
        computed=str(mp.fabs(det_D)),
        expected="0",
        tolerance="1e-40",
        source="numerical shadow of gramMatrixD_det_eq_zero (Lean, sorry-free)",
    )

    w.add_assertion(
        name="gram_h3_symbolic_D_radical_annihilated",
        computed=str(max_radical_residual),
        expected="0",
        tolerance="1e-40",
        source=("G_D applied to the three-strand q-antisymmetriser "
                "(-q^3, q^2, q^2, -q, -q, 1); shadow of "
                "gramMatrixD_mulVec_radical (Lean, sorry-free)"),
    )

    w.add_caveat(
        "The Lean definitions are CATEGORICAL (rational functions of q over "
        "generic q); this witness only verifies the q_0-specialisation. The "
        "determinant vanishing and the radical are proved for every real q in "
        "`gramMatrixD_det_eq_zero` / `gramMatrixD_mulVec_radical`, so the two "
        "assertions above are numerical shadows of Lean theorems rather than "
        "the evidence for them."
    )
    w.add_caveat(
        "`gram_h3_symbolic_matches_pyhecke` was red at 0.1721851904909 from "
        "2026-08-15 to 2026-08-23. It was not drift: it compared the "
        "convention-C Lean entries against a convention-D reference. The guard "
        "now compares D against D; the C-D gap is retained as data."
    )

    out = w.save()
    print(f"Witness: {out}")
    print(f"D (canonical) vs pyhecke, max abs diff : {mp.nstr(max_diff_D, 6)} at {cell_D}")
    print(f"C (excised)   vs pyhecke, max abs diff : {mp.nstr(max_diff_C, 6)} at {cell_C}")
    print(f"C - D convention gap                   : {mp.nstr(gap_CD, 6)} at {cell_CD}")
    print(f"Max symmetry violation (D)             : {mp.nstr(max_asymm, 6)}")
    print(f"det(G_D(q_0))                          : {mp.nstr(det_D, 6)}")
    print(f"det(G_C(q_0))                          : {mp.nstr(det_C, 6)}")
    print(f"Radical residual (D)                   : {mp.nstr(max_radical_residual, 6)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
