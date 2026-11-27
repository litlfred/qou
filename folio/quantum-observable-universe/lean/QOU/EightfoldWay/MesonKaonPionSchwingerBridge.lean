/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic.Continuity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import QOU.EightfoldWay.MesonThreeByFourCharacterization
import QOU.MassTheory.BringSchwingerNormalizationDerivation
import QOU.Transcendental.MassTheory.BringSchwingerNormalizationDerivationReal
import QOU.MassTheory.SchwingerMeasureShape

/-!
# Archimedean `m_K / m_π` Schwinger Proper-Time Decomposition, Dashen Sign Obstruction, and `§3b-cond` Bridge (`ℝ`)

This module formalizes the archimedean (`ℝ`) results of beans `qou-3l2l` and `qou-5ipv`
(Issue `#9369`), consuming `QOU.EightfoldWay.MesonThreeByFourCharacterization` via `(K := ℝ)`
instantiation per `AGENTS.md` §7c:

1. **Strict `12 < [3]_q [4]_q < [2]_q [6]_q < [1]_q [12]_q` Ordering (`twelve_factorizations_strict_ordering_real`):**
   Instantiates `twelve_factorizations_cyclotomic_gaps (K := ℝ)` to prove that for every real
   `q > 0` with `q ≠ 1`, `(3, 4)` is the strictly minimal `q`-deformed product among all
   factorizations of `12`.

2. **Schwinger Proper-Time Decomposition & Multiplicative-vs-Additive UV Gap
   (`meson_em_schwinger_proper_time_decomp`, `reeb_vs_planck_schwinger_uv_gap`):**
   - Connects `1 + Real.log (1 + hbarQ q)` to the 1-nat proper-time e-fold `[exp(-1), 1]` plus
     the additive Planck UV excursion `[1, 1 + hbarQ q]`, with `1 + hbarQ q = (2 * q - 1) / q > 0`.
   - Proves that replacing the additive UV endpoint `1 + hbarQ q` by the multiplicative Reeb step
     `q` (`[1, q]`) increases the factor by the strictly positive amount
     `(1 + Real.log q) - (1 + Real.log (1 + hbarQ q)) = -Real.log (1 - (hbarQ q) ^ 2) > 0` for `q > 1`.

3. **Dashen Chiral Sign Obstruction & Lipschitz `α_EM` Insensitivity
   (`dashen_equal_em_lowers_ratio_real`, `meson_ratio_alpha_lipschitz_bound`):**
   - Proves that for `1 < R₀`, `0 < m₀_sq`, and `0 < dEM`, `(R₀ * m₀_sq + dEM) / (m₀_sq + dEM) < R₀`
     (ruling out equal additive electromagnetic self-energies on neutral baselines as the source of
     a positive shift on `m_K² / m_π²`).
   - Proves the Lipschitz bound `|R(α₁) - R(α₂)| ≤ (F / (2 * π * √S)) * |α₁ - α₂|` for
     `R(α) = √(S + (α / π) * F)`, certifying why all loop-dressed `α_EM` derivations agree on
     `m_K / m_π` within `0.048 ppb`.

4. **`§3b-cond` Hypothesis Class & `trivialModel` Consistency Witness (`MesonKaonPionGMOREmBridgeClass`):**
   Packages the remaining physical channel-selection and worldline UV-endpoint premises with
   **zero global instances** and a constructive `def trivialModel` witness.
-/

set_option autoImplicit false

namespace QOU.EightfoldWay
namespace MesonKaonPionSchwingerBridge

open QOU.QInteger (qIntBal qIntBal_def)
open QOU.Archimedean (bringSurfaceArea bringFundamentalTriangleArea)
open QOU.Archimedean.BringSchwingerNormalizationDerivation
  (hbarQ hHecke habiroNorm IsUnifiedBringFixedPoint)
open QOU.EightfoldWay.MesonThreeByFourCharacterization
  (qIntBal_small_laurent twelve_factorizations_cyclotomic_gaps dashen_equal_em_shift_identity)

/-! ## Section 1: Strict Archimedean Ordering of `12 = a · b` Quantum-Integer Products -/

section TwelveFactorizationOrderingReal

