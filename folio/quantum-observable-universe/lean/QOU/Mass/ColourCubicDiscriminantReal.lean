import QOU.Mass.ColourCubicDiscriminant
import Mathlib.Tactic

/-!
# No real branch point — the archimedean consequence of the sum of squares

Chip on `conj:hecke-monodromy-step-two`. The probe
`computations/probes/colour_cubic_branch_monodromy_probe.py` reports, as its fourth assertion,
*"its six roots are complex, none real"* — measured numerically at 40 dps. This file proves it:
by `QOU.Mass.ColourCubicDiscriminant.colourDiscriminant_sos`,
`D(z) = (4z³ + 3z² + 3z + 4)² + 2z²(z² + 1)`, and over `ℝ` both summands are non-negative with the
second strictly positive unless `z = 0`, where `D(0) = 16`. So `D` never vanishes on `ℝ`: every
branch point of the colour cubic is non-real, and the monodromy the conjecture speaks of is
genuinely a statement about loops in `ℂ ∖ Δ`, not about real intervals.

Archimedean (ordering on `ℝ`), hence its own file per §7c; the identity it rests on is generic.

-- Ref: [leitner2026] computations/probes/colour_cubic_branch_monodromy_probe.py
-/

namespace QOU.Mass.ColourCubicDiscriminantReal

open QOU.Mass.ColourCubicDiscriminant

/-- `D(z) > 0` for every real `z`. -/
theorem colourDiscriminant_pos (z : ℝ) : 0 < colourDiscriminant z := by
  rw [colourDiscriminant_sos]
  rcases eq_or_ne z 0 with hz | hz
  · subst hz; norm_num
  · have h1 : 0 ≤ (4 * z ^ 3 + 3 * z ^ 2 + 3 * z + 4) ^ 2 := sq_nonneg _
    have h2 : 0 < 2 * z ^ 2 * (z ^ 2 + 1) := by positivity
    linarith

/-- **No real branch point.** The discriminant of the colour cubic has no real root. -/
theorem no_real_branch_point (z : ℝ) : colourDiscriminant z ≠ 0 :=
  ne_of_gt (colourDiscriminant_pos z)

end QOU.Mass.ColourCubicDiscriminantReal
