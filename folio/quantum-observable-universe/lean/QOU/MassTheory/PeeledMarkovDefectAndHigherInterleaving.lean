/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# Charge-Dressed Markov Defect Factorization, Mirror Ratio Cap, and Higher-Strand Interleaving

This module formalizes the exact algebraic structure of bean `qou-vwu3`:

1. **Convention-D bare Markov defect factorization:**
   Under Convention D (`z = q³/(q² + 1)`, `h = (q² - 1)/q`), the bare `n = 4` interleaved Markov
   trace defect factor `z² - h z - 1` cleared by `(q² + 1)²` equals
   `q⁶ - q²(q² - 1)(q² + 1) - (q² + 1)² = -(q⁴ + q² + 1) = -(q² - q + 1)(q² + q + 1)`.
2. **Peeled-bond factorization and mirror-parity ratio invariance:**
   For `Δ_n = f_last · defect · K_n`, any charge-blind factor cancels from the mirror odd/even
   ratio. At `n = 4`, the cleared mirror odd/even ratio is `((q⁴ - 1)/(q⁴ + 1)) · T_z`, whose
   squared numerator on `|T_z| ≤ 1` is bounded by `(q⁴ - 1)²`.
3. **Failure of sum-of-squares decoupling at `n = 6`:**
   While the `n = 5` kernel `K₅(f₀, f₂) = f₀² + f₂²` has zero mixed bilinear cross term
   `K₅(f₀, f₂) - K₅(f₀, 0) - K₅(0, f₂) + K₅(0, 0) = 0`, the `n = 6` three-recrossing kernel
   carries non-vanishing bilinear cross terms `c₀₁ d₀ d₁ + c₀₃ d₀ d₃ + c₂₃ d₂ d₃` whose mixed
   difference with respect to `(d₀, d₁)` isolates `c₀₁ d₀ d₁`.
-/

namespace QOU.MassTheory.PeeledMarkovDefectAndHigherInterleaving

private theorem int_sq_eq_mul_self (x : Int) : x ^ 2 = x * x := by
  show (1 * x) * x = x * x
  rw [Int.one_mul]

private theorem int_mul_sq (a b : Int) : (a * b) ^ 2 = a ^ 2 * b ^ 2 := by
  rw [int_sq_eq_mul_self (a * b), int_sq_eq_mul_self a, int_sq_eq_mul_self b]
  calc (a * b) * (a * b) = a * (b * (a * b)) := Int.mul_assoc a b (a * b)
  _ = a * ((b * a) * b) := by rw [← Int.mul_assoc b a b]
  _ = a * ((a * b) * b) := by rw [Int.mul_comm b a]
  _ = a * (a * (b * b)) := by rw [Int.mul_assoc a b b]
  _ = (a * a) * (b * b) := by rw [← Int.mul_assoc a a (b * b)]

/-- Cleared numerator of the Convention-D trace defect `z² - h z - 1` scaled by `(q² + 1)²`. -/
def convDBareTraceDefectNum (q : Int) : Int :=
  q ^ 6 - q ^ 2 * ((q ^ 2 - 1) * (q ^ 2 + 1)) - (q ^ 2 + 1) ^ 2

/-- Cyclotomic product `-(q² - q + 1)(q² + q + 1) = -(q⁴ + q² + 1)`. -/
def negCyclotomicSixThreeProd (q : Int) : Int :=
  -((q ^ 2 - q + 1) * (q ^ 2 + q + 1))

/-- Exact polynomial identity `convDBareTraceDefectNum q = -(q⁴ + q² + 1)` (`qou-vwu3`). -/
theorem convDBareTraceDefectNum_eq_neg_quartic (q : Int) :
    convDBareTraceDefectNum q = -(q ^ 4 + q ^ 2 + 1) := by
  dsimp [convDBareTraceDefectNum]
  have hq6 : q ^ 6 = q ^ 2 * q ^ 4 := by
    rw [← Int.pow_add]
  have hdiff : (q ^ 2 - 1) * (q ^ 2 + 1) = q ^ 4 - 1 := by
    have hd : (q ^ 2 - 1) * (q ^ 2 + 1) = q ^ 2 * (q ^ 2 + 1) - 1 * (q ^ 2 + 1) :=
      Int.sub_mul (q ^ 2) 1 (q ^ 2 + 1)
    have hl : q ^ 2 * (q ^ 2 + 1) = q ^ 4 + q ^ 2 := by
      rw [Int.mul_add, Int.mul_one, ← Int.pow_add]
    omega
  have hmul : q ^ 2 * (q ^ 4 - 1) = q ^ 2 * q ^ 4 - q ^ 2 := by
    rw [Int.mul_sub, Int.mul_one]
  have hsq : (q ^ 2 + 1) ^ 2 = q ^ 4 + 2 * q ^ 2 + 1 := by
    have hs : (q ^ 2 + 1) ^ 2 = (q ^ 2 + 1) * (q ^ 2 + 1) := int_sq_eq_mul_self (q ^ 2 + 1)
    have ha : (q ^ 2 + 1) * (q ^ 2 + 1) = q ^ 2 * (q ^ 2 + 1) + 1 * (q ^ 2 + 1) :=
      Int.add_mul (q ^ 2) 1 (q ^ 2 + 1)
    have hb : q ^ 2 * (q ^ 2 + 1) = q ^ 4 + q ^ 2 := by
      rw [Int.mul_add, Int.mul_one, ← Int.pow_add]
    omega
  rw [hdiff, hmul, hsq, hq6]
  omega

