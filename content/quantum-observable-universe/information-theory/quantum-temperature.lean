/-
  Quantum temperature: T_q = ℏ_q = (q - 1) / q.

  Temperature is the quantum Planck constant — the tick rate
  of the Reeb dynamics.  Inverse temperature β_q = 1/ℏ_q = t_P.

**Ground ring**: archimedean specialisation over `ℝ` (AGENTS.md §7c).
The substrate field `q = sp.field p : ℝ`; the underlying combinatorial
content stays generic to any commutative ring carrying the same
`q`-data, but the inequalities (`0 < q`, `q < 1`) and the division
identities below are archimedean and so live over `ℝ`.
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

namespace QOU.Information

/-- **Quantum temperature** at a point p ∈ M.
    T_q(p) = ℏ_q(p) = (q(p) - 1) / q(p).
    Label: def:quantum-temperature -/
noncomputable def quantumTemperature {M : Type*} (sp : SubstrateParameter M)
    (p : M) : ℝ :=
  quantumPlanckConstant sp p

/-- **Inverse temperature** (Planck time).
    β_q(p) = 1 / T_q(p) = q(p) / (q(p) - 1).
    Label: def:quantum-temperature -/
noncomputable def inverseTemperature {M : Type*} (sp : SubstrateParameter M)
    (p : M) : ℝ :=
  sp.field p / (sp.field p - 1)

/-- The quantum temperature is non-negative. -/
theorem quantumTemperature_nonneg {M : Type*} (sp : SubstrateParameter M)
    (p : M) : 0 ≤ quantumTemperature sp p :=
  quantumPlanckConstant_nonneg sp p

/-- The quantum temperature is strictly positive when q > 1. -/
theorem quantumTemperature_pos {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) : 0 < quantumTemperature sp p := by
  unfold quantumTemperature quantumPlanckConstant
  have hq_pos : (0 : ℝ) < sp.field p := by linarith
  have hinv_pos : (0 : ℝ) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
  have hinv_lt : (sp.field p)⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

/-- The quantum temperature is bounded above by 1. -/
theorem quantumTemperature_lt_one {M : Type*} (sp : SubstrateParameter M)
    (p : M) : quantumTemperature sp p < 1 :=
  quantumPlanckConstant_lt_one sp p

/-- Inverse temperature equals the reciprocal of temperature when q > 1. -/
theorem inverseTemperature_eq_inv {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    inverseTemperature sp p = 1 / quantumTemperature sp p := by
  unfold inverseTemperature quantumTemperature quantumPlanckConstant
  have hq_ne : sp.field p ≠ 0 := by linarith
  have hq1_ne : sp.field p - 1 ≠ 0 := by linarith
  field_simp

/-- β_q · T_q = 1: the product of inverse temperature and temperature is unity. -/
theorem beta_times_temperature {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    inverseTemperature sp p * quantumTemperature sp p = 1 := by
  unfold inverseTemperature quantumTemperature quantumPlanckConstant
  have hq_ne : sp.field p ≠ 0 := by linarith
  have hq1_ne : sp.field p - 1 ≠ 0 := by linarith
  field_simp

/-- At classicality (q = 1), temperature vanishes. -/
theorem quantumTemperature_classical {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p = 1) :
    quantumTemperature sp p = 0 := by
  unfold quantumTemperature quantumPlanckConstant
  rw [hq]; simp

/-- The quantum temperature equals (q - 1) / q. -/
theorem quantumTemperature_eq {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq_ne : sp.field p ≠ 0) :
    quantumTemperature sp p = (sp.field p - 1) / sp.field p := by
  unfold quantumTemperature quantumPlanckConstant
  field_simp

end QOU.Information
