import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.Complex.Exponential
import Mathlib.Data.Fin.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity


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

/-- The primitive fifth root of unity `ζ = exp(2πi/5)` satisfies the fifth
cyclotomic equation `1 + ζ + ζ² + ζ³ + ζ⁴ = 0`. -/
lemma ζ_cyclotomic : 1 + ζ + ζ ^ 2 + ζ ^ 3 + ζ ^ 4 = 0 := by
  have h1 : (ζ - 1) * (1 + ζ + ζ ^ 2 + ζ ^ 3 + ζ ^ 4) = 0 := by
    calc (ζ - 1) * (1 + ζ + ζ ^ 2 + ζ ^ 3 + ζ ^ 4) = ζ ^ 5 - 1 := by ring
      _ = 1 - 1 := by rw [ζ_pow_five]
      _ = 0 := by ring
  have hne : ζ - 1 ≠ 0 := by
    intro hEq
    have hζ1 : ζ = 1 := sub_eq_zero.mp hEq
    have him : ζ.im = Real.sin (2 * Real.pi / 5) := by
      unfold ζ
      have harg : (2 * ↑Real.pi * Complex.I / 5 : ℂ) = ↑(2 * Real.pi / 5) * Complex.I := by
        push_cast; ring
      rw [harg, Complex.exp_ofReal_mul_I_im]
    have hsin0 : Real.sin (2 * Real.pi / 5) = 0 := by
      rw [← him, hζ1, Complex.one_im]
    have hpos : 0 < 2 * Real.pi / 5 := by positivity
    have hlt : 2 * Real.pi / 5 < Real.pi := by linarith [Real.pi_pos]
    have hsin_pos : 0 < Real.sin (2 * Real.pi / 5) :=
      Real.sin_pos_of_pos_of_lt_pi hpos hlt
    linarith
  exact (mul_eq_zero.mp h1).resolve_left hne

/-- Unscaled Lagrange resolvent mode `W_k = ∑_{j=0}^4 ζ^{k j} x_j` with reduced powers of `ζ`. -/
noncomputable def rawResolvent (x : Fin 5 → ℂ) : Fin 5 → ℂ
  | 0 => x 0 + x 1 + x 2 + x 3 + x 4
  | 1 => x 0 + ζ * x 1 + ζ ^ 2 * x 2 + ζ ^ 3 * x 3 + ζ ^ 4 * x 4
  | 2 => x 0 + ζ ^ 2 * x 1 + ζ ^ 4 * x 2 + ζ * x 3 + ζ ^ 3 * x 4
  | 3 => x 0 + ζ ^ 3 * x 1 + ζ * x 2 + ζ ^ 4 * x 3 + ζ ^ 2 * x 4
  | 4 => x 0 + ζ ^ 4 * x 1 + ζ ^ 3 * x 2 + ζ ^ 2 * x 3 + ζ * x 4

lemma lagrangeResolvent_eq_rawResolvent (x : Fin 5 → ℂ) (k : Fin 5) :
    lagrangeResolvent x k = (1 / Complex.ofReal (Real.sqrt 5)) * rawResolvent x k := by
  unfold lagrangeResolvent
  simp only [Fin.sum_univ_five]
  norm_num
  fin_cases k <;> simp [rawResolvent]

/-- **Unscaled Hermitian quadric identity:**
`2 * (W₁ W₄ + W₂ W₃) + W₀² = 5 * ∑_{j=0}^4 x_j²`. -/
theorem rawResolvent_hermitian_quadric_identity (x : Fin 5 → ℂ) :
    2 * (rawResolvent x 1 * rawResolvent x 4 +
         rawResolvent x 2 * rawResolvent x 3) +
      (rawResolvent x 0) ^ 2 =
      5 * ∑ j : Fin 5, (x j) ^ 2 := by
  simp only [rawResolvent, Fin.sum_univ_five]
  linear_combination
    (2*(x 0)*(x 1) + 2*(x 0)*(x 2) + 2*(x 0)*(x 3) + 2*(x 0)*(x 4) - 4*(x 1)^2 + 2*(x 1)*(x 2) + 2*(x 1)*(x 3) + 2*(x 1)*(x 4) - 4*(x 2)^2 + 2*(x 2)*(x 3) + 2*(x 2)*(x 4) - 4*(x 3)^2 + 2*(x 3)*(x 4) - 4*(x 4)^2 + ζ^4*(2*(x 1)*(x 4) + 2*(x 2)*(x 3)) + ζ^3*(2*(x 1)*(x 2) + 2*(x 1)*(x 3) - 2*(x 1)*(x 4) - 2*(x 2)*(x 3) + 2*(x 2)*(x 4) + 2*(x 3)*(x 4)) + ζ^2*(2*(x 1)*(x 4) + 2*(x 2)*(x 3)) + ζ*(4*(x 1)^2 - 2*(x 1)*(x 2) - 2*(x 1)*(x 3) - 2*(x 1)*(x 4) + 4*(x 2)^2 - 2*(x 2)*(x 3) - 2*(x 2)*(x 4) + 4*(x 3)^2 - 2*(x 3)*(x 4) + 4*(x 4)^2)) * ζ_cyclotomic

