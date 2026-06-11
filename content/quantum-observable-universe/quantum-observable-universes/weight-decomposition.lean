import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.WeightDecomposition

The `T`-weight decomposition of differential forms `Ω^k(A)` into
horizontal (weight-0) and vertical (non-zero weight) components.

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse.lean (monolithic)
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Weight decomposition** of differential forms.

    Given a torus action on `Ω^k(A)`, every form `α` decomposes uniquely
    as `α = α_H + α_V` where `α_H = π_H(α)` is the horizontal (weight-0)
    component and `α_V = π_V(α)` is the vertical (non-zero weight) component.

    The projections `π_H` and `π_V` are idempotent and complementary:
    `π_H + π_V = id`, `π_H ∘ π_H = π_H`, `π_V ∘ π_V = π_V`.

    LaTeX: `\label{def:weight-decomposition}`
    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
structure WeightDecomposition (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] where
  /-- The object of `k`-forms `Ω^k(A)` in `C`. -/
  forms : C
  /-- The horizontal projection `π_H : Ω^k(A) → Ω^k(A)` (weight-0). -/
  proj_H : forms ⟶ forms
  /-- The vertical projection `π_V : Ω^k(A) → Ω^k(A)` (non-zero weight). -/
  proj_V : forms ⟶ forms
  /-- Complementarity: `π_H + π_V = id`. -/
  complementary : proj_H + proj_V = 𝟙 forms
  /-- Idempotency of horizontal projection: `π_H ∘ π_H = π_H`. -/
  proj_H_idem : proj_H ≫ proj_H = proj_H
  /-- Idempotency of vertical projection: `π_V ∘ π_V = π_V`. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V

end QOU
