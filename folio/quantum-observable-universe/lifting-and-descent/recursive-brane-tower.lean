import Mathlib.Algebra.Module.Basic
import Mathlib.LinearAlgebra.Span.Basic


/-!
# QOU.RecursiveBraneTower — The recursive brane tower {Aₙ}

Starting from A₀ = A, define A_{n+1} = J¹(Aₙ) recursively.
The tower A₀ ↪ A₁ ↪ A₂ ↪ ⋯ carries the ascent/descent structure.

## References

- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

/-- The recursive brane tower: a sequence of R-modules connected by
    ascent embeddings (jet prolongation) and descent retractions.

    Starting from A₀ = A, the tower is defined by A_{n+1} = J¹(Aₙ).
    The ascent maps are the canonical inclusions Aₙ ↪ J¹(Aₙ) via the
    unit section, and the descent maps are the retractions.

    LaTeX: `\label{def:recursive-brane-tower}` -/
-- Ref: [leitner2026] §3, Definition: Recursive brane tower
structure RecursiveBraneTower (R : Type*) [CommRing R] where
  /-- The module at level n (representing End_𝒞(Aₙ)). -/
  level : ℕ → Type*
  /-- Each level carries an R-module structure. -/
  instAddCommGroup : ∀ n, AddCommGroup (level n)
  instModule : ∀ n, Module R (level n)
  /-- Ascent: jet prolongation ℓₙ : level n → level (n+1).
      An R-linear embedding (the unit section of the jet bundle). -/
  ascent : ∀ n, level n →ₗ[R] level (n + 1)
  /-- Descent: retraction 𝔡_{n+1} : level (n+1) → level n.
      An R-linear map (projection from jet bundle to base). -/
  descent : ∀ n, level (n + 1) →ₗ[R] level n
  /-- The descent is a left inverse of the ascent: 𝔡 ∘ ℓ = id. -/
  retraction : ∀ n, (descent n).comp (ascent n) = LinearMap.id

attribute [instance] RecursiveBraneTower.instAddCommGroup
attribute [instance] RecursiveBraneTower.instModule

end QOU