/-- **Part (3): Hermitian quadric identity on the Bring surface.**
The Lagrange resolvents satisfy
`2 * (w₁ w₄ + w₂ w₃) + w₀² = (1/√5)² * (5 * ∑_{j=0}^4 x_j²)`. -/
theorem lagrange_resolvent_hermitian_quadric_identity (x : Fin 5 → ℂ) :
    2 * (lagrangeResolvent x 1 * lagrangeResolvent x 4 +
         lagrangeResolvent x 2 * lagrangeResolvent x 3) +
      (lagrangeResolvent x 0) ^ 2 =
      (1 / Complex.ofReal (Real.sqrt 5)) ^ 2 * (5 * ∑ j : Fin 5, (x j) ^ 2) := by
  simp only [lagrangeResolvent_eq_rawResolvent]
  have hid := rawResolvent_hermitian_quadric_identity x
  linear_combination (1 / Complex.ofReal (Real.sqrt 5)) ^ 2 * hid

/-- When the first two power sums vanish (`∑ x_j = 0` and `∑ x_j² = 0`),
the Hermitian quadric `w₁ w₄ + w₂ w₃` vanishes identically. -/
theorem lagrange_resolvent_hermitian_quadric_vanishes (x : Fin 5 → ℂ)
    (h1 : ∑ j : Fin 5, x j = 0)
    (h2 : ∑ j : Fin 5, (x j) ^ 2 = 0) :
    lagrangeResolvent x 1 * lagrangeResolvent x 4 +
      lagrangeResolvent x 2 * lagrangeResolvent x 3 = 0 := by
  have hid := lagrange_resolvent_hermitian_quadric_identity x
  have hw0 : lagrangeResolvent x 0 = 0 := lagrange_resolvent_w0_vanishes x h1
  rw [hw0, h2] at hid
  linear_combination (1 / 2 : ℂ) * hid

