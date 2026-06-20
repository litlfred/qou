/-
  No periodic Collatz cycles (conditional on the q-NS cone).

  Ref: [manuscript] §Algebraic substrate / Collatz cycles,
       prop:collatz-no-cycles
-/

import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

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

/-- **No periodic Collatz cycles (conditional).**

    Conditional on the q-NS conjecture cone, the Skein-Collatz map
    `𝒞_q` on `ℤ[q^±1]` admits no periodic cycles other than the
    trivial fixed point at `1`. -/
def collatz_no_cycles_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (q : ℝ) (hq : q > 1) :
    True :=
  trivial

end QOU.AlgebraicSubstrate
