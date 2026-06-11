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
# QOU.CatHodgeInvolution

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/CatHodgeInvolution.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- An **involutive endomorphism** in a category, modeling the Hodge star
    operator `⋆`.  When `⋆² = id`, the eigenvalue decomposition
    `V = V⁺ ⊕ V⁻` (self-dual ⊕ anti-self-dual) follows from the spectral
    theory of involutions.  This is the most general setting: works over any
    field, in any category with an identity. -/
structure CatHodgeInvolution {C : Type u} [CategoryTheory.Category.{v} C]
    (X : C) where
  /-- The Hodge star operator `⋆ : X ⟶ X`. -/
  star : X ⟶ X
  /-- Involutivity: `⋆ ≫ ⋆ = id_X`. -/
  star_sq : star ≫ star = 𝟙 X

/-- A morphism `f : Y ⟶ X` is **self-dual** w.r.t. a categorical Hodge
    involution if `f ≫ ⋆ = f`, i.e. `f` lands in the `+1`-eigenspace. -/
def CatHodgeInvolution.IsSelfDual {C : Type u} [CategoryTheory.Category.{v} C]
    {X : C} (h : CatHodgeInvolution X) {Y : C} (f : Y ⟶ X) : Prop :=
  f ≫ h.star = f

/-- An **involution on a type** (concrete version for the ℂ realisation).
    Models the Hodge star acting pointwise on sections of a bundle. -/
structure HodgeInvolution (V : Type*) where
  /-- The Hodge star `⋆ : V → V`. -/
  star : V → V
  /-- Involutivity: `⋆(⋆(v)) = v` for all `v`. -/
  star_sq : ∀ v, star (star v) = v

/-- An element `v : V` is **self-dual** if `⋆(v) = v`. -/
def HodgeInvolution.IsSelfDual {V : Type*} (h : HodgeInvolution V)
    (v : V) : Prop :=
  h.star v = v

/-- An element `v : V` is **anti-self-dual** if `⋆(v) = -v`. -/
def HodgeInvolution.IsAntiSelfDual {V : Type*} [Neg V]
    (h : HodgeInvolution V) (v : V) : Prop :=
  h.star v = -v

end QOU