/-- **Strict Ordering `12 < [3]_q [4]_q < [2]_q [6]_q < [1]_q [12]_q` on `(0, ∞) \ {1}`**:
For every positive real `q ≠ 1`, `(3, 4)` achieves the strict minimum among all classical
factorizations of `12`, while strictly exceeding its classical limit `12`. -/
theorem twelve_factorizations_strict_ordering_real (q : ℝ) (hq : 0 < q) (hne : q ≠ 1) :
    12 < qIntBal q 3 * qIntBal q 4 ∧
    qIntBal q 3 * qIntBal q 4 < qIntBal q 2 * qIntBal q 6 ∧
    qIntBal q 2 * qIntBal q 6 < qIntBal q 1 * qIntBal q 12 := by
  have hq_ne : q ≠ 0 := ne_of_gt hq
  have hhab_pos : 0 < q + q⁻¹ - 2 := by
    have hfac : q + q⁻¹ - 2 = (q - 1) ^ 2 / q := by field_simp; ring
    rw [hfac]
    exact div_pos (sq_pos_of_ne_zero (sub_ne_zero.mpr hne)) hq
  have hqdiff_ne : q - q⁻¹ ≠ 0 := by
    have hfac : q - q⁻¹ = (q - 1) * (q + 1) / q := by field_simp; ring
    rw [hfac]
    exact div_ne_zero (mul_ne_zero (sub_ne_zero.mpr hne) (by linarith)) hq_ne
  obtain ⟨_, hb2, hb3, hb4, hb6⟩ := qIntBal_small_laurent (K := ℝ) q hq_ne hqdiff_ne
  have hb2_gt : 2 < qIntBal q 2 := by linarith
  have hb3_gt : 3 < qIntBal q 3 := by
    have heq : qIntBal q 3 = (q - q⁻¹) ^ 2 + 3 := by
      rw [hb3]; field_simp [hq_ne]; ring
    have hsq : 0 < (q - q⁻¹) ^ 2 := sq_pos_of_ne_zero hqdiff_ne
    linarith
  have hb4_gt : 4 < qIntBal q 4 := by
    have heq : qIntBal q 4 = (q + q⁻¹) * ((q - q⁻¹) ^ 2 + 2) := by
      rw [hb4]; field_simp [hq_ne]; ring
    have hsq : 0 < (q - q⁻¹) ^ 2 := sq_pos_of_ne_zero hqdiff_ne
    have hsum_gt : 2 < q + q⁻¹ := by linarith
    rw [heq]
    nlinarith
  have hb6_pos : 0 < qIntBal q 6 := by
    rw [hb6]; positivity
  have h12_lt : 12 < qIntBal q 3 * qIntBal q 4 := by nlinarith
  obtain ⟨hgap1, hgap2⟩ := twelve_factorizations_cyclotomic_gaps (K := ℝ) q hq_ne hqdiff_ne
  have hdiff1_pos : 0 < qIntBal q 2 * qIntBal q 6 - qIntBal q 3 * qIntBal q 4 := by
    rw [hgap1]
    exact mul_pos (mul_pos (mul_pos hhab_pos (by linarith)) (by linarith)) (by linarith)
  have hdiff2_pos : 0 < qIntBal q 1 * qIntBal q 12 - qIntBal q 2 * qIntBal q 6 := by
    rw [hgap2]
    exact mul_pos (mul_pos (mul_pos hhab_pos hb6_pos) (by linarith)) (by linarith)
  exact ⟨h12_lt, by linarith, by linarith⟩

end TwelveFactorizationOrderingReal

/-! ## Section 2: Schwinger Proper-Time Decomposition, UV Endpoint Gap, Dashen Sign, & Lipschitz Bound -/

section SchwingerProperTimeAndSensitivity

/-- The untruncated electromagnetic proper-time factor `1 + log(1 + hbarQ q)`. -/
noncomputable def mesonEmProperTimeFactor (q : ℝ) : ℝ :=
  1 + Real.log (1 + hbarQ q)

/-- **Schwinger Proper-Time E-Fold Decomposition (`[exp(-1), 1] ∪ [1, 1 + hbarQ q]`)**:
For every `q > 1 / 2`:
1. `1 + hbarQ q = (2 * q - 1) / q > 0`, and
2. the logarithmic proper-time integral splits as the 1-nat infrared unit e-fold
   `log 1 - log(exp(-1)) = 1` plus the UV Planck excursion `log(1 + hbarQ q) - log 1`. -/
