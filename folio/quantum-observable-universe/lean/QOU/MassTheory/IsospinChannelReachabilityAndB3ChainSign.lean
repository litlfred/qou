/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# Isospin Channel Reachability Under Convention D and Two-Bond Chain `b₃` Sign Structure

This module formalizes the algebraic identities underlying beans `qou-kj4v` and `qou-q8vl`:

1. **`qou-kj4v` (Isospin T channel selection & Convention D deuteron reachability):**
   - On the two-nucleon Hecke algebra `H₂(q)`, the symmetric (`T = 1`, `P₊`) and antisymmetric
     (`T = 0`, `P₋`) projector trace weights satisfy `μ₊ + μ₋ = 1`, cleared over `ℤ[q, z]` as
     `(q z + 1) + (q² - q z) = q² + 1`.
   - Under Convention D (`z = q³ / (q² + 1)`, `h = (q² - 1) / q`), the singlet-triplet splitting
     numerator `2z - h` clears `q(q² + 1)` to `2q⁴ - (q² - 1)(q² + 1) = q⁴ + 1 > 0` for all `q`,
     forcing `μ₋ < μ₊` and binding the isospin singlet (`T = 0`) more strongly than the triplet.
   - Under Convention C (`z_C = q / (q² + 1)`), `2 z_C ≤ 1` because `(q² + 1) - 2q = (q - 1)² ≥ 0`,
     whereas under Convention D, `2 z_D - 1 = (q - 1)(2q² + q + 1) / (q² + 1) > 0` for `q > 1`,
     shifting the admissible interval `[z - h, z]` upward to contain the deuteron target.

2. **`qou-q8vl` (Two-bond chain `b₃` sign invariance under uniform reflection):**
   - For the `A = 3` two-bond chain, the third-order cumulant factor `φᵀ₃ = g₀₁ · g₁₂` is a
     product of two bond deviations `g_ij = μ_ij - 1`.
   - Reflecting both bond deviations (`g₀₁ ↦ -g₀₁`, `g₁₂ ↦ -g₁₂`) leaves `g₀₁ · g₁₂` strictly
     invariant, proving that uniform attraction across both bonds cannot flip the chain's `b₃` sign.
   - Achieving `-g₀₁ · g₁₂ > 0` on the two-bond chain requires sign-mixed deviations (`g_pn` and
     `g_nn`/`g_pp` of opposite sign), matching the physical deuteron-bound / diproton-dineutron-unbound
     two-nucleon spectrum.
-/

namespace QOU.MassTheory.IsospinChannelReachabilityAndB3ChainSign

private theorem int_sq_eq_mul_self (x : Int) : x ^ 2 = x * x := by
  show (1 * x) * x = x * x
  rw [Int.one_mul]

/-- Cleared numerator of the symmetric (`T = 1`) projector weight `μ₊ = (z + 1/q)/(q + 1/q)`,
scaled by `q(q² + 1)` where `z_num = z(q² + 1)`. -/
def isospinTripletClearedNum (q z_num : Int) : Int :=
  q * z_num + (q ^ 2 + 1)

/-- Cleared numerator of the antisymmetric (`T = 0`) projector weight `μ₋ = (q - z)/(q + 1/q)`,
scaled by `q(q² + 1)` where `z_num = z(q² + 1)`. -/
def isospinSingletClearedNum (q z_num : Int) : Int :=
  q ^ 2 * (q ^ 2 + 1) - q * z_num

/-- Common denominator `q(q + 1/q)(q² + 1) = (q² + 1)²` for the cleared projector weights. -/
def isospinProjectorClearedDenom (q : Int) : Int :=
  (q ^ 2 + 1) ^ 2

/-- Partition of unity `μ₊ + μ₋ = 1` cleared of denominators (`qou-kj4v`). -/
theorem isospinProjector_cleared_sum_eq_denom (q z_num : Int) :
    isospinTripletClearedNum q z_num + isospinSingletClearedNum q z_num =
      isospinProjectorClearedDenom q := by
  unfold isospinTripletClearedNum isospinSingletClearedNum isospinProjectorClearedDenom
  have hsq : (q ^ 2 + 1) ^ 2 = q ^ 2 * (q ^ 2 + 1) + (q ^ 2 + 1) := by
    rw [int_sq_eq_mul_self (q ^ 2 + 1), Int.add_mul, Int.one_mul]
  omega

/-- Cleared numerator of `2z - h` under Convention D (`z = q³/(q² + 1)`, `h = (q² - 1)/q`),
scaled by `q(q² + 1)`. -/
def convDTwoZSubHClearedNum (q : Int) : Int :=
  2 * (q * q ^ 3) - (q ^ 2 - 1) * (q ^ 2 + 1)