/-- **Unscaled symmetric cubic identity:**
`3 * (W₁² W₃ + W₄² W₂ + W₂² W₁ + W₃² W₄) + 6 * W₀ * (W₁ W₄ + W₂ W₃) + W₀³ = 25 * ∑_{j=0}^4 x_j³`. -/
theorem rawResolvent_symmetric_cubic_identity (x : Fin 5 → ℂ) :
    3 * (rawResolvent x 1 ^ 2 * rawResolvent x 3 +
         rawResolvent x 4 ^ 2 * rawResolvent x 2 +
         rawResolvent x 2 ^ 2 * rawResolvent x 1 +
         rawResolvent x 3 ^ 2 * rawResolvent x 4) +
      6 * rawResolvent x 0 *
        (rawResolvent x 1 * rawResolvent x 4 +
         rawResolvent x 2 * rawResolvent x 3) +
      (rawResolvent x 0) ^ 3 =
      25 * ∑ j : Fin 5, (x j) ^ 3 := by
  simp only [rawResolvent, Fin.sum_univ_five]
  linear_combination
    (15*(x 0)^2*(x 1) + 15*(x 0)^2*(x 2) + 15*(x 0)^2*(x 3) + 15*(x 0)^2*(x 4) + 3*(x 0)*(x 1)^2 + 6*(x 0)*(x 1)*(x 2) + 6*(x 0)*(x 1)*(x 3) + 6*(x 0)*(x 1)*(x 4) + 3*(x 0)*(x 2)^2 + 6*(x 0)*(x 2)*(x 3) + 6*(x 0)*(x 2)*(x 4) + 3*(x 0)*(x 3)^2 + 6*(x 0)*(x 3)*(x 4) + 3*(x 0)*(x 4)^2 - 24*(x 1)^3 + 3*(x 1)^2*(x 2) + 3*(x 1)^2*(x 3) + 3*(x 1)^2*(x 4) + 3*(x 1)*(x 2)^2 + 6*(x 1)*(x 2)*(x 3) + 6*(x 1)*(x 2)*(x 4) + 3*(x 1)*(x 3)^2 + 6*(x 1)*(x 3)*(x 4) + 3*(x 1)*(x 4)^2 - 24*(x 2)^3 + 3*(x 2)^2*(x 3) + 3*(x 2)^2*(x 4) + 3*(x 2)*(x 3)^2 + 6*(x 2)*(x 3)*(x 4) + 3*(x 2)*(x 4)^2 - 24*(x 3)^3 + 3*(x 3)^2*(x 4) + 3*(x 3)*(x 4)^2 - 24*(x 4)^3 + ζ^8*(3*(x 1)^2*(x 2) + 3*(x 1)*(x 3)^2 + 3*(x 2)^2*(x 4) + 3*(x 3)*(x 4)^2) + ζ^7*(-3*(x 1)^2*(x 2) + 6*(x 1)^2*(x 3) + 3*(x 1)^2*(x 4) + 6*(x 1)*(x 2)^2 - 3*(x 1)*(x 3)^2 + 3*(x 1)*(x 4)^2 + 3*(x 2)^2*(x 3) - 3*(x 2)^2*(x 4) + 3*(x 2)*(x 3)^2 + 6*(x 2)*(x 4)^2 + 6*(x 3)^2*(x 4) - 3*(x 3)*(x 4)^2) + ζ^6*(6*(x 1)^3 - 6*(x 1)^2*(x 3) - 3*(x 1)^2*(x 4) - 6*(x 1)*(x 2)^2 + 12*(x 1)*(x 2)*(x 3) + 12*(x 1)*(x 2)*(x 4) + 12*(x 1)*(x 3)*(x 4) - 3*(x 1)*(x 4)^2 + 6*(x 2)^3 - 3*(x 2)^2*(x 3) - 3*(x 2)*(x 3)^2 + 12*(x 2)*(x 3)*(x 4) - 6*(x 2)*(x 4)^2 + 6*(x 3)^3 - 6*(x 3)^2*(x 4) + 6*(x 4)^3) + ζ^5*(-6*(x 1)^3 + 9*(x 1)^2*(x 2) + 3*(x 1)^2*(x 3) + 6*(x 1)^2*(x 4) + 3*(x 1)*(x 2)^2 + 9*(x 1)*(x 3)^2 + 6*(x 1)*(x 4)^2 - 6*(x 2)^3 + 6*(x 2)^2*(x 3) + 9*(x 2)^2*(x 4) + 6*(x 2)*(x 3)^2 + 3*(x 2)*(x 4)^2 - 6*(x 3)^3 + 3*(x 3)^2*(x 4) + 9*(x 3)*(x 4)^2 - 6*(x 4)^3) + ζ^4*(3*(x 0)*(x 1)^2 + 6*(x 0)*(x 1)*(x 2) + 6*(x 0)*(x 1)*(x 3) + 6*(x 0)*(x 1)*(x 4) + 3*(x 0)*(x 2)^2 + 6*(x 0)*(x 2)*(x 3) + 6*(x 0)*(x 2)*(x 4) + 3*(x 0)*(x 3)^2 + 6*(x 0)*(x 3)*(x 4) + 3*(x 0)*(x 4)^2 - 3*(x 1)^2*(x 2) + 6*(x 1)^2*(x 3) + 9*(x 1)^2*(x 4) + 6*(x 1)*(x 2)^2 + 6*(x 1)*(x 2)*(x 3) + 6*(x 1)*(x 2)*(x 4) - 3*(x 1)*(x 3)^2 + 6*(x 1)*(x 3)*(x 4) + 9*(x 1)*(x 4)^2 + 9*(x 2)^2*(x 3) - 3*(x 2)^2*(x 4) + 9*(x 2)*(x 3)^2 + 6*(x 2)*(x 3)*(x 4) + 6*(x 2)*(x 4)^2 + 6*(x 3)^2*(x 4) - 3*(x 3)*(x 4)^2) + ζ^3*(3*(x 0)*(x 1)^2 + 6*(x 0)*(x 1)*(x 2) + 6*(x 0)*(x 1)*(x 3) + 6*(x 0)*(x 1)*(x 4) + 3*(x 0)*(x 2)^2 + 6*(x 0)*(x 2)*(x 3) + 6*(x 0)*(x 2)*(x 4) + 3*(x 0)*(x 3)^2 + 6*(x 0)*(x 3)*(x 4) + 3*(x 0)*(x 4)^2 + 9*(x 1)^2*(x 2) + 6*(x 1)^2*(x 3) - 6*(x 1)^2*(x 4) + 6*(x 1)*(x 2)^2 + 6*(x 1)*(x 2)*(x 3) + 6*(x 1)*(x 2)*(x 4) + 9*(x 1)*(x 3)^2 + 6*(x 1)*(x 3)*(x 4) - 6*(x 1)*(x 4)^2 - 6*(x 2)^2*(x 3) + 9*(x 2)^2*(x 4) - 6*(x 2)*(x 3)^2 + 6*(x 2)*(x 3)*(x 4) + 6*(x 2)*(x 4)^2 + 6*(x 3)^2*(x 4) + 9*(x 3)*(x 4)^2) + ζ^2*(3*(x 0)*(x 1)^2 + 6*(x 0)*(x 1)*(x 2) + 6*(x 0)*(x 1)*(x 3) + 6*(x 0)*(x 1)*(x 4) + 3*(x 0)*(x 2)^2 + 6*(x 0)*(x 2)*(x 3) + 6*(x 0)*(x 2)*(x 4) + 3*(x 0)*(x 3)^2 + 6*(x 0)*(x 3)*(x 4) + 3*(x 0)*(x 4)^2 + 6*(x 1)^2*(x 4) + 6*(x 1)*(x 2)*(x 3) + 6*(x 1)*(x 2)*(x 4) + 6*(x 1)*(x 3)*(x 4) + 6*(x 1)*(x 4)^2 + 6*(x 2)^2*(x 3) + 6*(x 2)*(x 3)^2 + 6*(x 2)*(x 3)*(x 4)) + ζ*(3*(x 0)*(x 1)^2 + 6*(x 0)*(x 1)*(x 2) + 6*(x 0)*(x 1)*(x 3) + 6*(x 0)*(x 1)*(x 4) + 3*(x 0)*(x 2)^2 + 6*(x 0)*(x 2)*(x 3) + 6*(x 0)*(x 2)*(x 4) + 3*(x 0)*(x 3)^2 + 6*(x 0)*(x 3)*(x 4) + 3*(x 0)*(x 4)^2 + 24*(x 1)^3 - 3*(x 1)^2*(x 2) - 3*(x 1)^2*(x 3) - 3*(x 1)^2*(x 4) - 3*(x 1)*(x 2)^2 - 6*(x 1)*(x 2)*(x 3) - 6*(x 1)*(x 2)*(x 4) - 3*(x 1)*(x 3)^2 - 6*(x 1)*(x 3)*(x 4) - 3*(x 1)*(x 4)^2 + 24*(x 2)^3 - 3*(x 2)^2*(x 3) - 3*(x 2)^2*(x 4) - 3*(x 2)*(x 3)^2 - 6*(x 2)*(x 3)*(x 4) - 3*(x 2)*(x 4)^2 + 24*(x 3)^3 - 3*(x 3)^2*(x 4) - 3*(x 3)*(x 4)^2 + 24*(x 4)^3)) * ζ_cyclotomic

