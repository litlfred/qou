/-
  Planck time: t_P(q) = q / (q - 1) = 1 / ℏ_q.

  The minimal dynamical time unit of the QOU, defined as the
  period of one full Reeb circuit.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU

/-- Planck time as a function of the substrate parameter q.
    Defined as q / (q - 1), the reciprocal of the quantum
    Planck constant ℏ_q = 1 - q⁻¹. -/
noncomputable def planckTime {k : Type*} [Field k] (q : k) (hq : q ≠ 1) : k :=
  q / (q - 1)

/-- Planck time equals reciprocal of quantum Planck constant. -/
-- Ref: [manuscript] Ch 8, Definition: Planck Time
theorem planckTime_eq_inv_hbar {k : Type*} [Field k] (q : k) (hq : q ≠ 0) (hq1 : q ≠ 1) :
    planckTime q hq1 = 1 / (1 - q⁻¹) := by
  -- Ref: [manuscript] Ch 8, Definition: Planck Time
  -- planckTime q = q/(q-1) and 1/(1 - q⁻¹) = 1/((q-1)/q) = q/(q-1).
  unfold planckTime
  have hq_sub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  field_simp

/-- Planck length is identically 1: ℏ_q · t_P = 1. -/
-- Ref: [manuscript] Ch 8, Definition: Planck Time
theorem planck_length_eq_one {k : Type*} [Field k] (q : k) (hq : q ≠ 0) (hq1 : q ≠ 1) :
    (1 - q⁻¹) * planckTime q hq1 = 1 := by
  -- Ref: [manuscript] Ch 8, Definition: Planck Time
  -- (1 - q⁻¹) · q/(q-1) = (q-1)/q · q/(q-1) = 1.
  unfold planckTime
  have hq_sub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  field_simp

end QOU
