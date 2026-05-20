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
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum

namespace QOU.BringsSurface

-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] Bring, "Meletemata quaedam mathematica circa transformationem aequationum algebraicarum," Lund 1786
noncomputable def ζ : ℂ := Complex.exp (2 * Real.pi * Complex.I / 5)

/-- ζ is a primitive 5th root of unity: ζ^5 = 1.
    Since ζ = exp(2πi/5), we have ζ^5 = exp(5 · 2πi/5) = exp(2πi) = 1. -/
-- Ref: [manuscript] Ch. 6, §1
lemma ζ_pow_five : ζ ^ 5 = 1 := by
  unfold ζ
  rw [← Complex.exp_nat_mul]
  have h : (↑(5 : ℕ) : ℂ) * (2 * ↑Real.pi * Complex.I / 5) =
      ↑(1 : ℕ) * (2 * ↑Real.pi * Complex.I) := by push_cast; ring
  rw [h]
  exact Complex.exp_nat_mul_two_pi_mul_I 1

/-- ζ is nonzero (since ζ^5 = 1 ≠ 0). -/
lemma ζ_ne_zero : ζ ≠ 0 := by
  intro h
  have := ζ_pow_five
  rw [h, zero_pow (by omega : 5 ≠ 0)] at this
  exact zero_ne_one this

/-- ζ^4 = ζ⁻¹, since ζ^4 · ζ = ζ^5 = 1 = ζ⁻¹ · ζ. -/
lemma ζ_pow_four_eq_inv : ζ ^ 4 = ζ⁻¹ := by
  have h : ζ ^ 4 * ζ = 1 := by rw [← pow_succ, ζ_pow_five]
  exact mul_right_cancel₀ ζ_ne_zero (h.trans (inv_mul_cancel₀ ζ_ne_zero).symm)

/-- ζ^(5+n) = ζ^n (periodicity from ζ^5 = 1). -/
private lemma ζ_pow_add_five (n : ℕ) : ζ ^ (5 + n) = ζ ^ n := by
  rw [pow_add, ζ_pow_five, one_mul]

-- Simp lemmas reducing ζ^n for n ≥ 5 that appear after expanding k·j products.
-- The products k·j for k,j ∈ {0,1,2,3,4} range over {0,...,16}.
@[simp] private lemma ζ_r5  : ζ ^ 5  = 1     := ζ_pow_five
@[simp] private lemma ζ_r6  : ζ ^ 6  = ζ ^ 1 := ζ_pow_add_five 1
@[simp] private lemma ζ_r8  : ζ ^ 8  = ζ ^ 3 := ζ_pow_add_five 3
@[simp] private lemma ζ_r10 : ζ ^ 10 = 1     := by
  rw [show (10 : ℕ) = 5 + 5 from rfl, ζ_pow_add_five]; exact ζ_pow_five
@[simp] private lemma ζ_r12 : ζ ^ 12 = ζ ^ 2 := by
  rw [show (12 : ℕ) = 5 + 7 from rfl, ζ_pow_add_five,
      show (7 : ℕ) = 5 + 2 from rfl, ζ_pow_add_five]
@[simp] private lemma ζ_r15 : ζ ^ 15 = 1     := by
  rw [show (15 : ℕ) = 5 + 10 from rfl, ζ_pow_add_five]; exact ζ_r10
@[simp] private lemma ζ_r16 : ζ ^ 16 = ζ ^ 1 := by
  rw [show (16 : ℕ) = 5 + 11 from rfl, ζ_pow_add_five,
      show (11 : ℕ) = 5 + 6 from rfl, ζ_pow_add_five]; exact ζ_r6

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
    Proof: case-split on k ∈ {0,1,2,3,4}, expand the Fin 5 sums,
    reduce powers of ζ modulo 5 using ζ^5 = 1, and close by ring. -/
-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] Bring, "Meletemata quaedam mathematica circa transformationem aequationum algebraicarum," Lund 1786
theorem lagrange_resolvent_diagonal_action
    (x : Fin 5 → ℂ) :
    ∀ k : Fin 5, lagrangeResolvent (cyclicPerm x) k = ζ⁻¹ ^ k.val * lagrangeResolvent x k := by
  intro k
  -- Replace ζ⁻¹ with ζ^4 to work entirely with non-negative powers
  have hinv : ζ⁻¹ = ζ ^ 4 := ζ_pow_four_eq_inv.symm
  rw [hinv]
  -- Unfold the resolvent and permutation definitions
  unfold lagrangeResolvent cyclicPerm
  -- Expand sums over Fin 5 to get explicit 5-term expressions
  simp only [Fin.sum_univ_five, Fin.val_mk]
  -- Evaluate the modular arithmetic (j+1)%5 for each j = 0,1,2,3,4
  norm_num
  -- Case-split on k ∈ {0,1,2,3,4}, reduce ζ powers mod 5, close by ring
  fin_cases k <;> simp only [Fin.val_mk] <;> ring_nf <;>
    simp only [ζ_r5, ζ_r6, ζ_r8, ζ_r10, ζ_r12, ζ_r15, ζ_r16, pow_one, one_mul] <;>
    ring

end QOU.BringsSurface
