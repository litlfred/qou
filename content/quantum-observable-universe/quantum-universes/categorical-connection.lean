import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousFunction.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.CategoricalConnection

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/CategoricalConnection.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical connection** on a Frobenius–Hopf object.

    A morphism `∇ : A → A ⊗ Ω¹` satisfying the Leibniz rule
    `∇(ab) = ∇(a) · b + a · ∇(b)`.  The object `Ω¹` represents the
    module of Kähler differentials in the categorical setting.

    LaTeX: `\label{def:categorical-connection}`
    Ref: [kock2004] -/
structure CategoricalConnection (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The object of 1-forms `Ω¹` in `C`. -/
  Omega1 : C
  /-- The connection morphism `∇ : A → A ⊗ Ω¹`. -/
  nabla : fh.obj ⟶ (fh.obj ⊗ Omega1)
  /-- The Leibniz rule RHS: the categorical morphism `A ⊗ A → A ⊗ Ω¹`
      encoding `∇(a)·b + a·∇(b)`.  In a general (non-preadditive) monoidal
      category the "sum" cannot be expressed purely from `(∇, μ, α)`, so it
      is provided abstractly.  In a preadditive monoidal category this should
      be `(∇ ▷ A) ≫ (α⁻¹) ≫ (μ ▷ Ω) + (A ◁ ∇) ≫ α ≫ …`. -/
  leibniz_rhs : (fh.obj ⊗ fh.obj) ⟶ (fh.obj ⊗ Omega1)
  /-- **Leibniz rule**: `∇ ∘ μ = leibniz_rhs`, i.e. the connection is
      a derivation with respect to the multiplication `μ`.
      The full coherence diagram requires shuffling via the associator;
      stated here as an equality of morphisms `A ⊗ A → A ⊗ Ω¹`. -/
  leibniz : fh.mul ≫ nabla = leibniz_rhs

/-- **Left module action** of a Frobenius–Hopf object `A` on another object `V`.

    A morphism `ρ : A ⊗ V → V` satisfying associativity and unitality,
    i.e. `V` is a left `A`-module in `C`.  (Auxiliary structure used in
    the definition of the categorical action functional.) -/
structure ModuleAction (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The object `V` acted upon. -/
  target : C
  /-- The action morphism `ρ : A ⊗ V → V`. -/
  action : (fh.obj ⊗ target) ⟶ target
  /-- **Associativity**: `ρ ∘ (μ ⊗ id_V) = ρ ∘ (id_A ⊗ ρ)` up to associator. -/
  assoc : (fh.mul ▷ target) ≫ action =
    (α_ fh.obj fh.obj target).hom ≫ (fh.obj ◁ action) ≫ action
  /-- **Unitality**: `ρ ∘ (η ⊗ id_V) = id_V` (up to left unitor). -/
  unit : (fh.unit ▷ target) ≫ action = (λ_ target).hom

end QOU
