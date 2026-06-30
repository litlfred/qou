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
# QOU.CQuantumObservableUniverse

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/CQuantumObservableUniverse.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **ℂ quantum observable universe**: CR manifold data satisfying the
    vanishing conditions `H⁰(M, Ad(P)) = 0` and `Γ_c(M, S) = 0`.

    LaTeX: `\label{def:c-quantum-observable-universe}` -/
structure CQuantumObservableUniverse extends CRManifoldData where
  /-- The type of global sections of the adjoint bundle `Ad(P)`. -/
  adjointSections : Type*
  /-- `H⁰(M, Ad(P))` is trivial: all global adjoint sections are equal.
      In a vector space this means `H⁰(M, Ad(P)) = 0`. -/
  adjoint_cohomology_vanishes : Subsingleton adjointSections
  /-- The type of compactly supported sections of the state bundle `S`. -/
  compactStateSections : Type*
  /-- `Γ_c(M, S)` is trivial: all compactly supported state sections are equal. -/
  state_sections_vanish : Subsingleton compactStateSections

end QOU
