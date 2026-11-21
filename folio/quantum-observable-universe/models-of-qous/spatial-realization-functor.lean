import QOU.Basic
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic


/-!
# QOU.SpatialRealizationFunctor

The spatial realization of a Frobenius–Hopf object `A` is the space
`Spec(A) = { p : 𝟙 → A | p is a categorical point }`, equipped with
local germs, Kähler differentials, contact form, and Reeb derivation
derived within the monoidal category.  Under the fibre functor `τ`,
these algebraic structures map to their geometric counterparts on a
contact manifold.

LaTeX label: `def:spatial-realization-functor`

## References

- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [leitner2026] §1-quantum-observable-universe/spatial-realization-functor
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Spatial realization functor**.

    Given a quantum observable universe `(C, A, τ)`, the spatial realization
    `Spec(A)` is the collection of categorical points `p : 𝟙 → A`.  The
    fibre functor `τ : C → D` maps the algebraic structures on `A` —
    Kähler differentials `Ω¹(A)`, the Frobenius-induced contact form `θ_A`,
    and the Reeb derivation `ξ` — to their geometric counterparts on the
    manifold `M = τ(Spec(A))`.

    LaTeX: `\label{def:spatial-realization-functor}` -/
-- Ref: [kock2004], [leitner2026] §1
structure SpatialRealizationFunctor (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C] where
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : FrobeniusHopfData C
  /-- The object of Kähler differentials `Ω¹(A)` in `C`. -/
  differentials : C
  /-- The universal derivation `d : A → Ω¹(A)`. -/
  universalDeriv : frobHopf.obj ⟶ differentials
  /-- The contact form `θ_A ∈ Ω¹(A)`, induced by the Frobenius form. -/
  contactForm : (𝟙_ C) ⟶ differentials
  /-- The geometric target category. -/
  D : Type u
  [catD : Category.{v} D]
  /-- The fibre functor `τ : C → D`. -/
  fibreFunctor : C ⥤ D

end QOU
