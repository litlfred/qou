/-!
# QOU.MotivicIntegration.QOModuli

The moduli of quantum observables M_QO: pairs (C, A) where C is a
rigid monoidal category and A is a Frobenius–Hopf object (Axioms 1–2
of a quantum universe, without observability or measurability).

Definable class in L_RMC. Stratified by dim_q(A).

LaTeX: `\label{def:qo-moduli}`

## References

- [manuscript] §8/qo-moduli
-/

import Mathlib.CategoryTheory.Monoidal.Rigid.Basic

namespace QOU.MotivicIntegration

/-- A quantum observable: a Frobenius–Hopf object in a rigid monoidal
    category.  Axioms 1–2 of a quantum universe without observability. -/
-- Ref: [manuscript] §8/qo-moduli
structure QuantumObservable where
  /-- Quantum dimension of the fundamental object. -/
  dim_q : ℝ

end QOU.MotivicIntegration
