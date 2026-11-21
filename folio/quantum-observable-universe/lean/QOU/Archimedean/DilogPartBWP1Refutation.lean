import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

/-!
# Dilog Part-B W-P1 — refutation of the UNCONDITIONAL joint boundary limit (scope-(b))

The joint W-P1 capstone (`tendsto_wp1_sum_of_no_resonance`, #4270) proves W-P1 convergence
*conditionally* on a Diophantine no-resonance bound `c(q−1) ≤ 1−x·qⁿ`.  This file proves
that hypothesis is **necessary**: the *unconditional* joint boundary limit
`(q−1)·log(1−x·qⁿ) → 0` is **false**, by exhibiting an explicit counter-sequence along which
the boundary term converges to a nonzero value (`log x ≠ 0`).  A scope-(b) refutation
(AGENTS.md §"Before declaring refuted"): a *proved* obstruction with a named witness.

## The counter-sequence

For fixed `x ∈ (0,1)`, `L := log(1/x) > 0`,

`q_m := exp(L / (m + e^{−m}))`,   `n_m := m`.

Then `1 < q_m`, `q_m → 1⁺`, and `x·q_m^m = exp(−β_m) → 1⁻` with
`β_m := L·e^{−m}/(m+e^{−m}) → 0`, yet the boundary term does **not** vanish:

`(q_m − 1)·log(1 − x·q_m^m)  ⟶  log x  ≠  0`.

The proof factors the term as `A_m · B_m` with

* **(A)** `A_m := m·(q_m − 1) → L`  (squeeze: `t ≤ eᵗ − 1 ≤ t·eᵗ` at `t = L/(m+e^{−m})`, both
  ends `·m → L`);
* **(B)** `B_m := log(1 − x·q_m^m)/m → −1`  (`δ_m = 1 − e^{−β_m} ∈ [β_m e^{−β_m}, β_m]`, so
  `log β_m − β_m ≤ log δ_m ≤ log β_m`, and `log β_m/m = log L/m − 1 − log(m+e^{−m})/m → −1`).

Then `A_m · B_m → L·(−1) = −L = log x`, and uniqueness of limits gives `↛ 0`.

## Base ring (§7c)

Archimedean throughout (`ℝ`): `Real.exp`, `Real.log`, `atTop` limits.

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit; docs/coordination/dilog-part-b-cusp-attack.md (2026-07-25 counter-sequence); bean qou-jplv
-/

namespace QOU.Archimedean

open Filter Topology

variable {x : ℝ}

/-- `L := log(1/x)`, positive for `x ∈ (0,1)`.  Target boundary value is `−L = log x`. -/
noncomputable def wpRefL (x : ℝ) : ℝ := Real.log (1 / x)

/-- The resonant width exponent `t_m := L / (m + e^{−m})`. -/
noncomputable def wpRefT (x : ℝ) (m : ℕ) : ℝ := wpRefL x / ((m : ℝ) + Real.exp (-(m : ℝ)))

/-- The counter-sequence `q_m := exp(t_m)`. -/
noncomputable def qSeq (x : ℝ) (m : ℕ) : ℝ := Real.exp (wpRefT x m)

/-- The endpoint gap exponent `β_m := L·e^{−m}/(m+e^{−m})`, so `x·q_m^m = exp(−β_m)`. -/
noncomputable def wpRefBeta (x : ℝ) (m : ℕ) : ℝ :=
  wpRefL x * Real.exp (-(m : ℝ)) / ((m : ℝ) + Real.exp (-(m : ℝ)))

theorem wpRefL_pos (hx0 : 0 < x) (hx1 : x < 1) : 0 < wpRefL x := by
  have h1x : 1 < 1 / x := by rw [lt_div_iff₀ hx0]; linarith
  exact Real.log_pos h1x

/-- `log x = − L`. -/
theorem log_eq_neg_wpRefL (hx0 : 0 < x) : Real.log x = - wpRefL x := by
  unfold wpRefL
  rw [one_div, Real.log_inv, neg_neg]

theorem wpRef_denom_pos (m : ℕ) : 0 < (m : ℝ) + Real.exp (-(m : ℝ)) := by
  have := Real.exp_pos (-(m : ℝ)); positivity

theorem wpRefT_pos (hx0 : 0 < x) (hx1 : x < 1) (m : ℕ) : 0 < wpRefT x m :=
  div_pos (wpRefL_pos hx0 hx1) (wpRef_denom_pos m)

theorem wpRefBeta_pos (hx0 : 0 < x) (hx1 : x < 1) (m : ℕ) : 0 < wpRefBeta x m := by
  unfold wpRefBeta
  have := Real.exp_pos (-(m : ℝ))
  exact div_pos (mul_pos (wpRefL_pos hx0 hx1) this) (wpRef_denom_pos m)

/-- **`1 < q_m`.** -/
theorem one_lt_qSeq (hx0 : 0 < x) (hx1 : x < 1) (m : ℕ) : 1 < qSeq x m := by
  have h := wpRefT_pos hx0 hx1 m
  have : Real.exp 0 < Real.exp (wpRefT x m) := Real.exp_lt_exp.mpr h
  rwa [Real.exp_zero] at this

/-- The denominator `m + e^{−m} → ∞`. -/
theorem wpRef_denom_atTop :
    Tendsto (fun m : ℕ => (m : ℝ) + Real.exp (-(m : ℝ))) atTop atTop := by
  refine tendsto_atTop_mono (fun m => ?_) (tendsto_natCast_atTop_atTop (R := ℝ))
  have := (Real.exp_pos (-(m : ℝ))).le; linarith

/-- `t_m → 0`. -/
theorem tendsto_wpRefT_zero (hx0 : 0 < x) : Tendsto (wpRefT x) atTop (𝓝 0) := by
  unfold wpRefT
  exact Tendsto.div_atTop tendsto_const_nhds wpRef_denom_atTop

/-- `q_m → 1`. -/
theorem tendsto_qSeq_one (hx0 : 0 < x) : Tendsto (qSeq x) atTop (𝓝 1) := by
  unfold qSeq
  have h := (Real.continuous_exp.tendsto 0).comp (tendsto_wpRefT_zero hx0)
  rwa [Real.exp_zero] at h

/-- `β_m → 0`. -/
theorem tendsto_wpRefBeta_zero (hx0 : 0 < x) : Tendsto (wpRefBeta x) atTop (𝓝 0) := by
  unfold wpRefBeta
  have hexp : Tendsto (fun m : ℕ => Real.exp (-(m : ℝ))) atTop (𝓝 0) :=
    Real.tendsto_exp_atBot.comp
      (tendsto_neg_atBot_iff.mpr (tendsto_natCast_atTop_atTop (R := ℝ)))
  have hnum : Tendsto (fun m : ℕ => wpRefL x * Real.exp (-(m : ℝ))) atTop (𝓝 0) := by
    simpa using hexp.const_mul (wpRefL x)
  have hden : Tendsto (fun m : ℕ => ((m : ℝ) + Real.exp (-(m : ℝ)))⁻¹) atTop (𝓝 0) :=
    Tendsto.inv_tendsto_atTop wpRef_denom_atTop
  have : Tendsto (fun m : ℕ => (wpRefL x * Real.exp (-(m : ℝ)))
      * ((m : ℝ) + Real.exp (-(m : ℝ)))⁻¹) atTop (𝓝 (0 * 0)) := hnum.mul hden
  rw [mul_zero] at this
  simpa [div_eq_mul_inv] using this

/-- **Endpoint identity** `x·q_m^m = exp(−β_m)`.  Pure algebra: `q_m^m = exp(m·t_m)`,
    `x = exp(log x) = exp(−L)`, and `−L + m·t_m = −β_m`. -/
theorem endpoint_eq (hx0 : 0 < x) (m : ℕ) :
    x * (qSeq x m) ^ m = Real.exp (- wpRefBeta x m) := by
  have hlog : Real.log x + (m : ℝ) * wpRefT x m = - wpRefBeta x m := by
    rw [log_eq_neg_wpRefL hx0]
    unfold wpRefT wpRefBeta wpRefL
    have hd : (m : ℝ) + Real.exp (-(m : ℝ)) ≠ 0 := ne_of_gt (wpRef_denom_pos m)
    field_simp
    ring
  unfold qSeq
  rw [← Real.exp_nat_mul]
  nth_rewrite 1 [show x = Real.exp (Real.log x) from (Real.exp_log hx0).symm]
  rw [← Real.exp_add, hlog]

/-- Algebraic identity `m·t_m = L − β_m`. -/
theorem m_mul_wpRefT_eq (m : ℕ) :
    (m : ℝ) * wpRefT x m = wpRefL x - wpRefBeta x m := by
  unfold wpRefT wpRefBeta
  have hd : (m : ℝ) + Real.exp (-(m : ℝ)) ≠ 0 := ne_of_gt (wpRef_denom_pos m)
  field_simp
  ring

/-- `m·t_m → L`. -/
theorem tendsto_m_mul_wpRefT (hx0 : 0 < x) :
    Tendsto (fun m : ℕ => (m : ℝ) * wpRefT x m) atTop (𝓝 (wpRefL x)) := by
  have h : Tendsto (fun m : ℕ => wpRefL x - wpRefBeta x m) atTop (𝓝 (wpRefL x - 0)) :=
    tendsto_const_nhds.sub (tendsto_wpRefBeta_zero hx0)
  rw [sub_zero] at h
  exact h.congr (fun m => (m_mul_wpRefT_eq m).symm)

/-- **(A)** `m·(q_m − 1) → L`.  Squeeze `m·t_m ≤ m·(q_m−1) ≤ m·t_m·q_m` from
    `t ≤ eᵗ − 1 ≤ t·eᵗ` (both from `Real.add_one_le_exp`), both ends `→ L`. -/
theorem tendsto_A (hx0 : 0 < x) (hx1 : x < 1) :
    Tendsto (fun m : ℕ => (m : ℝ) * (qSeq x m - 1)) atTop (𝓝 (wpRefL x)) := by
  have hlow := tendsto_m_mul_wpRefT hx0
  have hupp : Tendsto (fun m : ℕ => (m : ℝ) * wpRefT x m * qSeq x m) atTop (𝓝 (wpRefL x)) := by
    have h := hlow.mul (tendsto_qSeq_one hx0)
    rwa [mul_one] at h
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlow hupp ?_ ?_
  · refine Filter.Eventually.of_forall (fun m => ?_)
    have hle : wpRefT x m ≤ qSeq x m - 1 := by
      have := Real.add_one_le_exp (wpRefT x m); unfold qSeq; linarith
    exact mul_le_mul_of_nonneg_left hle (Nat.cast_nonneg m)
  · refine Filter.Eventually.of_forall (fun m => ?_)
    have hle : qSeq x m - 1 ≤ wpRefT x m * qSeq x m := by
      have hpos := Real.exp_pos (wpRefT x m)
      have h := Real.add_one_le_exp (-(wpRefT x m))
      have hchain : Real.exp (wpRefT x m) * (1 - wpRefT x m)
          ≤ Real.exp (wpRefT x m) * Real.exp (-(wpRefT x m)) :=
        mul_le_mul_of_nonneg_left (by linarith) hpos.le
      rw [← Real.exp_add, add_neg_cancel, Real.exp_zero] at hchain
      unfold qSeq; nlinarith [hpos]
    calc (m : ℝ) * (qSeq x m - 1) ≤ (m : ℝ) * (wpRefT x m * qSeq x m) :=
          mul_le_mul_of_nonneg_left hle (Nat.cast_nonneg m)
      _ = (m : ℝ) * wpRefT x m * qSeq x m := by ring

/-- `log β_m = log L − m − log(m+e^{−m})`. -/
theorem log_wpRefBeta_eq (hx0 : 0 < x) (hx1 : x < 1) (m : ℕ) :
    Real.log (wpRefBeta x m)
      = Real.log (wpRefL x) - (m : ℝ) - Real.log ((m : ℝ) + Real.exp (-(m : ℝ))) := by
  unfold wpRefBeta
  have hL : (0 : ℝ) < wpRefL x := wpRefL_pos hx0 hx1
  have he : (0 : ℝ) < Real.exp (-(m : ℝ)) := Real.exp_pos _
  have hd : (0 : ℝ) < (m : ℝ) + Real.exp (-(m : ℝ)) := wpRef_denom_pos m
  rw [Real.log_div (by positivity) (ne_of_gt hd),
      Real.log_mul (ne_of_gt hL) (ne_of_gt he), Real.log_exp]
  ring

/-- `log y / y → 0` at atTop. -/
theorem tendsto_log_div_self_atTop :
    Tendsto (fun y : ℝ => Real.log y / y) atTop (𝓝 0) :=
  Real.isLittleO_log_id_atTop.tendsto_div_nhds_zero

/-- `(m+e^{−m})/m → 1`. -/
theorem tendsto_denom_div_m :
    Tendsto (fun m : ℕ => ((m : ℝ) + Real.exp (-(m : ℝ))) / (m : ℝ)) atTop (𝓝 1) := by
  have hexp : Tendsto (fun m : ℕ => Real.exp (-(m : ℝ))) atTop (𝓝 0) :=
    Real.tendsto_exp_atBot.comp
      (tendsto_neg_atBot_iff.mpr (tendsto_natCast_atTop_atTop (R := ℝ)))
  have hinv : Tendsto (fun m : ℕ => ((m : ℝ))⁻¹) atTop (𝓝 0) :=
    tendsto_inv_atTop_zero.comp (tendsto_natCast_atTop_atTop (R := ℝ))
  have hquot : Tendsto (fun m : ℕ => Real.exp (-(m : ℝ)) / (m : ℝ)) atTop (𝓝 0) := by
    have := hexp.mul hinv; rw [mul_zero] at this; simpa [div_eq_mul_inv] using this
  have h1 : Tendsto (fun m : ℕ => (1 : ℝ) + Real.exp (-(m : ℝ)) / (m : ℝ)) atTop (𝓝 (1 + 0)) :=
    tendsto_const_nhds.add hquot
  rw [add_zero] at h1
  refine h1.congr' ?_
  filter_upwards [eventually_gt_atTop 0] with m hm
  have hm0 : (m : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hm.ne'
  field_simp

/-- `log(m+e^{−m})/m → 0`. -/
theorem tendsto_log_denom_div_m :
    Tendsto (fun m : ℕ => Real.log ((m : ℝ) + Real.exp (-(m : ℝ))) / (m : ℝ)) atTop (𝓝 0) := by
  have hcomp : Tendsto (fun m : ℕ =>
      Real.log ((m : ℝ) + Real.exp (-(m : ℝ))) / ((m : ℝ) + Real.exp (-(m : ℝ))))
      atTop (𝓝 0) := tendsto_log_div_self_atTop.comp wpRef_denom_atTop
  have hprod := hcomp.mul tendsto_denom_div_m
  rw [mul_one] at hprod
  refine hprod.congr' ?_
  filter_upwards [eventually_gt_atTop 0] with m hm
  have hm0 : (m : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hm.ne'
  have hd : (m : ℝ) + Real.exp (-(m : ℝ)) ≠ 0 := ne_of_gt (wpRef_denom_pos m)
  field_simp

/-- `log β_m/m → −1`. -/
theorem tendsto_log_wpRefBeta_div_m (hx0 : 0 < x) (hx1 : x < 1) :
    Tendsto (fun m : ℕ => Real.log (wpRefBeta x m) / (m : ℝ)) atTop (𝓝 (-1)) := by
  have hLinv : Tendsto (fun m : ℕ => Real.log (wpRefL x) / (m : ℝ)) atTop (𝓝 0) := by
    have hinv : Tendsto (fun m : ℕ => ((m : ℝ))⁻¹) atTop (𝓝 0) :=
      tendsto_inv_atTop_zero.comp (tendsto_natCast_atTop_atTop (R := ℝ))
    have := hinv.const_mul (Real.log (wpRefL x))
    rw [mul_zero] at this; simpa [div_eq_mul_inv] using this
  have hcombo : Tendsto (fun m : ℕ =>
      Real.log (wpRefL x) / (m : ℝ) - 1 - Real.log ((m : ℝ) + Real.exp (-(m : ℝ))) / (m : ℝ))
      atTop (𝓝 (0 - 1 - 0)) :=
    (hLinv.sub tendsto_const_nhds).sub tendsto_log_denom_div_m
  rw [zero_sub, sub_zero] at hcombo
  refine hcombo.congr' ?_
  filter_upwards [eventually_gt_atTop 0] with m hm
  have hm0 : (m : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hm.ne'
  rw [log_wpRefBeta_eq hx0 hx1 m]
  field_simp

/-- Per-step log lower bound `log β_m − β_m ≤ log δ_m` (from `β e^{−β} ≤ 1 − e^{−β}`). -/
theorem logDelta_lower (hx0 : 0 < x) (hx1 : x < 1) (m : ℕ) :
    Real.log (wpRefBeta x m) - wpRefBeta x m ≤ Real.log (1 - x * (qSeq x m) ^ m) := by
  have hβpos : 0 < wpRefBeta x m := wpRefBeta_pos hx0 hx1 m
  have he : (0 : ℝ) < Real.exp (- wpRefBeta x m) := Real.exp_pos _
  rw [endpoint_eq hx0]
  have hprodpos : 0 < wpRefBeta x m * Real.exp (- wpRefBeta x m) := mul_pos hβpos he
  have hkey : (wpRefBeta x m + 1) * Real.exp (- wpRefBeta x m) ≤ 1 := by
    have h := Real.add_one_le_exp (wpRefBeta x m)
    have hmul : (wpRefBeta x m + 1) * Real.exp (- wpRefBeta x m)
        ≤ Real.exp (wpRefBeta x m) * Real.exp (- wpRefBeta x m) :=
      mul_le_mul_of_nonneg_right h he.le
    rwa [← Real.exp_add, add_neg_cancel, Real.exp_zero] at hmul
  have hlb : wpRefBeta x m * Real.exp (- wpRefBeta x m) ≤ 1 - Real.exp (- wpRefBeta x m) := by
    have hexp : (wpRefBeta x m + 1) * Real.exp (- wpRefBeta x m)
        = Real.exp (- wpRefBeta x m) + wpRefBeta x m * Real.exp (- wpRefBeta x m) := by ring
    linarith [hkey, hexp]
  have hlog_lb : Real.log (wpRefBeta x m) - wpRefBeta x m
      = Real.log (wpRefBeta x m * Real.exp (- wpRefBeta x m)) := by
    rw [Real.log_mul (ne_of_gt hβpos) (ne_of_gt he), Real.log_exp]; ring
  rw [hlog_lb]
  exact Real.log_le_log hprodpos hlb

/-- Per-step log upper bound `log δ_m ≤ log β_m` (from `1 − e^{−β} ≤ β`). -/
theorem logDelta_upper (hx0 : 0 < x) (hx1 : x < 1) (m : ℕ) :
    Real.log (1 - x * (qSeq x m) ^ m) ≤ Real.log (wpRefBeta x m) := by
  have hβpos : 0 < wpRefBeta x m := wpRefBeta_pos hx0 hx1 m
  have he : (0 : ℝ) < Real.exp (- wpRefBeta x m) := Real.exp_pos _
  rw [endpoint_eq hx0]
  have hδpos : 0 < 1 - Real.exp (- wpRefBeta x m) := by
    have hlt : Real.exp (- wpRefBeta x m) < 1 := by
      have h := Real.exp_lt_exp.mpr (show - wpRefBeta x m < 0 by linarith)
      rwa [Real.exp_zero] at h
    linarith
  have hub : 1 - Real.exp (- wpRefBeta x m) ≤ wpRefBeta x m := by
    have := Real.add_one_le_exp (- wpRefBeta x m); linarith
  exact Real.log_le_log hδpos hub

/-- **(B)** `log(1 − x·q_m^m)/m → −1`.  Squeeze `(log β_m − β_m)/m ≤ log δ_m/m ≤ log β_m/m`
    (from `logDelta_lower`/`logDelta_upper`, divided by `m>0`), both ends `→ −1`. -/
theorem tendsto_B (hx0 : 0 < x) (hx1 : x < 1) :
    Tendsto (fun m : ℕ => Real.log (1 - x * (qSeq x m) ^ m) / (m : ℝ)) atTop (𝓝 (-1)) := by
  have hupper := tendsto_log_wpRefBeta_div_m hx0 hx1
  have hlower : Tendsto (fun m : ℕ => (Real.log (wpRefBeta x m) - wpRefBeta x m) / (m : ℝ))
      atTop (𝓝 (-1)) := by
    have hbm : Tendsto (fun m : ℕ => wpRefBeta x m / (m : ℝ)) atTop (𝓝 0) := by
      have hinv : Tendsto (fun m : ℕ => ((m : ℝ))⁻¹) atTop (𝓝 0) :=
        tendsto_inv_atTop_zero.comp (tendsto_natCast_atTop_atTop (R := ℝ))
      have := (tendsto_wpRefBeta_zero hx0).mul hinv
      rw [mul_zero] at this; simpa [div_eq_mul_inv] using this
    have hcomb := hupper.sub hbm
    rw [sub_zero] at hcomb
    refine hcomb.congr (fun m => ?_)
    rw [sub_div]
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hlower hupper ?_ ?_
  · filter_upwards [eventually_gt_atTop 0] with m hm
    have hm' : (0 : ℝ) < (m : ℝ) := by exact_mod_cast hm
    exact (div_le_div_iff_of_pos_right hm').mpr (logDelta_lower hx0 hx1 m)
  · filter_upwards [eventually_gt_atTop 0] with m hm
    have hm' : (0 : ℝ) < (m : ℝ) := by exact_mod_cast hm
    exact (div_le_div_iff_of_pos_right hm').mpr (logDelta_upper hx0 hx1 m)

/-- **Crux.**  Along the counter-sequence `q_m`, the boundary term converges to `log x`:

    `(q_m − 1)·log(1 − x·q_m^m)  ⟶  log x`.

    Factor `= [m·(q_m−1)]·[log(1−x q_m^m)/m] → L·(−1) = −L = log x`. -/
theorem tendsto_boundary_refute (hx0 : 0 < x) (hx1 : x < 1) :
    Tendsto (fun m : ℕ => (qSeq x m - 1) * Real.log (1 - x * (qSeq x m) ^ m))
      atTop (𝓝 (Real.log x)) := by
  have hAB : Tendsto (fun m : ℕ =>
      ((m : ℝ) * (qSeq x m - 1)) * (Real.log (1 - x * (qSeq x m) ^ m) / (m : ℝ)))
      atTop (𝓝 (wpRefL x * (-1))) := (tendsto_A hx0 hx1).mul (tendsto_B hx0 hx1)
  rw [show wpRefL x * (-1) = Real.log x by rw [log_eq_neg_wpRefL hx0]; ring] at hAB
  refine hAB.congr' ?_
  filter_upwards [eventually_gt_atTop 0] with m hm
  have hm0 : (m : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hm.ne'
  field_simp

/-- **Refutation of the unconditional joint boundary limit (scope-(b)).**  The limit
    `(q−1)·log(1−x·qⁿ) → 0` is FALSE: along the explicit counter-sequence `q_m`, the boundary
    term converges to `log x ≠ 0` (`tendsto_boundary_refute`), so by uniqueness of limits it
    does not converge to `0`.  This proves the Diophantine no-resonance hypothesis of
    `tendsto_wp1_sum_of_no_resonance` (#4270) is **necessary**. -/
theorem not_tendsto_boundary_zero (hx0 : 0 < x) (hx1 : x < 1) :
    ¬ Tendsto (fun m : ℕ => (qSeq x m - 1) * Real.log (1 - x * (qSeq x m) ^ m))
        atTop (𝓝 0) := by
  intro hcontra
  have huniq := tendsto_nhds_unique (tendsto_boundary_refute hx0 hx1) hcontra
  have hlogx : Real.log x < 0 := Real.log_neg hx0 hx1
  linarith [huniq]

end QOU.Archimedean
