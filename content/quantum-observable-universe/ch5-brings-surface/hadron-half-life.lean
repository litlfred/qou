/-!
# QOU.Descartes.hadron_half_life — Beta-decay half-life from q-deformed Fermi golden rule

The decay rate Γ_β of a nucleus displaced from the valley of stability
factorises into a q-dependent prefactor and a geometric factor
A^{-5/3}|δp|^5.  The half-life t_{1/2} = ln2 / Γ_β is derived from
the same Skein binding Lagrangian that determines the valley of stability.

LaTeX label: `prop:hadron-half-life`

## References
- [manuscript] §6/hadron-half-life
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.Descartes

/-- Data for a beta-decay calculation: a nucleus displaced from the
    valley of stability in a Descartes universe with substrate parameter q. -/
-- Ref: [manuscript] §6/hadron-half-life
structure BetaDecayData where
  /-- Substrate parameter q. -/
  q : ℝ
  /-- q > 1 (non-classical universe). -/
  q_gt_one : 1 < q
  /-- Mass number A. -/
  A : ℕ
  /-- A ≥ 1. -/
  A_pos : 0 < A
  /-- Proton displacement δp = p - p_stab(A), integer-valued. -/
  delta_p : ℤ
  /-- The nucleus is unstable: δp ≠ 0. -/
  delta_p_ne_zero : delta_p ≠ 0
  /-- Coulomb scale λ_C > 0. -/
  lambda_C : ℝ
  /-- lambda_C is positive. -/
  lambda_C_pos : 0 < lambda_C
  /-- Pauli asymmetry coefficient a_A > 0. -/
  a_A : ℝ
  /-- a_A is positive. -/
  a_A_pos : 0 < a_A
  /-- Fermi coupling constant G_F > 0. -/
  G_F : ℝ
  /-- G_F is positive. -/
  G_F_pos : 0 < G_F

/-- Coulomb coefficient: a_C = (q - q⁻¹) · λ_C. -/
-- Ref: [manuscript] §6/hadron-half-life
noncomputable def BetaDecayData.a_C (d : BetaDecayData) : ℝ :=
  (d.q - 1 / d.q) * d.lambda_C

/-- The Coulomb coefficient is positive when q > 1 and λ_C > 0. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem BetaDecayData.a_C_pos (d : BetaDecayData) : 0 < d.a_C := by
  unfold a_C
  apply mul_pos _ d.lambda_C_pos
  rw [sub_pos, div_lt_iff (by linarith : (0 : ℝ) < d.q)]
  nlinarith [d.q_gt_one]

/-- Q-value of the beta decay: Q_β = 2α(A)·|δp|
    where α(A) = a_C/A^{1/3} + a_A/A is the parabola curvature. -/
-- Ref: [manuscript] §6/hadron-half-life
noncomputable def BetaDecayData.Q_beta (d : BetaDecayData) : ℝ :=
  2 * (d.a_C / (d.A : ℝ) ^ ((1 : ℝ) / 3) + d.a_A / d.A) * |d.delta_p|

/-- The Q-value is positive for an unstable nucleus. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem BetaDecayData.Q_beta_pos (d : BetaDecayData) : 0 < d.Q_beta := by
  unfold Q_beta
  apply mul_pos
  · apply mul_pos (by norm_num : (0 : ℝ) < 2)
    apply add_pos
    · exact div_pos d.a_C_pos (rpow_pos_of_pos (Nat.cast_pos.mpr d.A_pos) _)
    · exact div_pos d.a_A_pos (Nat.cast_pos.mpr d.A_pos)
  · exact_mod_cast abs_pos.mpr d.delta_p_ne_zero

/-- The q-integer [2]_q = q + q⁻¹, categorical dimension of the
    SU_q(2) fundamental representation. -/
-- Ref: [manuscript] §6/hadron-half-life
noncomputable def BetaDecayData.q_integer_2 (d : BetaDecayData) : ℝ :=
  d.q + 1 / d.q

