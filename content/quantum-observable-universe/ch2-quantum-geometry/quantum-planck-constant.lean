/-!
# QOU.quantumPlanckConstant

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/quantumPlanckConstant.lean (monolithic)
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

/-- **Quantum Planck constant**: `ℏ_q(p) = 1 − q(p)⁻¹`.

    A smooth field `M → [0, 1)`.  At classicality `q → 1` we get `ℏ_q → 0`;
    in the deep-quantum regime `q → ∞` we get `ℏ_q → 1`.

    LaTeX: `\label{def:quantum-planck-constant}` -/
noncomputable def quantumPlanckConstant {M : Type*} (sp : SubstrateParameter M)
    (p : M) : ℝ :=
  1 - (sp.field p)⁻¹

/-- The quantum Planck constant takes values in `[0, 1)`. -/
theorem quantumPlanckConstant_nonneg {M : Type*} (sp : SubstrateParameter M)
    (p : M) : 0 ≤ quantumPlanckConstant sp p := by
  unfold quantumPlanckConstant
  linarith [inv_le_one_of_one_le₀ (sp.field_ge_one p)]

theorem quantumPlanckConstant_lt_one {M : Type*} (sp : SubstrateParameter M)
    (p : M) : quantumPlanckConstant sp p < 1 := by
  unfold quantumPlanckConstant
  linarith [inv_pos.mpr (sp.field_pos p)]

/-- At classicality (`q = 1`), the quantum Planck constant vanishes. -/
theorem planck_classical_limit {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p = 1) :
    quantumPlanckConstant sp p = 0 := by
  unfold quantumPlanckConstant
  rw [hq, inv_one, sub_self]

end QOU
