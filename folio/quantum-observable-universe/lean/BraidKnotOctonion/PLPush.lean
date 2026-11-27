/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Analysis.Convex.Gauge
import Mathlib.Topology.UnitInterval
import Mathlib.Topology.Order.IntermediateValue

set_option autoImplicit false

/-!
# Pushing the centre of a convex body (issue #8902, stage 2, part 4)

The geometric tool for "a Δ-move is an ambient isotopy". Let `S` be a convex neighbourhood of
`0` in a real normed space, with gauge `g`, and let `w` be a vector with `g w < 1` (so `w` lies
in the interior of `S`). The **push**

    push S w x = x + max 0 (1 - g x) • w

moves `0` to `w`, is the identity where `g ≥ 1` (outside the interior of `S`), and on every
segment from `0` to a point `a` with `g a = 1` it is the affine map onto the segment from `w`
to `a`. It is a homeomorphism, and `s ↦ push S (s • w)`, `s ∈ [0, 1]`, is an isotopy from the
identity whose inverses are jointly continuous.

## What is a DEFINITION here

* `pushCoef S x = max 0 (1 - gauge S x)`, `push S w x = x + pushCoef S x • w`.
* `pullTime S w y` — the unique `t ∈ [0, 1]` with `t = pushCoef S (y - t • w)`; the inverse
  of the push is `y ↦ y - pullTime S w y • w`.

## What is a THEOREM here

* `pushHomeomorph` — the push is a homeomorphism when `gauge S w < 1`.
* `pullTime_dist_le` — the pull time is Lipschitz in `(w, y)` near any `w` with `gauge S w < 1`.
* `pushFamily`, `pushFamily_zero`, `continuous_pushFamily`, `continuous_pushFamily_symm` — the
  isotopy `s ↦ push S (s • v)`, `s ∈ [0, 1]`: it starts at the identity and it and its inverses
  are jointly continuous.
* `push_of_one_le_gauge`, `push_zero`, `push_smul_of_gauge_eq_one` — the push fixes the
  complement of the interior, sends `0` to `w`, and maps `[0, a]` onto `[w, a]` when `g a = 1`.

## What is NOT proved here

* Anything about links. Choosing `S` so that it meets a link only in the edge being moved is
  the next file.
-/

namespace QOU.MathlibExt.PL

open Set Metric

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] {S : Set E}

/-- The push coefficient `max 0 (1 - gauge S x)`. -/
noncomputable def pushCoef (S : Set E) (x : E) : ℝ := max 0 (1 - gauge S x)

/-- **The push** of the centre of `S` towards `w`. -/
noncomputable def push (S : Set E) (w : E) (x : E) : E := x + pushCoef S x • w

lemma pushCoef_nonneg (x : E) : 0 ≤ pushCoef S x := le_max_left _ _

lemma pushCoef_le_one (x : E) : pushCoef S x ≤ 1 :=
  max_le zero_le_one (by linarith [gauge_nonneg (s := S) x])

lemma pushCoef_of_one_le_gauge {x : E} (h : 1 ≤ gauge S x) : pushCoef S x = 0 :=
  max_eq_left (by linarith)

section Body

variable (hc : Convex ℝ S) (h0 : S ∈ nhds (0 : E))
include hc h0

omit hc in
lemma exists_gauge_le_norm : ∃ C : ℝ, 0 ≤ C ∧ ∀ x, gauge S x ≤ C * ‖x‖ := by
  obtain ⟨r, hr, hball⟩ := Metric.mem_nhds_iff.mp h0
  refine ⟨1 / r, by positivity, fun x => ?_⟩
  have := gauge_mono (absorbent_nhds_zero (ball_mem_nhds (0 : E) hr)) hball x
  rw [gauge_ball hr.le] at this
  calc gauge S x ≤ ‖x‖ / r := this
    _ = 1 / r * ‖x‖ := by ring

lemma gauge_sub_le (x y : E) : gauge S x ≤ gauge S y + gauge S (x - y) := by
  have := gauge_add_le hc (absorbent_nhds_zero h0) y (x - y)
  simpa using this

