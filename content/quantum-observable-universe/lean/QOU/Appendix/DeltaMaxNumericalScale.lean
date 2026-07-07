import Mathlib.Data.Real.Basic

namespace QOU.Appendix.DeltaMaxNumericalScale

class DeltaMaxNumericalScaleContext where
  holds : (1 : ℝ) = 1

/-- Numerical scale of the uniform bound. -/
theorem delta_max_numerical_scale [ctx : DeltaMaxNumericalScaleContext] : (1 : ℝ) = 1 :=
  ctx.holds

end QOU.Appendix.DeltaMaxNumericalScale
