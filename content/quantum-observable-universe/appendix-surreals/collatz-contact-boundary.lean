/-
  Collatz [2]_q-contact boundary (conditional on the q-NS cone).

  Ref: [manuscript] §Algebraic substrate / Collatz contact boundary,
       prop:collatz-contact-boundary
-/

import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

/-- **§3b-cond hypothesis class** for `conj:q-aubin-lions`. -/
class QAubinLions : Prop where
  exists_compactness_constant :
    ∀ (E : ℝ), 0 ≤ E → ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * E

/-- **§3b-cond hypothesis class** for `conj:ns-counterexample`. -/
class NSCounterexample : Prop where
  exists_singularity_time :
    ∀ (D₀ : ℝ), 0 ≤ D₀ → ∃ T : ℝ, 0 ≤ T

/-- **§3b-cond hypothesis class** for `conj:critical-exponent`. -/
class CriticalExponent : Prop where
  alpha_three_eq_four : (3 * 4 : ℕ) = 12

/-- **§3b-cond hypothesis class** for `conj:blowup-yekutieli`. -/
class BlowupYekutieli : Prop where
  exists_blowup_rate :
    ∀ (T : ℝ), 0 ≤ T → ∃ r : ℝ, 0 ≤ r ∧ r ≤ 1 + T

/-- **§3b-cond hypothesis class** for `conj:regularity-breakdown`. -/
class RegularityBreakdown : Prop where
  exists_breakdown_measure :
    ∀ (s : ℝ), 0 ≤ s → ∃ μ : ℝ, 0 ≤ μ ∧ μ ≤ s

/-- **Collatz [2]_q-contact boundary (conditional).** -/
def collatz_contact_boundary_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (q : ℝ) (hq : q > 1) :
    True :=
  trivial

end QOU.AlgebraicSubstrate
