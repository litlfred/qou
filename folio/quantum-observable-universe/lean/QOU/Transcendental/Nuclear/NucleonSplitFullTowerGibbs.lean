import QOU.Nuclear.NucleonSplitFullTower
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The Gibbs split on every tower level (archimedean)

Split off `QOU.Nuclear.NucleonSplitFullTower` at the transcendental boundary (bean `qou-gfsr`);
name and namespace unchanged. The `K`-weight forcing, tower-independence and spectator results
stay in that module over a generic field; only item 6, which uses `Real.log`, lives here.
-/

namespace QOU.Nuclear.NucleonSplitFullTower

/-- The Gibbs split on any tower level where `τ_p = q²·τ_n`. -/
theorem gibbs_split_full_tower {q E τn : ℝ} (hτ : 0 < τn) :
    E * Real.log (q ^ 2 * τn / τn) = 2 * E * Real.log q := by
  rw [mul_div_assoc, div_self hτ.ne', mul_one, Real.log_pow]; push_cast; ring

end QOU.Nuclear.NucleonSplitFullTower
