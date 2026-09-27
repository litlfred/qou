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
import Mathlib.Topology.ContinuousMap.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.Fermion

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/Fermion.lean (monolithic).
That file no longer exists — the library was split, and `Fermion` now lives at
  folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Particles.lean
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Reeb decomposition** of a differential form on a CR manifold.

    Re-declared from the library module
    `QOU.QuantumObservableUniverse.Particles` so this sibling is a
    self-contained compilation unit — importing the library module would
    collide with this block's own `Fermion` / `Boson` /
    `Boson.total_eq_horizontal` declarations.  Keep field-for-field in
    sync with the library.

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

/-- **q-Harmonic form (Particle)**: a section in the kernel of `Δ_q`.
    Re-declared from `QOU.QuantumObservableUniverse.Particles` (see the
    note on `ReebDecomposition` above).  Keep field-for-field in sync.
    LaTeX: `\label{def:q-harmonic-form}` -/
structure QHarmonicForm (M : Type*) extends ReebDecomposition M where
  /-- The q-Laplacian value `Δ_q(α)` at each point. -/
  q_laplacian : M → ℝ
  /-- The q-Laplacian vanishes: `Δ_q α = 0`. -/
  q_laplacian_vanishes : ∀ (p : M), q_laplacian p = 0

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
