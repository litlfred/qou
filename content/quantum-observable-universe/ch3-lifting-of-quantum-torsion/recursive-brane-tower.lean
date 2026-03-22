/-!
# QOU.RecursiveBraneTower — The recursive brane tower {Aₙ}

Starting from A₀ = A, define A_{n+1} = J¹(Aₙ) recursively.
The tower A₀ ↪ A₁ ↪ A₂ ↪ ⋯ carries the ascent/descent structure.

## References

- [manuscript] §3 Lifting and Descent
-/

import Mathlib.Algebra.Module.Basic

namespace QOU

variable {R : Type*} [CommRing R]

/-- The recursive brane tower: a sequence of R-modules connected by
    ascent embeddings (jet prolongation) and descent retractions.

    LaTeX: `\label{def:recursive-brane-tower}` -/
-- Ref: [manuscript] §3, Definition: Recursive brane tower
structure RecursiveBraneTower (R : Type*) [CommRing R] where
  /-- The module at level n (representing End_𝒞(Aₙ)). -/
  level : ℕ → Type*
  /-- Each level is an R-module. -/
  addCommGroup : ∀ n, AddCommGroup (level n)
  module : ∀ n, Module R (level n)
  /-- Ascent: jet prolongation ℓₙ : level n → level (n+1). -/
  ascent : ∀ n, @LinearMap R R _ _ _ (level n) (level (n + 1))
    (addCommGroup n) (module n) (addCommGroup (n + 1)) (module (n + 1)) LinearMap.id.toModule
  /-- Descent: retraction 𝔡_{n+1} : level (n+1) → level n. -/
  descent : ∀ n, @LinearMap R R _ _ _ (level (n + 1)) (level n)
    (addCommGroup (n + 1)) (module (n + 1)) (addCommGroup n) (module n) LinearMap.id.toModule

end QOU
