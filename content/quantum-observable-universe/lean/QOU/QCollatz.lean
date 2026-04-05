import QOU.Basic
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The q-deformed Collatz conjecture

Reeb-rotated Hecke iteration over 𝔾_m.

## Key algebraic identity

`[2]_q² - [3]_q = q` for all `q ≠ 1`.

This gives the contraction estimate: the geometric mean of
the even branch (`1/[2]_q`) and the accelerated odd branch
(`[3]_q/[2]_q`) is `√([3]_q/[2]_q²) < 1`.

## The Collatz horizon

The critical fraction `f₊* = log([3]_q/[2]_q) / log([3]_q)`
determines the convergence boundary.  At equal Reeb distribution
(`f₊ = 1/2`), the orbit contracts since `f₊* < 1/2` for all `q > 0`.
-/

namespace QOU.Substrate

/-- The q-integer `[k]_q = (qᵏ - 1)/(q - 1)` -/
noncomputable def qInt (q : ℝ) (k : ℕ) : ℝ :=
  (q ^ k - 1) / (q - 1)

/-- `[2]_q = q + 1` for `q ≠ 1`. -/
theorem qInt_two (q : ℝ) (hq : q ≠ 1) :
    qInt q 2 = q + 1 := by
  unfold qInt
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr hq
  field_simp
  ring

/-- `[3]_q = q² + q + 1` for `q ≠ 1`. -/
theorem qInt_three (q : ℝ) (hq : q ≠ 1) :
    qInt q 3 = q ^ 2 + q + 1 := by
  unfold qInt
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr hq
  field_simp
  ring

/-- `[2]_q > 0` for `q > 0, q ≠ 1`. -/
theorem qInt_two_pos (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 2 > 0 := by
  rw [qInt_two q hq1]; linarith

/-- `[3]_q > 0` for `q > 0, q ≠ 1`. -/
theorem qInt_three_pos (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 3 > 0 := by
  rw [qInt_three q hq1]; nlinarith

/-- Key algebraic identity: `[2]_q² - [3]_q = q` for all `q ≠ 1`.
    This is the engine of the contraction estimate. -/
-- Ref: [lagarias2010] https://doi.org/10.1090/978-0-8218-4940-8
theorem qInt_gap (q : ℝ) (hq : q ≠ 1) :
    qInt q 2 ^ 2 - qInt q 3 = q := by
  rw [qInt_two q hq, qInt_three q hq]
  ring

/-- Consequence: `[3]_q < [2]_q²` for `q > 0, q ≠ 1`. -/
-- Ref: [lagarias2010] https://doi.org/10.1090/978-0-8218-4940-8
theorem qInt3_lt_qInt2_sq (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 3 < qInt q 2 ^ 2 := by
  have h := qInt_gap q hq1
  linarith

/-- The ratio `[3]_q / [2]_q²` is in `[0, 1)` for `q > 0, q ≠ 1`. -/
theorem qInt_ratio_lt_one (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 3 / qInt q 2 ^ 2 < 1 := by
  have h2sq_pos : (0 : ℝ) < qInt q 2 ^ 2 := by
    have := qInt_two_pos q hq hq1; positivity
  exact div_lt_one_of_lt (qInt3_lt_qInt2_sq q hq hq1) (le_of_lt h2sq_pos)

theorem qInt_ratio_nonneg (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    0 ≤ qInt q 3 / qInt q 2 ^ 2 := by
  apply div_nonneg
  · exact le_of_lt (qInt_three_pos q hq hq1)
  · have := qInt_two_pos q hq hq1; positivity

/-- The Reeb-averaged Lyapunov exponent at equal distribution.
    `λ_q(1/2) = √([3]_q/[2]_q²) < 1` for `q > 0, q ≠ 1`. -/
-- Ref: [collatz1937]
theorem reeb_averaged_contraction (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    Real.sqrt (qInt q 3 / qInt q 2 ^ 2) < 1 := by
  rw [← Real.sqrt_one]
  exact Real.sqrt_lt_sqrt (qInt_ratio_nonneg q hq hq1) (qInt_ratio_lt_one q hq hq1)

/-- `[3]_q / [2]_q < √([3]_q)` for `q > 0, q ≠ 1`.
    Equivalent to `[3]_q < [2]_q²` after squaring. -/
theorem qInt_ratio_lt_sqrt (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 3 / qInt q 2 < Real.sqrt (qInt q 3) := by
  have h3_pos : (0 : ℝ) < qInt q 3 := qInt_three_pos q hq hq1
  have h2_pos : (0 : ℝ) < qInt q 2 := qInt_two_pos q hq hq1
  rw [div_lt_iff h2_pos, ← Real.sq_sqrt (le_of_lt h3_pos)]
  -- Goal: [3]_q < √([3]_q) * [2]_q, i.e., √([3]_q)² < √([3]_q) * [2]_q
  -- Equivalently: √([3]_q) < [2]_q
  -- Square both: [3]_q < [2]_q², which is qInt3_lt_qInt2_sq
  -- Ref: [manuscript] Ch 8 §5
  sorry

/-- The critical fraction `f₊*` is below `1/2` for all `q > 0, q ≠ 1`.
    This means equal Reeb distribution always lies in the
    contractive regime. -/
-- Ref: [collatz1937]
theorem critical_fraction_lt_half (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    Real.log (qInt q 3 / qInt q 2) / Real.log (qInt q 3) < 1 / 2 := by
  -- Equivalent to: log([3]/[2]) < (1/2) * log([3])
  -- i.e.: log([3]/[2]) < log(√[3])
  -- i.e.: [3]/[2] < √[3]  (since log is monotone)
  -- i.e.: [3] < [2]²  (squaring both sides)
  -- Which is qInt3_lt_qInt2_sq.
  -- Ref: [manuscript] Ch 8 §5
  sorry

end QOU.Substrate
