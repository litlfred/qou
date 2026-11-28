import Mathlib.Analysis.Real.Pi.Bounds
import QOU.MassTheory.EmPerLoopMeasureConditional
import QOU.MassTheory.EmFormBLoopMeasure

/-!
# `μ₁ = 1/(8π)` as a conditional on two named hypotheses

Bean `qou-l4t2`, archimedean half of `QOU.MassTheory.EmPerLoopMeasureConditional`.

* `HeatKernelLeadingCoeff a₀` is Clause A: `a₀ = 1/(4π)`, the leading
  Minakshisundaram–Pleijel coefficient of the heat kernel on a surface, per unit area.
  It is a standard analytic fact that Mathlib does not have. It is carried as a hypothesis
  here, so `π` appears only in this file.
* `GermPeriodShare μ₁ a₀` is the open Φ / R2 identification (see the generic file).

`perLoop_eq_inv_eight_pi`: both hypotheses together give `μ₁ = 1/(8π)`.
`formB_twoLoop_at_conditional_measure`: under the same hypotheses, the two-loop Form B
coefficient `s·μ₁·(−h²)` is `−s h²/(8π)`.

Neither class has an instance. This is the phase-4 identification stated as an
implication. It is not a derivation of `1/(8π)`, and nothing downstream may treat it as one.

-- Ref: [leitner2026] Ch. mass-theory, per-loop measure, Clause A (heat-kernel coefficient)
-/

set_option autoImplicit false

namespace QOU.Archimedean
namespace EmPerLoopMeasureConditionalReal

open QOU.MassTheory.EmPerLoopMeasureConditional
open QOU.MassTheory.EmFormBLoopMeasure

/-- **Hypothesis (Clause A).** The heat-kernel leading coefficient is `1/(4π)`. -/
class HeatKernelLeadingCoeff (a₀ : ℝ) : Prop where
  eq : a₀ = 1 / (4 * Real.pi)

/-- Conditional on Φ (`GermPeriodShare`) and Clause A, `μ₁ = 1/(8π)`. -/
theorem perLoop_eq_inv_eight_pi (μ₁ a₀ : ℝ) [GermPeriodShare μ₁ a₀]
    [ha : HeatKernelLeadingCoeff a₀] : μ₁ = 1 / (8 * Real.pi) := by
  rw [perLoop_eq_half_heatKernel μ₁ a₀, ha.eq]
  have : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp; ring

/-- Under the same two hypotheses, the one-loop-measure Form B coefficient at two
loops is `−s·h²/(8π)`. -/
theorem formB_twoLoop_at_conditional_measure (s h μ₁ a₀ : ℝ) [GermPeriodShare μ₁ a₀]
    [HeatKernelLeadingCoeff a₀] :
    formBCoeff s h μ₁ 1 = -(s * h ^ 2) / (8 * Real.pi) := by
  rw [perLoop_eq_inv_eight_pi μ₁ a₀]
  unfold formBCoeff
  ring

end EmPerLoopMeasureConditionalReal
end QOU.Archimedean
