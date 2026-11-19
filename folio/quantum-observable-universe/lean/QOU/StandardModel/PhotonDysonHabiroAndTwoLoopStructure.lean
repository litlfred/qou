/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Data.Real.Basic
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic

/-!
# 1PI Photon Dyson Resummation, Level-4 Two-Loop Quartic Fixed-Point Uniqueness (`qou-l4t2`), and Tree-Complexity Monotonicity

This module establishes the unconditional algebraic and real-analytic structure governing the
electromagnetic Schwinger–Habiro fixed-point tower (`beans/defs/qou-l4t2`, companion to
`QOU.StandardModel.ElectroweakBringSchwingerBridge` and
`QOU.Archimedean.EmCouplingBringZeroMode`):

1. **Section 1 — 1PI Photon Dyson Geometric Resummation & Uniqueness of Form B over Form A:**
   - Defines the 1PI Habiro–Schwinger photon self-energy resummed kernel
     $\Sigma_{\mathrm{Dyson}}(H, h, \alpha) = \frac{\alpha H}{1 + h^2 \alpha}$ ($h = q - q^{-1}$,
     $H = \frac{q + q^{-1}}{8\pi}$), alongside Form A ($\Sigma_A = \alpha H$) and Form B
     ($\Sigma_B = \alpha H(1 - h^2\alpha)$).
   - Proves the exact algebraic Dyson truncation identities:
     $$\Sigma_{\mathrm{Dyson}} - \Sigma_B = \frac{h^4 H \alpha^3}{1 + h^2\alpha}, \qquad
       \Sigma_{\mathrm{Dyson}} - \Sigma_A = -\frac{h^2 H \alpha^2}{1 + h^2\alpha}.$$
   - Proves strict ordering $\Sigma_B(\alpha) < \Sigma_{\mathrm{Dyson}}(\alpha) < \Sigma_A(\alpha)$
     and the sharp cubic remainder bound $0 < \Sigma_{\mathrm{Dyson}}(\alpha) - \Sigma_B(\alpha) < h^4 H \alpha^3$
     (strictly $< 10^{-10}$ on the physical regime $0 < H \le \tfrac{1}{10}$, $0 < |h| \le \tfrac{22}{100}$,
     $0 < \alpha \le \tfrac{1}{137}$), plus exact bar-invariance ($q \mapsto q^{-1}$).

2. **Section 2 — Existence, Uniqueness, & Comparative Root Ordering for the Level-4 Quartic Fixed Point (`qou-l4t2`):**
   - Formalizes the Level-4 two-loop quartic fixed-point polynomial
     $$P_4(T, H, h, c_2; \alpha) = c_2 \alpha^4 - H h^2 \alpha^3 + H \alpha^2 + T \alpha - 1$$
     together with the cleared resummed Dyson quadratic
     $$P_{\mathrm{resum}}(T, H, h; \alpha) = (T\alpha - 1)(1 + h^2\alpha) + H\alpha^2
       = (T h^2 + H)\alpha^2 + (T - h^2)\alpha - 1$$
     and Form A quadratic $P_{\mathrm{FormA}}(T, H; \alpha) = H\alpha^2 + T\alpha - 1$.
   - Proves exact `HasDerivAt` derivative positivity $P_4'(\alpha) > 99 > 0$ on $[0, 1/T]$,
     divided-difference strict monotonicity $P_4(\beta) - P_4(\alpha) > 99(\beta - \alpha)$ on $[0, 1/T]$,
     endpoint sign change $P_4(0) = -1 < 0 < P_4(1/T)$, and **existence and uniqueness** of the
     physical root $\alpha_\star \in (0, 1/T)$ via the Intermediate Value Theorem.
   - Proves the exact comparative inverse-root ordering at $c_2 = 0$:
     $$\alpha_{\mathrm{FormB}}^{-1} < \alpha_{\mathrm{resum}}^{-1} < \alpha_{\mathrm{FormA}}^{-1},$$
     and the exact monotone sign law in the two-loop coefficient $c_2$:
     $$c_2 > 0 \implies \alpha_{\mathrm{FormB}}^{-1} < \alpha_4(c_2)^{-1}, \qquad
       c_2 < 0 \implies \alpha_4(c_2)^{-1} < \alpha_{\mathrm{FormB}}^{-1}.$$

3. **Section 3 — Exact Tree-Complexity Derivative $C'(q) \ge 90 > 0$ & Anchor-Shift Counterterm Equivalence:**
   - Defines the singularity-free Laurent geometric sums $[9]_q = \sum_{k=0}^8 q^{8-2k}$ and
     $[10]_q = \sum_{j=0}^9 q^{9-2j}$ and the bare EM tree complexity $C(q) = q [9]_q [10]_q$.
   - Proves exact telescopic identities $(q - q^{-1})[9]_q = q^9 - q^{-9}$ and
     $(q - q^{-1})[10]_q = q^{10} - q^{-10}$, `HasDerivAt` differentiability with sharp lower
     bound $C'(q) \ge 90 > 0$ for all $q \ge 1$ (attained at $q = 1$), finite-increment bound
     $90(q_2 - q_1) \le C(q_2) - C(q_1)$ for $1 \le q_1 < q_2$, and the exact two-loop counterterm
     identity $T(q_2) + \Delta_2 = T(q_1) \iff \Delta_2 = -(C(q_2) - C(q_1))$.
-/

namespace QOU.StandardModel.PhotonDysonHabiroAndTwoLoopStructure

-- ============================================================================
-- § 1. 1PI Photon Dyson Resummation & Uniqueness of Form B over Form A
-- ============================================================================

section DysonResummation

/-- Hecke skew parameter $h(q) = q - q^{-1}$. -/
noncomputable def heckeSkew (q : ℝ) : ℝ :=
  q - q⁻¹

/-- Shared Bring harmonic-1-form Habiro normalisation $H(q) = \frac{q + q^{-1}}{8\pi}$. -/
noncomputable def habiroNorm (q : ℝ) : ℝ :=
  (q + q⁻¹) / (8 * Real.pi)

/-- Resummed 1PI Dyson geometric photon self-energy kernel
$\Sigma_{\mathrm{Dyson}}(H, h, \alpha) = \frac{\alpha H}{1 + h^2 \alpha}$. -/
noncomputable def sigmaDyson (H h α : ℝ) : ℝ :=
  (α * H) / (1 + h ^ 2 * α)

/-- Leading 1-loop Form-A self-energy $\Sigma_A(H, \alpha) = \alpha H$. -/
def sigmaFormA (H α : ℝ) : ℝ :=
  α * H

/-- Truncated 1-loop Form-B Schwinger–Habiro self-energy
$\Sigma_B(H, h, \alpha) = \alpha H(1 - h^2 \alpha)$. -/
def sigmaFormB (H h α : ℝ) : ℝ :=
  α * H * (1 - h ^ 2 * α)

/-- **Exact Algebraic Dyson Truncation Identities:**
Whenever $1 + h^2 \alpha \neq 0$, Form B matches the resummed 1PI Dyson geometric series through
$O(\alpha^2)$ with exact cubic remainder $\frac{h^4 H \alpha^3}{1 + h^2 \alpha}$, whereas Form A
misses the $-h^2 H \alpha^2$ Dyson self-insertion. -/
theorem dyson_truncation_identities {H h α : ℝ} (hden : 1 + h ^ 2 * α ≠ 0) :
    sigmaDyson H h α - sigmaFormB H h α = (h ^ 4 * H * α ^ 3) / (1 + h ^ 2 * α) ∧
      sigmaDyson H h α - sigmaFormA H α = -(h ^ 2 * H * α ^ 2) / (1 + h ^ 2 * α) := by
  unfold sigmaDyson sigmaFormB sigmaFormA
  refine ⟨?_, ?_⟩
  · calc
      α * H / (1 + h ^ 2 * α) - α * H * (1 - h ^ 2 * α) =
          (α * H - α * H * (1 - h ^ 2 * α) * (1 + h ^ 2 * α)) / (1 + h ^ 2 * α) := by
        rw [sub_div, mul_div_cancel_right₀ _ hden]
      _ = (h ^ 4 * H * α ^ 3) / (1 + h ^ 2 * α) := by ring
  · calc
      α * H / (1 + h ^ 2 * α) - α * H =
          (α * H - α * H * (1 + h ^ 2 * α)) / (1 + h ^ 2 * α) := by
        rw [sub_div, mul_div_cancel_right₀ _ hden]
      _ = -(h ^ 2 * H * α ^ 2) / (1 + h ^ 2 * α) := by ring