/-- The push coefficient is Lipschitz. -/
lemma abs_pushCoef_sub_le {C : ℝ} (hC : ∀ x, gauge S x ≤ C * ‖x‖) (x y : E) :
    |pushCoef S x - pushCoef S y| ≤ C * ‖x - y‖ := by
  have h1 := gauge_sub_le hc h0 x y
  have h2 := gauge_sub_le hc h0 y x
  have h3 := hC (x - y)
  have h4 := hC (y - x)
  rw [norm_sub_rev] at h4
  have hg : |(1 - gauge S x) - (1 - gauge S y)| ≤ C * ‖x - y‖ := by
    rw [abs_le]; constructor <;> linarith
  unfold pushCoef
  rw [max_comm, max_comm 0]
  exact (abs_max_sub_max_le_abs _ _ 0).trans hg

/-- Moving against `w` raises the push coefficient by at most `δ · gauge S w`. -/
lemma pushCoef_sub_smul_le (p w : E) {δ : ℝ} (hδ : 0 ≤ δ) :
    pushCoef S (p - δ • w) ≤ pushCoef S p + δ * gauge S w := by
  have hsub := gauge_sub_le hc h0 p (p - δ • w)
  rw [sub_sub_cancel, gauge_smul_of_nonneg hδ, smul_eq_mul] at hsub
  have hg := mul_nonneg hδ (gauge_nonneg (s := S) w)
  unfold pushCoef
  apply max_le
  · exact add_nonneg (le_max_left _ _) hg
  · linarith [le_max_right 0 (1 - gauge S p)]

/-- The root function `t ↦ t - pushCoef S (y - t • w)` grows at rate at least `1 - gauge S w`. -/
lemma root_fun_mono (y w : E) {t t' : ℝ} (h : t ≤ t') :
    (1 - gauge S w) * (t' - t) ≤
      (t' - pushCoef S (y - t' • w)) - (t - pushCoef S (y - t • w)) := by
  have := pushCoef_sub_smul_le hc h0 (y - t • w) w (sub_nonneg.mpr h)
  rw [sub_sub, ← add_smul, add_sub_cancel] at this
  nlinarith

lemma exists_root (y w : E) : ∃ t ∈ Icc (0 : ℝ) 1, t = pushCoef S (y - t • w) := by
  have hcont : ContinuousOn (fun t : ℝ => t - pushCoef S (y - t • w)) (Icc 0 1) := by
    obtain ⟨C, _, hC⟩ := exists_gauge_le_norm h0
    have : Continuous (pushCoef S) :=
      continuous_const.max (continuous_const.sub (continuous_gauge hc h0))
    exact (continuous_id.sub (this.comp (continuous_const.sub
      (continuous_id.smul continuous_const)))).continuousOn
  have h0' : (0 : ℝ) - pushCoef S (y - (0 : ℝ) • w) ≤ 0 := by
    linarith [pushCoef_nonneg (S := S) (y - (0 : ℝ) • w)]
  have h1' : 0 ≤ (1 : ℝ) - pushCoef S (y - (1 : ℝ) • w) := by
    linarith [pushCoef_le_one (S := S) (y - (1 : ℝ) • w)]
  obtain ⟨t, ht, hroot⟩ := intermediate_value_Icc zero_le_one hcont ⟨h0', h1'⟩
  exact ⟨t, ht, by linarith [hroot]⟩

end Body

/-- **The pull time**: the unique root in `[0, 1]` of `t = pushCoef S (y - t • w)` (when the
body is a convex neighbourhood of `0`; otherwise `0`). -/
noncomputable def pullTime (S : Set E) (w y : E) : ℝ := by
  classical
  exact if h : Convex ℝ S ∧ S ∈ nhds (0 : E) then Classical.choose (exists_root h.1 h.2 y w)
    else 0

section Body2

variable (hc : Convex ℝ S) (h0 : S ∈ nhds (0 : E))
include hc h0

lemma pullTime_spec (w y : E) :
    pullTime S w y ∈ Icc (0 : ℝ) 1 ∧ pullTime S w y = pushCoef S (y - pullTime S w y • w) := by
  have h : Convex ℝ S ∧ S ∈ nhds (0 : E) := ⟨hc, h0⟩
  simp only [pullTime, dif_pos h]
  exact Classical.choose_spec (exists_root h.1 h.2 y w)

