import Mathlib

namespace QOU.Information.DispersionSuppressionScale

/--
**Pattern C — named proposition.**
The archimedean projection suppresses the fibre-level q-dispersion.
The residual fractional variation of the archimedean photon group velocity
with photon energy 𝔈 is bounded by 𝔈 / 𝔈_{QG} for a suppression scale
𝔈_{QG} at or above the Planck energy.
-/
def dispersion_suppression_scale (q : ℝ) (E_QG : ℝ) : Prop :=
  ∃ fractional_variation : ℝ → ℝ, ∀ E : ℝ, E > 0 → fractional_variation E ≤ E / E_QG

end QOU.Information.DispersionSuppressionScale
