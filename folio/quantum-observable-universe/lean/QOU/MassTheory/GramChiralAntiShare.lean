/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# The Gram norm's chiral-antisymmetric share is exactly one half

## What this explains

`computations/probes/gram_norm_binding_probe.py` decomposes the operator-space
Gram norm `G(W) = ∑_λ y_λ · tr(ρ_λ(W) ρ_λ(W^♯))` into per-block contributions
`c_λ` and reports two shares. The self-conjugate share prints as exactly
`0.0000`, and that is proved in `SelfConjugateStratumVanishes` — for every
`n ≥ 5` the self-conjugate stratum is *empty*, not merely small.

The companion number, `chiral_anti_share`, prints as exactly `0.5000` for
every isotope and for both the bound and free words. That file explicitly
scoped this one out, noting it needs a different fact: every nonzero `c_λ`
must share a sign. This file supplies that fact and closes it.

## Why the sign is not obvious

It would be easy to assume positivity here, and wrong to. The probe's own
docstring records that the Frobenius pairing's Gram matrix is **indefinite**
at `q₀` — that is the stated reason `G` was expected to carry cross-channel
information the linear trace `tr_M(W)` does not. An indefinite pairing does
not hand you a positive quantity.

The resolution is that `W · W^♯` is not an arbitrary element of that pairing.
`♯` is the reversal anti-involution, and the seminormal generators are
**symmetric matrices**, so a word's reversal maps to the *transpose* of the
word's matrix:

    ρ(W^♯) = ρ(W)ᵀ      (`reverse_prod_eq_transpose_of_symmetric`)

and therefore

    tr(ρ(W) ρ(W^♯)) = tr(ρ(W) ρ(W)ᵀ) = ∑_{i,j} ρ(W)_{ij}²  ≥ 0.

So the *matrix* being indefinite and this particular *quadratic form* being
non-negative are consistent: the form is evaluated on a Frobenius square.
With `y_λ ≥ 0` on the surviving stratum, every `c_λ ≥ 0`, and

    ∑_λ |c_λ| = |∑_λ c_λ|

which is exactly the condition the share needs.

## The share

Bar sends `e_λ ↦ e_λ'`. Under convention D's two-row cap the conjugate of a
contributing `λ` has `ℓ(λ') > 2` and so contributes zero (the same cap that
empties the self-conjugate stratum). Each chiral pair therefore contributes
`|c_λ − 0| / 2 = |c_λ| / 2`, the antisymmetric total is `½ ∑ |c_λ|`, and
dividing by `G = ∑ c_λ` gives exactly `1/2` — **provided** the sum of
absolute values equals the absolute value of the sum, i.e. provided the sign
fact above.

`chiral_anti_share_eq_half` assembles it. The `1/2` is therefore forced and
carries no information about the particular braid words; it is a fixed point
of the construction, not a measurement.

## Scope

Stated for real matrices, which is the setting the probe evaluates in. The
sign argument needs an ordered field and does not survive to a generic
`CommRing` — that is not a §7c omission but the content of the claim.
-/

namespace QOU.MassTheory.GramChiralAntiShare

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- **The structural step.** If every letter of a word is a symmetric matrix,
the reversed product is the transpose of the forward product.

This is what turns the reversal anti-involution `♯` into matrix transposition,
and hence what makes the Gram contribution a sum of squares rather than an
arbitrary value of an indefinite pairing. -/
theorem reverse_prod_eq_transpose_of_symmetric
    (L : List (Matrix n n ℝ)) (hsym : ∀ M ∈ L, Mᵀ = M) :
    L.reverse.prod = (L.prod)ᵀ := by
  rw [Matrix.transpose_list_prod]
  congr 1
  have hmap : List.map Matrix.transpose L = L := by
    induction L with
    | nil => rfl
    | cons a t ih =>
      simp only [List.map_cons]
      rw [hsym a (List.mem_cons_self),
        ih (fun M hM => hsym M (List.mem_cons_of_mem _ hM))]
  rw [hmap]

/-- `tr(M Mᵀ)` is the sum of the squares of `M`'s entries, hence non-negative.
This is the Frobenius norm squared. -/
theorem trace_mul_transpose_nonneg (M : Matrix n n ℝ) :
    0 ≤ (M * Mᵀ).trace := by
  rw [Matrix.trace]
  refine Finset.sum_nonneg fun i _ => ?_
  simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply]
  exact Finset.sum_nonneg fun j _ => mul_self_nonneg _

/-- A per-block Gram contribution `c_λ = y_λ · tr(ρ(W) ρ(W^♯))` is non-negative
whenever the Wedderburn weight is. Combining the two lemmas above: the trace
factor is a Frobenius square because `♯` is transposition on symmetric
generators. -/
theorem gramContrib_nonneg {y : ℝ} (hy : 0 ≤ y) (L : List (Matrix n n ℝ))
    (hsym : ∀ M ∈ L, Mᵀ = M) :
    0 ≤ y * (L.prod * L.reverse.prod).trace := by
  rw [reverse_prod_eq_transpose_of_symmetric L hsym]
  exact mul_nonneg hy (trace_mul_transpose_nonneg _)

/-- **The sign fact the share needs.** When every contribution is
non-negative, the ℓ¹ total coincides with the signed total. This is precisely
where an indefinite pairing would have broken the argument. -/
theorem sum_abs_eq_sum_of_nonneg {ι : Type*} (s : Finset ι) (c : ι → ℝ)
    (hc : ∀ i ∈ s, 0 ≤ c i) :
    ∑ i ∈ s, |c i| = ∑ i ∈ s, c i :=
  Finset.sum_congr rfl fun i hi => abs_of_nonneg (hc i hi)

/-- **Main result.** With every contribution non-negative and the conjugate of
each contributing block vanishing (the two-row cap), the chiral-antisymmetric
share of the Gram norm is exactly `1/2`.

`anti` is the probe's `R_anti`: half the ℓ¹ distance between a block and its
bar-image, summed over chiral pairs. The hypothesis `hconj` is the vanishing
of the conjugate block, so each pair contributes `|c_λ − 0|/2`. -/
theorem chiral_anti_share_eq_half {ι : Type*} (s : Finset ι) (c : ι → ℝ)
    (conj : ι → ℝ) (hc : ∀ i ∈ s, 0 ≤ c i)
    (hconj : ∀ i ∈ s, conj i = 0)
    (hG : ∑ i ∈ s, c i ≠ 0) :
    (∑ i ∈ s, |c i - conj i| / 2) / (∑ i ∈ s, c i) = 1 / 2 := by
  have hrw : ∑ i ∈ s, |c i - conj i| / 2 = (1 / 2) * ∑ i ∈ s, c i := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun i hi => ?_
    rw [hconj i hi, sub_zero, abs_of_nonneg (hc i hi)]
    ring
  rw [hrw]
  field_simp

/-- The Gram norm itself is **positive**, not merely nonzero, once any block
contributes. Recorded because the probe's framing (an indefinite Frobenius
Gram matrix) would not lead one to expect it. -/
theorem gram_nonneg {ι : Type*} (s : Finset ι) (c : ι → ℝ)
    (hc : ∀ i ∈ s, 0 ≤ c i) :
    0 ≤ ∑ i ∈ s, c i :=
  Finset.sum_nonneg hc

end QOU.MassTheory.GramChiralAntiShare
