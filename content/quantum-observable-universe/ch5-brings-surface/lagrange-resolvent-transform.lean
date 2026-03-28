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
  have : (5 : ℂ) * (2 * ↑Real.pi * Complex.I / 5) = ↑(2 * Real.pi) * Complex.I := by
    push_cast
    ring
  rw [this]
  exact Complex.exp_mul_I_two_pi_sub_eq_of_eq rfl |>.symm ▸ Complex.exp_two_pi_mul_I

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
  rw [show (5 : ℕ) = 1 + 4 from rfl, pow_add, pow_one] at h5
  exact (mul_right_eq_one₀.mp h5 |>.resolve_right (pow_ne_zero 4 hne)).symm ▸
    (mul_inv_cancel_left₀ hne (ζ ^ 4) ▸ eq_comm.mpr (inv_eq_of_mul_eq_one_right h5))

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
    Proof: unfold both sides, then show the inner sums are related by the
    reindexing identity Σ_j ζ^{kj} x_{j+1} = ζ^{-k} Σ_j ζ^{kj} x_j,
    which follows from ζ^4 = ζ⁻¹ (since ζ^5 = 1). -/
-- Ref: [manuscript] Ch. 6, §1
-- Ref: [bring1786] https://doi.org/10.1007/BF02386200
theorem lagrange_resolvent_diagonal_action
    (x : Fin 5 → ℂ) :
    ∀ k : Fin 5, lagrangeResolvent (cyclicPerm x) k = ζ⁻¹ ^ k.val * lagrangeResolvent x k := by
  intro k
  unfold lagrangeResolvent cyclicPerm
  -- Both sides have the form (1/√5) * (sum). Factor out the prefactor.
  -- It suffices to show the inner sums satisfy the shift identity.
  simp only
  -- Pull ζ⁻¹^k into the product with the prefactor
  ring_nf
  -- Reduce to showing equality of the expanded sums
  congr 1
  -- Expand sums over Fin 5 and simplify modular indices
  simp only [Fin.sum_univ_five, Fin.val_mk]
  norm_num
  -- Each case: use ζ^4 = ζ⁻¹ to equate shifted and unshifted terms
  have h4 : ζ ^ 4 = ζ⁻¹ := ζ_pow_four_eq_inv
  have h5 : ζ ^ 5 = 1 := ζ_pow_five
  -- Reduce all powers of ζ using ζ^5 = 1, then use ζ^4 = ζ⁻¹
  fin_cases k <;> simp_all only [Fin.val_mk] <;> ring

end QOU.BringsSurface
