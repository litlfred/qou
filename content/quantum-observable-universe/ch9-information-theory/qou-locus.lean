/-!
# QOU.MotivicIntegration.QOULocus

The QOU locus M_QOU ⊂ M_QO: the definable sublocus where the QOU
axioms (observability, measurability, volume constraint) hold.

Axiom filtration: M_QO ⊃ M_obs ⊃ M_meas ⊃ M_QOU.
Each inclusion is a definable embedding; axiom independence
ensures they are strict.

LaTeX: `\label{def:qou-locus}`

## References

- [manuscript] §8/qou-locus
-/

import Mathlib.Data.Real.Basic

namespace QOU.MotivicIntegration

/-- The QOU locus: the sublocus of M_QO satisfying all QOU axioms.
    Observability: Hom(1, Ad(A)) = 0.
    Measurability: c₁ = c₂ = 0.
    Volume constraint: Λ²V ↠ 1. -/
-- Ref: [manuscript] §8/qou-locus
structure QOULocus where
  /-- Observability holds. -/
  observable : Prop
  /-- Measurability holds. -/
  measurable : Prop
  /-- Volume constraint holds. -/
  volume_constraint : Prop

end QOU.MotivicIntegration