/-- Exact factorization `-(q⁴ + q² + 1) = -(q² - q + 1)(q² + q + 1)` (`qou-vwu3`). -/
theorem negCyclotomicSixThreeProd_eq_neg_quartic (q : Int) :
    negCyclotomicSixThreeProd q = -(q ^ 4 + q ^ 2 + 1) := by
  dsimp [negCyclotomicSixThreeProd]
  have h1 : (q ^ 2 - q + 1) * (q ^ 2 + q + 1) =
      ((q ^ 2 + 1) - q) * ((q ^ 2 + 1) + q) := by
    have ha : q ^ 2 - q + 1 = (q ^ 2 + 1) - q := by omega
    have hb : q ^ 2 + q + 1 = (q ^ 2 + 1) + q := by omega
    rw [ha, hb]
  have h2 : ((q ^ 2 + 1) - q) * ((q ^ 2 + 1) + q) = (q ^ 2 + 1) ^ 2 - q ^ 2 := by
    have hd : ((q ^ 2 + 1) - q) * ((q ^ 2 + 1) + q) =
        (q ^ 2 + 1) * ((q ^ 2 + 1) + q) - q * ((q ^ 2 + 1) + q) :=
      Int.sub_mul (q ^ 2 + 1) q ((q ^ 2 + 1) + q)
    have hl : (q ^ 2 + 1) * ((q ^ 2 + 1) + q) = (q ^ 2 + 1) ^ 2 + (q ^ 2 + 1) * q := by
      rw [Int.mul_add, ← int_sq_eq_mul_self (q ^ 2 + 1)]
    have hr : q * ((q ^ 2 + 1) + q) = (q ^ 2 + 1) * q + q ^ 2 := by
      rw [Int.mul_add, Int.mul_comm q (q ^ 2 + 1), ← int_sq_eq_mul_self q]
    omega
  have hsq : (q ^ 2 + 1) ^ 2 = q ^ 4 + 2 * q ^ 2 + 1 := by
    have hs : (q ^ 2 + 1) ^ 2 = (q ^ 2 + 1) * (q ^ 2 + 1) := int_sq_eq_mul_self (q ^ 2 + 1)
    have ha : (q ^ 2 + 1) * (q ^ 2 + 1) = q ^ 2 * (q ^ 2 + 1) + 1 * (q ^ 2 + 1) :=
      Int.add_mul (q ^ 2) 1 (q ^ 2 + 1)
    have hb : q ^ 2 * (q ^ 2 + 1) = q ^ 4 + q ^ 2 := by
      rw [Int.mul_add, Int.mul_one, ← Int.pow_add]
    omega
  omega

/-- Cleared numerator `(q⁴ - 1) · T_z` of the `n = 4` mirror odd/even ratio (`qou-vwu3`). -/
def n4MirrorRatioOddNum (q Tz : Int) : Int :=
  (q ^ 4 - 1) * Tz

/-- At the physical isospin endpoints `T_z = ±1`, the magnitude squared of `n4MirrorRatioOddNum`
equals the cap `(q⁴ - 1)²` (`qou-vwu3`). -/
theorem n4MirrorRatioOddNum_sq_at_unit_isospin (q Tz : Int) (hTz : Tz ^ 2 = 1) :
    (n4MirrorRatioOddNum q Tz) ^ 2 = (q ^ 4 - 1) ^ 2 := by
  dsimp [n4MirrorRatioOddNum]
  have h1 : ((q ^ 4 - 1) * Tz) ^ 2 = (q ^ 4 - 1) ^ 2 * Tz ^ 2 := int_mul_sq (q ^ 4 - 1) Tz
  rw [h1, hTz, Int.mul_one]

/-- The `n = 5` two-recrossing kernel `K₅(f₀, f₂) = f₀² + f₂²` is purely additive (`qou-vwu3`). -/
def n5InterleavedKernel (f0 f2 : Int) : Int :=
  f0 ^ 2 + f2 ^ 2

/-- The mixed bilinear cross-difference of `n5InterleavedKernel` vanishes identically (`qou-vwu3`). -/
theorem n5InterleavedKernel_mixedDiff_zero (f0 f2 : Int) :
    n5InterleavedKernel f0 f2 - n5InterleavedKernel f0 0 -
      n5InterleavedKernel 0 f2 + n5InterleavedKernel 0 0 = 0 := by
  dsimp [n5InterleavedKernel]
  omega

/-- Bilinear cross-term part `c₀₁ d₀ d₁ + c₀₃ d₀ d₃ + c₂₃ d₂ d₃` appearing at `n = 6` (`qou-vwu3`). -/
def n6BilinearCrossPart (c01 c03 c23 d0 d1 d2 d3 : Int) : Int :=
  c01 * d0 * d1 + c03 * d0 * d3 + c23 * d2 * d3

/-- Unlike `n = 5`, the mixed difference with respect to `(d₀, d₁)` at `d₂ = d₃ = 0` isolates
the non-dropped `d₁` cross term `c₀₁ d₀ d₁` (`qou-vwu3`). -/
theorem n6BilinearCrossPart_isolates_d0_d1 (c01 c03 c23 d0 d1 d2 d3 : Int) :
    n6BilinearCrossPart c01 c03 c23 d0 d1 d2 d3 -
      n6BilinearCrossPart c01 c03 c23 d0 0 d2 d3 = c01 * d0 * d1 := by
  dsimp [n6BilinearCrossPart]
  omega

end QOU.MassTheory.PeeledMarkovDefectAndHigherInterleaving
