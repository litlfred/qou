/-!
# QOU.QTorsionLeaf

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/QTorsionLeaf.lean (monolithic)
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

/-- **q-Torsion leaf**: a maximal integral submanifold `L ↪ M` of `H`
    that is invariant under the q-deformed Reeb flow.

    LaTeX: `\label{def:q-torsion-leaf}` -/
structure QTorsionLeaf (M : Type*) where
  /-- The leaf as a subset of `M`. -/
  leaf : Set M
  /-- The leaf is non-empty. -/
  nonempty : leaf.Nonempty
  /-- Tangent inclusion: `T_p L ⊂ H_p` for all `p ∈ L`
      (integrality of the horizontal distribution). -/
  /-- A "tangent test" function: for each `p ∈ L`, the horizontal
      component dominates (formalises `T_p L ⊂ H_p`).  Concretely,
      for any Reeb decomposition with the leaf as support, the vertical
      component vanishes on the leaf. -/
  tangent_in_horizontal : ∀ (rd : ReebDecomposition M),
    (∀ p, p ∈ leaf → rd.vertical p = 0)
  /-- Flow invariance: `φ^q_t(L) = L` for all `t ∈ ℝ`. -/
  flow_invariant : ∀ (qrf : QReebFlow M) (t : ℝ),
    ∀ (p : M), p ∈ leaf → qrf.flow t p ∈ leaf

end QOU
