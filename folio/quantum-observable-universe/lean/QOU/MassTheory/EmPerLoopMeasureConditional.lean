import Mathlib.Tactic
import QOU.MassTheory.PerLoopMeasureShadowAssembly

/-!
# The per-loop measure as a conditional: `μ₁ = a₀ / 2` given the period-share identification

Bean `qou-l4t2`. The two-loop α_EM slot is `−h²[2]_q α² μ₁` (owner rulings 2026-11-28:
bar-odd join, one-factor measure, `EmFormBLoopMeasure`). This file states, over a generic
field, what fixes `μ₁`, and keeps the open part as a named hypothesis.

* **Derived (Clause B).** The channel count is `pairCount = 2`
  (`PerLoopMeasureShadowAssembly`, forced by the reality involution `ρ`).
* **Open (Φ, the germ-curvature period motion).** `GermPeriodShare μ₁ a₀` says the per-loop
  measure, summed over the channels, equals the heat-kernel coefficient `a₀`. This is the
  R2 / B2 τ-lift identification. The owner ruled on 2026-07-19 that it is not proved, and
  audit `2026-08-02-moc-gauss-manin-not-derivable` shows it does not follow from the `E⁴`
  model. No instance of this class exists anywhere, and none should be added.
* **Conclusion.** `μ₁ = a₀ / 2` (`perLoop_eq_half_heatKernel`). The value of `a₀` is
  analytic (Clause A) and lives in `QOU.Transcendental.MassTheory.EmPerLoopMeasureConditionalReal`.

`perLoop_share_satisfiable` shows the class does not pin `a₀`: for every `a₀`, the pair
`(a₀/2, a₀)` satisfies it. So the content of `1/(8π)` is all in Clause A plus Φ, and this
file contributes only the factor `1/2`.

-- Ref: [leitner2026] Ch. mass-theory, per-loop measure (R2, phase-4 identification)
-/

set_option autoImplicit false

namespace QOU.MassTheory
namespace EmPerLoopMeasureConditional

open QOU.Archimedean.PerLoopMeasureShadowAssembly (pairCount)

variable {K : Type*} [Field K] [CharZero K]

/-- The Clause-B channel count, read in `K`. -/
def channelCount : K := ((pairCount : ℤ) : K)

theorem channelCount_eq_two : (channelCount : K) = 2 := by
  simp [channelCount, pairCount]

/-- **Open hypothesis (Φ / R2).** The per-loop measure `μ₁`, summed over the
`channelCount` conjugate channels, is the heat-kernel coefficient `a₀`. -/
class GermPeriodShare (μ₁ a₀ : K) : Prop where
  share : channelCount * μ₁ = a₀

/-- Conditional on `GermPeriodShare`, the per-loop measure is half the heat-kernel
coefficient. The `1/2` is the derived Clause-B channel count. -/
theorem perLoop_eq_half_heatKernel (μ₁ a₀ : K) [h : GermPeriodShare μ₁ a₀] :
    μ₁ = a₀ / 2 := by
  have hs := h.share
  rw [channelCount_eq_two] at hs
  rw [← hs]; ring

/-- The class does not fix `a₀`: every `a₀` has a compatible `μ₁`. -/
theorem perLoop_share_satisfiable (a₀ : K) : GermPeriodShare (a₀ / 2) a₀ :=
  ⟨by rw [channelCount_eq_two]; ring⟩

/-- Given the share, `μ₁` is unique. -/
theorem perLoop_unique (μ₁ μ₁' a₀ : K) [GermPeriodShare μ₁ a₀] [GermPeriodShare μ₁' a₀] :
    μ₁ = μ₁' := by
  rw [perLoop_eq_half_heatKernel μ₁ a₀, perLoop_eq_half_heatKernel μ₁' a₀]

end EmPerLoopMeasureConditional
end QOU.MassTheory