/-- **Strict Ordering & Cubic Remainder Bound ($\Sigma_B < \Sigma_{\mathrm{Dyson}} < \Sigma_A$):**
For $H > 0$, $h \neq 0$, and $\alpha > 0$:
1. $\Sigma_B(H, h, \alpha) < \Sigma_{\mathrm{Dyson}}(H, h, \alpha) < \Sigma_A(H, \alpha)$,
2. $0 < \Sigma_{\mathrm{Dyson}}(H, h, \alpha) - \Sigma_B(H, h, \alpha) < h^4 H \alpha^3$,
3. On the physical regime $H \le \frac{1}{10}$, $|h| \le \frac{22}{100}$, $\alpha \le \frac{1}{137}$,
   the resummed-vs-Form-B difference satisfies $\Sigma_{\mathrm{Dyson}} - \Sigma_B < 10^{-10}$. -/
theorem dyson_strict_ordering_and_cubic_bound
    {H h α : ℝ} (hH : 0 < H) (hh : h ≠ 0) (hα : 0 < α) :
    sigmaFormB H h α < sigmaDyson H h α ∧
      sigmaDyson H h α < sigmaFormA H α ∧
      0 < sigmaDyson H h α - sigmaFormB H h α ∧
      sigmaDyson H h α - sigmaFormB H h α < h ^ 4 * H * α ^ 3 ∧
      (H ≤ 1 / 10 → |h| ≤ 22 / 100 → α ≤ 1 / 137 →
        sigmaDyson H h α - sigmaFormB H h α < (10 : ℝ) ^ (-10 : ℤ)) := by
  have hh2_pos : 0 < h ^ 2 := sq_pos_of_ne_zero hh
  have hh4_pos : 0 < h ^ 4 := by
    have h4eq : h ^ 4 = (h ^ 2) ^ 2 := by ring
    rw [h4eq]
    exact sq_pos_of_pos hh2_pos
  have hden_gt_one : 1 < 1 + h ^ 2 * α := by
    have hp : 0 < h ^ 2 * α := mul_pos hh2_pos hα
    linarith
  have hden_pos : 0 < 1 + h ^ 2 * α := lt_trans zero_lt_one hden_gt_one
  have hden_ne : 1 + h ^ 2 * α ≠ 0 := ne_of_gt hden_pos
  have hid := dyson_truncation_identities (H := H) hden_ne
  have hnumB_pos : 0 < h ^ 4 * H * α ^ 3 :=
    mul_pos (mul_pos hh4_pos hH) (pow_pos hα 3)
  have hdiffB_pos : 0 < sigmaDyson H h α - sigmaFormB H h α := by
    rw [hid.1]
    exact div_pos hnumB_pos hden_pos
  have hdiffB_lt : sigmaDyson H h α - sigmaFormB H h α < h ^ 4 * H * α ^ 3 := by
    rw [hid.1]
    exact div_lt_self hnumB_pos hden_gt_one
  have hdiffA_neg : sigmaDyson H h α - sigmaFormA H α < 0 := by
    rw [hid.2]
    have hnumA_pos : 0 < h ^ 2 * H * α ^ 2 :=
      mul_pos (mul_pos hh2_pos hH) (sq_pos_of_pos hα)
    exact div_neg_of_neg_of_pos (neg_neg_of_pos hnumA_pos) hden_pos
  refine ⟨by linarith, by linarith, hdiffB_pos, hdiffB_lt, ?_⟩
  intro hH_le hh_le hα_le
  have hh4_le : h ^ 4 ≤ (22 / 100 : ℝ) ^ 4 := by
    have habs4 : |h| ^ 4 = h ^ 4 := by
      calc
        |h| ^ 4 = (|h| ^ 2) ^ 2 := by ring
        _ = (h ^ 2) ^ 2 := by rw [sq_abs]
        _ = h ^ 4 := by ring
    rw [← habs4]
    exact pow_le_pow_left₀ (abs_nonneg h) hh_le 4
  have hα3_le : α ^ 3 ≤ (1 / 137 : ℝ) ^ 3 :=
    pow_le_pow_left₀ (le_of_lt hα) hα_le 3
  have hprod_le : h ^ 4 * H * α ^ 3 ≤ (22 / 100 : ℝ) ^ 4 * (1 / 10) * (1 / 137) ^ 3 := by
    have hp1 : h ^ 4 * H ≤ (22 / 100 : ℝ) ^ 4 * (1 / 10) :=
      mul_le_mul hh4_le hH_le (le_of_lt hH) (by norm_num)
    exact mul_le_mul hp1 hα3_le (pow_nonneg (le_of_lt hα) 3) (by norm_num)
  have hnum_lt : (22 / 100 : ℝ) ^ 4 * (1 / 10) * (1 / 137) ^ 3 < (10 : ℝ) ^ (-10 : ℤ) := by
    norm_num
  exact lt_trans (lt_of_lt_of_le hdiffB_lt hprod_le) hnum_lt

/-- **Exact Bar-Invariance ($q \mapsto q^{-1}$) of $h(q)^2$, $H(q)$, $\Sigma_{\mathrm{Dyson}}$, and $\Sigma_B$:**
Although $h(q^{-1}) = -h(q)$ is bar-odd, $h(q)^2$, $H(q)$, $\Sigma_{\mathrm{Dyson}}$, and $\Sigma_B$
are strictly bar-even for all $q, \alpha \in \mathbb{R}$. -/
theorem dyson_bar_invariance (q α : ℝ) :
    heckeSkew q⁻¹ = -heckeSkew q ∧
      (heckeSkew q⁻¹) ^ 2 = (heckeSkew q) ^ 2 ∧
      habiroNorm q⁻¹ = habiroNorm q ∧
      sigmaDyson (habiroNorm q⁻¹) (heckeSkew q⁻¹) α =
        sigmaDyson (habiroNorm q) (heckeSkew q) α ∧
      sigmaFormB (habiroNorm q⁻¹) (heckeSkew q⁻¹) α =
        sigmaFormB (habiroNorm q) (heckeSkew q) α := by
  have hskew : heckeSkew q⁻¹ = -heckeSkew q := by
    unfold heckeSkew
    rw [inv_inv]
    ring
  have hsq : (heckeSkew q⁻¹) ^ 2 = (heckeSkew q) ^ 2 := by
    rw [hskew]
    ring
  have hhab : habiroNorm q⁻¹ = habiroNorm q := by
    unfold habiroNorm
    rw [inv_inv, add_comm]
  refine ⟨hskew, hsq, hhab, ?_, ?_⟩
  · unfold sigmaDyson
    rw [hhab, hsq]
  · unfold sigmaFormB
    rw [hhab, hsq]

end DysonResummation

-- ============================================================================
-- § 2. Level-4 Quartic Schwinger Fixed Point (`qou-l4t2`) & Root Ordering
-- ============================================================================

section QuarticFixedPoint

/-- Level-4 two-loop quartic fixed-point polynomial (`qou-l4t2`):
$P_4(T, H, h, c_2; \alpha) = c_2 \alpha^4 - H h^2 \alpha^3 + H \alpha^2 + T \alpha - 1$. -/
def quarticFixedPoint (T H h c₂ α : ℝ) : ℝ :=
  c₂ * α ^ 4 - H * h ^ 2 * α ^ 3 + H * α ^ 2 + T * α - 1

