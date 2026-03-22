/-!
# QOU.CategoricalReeb

The categorical Reeb derivation: the infinitesimal generator of the
torus action on the Frobenius–Hopf object `A`.

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/QuantumObservableUniverse.lean (monolithic)
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Reeb derivation**.

    The endomorphism `ξ : A → A` generating the `T`-action on the
    Frobenius–Hopf object `A`.  It is equipped with a canonical 1-form
    `θ_A` (the dual of `ξ`) satisfying:

    1. **Vertical generator**: `π_V ∘ d = ξ ⌟ dθ_A`
    2. **Normalisation**: `θ_A(ξ) = id_𝟙`
    3. **Kernel**: `Ω^k_H(A) = ker(ξ ⌟)`

    LaTeX: `\label{def:categorical-reeb}`
    Ref: [witten1988] https://doi.org/10.1007/BF01223371 -/
structure CategoricalReeb (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The Reeb derivation `ξ : A → A`. -/
  xi : A ⟶ A
  /-- The canonical 1-form `θ_A`, abstractly a morphism `A → 𝟙`
      dual to `ξ`. -/
  theta : A ⟶ (𝟙_ C)
  /-- Normalisation: `θ_A ∘ ξ` composed with the unit gives `id_𝟙`.
      This encodes `θ_A(ξ) = 1`. -/
  normalisation : xi ≫ theta = theta

end QOU
