import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic


/-!
# QOU.CategoricalDiracOperator

The q-deformed covariant derivative D_∇ = q⁻¹∇ + (1 - q⁻¹)ι_ξ∇,
serving as the categorical Dirac operator.

LaTeX: `\label{def:categorical-dirac-operator}`
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Dirac operator** `𝒟_∇ = q⁻¹∇ + (1 - q⁻¹)ι_ξ∇`.

    The q-deformed covariant derivative on a quantum observable universe.
    When q = 1, this reduces to the undeformed connection ∇.

    Ref: [manuscript] §1-quantum-observable-universe -/
-- Ref: [manuscript] §1-quantum-observable-universe
structure CategoricalDiracOperator (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The underlying connection. -/
  connection : CategoricalConnection C fh
  /-- The substrate parameter q. -/
  q : (𝟙_ C) ⟶ (𝟙_ C)
  /-- The Reeb derivation ξ. -/
  reeb : fh.obj ⟶ fh.obj
  /-- The Dirac morphism 𝒟_∇ : A → Ω¹(A). -/
  dirac : fh.obj ⟶ fh.obj

end QOU