/-- **Part (4): Symmetric cubic identity on the Bring surface.**
The Lagrange resolvents satisfy
`3 * (w₁² w₃ + w₄² w₂ + w₂² w₁ + w₃² w₄) + 6 * w₀ * (w₁ w₄ + w₂ w₃) + w₀³ = (1/√5)³ * (25 * ∑ x_j³)`. -/
theorem lagrange_resolvent_symmetric_cubic_identity (x : Fin 5 → ℂ) :
    3 * (lagrangeResolvent x 1 ^ 2 * lagrangeResolvent x 3 +
         lagrangeResolvent x 4 ^ 2 * lagrangeResolvent x 2 +
         lagrangeResolvent x 2 ^ 2 * lagrangeResolvent x 1 +
         lagrangeResolvent x 3 ^ 2 * lagrangeResolvent x 4) +
      6 * lagrangeResolvent x 0 *
        (lagrangeResolvent x 1 * lagrangeResolvent x 4 +
         lagrangeResolvent x 2 * lagrangeResolvent x 3) +
      (lagrangeResolvent x 0) ^ 3 =
      (1 / Complex.ofReal (Real.sqrt 5)) ^ 3 * (25 * ∑ j : Fin 5, (x j) ^ 3) := by
  simp only [lagrangeResolvent_eq_rawResolvent]
  have hid := rawResolvent_symmetric_cubic_identity x
  linear_combination (1 / Complex.ofReal (Real.sqrt 5)) ^ 3 * hid

