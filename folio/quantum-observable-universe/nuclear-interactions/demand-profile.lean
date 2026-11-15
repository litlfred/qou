import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic


/-!
# QOU.ParticleInteractions.DemandProfile — Demand profile of a derived atom

The demand profile of a derived atom is the set of its negative
normal-form coefficients; the demand magnitude is the sum of their
absolute values.

LaTeX label: `def:demand-profile`

## References
- [leitner2026] §4/demand-profile
-/

namespace QOU.ParticleInteractions

/-- A normal-form expansion: a finite list of (word index, coefficient)
    pairs. The word is abstracted as a natural-number index. -/
abbrev NormalForm := List (ℕ × ℝ)

/-- The **demand profile** of a derived atom: the sublist of NF entries
    whose coefficient is strictly negative. -/
-- Ref: [leitner2026] §4/demand-profile
noncomputable def demandProfile (a : NormalForm) : NormalForm :=
  a.filter (fun wc => wc.2 < 0)

/-- The **demand magnitude** `|dem|`: the sum of absolute values of the
    negative coefficients. -/
-- Ref: [leitner2026] §4/demand-profile
noncomputable def demandMagnitude (a : NormalForm) : ℝ :=
  ((demandProfile a).map (fun wc => |wc.2|)).sum

/-- Every entry of the demand profile has a strictly negative coefficient. -/
theorem demandProfile_neg (a : NormalForm) :
    ∀ wc ∈ demandProfile a, wc.2 < 0 := by
  intro wc hwc
  simp only [demandProfile, List.mem_filter, decide_eq_true_eq] at hwc
  exact hwc.2

end QOU.ParticleInteractions
