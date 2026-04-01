/-!
# QOU.SubstrateParameter

The substrate parameter is the fibre coordinate q ∈ k× on the
one-parameter family of interpolations between the full differential d
and the vertical projection π_V ∘ d.  Categorically, it is the unique
scalar such that d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d acts as q⁻¹ d on
horizontal forms and as d on vertical forms.
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
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousFunction.Basic

open scoped Topology CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Substrate parameter** (categorical): the fibre coordinate `q ∈ k×`
    on the one-parameter family of operators interpolating between
    the full differential `d` and the vertical differential `π_V ∘ d`.

    When the quantum universe is fibred over a space `M`, the substrate
    parameter becomes a field `q : M → k×`.

    Key properties:
    - `q(p) > 0` and `q(p) ≥ 1` (classicality bound)
    - `q(p)` is not a root of unity (ensures semisimplicity)
    - At `q = 1`: `d_q = d` (classical limit)
    - As `q → ∞`: `d_q → π_V ∘ d` (deep-quantum regime)

    LaTeX: `\label{def:substrate-parameter}` -/
structure SubstrateParameter (M : Type*) where
  /-- The substrate field `q : M → ℝ` with `q(p) ≥ 1`.
      Categorically, `q(p)` is the interpolation coefficient
      in `d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d` at the point `p`. -/
  field : M → ℝ
  /-- Invertibility: `q(p) > 0` for all `p`. -/
  field_pos : ∀ (p : M), 0 < field p
  /-- Lower bound: `q(p) ≥ 1` (classicality bound).
      At `q = 1` the interpolation yields `d_q = d`;
      `q > 1` is the quantum regime. -/
  field_ge_one : ∀ (p : M), 1 ≤ field p
  /-- The specialised value `q₀(p)` is never a root of unity,
      ensuring semisimplicity of the quantum group at each point.
      Encoded as: `q(p)^k ≠ 1` for all `k ≥ 1`. -/
  not_root_of_unity : ∀ (p : M) (k : ℕ), k ≥ 1 → field p ^ k ≠ 1

/-- The substrate parameter is strictly greater than 1 in the quantum regime. -/
theorem SubstrateParameter.field_ne_one {M : Type*}
    (sp : SubstrateParameter M) (p : M)
    (hq : sp.not_root_of_unity p 1 (le_refl 1)) : sp.field p ≠ 1 := by
  intro h
  exact hq (by simp [h])

/-- The interpolation coefficient `q⁻¹` is well-defined (q is positive). -/
theorem SubstrateParameter.field_ne_zero {M : Type*}
    (sp : SubstrateParameter M) (p : M) : sp.field p ≠ 0 :=
  ne_of_gt (sp.field_pos p)

/-- The quantum Planck constant `ℏ_q(p) = 1 − q(p)⁻¹` measures
    displacement along the Reeb fibre.  At `q = 1`, `ℏ_q = 0`;
    as `q → ∞`, `ℏ_q → 1`. -/
noncomputable def SubstrateParameter.planck {M : Type*}
    (sp : SubstrateParameter M) (p : M) : ℝ :=
  1 - (sp.field p)⁻¹

/-- The Planck constant is non-negative when `q ≥ 1`. -/
theorem SubstrateParameter.planck_nonneg {M : Type*}
    (sp : SubstrateParameter M) (p : M) : 0 ≤ sp.planck p := by
  unfold planck
  have hq := sp.field_ge_one p
  have hpos := sp.field_pos p
  linarith [inv_le_one_of_one_le₀ hq]

/-- At `q = 1` the Planck constant vanishes (classicality). -/
theorem SubstrateParameter.planck_classical {M : Type*}
    (sp : SubstrateParameter M) (p : M) (hq : sp.field p = 1) :
    sp.planck p = 0 := by
  unfold planck
  simp [hq]

end QOU
