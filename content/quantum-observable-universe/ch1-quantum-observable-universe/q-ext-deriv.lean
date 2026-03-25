/-!
# QOU.qExtDeriv

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/qExtDeriv.lean (monolithic)
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

/-- **q-Deformed exterior derivative**: `d_q α = q⁻¹ dα + (1 − q⁻¹) θ ∧ L_ξ α`.

    LaTeX: `\label{def:q-ext-deriv}` -/
noncomputable def qExtDeriv {M : Type*} (sp : SubstrateParameter M)
    (d_alpha : M → ℝ) (lieDerivReeb : M → ℝ) (theta : M → ℝ) (p : M) : ℝ :=
  (sp.field p)⁻¹ * d_alpha p +
    (1 - (sp.field p)⁻¹) * (theta p * lieDerivReeb p)

/-- The q-deformed exterior derivative recovers the classical `d` at `q = 1`. -/
theorem qExtDeriv_classical {M : Type*} (sp : SubstrateParameter M)
    (d_alpha lieDerivReeb theta : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qExtDeriv sp d_alpha lieDerivReeb theta p = d_alpha p := by
  simp [qExtDeriv, hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