/-- Exact polynomial identity `2q⁴ - (q² - 1)(q² + 1) = q⁴ + 1` (`qou-kj4v`). -/
theorem convDTwoZSubHClearedNum_eq_pow4_add_one (q : Int) :
    convDTwoZSubHClearedNum q = q ^ 4 + 1 := by
  unfold convDTwoZSubHClearedNum
  have h1 : q * q ^ 3 = q ^ 4 := by
    rw [← Int.pow_succ']
  have h2 : (q ^ 2 - 1) * (q ^ 2 + 1) = q ^ 4 - 1 := by
    have hd : (q ^ 2 - 1) * (q ^ 2 + 1) = q ^ 2 * (q ^ 2 + 1) - 1 * (q ^ 2 + 1) :=
      Int.sub_mul (q ^ 2) 1 (q ^ 2 + 1)
    have hl : q ^ 2 * (q ^ 2 + 1) = q ^ 4 + q ^ 2 := by
      rw [Int.mul_add, Int.mul_one, ← Int.pow_add]
    omega
  omega

/-- Cleared gap `(q² + 1) - 2q` bounding Convention C's `2 z_C ≤ 1` (`qou-kj4v`). -/
def convCHalfCeilingGap (q : Int) : Int :=
  q ^ 2 + 1 - 2 * q

/-- Under Convention C, `(q² + 1) - 2q = (q - 1)²` (`qou-kj4v`). -/
theorem convCHalfCeilingGap_eq_sq (q : Int) :
    convCHalfCeilingGap q = (q - 1) ^ 2 := by
  unfold convCHalfCeilingGap
  have hsq : (q - 1) ^ 2 = (q - 1) * (q - 1) := int_sq_eq_mul_self (q - 1)
  have hq2 : q ^ 2 = q * q := int_sq_eq_mul_self q
  have hexp : (q - 1) * (q - 1) = q * q - 2 * q + 1 := by
    have ha : (q - 1) * (q - 1) = q * (q - 1) - 1 * (q - 1) := Int.sub_mul q 1 (q - 1)
    have hb : q * (q - 1) = q * q - q := by rw [Int.mul_sub, Int.mul_one]
    omega
  omega

/-- Cleared excess `2q³ - (q² + 1)` showing `2 z_D > 1` under Convention D for `q > 1` (`qou-kj4v`). -/
def convDHalfExcessNum (q : Int) : Int :=
  2 * q ^ 3 - (q ^ 2 + 1)

/-- Exact factorization `2q³ - q² - 1 = (q - 1)(2q² + q + 1)` (`qou-kj4v`). -/
theorem convDHalfExcessNum_factor (q : Int) :
    convDHalfExcessNum q = (q - 1) * (2 * q ^ 2 + q + 1) := by
  unfold convDHalfExcessNum
  have hq3 : q ^ 3 = q * q ^ 2 := by rw [Int.pow_succ']
  have hdist : (q - 1) * (2 * q ^ 2 + q + 1) =
      q * (2 * q ^ 2 + q + 1) - 1 * (2 * q ^ 2 + q + 1) :=
    Int.sub_mul q 1 (2 * q ^ 2 + q + 1)
  have hmul : q * (2 * q ^ 2 + q + 1) = 2 * (q * q ^ 2) + q * q + q := by
    calc q * (2 * q ^ 2 + q + 1)
      _ = q * (2 * q ^ 2 + q) + q * 1 := Int.mul_add q (2 * q ^ 2 + q) 1
      _ = q * (2 * q ^ 2) + q * q + q * 1 := by rw [Int.mul_add]
      _ = 2 * (q * q ^ 2) + q * q + q := by
          have h2 : q * (2 * q ^ 2) = 2 * (q * q ^ 2) := by
            rw [← Int.mul_assoc, Int.mul_comm q 2, Int.mul_assoc]
          omega
  have hq2 : q ^ 2 = q * q := int_sq_eq_mul_self q
  omega

/-- Two-bond chain Ursell cumulant `φᵀ₃ = g₀₁ · g₁₂` (`qou-q8vl`). -/
def twoBondChainCumulant (g01 g12 : Int) : Int :=
  g01 * g12

/-- Reflecting both bond deviations (`g₀₁ ↦ -g₀₁`, `g₁₂ ↦ -g₁₂`) leaves the two-bond chain
cumulant strictly invariant (`qou-q8vl`). -/
theorem twoBondChainCumulant_reflect_both_invariant (g01 g12 : Int) :
    twoBondChainCumulant (-g01) (-g12) = twoBondChainCumulant g01 g12 := by
  dsimp [twoBondChainCumulant]
  have h1 : (-g01) * (-g12) = g01 * g12 := Int.neg_mul_neg g01 g12
  exact h1

/-- Signed three-body binding contribution `-φᵀ₃ = -(g₀₁ · g₁₂)` on a two-bond chain (`qou-q8vl`). -/
def twoBondChainBindingContrib (g01 g12 : Int) : Int :=
  -(twoBondChainCumulant g01 g12)

/-- When the two chain bonds have opposite-sign deviations (`g_pn < 0` attractive, `g_like > 0`
repulsive), the three-body binding contribution `-g_pn · g_like` is strictly positive (`qou-q8vl`). -/
theorem twoBondChainBindingContrib_pos_of_sign_mixed (g_pn g_like : Int)
    (h_pn : g_pn < 0) (h_like : 0 < g_like) :
    0 < twoBondChainBindingContrib g_pn g_like := by
  unfold twoBondChainBindingContrib twoBondChainCumulant
  have hneg : g_pn * g_like < 0 := Int.mul_neg_of_neg_of_pos h_pn h_like
  omega

end QOU.MassTheory.IsospinChannelReachabilityAndB3ChainSign
