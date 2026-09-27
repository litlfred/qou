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
import Mathlib.Topology.ContinuousMap.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.InvolutiveStructure

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/InvolutiveStructure.lean (monolithic).
That file no longer exists — the library was split, and `InvolutiveStructure` now lives at
  folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Structures.lean
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Involutive structure** (†-structure / *-structure) on a monoidal category.

    A contravariant endofunctor `† : C^op → C` that is the identity on objects,
    satisfies `f†† = f`, and is compatible with the monoidal structure.

    LaTeX: `\label{def:involutive-structure}` -/
structure InvolutiveStructure (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The involution on morphisms: `f† : Y ⟶ X` for `f : X ⟶ Y`. -/
  dagger : ∀ {X Y : C}, (X ⟶ Y) → (Y ⟶ X)
  /-- Involutivity: `f†† = f`. -/
  dagger_dagger : ∀ {X Y : C} (f : X ⟶ Y), dagger (dagger f) = f
  /-- Contravariance: `(g ∘ f)† = f† ∘ g†`. -/
  dagger_comp : ∀ {X Y Z : C} (f : X ⟶ Y) (g : Y ⟶ Z),
    dagger (f ≫ g) = dagger g ≫ dagger f
  /-- Identity: `id† = id`. -/
  dagger_id : ∀ (X : C), dagger (𝟙 X) = 𝟙 X

/-- `f†† = f` is the defining involutivity property. -/
theorem InvolutiveStructure.involutivity {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    (inv : InvolutiveStructure C) {X Y : C} (f : X ⟶ Y) :
    inv.dagger (inv.dagger f) = f :=
  inv.dagger_dagger f

end QOU
