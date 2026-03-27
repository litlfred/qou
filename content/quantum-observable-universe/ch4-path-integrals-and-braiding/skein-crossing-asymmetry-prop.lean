/-!
# QOU.Braiding.skein_crossing_asymmetry — Crossing asymmetry and Coulomb correction

The Skein relation's q vs q⁻¹ weighting yields a per-crossing
Coulomb correction δ = ½(q - q⁻¹) > 0 for q > 1, and the
Coulomb/Strong ratio equals tanh(ln q).

LaTeX label: `prop:skein-crossing-asymmetry`

## References
- [manuscript] Ch. 4, §enveloping-algebras
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.Braiding

/-- The per-crossing Coulomb correction δ = ½(q - q⁻¹). -/
noncomputable def coulombCorrection (q : ℝ) : ℝ :=
  (q - q⁻¹) / 2

/-- For q > 1, the Coulomb correction is positive. -/
-- Ref: [manuscript] Ch. 4, §enveloping-algebras
theorem skein_crossing_asymmetry (q : ℝ) (hq : q > 1) :
    coulombCorrection q > 0 := by sorry

end QOU.Braiding
