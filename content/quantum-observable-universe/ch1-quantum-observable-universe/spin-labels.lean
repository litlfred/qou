/-!
# QOU.SpinLabels

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/SpinLabels.lean (monolithic)
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

/-- **Spin labels**: the simple objects of a quantum observable universe
    are indexed by half-integer spin labels `j ∈ {0, 1/2, 1, 3/2, ...}`,
    with `V_j` having categorical dimension `2j + 1`.

    LaTeX: `\label{def:spin-labels}` -/
structure SpinLabels where
  /-- The spin label `j`, represented as twice the spin (so `j = 0, 1, 2, 3, ...`
      corresponds to spin `0, 1/2, 1, 3/2, ...`). -/
  twice_j : ℕ
  /-- The categorical dimension of `V_j` is `2j + 1 = twice_j + 1`. -/
  cat_dim : ℕ := twice_j + 1
  /-- The fundamental object has `j = 1/2` (twice_j = 1), dimension 2. -/

/-- The fundamental object has spin `1/2` and dimension `2`. -/
theorem SpinLabels.fundamental_dim : (SpinLabels.mk 1).cat_dim = 2 := by rfl

/-- The adjoint object has spin `1` and dimension `3`. -/
theorem SpinLabels.adjoint_dim : (SpinLabels.mk 2).cat_dim = 3 := by rfl

end QOU
