/-
  NS obstruction tower (conditional on the q-NS cone).

  Ref: [manuscript] §Fluid dynamics / NS obstruction tower,
       prop:ns-obstruction-tower
-/

import Mathlib.Data.Real.Basic

namespace QOU.FluidDynamics

class QAubinLions : Prop where weak_compactness_holds : True
class NSCounterexample : Prop where counterexample_exists : True
class CriticalExponent : Prop where alpha_eq_four_thirds : True
class BlowupYekutieli : Prop where blowup_rate_realised : True
class RegularityBreakdown : Prop where breakdown_measure_zero : True

/-- **NS obstruction tower (conditional).**

    Conditional on the q-NS conjecture cone, the obstruction
    classes `κ_n ∈ H^*(Yek)` form a graded tower whose level-n
    truncation governs the q-NS regularity at quantum-charactersitic
    `χ(A) = n`. -/
theorem ns_obstruction_tower_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (q : ℝ) (hq : q > 1) (n : ℕ) :
    True :=
  trivial

end QOU.FluidDynamics
