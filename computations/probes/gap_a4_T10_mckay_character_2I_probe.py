#!/usr/bin/env python3
"""GAP-A-4 T10 probe — McKay-character candidate via 2I (binary icosahedral).

After T9 scaffolded the McKay-E_8 direction, T10 tests the most direct
candidate: the 5-dim irrep of the binary icosahedral group 2I lifts the
5-dim icosahedral H irrep of A_5 ≅ I = 2I / ℤ_2 (the spin double cover).

If a "spin-lift" candidate functor existed mapping the 5-strand A_5
fiber action to the 3-strand H_3 Borromean h⁴ = −3/4 coefficient, the
natural place would be: take χ_5^{2I} (the dim-5 character of 2I) at a
canonically-lifted β_Bor and check whether this picks up h⁴ structure
distinct from T7's uniform 5/4 result.

KEY OBSERVATION (proves the candidate is REFUTED):

The center of 2I is Z = {±1} ⊂ 2I, with 2I/Z = I ≅ A_5.  For any group
element g ∈ 2I, χ_R^{2I}(g) = χ_R^{2I}(−g) when R is integer-spin
(factor +1 on center) and χ_R^{2I}(g) = −χ_R^{2I}(−g) when R is
half-integer-spin (factor −1 on center).

The 5-dim irrep H of 2I is INTEGER-SPIN (it factors through I), so:

  χ_5^{2I}(g) = χ_5^I(π(g))   for all g ∈ 2I,  π: 2I → I

i.e. the 2I-character on the dim-5 irrep is EXACTLY the I-character on H
composed with the projection.  This means **the spin lift adds no new
information at the dim-5 level** — the spin-cover ℤ_2 is in the kernel
of the dim-5 character map.

For β_Bor whose image in I (via the natural projection B_3 → S_3 → I
through any embedding) is the identity, χ_5^{2I}(β_Bor_lifted) =
χ_5^I(id) = 5.  This is independent of the q-deformation at the
character-evaluation level (the h⁴ structure comes from the q-twist of
the BRAIDING, not the character itself).

So the McKay-character / spin-lift candidate is REFUTED: the dim-5
2I-character on β_Bor reduces to the dim-5 A_5-character (via the
projection), which is already T4's structural input.  No new functor
appears.

This complements T8 (RT/q-Schur REFUTED): the icosahedral H is not
reachable via either quantum-group representation theory (T8) OR the
double-cover spin lift (T10).  The non-Schur-Weyl direction must
involve genuinely non-character-theoretic structure (Klein invariants
→ T11, or Bring discriminant → T12).

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T10-mckay-character-2I-probe.witness.json`.
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


# ── 2I irrep dims = Ê_8 Coxeter marks ─────────────────────────────


TWO_I_IRREP_DIMS = [1, 2, 3, 4, 5, 6, 4, 3, 2]

# Parity-on-center classification: which 2I irreps are integer-spin
# (factor through I ≅ A_5) vs half-integer-spin (faithful, see −1).
# By the McKay / affine Ê_8 structure:
#   integer-spin nodes (the I irreps lifted):  dim 1, 3, 3, 4, 5
#   half-integer-spin (genuinely 2I):           dim 2, 4, 6, 2
# These match A_5's 5 irreps (1, 3, 3, 4, 5) on the integer side,
# plus 4 "spinor" irreps on the half-integer side.
TWO_I_INTEGER_SPIN_DIMS = [1, 3, 3, 4, 5]  # = A_5 irrep dims
TWO_I_HALF_SPIN_DIMS = [2, 4, 6, 2]


# ── Test: spin-lift triviality on dim-5 H ─────────────────────────


def test_spin_lift_kernel() -> dict:
    print("=" * 78)
    print("T10 — McKay-character / spin-lift candidate (2I → I)")
    print("=" * 78)
    print(f"  Binary icosahedral group 2I:")
    print(f"    Order: 120 = 2 · |A_5|")
    print(f"    Irrep dims: {TWO_I_IRREP_DIMS}")
    print(f"    Integer-spin (factor through I): {TWO_I_INTEGER_SPIN_DIMS}")
    print(f"    Half-integer-spin (genuinely 2I): {TWO_I_HALF_SPIN_DIMS}")
    print()
    print(f"  Burnside check:")
    int_sum_sq = sum(d * d for d in TWO_I_INTEGER_SPIN_DIMS)
    half_sum_sq = sum(d * d for d in TWO_I_HALF_SPIN_DIMS)
    print(f"    Σ dim²(integer) = {int_sum_sq}  (should equal |A_5| = 60)")
    print(f"    Σ dim²(half)    = {half_sum_sq}  (should equal "
          f"|2I| − |A_5| = 60)")
    print(f"    Total           = {int_sum_sq + half_sum_sq}  "
          f"(should equal |2I| = 120)")
    print()
    print(f"  KEY OBSERVATION:")
    print(f"    The dim-5 irrep H sits on the INTEGER-SPIN side (dims")
    print(f"    1, 3, 3, 4, 5 — exactly the A_5 irreps).")
    print(f"    ⟹ χ_5^{{2I}}(g) = χ_5^{{A_5}}(π(g)) for all g ∈ 2I,")
    print(f"      where π : 2I → A_5 is the canonical projection.")
    print()
    print(f"  CONSEQUENCE:")
    print(f"    For β_Bor with π(β_Bor) = id ∈ A_5 (writhe 0, image is")
    print(f"    identity in S_3 hence in A_5 via any natural embedding):")
    print(f"      χ_5^{{2I}}(β_Bor_lifted) = χ_5^{{A_5}}(id) = 5  exactly.")
    print(f"    ⟹ The spin-lift adds NO new information at dim-5;")
    print(f"      the spin ℤ_2 is in the KERNEL of χ_5^{{2I}}.")
    print(f"    ⟹ McKay-character / spin-lift candidate REFUTED.")
    return {
        "int_spin_dims": TWO_I_INTEGER_SPIN_DIMS,
        "half_spin_dims": TWO_I_HALF_SPIN_DIMS,
        "int_burnside_sum_sq": int_sum_sq,
        "half_burnside_sum_sq": half_sum_sq,
        "total_burnside_sum_sq": int_sum_sq + half_sum_sq,
        "dim_5_is_integer_spin": True,
        "chi_5_on_betaBor_lifted": 5,
        "verdict": (
            "Spin-lift adds no new structure at dim-5 (the dim-5 irrep is "
            "integer-spin, projects from 2I to A_5 trivially on the center). "
            "χ_5^{2I}(β_Bor_lifted) = 5 exactly, identical to χ_5^{A_5}(id). "
            "McKay-character candidate REFUTED — the h⁴ obstruction is not "
            "resolved by spin-lifting."
        ),
    }


# ── main ─────────────────────────────────────────────────────────


def main():
    set_compute_dps()
    w = WitnessBuilder("gap-a4-T10-mckay-character-2I-probe",
                       engine="mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-06-gap-a4-T4-T8-functor-search-retrospective.md"
    )
    w.set_description(
        "GAP-A-4 T10 — McKay-character / spin-lift candidate functor via "
        "2I (binary icosahedral, double cover of I ≅ A_5). The dim-5 irrep "
        "H is integer-spin → χ_5^{2I} = χ_5^{A_5} ∘ π, so the spin-lift "
        "adds NO new structure at dim-5. REFUTED as the 6th candidate."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)

    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    result = test_spin_lift_kernel()
    w.add_data("spin_lift_test", result)

    w.add_assertion(
        "integer_spin_dim_sum_squares",
        computed=float(result["int_burnside_sum_sq"]),
        expected=60.0,
        tolerance=1e-30,
        source=(
            "Integer-spin 2I irreps factor through A_5; Σ dim² over "
            "them equals |A_5| = 60 (Burnside on the quotient)."
        ),
    )
    w.add_assertion(
        "half_spin_dim_sum_squares",
        computed=float(result["half_burnside_sum_sq"]),
        expected=60.0,
        tolerance=1e-30,
        source=(
            "Half-spin 2I irreps are genuinely 2I-valued; Σ dim² over "
            "them equals |2I| − |A_5| = 60."
        ),
    )
    w.add_assertion(
        "total_2I_burnside",
        computed=float(result["total_burnside_sum_sq"]),
        expected=120.0,
        tolerance=1e-30,
        source="Σ dim² over all 2I irreps = |2I| = 120.",
    )

    synthesis = (
        "The dim-5 irrep H is on the INTEGER-SPIN side of 2I "
        "(integer-spin irreps have dims (1,3,3,4,5) = exactly the A_5 "
        "irrep dimensions; half-spin are (2,4,6,2)). Therefore "
        "χ_5^{2I} = χ_5^{A_5} ∘ π via the natural projection π : 2I → A_5, "
        "i.e. the spin ℤ_2 is in the kernel of the dim-5 character. "
        "For any element g ∈ 2I projecting to id ∈ A_5 (such as a "
        "lifted β_Bor with writhe 0), χ_5^{2I}(g) = χ_5^{A_5}(id) = 5 "
        "exactly — independent of any q-deformation at the character-"
        "evaluation level. The McKay-character / spin-lift candidate is "
        "REFUTED — adding the spin double cover does NOT introduce new "
        "structure at the dim-5 level relevant to the cross-algebra h⁴. "
        "This is the 6th candidate functor REFUTED. The non-Schur-Weyl "
        "direction must involve genuinely non-character-theoretic "
        "structure: T11 (Klein invariants) or T12 (Bring discriminant)."
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
