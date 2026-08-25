/-
# Mathlib-gap infra: differentiability of `Real.sinc` (bean qou-shrp, step 1)

Mathlib defines `Real.sinc x = if x = 0 then 1 else sin x / x` and proves
`Real.continuous_sinc` and `Real.sinc_zero`, but carries **no**
differentiability or analyticity lemmas for it.  The `qou-shrp` route to
van der Veen's `½` needs `φ = log 2 + log(sinc)` to be `C¹` across `0`, so
those lemmas have to exist.  This file supplies them, sorry-free:

* `hasDerivAt_sinc_zero` — `sinc′(0) = 0` (the removable point);
* `hasDerivAt_sinc` — `sinc′(x) = (x·cos x − sin x)/x²` off `0`;
* `differentiable_sinc` — `sinc` is differentiable everywhere.

Nothing here is QOU-specific; it is stated in Mathlib style and is a
candidate for upstreaming.  Authored under the owner's standing
authorisation to add Mathlib infrastructure rather than route around a gap
("add mathlib infra if needed", 2026-08-11).

The derivative at `0` comes from the slope characterisation plus
`Real.sin_bound`: for `|y| ≤ 1`,

    |slope sinc 0 y| = |sin y − y| / y² ≤ |y|²·(5/96) + |y|/6  →  0,

using `|sin y − y| ≤ |sin y − (y − y³/6)| + |y|³/6`.
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Sinc
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv

namespace QOU.Knot

open Real Filter Topology

/-- Off the origin, `sinc` agrees with `sin x / x` on a neighbourhood. -/
theorem sinc_eventuallyEq {x : ℝ} (hx : x ≠ 0) :
    Real.sinc =ᶠ[𝓝 x] fun y => Real.sin y / y := by
  filter_upwards [isOpen_ne.mem_nhds hx] with y hy
  simp [Real.sinc, hy]

/-- **`sinc` is differentiable away from `0`**, with the quotient-rule
    derivative `(x·cos x − sin x)/x²`. -/
theorem hasDerivAt_sinc {x : ℝ} (hx : x ≠ 0) :
    HasDerivAt Real.sinc ((x * Real.cos x - Real.sin x) / x ^ 2) x := by
  have hquot : HasDerivAt (fun y => Real.sin y / y)
      ((Real.cos x * x - Real.sin x * 1) / x ^ 2) x :=
    (Real.hasDerivAt_sin x).div (hasDerivAt_id x) hx
  have hval : (Real.cos x * x - Real.sin x * 1) / x ^ 2
      = (x * Real.cos x - Real.sin x) / x ^ 2 := by ring
  rw [hval] at hquot
  exact hquot.congr_of_eventuallyEq (sinc_eventuallyEq hx)

/-- **`sinc` is differentiable at the removable point, with derivative `0`.**
    The slope is `(sin y − y)/y²`, which `Real.sin_bound` squeezes to `0`. -/
theorem hasDerivAt_sinc_zero : HasDerivAt Real.sinc 0 0 := by
  rw [hasDerivAt_iff_tendsto_slope]
  -- the comparison function |y|²·(5/96) + |y|/6 → 0
  have hg : Tendsto (fun y : ℝ => |y| ^ 2 * (5 / 96) + |y| / 6)
      (𝓝[≠] (0 : ℝ)) (𝓝 0) := by
    have hcont : Continuous fun y : ℝ => |y| ^ 2 * (5 / 96) + |y| / 6 := by
      fun_prop
    have := (hcont.tendsto 0).mono_left (nhdsWithin_le_nhds (s := {(0:ℝ)}ᶜ))
    simpa using this
  refine squeeze_zero_norm' ?_ hg
  filter_upwards [self_mem_nhdsWithin,
    mem_nhdsWithin_of_mem_nhds (Metric.closedBall_mem_nhds (0 : ℝ) one_pos)]
    with y hy0 hy1
  have hy : y ≠ 0 := hy0
  have hy1' : |y| ≤ 1 := by simpa [Real.closedBall_eq_Icc, abs_le] using hy1
  -- slope sinc 0 y = (sin y − y)/y²
  have hslope : slope Real.sinc 0 y = (Real.sin y - y) / y ^ 2 := by
    have h0 : Real.sinc 0 = 1 := Real.sinc_zero
    have hyv : Real.sinc y = Real.sin y / y := by simp [Real.sinc, hy]
    rw [slope_def_field, h0, hyv, sub_zero, div_sub_one hy, div_div, ← sq]
  rw [hslope, Real.norm_eq_abs, abs_div]
  -- |sin y − y| ≤ |y|⁴·(5/96) + |y|³/6
  have hb := Real.sin_bound hy1'
  have hnum : |Real.sin y - y| ≤ |y| ^ 4 * (5 / 96) + |y| ^ 3 / 6 := by
    have hsplit : Real.sin y - y
        = (Real.sin y - (y - y ^ 3 / 6)) + (-(y ^ 3) / 6) := by ring
    have habs3 : |(-(y ^ 3) / 6)| = |y| ^ 3 / 6 := by
      rw [abs_div, abs_neg, abs_pow]
      norm_num
    calc |Real.sin y - y|
        = |(Real.sin y - (y - y ^ 3 / 6)) + (-(y ^ 3) / 6)| := by rw [← hsplit]
      _ ≤ |Real.sin y - (y - y ^ 3 / 6)| + |(-(y ^ 3) / 6)| := abs_add_le _ _
      _ ≤ |y| ^ 4 * (5 / 96) + |y| ^ 3 / 6 := by rw [habs3]; linarith [hb]
  have hy2 : |y ^ 2| = |y| ^ 2 := by rw [abs_pow]
  have hy2pos : (0:ℝ) < |y| ^ 2 := by positivity
  rw [hy2, div_le_iff₀ hy2pos]
  calc |Real.sin y - y| ≤ |y| ^ 4 * (5 / 96) + |y| ^ 3 / 6 := hnum
    _ = (|y| ^ 2 * (5 / 96) + |y| / 6) * |y| ^ 2 := by ring

/-- **`sinc` is differentiable everywhere.** -/
theorem differentiable_sinc : Differentiable ℝ Real.sinc := by
  intro x
  rcases eq_or_ne x 0 with rfl | hx
  · exact hasDerivAt_sinc_zero.differentiableAt
  · exact (hasDerivAt_sinc hx).differentiableAt

end QOU.Knot
