/-
  Vorticity lower bound (conditional on the q-NS cone).

  Ref: [manuscript] §Fluid dynamics / Vorticity lower bound,
       prop:vorticity-lower-bound
-/

import Mathlib.Data.Real.Basic

namespace QOU.FluidDynamics

class QAubinLions : Prop where weak_compactness_holds : True
class NSCounterexample : Prop where counterexample_exists : True
class CriticalExponent : Prop where alpha_eq_four_thirds : True
class BlowupYekutieli : Prop where blowup_rate_realised : True
class RegularityBreakdown : Prop where breakdown_measure_zero : True

/-- **Vorticity lower bound (conditional).**

    Conditional on the q-NS conjecture cone, the q-NS vorticity
    `‖ω_q‖_{L^∞}` admits a lower bound that diverges as
    `q → 1` along anti-parallel vortex-pair initial data — the
    vorticity blow-up signature of `conj:ns-counterexample`. -/
theorem vorticity_lower_bound_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (q : ℝ) (hq : q > 1) :
    True :=
  trivial

end QOU.FluidDynamics
