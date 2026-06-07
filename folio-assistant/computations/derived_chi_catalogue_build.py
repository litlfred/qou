#!/usr/bin/env python3
"""derived_chi_catalogue_build.py — populate the 3-axis catalogue.

Phase 1 of the catalogue work-plan
(`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`).

This script emits the first three derived cells for the **Borromean**
knot operator (3 strands, atom = baryon/nucleon):

  (borromean, (3),     borromean-baryon)   χ = 1                  [algebraic]
  (borromean, (2,1),   borromean-baryon)   χ = 2 − 3h⁴ − h⁶       [R-matrix]
  (borromean, (1,1,1), borromean-baryon)   χ = 1                  [algebraic]

The (2,1) cell independently re-derives T17 (PR #1933 — currently open).
The (3) and (1,1,1) cells are derived algebraically from the 1-dim Hecke
reps σ_i → q and σ_i → −q⁻¹.

## R-matrix derivation (matches T17 conventions; gotchas baked in)

In the standard basis {↑↑, ↑↓, ↓↑, ↓↓} of `V⊗V` (V = ℂ²), the braided
R-matrix of `U_q(sl₂)` factors through the Hecke quotient
`(R − q)(R + q⁻¹) = 0`:

    R = q·E₁₁⊗E₁₁  +  q·E₂₂⊗E₂₂
        + E₂₂⊗E₁₁ + E₁₁⊗E₂₂            (off-diagonal flip part)
        + (q − q⁻¹)·E₂₁⊗E₁₂            (Hecke quotient correction)

Equivalently, in the 4×4 form on {↑↑, ↑↓, ↓↑, ↓↓}:

    R = [[ q,  0,        0,        0 ],
         [ 0,  q − q⁻¹,  1,        0 ],
         [ 0,  1,        0,        0 ],
         [ 0,  0,        0,        q ]]

This satisfies the Hecke relation `(R − q)(R + q⁻¹) = 0`, equivalently
`R² = (q − q⁻¹)·R + I`, which gives the **braided inverse**

    R⁻¹ = R − (q − q⁻¹)·I             (Gotcha 2 from T17 PR body)

(The naive `R⁻¹ = R(q ↦ q⁻¹)` is WRONG for the braided form; T17 hit
this and recorded it as a 0.39 numerical discrepancy.)

### Lifting to V⊗³

  σ_1 = R ⊗ I₂   (acts on strands 1,2)
  σ_2 = I₂ ⊗ R   (acts on strands 2,3)

Both are 8×8 matrices over ℚ(q).

### Borromean braid

    β_Bor = (σ_1⁻¹·σ_2)³

(The Borromean rings; convention matches T17 PR #1933.)

### Schur-Weyl trace decomposition

    tr_{V⊗³}(β_Bor) = dim(V_{3/2})·χ⁽³⁾(β_Bor) + dim(V_{1/2})·χ⁽²,¹⁾(β_Bor)
                    = 4·χ⁽³⁾(β_Bor) + 2·χ⁽²,¹⁾(β_Bor)

(Gotcha 1 from T17 PR body: **classical** dims `4` and `2`, NOT the
q-deformed `[4]_q` / `[2]_q`. T17 hit this and recorded it as a 0.13
discrepancy.) With `χ⁽³⁾ = 1` (algebraic), this lets us solve

    χ⁽²,¹⁾(β_Bor) = (tr − 4) / 2.

## Output

Writes `derived-chi-catalogue.witness.json` with the 3 cells + a
schema-versioned manifest. Asserts the (2,1) cell reproduces T17's
`2 − 3h⁴ − h⁶` to 50 dps.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue import (  # noqa: E402
    DerivedChiCatalogue,
    KnotPartitionAtomCell,
)


# ── Symbolic R-matrix machinery (T17-faithful) ─────────────────────


def build_r_matrix(q: sp.Symbol) -> sp.Matrix:
    """Braided R-matrix of U_q(sl₂) on V⊗V, basis {↑↑, ↑↓, ↓↑, ↓↓}.

    Satisfies the Hecke relation (R − q)(R + q⁻¹) = 0, equivalently
    R² = (q − q⁻¹)·R + I, so R⁻¹ = R − (q − q⁻¹)·I.
    """
    h = q - 1 / q
    return sp.Matrix([
        [q, 0,  0, 0],
        [0, h,  1, 0],
        [0, 1,  0, 0],
        [0, 0,  0, q],
    ])


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    """Kronecker product."""
    return sp.Matrix(sp.kronecker_product(a, b))


def lift_to_v_otimes_3(R: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
    """Lift R to σ_1 = R⊗I and σ_2 = I⊗R on V⊗³ (8×8 each)."""
    I2 = sp.eye(2)
    sigma_1 = kron(R, I2)
    sigma_2 = kron(I2, R)
    return sigma_1, sigma_2


def braided_inverse(R: sp.Matrix, q: sp.Symbol) -> sp.Matrix:
    """Braided inverse R⁻¹ = R − (q − q⁻¹)·I (Gotcha 2 in T17 PR body)."""
    return R - (q - 1 / q) * sp.eye(R.shape[0])


def borromean_braid_word_action(
    sigma_1: sp.Matrix, sigma_2: sp.Matrix, q: sp.Symbol
) -> sp.Matrix:
    """Compute the 8×8 action of β_Bor = (σ_1⁻¹·σ_2)³ on V⊗³."""
    # Lift braided inverse of R: σ_1⁻¹ = (R⁻¹)⊗I, σ_2⁻¹ = I⊗R⁻¹
    h_id = (q - 1 / q) * sp.eye(8)
    sigma_1_inv = sigma_1 - h_id  # σ_1⁻¹ = σ_1 − (q − q⁻¹)·I
    factor = sigma_1_inv * sigma_2
    return factor * factor * factor


# ── 1-dim Hecke reps for the (3) and (1,1,1) blocks ────────────────


def chi_trivial_rep(braid_word_action_on_sigma_i: list[int], q: sp.Symbol) -> sp.Expr:
    """Trivial rep: σ_i → q. So σ_i⁻¹ → q⁻¹.

    `braid_word_action_on_sigma_i` is a list of integers; sign indicates
    inverse (e.g. -1 means σ_1⁻¹). Returns the product of q^sign for
    each entry."""
    out = sp.Integer(1)
    for s in braid_word_action_on_sigma_i:
        out *= q if s > 0 else 1 / q
    return sp.simplify(out)


def chi_sign_rep(braid_word_action_on_sigma_i: list[int], q: sp.Symbol) -> sp.Expr:
    """Sign rep: σ_i → −q⁻¹. So σ_i⁻¹ → −q (from (−q⁻¹)·(−q) = 1).

    Returns the product over the braid word."""
    out = sp.Integer(1)
    for s in braid_word_action_on_sigma_i:
        out *= (-1 / q) if s > 0 else (-q)
    return sp.simplify(out)


# ── Main derivation ────────────────────────────────────────────────


def main() -> int:
    t0 = time.monotonic()
    wb = WitnessBuilder(
        "derived-chi-catalogue", engine="sympy", start_time=t0
    )
    wb.set_description(
        "Phase 1 of the 3-axis (knot, partition, atom) derived-χ "
        "catalogue. Emits the first three Borromean cells via "
        "R-matrix on V⊗³ (matches T17 / PR #1933 conventions) plus "
        "the (3) and (1,1,1) blocks from the 1-dim Hecke reps. "
        "Independent re-derivation; cross-validates T17."
    )

    q = sp.Symbol("q", positive=True)
    h = sp.Symbol("h")  # h = q − q⁻¹, the canonical Kassel-Faddeev variable
    # (matches T17 / PR #1933 — verified by `8 − 6h⁴ − 2h⁶|_{h=q−q⁻¹} =
    # −2q⁶ + 6q⁴ − 6q² + 12 − 6q⁻² + 6q⁻⁴ − 2q⁻⁶`, which equals tr_{V⊗³}(β_Bor)).

    # Borromean braid word: (σ_1⁻¹·σ_2)³  =  [−1, +2, −1, +2, −1, +2]
    bor_word_braid = [-1, +2, -1, +2, -1, +2]
    bor_word_pretty = "(σ_1^{-1}·σ_2)^3"

    # ── R-matrix derivation of the (2,1) character ──
    R = build_r_matrix(q)
    sigma_1, sigma_2 = lift_to_v_otimes_3(R)
    M = borromean_braid_word_action(sigma_1, sigma_2, q)
    tr_M = sp.expand(M.trace())
    tr_M = sp.simplify(tr_M)

    print("=" * 78)
    print(" 3-axis catalogue — Phase 1 Borromean cells (R-matrix derivation)")
    print("=" * 78)
    print(f"  Braid word: β_Bor = {bor_word_pretty}")
    print(f"  R-matrix on V⊗V matches T17 conventions (Hecke quotient).")
    print(f"  Braided inverse: R⁻¹ = R − (q − q⁻¹)·I  ✓")
    print()
    print(f"  tr_{{V⊗³}}(β_Bor) = {tr_M}")

    # Schur-Weyl: 4·χ^(3) + 2·χ^(2,1) = tr.  χ^(3) = 1 (algebraic).
    chi_3 = chi_trivial_rep(bor_word_braid, q)
    chi_111 = chi_sign_rep(bor_word_braid, q)
    print()
    print(f"  χ^(3)(β_Bor) = {chi_3}   (trivial Hecke rep)")
    print(f"  χ^(1,1,1)(β_Bor) = {chi_111}   (sign Hecke rep)")

    chi_21_in_q = sp.simplify((tr_M - 4 * chi_3) / 2)
    print(f"  χ^(2,1)(β_Bor) in q = {chi_21_in_q}")

    # ── Verify reproduction of T17's result ──
    # T17: χ^(2,1)(β_Bor) = 2 − 3h⁴ − h⁶ with h = q − q⁻¹.
    # We verify by substituting h = q − q⁻¹ and comparing as Laurent polys in q.
    T17_in_h = 2 - 3 * h ** 4 - h ** 6
    T17_in_q = sp.expand(T17_in_h.subs(h, q - 1 / q))
    diff = sp.simplify(chi_21_in_q - T17_in_q)
    matches_t17 = diff == 0
    print(f"  T17 prediction in q:  {sp.expand(T17_in_q)}")
    print(f"  difference (should be 0): {diff}")
    print()

    # ── Express χ^(2,1) as an h-polynomial (h = q − q⁻¹) for the catalogue ──
    # Strategy: T17 already gives the closed form; we record it directly,
    # backed by our independent computation matching T17 (the assertion below).
    chi_21_h_pairs = [(0, "2"), (4, "-3"), (6, "-1")] if matches_t17 else []

    wb.add_assertion(
        "rmatrix_reproduces_T17_chi_21",
        computed=matches_t17,
        expected=True,
        source="The independent R-matrix derivation of χ^(2,1)(β_Bor) "
               "must reproduce T17 (PR #1933): 2 − 3h⁴ − h⁶ to all orders ≤ h⁶. "
               "Cross-validates T17 and confirms the catalogue's first derived cell.",
    )

    wb.add_assertion(
        "chi_trivial_is_unity",
        computed=chi_3 == 1,
        expected=True,
        source="χ^(3)(β_Bor) from trivial Hecke rep (σ_i → q, σ_i⁻¹ → q⁻¹) "
               "evaluated on (σ_1⁻¹σ_2)^3 is q⁻¹·q·q⁻¹·q·q⁻¹·q = 1 exactly.",
    )

    wb.add_assertion(
        "chi_sign_is_unity",
        computed=chi_111 == 1,
        expected=True,
        source="χ^(1,1,1)(β_Bor) from sign Hecke rep (σ_i → −q⁻¹, σ_i⁻¹ → −q) "
               "evaluated on (σ_1⁻¹σ_2)^3 is ((−q)·(−q⁻¹))^3 = 1 exactly.",
    )

    # ── Populate the catalogue ──
    cat = DerivedChiCatalogue()

    derivation_self = (
        "qou/folio-assistant/computations/derived_chi_catalogue_build.py "
        "(this script; independent re-derivation cross-validating PR #1933 / T17)"
    )

    cat.add(KnotPartitionAtomCell(
        knot="borromean",
        partition=(3,),
        atom="borromean-baryon",
        braid_word=bor_word_pretty,
        strand_count=3,
        chi_lambda_q_taylor=[(0, "1")],
        mu_eigenvalues=["1"],
        k_lambda=2,  # not max-|μ| partition (per (2,1) being the standard)
        y_lambda_at_zero="1",  # trivial-rep Markov weight at q=1
        y_star_shadow_price=None,
        tier="derived",
        derivation_ref=derivation_self + " / trivial Hecke rep σ_i ↦ q",
        notes="χ^(3)(β_Bor) = 1 exactly (q-independent), from the 1-dim trivial Hecke rep.",
    ))

    cat.add(KnotPartitionAtomCell(
        knot="borromean",
        partition=(2, 1),
        atom="borromean-baryon",
        braid_word=bor_word_pretty,
        strand_count=3,
        chi_lambda_q_taylor=chi_21_h_pairs,
        mu_eigenvalues=["?", "?"],  # to be filled by Hoefsmit seminormal probe
        k_lambda=1,  # max-|μ| partition for β_Bor per prop:per-partition-k-lambda-rule
        y_lambda_at_zero="1/4",  # T18 result (PR #1933 cont. / b6c23f2053 on main)
        y_star_shadow_price=None,
        tier="derived",
        derivation_ref=(
            derivation_self
            + "; cross-validates PR #1933 (T17 R-matrix); "
              "y_lambda from main@b6c23f2053 (T18 Markov-normalisation)"
        ),
        notes=(
            "χ^(2,1)(β_Bor) = 2 − 3h⁴ − h⁶ derived independently via Schur-Weyl + "
            "R-matrix on V⊗³; reproduces T17 exactly. mu_eigenvalues populated in a "
            "follow-up commit using the Hoefsmit seminormal form."
        ),
    ))

    cat.add(KnotPartitionAtomCell(
        knot="borromean",
        partition=(1, 1, 1),
        atom="borromean-baryon",
        braid_word=bor_word_pretty,
        strand_count=3,
        chi_lambda_q_taylor=[(0, "1")],
        mu_eigenvalues=["1"],
        k_lambda=2,
        y_lambda_at_zero="1",  # sign-rep Markov weight at q=1
        y_star_shadow_price=None,
        tier="derived",
        derivation_ref=derivation_self + " / sign Hecke rep σ_i ↦ −q⁻¹",
        notes=(
            "χ^(1,1,1)(β_Bor) = 1 exactly (q-independent), from the 1-dim sign Hecke "
            "rep. Not visible in V⊗³ at U_q(sl₂); derived algebraically."
        ),
    ))

    # ── Emit witness ──
    wb.add_data("catalogue", cat.to_dict())
    wb.add_data("h_convention", "h = q − q⁻¹ (Kassel-Faddeev; matches T17 / PR #1933)")
    wb.add_data("rmatrix_trace_borromean_q", str(tr_M))
    wb.add_data("rmatrix_trace_borromean_h", "8 − 6h⁴ − 2h⁶  with  h = q − q⁻¹")
    wb.add_data("schur_weyl_check", {
        "tr_VotimesThree_in_q": str(tr_M),
        "four_times_chi_3": "4",
        "two_times_chi_21_in_q": str(sp.expand(2 * chi_21_in_q)),
        "sum_minus_tr": str(sp.simplify(4 + 2 * chi_21_in_q - tr_M)),
    })

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if matches_t17:
        print("  ✓ Independent R-matrix derivation reproduces T17's χ^(2,1) exactly.")
        print("  ✓ Trivial Hecke rep gives χ^(3) = 1.")
        print("  ✓ Sign Hecke rep gives χ^(1,1,1) = 1.")
        print()
        print(f"  Catalogue: {cat.tier_counts()}  (Phase 1 — 3 derived cells)")
    else:
        print(f"  ✗ MISMATCH vs T17: chi_21 − T17 = {diff}")
        print("  HALTING — do not emit a broken catalogue.")
        return 1

    out = wb.save()
    print()
    print(f"  ✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
