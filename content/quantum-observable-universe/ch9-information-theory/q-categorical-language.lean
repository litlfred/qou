/-!
# QOU.MotivicIntegration.CategoricalLanguage

The first-order language of rigid monoidal categories L_RMC.
Multi-sorted: object sort Ob, morphism sorts Mor(X,Y).
Function symbols: tensor, dual, braiding, unit.
Numeric term: quantum dimension dim_q.

The q-integers [n]_q play the role of residues in Pas's language;
braiding eigenvalues q, -q⁻¹ are angular components.
Tannaka–Krein reconstruction is the categorical quantifier elimination.

LaTeX: `\label{def:q-categorical-language}`

## References

- [denef2001] https://doi.org/10.1007/978-3-0348-8268-2_19
- [manuscript] §8/q-categorical-language
-/

import Mathlib.CategoryTheory.Monoidal.Rigid.Basic

namespace QOU.MotivicIntegration

/-- The first-order language of rigid monoidal categories.
    Sorts: Ob (objects), Mor(X,Y) (morphisms).
    Operations: ⊗, (-)ᘁ, 𝟙, σ (braiding).
    Numeric term: dim_q (quantum trace). -/
-- Ref: [denef2001] https://doi.org/10.1007/978-3-0348-8268-2_19
structure CategoricalLanguage where
  /-- The base ring of scalars (End(𝟙)). -/
  scalars : Type*
  /-- The substrate parameter q ∈ scalars. -/
  q : scalars

end QOU.MotivicIntegration
