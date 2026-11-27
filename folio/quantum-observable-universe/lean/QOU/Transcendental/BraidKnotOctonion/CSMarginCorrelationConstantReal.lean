import BraidKnotOctonion.CSMarginCorrelationConstant
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# CS margin correlation constant: the `Real.sqrt` form (Transcendental companion)

Split from `BraidKnotOctonion.CSMarginCorrelationConstant` (bean `qou-dk7p`). That module
proves `ρ² = 24/25` over any characteristic-zero field; this file takes the square root at
`ℝ`. Original name and namespace kept.
-/

namespace QOU.BraidsAndKnots.CSMarginCorrelationConstant

/-- **The (CS) correlation is `ρ_P = 2√6/5` (sorry-free).**

Over `ℝ`, with `Â₃ = 8/(5π)`, `V_A = 8/(9π²)` and `π > 0`, the correlation `ρ_P = Â₃/√(3 V_A)`
equals `2√6/5`. Proved from the rational square (`csMargin_rhoSq_eq`) via `√`-of-square with both
sides nonnegative. This is the exact RHS of the leading-order margin `m∞ = ρ_P − √(V_D/V_A)`. -/
theorem csMargin_rho_eq {π : ℝ} (hπ : 0 < π) :
    (8 / (5 * π)) / Real.sqrt (3 * (8 / (9 * π ^ 2))) = 2 * Real.sqrt 6 / 5 := by
  have hπ' : π ≠ 0 := ne_of_gt hπ
  have hrad : (0 : ℝ) ≤ 3 * (8 / (9 * π ^ 2)) := by positivity
  have hlhs : (0 : ℝ) ≤ (8 / (5 * π)) / Real.sqrt (3 * (8 / (9 * π ^ 2))) := by positivity
  have hrhs : (0 : ℝ) ≤ 2 * Real.sqrt 6 / 5 := by positivity
  have hsq : ((8 / (5 * π)) / Real.sqrt (3 * (8 / (9 * π ^ 2)))) ^ 2
      = (2 * Real.sqrt 6 / 5) ^ 2 := by
    have hden : (Real.sqrt (3 * (8 / (9 * π ^ 2)))) ^ 2 = 3 * (8 / (9 * π ^ 2)) :=
      Real.sq_sqrt hrad
    have h6 : (Real.sqrt 6) ^ 2 = 6 := Real.sq_sqrt (by norm_num)
    rw [div_pow, hden, csMargin_rhoSq_eq π hπ', div_pow, mul_pow, h6]
    norm_num
  calc (8 / (5 * π)) / Real.sqrt (3 * (8 / (9 * π ^ 2)))
      = Real.sqrt (((8 / (5 * π)) / Real.sqrt (3 * (8 / (9 * π ^ 2)))) ^ 2) :=
        (Real.sqrt_sq hlhs).symm
    _ = Real.sqrt ((2 * Real.sqrt 6 / 5) ^ 2) := by rw [hsq]
    _ = 2 * Real.sqrt 6 / 5 := Real.sqrt_sq hrhs

end QOU.BraidsAndKnots.CSMarginCorrelationConstant
