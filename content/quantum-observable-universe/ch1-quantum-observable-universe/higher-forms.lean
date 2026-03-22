/-!
# QOU.HigherForms

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/HigherForms.lean (monolithic)
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

/-- **Higher differential forms** `Ωᵏ(A) = ⋀ᵏ_A Ω¹(A)`.

    The graded `A`-bimodule of exterior powers of Kähler differentials,
    with `Ω⁰(A) = A` and `d : Ωᵏ → Ωᵏ⁺¹` satisfying `d² = 0`.

    LaTeX: `\label{def:higher-forms}` -/
structure HigherForms (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The underlying Frobenius–Hopf object `A`. -/
  frobHopf : @FrobeniusHopfData C _ _
  /-- The degree-`k` form object `Ωᵏ(A)` in `C`. -/
  formObj : ℕ → C
  /-- `Ω⁰(A) = A`. -/
  degree_zero : formObj 0 = frobHopf.obj
  /-- The differential `d : Ωᵏ(A) → Ωᵏ⁺¹(A)`. -/
  d : (k : ℕ) → formObj k ⟶ formObj (k + 1)

end QOU
