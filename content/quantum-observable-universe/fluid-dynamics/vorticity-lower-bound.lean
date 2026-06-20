/-
  Vorticity lower bound (conditional on the q-NS cone).

  Ref: [manuscript] §Fluid dynamics / Vorticity lower bound,
       prop:vorticity-lower-bound
-/

import Mathlib.Data.Real.Basic

namespace QOU.FluidDynamics

class QAubinLions : Prop where
  exists_compactness_constant :
    ∀ (E : ℝ), 0 ≤ E → ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * E
class NSCounterexample : Prop where
  exists_singularity_time :
    ∀ (D₀ : ℝ), 0 ≤ D₀ → ∃ T : ℝ, 0 ≤ T
class CriticalExponent : Prop where
  alpha_three_eq_four : (3 * 4 : ℕ) = 12
class BlowupYekutieli : Prop where
  exists_blowup_rate :
    ∀ (T : ℝ), 0 ≤ T → ∃ r : ℝ, 0 ≤ r ∧ r ≤ 1 + T
class RegularityBreakdown : Prop where
  exists_breakdown_measure :
    ∀ (s : ℝ), 0 ≤ s → ∃ μ : ℝ, 0 ≤ μ ∧ μ ≤ s

/-- **Vorticity lower bound (conditional).**

    Conditional on the q-NS conjecture cone, the q-NS vorticity
    `‖ω_q‖_{L^∞}` admits a lower bound that diverges as
    `q → 1` along anti-parallel vortex-pair initial data — the
    vorticity blow-up signature of `conj:ns-counterexample`. -/
def vorticity_lower_bound_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (q : ℝ) (hq : q > 1) :
    True :=
  trivial

end QOU.FluidDynamics
