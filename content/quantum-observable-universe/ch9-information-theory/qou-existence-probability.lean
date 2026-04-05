/-!
# QOU.MotivicIntegration.QOUExistenceProbability

The categorical probability of QOU existence:
  Prob_q(QOU) := μ_q(M_QOU) / μ_q(M_QO) ∈ K₀(C)[L_q⁻¹]

Factorises along the axiom filtration:
  Prob_q(QOU) = Prob_q(obs) · Prob_q(meas | obs) · Prob_q(vol | meas)

Each factor is the motivic codimension of the corresponding axiom.

LaTeX: `\label{def:qou-existence-probability}`

## References

- [denef2001] https://doi.org/10.1007/978-3-0348-8268-2_19
- [manuscript] §8/qou-existence-probability
-/

import Mathlib.Data.Real.Basic

namespace QOU.MotivicIntegration

/-- The categorical probability of QOU existence:
    ratio of motivic measures in K₀(C)[L_q⁻¹]. -/
-- Ref: [denef2001] https://doi.org/10.1007/978-3-0348-8268-2_19
structure ExistenceProbability where
  /-- Motivic measure of QOU locus. -/
  numerator : ℝ
  /-- Motivic measure of QO moduli. -/
  denominator : ℝ
  /-- Denominator is non-zero. -/
  denom_pos : denominator > 0

end QOU.MotivicIntegration