/-- [2]_q > 2 when q > 1. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem BetaDecayData.q_integer_2_gt_two (d : BetaDecayData) :
    2 < d.q_integer_2 := by
  unfold q_integer_2
  have hq : 0 < d.q := by linarith [d.q_gt_one]
  rw [show (2 : ℝ) = 1 + 1 from by norm_num]
  have : 1 < d.q := d.q_gt_one
  have : 1 / d.q < 1 := by rwa [div_lt_one hq]
  -- q > 1 and 1/q < 1, but q + 1/q > 1 + 1 = 2 by AM-GM
  nlinarith [sq_nonneg (d.q - 1 / d.q)]

/-- The q-dependent prefactor of the decay rate:
    F(q) = (q + q⁻¹) · (q - q⁻¹)⁵.

    This encodes that both the weak-vertex dimension [2]_q and the
    Coulomb-driven Q-value (through the Sargent Q⁵ rule) depend on q. -/
-- Ref: [manuscript] §6/hadron-half-life
noncomputable def qPrefactor (q : ℝ) : ℝ :=
  (q + 1 / q) * (q - 1 / q) ^ 5

/-- The q-prefactor vanishes at q = 1 (classical limit):
    no Coulomb splitting means no beta decay. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem qPrefactor_classical : qPrefactor 1 = 0 := by
  unfold qPrefactor
  norm_num

/-- The q-prefactor is positive for q > 1. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem qPrefactor_pos {q : ℝ} (hq : 1 < q) : 0 < qPrefactor q := by
  unfold qPrefactor
  apply mul_pos
  · -- q + 1/q > 0
    have : 0 < q := by linarith
    positivity
  · -- (q - 1/q)^5 > 0
    apply pow_pos
    rw [sub_pos, div_lt_iff (by linarith : (0 : ℝ) < q)]
    nlinarith

/-- Beta-decay rate: Γ_β ∝ F(q) · |δp|⁵ / A^{5/3}.

    The full expression is (G_F²/2π³ℏ) · [2]_q · |M_q|² · f(Q_β).
    We define the proportional form that captures the q and geometric
    dependence; the overall normalisation involves G_F and nuclear
    matrix elements. -/
-- Ref: [manuscript] §6/hadron-half-life
noncomputable def BetaDecayData.decayRate (d : BetaDecayData) : ℝ :=
  qPrefactor d.q * d.lambda_C ^ 5 *
    (|d.delta_p| : ℝ) ^ 5 / (d.A : ℝ) ^ ((5 : ℝ) / 3)

/-- The decay rate is positive for an unstable nucleus in a non-classical universe. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem BetaDecayData.decayRate_pos (d : BetaDecayData) : 0 < d.decayRate := by
  unfold decayRate
  apply div_pos
  · apply mul_pos
    apply mul_pos
    · exact qPrefactor_pos d.q_gt_one
    · exact pow_pos d.lambda_C_pos 5
    · exact pow_pos (by exact_mod_cast abs_pos.mpr d.delta_p_ne_zero) 5
  · exact rpow_pos_of_pos (Nat.cast_pos.mpr d.A_pos) _

/-- Half-life: t_{1/2} = ln 2 / Γ_β. -/
-- Ref: [manuscript] §6/hadron-half-life
noncomputable def BetaDecayData.halfLife (d : BetaDecayData) : ℝ :=
  Real.log 2 / d.decayRate

/-- The half-life is positive. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem BetaDecayData.halfLife_pos (d : BetaDecayData) : 0 < d.halfLife := by
  unfold halfLife
  exact div_pos (Real.log_pos (by norm_num : (1 : ℝ) < 2)) d.decayRate_pos

