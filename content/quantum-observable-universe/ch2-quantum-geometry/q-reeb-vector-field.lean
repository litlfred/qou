/-!
# QOU.qReebVectorField

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/qReebVectorField.lean (monolithic)
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

/-- **q-Deformed Reeb vector field**: defined by its action on smooth functions
    `ξ_q(f) = q⁻¹ ξ(f) + (1 − q⁻¹) [ξ, X_f]_q`.

    LaTeX: `\label{def:q-reeb-vector-field}` -/
noncomputable def qReebVectorField {M : Type*} (sp : SubstrateParameter M)
    (xi_f : M → ℝ) (bracket_q_xi_Xf : M → ℝ) (p : M) : ℝ :=
  (sp.field p)⁻¹ * xi_f p +
    (1 - (sp.field p)⁻¹) * bracket_q_xi_Xf p

end QOU
