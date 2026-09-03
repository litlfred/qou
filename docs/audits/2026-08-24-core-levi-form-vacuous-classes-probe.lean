import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.FluidDynamics

-- Copied verbatim from fluid-dynamics/core-levi-form.lean.
class QAubinLions : Prop where
  exists_compactness_constant : ∀ (E : ℝ), 0 ≤ E → ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * E
class NSCounterexample : Prop where
  exists_singularity_time : ∀ (D₀ : ℝ), 0 ≤ D₀ → ∃ T : ℝ, 0 ≤ T
class CriticalExponent : Prop where
  alpha_three_eq_four : (3 * 4 : ℕ) = 12
class BlowupYekutieli : Prop where
  exists_blowup_rate : ∀ (T : ℝ), 0 ≤ T → ∃ r : ℝ, 0 ≤ r ∧ r ≤ 1 + T
class RegularityBreakdown : Prop where
  exists_breakdown_measure : ∀ (s : ℝ), 0 ≤ s → ∃ μ : ℝ, 0 ≤ μ ∧ μ ≤ s

-- If each of these elaborates, the carrier asserts nothing: it is inhabited
-- unconditionally, so every `[C]`-conditional theorem downstream is in fact
-- unconditional. No `sorry`, no `axiom`, no hypothesis used.
theorem aubin      : QAubinLions        := ⟨fun E hE => ⟨0, le_refl 0, by linarith⟩⟩
theorem ns         : NSCounterexample   := ⟨fun _ _ => ⟨0, le_refl 0⟩⟩
theorem crit       : CriticalExponent   := ⟨by norm_num⟩
theorem blowup     : BlowupYekutieli    := ⟨fun T hT => ⟨0, le_refl 0, by linarith⟩⟩
theorem breakdown  : RegularityBreakdown := ⟨fun s hs => ⟨0, le_refl 0, hs⟩⟩

#print axioms aubin
#print axioms ns
#print axioms crit
#print axioms blowup
#print axioms breakdown

end QOU.FluidDynamics