/-- Exact derivative of `quarticFixedPoint` with respect to $\alpha$:
$P_4'(T, H, h, c_2; \alpha) = 4 c_2 \alpha^3 - 3 H h^2 \alpha^2 + 2 H \alpha + T$. -/
def quarticFixedPointDeriv (T H h c₂ α : ℝ) : ℝ :=
  4 * c₂ * α ^ 3 - 3 * H * h ^ 2 * α ^ 2 + 2 * H * α + T

/-- Cleared resummed rational Dyson quadratic:
$P_{\mathrm{resum}}(T, H, h; \alpha) = (T \alpha - 1)(1 + h^2 \alpha) + H \alpha^2$. -/
def resummedDysonPoly (T H h α : ℝ) : ℝ :=
  (T * α - 1) * (1 + h ^ 2 * α) + H * α ^ 2

/-- Form-A quadratic fixed-point polynomial:
$P_{\mathrm{FormA}}(T, H; \alpha) = H \alpha^2 + T \alpha - 1$. -/
def formAPoly (T H α : ℝ) : ℝ :=
  H * α ^ 2 + T * α - 1

/-- Algebraic polynomial identities connecting Form A, Resummed Dyson, and Form B (`c₂ = 0`):
1. $P_{\mathrm{resum}}(T, H, h; \alpha) = (T h^2 + H)\alpha^2 + (T - h^2)\alpha - 1$,
2. $P_{\mathrm{resum}}(T, H, h; \alpha) = (1 + h^2 \alpha)\, P_4(T, H, h, 0; \alpha) + H h^4 \alpha^4$,
3. $(1 + h^2 \alpha)\, P_{\mathrm{FormA}}(T, H; \alpha) = P_{\mathrm{resum}}(T, H, h; \alpha) + H h^2 \alpha^3$,
4. For $\alpha \neq 0$ and $1 + h^2\alpha \neq 0$, $P_{\mathrm{resum}}(T, H, h; \alpha) = 0 \iff \alpha^{-1} = T + \Sigma_{\mathrm{Dyson}}(H, h, \alpha)$. -/
theorem resummedDysonPoly_identities (T H h α : ℝ) :
    resummedDysonPoly T H h α = (T * h ^ 2 + H) * α ^ 2 + (T - h ^ 2) * α - 1 ∧
      resummedDysonPoly T H h α =
        (1 + h ^ 2 * α) * quarticFixedPoint T H h 0 α + H * h ^ 4 * α ^ 4 ∧
      (1 + h ^ 2 * α) * formAPoly T H α =
        resummedDysonPoly T H h α + H * h ^ 2 * α ^ 3 ∧
      (α ≠ 0 → 1 + h ^ 2 * α ≠ 0 →
        (resummedDysonPoly T H h α = 0 ↔ α⁻¹ = T + sigmaDyson H h α)) := by
  refine ⟨by unfold resummedDysonPoly; ring,
    by unfold resummedDysonPoly quarticFixedPoint; ring,
    by unfold resummedDysonPoly formAPoly; ring, ?_⟩
  intro hα hden
  unfold resummedDysonPoly sigmaDyson
  have hprod_ne : α * (1 + h ^ 2 * α) ≠ 0 := mul_ne_zero hα hden
  have hkey : (T + α * H / (1 + h ^ 2 * α) - α⁻¹) * (α * (1 + h ^ 2 * α)) =
      (T * α - 1) * (1 + h ^ 2 * α) + H * α ^ 2 := by
    have h1 : α⁻¹ * (α * (1 + h ^ 2 * α)) = 1 + h ^ 2 * α := by
      rw [← mul_assoc, inv_mul_cancel₀ hα, one_mul]
    have h2 : (α * H / (1 + h ^ 2 * α)) * (α * (1 + h ^ 2 * α)) = H * α ^ 2 := by
      calc
        (α * H / (1 + h ^ 2 * α)) * (α * (1 + h ^ 2 * α)) =
            ((α * H / (1 + h ^ 2 * α)) * (1 + h ^ 2 * α)) * α := by ring
        _ = (α * H) * α := by rw [div_mul_cancel₀ _ hden]
        _ = H * α ^ 2 := by ring
    calc
      (T + α * H / (1 + h ^ 2 * α) - α⁻¹) * (α * (1 + h ^ 2 * α)) =
          T * (α * (1 + h ^ 2 * α)) + (α * H / (1 + h ^ 2 * α)) * (α * (1 + h ^ 2 * α)) -
            α⁻¹ * (α * (1 + h ^ 2 * α)) := by ring
      _ = T * (α * (1 + h ^ 2 * α)) + H * α ^ 2 - (1 + h ^ 2 * α) := by rw [h1, h2]
      _ = (T * α - 1) * (1 + h ^ 2 * α) + H * α ^ 2 := by ring
  rw [← hkey, mul_eq_zero]
  constructor
  · rintro (h0 | hbad)
    · linarith
    · exact absurd hbad hprod_ne
  · intro hfp
    exact Or.inl (by linarith)

