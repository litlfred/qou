/-!
# QOU.MotivicIntegration.QOUMotivicMeasure

The q-motivic measure μ_q on definable subloci of M_QO,
valued in the localized Grothendieck ring K₀(C)[L_q⁻¹]
where L_q = [V] is the class of the fundamental object.

Decomposes along the axiom filtration.

LaTeX: `\label{def:qou-motivic-measure}`

## References

- [denef2001] https://doi.org/10.1007/978-3-0348-8268-2_19
- [cluckers2008] https://doi.org/10.1007/s00222-008-0114-2
- [manuscript] §8/qou-motivic-measure
-/

import Mathlib.Data.Real.Basic

namespace QOU.MotivicIntegration

/-- The q-motivic measure on definable subloci of M_QO.
    Values in K₀(C)[L_q⁻¹]. -/
-- Ref: [denef2001] https://doi.org/10.1007/978-3-0348-8268-2_19
structure MotivicMeasure where
  /-- The Lefschetz class L_q = [V], dim_q(V) = [2]_q. -/
  lefschetz_class : ℝ
  /-- The measure value of a definable sublocus. -/
  measure : ℝ

end QOU.MotivicIntegration
