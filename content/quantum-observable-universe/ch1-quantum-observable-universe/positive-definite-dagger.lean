/-!
# QOU.PositiveDefiniteStructure

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/PositiveDefiniteStructure.lean (monolithic)
-/

import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic
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

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Positive-definite structure** on an involutive monoidal category.

    The involution is positive-definite if for every non-zero
    `f : 𝟙 → X`, the composite `f ≫ f† : 𝟙 → 𝟙` is positive
    in `End(𝟙) ≅ R`.

    LaTeX: `\label{def:positive-definite-dagger}` -/
structure PositiveDefiniteStructure (C : Type u)
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    extends InvolutiveStructure C where
  /-- Positive-definiteness: for non-zero `f : 𝟙 → X`, `f ≫ f† ≠ 0`.
      (In an ℝ-linear category, this encodes positivity.) -/
  positive_definite : ∀ {X : C} (f : (𝟙_ C) ⟶ X),
    f ≠ 0 → f ≫ dagger f ≠ 0

end QOU