/-- When the first three power sums vanish (`∑ x_j = 0`, `∑ x_j² = 0`, `∑ x_j³ = 0`),
the symmetric cubic `w₁² w₃ + w₄² w₂ + w₂² w₁ + w₃² w₄` vanishes identically. -/
theorem lagrange_resolvent_symmetric_cubic_vanishes (x : Fin 5 → ℂ)
    (h1 : ∑ j : Fin 5, x j = 0)
    (h2 : ∑ j : Fin 5, (x j) ^ 2 = 0)
    (h3 : ∑ j : Fin 5, (x j) ^ 3 = 0) :
    lagrangeResolvent x 1 ^ 2 * lagrangeResolvent x 3 +
      lagrangeResolvent x 4 ^ 2 * lagrangeResolvent x 2 +
      lagrangeResolvent x 2 ^ 2 * lagrangeResolvent x 1 +
      lagrangeResolvent x 3 ^ 2 * lagrangeResolvent x 4 = 0 := by
  have hid := lagrange_resolvent_symmetric_cubic_identity x
  have hw0 : lagrangeResolvent x 0 = 0 := lagrange_resolvent_w0_vanishes x h1
  have hq : lagrangeResolvent x 1 * lagrangeResolvent x 4 +
      lagrangeResolvent x 2 * lagrangeResolvent x 3 = 0 :=
    lagrange_resolvent_hermitian_quadric_vanishes x h1 h2
  rw [hw0, h3, hq] at hid
  linear_combination (1 / 3 : ℂ) * hid

/-- **Master theorem (`qou:QOU.BringsSurface.lagrange_resolvent_transform`):**
1. The cyclic permutation `σ` acts diagonally on the Lagrange resolvents:
   `σ(w_k) = ζ^{-k} w_k` for all `k ∈ {0, 1, 2, 3, 4}`.
2. On the Bring surface (`∑ x_j = 0`, `∑ x_j² = 0`, `∑ x_j³ = 0`), the three power-sum
   constraints transform into the linear projection `w₀ = 0`, the Hermitian quadric
   `w₁ w₄ + w₂ w₃ = 0`, and the symmetric cubic
   `w₁² w₃ + w₄² w₂ + w₂² w₁ + w₃² w₄ = 0`. -/
theorem lagrange_resolvent_transform (x : Fin 5 → ℂ)
    (h1 : ∑ j : Fin 5, x j = 0)
    (h2 : ∑ j : Fin 5, (x j) ^ 2 = 0)
    (h3 : ∑ j : Fin 5, (x j) ^ 3 = 0) :
    (∀ k : Fin 5, lagrangeResolvent (cyclicPerm x) k = ζ⁻¹ ^ k.val * lagrangeResolvent x k) ∧
    lagrangeResolvent x 0 = 0 ∧
    lagrangeResolvent x 1 * lagrangeResolvent x 4 +
      lagrangeResolvent x 2 * lagrangeResolvent x 3 = 0 ∧
    lagrangeResolvent x 1 ^ 2 * lagrangeResolvent x 3 +
      lagrangeResolvent x 4 ^ 2 * lagrangeResolvent x 2 +
      lagrangeResolvent x 2 ^ 2 * lagrangeResolvent x 1 +
      lagrangeResolvent x 3 ^ 2 * lagrangeResolvent x 4 = 0 :=
  ⟨lagrange_resolvent_diagonal_action x,
   lagrange_resolvent_w0_vanishes x h1,
   lagrange_resolvent_hermitian_quadric_vanishes x h1 h2,
   lagrange_resolvent_symmetric_cubic_vanishes x h1 h2 h3⟩

end QOU.BringsSurface
