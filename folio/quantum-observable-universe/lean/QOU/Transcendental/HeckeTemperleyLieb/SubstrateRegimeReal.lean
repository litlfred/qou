import HeckeTemperleyLieb.SubstrateRegime
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# Substrate regime: the golden ratio as `(1 + √5)/2` (Transcendental companion)

Split from `HeckeTemperleyLieb.SubstrateRegime` (bean `qou-dk7p`). That module states the
regime `1 < q < φ` for a symbol `φ`; this file supplies `φ = (1 + Real.sqrt 5)/2` and checks
`φ² = φ + 1`, so `one_lt_of_sq_eq_add_one` applies. Original names kept.
-/

namespace QOU.MathlibExt

/-- The golden ratio `(1 + √5)/2` at `ℝ`. -/
noncomputable def goldenRatio : ℝ := (1 + Real.sqrt 5) / 2

theorem goldenRatio_sq : goldenRatio ^ 2 = goldenRatio + 1 := by
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  unfold goldenRatio
  field_simp
  nlinarith [h5]

theorem one_lt_goldenRatio : 1 < goldenRatio :=
  one_lt_of_sq_eq_add_one (by unfold goldenRatio; positivity) goldenRatio_sq

end QOU.MathlibExt
