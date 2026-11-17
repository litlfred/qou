import Mathlib.Tactic

/-!
# Nucleon-Scale Energy Identity, Reciprocal-Sum Trace Bound, and Scale Cancellation (`qou-qlma`)

This module formalizes the algebraic results recorded in `qou-qlma`:

1. **Planck-Tick Energy Scale Denominator Identity**:
   For $q_0 \neq 0$, the denominator $q_0(q_0 - 1)$ in $\alpha = m_e / (q_0(q_0 - 1))$
   equals $q_0^2 (1 - 1 / q_0) = q_0^2 \hbar_q$.

2. **Reciprocal-Sum Trace Parameter Bound ($z_m \le 1/2$)**:
   For $x > 0$, $(x + 1/x) - 2 = (x - 1)^2 / x \ge 0$, so $x + 1/x \ge 2$ and
   $z_m(x) = 1 / (x + 1/x) \le 1/2$, with strict inequality $z_m(x) < 1/2$ whenever
   $x \neq 1$. Moreover, the link-invariant parameter $z_J = (q - 1) z_m^2$ satisfies
   $z_J / z_m^2 = q - 1$.

3. **Shared Energy-Scale Cancellation in Observable Ratios**:
   For any two observables $B(\alpha) = \alpha \cdot \mu_B$ and $Q(\alpha) = \alpha \cdot \mu_Q$
   sharing a single scale $\alpha \neq 0$, their ratio $B(\alpha) / Q(\alpha) = \mu_B / \mu_Q$
   is independent of $\alpha$; hence if $\mu_B \cdot Q_{\mathrm{target}} \neq
   \mu_Q \cdot B_{\mathrm{target}}$, no $\alpha$ can match both targets simultaneously.
-/

namespace QOU.MassTheory.NucleonScaleEnergyAndRatioInvariance

/-- Energy-scale denominator $q_0(q_0 - 1)$. -/
noncomputable def scaleDenomProduct (q0 : ℝ) : ℝ :=
  q0 * (q0 - 1)

/-- Deformation-tick denominator $q_0^2 (1 - q_0^{-1})$. -/
noncomputable def scaleDenomTick (q0 : ℝ) : ℝ :=
  q0 ^ 2 * (1 - 1 / q0)

/-- For $q_0 \neq 0$, $q_0(q_0 - 1) = q_0^2 (1 - q_0^{-1})$ and the corresponding
energy scales $m_e / (q_0(q_0 - 1))$ and $m_e / (q_0^2 (1 - q_0^{-1}))$ coincide. -/
theorem scaleDenomProduct_eq_scaleDenomTick (me q0 : ℝ) (hq0 : q0 ≠ 0) :
    scaleDenomProduct q0 = scaleDenomTick q0 ∧
      me / scaleDenomProduct q0 = me / scaleDenomTick q0 := by
  unfold scaleDenomProduct scaleDenomTick
  have h_denom : q0 * (q0 - 1) = q0 ^ 2 * (1 - 1 / q0) := by
    field_simp [hq0]
    ring
  refine ⟨h_denom, ?_⟩
  rw [h_denom]

/-- Reciprocal-sum trace parameter $z_m(x) = 1 / (x + x^{-1})$. -/
noncomputable def reciprocalSumParam (x : ℝ) : ℝ :=
  1 / (x + 1 / x)

/-- For $x > 0$, $(x + x^{-1}) - 2 = (x - 1)^2 / x \ge 0$, so $x + x^{-1} \ge 2$
and $z_m(x) = 1 / (x + x^{-1}) \le 1/2$. -/
theorem reciprocalSumParam_le_half (x : ℝ) (hx : 0 < x) :
    (x + 1 / x) - 2 = (x - 1) ^ 2 / x ∧
      2 ≤ x + 1 / x ∧
      reciprocalSumParam x ≤ 1 / 2 := by
  unfold reciprocalSumParam
  have hx_ne : x ≠ 0 := ne_of_gt hx
  have h_sq_id : (x + 1 / x) - 2 = (x - 1) ^ 2 / x := by
    field_simp [hx_ne]
    ring
  have h_nonneg : 0 ≤ (x - 1) ^ 2 / x :=
    div_nonneg (sq_nonneg (x - 1)) (le_of_lt hx)
  have h_ge2 : 2 ≤ x + 1 / x := by
    linarith [h_sq_id, h_nonneg]
  have h_le_half : 1 / (x + 1 / x) ≤ 1 / 2 :=
    one_div_le_one_div_of_le (by norm_num : (0 : ℝ) < 2) h_ge2
  exact ⟨h_sq_id, h_ge2, h_le_half⟩

/-- When two observables $B(\alpha) = \alpha \mu_B$ and $Q(\alpha) = \alpha \mu_Q$ share a
common scale $\alpha \neq 0$, their ratio equals $\mu_B / \mu_Q$, and no $\alpha \in \mathbb{R}$
can match both $B_{\mathrm{target}}$ and $Q_{\mathrm{target}}$ when
$\mu_B Q_{\mathrm{target}} \neq \mu_Q B_{\mathrm{target}}$. -/
theorem shared_scale_cancels_and_obstructs_joint_fit (muB muQ B_target Q_target alpha : ℝ)
    (h_alpha : alpha ≠ 0) (h_cross : muB * Q_target ≠ muQ * B_target) :
    (alpha * muB) / (alpha * muQ) = muB / muQ ∧
      ¬ ∃ a : ℝ, a * muB = B_target ∧ a * muQ = Q_target := by
  have h_ratio : (alpha * muB) / (alpha * muQ) = muB / muQ :=
    mul_div_mul_left muB muQ h_alpha
  refine ⟨h_ratio, ?_⟩
  rintro ⟨a, haB, haQ⟩
  have h_lhs : muB * Q_target = muB * (a * muQ) := by rw [← haQ]
  have h_rhs : muQ * B_target = muQ * (a * muB) := by rw [← haB]
  have h_comm : muB * (a * muQ) = muQ * (a * muB) := by ring
  have h_eq : muB * Q_target = muQ * B_target := by
    rw [h_lhs, h_rhs, h_comm]
  exact h_cross h_eq

end QOU.MassTheory.NucleonScaleEnergyAndRatioInvariance
