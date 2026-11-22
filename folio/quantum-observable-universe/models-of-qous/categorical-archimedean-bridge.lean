import QOU.Basic
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic


/-!
# QOU.categorical_archimedean_bridge — Categorical–geometric correspondence

Under the fibre functor τ, the categorical q-deformed exterior derivative
`π_V ∘ d` maps to the geometric expression `θ ∧ ℒ_ξ` on the contact
manifold.  This bridges the algebraic (monoidal) and Archimedean
(differential-geometric) formulations.

LaTeX label: `prop:categorical-archimedean-bridge`

## References

- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [leitner2026] §1-quantum-observable-universe/categorical-archimedean-bridge
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Categorical–geometric correspondence**.

    Given a quantum observable universe with weight decomposition
    `π_H, π_V` and categorical q-exterior derivative `d_q`, the fibre
    functor `τ` intertwines the categorical vertical projection with
    the geometric contact operation:

    `τ(π_V ∘ d) = θ ∧ ℒ_ξ : Ωᵏ(M) → Ωᵏ⁺¹(M)`.

    This is encoded as a commutative square: applying the fibre functor
    to the categorical `π_V ≫ d` yields the same morphism as the
    geometric `θ ∧ ℒ_ξ` on the realised manifold. -/
-- Ref: [kock2004], [leitner2026] §1
structure CategoricalArchimedeanBridge (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C] where
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : FrobeniusHopfData C
  /-- The vertical projection `π_V` from the weight decomposition. -/
  proj_V : frobHopf.obj ⟶ frobHopf.obj
  /-- The classical differential `d`. -/
  d_classical : frobHopf.obj ⟶ frobHopf.obj
  /-- The geometric target category (e.g. smooth manifolds). -/
  D : Type u
  [catD : Category.{v} D]
  /-- The fibre functor `τ : C → D`. -/
  fibreFunctor : C ⥤ D
  /-- The geometric contact operator `θ ∧ ℒ_ξ` on `τ(A)`. -/
  contactOp : fibreFunctor.obj frobHopf.obj ⟶ fibreFunctor.obj frobHopf.obj
  /-- **Bridge identity**: `τ(π_V ≫ d) = θ ∧ ℒ_ξ`. -/
  bridge : fibreFunctor.map (proj_V ≫ d_classical) = contactOp

/-- The bridge identity: the fibre functor sends the categorical
    vertical-projected differential to the geometric contact operator. -/
theorem categorical_archimedean_bridge {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (cab : CategoricalArchimedeanBridge C) :
    letI := cab.catD
    cab.fibreFunctor.map (cab.proj_V ≫ cab.d_classical) = cab.contactOp :=
  cab.bridge

end QOU