/-- **Exact `HasDerivAt`, Strict Derivative Positivity (`P_4' > 99 > 0`), & Divided-Difference
Strict Monotonicity on `[0, 1/T]`:**
Whenever $T \ge 100$, $0 \le H \le 1$, $h^2 \le 1$, and $|c_2| \le 1$:
1. `HasDerivAt (quarticFixedPoint T H h c₂) (quarticFixedPointDeriv T H h c₂ α) α` for all $\alpha \in \mathbb{R}$,
2. $99 < P_4'(\alpha)$ (hence $0 < P_4'(\alpha)$) for every $\alpha \in [0, 1/T]$,
3. $99(\beta - \alpha) < P_4(\beta) - P_4(\alpha)$ for every $0 \le \alpha < \beta \le 1/T$. -/
theorem quarticFixedPoint_deriv_pos_and_strictMonoOn
    {T H h c₂ : ℝ}
    (hT : 100 ≤ T) (hH0 : 0 ≤ H) (hH1 : H ≤ 1) (hh1 : h ^ 2 ≤ 1) (hc2 : |c₂| ≤ 1) :
    (∀ α : ℝ, HasDerivAt (quarticFixedPoint T H h c₂)
      (quarticFixedPointDeriv T H h c₂ α) α) ∧
      (∀ α : ℝ, 0 ≤ α → α ≤ 1 / T → 99 < quarticFixedPointDeriv T H h c₂ α) ∧
      (∀ α β : ℝ, 0 ≤ α → α < β → β ≤ 1 / T →
        99 * (β - α) < quarticFixedPoint T H h c₂ β - quarticFixedPoint T H h c₂ α) := by
  have hc2_lo : -1 ≤ c₂ := (abs_le.mp hc2).1
  have h1T_le : 1 / T ≤ 1 / 100 :=
    one_div_le_one_div_of_le (by norm_num) hT
  have hderiv : ∀ α : ℝ, HasDerivAt (quarticFixedPoint T H h c₂)
      (quarticFixedPointDeriv T H h c₂ α) α := by
    intro α
    unfold quarticFixedPoint quarticFixedPointDeriv
    have hp4 : HasDerivAt (fun x : ℝ => c₂ * x ^ 4) (c₂ * (4 * α ^ 3)) α :=
      (hasDerivAt_pow 4 α).const_mul c₂
    have hp3 : HasDerivAt (fun x : ℝ => (H * h ^ 2) * x ^ 3) ((H * h ^ 2) * (3 * α ^ 2)) α :=
      (hasDerivAt_pow 3 α).const_mul (H * h ^ 2)
    have hp2 : HasDerivAt (fun x : ℝ => H * x ^ 2) (H * (2 * α ^ 1)) α :=
      (hasDerivAt_pow 2 α).const_mul H
    have hp1 : HasDerivAt (fun x : ℝ => T * x) (T * 1) α :=
      (hasDerivAt_id α).const_mul T
    have hp0 : HasDerivAt (fun _ : ℝ => (1 : ℝ)) 0 α := hasDerivAt_const α 1
    convert (((hp4.sub hp3).add hp2).add hp1).sub hp0 using 1
    ring
  have hd_gt : ∀ α : ℝ, 0 ≤ α → α ≤ 1 / T → 99 < quarticFixedPointDeriv T H h c₂ α := by
    intro α hα0 hαT
    have hα_le : α ≤ 1 / 100 := le_trans hαT h1T_le
    have hα2_le : α ^ 2 ≤ (1 / 100 : ℝ) ^ 2 := pow_le_pow_left₀ hα0 hα_le 2
    have hα3_nonneg : 0 ≤ α ^ 3 := pow_nonneg hα0 3
    have hα3_le : α ^ 3 ≤ (1 / 100 : ℝ) ^ 3 := pow_le_pow_left₀ hα0 hα_le 3
    have hc2_term : -4 * (1 / 100 : ℝ) ^ 3 ≤ 4 * c₂ * α ^ 3 := by
      have h1 : -α ^ 3 ≤ c₂ * α ^ 3 := by nlinarith
      linarith
    have hh_nonneg : 0 ≤ H * h ^ 2 := mul_nonneg hH0 (sq_nonneg h)
    have hh_le_one : H * h ^ 2 ≤ 1 := by nlinarith [sq_nonneg h]
    have h3_term : 3 * H * h ^ 2 * α ^ 2 ≤ 3 * (1 / 100 : ℝ) ^ 2 := by
      nlinarith [sq_nonneg α]
    have h2_term : 0 ≤ 2 * H * α := by positivity
    unfold quarticFixedPointDeriv
    linarith
  have hmono : ∀ α β : ℝ, 0 ≤ α → α < β → β ≤ 1 / T →
      99 * (β - α) < quarticFixedPoint T H h c₂ β - quarticFixedPoint T H h c₂ α := by
    intro α β hα0 hαβ hβT
    have hβ0 : 0 ≤ β := le_trans hα0 (le_of_lt hαβ)
    have hβ_le : β ≤ 1 / 100 := le_trans hβT h1T_le
    have hα_le : α ≤ 1 / 100 := le_trans (le_of_lt hαβ) hβ_le
    have hfac : quarticFixedPoint T H h c₂ β - quarticFixedPoint T H h c₂ α =
        (β - α) * (c₂ * (α ^ 3 + α ^ 2 * β + α * β ^ 2 + β ^ 3) -
          H * h ^ 2 * (α ^ 2 + α * β + β ^ 2) + H * (α + β) + T) := by
      unfold quarticFixedPoint
      ring
    have hsum3_nonneg : 0 ≤ α ^ 3 + α ^ 2 * β + α * β ^ 2 + β ^ 3 := by positivity
    have hsum3_le : α ^ 3 + α ^ 2 * β + α * β ^ 2 + β ^ 3 ≤ 4 * (1 / 100 : ℝ) ^ 3 := by
      have h1 : α ^ 3 ≤ (1 / 100 : ℝ) ^ 3 := pow_le_pow_left₀ hα0 hα_le 3
      have h2 : β ^ 3 ≤ (1 / 100 : ℝ) ^ 3 := pow_le_pow_left₀ hβ0 hβ_le 3
      have h3 : α ^ 2 * β ≤ (1 / 100 : ℝ) ^ 3 := by
        calc
          α ^ 2 * β ≤ (1 / 100 : ℝ) ^ 2 * (1 / 100) :=
            mul_le_mul (pow_le_pow_left₀ hα0 hα_le 2) hβ_le hβ0 (by norm_num)
          _ = (1 / 100 : ℝ) ^ 3 := by ring
      have h4 : α * β ^ 2 ≤ (1 / 100 : ℝ) ^ 3 := by
        calc
          α * β ^ 2 ≤ (1 / 100 : ℝ) * (1 / 100) ^ 2 :=
            mul_le_mul hα_le (pow_le_pow_left₀ hβ0 hβ_le 2) (sq_nonneg β) (by norm_num)
          _ = (1 / 100 : ℝ) ^ 3 := by ring
      linarith
    have hsum2_nonneg : 0 ≤ α ^ 2 + α * β + β ^ 2 := by positivity
    have hsum2_le : α ^ 2 + α * β + β ^ 2 ≤ 3 * (1 / 100 : ℝ) ^ 2 := by
      have h1 : α ^ 2 ≤ (1 / 100 : ℝ) ^ 2 := pow_le_pow_left₀ hα0 hα_le 2
      have h2 : β ^ 2 ≤ (1 / 100 : ℝ) ^ 2 := pow_le_pow_left₀ hβ0 hβ_le 2
      have h3 : α * β ≤ (1 / 100 : ℝ) ^ 2 := by
        calc
          α * β ≤ (1 / 100 : ℝ) * (1 / 100) := mul_le_mul hα_le hβ_le hβ0 (by norm_num)
          _ = (1 / 100 : ℝ) ^ 2 := by ring
      linarith
    have hc2_q : -4 * (1 / 100 : ℝ) ^ 3 ≤ c₂ * (α ^ 3 + α ^ 2 * β + α * β ^ 2 + β ^ 3) := by
      have h1 : -(α ^ 3 + α ^ 2 * β + α * β ^ 2 + β ^ 3) ≤
          c₂ * (α ^ 3 + α ^ 2 * β + α * β ^ 2 + β ^ 3) := by nlinarith
      linarith
    have hh_le_one : H * h ^ 2 ≤ 1 := by nlinarith [sq_nonneg h]
    have hh_q : H * h ^ 2 * (α ^ 2 + α * β + β ^ 2) ≤ 3 * (1 / 100 : ℝ) ^ 2 := by
      nlinarith
    have hH_lin : 0 ≤ H * (α + β) := by positivity
    have hQ_gt : 99 < c₂ * (α ^ 3 + α ^ 2 * β + α * β ^ 2 + β ^ 3) -
        H * h ^ 2 * (α ^ 2 + α * β + β ^ 2) + H * (α + β) + T := by
      linarith
    rw [hfac, mul_comm 99 (β - α)]
    exact mul_lt_mul_of_pos_left hQ_gt (sub_pos.mpr hαβ)
  exact ⟨hderiv, hd_gt, hmono⟩

