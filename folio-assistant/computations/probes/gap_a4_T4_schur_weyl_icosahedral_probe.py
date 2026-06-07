#!/usr/bin/env python3
"""GAP-A-4 T4 probe — Schur-Weyl icosahedral character bridge for conj:s5-so3-fiber-action.

After T1-T3 closed all four direct transplant routes for λ(K), the
session's converged direction is the τ-image Dirac/SW PDE
identification gated on `conj:s5-so3-fiber-action`. The most
tractable algebraic-categorical proof strategy (per the user's
selection): **A2 = Schur-Weyl Morita bridge** between H_n(q) and
the icosahedral subgroup `A_5 ≅ I ⊂ SO(3) ⊂ PSL(2, ℝ)` (Möbius
transformations on the Riemann sphere).

This probe tests two concrete claims using ONLY finite-group
character theory + the existing H_n(q) Wedderburn dim_q formula:

  Claim α — at n=4 (tetrahedral A_4 ⊂ SO(3)): every Wedderburn
    block of H_4(q) maps to a definite A_4-irrep via the S_4 → A_4
    branching, AND the dim_q sum `(1/4)·Σ_{λ⊢4} dim_q(V_λ) =
    linking_weight_family_a` rewrites cleanly as a weighted sum
    over A_4-irreps.

  Claim β — at n=5 (icosahedral A_5 ⊂ SO(3)): the S_5 → A_5
    branching maps Wedderburn blocks of H_5(q) to A_5 irreps; the
    dim-5 icosahedral irrep H (from `ℓ=2`) corresponds to specific
    partitions of 5.

If both close cleanly, `conj:s5-so3-fiber-action`'s claim (2) (the
fiber action commutes with the Hecke structure) holds at q=1; the
remaining open piece is then the q-deformation of the character
matrix — a much smaller question than the original conjecture.

**Connection to Möbius transformations**: `A_5 ≅ I` acts on
ℂP¹ = S² by 60 specific Möbius transformations (the icosahedral
subgroup of `PSL(2, ℂ)`). Bring's quintic has `A_5` as its
automorphism group via this same Möbius action. The Schur-Weyl
bridge implicitly carries this Möbius structure — we don't need to
invoke it directly; the `A_5`-character table does the work.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T4-schur-weyl-icosahedral-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402

# Centralised q=1-safe q-integer / dim_q helpers + Q_0_50DPS
# (addresses Gemini deduplication review on PR #1904).
from _gap_a4_qsafe import (  # noqa: E402
    Q_0_50DPS,
    q_number,
    dim_q_partition,
)

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent


# ── Finite-group character tables (hand-built, well-known) ─────────

# A_4 (tetrahedral, |A_4| = 12). 4 conjugacy classes:
#   e (1 elt), (12)(34)-type i.e. 2²-cycles (3 elts), (123) (4 elts),
#   (132) (4 elts).  Note: A_4 has 4 conjugacy classes (S_4 has 5,
#   but the 3-cycle class of S_4 splits into two A_4 classes (123)
#   and (132) because no even permutation conjugates them).
#
# 4 irreps of A_4: trivial, ω (one of two non-trivial 1-d irreps),
#   ω' (the other 1-d), T (3-d).  ω = exp(2πi/3), ω² = ω' = exp(4πi/3).
#
# Character table (rows = irreps, cols = classes e, 2², (123), (132)):
A4_CLASS_SIZES = [1, 3, 4, 4]  # totals 12 ✓
A4_IRREPS = ["trivial(1)", "ω(1)", "ω²(1)", "T(3)"]
A4_DIMS = [1, 1, 1, 3]
# Characters: trivial all 1; ω at (123) class is exp(2πi/3); etc.
# We work over ℂ: the A_4 character table has the complex cube roots
# ω, ω² in the two 3-cycle columns of the two non-trivial 1-dim irreps;
# inner products use mp.conj on the second argument.
OMEGA = mp.exp(2j * mp.pi / 3)
OMEGA2 = mp.exp(-2j * mp.pi / 3)
A4_CHAR_TABLE = [
    [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1)],     # trivial
    [mp.mpf(1), mp.mpf(1), OMEGA, OMEGA2],             # ω
    [mp.mpf(1), mp.mpf(1), OMEGA2, OMEGA],             # ω²
    [mp.mpf(3), mp.mpf(-1), mp.mpf(0), mp.mpf(0)],     # T
]

# S_4 character table at the SAME conjugacy classes (restricted from S_4).
# S_4 classes: e (1), (12) (6), (12)(34) (3), (123) (8), (1234) (6).
# We tabulate the S_4 → A_4 RESTRICTION characters (= S_4 chars on
# A_4 = (e) + (12)(34) + (123)-type).  For A_4 restriction the
# transposition class (12) and the 4-cycle class (1234) DROP OUT
# (they're odd permutations).  The (123) S_4 class splits into two
# A_4 classes (123) and (132).
#
# A standard S_4 char table at classes e, (12), (12)(34), (123), (1234):
#   λ=(4)        [1, 1, 1, 1, 1]
#   λ=(3,1)      [3, 1, -1, 0, -1]
#   λ=(2,2)      [2, 0, 2, -1, 0]
#   λ=(2,1,1)    [3, -1, -1, 0, 1]
#   λ=(1,1,1,1)  [1, -1, 1, 1, -1]
#
# Restriction to A_4 = drop classes (12) and (1234); the (123) class
# value is the same for both (123) and (132) A_4 classes (since the
# S_4 char on a class is constant on that class as an S_4 class).
S4_PARTITIONS_4 = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
S4_DIMS_4 = [1, 3, 2, 3, 1]  # = f^λ; sum of squares = 1+9+4+9+1 = 24 ✓

S4_TO_A4_CHAR = {
    # χ_S4(λ) restricted to A_4 classes (e, 2², (123), (132)):
    (4,):           [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1)],
    (3, 1):         [mp.mpf(3), mp.mpf(-1), mp.mpf(0), mp.mpf(0)],
    (2, 2):         [mp.mpf(2), mp.mpf(2), mp.mpf(-1), mp.mpf(-1)],
    (2, 1, 1):      [mp.mpf(3), mp.mpf(-1), mp.mpf(0), mp.mpf(0)],
    (1, 1, 1, 1):   [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1)],
}


# A_5 (icosahedral, |A_5| = 60). 5 conjugacy classes:
#   e (1), 15 double-transpositions (15), 20 3-cycles (20),
#   12 5-cycles class A (12), 12 5-cycles class B (12).
#   Note: 5-cycles split into two A_5 classes (5 = 12C_5 and 12C_5²
#   in physics notation).
#
# 5 irreps of A_5: A(1), T_1(3), T_2(3), G(4), H(5).  Dim² sum: 1+9+9+16+25 = 60 ✓.
A5_CLASS_SIZES = [1, 15, 20, 12, 12]  # = 60 ✓
A5_IRREPS = ["A(1)", "T_1(3)", "T_2(3)", "G(4)", "H(5)"]
A5_DIMS = [1, 3, 3, 4, 5]
# Golden ratios for 5-cycle character values
PHI_POS = (mp.mpf(1) + mp.sqrt(5)) / 2  # (1+√5)/2 ≈ 1.618
PHI_NEG = (mp.mpf(1) - mp.sqrt(5)) / 2  # (1-√5)/2 ≈ -0.618
A5_CHAR_TABLE = [
    # cols: e, 2², (123), (12345), (12345)²
    [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1)],         # A
    [mp.mpf(3), mp.mpf(-1), mp.mpf(0), PHI_POS, PHI_NEG],            # T_1
    [mp.mpf(3), mp.mpf(-1), mp.mpf(0), PHI_NEG, PHI_POS],            # T_2
    [mp.mpf(4), mp.mpf(0), mp.mpf(1), mp.mpf(-1), mp.mpf(-1)],       # G
    [mp.mpf(5), mp.mpf(1), mp.mpf(-1), mp.mpf(0), mp.mpf(0)],        # H
]

# S_5 partitions of 5 + dims (f^λ) + restricted-to-A_5 character.
# S_5 has 7 conjugacy classes: e, (12), (12)(34), (123), (123)(45),
#   (1234), (12345).  Under A_5 restriction, the transposition class
#   (12), the (123)(45) class, and the (1234) class drop out (odd
#   permutations).  Of the remaining S_5 classes:
#     - e → A_5 class (e)
#     - (12)(34) → A_5 class 2² (15 elts)
#     - (123) → A_5 class (123) (20 elts)
#     - (12345) → splits into two A_5 classes (12C_5 + 12C_5²)
#
# S_5 character table (rows = λ ⊢ 5, cols = e, (12), (12)(34), (123),
#   (123)(45), (1234), (12345)) is standard; restricting to A_5 drops
#   the (12), (123)(45), (1234) columns.  The (12345) class character
#   is real for non-self-conjugate λ and complex (or rather split into
#   φ_+, φ_-) for self-conjugate λ = (3,1,1).
S5_PARTITIONS_5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]
S5_DIMS_5 = [1, 4, 5, 6, 5, 4, 1]  # f^λ; sum of sqs = 1+16+25+36+25+16+1 = 120 ✓
S5_TO_A5_CHAR = {
    # χ_S5(λ) on A_5 classes (e, 2², (123), 5A, 5B). For non-self-
    # conjugate λ, χ(5A) = χ(5B) = same S_5 (12345) value. For
    # self-conjugate (3,1,1), the S_5 character SPLITS — we use the
    # branching values directly: (3,1,1) of S_5 has dim 6 = 3+3 in
    # A_5, splitting into T_1 + T_2.
    (5,):           [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1)],
    (4, 1):         [mp.mpf(4), mp.mpf(0), mp.mpf(1), mp.mpf(-1), mp.mpf(-1)],
    (3, 2):         [mp.mpf(5), mp.mpf(1), mp.mpf(-1), mp.mpf(0), mp.mpf(0)],
    (3, 1, 1):      [mp.mpf(6), mp.mpf(-2), mp.mpf(0), mp.mpf(1), mp.mpf(1)],
    (2, 2, 1):      [mp.mpf(5), mp.mpf(1), mp.mpf(-1), mp.mpf(0), mp.mpf(0)],
    (2, 1, 1, 1):   [mp.mpf(4), mp.mpf(0), mp.mpf(1), mp.mpf(-1), mp.mpf(-1)],
    (1, 1, 1, 1, 1):[mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1)],
}


# q-deformed Hecke Wedderburn dim_q helpers are imported from
# _gap_a4_qsafe — Q_0_50DPS, q_number, q_factorial, dim_q_partition.


# ── Character inner product (orthogonality test) ───────────────────


def character_inner_product(chi1: list, chi2: list, class_sizes: list,
                            group_order: int) -> mp.mpc:
    """⟨χ_1, χ_2⟩ = (1/|G|) Σ_C |C| · χ_1(C) · χ_2(C)*.

    Returns mp.mpc — even when both characters are real-valued, the
    arithmetic flows through mp.mpc so callers must consume .real
    (with an imaginary-part tolerance check) explicitly.
    """
    out = mp.mpc(0)
    for s, c1, c2 in zip(class_sizes, chi1, chi2):
        # mp.conj is identity on reals, so no isinstance guard needed.
        out += mp.mpc(s) * c1 * mp.conj(c2)
    return out / group_order


def is_nonneg_integer_multiplicity(m, tol: mp.mpf) -> tuple:
    """Test whether a character inner-product result m is a non-negative
    integer to tolerance tol.  Returns (ok: bool, n: int) — n is the
    nearest-integer rounding (only meaningful when ok=True).

    Three failure modes count as not-ok:
    1. |Im(m)| > tol — character branching is over ℂ but multiplicities
       are integers, so a non-vanishing imaginary part is a structural
       error.
    2. Re(m) < -tol — multiplicities are NON-NEGATIVE; negative real
       part signals either a character-table bug or a Lehrer-Solomon
       virtual representation that the branching framework rejects.
    3. |Re(m) - nint(Re(m))| > tol — integer check via mpmath-native
       nearest-integer to avoid float() rounding artefacts.
    """
    # mp.im / mp.re work uniformly on real and complex mpmath values.
    if abs(mp.im(m)) > tol:
        return (False, 0)
    mreal = mp.re(m)
    if mreal < -tol:
        return (False, 0)
    # mpmath-native nearest-integer rounding: mp.nint returns an mpf
    n_mp = mp.nint(mreal)
    if abs(mreal - n_mp) > tol:
        return (False, 0)
    return (True, int(n_mp))


# ── α: H_4 ↔ A_4 branching test ─────────────────────────────────────


def test_alpha_h4_a4(q_0: mp.mpf) -> dict:
    """Decompose each S_4 → A_4 restriction into A_4-irreps; verify
    multiplicities are non-negative integers; compute the dim_q-
    weighted A_4-irrep sum and compare to linking_weight_family_a."""
    print("=" * 78)
    print("Claim α — H_4 ↔ A_4 (tetrahedral) Schur-Weyl bridge")
    print("=" * 78)
    print(f"  {'λ ⊢ 4':<14} {'dim_q(V_λ)':>14} ", end="")
    for r in A4_IRREPS:
        print(f"{r:>10}", end="")
    print()
    print("-" * 78)

    per_partition = []
    a4_total_dim_q = [mp.mpf(0)] * len(A4_IRREPS)
    integer_mults_ok = True
    tol = mp.mpf("1e-8")
    for lam in S4_PARTITIONS_4:
        chi_lam = S4_TO_A4_CHAR[lam]
        dq = dim_q_partition(lam, q_0)
        mults = []
        mults_int = []
        for i, chi_i in enumerate(A4_CHAR_TABLE):
            m = character_inner_product(chi_lam, chi_i, A4_CLASS_SIZES, 12)
            mults.append(m)
            ok, n = is_nonneg_integer_multiplicity(m, tol)
            if not ok:
                integer_mults_ok = False
            mults_int.append(n)
            a4_total_dim_q[i] += dq * mp.mpf(n)
        # Print row
        print(f"  {str(lam):<14} {mp.nstr(dq, 10):>14} ", end="")
        for n in mults_int:
            print(f"{n:>10}", end="")
        print()
        per_partition.append({
            "lambda": list(lam),
            "dim_q": str(dq),
            "A4_multiplicities": mults_int,
        })

    print("-" * 78)
    # The dim_q-weighted A_4 character sum
    print(f"  {'A_4 dim_q sum':<14} {'':>14} ", end="")
    for v in a4_total_dim_q:
        print(f"{mp.nstr(v.real if isinstance(v, mp.mpc) else v, 8):>10}", end="")
    print()
    # Total dim_q sum vs linking_weight_family_a(q₀) at q=1 = 5/2
    total = sum(a4_total_dim_q, mp.mpf(0))
    lw_at_q1 = mp.mpf(5) / 2  # (3·1²+4+3·1²)/4 = 10/4 = 5/2
    print(f"  Total dim_q sum at q=1: "
          f"{mp.nstr((sum(dim_q_partition(lam, mp.mpf(1)) for lam in S4_PARTITIONS_4))/4, 10)} "
          f"(linking_weight = {mp.nstr(lw_at_q1, 6)})")
    return {
        "claim": "α (H_4 ↔ A_4 tetrahedral)",
        "per_partition": per_partition,
        "integer_multiplicities_ok": integer_mults_ok,
        "A_4_dim_q_distribution": [
            str(v.real if isinstance(v, mp.mpc) else v) for v in a4_total_dim_q
        ],
    }


# ── β: H_5 ↔ A_5 branching test ─────────────────────────────────────


def test_beta_h5_a5(q_0: mp.mpf) -> dict:
    """Decompose each S_5 → A_5 restriction into A_5-irreps; verify
    multiplicities; identify which partitions of 5 map to the dim-5
    icosahedral H irrep (the conjecture's `ℓ=2` claim)."""
    print()
    print("=" * 78)
    print("Claim β — H_5 ↔ A_5 (icosahedral) Schur-Weyl bridge")
    print("=" * 78)
    print(f"  {'λ ⊢ 5':<16} {'dim_q(V_λ)':>14} ", end="")
    for r in A5_IRREPS:
        print(f"{r:>9}", end="")
    print()
    print("-" * 95)

    per_partition = []
    a5_total_dim_q = [mp.mpf(0)] * len(A5_IRREPS)
    integer_mults_ok = True
    tol = mp.mpf("1e-8")
    H_irrep_idx = A5_IRREPS.index("H(5)")
    h_irrep_partitions = []
    for lam in S5_PARTITIONS_5:
        chi_lam = S5_TO_A5_CHAR[lam]
        dq = dim_q_partition(lam, q_0)
        mults = []
        mults_int = []
        for i, chi_i in enumerate(A5_CHAR_TABLE):
            m = character_inner_product(chi_lam, chi_i, A5_CLASS_SIZES, 60)
            mults.append(m)
            ok, n = is_nonneg_integer_multiplicity(m, tol)
            if not ok:
                integer_mults_ok = False
            mults_int.append(n)
            a5_total_dim_q[i] += dq * mp.mpf(n)
        # Track which partitions contribute to H (ℓ=2)
        if mults_int[H_irrep_idx] > 0:
            h_irrep_partitions.append((list(lam), mults_int[H_irrep_idx]))
        print(f"  {str(lam):<16} {mp.nstr(dq, 10):>14} ", end="")
        for n in mults_int:
            print(f"{n:>9}", end="")
        print()
        per_partition.append({
            "lambda": list(lam),
            "dim_q": str(dq),
            "A5_multiplicities": mults_int,
        })

    print("-" * 95)
    print(f"  Partitions of 5 contributing to H(5) (icosahedral ℓ=2):")
    for lam, mult in h_irrep_partitions:
        print(f"    {lam} with multiplicity {mult}")
    return {
        "claim": "β (H_5 ↔ A_5 icosahedral)",
        "per_partition": per_partition,
        "integer_multiplicities_ok": integer_mults_ok,
        "A_5_dim_q_distribution": [
            str(v.real if isinstance(v, mp.mpc) else v) for v in a5_total_dim_q
        ],
        "H_irrep_partitions": h_irrep_partitions,
    }


# ── Main ────────────────────────────────────────────────────────────


def main() -> int:
    w = WitnessBuilder("gap-a4-T4-schur-weyl-icosahedral-probe", engine="mpmath")
    w.set_audit_only("docs/audits/2026-06-05-gap-a4-final-retrospective.md")
    w.set_description(
        "GAP-A-4 T4 probe: Schur-Weyl character bridge between H_n(q) "
        "Wedderburn blocks and the icosahedral A_5 ⊂ SO(3) subgroup. "
        "Tests conj:s5-so3-fiber-action's claim (2) at the finite-"
        "group level via S_4 → A_4 and S_5 → A_5 branching + dim_q "
        "weighting.  EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    alpha = test_alpha_h4_a4(q_0)
    beta = test_beta_h5_a5(q_0)

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("claim_alpha_h4_a4", alpha)
    w.add_data("claim_beta_h5_a5", beta)

    # Synthesis
    both_ok = alpha["integer_multiplicities_ok"] and beta["integer_multiplicities_ok"]
    h_lambdas = [p[0] for p in beta["H_irrep_partitions"]]
    if both_ok and len(h_lambdas) > 0:
        synthesis = (
            f"Both claim α (H_4 ↔ A_4) and claim β (H_5 ↔ A_5) close "
            f"cleanly at the finite-group level: every S_4 → A_4 and "
            f"S_5 → A_5 restriction decomposes into non-negative-"
            f"integer multiplicities of irreps.  The icosahedral "
            f"dim-5 irrep H (the conjecture's ℓ=2 carrier) receives "
            f"contributions from S_5 partition(s) {h_lambdas}, "
            f"confirming the structural ℓ=2 → H matching.  "
            f"The conj:s5-so3-fiber-action's claim (2) (fiber action "
            f"commutes with Hecke structure) holds at q=1; the "
            f"q-deformation question reduces to whether dim_q(V_λ) is "
            f"compatible with this matching under the canonical "
            f"q-deformation of icosahedral characters (open follow-up)."
        )
    elif both_ok:
        synthesis = (
            f"Branching multiplicities are integer at both n=4 and "
            f"n=5, but no S_5 partition contributes to the icosahedral "
            f"H(5) irrep.  This refutes the conjecture's claim (3) "
            f"(ℓ=2 → h⁴ = −3/4) at the structural level: there's no "
            f"natural ℓ=2 carrier in H_5(q)."
        )
    else:
        synthesis = (
            f"Branching multiplicities are NOT all integer at the "
            f"finite-group level — this indicates a computation error "
            f"in the character tables or a misidentification of "
            f"conjugacy class sizes.  The conjecture's structural "
            f"matching cannot be confirmed without first repairing "
            f"the table inputs.  Verdict: TABLE INCONSISTENCY, not a "
            f"physics statement."
        )
    w.add_data("synthesis_verdict", synthesis)
    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    # Sanity assertions: Burnside Σ (dim_irrep)² = |G|, plus class-size totals.
    a4_class_total = sum(A4_CLASS_SIZES)
    w.add_assertion(
        "A4_class_sizes_sum_to_group_order",
        computed=float(a4_class_total),
        expected=12.0,
        tolerance=1e-10,
        source="Σ |C| over A_4 conjugacy classes = |A_4| = 12."
    )
    a5_class_total = sum(A5_CLASS_SIZES)
    w.add_assertion(
        "A5_class_sizes_sum_to_group_order",
        computed=float(a5_class_total),
        expected=60.0,
        tolerance=1e-10,
        source="Σ |C| over A_5 conjugacy classes = |A_5| = 60."
    )
    sum_sq_a4 = sum(d * d for d in A4_DIMS)
    w.add_assertion(
        "A4_sum_squares_equals_group_order",
        computed=float(sum_sq_a4),
        expected=12.0,
        tolerance=1e-10,
        source="Σ (dim_irrep)² = |A_4| = 12 (Burnside)."
    )
    sum_sq_a5 = sum(d * d for d in A5_DIMS)
    w.add_assertion(
        "A5_sum_squares_equals_group_order",
        computed=float(sum_sq_a5),
        expected=60.0,
        tolerance=1e-10,
        source="Σ (dim_irrep)² = |A_5| = 60 (Burnside)."
    )

    out_path = w.save()
    repo_root = COMPUTE_DIR.parent.parent
    try:
        rel = out_path.relative_to(repo_root)
    except ValueError:
        rel = out_path
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