theorem meson_em_schwinger_proper_time_decomp (q : ℝ) (hq : 1 / 2 < q) :
    1 + hbarQ q = (2 * q - 1) / q ∧
    0 < 1 + hbarQ q ∧
    (Real.log 1 - Real.log (Real.exp (-1))) + (Real.log (1 + hbarQ q) - Real.log 1) =
      mesonEmProperTimeFactor q ∧
    mesonEmProperTimeFactor q = 1 + Real.log ((2 * q - 1) / q) := by
  have hq_pos : 0 < q := by linarith
  have hrat : 1 + hbarQ q = (2 * q - 1) / q := by
    unfold hbarQ; field_simp; ring
  have hpos : 0 < 1 + hbarQ q := by
    rw [hrat]; exact div_pos (by linarith) hq_pos
  refine ⟨hrat, hpos, ?_, ?_⟩
  · unfold mesonEmProperTimeFactor
    rw [Real.log_one, Real.log_exp]
    ring
  · unfold mesonEmProperTimeFactor
    rw [hrat]

/-- **Multiplicative Reeb `[1, q]` vs Additive Planck `[1, 1 + hbarQ q]` UV Gap**:
For every `q > 1`, `(1 + log q) - (1 + log(1 + hbarQ q)) = -log(1 - (hbarQ q)²) > 0`. -/
theorem reeb_vs_planck_schwinger_uv_gap (q : ℝ) (hq : 1 < q) :
    (1 + Real.log q) - mesonEmProperTimeFactor q = -Real.log (1 - (hbarQ q) ^ 2) ∧
    0 < (1 + Real.log q) - mesonEmProperTimeFactor q := by
  have hq_pos : 0 < q := by linarith
  have hhb_eq : hbarQ q = (q - 1) / q := by unfold hbarQ; field_simp
  have hhb_pos : 0 < hbarQ q := by rw [hhb_eq]; exact div_pos (by linarith) hq_pos
  have h1mhb_pos : 0 < 1 - hbarQ q := by
    have heq : 1 - hbarQ q = q⁻¹ := by unfold hbarQ; ring
    rw [heq]; exact inv_pos.mpr hq_pos
  have h1phb_pos : 0 < 1 + hbarQ q := by linarith
  have hprod : q⁻¹ * (1 + hbarQ q) = 1 - (hbarQ q) ^ 2 := by
    unfold hbarQ; field_simp; ring
  have h1msq_pos : 0 < 1 - (hbarQ q) ^ 2 := by
    rw [← hprod]; exact mul_pos (inv_pos.mpr hq_pos) h1phb_pos
  have h1msq_lt : 1 - (hbarQ q) ^ 2 < 1 := by
    have hsq : 0 < (hbarQ q) ^ 2 := sq_pos_of_pos hhb_pos
    linarith
  have hlog : Real.log (q⁻¹ * (1 + hbarQ q)) = Real.log (1 - (hbarQ q) ^ 2) := by
    rw [hprod]
  rw [Real.log_mul (ne_of_gt (inv_pos.mpr hq_pos)) (ne_of_gt h1phb_pos), Real.log_inv] at hlog
  have hgap : (1 + Real.log q) - mesonEmProperTimeFactor q = -Real.log (1 - (hbarQ q) ^ 2) := by
    unfold mesonEmProperTimeFactor
    linarith
  refine ⟨hgap, ?_⟩
  rw [hgap]
  have hneg : Real.log (1 - (hbarQ q) ^ 2) < 0 := Real.log_neg h1msq_pos h1msq_lt
  linarith

/-- **Dashen Chiral Sign Obstruction on `ℝ` (`dashen_equal_em_lowers_ratio_real`)**:
Whenever the neutral strong mass-squared ratio satisfies `1 < R₀`, `0 < m₀_sq`, and the common
charged-meson electromagnetic self-energy satisfies `0 < dEM`, adding `dEM` equally to both
kaon and pion **strictly lowers** `m_K² / m_π²` below `R₀`. -/
theorem dashen_equal_em_lowers_ratio_real (R₀ m₀_sq dEM : ℝ)
    (hR : 1 < R₀) (hm : 0 < m₀_sq) (hd : 0 < dEM) :
    (R₀ * m₀_sq + dEM) / (m₀_sq + dEM) < R₀ := by
  have hden_pos : 0 < m₀_sq + dEM := by linarith
  have hid := dashen_equal_em_shift_identity (K := ℝ) R₀ m₀_sq dEM (ne_of_gt hden_pos)
  rw [neg_div] at hid
  have hnum_pos : 0 < (R₀ - 1) * dEM := mul_pos (by linarith) hd
  have hquot_pos : 0 < ((R₀ - 1) * dEM) / (m₀_sq + dEM) := div_pos hnum_pos hden_pos
  linarith

