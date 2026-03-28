/-!
# QOU.BringsSurface.lagrange_resolvent_transform — DFT diagonalises C₅ on Bring's surface

The discrete Fourier transform w_k = (1/√5) Σ ζ^{kj} x_j converts the
three power-sum constraints of the Bring surface into spectral form,
and the cyclic permutation σ acts diagonally: σ(w_k) = ζ^{-k} w_k.
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Complex.Exponential
import Mathlib.Data.Fin.Basic
import Mathlib.Algebra.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

namespace QOU.BringsSurface

-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] https://doi.org/10.1007/BF02386200
noncomputable def ζ : ℂ := Complex.exp (2 * Real.pi * Complex.I / 5)

/-- ζ is a primitive 5th root of unity: ζ^5 = 1.
    Follows from exp(2πi) = 1 since ζ^5 = exp(5 · 2πi/5) = exp(2πi). -/
-- Ref: [manuscript] Ch. 6, §1
lemma ζ_pow_five : ζ ^ 5 = 1 := by
  unfold ζ
  rw [← Complex.exp_nat_mul]
  congr 1
  push_cast
  ring

/-- ζ is nonzero (since it's a root of unity). -/
lemma ζ_ne_zero : ζ ≠ 0 := by
  intro h
  have := ζ_pow_five
  rw [h, zero_pow (by omega : 5 ≠ 0)] at this
  exact zero_ne_one this

/-- ζ^4 = ζ⁻¹, since ζ^5 = 1 implies ζ · ζ^4 = 1. -/
lemma ζ_pow_four_eq_inv : ζ ^ 4 = ζ⁻¹ := by
  have h5 := ζ_pow_five
  have hne := ζ_ne_zero
  rw [inv_eq_iff_eq_inv]
  rw [show (5 : ℕ) = 4 + 1 from rfl, pow_succ] at h5
  exact eq_inv_of_mul_eq_one_right h5

-- Power reduction lemmas: ζ^(5+n) = ζ^n
private lemma ζ_pow_reduce (n : ℕ) : ζ ^ (5 + n) = ζ ^ n := by
  rw [pow_add, ζ_pow_five, one_mul]

private lemma ζ_pow_6 : ζ ^ 6 = ζ := by
  have := ζ_pow_reduce 1; rw [pow_one] at this; exact this

private lemma ζ_pow_8 : ζ ^ 8 = ζ ^ 3 := by exact ζ_pow_reduce 3

private lemma ζ_pow_10 : ζ ^ 10 = 1 := by
  rw [show (10 : ℕ) = 5 + 5 from rfl, pow_add, ζ_pow_five, one_mul, ζ_pow_five]

private lemma ζ_pow_12 : ζ ^ 12 = ζ ^ 2 := by
  rw [show (12 : ℕ) = 5 + (5 + 2) from rfl]
  rw [ζ_pow_reduce, ζ_pow_reduce]

private lemma ζ_pow_16 : ζ ^ 16 = ζ := by
  rw [show (16 : ℕ) = 5 + (5 + (5 + 1)) from rfl]
  rw [ζ_pow_reduce, ζ_pow_reduce, ζ_pow_reduce, pow_one]

/-- The Lagrange resolvent (DFT) of coordinates on the Bring surface. -/
noncomputable def lagrangeResolvent (x : Fin 5 → ℂ) (k : Fin 5) : ℂ :=
  (1 / Complex.ofReal (Real.sqrt 5)) * ∑ j : Fin 5, ζ ^ (k.val * j.val) * x j

/-- The cyclic permutation σ: x_j ↦ x_{j+1 mod 5}. -/
def cyclicPerm (x : Fin 5 → ℂ) : Fin 5 → ℂ :=
  fun j => x ⟨(j.val + 1) % 5, Nat.mod_lt _ (by omega)⟩

/-- Part (1): w_0 = 0 from the constraint Σx_i = 0.
    At k=0, ζ^0 = 1, so w_0 = (1/√5) Σ x_j = 0. -/
-- Ref: [manuscript] Ch. 6, §1
theorem lagrange_resolvent_w0_vanishes
    (x : Fin 5 → ℂ)
    (h_sum : ∑ i, x i = 0) :
    lagrangeResolvent x ⟨0, by omega⟩ = 0 := by
  unfold lagrangeResolvent
  simp only [Fin.val_mk, Nat.zero_mul, pow_zero, one_mul]
  rw [h_sum, mul_zero]

/-- Part (2): The cyclic permutation acts diagonally on Lagrange resolvents.
    σ(w_k) = ζ^{-k} · w_k for all k.
    Proof: case-split on k ∈ Fin 5, expand sums, reduce ζ powers mod 5. -/
-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] https://doi.org/10.1007/BF02386200
theorem lagrange_resolvent_diagonal_action
    (x : Fin 5 → ℂ) :
    ∀ k : Fin 5, lagrangeResolvent (cyclicPerm x) k = ζ⁻¹ ^ k.val * lagrangeResolvent x k := by
  intro k
  -- Replace ζ⁻¹ with ζ^4 everywhere
  have hinv : ζ⁻¹ = ζ ^ 4 := ζ_pow_four_eq_inv.symm
  rw [hinv]
  -- Unfold definitions
  unfold lagrangeResolvent cyclicPerm
  -- Expand sums over Fin 5
  simp only [Fin.sum_univ_five, Fin.val_mk]
  -- Simplify modular arithmetic
  norm_num
  -- Case split on k and use power reduction + ring
  fin_cases k <;> simp only [Fin.val_mk] <;> ring_nf <;>
    simp only [ζ_pow_five, ζ_pow_6, ζ_pow_8, ζ_pow_10, ζ_pow_12, ζ_pow_16] <;>
    ring

end QOU.BringsSurface
