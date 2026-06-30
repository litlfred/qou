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
# QOU.SpinLabels

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/SpinLabels.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Spin labels**: the simple objects of a quantum observable universe
    are indexed by half-integer spin labels `j ∈ {0, 1/2, 1, 3/2, ...}`,
    with `V_j` having categorical dimension `2j + 1`.

    By the SU(2) emergence theorem (`thm:su2-emergence`), the gauge group
    of any QOU is `SU(2)`, whose irreducible representations are exactly
    the spin-`j` representations `V_j` with `dim V_j = 2j + 1`.

    LaTeX: `\label{prop:spin-labels}` -/
structure SpinLabels where
  /-- The spin label `j`, represented as twice the spin (so `j = 0, 1, 2, 3, ...`
      corresponds to spin `0, 1/2, 1, 3/2, ...`). -/
  twice_j : ℕ
  /-- The categorical dimension of `V_j` is `2j + 1 = twice_j + 1`. -/
  cat_dim : ℕ := twice_j + 1

/-- **Spin decomposition** in a QOU: the simple objects of `C` are
    indexed by `SpinLabels`, and the fundamental object has spin `1/2`.

    This connects `SpinLabels` to the categorical framework: given a QOU,
    the SU(2) emergence theorem forces the simple objects to be exactly
    the spin-`j` representations.  The fundamental object `V` from the
    QOU has `j = 1/2` (categorical dimension 2). -/
structure SpinDecomposition (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The simple object in `C` at spin label `j`. -/
  simpleObj : SpinLabels → C
  /-- The fundamental object `V` corresponds to spin `1/2`. -/
  fundamentalObj : C
  /-- `V = V_{1/2}` (the spin-1/2 representation). -/
  fundamental_is_half : fundamentalObj = simpleObj ⟨1⟩
  /-- The adjoint object `Ad(A)` corresponds to spin `1`. -/
  adjointObj : C
  /-- `Ad(A) = V_1` (the spin-1 representation). -/
  adjoint_is_one : adjointObj = simpleObj ⟨2⟩

/-- The fundamental object has spin `1/2` and dimension `2`. -/
theorem SpinLabels.fundamental_dim : (SpinLabels.mk 1).cat_dim = 2 := rfl

/-- The adjoint object has spin `1` and dimension `3`. -/
theorem SpinLabels.adjoint_dim : (SpinLabels.mk 2).cat_dim = 3 := rfl

/-- The trivial object has spin `0` and dimension `1`. -/
theorem SpinLabels.trivial_dim : (SpinLabels.mk 0).cat_dim = 1 := rfl

end QOU