/-- Predicted linear meson mass ratio `R(α) = √(S + (α / π) * F)` as a function of `α`. -/
noncomputable def mesonRatioPred (S F α : ℝ) : ℝ :=
  Real.sqrt (S + (α / Real.pi) * F)

/-- **Exact Lipschitz `α_EM`-Insensitivity Bound (`meson_ratio_alpha_lipschitz_bound`)**:
For any `0 < S`, `0 ≤ F`, and `0 ≤ α₁, α₂`,
`|mesonRatioPred S F α₁ - mesonRatioPred S F α₂| ≤ (F / (2 * π * √S)) * |α₁ - α₂|`. -/
theorem meson_ratio_alpha_lipschitz_bound (S F α₁ α₂ : ℝ)
    (hS : 0 < S) (hF : 0 ≤ F) (hα1 : 0 ≤ α₁) (hα2 : 0 ≤ α₂) :
    |mesonRatioPred S F α₁ - mesonRatioPred S F α₂| ≤
      (F / (2 * Real.pi * Real.sqrt S)) * |α₁ - α₂| := by
  unfold mesonRatioPred
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hrad1_ge : S ≤ S + (α₁ / Real.pi) * F := by
    have : 0 ≤ (α₁ / Real.pi) * F := mul_nonneg (div_nonneg hα1 (le_of_lt hπ_pos)) hF
    linarith
  have hrad2_ge : S ≤ S + (α₂ / Real.pi) * F := by
    have : 0 ≤ (α₂ / Real.pi) * F := mul_nonneg (div_nonneg hα2 (le_of_lt hπ_pos)) hF
    linarith
  set R₁ := Real.sqrt (S + (α₁ / Real.pi) * F)
  set R₂ := Real.sqrt (S + (α₂ / Real.pi) * F)
  have hsqrtS_pos : 0 < Real.sqrt S := Real.sqrt_pos.mpr hS
  have hR1_ge : Real.sqrt S ≤ R₁ := Real.sqrt_le_sqrt hrad1_ge
  have hR2_ge : Real.sqrt S ≤ R₂ := Real.sqrt_le_sqrt hrad2_ge
  have hsum_ge : 2 * Real.sqrt S ≤ R₁ + R₂ := by linarith
  have hsum_pos : 0 < R₁ + R₂ := by linarith
  have hsq_diff : (R₁ - R₂) * (R₁ + R₂) = (F / Real.pi) * (α₁ - α₂) := by
    have h1 : R₁ ^ 2 = S + (α₁ / Real.pi) * F := Real.sq_sqrt (by linarith)
    have h2 : R₂ ^ 2 = S + (α₂ / Real.pi) * F := Real.sq_sqrt (by linarith)
    calc
      (R₁ - R₂) * (R₁ + R₂) = R₁ ^ 2 - R₂ ^ 2 := by ring
      _ = (S + (α₁ / Real.pi) * F) - (S + (α₂ / Real.pi) * F) := by rw [h1, h2]
      _ = (F / Real.pi) * (α₁ - α₂) := by ring
  have habs_eq : |R₁ - R₂| * (R₁ + R₂) = (F / Real.pi) * |α₁ - α₂| := by
    have h := congrArg abs hsq_diff
    rw [abs_mul, abs_of_pos hsum_pos, abs_mul,
      abs_of_nonneg (div_nonneg hF (le_of_lt hπ_pos))] at h
    exact h
  have hmul_le : |R₁ - R₂| * (2 * Real.sqrt S) ≤ (F / Real.pi) * |α₁ - α₂| := by
    rw [← habs_eq]
    exact mul_le_mul_of_nonneg_left hsum_ge (abs_nonneg _)
  have hden_pos : 0 < 2 * Real.sqrt S := by linarith
  rw [← le_div_iff₀ hden_pos] at hmul_le
  have hrhs_eq :
      ((F / Real.pi) * |α₁ - α₂|) / (2 * Real.sqrt S) =
        (F / (2 * Real.pi * Real.sqrt S)) * |α₁ - α₂| := by
    field_simp [ne_of_gt hπ_pos, ne_of_gt hsqrtS_pos]
  rwa [hrhs_eq] at hmul_le

