/-!
# QOU.Basic — Shared Foundations

Common imports, notation, and base structures used throughout the
Quantum Observable Universe formalization.
-/

import Mathlib.Topology.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Functor.Basic

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
