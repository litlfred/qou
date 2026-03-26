/-!
# QOU.QHarmonicForm

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/QHarmonicForm.lean (monolithic)
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

/-- **q-Harmonic form (Particle)**: a section `α` in the kernel of the
    q-Laplacian `Δ_q = d_q δ_q + δ_q d_q`.

    LaTeX: `\label{def:q-harmonic-form}` -/
structure QHarmonicForm (M : Type*) extends ReebDecomposition M where
  /-- The q-Laplacian applied to this form vanishes: `Δ_q α = 0`. -/
  /-- The q-Laplacian value `Δ_q(α)` at each point. -/
  q_laplacian : M → ℝ
  /-- The q-Laplacian vanishes: `Δ_q α = 0`. -/
  q_laplacian_vanishes : ∀ (p : M), q_laplacian p = 0

end QOU
