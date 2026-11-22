import QOU.QuantumObservableUniverses.QDifferentialGeometry
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.CategoricalLagrangian.unique — uniqueness of the categorical Lagrangian

Given `(∇, ψ, ψ*)`, `𝓛_q` is uniquely determined by its defining formula:
the `lagrangian_formula` field forces the endomorphism, so two Lagrangians
sharing the Dirac operator, state, and costate coincide.

LaTeX: `\label{prop:categorical-lagrangian-unique}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-lagrangian-unique
- [connes1994] Noncommutative Geometry
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Uniqueness of the categorical Lagrangian.**

    Given fixed Dirac operator, state, and costate, the Lagrangian
    `𝒟_∇² + ψ* ⊗ 𝒟_∇ψ` is uniquely determined: the `lagrangian` morphism is
    forced by [`def:categorical-lagrangian`]'s `lagrangian_formula`, so two
    such Lagrangians are equal.

    This replaces the earlier `axiom … : Subsingleton (CategoricalLagrangian …)`,
    which was **false** (the structure has free fields).  Uniqueness holds only
    conditionally on shared data — exactly the narrative claim. -/
-- Ref: [connes1994]
theorem CategoricalLagrangian.unique
    {R : Type*} [CommRing R]
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C)
    (L₁ L₂ : CategoricalLagrangian R C fh)
    (hdirac : L₁.dirac = L₂.dirac)
    (hstate : L₁.state = L₂.state) (hcostate : L₁.costate = L₂.costate) :
    L₁ = L₂ := by
  obtain ⟨d₁, s₁, cs₁, l₁, hf₁⟩ := L₁
  obtain ⟨d₂, s₂, cs₂, l₂, hf₂⟩ := L₂
  simp only at hdirac hstate hcostate
  subst hdirac hstate hcostate
  -- `lagrangian` is forced by the formula from the (now shared) data.
  have hl : l₁ = l₂ := hf₁.trans hf₂.symm
  subst hl
  rfl

end QOU
