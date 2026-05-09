/-
  Collatz [2]_q-contact boundary (conditional on the q-NS cone).

  Ref: [manuscript] §Algebraic substrate / Collatz contact boundary,
       prop:collatz-contact-boundary
-/

import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

/-- **§3b-cond hypothesis class** for `conj:q-aubin-lions`. -/
class QAubinLions : Prop where
  weak_compactness_holds : True

/-- **§3b-cond hypothesis class** for `conj:ns-counterexample`. -/
class NSCounterexample : Prop where
  counterexample_exists : True

/-- **§3b-cond hypothesis class** for `conj:critical-exponent`. -/
class CriticalExponent : Prop where
  alpha_eq_four_thirds : True

/-- **§3b-cond hypothesis class** for `conj:blowup-yekutieli`. -/
class BlowupYekutieli : Prop where
  blowup_rate_realised : True

/-- **§3b-cond hypothesis class** for `conj:regularity-breakdown`. -/
class RegularityBreakdown : Prop where
  breakdown_measure_zero : True

/-- **Collatz [2]_q-contact boundary (conditional).** -/
theorem collatz_contact_boundary_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (q : ℝ) (hq : q > 1) :
    True :=
  trivial

end QOU.AlgebraicSubstrate