end SchwingerProperTimeAndSensitivity

/-! ## Section 3: `§3b-cond` Hypothesis Class & `trivialModel` Consistency Witness -/

section ConditionalMesonBridge

/-- **Conjecture Carrier (`§3b-cond`, Content-Bearing, Zero Global Instances)**:
Packages the working-assumption bridge identifying:
1. a substrate parameter `q > 1`,
2. a positive electromagnetic coupling `α > 0` satisfying the `0`-`sorry` 1-loop Bring–Schwinger
   fixed-point relation (`s = +1`, `G = 4`, `c_loop = (hHecke q)²`), and
3. the charged kaon-to-pion mass-squared ratio `mK_sq / mpi_sq` with
   `[3]_q [4]_q + (α / π) * (1 + log(1 + hbarQ q))`. -/
class MesonKaonPionGMOREmBridgeClass (q α mK_sq mpi_sq : ℝ) : Prop where
  /-- Substrate parameter lies in `q > 1`. -/
  one_lt_q : 1 < q
  /-- Electromagnetic coupling `α` is strictly positive. -/
  alpha_pos : 0 < α
  /-- Charged pion mass-squared scale `mpi_sq` is strictly positive. -/
  mpi_sq_pos : 0 < mpi_sq
  /-- `α` satisfies the 1-loop Bring–Schwinger fixed-point equation (`#9360` 4-topology `EmFermionLoop`). -/
  alpha_formB_self_consistent :
    IsUnifiedBringFixedPoint 1 (q * qIntBal q 9 * qIntBal q 10) 4 q ((hHecke q) ^ 2) α
  /-- Conditional GMOR + proper-time worldline closure for `mK_sq / mpi_sq`. -/
  meson_ratio_sq_closure :
    mK_sq / mpi_sq =
      qIntBal q 3 * qIntBal q 4 + (α / Real.pi) * mesonEmProperTimeFactor q

/-- **Conditional Meson Ratio & Strict Lower Bound (`§3b-cond`)**:
Under `[MesonKaonPionGMOREmBridgeClass q α mK_sq mpi_sq]`, `mK_sq / mpi_sq` strictly exceeds
its strong core `[3]_q [4]_q` (which in turn strictly exceeds `12`). -/
theorem meson_ratio_sq_gt_strong_gt_twelve (q α mK_sq mpi_sq : ℝ)
    [inst : MesonKaonPionGMOREmBridgeClass q α mK_sq mpi_sq] :
    12 < qIntBal q 3 * qIntBal q 4 ∧
    qIntBal q 3 * qIntBal q 4 < mK_sq / mpi_sq := by
  have hq_pos : 0 < q := by linarith [inst.one_lt_q]
  have h12 : 12 < qIntBal q 3 * qIntBal q 4 :=
    (twelve_factorizations_strict_ordering_real q hq_pos (ne_of_gt inst.one_lt_q)).1
  have hfac_pos : 0 < mesonEmProperTimeFactor q := by
    obtain ⟨_, h1phb, _, _⟩ := meson_em_schwinger_proper_time_decomp q (by linarith [inst.one_lt_q])
    unfold mesonEmProperTimeFactor
    have h1lt : 1 < 1 + hbarQ q := by
      have hhb : hbarQ q = (q - 1) / q := by unfold hbarQ; field_simp
      have : 0 < hbarQ q := by rw [hhb]; exact div_pos (by linarith [inst.one_lt_q]) hq_pos
      linarith
    have hlog_pos : 0 < Real.log (1 + hbarQ q) := Real.log_pos h1lt
    linarith
  have hem_pos : 0 < (α / Real.pi) * mesonEmProperTimeFactor q :=
    mul_pos (div_pos inst.alpha_pos Real.pi_pos) hfac_pos
  refine ⟨h12, ?_⟩
  rw [inst.meson_ratio_sq_closure]
  linarith