/-- Any root agrees with the pull time when `gauge S w < 1`. -/
lemma eq_pullTime {w y : E} (hw : gauge S w < 1) {t : ℝ} (ht : t = pushCoef S (y - t • w)) :
    t = pullTime S w y := by
  obtain ⟨-, hτ⟩ := pullTime_spec hc h0 w y
  set τ := pullTime S w y
  by_contra hne
  rcases lt_or_gt_of_ne hne with hlt | hlt
  · have := root_fun_mono hc h0 y w hlt.le
    have hpos : 0 < (1 - gauge S w) * (τ - t) := mul_pos (by linarith) (by linarith)
    linarith
  · have := root_fun_mono hc h0 y w hlt.le
    have hpos : 0 < (1 - gauge S w) * (t - τ) := mul_pos (by linarith) (by linarith)
    linarith

/-- **The pull time is Lipschitz** near any `w` with `gauge S w < 1`. -/
lemma pullTime_dist_le {C : ℝ} (hC0 : 0 ≤ C) (hC : ∀ x, gauge S x ≤ C * ‖x‖) (w w' y y' : E) :
    (1 - gauge S w) * |pullTime S w y - pullTime S w' y'| ≤ C * (‖y - y'‖ + ‖w - w'‖) := by
  obtain ⟨-, hτ⟩ := pullTime_spec hc h0 w y
  obtain ⟨⟨h0', h1'⟩, hτ'⟩ := pullTime_spec hc h0 w' y'
  set τ := pullTime S w y
  set τ' := pullTime S w' y'
  have hlip := abs_pushCoef_sub_le hc h0 hC (y - τ' • w) (y' - τ' • w')
  have hn : ‖(y - τ' • w) - (y' - τ' • w')‖ ≤ ‖y - y'‖ + ‖w - w'‖ := by
    have : (y - τ' • w) - (y' - τ' • w') = (y - y') - τ' • (w - w') := by
      rw [smul_sub]; abel
    rw [this]
    refine (norm_sub_le _ _).trans (add_le_add le_rfl ?_)
    rw [norm_smul, Real.norm_of_nonneg h0']
    exact mul_le_of_le_one_left (norm_nonneg _) h1'
  have hbound : |τ' - pushCoef S (y - τ' • w)| ≤ C * (‖y - y'‖ + ‖w - w'‖) := by
    have : τ' - pushCoef S (y - τ' • w) = pushCoef S (y' - τ' • w') - pushCoef S (y - τ' • w) := by
      rw [← hτ']
    rw [this, abs_sub_comm]
    exact hlip.trans (mul_le_mul_of_nonneg_left hn hC0)
  rcases le_total τ τ' with hle | hle
  · have := root_fun_mono hc h0 y w hle
    rw [← hτ, sub_self, sub_zero] at this
    rw [abs_sub_comm, abs_of_nonneg (sub_nonneg.mpr hle)]
    exact this.trans ((le_abs_self _).trans hbound)
  · have := root_fun_mono hc h0 y w hle
    rw [← hτ, sub_self, zero_sub] at this
    rw [abs_of_nonneg (sub_nonneg.mpr hle)]
    have h2 := neg_abs_le (τ' - pushCoef S (y - τ' • w))
    linarith

lemma continuous_push (w : E) : Continuous (push S w) :=
  continuous_id.add ((continuous_const.max (continuous_const.sub
    (continuous_gauge hc h0))).smul continuous_const)

lemma continuous_push_family (v : E) : Continuous fun p : ℝ × E => push S (p.1 • v) p.2 :=
  continuous_snd.add (((continuous_const.max (continuous_const.sub
    (continuous_gauge hc h0))).comp continuous_snd).smul (continuous_fst.smul continuous_const))

/-- **The pull time of the family `s ↦ s • v` is jointly continuous** on `[0, 1] × E`. -/
lemma continuous_pull_family {v : E} (hv : gauge S v < 1) :
    Continuous fun p : unitInterval × E => pullTime S ((p.1 : ℝ) • v) p.2 := by
  obtain ⟨C, hC0, hC⟩ := exists_gauge_le_norm h0
  have hκ : 0 < 1 - gauge S v := by linarith
  refine Metric.continuous_iff.mpr fun p ε hε => ?_
  set K := C * (1 + ‖v‖) + 1
  have hK : 0 < K := by positivity
  refine ⟨ε * (1 - gauge S v) / K, by positivity, fun p' hp' => ?_⟩
  rw [Prod.dist_eq] at hp'
  have hs : dist (p'.1 : ℝ) p.1 < ε * (1 - gauge S v) / K := by
    rw [← Subtype.dist_eq]; exact (le_max_left _ _).trans_lt hp'
  have hy : dist p'.2 p.2 < ε * (1 - gauge S v) / K := (le_max_right _ _).trans_lt hp'
  have hb := pullTime_dist_le hc h0 hC0 hC ((p.1 : ℝ) • v) ((p'.1 : ℝ) • v) p.2 p'.2
  have hgs : gauge S ((p.1 : ℝ) • v) ≤ gauge S v := by
    rw [gauge_smul_of_nonneg p.1.2.1, smul_eq_mul]
    exact mul_le_of_le_one_left (gauge_nonneg v) p.1.2.2
  have hnw : ‖(p.1 : ℝ) • v - (p'.1 : ℝ) • v‖ ≤ dist (p'.1 : ℝ) p.1 * ‖v‖ := by
    rw [← sub_smul, norm_smul, Real.norm_eq_abs, Real.dist_eq, abs_sub_comm]
  rw [Real.dist_eq, abs_sub_comm]
  have hd0 := dist_nonneg (x := (p'.1 : ℝ)) (y := p.1)
  have hy0 := dist_nonneg (x := p'.2) (y := p.2)
  rw [← dist_eq_norm, dist_comm] at hb
  have key : (1 - gauge S v) * |pullTime S ((p.1 : ℝ) • v) p.2 -
      pullTime S ((p'.1 : ℝ) • v) p'.2| < (1 - gauge S v) * ε := by
    have h1 : (1 - gauge S v) * |pullTime S ((p.1 : ℝ) • v) p.2 -
        pullTime S ((p'.1 : ℝ) • v) p'.2| ≤ C * (dist p'.2 p.2 + dist (p'.1 : ℝ) p.1 * ‖v‖) := by
      refine le_trans ?_ (hb.trans (mul_le_mul_of_nonneg_left (add_le_add le_rfl hnw) hC0))
      exact mul_le_mul_of_nonneg_right (by linarith) (abs_nonneg _)
    have hδ : C * (dist p'.2 p.2 + dist (p'.1 : ℝ) p.1 * ‖v‖) <
        (1 - gauge S v) * ε := by
      have : C * (dist p'.2 p.2 + dist (p'.1 : ℝ) p.1 * ‖v‖) ≤
          K * max (dist p'.2 p.2) (dist (p'.1 : ℝ) p.1) := by
        have hm1 := le_max_left (dist p'.2 p.2) (dist (p'.1 : ℝ) p.1)
        have hm2 := le_max_right (dist p'.2 p.2) (dist (p'.1 : ℝ) p.1)
        have hm0 : 0 ≤ max (dist p'.2 p.2) (dist (p'.1 : ℝ) p.1) := le_trans hy0 hm1
        simp only [K]
        nlinarith [norm_nonneg v, mul_nonneg hC0 (norm_nonneg v)]
      refine this.trans_lt ?_
      have hmax : max (dist p'.2 p.2) (dist (p'.1 : ℝ) p.1) < ε * (1 - gauge S v) / K :=
        max_lt hy hs
      calc K * max (dist p'.2 p.2) (dist (p'.1 : ℝ) p.1)
          < K * (ε * (1 - gauge S v) / K) := mul_lt_mul_of_pos_left hmax hK
        _ = (1 - gauge S v) * ε := by field_simp
    exact h1.trans_lt hδ
  exact lt_of_mul_lt_mul_left key hκ.le

lemma pullTime_push {w : E} (hw : gauge S w < 1) (x : E) :
    pullTime S w (push S w x) = pushCoef S x :=
  (eq_pullTime hc h0 hw (by simp [push])).symm

lemma push_pull (w y : E) : push S w (y - pullTime S w y • w) = y := by
  obtain ⟨-, hτ⟩ := pullTime_spec hc h0 w y
  simp only [push]
  rw [← hτ, sub_add_cancel]

/-- **The push is a homeomorphism** when `gauge S w < 1`. -/
noncomputable def pushHomeomorph {w : E} (hw : gauge S w < 1) : E ≃ₜ E where
  toFun := push S w
  invFun y := y - pullTime S w y • w
  left_inv x := by
    simp only
    rw [pullTime_push hc h0 hw]
    simp [push]
  right_inv := push_pull hc h0 w
  continuous_toFun := continuous_push hc h0 w
  continuous_invFun := by
    obtain ⟨C, hC0, hC⟩ := exists_gauge_le_norm h0
    have hκ : 0 < 1 - gauge S w := by linarith
    have hτ : Continuous (pullTime S w) := by
      refine Metric.continuous_iff.mpr fun y ε hε => ?_
      refine ⟨ε * (1 - gauge S w) / (C + 1), by positivity, fun y' hy' => ?_⟩
      have := pullTime_dist_le hc h0 hC0 hC w w y' y
      rw [sub_self, norm_zero, add_zero, ← dist_eq_norm] at this
      rw [Real.dist_eq]
      have hC1 : 0 < C + 1 := by linarith
      have : (1 - gauge S w) * |pullTime S w y' - pullTime S w y| <
          (1 - gauge S w) * ε := by
        calc _ ≤ C * dist y' y := this
          _ ≤ (C + 1) * dist y' y := by nlinarith [dist_nonneg (x := y') (y := y)]
          _ < (C + 1) * (ε * (1 - gauge S w) / (C + 1)) := by
              exact mul_lt_mul_of_pos_left hy' hC1
          _ = (1 - gauge S w) * ε := by field_simp
      exact lt_of_mul_lt_mul_left this hκ.le
    exact continuous_id.sub (hτ.smul continuous_const)

