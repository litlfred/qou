import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU

/-- Crossing energy `E_×(q) = (q − q⁻¹)/2`, local form for this
statement; to be unified with the climax-volume-mass declaration when
the proof is discharged. -/
noncomputable def crossingEnergyGap (q : ℝ) : ℝ := (q - q⁻¹) / 2

/-- **Physically normalised gap vanishes linearly.**  With
`ℏ_q = (q−1)/q`, the crossing-energy gap bound
`Δ_q = E_×(q)·(q−1)²` satisfies the exact identity
`Δ_q / ℏ_q² = q(q−1)(q+1)/2`: the archimedean normalisation buys
back two of the three vanishing orders at `q = 1`, no more. -/
theorem physical_units_gap_linear (q : ℝ) (h0 : q ≠ 0) (h1 : q ≠ 1) :
    (crossingEnergyGap q * (q - 1) ^ 2) / ((q - 1) / q) ^ 2
      = q * (q - 1) * (q + 1) / 2 := by
  -- Ref: [manuscript] models-of-qous/physical-units-gap-linear.md
  sorry

/-- At the symmetric point the categorical bound vanishes identically. -/
theorem gap_bound_vanishes_at_one :
    crossingEnergyGap 1 * ((1 : ℝ) - 1) ^ 2 = 0 := by
  -- Ref: [manuscript] models-of-qous/physical-units-gap-linear.md
  sorry

end QOU
