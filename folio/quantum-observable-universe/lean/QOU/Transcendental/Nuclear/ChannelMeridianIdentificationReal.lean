/-
  Archimedean specialisation of `QOU.Nuclear.ChannelMeridianIdentification` §3:
  the meridian period is `P = 2π`, the non-analytic `exp` label of the winding's
  root of unity (owner ruling 2026-11-27).  Same namespace; original names kept.
-/
import QOU.Nuclear.ChannelMeridianIdentification
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.QBeta.ChannelMeridianIdentification

open QOU.Knot.DeformedMeridianWinding

/-- **Boost dominance kills the winding.**  The meridian's imaginary part is
`−2πk`, so `Im²u = 4π²k²`.  If the anchor is boost-dominated — `ϑ² < t²`, the
`S > 0` branch of `s_channel_sign_pos` — and the substrate scale is subarchimedean
in the sense `|t| < 2π` (amply true at `t = ln q₀ ≈ 0.104`), then `k = 0`.

There is no room here: the smallest nonzero winding already contributes
`2π ≈ 6.28`, some sixty times `ln q₀`. -/
theorem winding_eq_zero_of_boost_dominated {N k : ℕ} {t : ℝ}
    (ht : |t| < 2 * Real.pi)
    (hboost : (meridian ((N : ℝ) * t) k).im ^ 2 < t ^ 2) :
    k = 0 := by
  rw [meridian_im] at hboost
  refine winding_eq_zero_of_lt_period (P := 2 * Real.pi) (by positivity) ht ?_
  have : (-(2 * Real.pi * (k : ℝ))) ^ 2 = (2 * Real.pi * (k : ℝ)) ^ 2 := by ring
  linarith

/-- **The identification collapses a boost-dominated anchor to `ϑ = 0`.**
Combining §2 and §3: the colour is degenerate AND the angular deformation
vanishes identically. -/
theorem color_one_and_theta_zero {N k : ℕ} {t : ℝ}
    (ht0 : t ≠ 0) (htpi : |t| < 2 * Real.pi)
    (hRe : (meridian ((N : ℝ) * t) k).re = t)
    (hboost : (meridian ((N : ℝ) * t) k).im ^ 2 < t ^ 2) :
    N = 1 ∧ (meridian ((N : ℝ) * t) k).im = 0 := by
  refine ⟨color_eq_one_of_re_eq_log ht0 hRe, ?_⟩
  rw [meridian_im, winding_eq_zero_of_boost_dominated htpi hboost]
  norm_num

end QOU.QBeta.ChannelMeridianIdentification