lemma pushHomeomorph_apply {w : E} (hw : gauge S w < 1) (x : E) :
    pushHomeomorph hc h0 hw x = push S w x := rfl

lemma pushHomeomorph_symm_apply {w : E} (hw : gauge S w < 1) (y : E) :
    (pushHomeomorph hc h0 hw).symm y = y - pullTime S w y • w := rfl

omit hc h0 in
lemma gauge_smul_unit_lt {v : E} (hv : gauge S v < 1) (s : unitInterval) :
    gauge S ((s : ℝ) • v) < 1 := by
  rw [gauge_smul_of_nonneg s.2.1, smul_eq_mul]
  calc (s : ℝ) * gauge S v ≤ gauge S v := mul_le_of_le_one_left (gauge_nonneg v) s.2.2
    _ < 1 := hv

/-- **The push isotopy** `s ↦ push S (s • v)`. -/
noncomputable def pushFamily {v : E} (hv : gauge S v < 1) (s : unitInterval) : E ≃ₜ E :=
  pushHomeomorph hc h0 (gauge_smul_unit_lt hv s)

lemma pushFamily_apply {v : E} (hv : gauge S v < 1) (s : unitInterval) (x : E) :
    pushFamily hc h0 hv s x = push S ((s : ℝ) • v) x := rfl

