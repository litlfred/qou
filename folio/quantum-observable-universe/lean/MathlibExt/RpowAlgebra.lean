/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Real.rpow ↔ Real.sqrt bridges for QOU substrate computations

Provides the conversion lemmas needed when closed forms are stated in
`Real.rpow` half-integer-exponent form but want to be discharged using
polynomial-in-sqrt-q identities.

Strategy: substitute `u := Real.sqrt q` (so q = u^2 for q ≥ 0), then
the rpow expressions become polynomial in u and `field_simp + ring`
closes the goal.

Ref: Mathlib.Analysis.SpecialFunctions.Pow.Real
Ref: Mathlib.Analysis.SpecialFunctions.Sqrt
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.MathlibExt.RpowAlgebra

/-- q^{1/2} = sqrt(q) for q ≥ 0. -/
theorem rpow_half (q : ℝ) (hq : 0 ≤ q) :
    q ^ ((1 : ℝ) / 2) = Real.sqrt q :=
  (Real.sqrt_eq_rpow q).symm

/-- q^{-1/2} = (sqrt q)⁻¹ for q > 0. -/
theorem rpow_neg_half (q : ℝ) (hq : 0 < q) :
    q ^ ((-1 : ℝ) / 2) = (Real.sqrt q)⁻¹ := by
  rw [show ((-1 : ℝ) / 2) = -((1 : ℝ) / 2) by ring]
  rw [Real.rpow_neg (le_of_lt hq), rpow_half q (le_of_lt hq)]

/-- (sqrt q)^2 = q for q ≥ 0. -/
theorem sqrt_sq_eq (q : ℝ) (hq : 0 ≤ q) :
    (Real.sqrt q) ^ 2 = q := by
  rw [sq, Real.mul_self_sqrt hq]

/-- q^{5/2} = (sqrt q)^5 for q ≥ 0.

    Proof: q^{5/2} = q^{2 + 1/2} = q^2 · q^{1/2} = (sqrt q)^4 · sqrt q
                  = (sqrt q)^5.
-/
theorem rpow_five_half (q : ℝ) (hq : 0 ≤ q) :
    q ^ ((5 : ℝ) / 2) = (Real.sqrt q) ^ 5 := by
  -- Write 5/2 = 2 + 1/2
  have h_decomp : ((5 : ℝ) / 2) = 2 + (1 : ℝ) / 2 := by ring
  rw [h_decomp]
  -- For q > 0 use Real.rpow_add; for q = 0 both sides are 0.
  rcases eq_or_lt_of_le hq with rfl | hq_pos
  · -- q = 0: 0^{5/2} = 0 = (sqrt 0)^5
    rw [Real.sqrt_zero, Real.zero_rpow (by norm_num : (2 + (1:ℝ)/2) ≠ 0)]; norm_num
  · rw [Real.rpow_add hq_pos]
    rw [rpow_half q hq]
    -- q^2 = (sqrt q)^4 via (sqrt q)^2 = q squared.
    have : q ^ (2 : ℝ) = (Real.sqrt q) ^ 4 := by
      rw [show (2 : ℝ) = ((2 : ℕ) : ℝ) by norm_num]
      rw [Real.rpow_natCast]
      rw [show (4 : ℕ) = 2 * 2 by rfl, pow_mul]
      rw [sqrt_sq_eq q hq]
    rw [this]
    ring

end QOU.MathlibExt.RpowAlgebra