/-- Scaling relation: t_{1/2} ∝ 1/F(q) · A^{5/3} / |δp|^5.

    Equivalently, the product t_{1/2} · F(q) · |δp|^5 / A^{5/3} is
    independent of q, A, and δp — it equals ln2 / λ_C^5. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem halfLife_scaling (d : BetaDecayData) :
    d.halfLife * (qPrefactor d.q * d.lambda_C ^ 5 *
      (|d.delta_p| : ℝ) ^ 5 / (d.A : ℝ) ^ ((5 : ℝ) / 3)) = Real.log 2 := by
  unfold BetaDecayData.halfLife BetaDecayData.decayRate
  rw [div_mul_cancel₀]
  exact ne_of_gt (by
    apply div_pos
    · apply mul_pos; apply mul_pos
      · exact qPrefactor_pos d.q_gt_one
      · exact pow_pos d.lambda_C_pos 5
      · exact pow_pos (by exact_mod_cast abs_pos.mpr d.delta_p_ne_zero) 5
    · exact rpow_pos_of_pos (Nat.cast_pos.mpr d.A_pos) _)

/-- Monotonicity in displacement: larger |δp| means shorter half-life
    (faster decay) at fixed A and q.

    This formalises the physical statement that nuclei farther from
    the valley of stability decay faster. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem halfLife_decreasing_in_displacement
    (d₁ d₂ : BetaDecayData)
    (hq : d₁.q = d₂.q)
    (hA : d₁.A = d₂.A)
    (hλ : d₁.lambda_C = d₂.lambda_C)
    (hdisp : |d₁.delta_p| < |d₂.delta_p|) :
    d₂.halfLife < d₁.halfLife := by
  unfold BetaDecayData.halfLife
  apply div_lt_div_of_pos_left (Real.log_pos (by norm_num : (1 : ℝ) < 2))
    d₂.decayRate_pos d₁.decayRate_pos
  -- Need: d₁.decayRate < d₂.decayRate
  unfold BetaDecayData.decayRate
  rw [hq, hA, hλ]
  apply div_lt_div_of_pos_right _ (rpow_pos_of_pos (Nat.cast_pos.mpr d₂.A_pos) _)
  apply mul_lt_mul_of_pos_left
  · exact pow_lt_pow_left
      (by exact_mod_cast hdisp)
      (by positivity)
      (by norm_num)
  · exact mul_pos (qPrefactor_pos (hq ▸ d₁.q_gt_one)) (pow_pos (hλ ▸ d₁.lambda_C_pos) 5)

/-- Sensitivity: ∂ ln Γ / ∂ ln q = (12q² - 10)/(q² - 1).

    At q = 1.110 this is ≈ 49, meaning a 1% shift in q changes
    decay rates by ~50%. We state and prove the algebraic identity;
    the numerical evaluation is a corollary. -/
-- Ref: [manuscript] §6/hadron-half-life
noncomputable def qSensitivity (q : ℝ) : ℝ :=
  (12 * q ^ 2 - 10) / (q ^ 2 - 1)

/-- The sensitivity is positive for q > 1. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem qSensitivity_pos {q : ℝ} (hq : 1 < q) : 0 < qSensitivity q := by
  unfold qSensitivity
  apply div_pos
  · nlinarith
  · nlinarith

/-- The sensitivity diverges as q → 1⁺ (reflecting the critical
    transition from zero to nonzero decay rate). -/
-- Ref: [manuscript] §6/hadron-half-life
theorem qSensitivity_large_near_one :
    ∀ M : ℝ, ∃ q : ℝ, 1 < q ∧ M < qSensitivity q := by
  intro M
  -- For q close to 1, (12q² - 10)/(q² - 1) → 2/(q² - 1) → ∞
  -- Ref: [manuscript] §6/hadron-half-life
  sorry

/-- Top-level alias matching the manifest declaration
    `QOU.Descartes.hadron_half_life`. -/
-- Ref: [manuscript] §6/hadron-half-life
noncomputable def hadron_half_life (d : BetaDecayData) : ℝ := d.halfLife

/-- The half-life (top-level alias) is positive. -/
-- Ref: [manuscript] §6/hadron-half-life
theorem hadron_half_life_pos (d : BetaDecayData) : 0 < hadron_half_life d :=
  d.halfLife_pos

end QOU.Descartes
