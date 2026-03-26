/-!
# QOU.ReebDecomposition

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/ReebDecomposition.lean (monolithic)
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

/-- **Reeb decomposition** of a differential form on a CR manifold.

    Every `k`-form `α` decomposes as `α = α_H + θ ∧ ι_ξ α` where
    `α_H` is the horizontal component and `θ ∧ ι_ξ α` is the vertical
    component.

    LaTeX: `\label{def:reeb-decomposition}` -/
structure ReebDecomposition (M : Type*) where
  /-- The total form (abstract representative). -/
  total : M → ℝ
  /-- Horizontal component `α_H` satisfying `ι_ξ α_H = 0`. -/
  horizontal : M → ℝ
  /-- Vertical component `α_V = θ ∧ ι_ξ α`. -/
  vertical : M → ℝ
  /-- Decomposition identity: `total = horizontal + vertical`. -/
  decomp : ∀ (p : M), total p = horizontal p + vertical p

/-- A form is **purely horizontal** iff its vertical component vanishes. -/
def ReebDecomposition.isPurelyHorizontal {M : Type*}
    (rd : ReebDecomposition M) : Prop :=
  ∀ (p : M), rd.vertical p = 0

end QOU
