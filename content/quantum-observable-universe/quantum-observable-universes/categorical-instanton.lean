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
# QOU.CategoricalInstanton

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/CategoricalInstanton.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Categorical instanton**: a connection whose curvature is self-dual
    with respect to the q-Hodge star `⋆_q`.

    `⋆_q F_∇ = F_∇`, equivalently `F_∇` lies in the `+1`-eigenspace
    `Ω⁺(A)` of the Hodge involution.

    LaTeX: `\label{def:categorical-instanton}` -/
structure CategoricalInstanton {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _) where
  /-- The connection morphism `∇ : A → A ⊗ Ω¹(A)` (represented as endo). -/
  connection : fh.obj ⟶ fh.obj
  /-- The curvature `F_∇ = ∇² : A → Ω²(A)` (represented as endo). -/
  curvature : fh.obj ⟶ fh.obj
  /-- The q-Hodge star involution on `Ω²(A)`. -/
  hodge : CatHodgeInvolution fh.obj
  /-- **Self-duality**: `⋆_q(F_∇) = F_∇`. -/
  self_dual : hodge.IsSelfDual curvature

end QOU