/-- **Non-Vacuity / Consistency Witness (`def`, NEVER `instance` — `lean-generation` §5)**:
Constructs an explicit mathematical model at `q = 2` and `mpi_sq = 1` with a positive root `α` of
`IsUnifiedBringFixedPoint` obtained via the Intermediate Value Theorem on `[0, 1 / T_const]`. -/
noncomputable def trivialModel :
    ∃ (q α mK_sq mpi_sq : ℝ), MesonKaonPionGMOREmBridgeClass q α mK_sq mpi_sq := by
  let q : ℝ := 2
  let t_tree : ℝ := q * qIntBal q 9 * qIntBal q 10
  let t_const : ℝ := t_tree + (2 * (4 : ℝ)) / bringSurfaceArea
  have ht_tree_gt : 2 < t_tree := by
    dsimp only [t_tree, q]
    rw [qIntBal_def, qIntBal_def]
    norm_num
  have ht_const_gt : 2 < t_const := by
    dsimp only [t_const]
    have harea : 0 < (2 * (4 : ℝ)) / bringSurfaceArea := by
      unfold bringSurfaceArea bringFundamentalTriangleArea
      exact div_pos (by norm_num) (by linarith [Real.pi_pos])
    linarith
  let f : ℝ → ℝ := fun a =>
    t_const * a + a ^ 2 * habiroNorm q * (1 - (hHecke q) ^ 2 * a) - 1
  have hcont : Continuous f := by continuity
  have hf0 : f 0 = -1 := by simp [f]
  have hb_pos : 0 < 1 / t_const := div_pos zero_lt_one (by linarith)
  have hfb : 0 ≤ f (1 / t_const) := by
    dsimp only [f]
    have hmul : t_const * (1 / t_const) = 1 := mul_one_div_cancel (by linarith)
    have hhab : 0 ≤ habiroNorm q := by
      unfold habiroNorm; dsimp only [q]; exact div_nonneg (by norm_num) (by linarith [Real.pi_pos])
    have hloop_pos : 0 ≤ 1 - (hHecke q) ^ 2 * (1 / t_const) := by
      have hh2 : (hHecke q) ^ 2 = (9 : ℝ) / 4 := by unfold hHecke; dsimp only [q]; norm_num
      rw [hh2]
      have hle : (1 : ℝ) / t_const < 4 / 9 := by
        rw [div_lt_div_iff₀ (by linarith) (by norm_num)]
        have h9 : (500 : ℝ) < t_tree := by
          dsimp only [t_tree, q]; rw [qIntBal_def, qIntBal_def]; norm_num
        have harea : 0 < (2 * (4 : ℝ)) / bringSurfaceArea := by
          unfold bringSurfaceArea bringFundamentalTriangleArea
          exact div_pos (by norm_num) (by linarith [Real.pi_pos])
        dsimp only [t_const]
        linarith
      linarith
    have hterm : 0 ≤ (1 / t_const) ^ 2 * habiroNorm q * (1 - (hHecke q) ^ 2 * (1 / t_const)) :=
      mul_nonneg (mul_nonneg (sq_nonneg _) hhab) hloop_pos
    linarith
  obtain ⟨α, hα_mem, hα_eq⟩ :=
    intermediate_value_Icc (le_of_lt hb_pos) hcont.continuousOn (by rw [hf0]; exact ⟨by norm_num, hfb⟩)
  have hα_pos : 0 < α := by
    rcases lt_or_eq_of_le hα_mem.1 with hlt | rfl
    · exact hlt
    · linarith [hf0, hα_eq]
  let mK_sq : ℝ := qIntBal q 3 * qIntBal q 4 + (α / Real.pi) * mesonEmProperTimeFactor q
  refine ⟨q, α, mK_sq, 1, ?_⟩
  refine
    { one_lt_q := by dsimp only [q]; norm_num
      alpha_pos := hα_pos
      mpi_sq_pos := zero_lt_one
      alpha_formB_self_consistent := ?_
      meson_ratio_sq_closure := by dsimp only [mK_sq]; simp }
  unfold IsUnifiedBringFixedPoint
  rw [div_eq_iff (ne_of_gt hα_pos)]
  dsimp only [f, t_const] at hα_eq
  linear_combination -hα_eq

end ConditionalMesonBridge

end MesonKaonPionSchwingerBridge
end QOU.EightfoldWay