/-- **Existence & Uniqueness of the Physical Quartic Schwinger Root (`qou-l4t2`):**
Under $T \ge 100$, $0 < H \le 1$, $h^2 \le 1$, $|c_2| \le 1$, and $-H T (T - h^2) < c_2$
(which holds automatically whenever $c_2 \ge 0$, or whenever $H \ge \frac{1}{100}$ and $|c_2| \le 1$):
1. $P_4(0) = -1 < 0$ and $0 < P_4(1/T)$,
2. There exists a **unique** physical root $\alpha_\star \in (0, 1/T)$ with $P_4(\alpha_\star) = 0$. -/
theorem quarticFixedPoint_exists_unique_root
    {T H h c₂ : ℝ}
    (hT : 100 ≤ T) (hH0 : 0 < H) (hH1 : H ≤ 1)
    (hh1 : h ^ 2 ≤ 1) (hc2 : |c₂| ≤ 1)
    (htop : -H * T * (T - h ^ 2) < c₂) :
    quarticFixedPoint T H h c₂ 0 = -1 ∧
      0 < quarticFixedPoint T H h c₂ (1 / T) ∧
      ∃! α : ℝ, (0 < α ∧ α < 1 / T) ∧ quarticFixedPoint T H h c₂ α = 0 := by
  have hT_pos : 0 < T := by linarith
  have hT_ne : T ≠ 0 := ne_of_gt hT_pos
  have h1T_pos : 0 < 1 / T := one_div_pos.mpr hT_pos
  have h0_eq : quarticFixedPoint T H h c₂ 0 = -1 := by
    unfold quarticFixedPoint; norm_num
  have h1T_pos_val : 0 < quarticFixedPoint T H h c₂ (1 / T) := by
    have heq : quarticFixedPoint T H h c₂ (1 / T) =
        (c₂ + H * T * (T - h ^ 2)) / T ^ 4 := by
      unfold quarticFixedPoint
      field_simp [hT_ne]
      ring
    rw [heq]
    exact div_pos (by linarith) (pow_pos hT_pos 4)
  refine ⟨h0_eq, h1T_pos_val, ?_⟩
  have hcont : Continuous (quarticFixedPoint T H h c₂) := by
    unfold quarticFixedPoint
    continuity
  have hivt := intermediate_value_Icc (le_of_lt h1T_pos) hcont.continuousOn
  have hzero_mem : (0 : ℝ) ∈ Set.Icc
      (quarticFixedPoint T H h c₂ 0) (quarticFixedPoint T H h c₂ (1 / T)) :=
    ⟨by linarith [h0_eq], le_of_lt h1T_pos_val⟩
  rcases hivt hzero_mem with ⟨αStar, hmem, hroot⟩
  have hα0_lt : 0 < αStar := by
    rcases eq_or_lt_of_le hmem.1 with rfl | hlt
    · linarith [h0_eq, hroot]
    · exact hlt
  have hα1T_lt : αStar < 1 / T := by
    rcases lt_or_eq_of_le hmem.2 with hlt | rfl
    · exact hlt
    · linarith [h1T_pos_val, hroot]
  have hmono := (quarticFixedPoint_deriv_pos_and_strictMonoOn hT (le_of_lt hH0) hH1 hh1 hc2).2.2
  refine ⟨αStar, ⟨⟨hα0_lt, hα1T_lt⟩, hroot⟩, ?_⟩
  rintro α' ⟨⟨hα'0, hα'1T⟩, hroot'⟩
  rcases lt_trichotomy α' αStar with hlt | heq | hgt
  · have hdiff := hmono α' αStar (le_of_lt hα'0) hlt (le_of_lt hα1T_lt)
    linarith [sub_pos.mpr hlt]
  · exact heq
  · have hdiff := hmono αStar α' (le_of_lt hα0_lt) hgt (le_of_lt hα'1T)
    linarith [sub_pos.mpr hgt]

/-- **Comparative Inverse-Root Ordering ($\alpha_{\mathrm{FormB}}^{-1} < \alpha_{\mathrm{resum}}^{-1} < \alpha_{\mathrm{FormA}}^{-1}$)
& Monotone Two-Loop Sign Law in $c_2$ (`qou-l4t2`):**
Under $T \ge 100$, $0 < H \le 1$, $0 < h^2 \le 1$, and $|c_2| \le 1$:
1. For any positive roots $\alpha_A, \alpha_{\mathrm{resum}}, \alpha_B > 0$ satisfying
   $P_{\mathrm{FormA}}(T, H; \alpha_A) = 0$,
   $P_{\mathrm{resum}}(T, H, h; \alpha_{\mathrm{resum}}) = 0$, and
   $P_4(T, H, h, 0; \alpha_B) = 0$:
   $$\alpha_A < \alpha_{\mathrm{resum}} < \alpha_B \quad\text{and}\quad
     \alpha_B^{-1} < \alpha_{\mathrm{resum}}^{-1} < \alpha_A^{-1}.$$
2. For any physical roots $\alpha_B, \alpha_4 \in (0, 1/T)$ satisfying
   $P_4(T, H, h, 0; \alpha_B) = 0$ and $P_4(T, H, h, c_2; \alpha_4) = 0$:
   - $c_2 > 0 \implies \alpha_B^{-1} < \alpha_4^{-1}$ (positive $c_2$ increases $\alpha^{-1}$),
   - $c_2 < 0 \implies \alpha_4^{-1} < \alpha_B^{-1}$ (negative $c_2$ decreases $\alpha^{-1}$). -/
theorem fixedPoint_comparative_root_ordering_and_c2_sign
    {T H h c₂ αA αResum αB α4 : ℝ}
    (hT : 100 ≤ T) (hH0 : 0 < H) (hH1 : H ≤ 1)
    (hh_pos : 0 < h ^ 2) (hh1 : h ^ 2 ≤ 1) (hc2 : |c₂| ≤ 1)
    (hαA_pos : 0 < αA) (hA_root : formAPoly T H αA = 0)
    (hαR_pos : 0 < αResum) (hR_root : resummedDysonPoly T H h αResum = 0)
    (hαB_pos : 0 < αB) (hαB_hi : αB < 1 / T) (hB_root : quarticFixedPoint T H h 0 αB = 0)
    (hα4_pos : 0 < α4) (hα4_hi : α4 < 1 / T) (h4_root : quarticFixedPoint T H h c₂ α4 = 0) :
    (αA < αResum ∧ αResum < αB ∧ αB⁻¹ < αResum⁻¹ ∧ αResum⁻¹ < αA⁻¹) ∧
      (0 < c₂ → αB⁻¹ < α4⁻¹) ∧
      (c₂ < 0 → α4⁻¹ < αB⁻¹) := by
  have hidB := (resummedDysonPoly_identities T H h αB).2.1
  have hidA := (resummedDysonPoly_identities T H h αResum).2.2.1
  have hR_at_B : 0 < resummedDysonPoly T H h αB := by
    rw [hidB, hB_root, mul_zero, zero_add]
    have hh4_pos : 0 < h ^ 4 := by
      have : h ^ 4 = (h ^ 2) ^ 2 := by ring
      rw [this]; exact sq_pos_of_pos hh_pos
    exact mul_pos (mul_pos hH0 hh4_pos) (pow_pos hαB_pos 4)
  have hR_lt_B : αResum < αB := by
    by_contra hge
    push_neg at hge
    have hexpR := (resummedDysonPoly_identities T H h αResum).1
    have hexpB := (resummedDysonPoly_identities T H h αB).1
    have hdiff : resummedDysonPoly T H h αResum - resummedDysonPoly T H h αB =
        (αResum - αB) * ((T * h ^ 2 + H) * (αResum + αB) + (T - h ^ 2)) := by
      rw [hexpR, hexpB]; ring
    have hcoef1_pos : 0 < T * h ^ 2 + H := by nlinarith
    have hcoef2_pos : 0 < T - h ^ 2 := by linarith
    have hfactor_pos : 0 < (T * h ^ 2 + H) * (αResum + αB) + (T - h ^ 2) :=
      add_pos (mul_pos hcoef1_pos (add_pos hαR_pos hαB_pos)) hcoef2_pos
    have hnonneg : 0 ≤ resummedDysonPoly T H h αResum - resummedDysonPoly T H h αB := by
      rw [hdiff]
      exact mul_nonneg (sub_nonneg.mpr hge) (le_of_lt hfactor_pos)
    linarith [hR_root, hR_at_B]
  have hA_at_R : 0 < formAPoly T H αResum := by
    have hden_pos : 0 < 1 + h ^ 2 * αResum := by nlinarith
    have hprod_pos : 0 < (1 + h ^ 2 * αResum) * formAPoly T H αResum := by
      rw [hidA, hR_root, zero_add]
      exact mul_pos (mul_pos hH0 hh_pos) (pow_pos hαR_pos 3)
    nlinarith
  have hA_lt_R : αA < αResum := by
    by_contra hge
    push_neg at hge
    have hdiff : formAPoly T H αA - formAPoly T H αResum =
        (αA - αResum) * (H * (αA + αResum) + T) := by
      unfold formAPoly; ring
    have hfactor_pos : 0 < H * (αA + αResum) + T := by positivity
    have hnonneg : 0 ≤ formAPoly T H αA - formAPoly T H αResum := by
      rw [hdiff]
      exact mul_nonneg (sub_nonneg.mpr hge) (le_of_lt hfactor_pos)
    linarith [hA_root, hA_at_R]
  have hinv_BR : αB⁻¹ < αResum⁻¹ := inv_strictAnti₀ hαR_pos hR_lt_B
  have hinv_RA : αResum⁻¹ < αA⁻¹ := inv_strictAnti₀ hαA_pos hA_lt_R
  have hmono4 := (quarticFixedPoint_deriv_pos_and_strictMonoOn hT (le_of_lt hH0) hH1 hh1 hc2).2.2
  have hP4_at_B : quarticFixedPoint T H h c₂ αB = c₂ * αB ^ 4 := by
    have hshift : quarticFixedPoint T H h c₂ αB =
        quarticFixedPoint T H h 0 αB + c₂ * αB ^ 4 := by
      unfold quarticFixedPoint; ring
    rw [hshift, hB_root, zero_add]
  refine ⟨⟨hA_lt_R, hR_lt_B, hinv_BR, hinv_RA⟩, ?_, ?_⟩
  · intro hc2_pos
    have hpos_B : 0 < quarticFixedPoint T H h c₂ αB := by
      rw [hP4_at_B]
      exact mul_pos hc2_pos (pow_pos hαB_pos 4)
    have h4_lt_B : α4 < αB := by
      by_contra hge
      push_neg at hge
      rcases eq_or_lt_of_le hge with rfl | hlt
      · linarith [h4_root, hpos_B]
      · have hd := hmono4 αB α4 (le_of_lt hαB_pos) hlt (le_of_lt hα4_hi)
        linarith [sub_pos.mpr hlt, h4_root, hpos_B]
    exact inv_strictAnti₀ hα4_pos h4_lt_B
  · intro hc2_neg
    have hneg_B : quarticFixedPoint T H h c₂ αB < 0 := by
      rw [hP4_at_B]
      exact mul_neg_of_neg_of_pos hc2_neg (pow_pos hαB_pos 4)
    have hB_lt_4 : αB < α4 := by
      by_contra hge
      push_neg at hge
      rcases eq_or_lt_of_le hge with rfl | hlt
      · linarith [h4_root, hneg_B]
      · have hd := hmono4 α4 αB (le_of_lt hα4_pos) hlt (le_of_lt hαB_hi)
        linarith [sub_pos.mpr hlt, h4_root, hneg_B]
    exact inv_strictAnti₀ hαB_pos hB_lt_4

