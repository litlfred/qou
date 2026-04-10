/-
  Boltzmann constant: k_B = ℏ_q = (q - 1) / q.

  The Boltzmann constant IS the quantum Planck constant.
  This is proved from the canonical ensemble: β = 1/(k_B T)
  with β_q = 1/ℏ_q and T_q = ℏ_q gives k_B = ℏ_q.
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace QOU.Information

/-- **Boltzmann constant** at a point p ∈ M.
    k_B(p) = ℏ_q(p) = (q(p) - 1) / q(p).
    Label: prop:boltzmann-constant -/
noncomputable def boltzmannConstant {M : Type*} (sp : SubstrateParameter M)
    (p : M) : ℝ :=
  quantumPlanckConstant sp p

/-- The Boltzmann constant equals the quantum Planck constant.
    This is the structural identification: k_B = ℏ_q. -/
theorem boltzmann_eq_planck {M : Type*} (sp : SubstrateParameter M)
    (p : M) : boltzmannConstant sp p = quantumPlanckConstant sp p :=
  rfl

/-- The Boltzmann constant satisfies β · k_B · T = 1 when β = 1/ℏ_q and T = ℏ_q.
    This is the content of the proposition: the classical relation
    β = 1/(k_B T) is satisfied identically. -/
theorem boltzmann_canonical_identity {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    let β := sp.field p / (sp.field p - 1)
    let T := quantumPlanckConstant sp p
    let k_B := boltzmannConstant sp p
    β * k_B * T = 1 := by
  simp only []
  unfold boltzmannConstant quantumPlanckConstant
  have hq_ne : sp.field p ≠ 0 := by linarith
  have hq1_ne : sp.field p - 1 ≠ 0 := by linarith
  field_simp
  ring

/-- The relation 1/(k_B · T) = β holds: inverse temperature is the
    reciprocal of k_B T. -/
theorem inverse_temperature_identity {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    1 / (boltzmannConstant sp p * quantumPlanckConstant sp p) =
    sp.field p / (sp.field p - 1) := by
  unfold boltzmannConstant quantumPlanckConstant
  have hq_ne : sp.field p ≠ 0 := by linarith
  have hq1_ne : sp.field p - 1 ≠ 0 := by linarith
  field_simp
  ring

/-- **Gas constant** (leading order).
    R_q ≈ ℏ_q³ / Vol(B₃) where Vol(B₃) is the Borromean volume.
    Parameterised by the Borromean volume as a positive real. -/
noncomputable def gasConstant {M : Type*} (sp : SubstrateParameter M)
    (p : M) (borromeanVolume : ℝ) : ℝ :=
  (quantumPlanckConstant sp p) ^ 3 / borromeanVolume

/-- The gas constant is positive when q > 1 and Borromean volume is positive. -/
theorem gasConstant_pos {M : Type*} (sp : SubstrateParameter M)
    (p : M) (V_B : ℝ) (hq : sp.field p > 1) (hV : 0 < V_B) :
    0 < gasConstant sp p V_B := by
  unfold gasConstant
  apply div_pos
  · apply pow_pos
    exact quantumTemperature_pos sp p hq
  · exact hV

/-- The gas constant vanishes at classicality. -/
theorem gasConstant_classical {M : Type*} (sp : SubstrateParameter M)
    (p : M) (V_B : ℝ) (hq : sp.field p = 1) :
    gasConstant sp p V_B = 0 := by
  unfold gasConstant quantumPlanckConstant
  rw [hq]; simp

/-- The gas constant equals N_A · k_B at leading order, where
    N_A = ℏ_q² / Vol(B₃) (categorical Avogadro number). -/
theorem gasConstant_eq_NA_kB {M : Type*} (sp : SubstrateParameter M)
    (p : M) (V_B : ℝ) (hV : V_B ≠ 0) :
    gasConstant sp p V_B =
    ((quantumPlanckConstant sp p) ^ 2 / V_B) *
      boltzmannConstant sp p := by
  unfold gasConstant boltzmannConstant
  field_simp
  ring

end QOU.Information
