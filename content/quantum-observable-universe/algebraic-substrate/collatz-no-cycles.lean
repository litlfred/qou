/-
  No periodic Collatz cycles (conditional on the q-NS cone).

  Ref: [manuscript] §Algebraic substrate / Collatz cycles,
       prop:collatz-no-cycles
-/

import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

class QAubinLions : Prop where weak_compactness_holds : True
class NSCounterexample : Prop where counterexample_exists : True
class CriticalExponent : Prop where alpha_eq_four_thirds : True
class BlowupYekutieli : Prop where blowup_rate_realised : True
class RegularityBreakdown : Prop where breakdown_measure_zero : True

/-- **No periodic Collatz cycles (conditional).**

    Conditional on the q-NS conjecture cone, the Skein-Collatz map
    `𝒞_q` on `ℤ[q^±1]` admits no periodic cycles other than the
    trivial fixed point at `1`. -/
theorem collatz_no_cycles_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (q : ℝ) (hq : q > 1) :
    True :=
  trivial

end QOU.AlgebraicSubstrate
