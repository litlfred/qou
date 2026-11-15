import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp


/-!
# QOU.Archimedean.QValueTransition — 𝒬_q as categorical action difference

The 𝒬_q-value is defined as the categorical action difference
between parent and daughter, NOT by classical energy conservation.

Classical energy conservation (E_before = E_after) is a q=1 limit.
At q ≠ 1, the q-differential satisfies d_q² ≠ 0, producing a
q-anomaly δ_q in the energy balance.

Note: this file does NOT assume classical conservation of energy.
The equivalence Q_q = T_e + T_ν + T_recoil holds only at q = 1.

LaTeX label: `def:Q-value-transition`

## References
- [leitner2026] §6/q-value-transition

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean

-- ═══════════════════════════════════════════════════════════════════
-- PRIMARY DEFINITION: 𝒬_q from categorical action (no conservation)
-- ═══════════════════════════════════════════════════════════════════

/-- The 𝒬_q-value of a beta decay transition.
    Defined as the categorical action difference — NOT as a sum of
    kinetic energies.  Classical energy conservation is NOT assumed. -/
-- Ref: [leitner2026] §6/q-value-transition
structure QqValue where
  /-- Substrate parameter. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Categorical action of parent nucleus S_q(N_par). -/
  S_parent : ℝ
  /-- Categorical action of daughter nucleus S_q(N_dau). -/
  S_daughter : ℝ
  /-- Categorical action of electron S_q(e). -/
  S_electron : ℝ
  S_electron_pos : 0 < S_electron
  /-- Categorical action of antineutrino S_q(ν̄) = 0 (unknot). -/
  S_antineutrino : ℝ := 0

/-- The 𝒬_q-value: action difference (primary definition). -/
-- Ref: [leitner2026] §6/q-value-transition
noncomputable def QqValue.value (Q : QqValue) : ℝ :=
  Q.S_parent - Q.S_daughter - Q.S_electron - Q.S_antineutrino

-- ═══════════════════════════════════════════════════════════════════
-- THE q-ANOMALY: δ_q = 𝒬_q - (T_e + T_ν + T_recoil)
-- ═══════════════════════════════════════════════════════════════════

/-- The q-anomaly: difference between categorical 𝒬_q and
    the sum of observed kinetic energies.

    Note: this is NONZERO at q ≠ 1.  Classical energy conservation
    (δ_q = 0) holds ONLY at q = 1. -/
-- Ref: [leitner2026] §6/q-value-transition
structure QAnomaly where
  /-- The categorical 𝒬_q. -/
  Q_q : ℝ
  /-- Sum of observed kinetic energies T_e + T_ν̄ + T_recoil. -/
  T_total : ℝ
  /-- The q-anomaly: δ_q = 𝒬_q - T_total. -/
  delta_q : ℝ := Q_q - T_total

/-- ℏ_q = 1 - q⁻¹ (quantum Planck constant). -/
-- Ref: [leitner2026] §6/q-value-transition
noncomputable def hbarQ' (q : ℝ) : ℝ := 1 - 1 / q

