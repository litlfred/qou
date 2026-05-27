import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic


/-!
# QOU.CategoricalLagrangian

The categorical Lagrangian ℒ_q(∇, ψ) = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ,
an endomorphism of A encoding the full physics before tracing.

LaTeX: `\label{def:categorical-lagrangian}`
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Lagrangian** `ℒ_q = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`.

    The endomorphism of A whose categorical trace yields the
    categorical action.  The first summand (𝒟²) encodes the bosonic
    sector (gravity + gauge); the second encodes fermionic coupling.

    Ref: [manuscript] §1-quantum-observable-universe -/
-- Ref: [manuscript] §1-quantum-observable-universe
structure CategoricalLagrangian (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The Dirac operator. -/
  dirac : CategoricalDiracOperator C fh
  /-- The state ψ : 𝟙 → A. -/
  state : (𝟙_ C) ⟶ fh.obj
  /-- The Lagrangian endomorphism ℒ_q ∈ End(A). -/
  lagrangian : fh.obj ⟶ fh.obj

end QOU
