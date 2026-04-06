/-!
# QOU.qLieBracket

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/qLieBracket.lean (monolithic)
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

/-- **q-Deformed Lie bracket**:
    `[V, W]_q = q⁻¹ [V, W] + (1 − q⁻¹)(θ(V) L_ξ W − θ(W) L_ξ V)`.

    LaTeX: `\label{def:q-lie-bracket}` -/
noncomputable def qLieBracket {M : Type*} (sp : SubstrateParameter M)
    (bracket_VW : M → ℝ) (thetaV_LxiW : M → ℝ) (thetaW_LxiV : M → ℝ)
    (p : M) : ℝ :=
  (sp.field p)⁻¹ * bracket_VW p +
    (1 - (sp.field p)⁻¹) * (thetaV_LxiW p - thetaW_LxiV p)

/-- The q-deformed Lie bracket recovers the classical bracket at `q = 1`. -/
theorem qLieBracket_classical {M : Type*} (sp : SubstrateParameter M)
    (bracket_VW thetaV_LxiW thetaW_LxiV : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qLieBracket sp bracket_VW thetaV_LxiW thetaW_LxiV p = bracket_VW p := by
  simp [qLieBracket, hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
