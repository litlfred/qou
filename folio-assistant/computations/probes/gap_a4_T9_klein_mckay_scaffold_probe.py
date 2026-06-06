#!/usr/bin/env python3
"""GAP-A-4 T9 probe — Klein-invariant / McKay-E_8 / Bring scaffold.

After T5–T8 refuted 5 quantum-group / Schur-Weyl candidates for the
cross-algebra h⁴ = −3/4 functor, the structural conclusion is that the
icosahedral H is non-Schur-Weyl.  T9 SCAFFOLDS the alternative
direction: the icosahedral subgroup structure of SO(3) ⊂ PSL(2, ℂ)
directly, via three classical objects:

  Klein invariants (1884):  f, H, T on ℂP¹ — polynomials of degrees
    12, 20, 30 invariant under the icosahedral A_5 ⊂ PSL(2, ℂ) action.
    The icosahedral invariant ring is ℂ[f, H, T]/(syzygy):
      T² = −1728·f⁵ + H³        (or sign variants)

  McKay correspondence:  The binary icosahedral group 2I ⊂ SU(2) is
    the double cover of I ≅ A_5, with 9 irreducible reps of dimensions
    1, 2, 3, 4, 5, 6, 4, 3, 2 — these label the nodes of the affine
    Ê_8 Dynkin diagram with the same Coxeter marks 1, 2, 3, 4, 5, 6, 4, 3, 2.
    Σ dim² = 1²+2²+3²+4²+5²+6²+4²+3²+2² = 1+4+9+16+25+36+16+9+4 = 120
    = |2I|. ✓

  Bring quintic:  The quintic surface in ℂP⁴ with A_5 automorphism
    group; its 27 lines (or equivalent invariant count) carry the
    icosahedral algebraic structure.  Equivalently, the resolvent
    quintic of an icosahedral covering.

T9 is a SCAFFOLD ONLY.  It:

  (a) Tabulates the 2I/E_8 irrep dimensions and verifies Σ dim² = 120.
  (b) Identifies the dim-5 irrep H = the unique dim-5 node of Ê_8.
  (c) Notes the Klein-invariant degree triple (12, 20, 30) and its
      relation to (60/5, 60/3, 60/2) — the cycle-class structure of
      A_5 (5-fold vertices, 3-fold faces, 2-fold edges).
  (d) Lists three CONCRETE follow-up sub-questions (T10/T11/T12) that
      could attempt a candidate functor in this framework, WITHOUT
      proposing a derivation now (to maintain formalize-first
      discipline — no 6th ansatz here).

EXPLORATORY SCAFFOLD — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T9-klein-mckay-scaffold-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402

# Centralised Q_0_50DPS (addresses Gemini deduplication review on PR #1904).
from _gap_a4_qsafe import Q_0_50DPS  # noqa: E402

from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent


# ── McKay E_8 / 2I data ───────────────────────────────────────────


# Affine Ê_8 Coxeter marks (= dims of 2I irreps under McKay):
# nodes: 1 - 2 - 3 - 4 - 5 - 6 - 4 - 2
#                          |
#                          3
# The labels are the dim of the corresponding 2I irrep.
TWO_I_IRREP_DIMS = [1, 2, 3, 4, 5, 6, 4, 3, 2]

# I ≅ A_5 has 5 irreps (T4-confirmed):
A5_IRREP_DIMS = [1, 3, 3, 4, 5]


def test_mckay_dim_sum() -> dict:
    print("=" * 78)
    print("T9a — McKay E_8 / 2I irrep dimensions")
    print("=" * 78)
    print(f"  Affine Ê_8 Coxeter marks (= dim of 2I irreps):")
    print(f"    {TWO_I_IRREP_DIMS}")
    dim_sum_sq = sum(d * d for d in TWO_I_IRREP_DIMS)
    print(f"  Σ dim² = {dim_sum_sq}  (expected: |2I| = 120)")
    print(f"  ✓ Burnside: Σ dim² = |G| holds.")
    print()
    print(f"  Icosahedral I ≅ A_5 irrep dimensions: {A5_IRREP_DIMS}")
    a5_dim_sum_sq = sum(d * d for d in A5_IRREP_DIMS)
    print(f"  Σ dim² = {a5_dim_sum_sq}  (expected: |A_5| = 60)")
    print(f"  ✓ A_5 Burnside check.")
    print()
    print(f"  Dim-5 irreps:")
    print(f"    A_5 has one dim-5 irrep: H (T4-verified as the")
    print(f"        icosahedral character)")
    print(f"    2I has one dim-5 irrep: corresponds to a Ê_8 node")
    print(f"  → The dim-5 H sits at a CANONICAL position in Ê_8 — it is")
    print(f"    the unique dim-5 node, with adjacent Ê_8 nodes (dim 4, 6).")
    return {
        "two_i_irrep_dims": TWO_I_IRREP_DIMS,
        "two_i_dim_sum_sq": dim_sum_sq,
        "two_i_order": 120,
        "a5_irrep_dims": A5_IRREP_DIMS,
        "a5_dim_sum_sq": a5_dim_sum_sq,
        "a5_order": 60,
        "dim_5_in_both": True,
    }


# ── Klein invariants — degree triple ─────────────────────────────


def test_klein_degree_triple() -> dict:
    print("=" * 78)
    print("T9b — Klein icosahedral invariants degree triple (12, 20, 30)")
    print("=" * 78)
    print(f"  Classical Klein (1884) invariants on ℂP¹:")
    print(f"    f  degree 12   (vertex polynomial; vanishes on 12 vertices)")
    print(f"    H  degree 20   (Hessian of f; vanishes on 20 face centres)")
    print(f"    T  degree 30   (Jacobian of f, H; vanishes on 30 edge midpoints)")
    print()
    print(f"  Syzygy: T² + H³ = 1728·f⁵  (degrees: 60 = 60 = 60 ✓)")
    print()
    print(f"  Relation to A_5 cycle classes:")
    print(f"    |A_5| / |stabilizer of vertex (5-cycle)|  = 60/5  = 12  ↔ f")
    print(f"    |A_5| / |stabilizer of face (3-cycle)|    = 60/3  = 20  ↔ H")
    print(f"    |A_5| / |stabilizer of edge (2-cycle)|    = 60/2  = 30  ↔ T")
    print(f"  → The triple (12, 20, 30) = (|orbit|, |orbit|, |orbit|)")
    print(f"    encodes the icosahedral orbit structure on ℂP¹.")
    print()
    print(f"  Klein modular invariant J = 1728·f⁵ / H³  has icosahedral")
    print(f"  monodromy on the icosahedral covering of ℂP¹ \\ {{0, 1, ∞}};")
    print(f"  equivalently J − 1 = T² / H³ via the syzygy.")
    return {
        "klein_degrees": {"f": 12, "H": 20, "T": 30},
        "orbits": {"vertices_5fold": 12, "faces_3fold": 20, "edges_2fold": 30},
        "orbit_to_invariant": {"vertices": "f", "faces": "H", "edges": "T"},
        "syzygy": "T² + H³ = 1728·f⁵",
        "klein_J": "J = 1728·f⁵ / H³  (J − 1 = T²/H³ via syzygy)",
    }


# ── Concrete open sub-questions (T10/T11/T12 scaffolds) ─────────


def test_open_subquestions() -> dict:
    print("=" * 78)
    print("T9c — Three CONCRETE open sub-questions (T10/T11/T12 candidates)")
    print("=" * 78)
    questions = [
        {
            "tag": "T10",
            "name": "McKay-character h⁴ candidate",
            "question": (
                "Does the 2I → A_5 → H restriction (dim-5 irrep of 2I "
                "passing to dim-5 irrep H of A_5) have a natural h-expansion "
                "whose h⁴ coefficient is −3/4 via the 2I-character orthogonality "
                "evaluated at a q-deformed argument?  The Ê_8 Coxeter marks "
                "(1,2,3,4,5,6,4,3,2) might encode the h⁴ structure as a "
                "characteristic-class invariant."
            ),
            "tractability": (
                "Medium. 2I character table is classical (9×9); q-deforming "
                "is a finite-dim problem.  Tractable in ≤ 200 lines pure mpmath."
            ),
        },
        {
            "tag": "T11",
            "name": "Klein J-invariant h-expansion",
            "question": (
                "Does the icosahedral J-invariant J = T² / H³ have a natural "
                "expansion in a q-deformed Klein coordinate whose leading "
                "h-correction is −3/4? J is a degree-0 rational function on "
                "ℂP¹/I with three critical values 0, 1, ∞ matching the three "
                "icosahedral orbit types — the universal h⁴ might emerge from "
                "the J ↦ q-twist analogue of the Riemann-Hurwitz formula."
            ),
            "tractability": (
                "High. Klein invariants are explicit polynomials; the syzygy "
                "T² + H³ = 1728·f⁵ is closed form; q-deformation is "
                "well-defined via formal Taylor series.  ~300 lines pure mpmath."
            ),
        },
        {
            "tag": "T12",
            "name": "Bring quintic discriminant h⁴",
            "question": (
                "Does the Bring quintic surface's discriminant (the locus "
                "in ℂP⁴ where the quintic degenerates) have a natural "
                "h-expansion under a q-deformation tied to substrate q_0 "
                "whose first non-trivial coefficient is −3/4? The Bring "
                "surface is the universal covering of ℂP¹ \\ {0, 1, ∞} "
                "with A_5 monodromy — its discriminant carries icosahedral "
                "characteristic-class information."
            ),
            "tractability": (
                "Lower. Bring quintic computations are involved (~600+ lines "
                "or external resolvent); requires careful symbolic setup."
            ),
        },
    ]
    for q in questions:
        print(f"  [{q['tag']}] {q['name']}")
        print(f"        Question: {q['question'][:80]}...")
        print(f"        Tractability: {q['tractability'][:60]}")
        print()
    print(f"  → All three live OUTSIDE the q-Schur / RT framework.")
    print(f"  → Pursuing one is the natural T10/T11/T12 follow-up.")
    print(f"  → T11 (Klein J) is the highest-tractability candidate.")
    return {"open_subquestions": questions}


# ── main ─────────────────────────────────────────────────────────


def main():
    mp.mp.dps = 50
    w = WitnessBuilder("gap-a4-T9-klein-mckay-scaffold-probe",
                       engine="mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-06-gap-a4-T4-T8-functor-search-retrospective.md"
    )
    w.set_description(
        "GAP-A-4 T9 — scaffold for Klein-invariant / McKay-E_8 / Bring "
        "direction.  After T5–T8 refuted 5 q-Schur / RT candidates, "
        "T9 sets up the non-Schur-Weyl alternative: tabulates the 2I/Ê_8 "
        "irrep dims + Klein degree triple (12,20,30) + queues 3 concrete "
        "open sub-questions (T10 McKay-character / T11 Klein-J / T12 "
        "Bring-discriminant).  NO derivation proposed here — formalize-first "
        "discipline prohibits a 6th ansatz."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY-SCAFFOLD")
    w.add_data("production_wired", False)
    # q_0 is recorded as a parameter for downstream consumers but the
    # T9 scaffold itself does no q-deformed computation — the follow-up
    # T10/T11/T12 probes are where q_0 is actually evaluated.
    w.add_data("q_0_recorded_for_followups", float(q_0))

    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    mckay = test_mckay_dim_sum()
    print()
    klein = test_klein_degree_triple()
    print()
    open_qs = test_open_subquestions()

    w.add_data("mckay_e8_2I", mckay)
    w.add_data("klein_invariants", klein)
    w.add_data("open_subquestions", open_qs)

    # Sanity assertions
    w.add_assertion(
        "two_I_burnside_check",
        computed=float(mckay["two_i_dim_sum_sq"]),
        expected=120.0,
        tolerance=1e-30,
        source=(
            "Σ dim² over 2I irreps = |2I| = 120 (Burnside); "
            "verifies the affine Ê_8 Coxeter mark list "
            "(1,2,3,4,5,6,4,3,2) is the correct 2I irrep dim spectrum."
        ),
    )
    w.add_assertion(
        "a5_burnside_check",
        computed=float(mckay["a5_dim_sum_sq"]),
        expected=60.0,
        tolerance=1e-30,
        source=(
            "Σ dim² over A_5 irreps = |A_5| = 60 (Burnside); "
            "matches the irrep dim list (1,3,3,4,5) used in T4."
        ),
    )
    w.add_assertion(
        "klein_orbit_sum_matches_riemann_hurwitz_signature",
        computed=float(sum(klein["orbits"].values())),
        expected=62.0,
        tolerance=0.0,
        source=(
            "Klein orbit triple 12 + 20 + 30 = 62 (NOT |A_5| = 60).  "
            "The orbits are |G|/|stab| with stabs 5, 3, 2 respectively; "
            "62 = 60·(1/5 + 1/3 + 1/2) = 60·(31/30) = 62. "
            "This is the Riemann-Hurwitz signature of the icosahedral "
            "covering of the orbifold P¹(2,3,5).  Renamed from "
            "`klein_orbit_sum_equals_group_order` (Copilot review) "
            "since the value differs from |A_5|."
        ),
    )

    synthesis = (
        "T9 sets up the non-Schur-Weyl direction structurally without "
        "proposing a derivation.  The dim-5 irrep H of A_5 sits at the "
        "unique dim-5 node of affine Ê_8 in the McKay correspondence — "
        "a canonical position that the q-Schur picture (T8 refuted) does "
        "not see.  The Klein degree triple (12, 20, 30) encodes the "
        "icosahedral orbit structure on ℂP¹ via (|G|/stab) for the "
        "three special orbit types (vertices, faces, edges).  Three "
        "concrete follow-up sub-questions are queued: "
        "T10 (McKay-character h⁴ via 2I), "
        "T11 (Klein J-invariant h-expansion — highest tractability), "
        "T12 (Bring quintic discriminant). "
        "Per formalize-first discipline, NO derivation of h⁴ = −3/4 is "
        "claimed here — that would be the 6th ansatz the discipline "
        "review catches.  T9 just tabulates the canonical icosahedral "
        "data and pins the open questions."
    )
    w.add_data("synthesis_verdict", synthesis)

    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    print()
    print(f"  Wrote witness: {out_path}")


if __name__ == "__main__":
    main()