end QuarticFixedPoint

-- ============================================================================
-- § 3. Tree-Complexity Derivative C'(q) ≥ 90 > 0 & Counterterm Equivalence
-- ============================================================================

section TreeComplexityMonotonicity

/-- Symmetric Laurent pair $f_k(q) = q^k + (q^k)^{-1}$. -/
noncomputable def symLaurent (k : ℕ) (q : ℝ) : ℝ :=
  q ^ k + (q ^ k)⁻¹

/-- Derivative of `symLaurent k` at $q \neq 0$:
$f_k'(q) = k q^{k-1} - \frac{k q^{k-1}}{(q^k)^2}$. -/
noncomputable def symLaurentDeriv (k : ℕ) (q : ℝ) : ℝ :=
  (k : ℝ) * q ^ (k - 1) - ((k : ℝ) * q ^ (k - 1)) / (q ^ k) ^ 2

/-- Singularity-free balanced quantum integer $[9]_q = \sum_{j=0}^8 q^{8 - 2j}$. -/
noncomputable def qBal9 (q : ℝ) : ℝ :=
  1 + symLaurent 2 q + symLaurent 4 q + symLaurent 6 q + symLaurent 8 q

/-- Derivative of `qBal9`. -/
noncomputable def qBal9Deriv (q : ℝ) : ℝ :=
  symLaurentDeriv 2 q + symLaurentDeriv 4 q + symLaurentDeriv 6 q + symLaurentDeriv 8 q

/-- Singularity-free balanced quantum integer $[10]_q = \sum_{j=0}^9 q^{9 - 2j}$. -/
noncomputable def qBal10 (q : ℝ) : ℝ :=
  symLaurent 1 q + symLaurent 3 q + symLaurent 5 q + symLaurent 7 q + symLaurent 9 q

/-- Derivative of `qBal10`. -/
noncomputable def qBal10Deriv (q : ℝ) : ℝ :=
  symLaurentDeriv 1 q + symLaurentDeriv 3 q + symLaurentDeriv 5 q +
    symLaurentDeriv 7 q + symLaurentDeriv 9 q

/-- Bare electromagnetic tree complexity $C(q) = q \cdot [9]_q \cdot [10]_q$. -/
noncomputable def emTreeComplexity (q : ℝ) : ℝ :=
  q * qBal9 q * qBal10 q

/-- Exact derivative of `emTreeComplexity`:
$C'(q) = [9]_q [10]_q + q [9]_q' [10]_q + q [9]_q [10]_q'$. -/
noncomputable def emTreeComplexityDeriv (q : ℝ) : ℝ :=
  qBal9 q * qBal10 q + q * qBal9Deriv q * qBal10 q + q * qBal9 q * qBal10Deriv q

/-- Tree + Bring zero-mode constant $T_{\mathrm{EM}}(q) = C(q) + \frac{2}{3\pi}$. -/
noncomputable def emTreePlusZeroMode (q : ℝ) : ℝ :=
  emTreeComplexity q + 2 / (3 * Real.pi)

/-- Elementary `HasDerivAt`, AM-GM lower bound $f_k(q) \ge 2$, derivative non-negativity
$f_k'(q) \ge 0$ on $q \ge 1$, and monotonicity $f_k(q_1) \le f_k(q_2)$ on $1 \le q_1 \le q_2$. -/
theorem symLaurent_deriv_and_mono (k : ℕ) {q q₁ q₂ : ℝ}
    (hq : 1 ≤ q) (hq₁ : 1 ≤ q₁) (hq₁₂ : q₁ ≤ q₂) :
    2 ≤ symLaurent k q ∧
      HasDerivAt (symLaurent k) (symLaurentDeriv k q) q ∧
      0 ≤ symLaurentDeriv k q ∧
      symLaurent k q₁ ≤ symLaurent k q₂ := by
  have hq_pos : 0 < q := lt_of_lt_of_le zero_lt_one hq
  have hqk_ge : 1 ≤ q ^ k := one_le_pow₀ hq
  have hqk_pos : 0 < q ^ k := lt_of_lt_of_le zero_lt_one hqk_ge
  have hqk_ne : q ^ k ≠ 0 := ne_of_gt hqk_pos
  have hamgm : 2 ≤ symLaurent k q := by
    unfold symLaurent
    have hsq : 0 ≤ (q ^ k - 1) ^ 2 / q ^ k := div_nonneg (sq_nonneg _) (le_of_lt hqk_pos)
    have hid : q ^ k + (q ^ k)⁻¹ - 2 = (q ^ k - 1) ^ 2 / q ^ k := by
      field_simp [hqk_ne]
      ring
    linarith
  have hderiv : HasDerivAt (symLaurent k) (symLaurentDeriv k q) q := by
    unfold symLaurent symLaurentDeriv
    have hpow : HasDerivAt (fun x : ℝ => x ^ k) ((k : ℝ) * q ^ (k - 1)) q :=
      hasDerivAt_pow k q
    have hinv : HasDerivAt (fun x : ℝ => (x ^ k)⁻¹) (-((k : ℝ) * q ^ (k - 1)) / (q ^ k) ^ 2) q :=
      hpow.inv hqk_ne
    convert hpow.add hinv using 1
    ring
  have hd_nonneg : 0 ≤ symLaurentDeriv k q := by
    unfold symLaurentDeriv
    have hsq_ge : 1 ≤ (q ^ k) ^ 2 := one_le_pow₀ hqk_ge
    have hnum_nonneg : 0 ≤ (k : ℝ) * q ^ (k - 1) :=
      mul_nonneg (Nat.cast_nonneg k) (pow_nonneg (le_of_lt hq_pos) _)
    have hdiv_le : ((k : ℝ) * q ^ (k - 1)) / (q ^ k) ^ 2 ≤ (k : ℝ) * q ^ (k - 1) :=
      div_le_self hnum_nonneg hsq_ge
    linarith
  have hmono : symLaurent k q₁ ≤ symLaurent k q₂ := by
    unfold symLaurent
    have hq₁_pos : 0 < q₁ := lt_of_lt_of_le zero_lt_one hq₁
    have hq₁k_ge : 1 ≤ q₁ ^ k := one_le_pow₀ hq₁
    have hq₂k_ge : q₁ ^ k ≤ q₂ ^ k := pow_le_pow_left₀ (le_of_lt hq₁_pos) hq₁₂ k
    have hq₁k_pos : 0 < q₁ ^ k := lt_of_lt_of_le zero_lt_one hq₁k_ge
    have hq₂k_pos : 0 < q₂ ^ k := lt_of_lt_of_le hq₁k_pos hq₂k_ge
    have hprod_ge : 1 ≤ q₁ ^ k * q₂ ^ k :=
      one_le_mul_of_one_le_of_one_le hq₁k_ge (le_trans hq₁k_ge hq₂k_ge)
    have hprod_pos : 0 < q₁ ^ k * q₂ ^ k := lt_of_lt_of_le zero_lt_one hprod_ge
    have hdiff : (q₂ ^ k + (q₂ ^ k)⁻¹) - (q₁ ^ k + (q₁ ^ k)⁻¹) =
        (q₂ ^ k - q₁ ^ k) * (q₁ ^ k * q₂ ^ k - 1) / (q₁ ^ k * q₂ ^ k) := by
      field_simp [ne_of_gt hq₁k_pos, ne_of_gt hq₂k_pos]
      ring
    have hnonneg : 0 ≤ (q₂ ^ k - q₁ ^ k) * (q₁ ^ k * q₂ ^ k - 1) / (q₁ ^ k * q₂ ^ k) :=
      div_nonneg (mul_nonneg (by linarith) (by linarith)) (le_of_lt hprod_pos)
    linarith
  exact ⟨hamgm, hderiv, hd_nonneg, hmono⟩

