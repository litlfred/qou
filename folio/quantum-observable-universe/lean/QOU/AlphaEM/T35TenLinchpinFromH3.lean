/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# The `[10]_q` linchpin of `T(3,5)`, from the actual `H₃(q)` representations

Bean `qou-15sj`.  The tree term `q·[9]_q·[10]_q` of every `α_em` form uses the
coefficient `[10]_q` for the torus knot `T(3,5) = closure of (σ₁σ₂)⁵`.  The
claim is that the 3-strand character sum of `(σ₁σ₂)⁵` collapses to
`q¹⁰ − q⁻¹⁰ = (q − q⁻¹)·[10]_q`.

PR #8177 proves the weight equivalence for *abstract* integer character values.
This file computes the characters from explicit representations of the Hecke
algebra `H₃(q)` (relation `σ² = (q − q⁻¹)σ + 1`) over any field:

* `V_(3)`: `σᵢ ↦ q`; character `q¹⁰`.
* `V_(1,1,1)`: `σᵢ ↦ −q⁻¹`; character `q⁻¹⁰`.
* a 2-dimensional representation `V_(2,1)` (`hookS1`, `hookS2`), checked to satisfy
  the Hecke and braid relations (`hook_hecke₁`, `hook_hecke₂`, `hook_braid`);
  its character on `(σ₁σ₂)⁵` is `−1` for every `q` (`hook_trace_T35`).

Then `t35_weights_unique`: a weighted sum `a·q¹⁰ + b·(−1) + c·q⁻¹⁰` equals
`q¹⁰ − q⁻¹⁰` for every nonzero rational `q` **iff** `(a, b, c) = (1, 0, −1)`.

**What this does not decide.** It proves that the collapse *requires* the
weights `(1, 0, −1)` (symmetric minus antisymmetric, hook dropped).  It does
not derive that the photon coupling *carries* those weights.  That remains the
open half of `qou-15sj`.  No measured value enters this file.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-/

namespace QOU.AlphaEM.T35Linchpin

open Matrix

section Hecke

variable {K : Type*} [Field K]

/-- `σ₁` on the 2-dimensional representation. -/
def hookS1 (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 1; 0, -q⁻¹]

/-- `σ₂` on the 2-dimensional representation. -/
def hookS2 (q : K) : Matrix (Fin 2) (Fin 2) K := !![-q⁻¹, 0; 1, q]

theorem hook_hecke₁ (q : K) (hq : q ≠ 0) :
    hookS1 q * hookS1 q = (q - q⁻¹) • hookS1 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [hookS1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

theorem hook_hecke₂ (q : K) (hq : q ≠ 0) :
    hookS2 q * hookS2 q = (q - q⁻¹) • hookS2 q + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [hookS2, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

theorem hook_braid (q : K) (hq : q ≠ 0) :
    hookS1 q * hookS2 q * hookS1 q = hookS2 q * hookS1 q * hookS2 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [hookS1, hookS2, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- The 1-dimensional characters satisfy the Hecke relation. -/
theorem sym_hecke (q : K) (hq : q ≠ 0) : q * q = (q - q⁻¹) * q + 1 := by
  field_simp; ring

theorem ext_hecke (q : K) (hq : q ≠ 0) :
    (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by
  field_simp; ring

/-- The character of `(σ₁σ₂)⁵` on the 2-dimensional representation is `−1`,
    independently of `q`. -/
theorem hook_trace_T35 (q : K) (hq : q ≠ 0) :
    ((hookS1 q * hookS2 q) ^ 5).trace = -1 := by
  have h3 : (hookS1 q * hookS2 q) ^ 3 = 1 := by
    ext i j; fin_cases i <;> fin_cases j <;>
      simp [hookS1, hookS2, pow_succ, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring
  have : (hookS1 q * hookS2 q) ^ 5 = (hookS1 q * hookS2 q) ^ 2 := by
    rw [show 5 = 3 + 2 from rfl, pow_add, h3, one_mul]
  rw [this, Matrix.trace_fin_two]
  simp [hookS1, hookS2, pow_two, Matrix.mul_apply, Fin.sum_univ_two]
  field_simp; ring

/-- Character of `(σ₁σ₂)⁵` on `V_(3)`. -/
theorem sym_char_T35 (q : K) : (q * q) ^ 5 = q ^ 10 := by ring

/-- Character of `(σ₁σ₂)⁵` on `V_(1,1,1)`. -/
theorem ext_char_T35 (q : K) : ((-q⁻¹) * (-q⁻¹)) ^ 5 = (q ^ 10)⁻¹ := by
  rw [neg_mul_neg, ← pow_two, ← pow_mul, inv_pow]

/-- `[n]_q = q^{n−1} + q^{n−3} + ⋯ + q^{1−n}`, written as a sum over `k < n`. -/
def qInt (n : ℕ) (q : K) : K := ∑ k ∈ Finset.range n, q ^ k * (q⁻¹) ^ (n - 1 - k)

/-- `(q − q⁻¹)·[10]_q = q¹⁰ − q⁻¹⁰`. -/
theorem binomial_eq_qInt_ten (q : K) (hq : q ≠ 0) :
    (q - q⁻¹) * qInt 10 q = q ^ 10 - (q ^ 10)⁻¹ := by
  simp [qInt, Finset.sum_range_succ]
  field_simp; ring

end Hecke

/-- **The `[10]_q` collapse forces the weights `(1, 0, −1)`.**  With the three
    actual characters of `(σ₁σ₂)⁵` (`q¹⁰`, `−1`, `q⁻¹⁰`), a weighted sum equals
    `q¹⁰ − q⁻¹⁰` for every nonzero rational `q` iff the weights are `(1, 0, −1)`. -/
theorem t35_weights_unique (a b c : ℚ) :
    (∀ q : ℚ, q ≠ 0 → a * q ^ 10 + b * (-1) + c * (q ^ 10)⁻¹ = q ^ 10 - (q ^ 10)⁻¹) ↔
      (a = 1 ∧ b = 0 ∧ c = -1) := by
  constructor
  · intro h
    have h1 := h 1 one_ne_zero
    have h2 := h 2 two_ne_zero
    have h3 := h (1 / 2) (by norm_num)
    norm_num at h1 h2 h3
    refine ⟨by linarith, by linarith, by linarith⟩
  · rintro ⟨rfl, rfl, rfl⟩ q _
    ring

/-- The convention-D Markov weights vanish on `(1,1,1)`, so they cannot produce
    the `[10]_q` collapse: with `c = 0` no `a, b` work. -/
theorem t35_no_collapse_without_antisymmetric (a b : ℚ) :
    ¬ ∀ q : ℚ, q ≠ 0 → a * q ^ 10 + b * (-1) + 0 * (q ^ 10)⁻¹ = q ^ 10 - (q ^ 10)⁻¹ := by
  intro h
  have := (t35_weights_unique a b 0).1 h
  norm_num at this

end QOU.AlphaEM.T35Linchpin
