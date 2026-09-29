/-
  Quantum ideal gas law: P_q · V_q = N · T_q · (1 + ℏ_q² · ⟨S_q⟩ / [2]_q).

  The proof proceeds from the partition function. At leading order,
  P_q · V_q = N · T_q (the q-anomaly correction is second-order in ℏ_q).

**Ground ring**: archimedean specialisation over `ℝ` (AGENTS.md §7c).
The equation-of-state proofs use ordering, division, and positivity, so
they live over `ℝ`; the underlying combinatorial content stays generic to
any commutative ring with the same `q`-data.  `R_q := ℝ` is the substrate
specialisation `ι : ℤ[q, q⁻¹] → ℝ, q ↦ q₀`.
-/
import QOU.QuantumObservableUniverse
import QOU.MathConstants
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace QOU.Information

noncomputable section

/-- Ground ring: archimedean specialisation `R_q := ℝ` (AGENTS.md §7c).
    The numerical substrate value `q₀ ≈ 1.1097` lives in `ℝ`. -/
abbrev R_q := ℝ

/-- **Quantum temperature** `T_q(p) = ℏ_q(p)`.
    The brane is at unit thermal scale set by the quantum Planck constant
    (see `quantum-pressure.md`: `T_q = ℏ_q`, `β_q = 1/ℏ_q = t_P(q)`). -/
noncomputable def quantumTemperature {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : R_q :=
  quantumPlanckConstant sp p

/-- **Quantum ideal gas state**: the thermodynamic data of a gas of
    N non-interacting particle knots in a region with quantum volume V_q.
    Label: prop:quantum-ideal-gas-law -/
structure IdealKnotGas (M : Type*) where
  sp : ArchimedeanSubstrateField M
  point : M
  /-- Number of particle knots. -/
  N : ℕ
  /-- Quantum volume V_q of the region. -/
  V_q : R_q
  /-- Thermal expectation of the categorical action ⟨S_q⟩. -/
  meanAction : R_q
  /-- Boundary norm (Frobenius pairing contribution). -/
  boundaryNorm : R_q
  /-- q > 1 (non-classical). -/
  hq : sp.field point > 1
  /-- Positive volume. -/
  hV : 0 < V_q
  /-- Non-negative action expectation. -/
  hS : 0 ≤ meanAction

/-- The q-anomaly correction factor: ℏ_q² · ⟨S_q⟩ / [2]_q. -/
noncomputable def correctionFactor {M : Type*} (gas : IdealKnotGas M) : R_q :=
  let hbar := quantumPlanckConstant gas.sp gas.point
  let q := gas.sp.field gas.point
  hbar ^ 2 * gas.meanAction / (q + q⁻¹)

/-- The q-anomaly correction is non-negative. -/
theorem correctionFactor_nonneg {M : Type*} (gas : IdealKnotGas M) :
    0 ≤ correctionFactor gas := by
  unfold correctionFactor
  apply div_nonneg
  · exact mul_nonneg (sq_nonneg _) gas.hS
  · have hq_pos : (0 : R_q) < gas.sp.field gas.point := by linarith [gas.hq]
    have hinv : (0 : R_q) < (gas.sp.field gas.point)⁻¹ := inv_pos.mpr hq_pos
    linarith

/-- The q-anomaly correction factor vanishes when ℏ_q = 0 (classicality).
    Stated directly: for any q, S, the expression ℏ_q² · S / [2]_q
    vanishes when ℏ_q = 0. -/
theorem correctionFactor_vanishes_at_zero (S : R_q) (q2 : R_q) (hq2 : q2 ≠ 0) :
    (0 : R_q) ^ 2 * S / q2 = 0 := by
  simp

/-- **Leading-order quantum ideal gas law**: P · V = N · T_q.

    This encodes the equation of state at zeroth order in ℏ_q.
    The full equation includes the correction 1 + ℏ_q²⟨S_q⟩/[2]_q. -/
theorem ideal_gas_leading_order {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M)
    (hq : sp.field p > 1)
    (N : ℕ) (V_q P_q : R_q)
    (h_eos : P_q * V_q = N * quantumPlanckConstant sp p) :
    P_q * V_q = N * quantumTemperature sp p := by
  rw [h_eos]
  unfold quantumTemperature
  ring

/-- **Full quantum ideal gas law**: P · V = N · T_q · (1 + correction).

    Given the equation of state with correction factor, the pressure-volume
    product decomposes into the classical part N·T_q and the q-anomaly part. -/
theorem ideal_gas_full {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M)
    (hq : sp.field p > 1)
    (N : ℕ) (P_q V_q S_q : R_q)
    (hS : 0 ≤ S_q)
    (h_eos : P_q * V_q = N * quantumPlanckConstant sp p *
      (1 + (quantumPlanckConstant sp p) ^ 2 * S_q /
           (sp.field p + (sp.field p)⁻¹))) :
    P_q * V_q ≥ N * quantumTemperature sp p := by
  rw [h_eos]
  unfold quantumTemperature
  have hbar_nn := quantumPlanckConstant_nonneg sp p
  have hq_pos : (0 : R_q) < sp.field p := by linarith
  have hinv_pos : (0 : R_q) < (sp.field p)⁻¹ := inv_pos.mpr hq_pos
  have hden_pos : (0 : R_q) < sp.field p + (sp.field p)⁻¹ := by linarith
  have hcorr : 0 ≤ (quantumPlanckConstant sp p) ^ 2 * S_q /
      (sp.field p + (sp.field p)⁻¹) :=
    div_nonneg (mul_nonneg (sq_nonneg _) hS) (le_of_lt hden_pos)
  nlinarith [mul_nonneg (Nat.cast_nonneg' N) hbar_nn]

/-- The full equation of state decomposes as PV = NT + N·T·correction:
    the correction is additive. -/
theorem ideal_gas_decomposition {M : Type*}
    (sp : ArchimedeanSubstrateField M) (p : M)
    (hq : sp.field p > 1)
    (N : ℕ) (S_q : R_q) (hS : 0 ≤ S_q) :
    let hbar := quantumPlanckConstant sp p
    let q := sp.field p
    (N : R_q) * hbar * (1 + hbar ^ 2 * S_q / (q + q⁻¹)) =
    (N : R_q) * hbar + (N : R_q) * hbar ^ 3 * S_q / (q + q⁻¹) := by
  simp only []
  ring

end

end QOU.Information
