/-
  Boltzmann constant: k_B = 1 in QOU natural units.

  The quantum Planck constant ℏ_q plays the role of k_B · T_phys.
  In QOU units, temperature T_q = ℏ_q already has units of energy,
  so k_B = 1 (no conversion needed).

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

namespace QOU.Information

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Thermal energy** at a point p ∈ M.
    The product k_B · T_phys in classical physics corresponds to ℏ_q
    in QOU. Since k_B = 1 in natural units, the thermal energy IS
    the quantum temperature: thermalEnergy = T_q = ℏ_q.
    Label: prop:boltzmann-constant -/
noncomputable def thermalEnergy {M : Type*} (sp : SubstrateParameter M)
    (p : M) : R_q :=
  quantumPlanckConstant sp p

/-- The canonical ensemble identity: β · T = 1.
    With β = q/(q-1) and T = (q-1)/q = ℏ_q, the product is unity.
    This is the content of the Boltzmann identification: inverse
    temperature is the reciprocal of the thermal energy. -/
theorem beta_times_thermalEnergy {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    let β := sp.field p / (sp.field p - 1)
    β * thermalEnergy sp p = 1 := by
  simp only []
  unfold thermalEnergy quantumPlanckConstant
  have hq_ne : sp.field p ≠ 0 := by linarith
  have hq1_ne : sp.field p - 1 ≠ 0 := by linarith
  field_simp
  ring

/-- Inverse temperature is the reciprocal of the thermal energy. -/
theorem inverse_temperature_eq {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    1 / thermalEnergy sp p = sp.field p / (sp.field p - 1) := by
  unfold thermalEnergy quantumPlanckConstant
  have hq_ne : sp.field p ≠ 0 := by linarith
  have hq1_ne : sp.field p - 1 ≠ 0 := by linarith
  field_simp

/-- The quantum ideal gas law in terms of thermal energy:
    PV = N · thermalEnergy = N · ℏ_q at leading order.
    This is the equation PV = N k_B T with k_B = 1. -/
theorem ideal_gas_thermal {M : Type*} (sp : SubstrateParameter M)
    (p : M) (N : ℕ) :
    (N : R_q) * thermalEnergy sp p =
    (N : R_q) * quantumPlanckConstant sp p := by
  unfold thermalEnergy

/-- The thermal energy is positive when q > 1. -/
theorem thermalEnergy_pos {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p > 1) :
    0 < thermalEnergy sp p := by
  unfold thermalEnergy quantumPlanckConstant
  have hq_pos : (0 : R_q) < sp.field p := by linarith
  have hinv_lt : (sp.field p)⁻¹ < 1 := by
    rw [inv_lt_one_iff_of_pos hq_pos]; linarith
  linarith [inv_pos.mpr hq_pos]

/-- **Gas constant** (leading order).
    R_q ≈ ℏ_q³ / Vol(B₃) where Vol(B₃) is the Borromean volume.
    Since k_B = 1, R = N_A where N_A = ℏ_q² / Vol(B₃). -/
noncomputable def gasConstant {M : Type*} (sp : SubstrateParameter M)
    (p : M) (borromeanVolume : R_q) : R_q :=
  (quantumPlanckConstant sp p) ^ 3 / borromeanVolume

/-- The gas constant is positive when q > 1 and Borromean volume is positive. -/
theorem gasConstant_pos {M : Type*} (sp : SubstrateParameter M)
    -- (p : M) (V_B : R_q) (hq : sp.field p > 1) (hV : 0 < V_B) :  -- (archimedean; not meaningful over R_q)
    0 < gasConstant sp p V_B := by
  unfold gasConstant
  apply div_pos
  · apply pow_pos
    exact thermalEnergy_pos sp p hq
  · exact hV

/-- The gas constant vanishes at classicality. -/
theorem gasConstant_classical {M : Type*} (sp : SubstrateParameter M)
    (p : M) (V_B : R_q) (hq : sp.field p = 1) :
    gasConstant sp p V_B = 0 := by
  unfold gasConstant quantumPlanckConstant
  rw [hq]; simp

/-- The gas constant factors as N_A · ℏ_q where N_A = ℏ_q² / Vol(B₃). -/
theorem gasConstant_factored {M : Type*} (sp : SubstrateParameter M)
    (p : M) (V_B : R_q) (hV : V_B ≠ 0) :
    gasConstant sp p V_B =
    ((quantumPlanckConstant sp p) ^ 2 / V_B) *
      thermalEnergy sp p := by
  unfold gasConstant thermalEnergy
  field_simp
  ring

end QOU.Information
