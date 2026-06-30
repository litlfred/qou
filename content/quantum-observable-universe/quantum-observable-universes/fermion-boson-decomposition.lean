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
# QOU.Fermion

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/Fermion.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Fermion**: a q-harmonic form with non-trivial vertical component.

    LaTeX: `\label{def:fermion}` -/
structure Fermion (M : Type*) extends QHarmonicForm M where
  /-- The vertical component is non-trivial: `ι_ξ α_V ≠ 0`. -/
  vertical_nontrivial : ∃ (p : M), vertical p ≠ 0

/-- **Boson**: a q-harmonic form that is purely horizontal.

    LaTeX: `\label{def:boson}` -/
structure Boson (M : Type*) extends QHarmonicForm M where
  /-- The form is purely horizontal: `ι_ξ α = 0`. -/
  purely_horizontal : ∀ (p : M), vertical p = 0

/-- A boson's total form equals its horizontal component. -/
theorem Boson.total_eq_horizontal {M : Type*} (b : Boson M) (p : M) :
    b.total p = b.horizontal p := by
  simpa [b.purely_horizontal p] using b.decomp p

end QOU
