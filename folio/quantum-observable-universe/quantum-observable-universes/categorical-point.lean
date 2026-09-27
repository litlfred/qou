import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.CategoricalPoint

A categorical point of a Frobenius–Hopf object `A` is a morphism
`p : 𝟙 → A` in the monoidal category `C`.

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse.lean (monolithic)
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Categorical point** of a Frobenius–Hopf object.

    A morphism `p : 𝟙 → A` in a monoidal category `C`.  In the archimedean
    realisation `A = 𝒪(G)`, a point corresponds to evaluation at `g ∈ G`;
    for `A = C^∞(M)`, to a point of the manifold `M`.

    The augmentation ideal at `p` is `𝔪_p = ker(p* : A → 𝟙)`.

    LaTeX: `\label{def:categorical-point}`
    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
structure CategoricalPoint (C : Type u) [Category.{v} C]
    [MonoidalCategory C] (A : C) where
  /-- The point morphism `p : 𝟙 → A`. -/
  point : (𝟙_ C) ⟶ A

end QOU