/-- **Exact Telescopic Quantum-Integer Identities, Sharp Derivative Bound $C'(q) \ge 90 > 0$,
Finite-Increment Lower Bound, & Two-Loop Counterterm Equivalence:**
1. For every $q \neq 0$, $(q - q^{-1})[9]_q = q^9 - q^{-9}$ and $(q - q^{-1})[10]_q = q^{10} - q^{-10}$;
2. At $q = 1$, $C(1) = 90$ and $C'(1) = 90$;
3. For every $q \ge 1$, `HasDerivAt emTreeComplexity (emTreeComplexityDeriv q) q` and
   $90 \le C'(q)$ (hence $0 < C'(q)$);
4. For every $1 \le q_1 < q_2$, $90(q_2 - q_1) \le C(q_2) - C(q_1)$ (strictly $C(q_1) < C(q_2)$);
5. For every $q_1, q_2, \Delta_2 \in \mathbb{R}$,
   $T_{\mathrm{EM}}(q_2) + \Delta_2 = T_{\mathrm{EM}}(q_1) \iff \Delta_2 = -(C(q_2) - C(q_1))$. -/
theorem emTreeComplexity_deriv_pos_increment_and_counterterm
    {q q₁ q₂ Δ₂ : ℝ} (hq_ne : q ≠ 0) (hq : 1 ≤ q) (hq₁ : 1 ≤ q₁) (hq₁₂ : q₁ < q₂) :
    ((q - q⁻¹) * qBal9 q = q ^ 9 - (q ^ 9)⁻¹ ∧
        (q - q⁻¹) * qBal10 q = q ^ 10 - (q ^ 10)⁻¹) ∧
      (emTreeComplexity 1 = 90 ∧ emTreeComplexityDeriv 1 = 90) ∧
      (HasDerivAt emTreeComplexity (emTreeComplexityDeriv q) q ∧
        90 ≤ emTreeComplexityDeriv q ∧ 0 < emTreeComplexityDeriv q) ∧
      (90 * (q₂ - q₁) ≤ emTreeComplexity q₂ - emTreeComplexity q₁ ∧
        emTreeComplexity q₁ < emTreeComplexity q₂) ∧
      (emTreePlusZeroMode q₂ + Δ₂ = emTreePlusZeroMode q₁ ↔
        Δ₂ = -(emTreeComplexity q₂ - emTreeComplexity q₁)) := by
  have htel : (q - q⁻¹) * qBal9 q = q ^ 9 - (q ^ 9)⁻¹ ∧
      (q - q⁻¹) * qBal10 q = q ^ 10 - (q ^ 10)⁻¹ := by
    have hinv_pow : ∀ k m : ℕ, k ≤ m → (q ^ k)⁻¹ * q ^ m = q ^ (m - k) := by
      intro k m hkm
      rw [inv_mul_eq_iff_eq_mul₀ (pow_ne_zero k hq_ne), ← pow_add, Nat.add_sub_of_le hkm]
    have hq_step : (q - q⁻¹) * q = q ^ 2 - 1 := by
      rw [sub_mul, inv_mul_cancel₀ hq_ne, sq]
    refine ⟨?_, ?_⟩
    · apply mul_right_cancel₀ (pow_ne_zero 9 hq_ne)
      have h9_clear : qBal9 q * q ^ 8 =
          1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 + q ^ 14 + q ^ 16 := by
        unfold qBal9 symLaurent
        simp only [add_mul, one_mul, ← pow_add]
        rw [hinv_pow 2 8 (by omega), hinv_pow 4 8 (by omega),
          hinv_pow 6 8 (by omega), hinv_pow 8 8 (by omega)]
        norm_num
        ring
      have hlhs : ((q - q⁻¹) * qBal9 q) * q ^ 9 =
          ((q - q⁻¹) * q) * (qBal9 q * q ^ 8) := by ring
      have hrhs : (q ^ 9 - (q ^ 9)⁻¹) * q ^ 9 = q ^ 18 - 1 := by
        rw [sub_mul, inv_mul_cancel₀ (pow_ne_zero 9 hq_ne), ← pow_add]
      rw [hlhs, hq_step, h9_clear, hrhs]
      ring
    · apply mul_right_cancel₀ (pow_ne_zero 10 hq_ne)
      have h10_clear : qBal10 q * q ^ 9 =
          1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8 + q ^ 10 + q ^ 12 + q ^ 14 + q ^ 16 + q ^ 18 := by
        unfold qBal10 symLaurent
        simp only [add_mul, ← pow_add]
        rw [hinv_pow 1 9 (by omega), hinv_pow 3 9 (by omega),
          hinv_pow 5 9 (by omega), hinv_pow 7 9 (by omega), hinv_pow 9 9 (by omega)]
        norm_num
        ring
      have hlhs : ((q - q⁻¹) * qBal10 q) * q ^ 10 =
          ((q - q⁻¹) * q) * (qBal10 q * q ^ 9) := by ring
      have hrhs : (q ^ 10 - (q ^ 10)⁻¹) * q ^ 10 = q ^ 20 - 1 := by
        rw [sub_mul, inv_mul_cancel₀ (pow_ne_zero 10 hq_ne), ← pow_add]
      rw [hlhs, hq_step, h10_clear, hrhs]
      ring
  have hat1 : emTreeComplexity 1 = 90 ∧ emTreeComplexityDeriv 1 = 90 := by
    unfold emTreeComplexity emTreeComplexityDeriv qBal9 qBal10 qBal9Deriv qBal10Deriv
      symLaurent symLaurentDeriv
    norm_num
  have hd_block : HasDerivAt emTreeComplexity (emTreeComplexityDeriv q) q ∧
      90 ≤ emTreeComplexityDeriv q ∧ 0 < emTreeComplexityDeriv q := by
    have hs1 := symLaurent_deriv_and_mono 1 hq hq₁ (le_of_lt hq₁₂)
    have hs2 := symLaurent_deriv_and_mono 2 hq hq₁ (le_of_lt hq₁₂)
    have hs3 := symLaurent_deriv_and_mono 3 hq hq₁ (le_of_lt hq₁₂)
    have hs4 := symLaurent_deriv_and_mono 4 hq hq₁ (le_of_lt hq₁₂)
    have hs5 := symLaurent_deriv_and_mono 5 hq hq₁ (le_of_lt hq₁₂)
    have hs6 := symLaurent_deriv_and_mono 6 hq hq₁ (le_of_lt hq₁₂)
    have hs7 := symLaurent_deriv_and_mono 7 hq hq₁ (le_of_lt hq₁₂)
    have hs8 := symLaurent_deriv_and_mono 8 hq hq₁ (le_of_lt hq₁₂)
    have hs9 := symLaurent_deriv_and_mono 9 hq hq₁ (le_of_lt hq₁₂)
    have hd9 : HasDerivAt qBal9 (qBal9Deriv q) q := by
      unfold qBal9 qBal9Deriv
      convert ((((hasDerivAt_const q (1 : ℝ)).add hs2.2.1).add hs4.2.1).add hs6.2.1).add hs8.2.1
        using 1
      ring
    have hd10 : HasDerivAt qBal10 (qBal10Deriv q) q := by
      unfold qBal10 qBal10Deriv
      convert (((hs1.2.1.add hs3.2.1).add hs5.2.1).add hs7.2.1).add hs9.2.1 using 1
    have hdC : HasDerivAt emTreeComplexity (emTreeComplexityDeriv q) q := by
      unfold emTreeComplexity emTreeComplexityDeriv
      have hq9 : HasDerivAt (fun x : ℝ => x * qBal9 x) (1 * qBal9 q + q * qBal9Deriv q) q :=
        (hasDerivAt_id q).mul hd9
      convert hq9.mul hd10 using 1
      ring
    have h9_ge : 9 ≤ qBal9 q := by
      unfold qBal9; linarith [hs2.1, hs4.1, hs6.1, hs8.1]
    have h10_ge : 10 ≤ qBal10 q := by
      unfold qBal10; linarith [hs1.1, hs3.1, hs5.1, hs7.1, hs9.1]
    have hd9_nn : 0 ≤ qBal9Deriv q := by
      unfold qBal9Deriv; linarith [hs2.2.2.1, hs4.2.2.1, hs6.2.2.1, hs8.2.2.1]
    have hd10_nn : 0 ≤ qBal10Deriv q := by
      unfold qBal10Deriv; linarith [hs1.2.2.1, hs3.2.2.1, hs5.2.2.1, hs7.2.2.1, hs9.2.2.1]
    have hprod90 : 90 ≤ qBal9 q * qBal10 q := by
      calc
        (90 : ℝ) = 9 * 10 := by norm_num
        _ ≤ qBal9 q * qBal10 q := mul_le_mul h9_ge h10_ge (by norm_num) (by linarith)
    have ht2 : 0 ≤ q * qBal9Deriv q * qBal10 q :=
      mul_nonneg (mul_nonneg (by linarith) hd9_nn) (by linarith)
    have ht3 : 0 ≤ q * qBal9 q * qBal10Deriv q :=
      mul_nonneg (mul_nonneg (by linarith) (by linarith)) hd10_nn
    have hdC_ge : 90 ≤ emTreeComplexityDeriv q := by
      unfold emTreeComplexityDeriv
      linarith
    exact ⟨hdC, hdC_ge, lt_of_lt_of_le (by norm_num) hdC_ge⟩
  have hinc_block : 90 * (q₂ - q₁) ≤ emTreeComplexity q₂ - emTreeComplexity q₁ ∧
      emTreeComplexity q₁ < emTreeComplexity q₂ := by
    have hs1_q1 := symLaurent_deriv_and_mono 1 hq₁ hq₁ (le_of_lt hq₁₂)
    have hs2_q1 := symLaurent_deriv_and_mono 2 hq₁ hq₁ (le_of_lt hq₁₂)
    have hs3_q1 := symLaurent_deriv_and_mono 3 hq₁ hq₁ (le_of_lt hq₁₂)
    have hs4_q1 := symLaurent_deriv_and_mono 4 hq₁ hq₁ (le_of_lt hq₁₂)
    have hs5_q1 := symLaurent_deriv_and_mono 5 hq₁ hq₁ (le_of_lt hq₁₂)
    have hs6_q1 := symLaurent_deriv_and_mono 6 hq₁ hq₁ (le_of_lt hq₁₂)
    have hs7_q1 := symLaurent_deriv_and_mono 7 hq₁ hq₁ (le_of_lt hq₁₂)
    have hs8_q1 := symLaurent_deriv_and_mono 8 hq₁ hq₁ (le_of_lt hq₁₂)
    have hs9_q1 := symLaurent_deriv_and_mono 9 hq₁ hq₁ (le_of_lt hq₁₂)
    have h9_q1_ge : 9 ≤ qBal9 q₁ := by
      unfold qBal9; linarith [hs2_q1.1, hs4_q1.1, hs6_q1.1, hs8_q1.1]
    have h10_q1_ge : 10 ≤ qBal10 q₁ := by
      unfold qBal10; linarith [hs1_q1.1, hs3_q1.1, hs5_q1.1, hs7_q1.1, hs9_q1.1]
    have h9_mono : qBal9 q₁ ≤ qBal9 q₂ := by
      unfold qBal9; linarith [hs2_q1.2.2.2, hs4_q1.2.2.2, hs6_q1.2.2.2, hs8_q1.2.2.2]
    have h10_mono : qBal10 q₁ ≤ qBal10 q₂ := by
      unfold qBal10
      linarith [hs1_q1.2.2.2, hs3_q1.2.2.2, hs5_q1.2.2.2, hs7_q1.2.2.2, hs9_q1.2.2.2]
    have hprod_q1_ge : 90 ≤ qBal9 q₁ * qBal10 q₁ := by
      calc
        (90 : ℝ) = 9 * 10 := by norm_num
        _ ≤ qBal9 q₁ * qBal10 q₁ := mul_le_mul h9_q1_ge h10_q1_ge (by norm_num) (by linarith)
    have hprod_mono : qBal9 q₁ * qBal10 q₁ ≤ qBal9 q₂ * qBal10 q₂ :=
      mul_le_mul h9_mono h10_mono (by linarith) (by linarith)
    have hq₂_pos : 0 < q₂ := lt_trans (lt_of_lt_of_le zero_lt_one hq₁) hq₁₂
    have hinc : 90 * (q₂ - q₁) ≤ emTreeComplexity q₂ - emTreeComplexity q₁ := by
      unfold emTreeComplexity
      have hstep1 : q₂ * (qBal9 q₁ * qBal10 q₁) ≤ q₂ * (qBal9 q₂ * qBal10 q₂) :=
        mul_le_mul_of_nonneg_left hprod_mono (le_of_lt hq₂_pos)
      have hstep2 : (q₂ - q₁) * 90 ≤ (q₂ - q₁) * (qBal9 q₁ * qBal10 q₁) :=
        mul_le_mul_of_nonneg_left hprod_q1_ge (le_of_lt (sub_pos.mpr hq₁₂))
      linarith
    have hpos90 : 0 < 90 * (q₂ - q₁) := mul_pos (by norm_num) (sub_pos.mpr hq₁₂)
    exact ⟨hinc, by linarith⟩
  have hct : emTreePlusZeroMode q₂ + Δ₂ = emTreePlusZeroMode q₁ ↔
      Δ₂ = -(emTreeComplexity q₂ - emTreeComplexity q₁) := by
    unfold emTreePlusZeroMode
    constructor <;> intro h <;> linarith
  exact ⟨htel, hat1, hd_block, hinc_block, hct⟩

end TreeComplexityMonotonicity

end QOU.StandardModel.PhotonDysonHabiroAndTwoLoopStructure
