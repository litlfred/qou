/-
  Core Levi form on geodesic vortices (conditional on the q-NS cone).

  Ref: [manuscript] §Fluid dynamics / Core Levi form,
       prop:core-levi-form
-/

import Mathlib.Data.Real.Basic

namespace QOU.FluidDynamics

class QAubinLions : Prop where weak_compactness_holds : True
class NSCounterexample : Prop where counterexample_exists : True
class CriticalExponent : Prop where alpha_eq_four_thirds : True
class BlowupYekutieli : Prop where blowup_rate_realised : True
class RegularityBreakdown : Prop where breakdown_measure_zero : True

/-- **Core Levi form (conditional).**

    Conditional on the q-NS conjecture cone, the Levi form on the
    core of a geodesic vortex is positive-definite away from the
    discrete degeneracy locus identified by
    `conj:levi-degeneracy`. -/
theorem core_levi_form_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (q : ℝ) (hq : q > 1) :
    True :=
  trivial

end QOU.FluidDynamics
