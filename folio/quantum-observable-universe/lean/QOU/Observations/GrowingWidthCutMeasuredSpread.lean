import QOU.MassTheory.GrowingWidthCutShapeExclusion

/-!
# Growing-width cut: the measured spread (comparison layer)

This is where measurement meets the shape exclusion of
`QOU.MassTheory.GrowingWidthCutShapeExclusion`. That module is measurement-free. The
numbers below are inputs from the probe
`computations/meson/growing_width_cut_shape_exclusion_probe.py`, not values derived in
Lean:

* the rescalings the balanced cut `w = 3/2` would need span
  `rmin = 0.5130070` (²H) to `rmax = 2.3770636` (⁴He);
* the AME2020 per-nucleon binding peaks at ⁴He (7.0739 MeV) and dips at ⁶Li
  (5.3323 MeV), so the target is not non-decreasing.

The measured spread is `rmax / rmin ≈ 4.63 ≥ 4`, so
`constant_error_at_least_two_of_four_le` applies: every constant is off by at least a
factor of two somewhere. The probe's dense value is 2.1526×.
-/

namespace QOU.Observations.GrowingWidthCutMeasuredSpread

open QOU.MassTheory

/-- Measured lower end of the required-rescaling spread (²H), a probe input. -/
noncomputable def measuredRmin : ℝ := 5130070 / 10000000

/-- Measured upper end of the required-rescaling spread (⁴He), a probe input. -/
noncomputable def measuredRmax : ℝ := 23770636 / 10000000

/-- **Comparison.** At the measured spread, every positive constant misses by at least
a factor of two somewhere. -/
theorem measured_constant_error_at_least_two {c : ℝ} (hc : 0 < c) :
    (2 : ℝ) ≤ max (measuredRmax / c) (c / measuredRmin) :=
  constant_error_at_least_two_of_four_le (by unfold measuredRmin; norm_num)
    (by unfold measuredRmin measuredRmax; norm_num) hc

end QOU.Observations.GrowingWidthCutMeasuredSpread
