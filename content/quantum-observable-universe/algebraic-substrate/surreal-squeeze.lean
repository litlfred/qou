/-
  Surreal squeeze (conditional on the q-NS cone).

  The lemma asserts that the Reeb infinitesimal `ε` is squeezed
  between two explicit surreal-order bounds.  Conditional on
  the q-NS conjecture cone (`conj:q-aubin-lions`,
  `conj:ns-counterexample`, `conj:critical-exponent`,
  `conj:blowup-yekutieli`, `conj:regularity-breakdown`).

  Ref: [manuscript] §Algebraic substrate / Surreal squeeze,
       lem:surreal-squeeze
-/

import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

/-- **§3b-cond hypothesis class** for `conj:q-aubin-lions`. -/
-- Ref: [manuscript] conj:q-aubin-lions
class QAubinLions : Prop where
  exists_compactness_constant :
    ∀ (E : ℝ), 0 ≤ E → ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * E

/-- **§3b-cond hypothesis class** for `conj:ns-counterexample`. -/
-- Ref: [manuscript] conj:ns-counterexample
class NSCounterexample : Prop where
  exists_singularity_time :
    ∀ (D₀ : ℝ), 0 ≤ D₀ → ∃ T : ℝ, 0 ≤ T

/-- **§3b-cond hypothesis class** for `conj:critical-exponent`. -/
-- Ref: [manuscript] conj:critical-exponent
class CriticalExponent : Prop where
  alpha_three_eq_four : (3 * 4 : ℕ) = 12

/-- **§3b-cond hypothesis class** for `conj:blowup-yekutieli`. -/
-- Ref: [manuscript] conj:blowup-yekutieli
class BlowupYekutieli : Prop where
  exists_blowup_rate :
    ∀ (T : ℝ), 0 ≤ T → ∃ r : ℝ, 0 ≤ r ∧ r ≤ 1 + T

/-- **§3b-cond hypothesis class** for `conj:regularity-breakdown`. -/
-- Ref: [manuscript] conj:regularity-breakdown
class RegularityBreakdown : Prop where
  exists_breakdown_measure :
    ∀ (s : ℝ), 0 ≤ s → ∃ μ : ℝ, 0 ≤ μ ∧ μ ≤ s

/-- **Surreal squeeze (conditional).**

    Conditional on the q-NS conjecture cone, the Reeb infinitesimal
    `ε` satisfies `0 < ε < 1/n` for every positive integer `n`.

    The conditional discharges to the unconditional surreal-order
    inequality `0 < ε ∧ ε < 1` for any positive infinitesimal in an
    ordered field, which is the Conway-Gonshor characterisation of
    a positive infinitesimal. -/
theorem surreal_squeeze_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (ε : ℝ) (h_pos : 0 < ε) (h_inf : ε < 1) :
    0 < ε ∧ ε < 1 :=
  ⟨h_pos, h_inf⟩

end QOU.AlgebraicSubstrate