/-- The self-deformation shift Δq_eff = (A-1)/A² · ℏ_q². -/
-- Ref: [leitner2026] §6/hadron-q-self-correction
noncomputable def delta_q_eff (q : ℝ) (A : ℕ) : ℝ :=
  ((A : ℝ) - 1) / (A : ℝ) ^ 2 * (hbarQ' q) ^ 2

/-- The self-deformation is positive for A ≥ 2 and q > 1. -/
-- Ref: [leitner2026] §6/hadron-q-self-correction
theorem delta_q_eff_pos {q : ℝ} {A : ℕ} (hq : 1 < q) (hA : 2 ≤ A) :
    0 < delta_q_eff q A := by
  unfold delta_q_eff hbarQ'
  have hA1 : (1 : ℝ) < (A : ℝ) := by exact_mod_cast (show 1 < A by omega)
  have hq0 : (0 : ℝ) < q := by linarith
  have hAne : (A : ℝ) ≠ 0 := by positivity
  apply mul_pos
  · apply div_pos
    · linarith
    · positivity
  · have hlt : 1 / q < 1 := by
      rw [div_lt_one hq0]; linarith
    have hpos : (0 : ℝ) < 1 - 1 / q := by linarith
    positivity

/-- At q = 1, the anomaly vanishes (classical limit). -/
-- Ref: [leitner2026] §6/q-value-transition
theorem delta_q_eff_classical (A : ℕ) : delta_q_eff 1 A = 0 := by
  unfold delta_q_eff hbarQ'
  simp

-- ═══════════════════════════════════════════════════════════════════
-- CROSSING ENERGY
-- ═══════════════════════════════════════════════════════════════════

/-- Crossing energy at a single crossing change d→u: q - q⁻¹. -/
-- Ref: [leitner2026] §6/q-value-transition
noncomputable def singleCrossingDelta (q : ℝ) : ℝ := q - 1 / q

/-- The single-crossing energy difference is positive for q > 1. -/
-- Ref: [leitner2026] §6/q-value-transition
theorem singleCrossingDelta_pos {q : ℝ} (hq : 1 < q) :
    0 < singleCrossingDelta q := by
  unfold singleCrossingDelta
  have hq0 : (0 : ℝ) < q := by linarith
  have hlt : 1 / q < 1 := by
    rw [div_lt_one hq0]; linarith
  linarith

/-- At q = 1: crossing change releases zero energy (no weak force). -/
-- Ref: [leitner2026] §6/q-value-transition
theorem singleCrossingDelta_classical : singleCrossingDelta 1 = 0 := by
  unfold singleCrossingDelta; norm_num

-- ═══════════════════════════════════════════════════════════════════
-- q-DEFORMED CONSERVATION (the CORRECT statement)
-- ═══════════════════════════════════════════════════════════════════

/-- The q-deformed energy balance: the daughter is evaluated at
    the SHIFTED q, not the original.

    S_q(parent) = S_{q+Δq}(daughter) + S_q(e) + S_q(ν̄) + kinetic + δ_q

    Note: this is NOT classical conservation.  The daughter nucleus
    lives in a shifted q-environment due to the re-reduction
    R2 moves in the Hecke algebra. -/
-- Ref: [leitner2026] §6/q-value-transition
structure QDeformedBalance where
  /-- Original substrate parameter. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Mass number of parent. -/
  A : ℕ
  A_ge_two : 2 ≤ A
  /-- Parent action at q. -/
  S_par : ℝ
  /-- Daughter action at shifted q + Δq_eff. -/
  S_dau_shifted : ℝ
  /-- Electron action. -/
  S_e : ℝ
  /-- Antineutrino action (= 0). -/
  S_nu : ℝ := 0
  /-- Total kinetic energy of products. -/
  T_total : ℝ
  /-- The balance: S_par = S_dau(q+Δq) + S_e + S_ν + T_total.
      Note: daughter is evaluated at SHIFTED q. -/
  balance : S_par = S_dau_shifted + S_e + S_nu + T_total

-- ═══════════════════════════════════════════════════════════════════
-- TRITIUM WORKED EXAMPLE (witness-backed from beta-decay-from-q.py)
-- ═══════════════════════════════════════════════════════════════════

/-- Tritium self-deformation: Δq_eff(³H) = (3-1)/3² · ℏ_q² = 2/9 · ℏ_q².
    At q = 1.110: ℏ_q² ≈ 0.009816, so Δq ≈ 0.00218. -/
-- Ref: [leitner2026] beta-decay-from-q.witness.json
theorem tritium_self_deformation :
    delta_q_eff 1.110 3 = (2 : ℝ) / 9 * (hbarQ' 1.110) ^ 2 := by
  unfold delta_q_eff
  norm_num

/-- Tritium self-deformation is positive. -/
-- Ref: [leitner2026] §6/q-value-transition
theorem tritium_delta_q_pos : 0 < delta_q_eff 1.110 3 := by
  apply delta_q_eff_pos (by norm_num : (1 : ℝ) < 1.110) (by norm_num : 2 ≤ 3)

/-- The self-deformation decreases with mass number: Δq_eff(A+1) < Δq_eff(A)
    for A ≥ 2 and q > 1.  Tritium (A=3) has the largest correction. -/
-- Ref: [leitner2026] §6/hadron-q-self-correction
theorem delta_q_decreasing {q : ℝ} (hq : 1 < q) {A : ℕ} (hA : 2 ≤ A) :
    delta_q_eff q (A + 1) < delta_q_eff q A := by
  unfold delta_q_eff
  have hq0 : (0 : ℝ) < q := by linarith
  have hlt : 1 / q < 1 := by
    rw [div_lt_one hq0]; linarith
  have hbpos : (0 : ℝ) < hbarQ' q := by unfold hbarQ'; linarith
  apply mul_lt_mul_of_pos_right
  · -- (A)/(A+1)² < (A-1)/A²
    -- Equivalently: A³ < (A-1)(A+1)² = (A²-1)(A+1) = A³ + A² - A - 1
    -- So need: 0 < A² - A - 1, which holds for A ≥ 2.
    have hA2 : (2:ℝ) ≤ (A:ℝ) := by exact_mod_cast hA
    push_cast
    rw [div_lt_div_iff₀ (by nlinarith : (0:ℝ) < ((A:ℝ)+1)^2)
                        (by nlinarith : (0:ℝ) < (A:ℝ)^2)]
    nlinarith
  · positivity

/-- Q_q-value for tritium: total log-ratio = -0.1021.
    Source: beta-decay-matrix.witness.json, σ₀ + σ₁ contributions. -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
noncomputable def tritium_ln_ratio : ℝ := -0.1021

/-- The tritium Q_q is negative (daughter has lower action than parent). -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
theorem tritium_Q_q_negative : tritium_ln_ratio < 0 := by
  unfold tritium_ln_ratio; norm_num

/-- Per-generator contribution fractions.
    σ₀ contributes 22% and σ₁ contributes 78% of the total. -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
noncomputable def sigma0_fraction : ℝ := 0.0229 / 0.1021  -- ≈ 0.224
noncomputable def sigma1_fraction : ℝ := 0.0792 / 0.1021  -- ≈ 0.776

/-- The two generator fractions sum to 1. -/
-- Ref: [leitner2026] beta-decay-matrix.witness.json
theorem generator_fractions_sum :
    sigma0_fraction + sigma1_fraction = 1 := by
  unfold sigma0_fraction sigma1_fraction
  norm_num

end QOU.Archimedean
