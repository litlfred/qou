import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousMap.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Module.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic

/-!
# QOU.Basic — Shared Foundations

Common imports, notation, and base structures used throughout the
Quantum Observable Universe formalization.
-/


open scoped Topology Manifold

/-! ## Core structures -/

/-- A quantum observable universe configuration. -/
structure QOUConfig where
  /-- The underlying topological space. -/
  carrier : Type*
  [topSpace : TopologicalSpace carrier]
  /-- Dimension of the manifold. -/
  dim : ℕ

/-- Formalization status marker — used only in comments/docstrings.
    Actual status tracked in `proof-objects.json`. -/
inductive FormalizationStatus where
  | notStarted
  | stated
  | hasSorry
  | proved
  | mathlibOk
