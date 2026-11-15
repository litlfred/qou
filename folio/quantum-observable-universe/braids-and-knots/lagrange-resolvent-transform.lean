import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Data.Fin.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum


/-!
# QOU.BringsSurface.lagrange_resolvent_transform — DFT diagonalises C₅ on Bring's surface

The discrete Fourier transform w_k = (1/√5) Σ ζ^{kj} x_j converts the
three power-sum constraints of the Bring surface into spectral form,
and the cyclic permutation σ acts diagonally: σ(w_k) = ζ^{-k} w_k.
-/
namespace QOU.BringsSurface

-- Ref: [leitner2026] Ch. 6, §1
-- Ref: [bring1786] Bring, "Meletemata quaedam mathematica circa transformationem aequationum algebraicarum," Lund 1786
noncomputable def ζ : ℂ := Complex.exp (2 * Real.pi * Complex.I / 5)

/-- ζ is a primitive 5th root of unity: ζ^5 = 1.
    Since ζ = exp(2πi/5), we have ζ^5 = exp(5 · 2πi/5) = exp(2πi) = 1. -/
-- Ref: [leitner2026] Ch. 6, §1
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

/-- **ζ-power reduction.**  `ζ^n = ζ^(n-5)` whenever `5 ≤ n`, from
    `ζ^5 = 1`.  As a conditional `simp` lemma this terminates: the
    exponent strictly decreases and the side condition fails once
    `n < 5`, so `simp` reduces any concrete power to its residue.

    **This replaces a hand-enumerated table** (`ζ^5, ζ^6, ζ^8, ζ^10,
    ζ^12, ζ^15, ζ^16`) whose comment justified the range as *"the
    products k·j for k,j ∈ {0,…,4} range over {0,…,16}"*.  That is
    true of the products and irrelevant to what the proof sees:
    `ring_nf` multiplies the `ζ^4` coming from `ζ⁻¹` into each term,
    so exponents reach `4·4 + 4·4 = 32`.  The `k = 4` case failed on
    `ζ^20, ζ^24, ζ^28, ζ^32`, none of them in the table.  A general
    lemma cannot go stale the way an enumerated one does. -/
@[simp] private lemma ζ_pow_reduce (n : ℕ) (h : 5 ≤ n) :
    ζ ^ n = ζ ^ (n - 5) := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le h
  simp [pow_add, ζ_pow_five]

/-- The Lagrange resolvent (DFT) of coordinates on the Bring surface. -/
noncomputable def lagrangeResolvent (x : Fin 5 → ℂ) (k : Fin 5) : ℂ :=
  (1 / Complex.ofReal (Real.sqrt 5)) * ∑ j : Fin 5, ζ ^ (k.val * j.val) * x j

/-- The cyclic permutation σ: x_j ↦ x_{j+1 mod 5}. -/
def cyclicPerm (x : Fin 5 → ℂ) : Fin 5 → ℂ :=
  fun j => x ⟨(j.val + 1) % 5, Nat.mod_lt _ (by omega)⟩

/-- Part (1): w_0 = 0 from the constraint Σx_i = 0.
    At k=0, ζ^0 = 1, so w_0 = (1/√5) Σ x_j = 0. -/
-- Ref: [leitner2026] Ch. 6, §1
theorem lagrange_resolvent_w0_vanishes
    (x : Fin 5 → ℂ)
    (h_sum : ∑ i, x i = 0) :
    lagrangeResolvent x ⟨0, by omega⟩ = 0 := by
  unfold lagrangeResolvent
  simp only [Nat.zero_mul, pow_zero, one_mul]
  rw [h_sum, mul_zero]

/-- Part (2): The cyclic permutation acts diagonally on Lagrange resolvents.
    σ(w_k) = ζ^{-k} · w_k for all k.
    Proof: case-split on k ∈ {0,1,2,3,4}, expand the Fin 5 sums,
    reduce powers of ζ modulo 5 using ζ^5 = 1, and close by ring. -/
-- Ref: [leitner2026] Ch. 6, §1
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
  simp only [Fin.sum_univ_five]
  -- Evaluate the modular arithmetic (j+1)%5 for each j = 0,1,2,3,4
  norm_num
  -- Case-split on k ∈ {0,1,2,3,4}, reduce ζ powers mod 5, close by ring
  fin_cases k <;> ring_nf <;> simp <;> ring

end QOU.BringsSurface