lemma pushFamily_zero {v : E} (hv : gauge S v < 1) (x : E) : pushFamily hc h0 hv 0 x = x := by
  simp [pushFamily_apply, push]

lemma continuous_pushFamily {v : E} (hv : gauge S v < 1) :
    Continuous fun p : unitInterval × E => pushFamily hc h0 hv p.1 p.2 :=
  (continuous_push_family hc h0 v).comp ((continuous_subtype_val.comp continuous_fst).prodMk
    continuous_snd)

lemma continuous_pushFamily_symm {v : E} (hv : gauge S v < 1) :
    Continuous fun p : unitInterval × E => (pushFamily hc h0 hv p.1).symm p.2 :=
  continuous_snd.sub ((continuous_pull_family hc h0 hv).smul
    ((continuous_subtype_val.comp continuous_fst).smul continuous_const))

end Body2

lemma push_of_one_le_gauge (w : E) {x : E} (h : 1 ≤ gauge S x) : push S w x = x := by
  simp [push, pushCoef_of_one_le_gauge h]

lemma push_zero (w : E) : push S w 0 = w := by
  simp [push, pushCoef]

/-- **The push maps `[0, a]` affinely onto `[w, a]`** when `gauge S a = 1`. -/
lemma push_smul_of_gauge_eq_one (w : E) {a : E} (ha : gauge S a = 1) {r : ℝ} (hr0 : 0 ≤ r)
    (hr1 : r ≤ 1) : push S w (r • a) = r • a + (1 - r) • w := by
  simp only [push, pushCoef, gauge_smul_of_nonneg hr0, smul_eq_mul, ha, mul_one]
  rw [max_eq_right (by linarith : (0 : ℝ) ≤ 1 - r)]

end QOU.MathlibExt.PL
