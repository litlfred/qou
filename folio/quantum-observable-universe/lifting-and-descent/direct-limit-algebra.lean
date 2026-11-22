import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Module.LinearMap.Defs


/-!
# QOU.DirectLimitAlgebra — Direct limit of the endomorphism algebras

The direct limit 𝒜_∞ = colim End_𝒞(Aₙ) is the algebra of
observables at infinite brane level.

## References

- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

variable {R : Type*} [CommRing R]

/-- The direct limit algebra of a brane tower: the colimit of
    the sequence End_𝒞(A₀) → End_𝒞(A₁) → End_𝒞(A₂) → ⋯
    with connecting maps given by jet prolongation.

    LaTeX: `\label{def:direct-limit-algebra}` -/
-- Ref: [leitner2026] §3, Definition: Direct limit algebra
structure DirectLimitAlgebra (R : Type*) [CommRing R] where
  /-- The module at each level. -/
  levelMod : ℕ → Type*
  /-- Module instances. -/
  instAddCommGroup : ∀ n, AddCommGroup (levelMod n)
  instModule : ∀ n, Module R (levelMod n)
  /-- Connecting maps (from jet prolongation). -/
  connect : ∀ n, levelMod n →ₗ[R] levelMod (n + 1)
  /-- Connecting maps are injective (ascent is an embedding). -/
  connect_injective : ∀ n, Function.Injective (connect n)

attribute [instance] DirectLimitAlgebra.instAddCommGroup
attribute [instance] DirectLimitAlgebra.instModule

end QOU
