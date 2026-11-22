/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLParamBiLip
import QOU.MathlibExt.PLInscribed

set_option autoImplicit false

/-!
# Geometry of a sampled polygon (issue #8902, C¹ bridge)

Sample a simple polygon `Q` at increasing times `σ 0 < σ 1 < … < σ m` in `[0, 1)` that include
every vertex time, with consecutive gaps (cyclically) between `γ` and `Γ`. The sampled polygon
`Q.sampled hm σ` has vertices `Q.param (σ k)`. This file proves the fine data that
`Polygon.isSimple_image` asks for: short edges, separated non-adjacent edges, and a uniform
angle bound at every vertex.

## What is a DEFINITION here

* `Polygon.sampled` — the polygon with vertices `Q.param (σ k)`.
* `Polygon.snext` — the time of the next sample, lifted past `1` at the last vertex.
* `Polygon.IsSample` — the sampling hypotheses.

## What is a THEOREM here

* `IsSample.piece` — each sampled edge lies on one edge of `Q`.
* `IsSample.edge_param` — points of a sampled edge are `Q.param` of the matching times.
* `IsSample.edge_len` — `‖edge‖ ≤ (n + 1) · Lm · gap`.
* `IsSample.injective` — the sampled vertices are distinct.
* `IsSample.sep` — non-adjacent sampled edges are `c γ` apart.
* `IsSample.angle` — a uniform angle bound `c / ((n + 1) Lm)` at every sampled vertex.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

namespace Polygon

/-- The polygon whose vertices are `Q.param (σ k)`. -/
noncomputable def sampled (Q : Polygon E) {m : ℕ} (hm : 2 ≤ m) (σ : Fin (m + 1) → ℝ) :
    Polygon E where
  n := m
  two_le := hm
  v k := Q.param (σ k)

/-- The time of the next sample, lifted by `1` at the last vertex. -/
def snext {m : ℕ} (σ : Fin (m + 1) → ℝ) (k : Fin (m + 1)) : ℝ :=
  σ (finRotate (m + 1) k) + if k = Fin.last m then 1 else 0

/-- The sampling hypotheses. -/
structure IsSample (Q : Polygon E) {m : ℕ} (σ : Fin (m + 1) → ℝ) (γ Γ : ℝ) : Prop where
  mono : StrictMono σ
  nonneg : 0 ≤ σ 0
  lt_one : σ (Fin.last m) < 1
  vert : ∀ i, ∃ k, σ k = Q.vtime i
  gap_ge : ∀ k, γ ≤ snext σ k - σ k
  gap_le : ∀ k, snext σ k - σ k ≤ Γ

namespace IsSample

variable {Q : Polygon E} {m : ℕ} {σ : Fin (m + 1) → ℝ} {γ Γ : ℝ} (hS : Q.IsSample σ γ Γ)
include hS

lemma zero_eq : σ 0 = 0 := by
  obtain ⟨k, hk⟩ := hS.vert 0
  have h1 : σ 0 ≤ σ k := hS.mono.monotone (Fin.zero_le k)
  have hv : Q.vtime 0 = 0 := by simp [vtime]
  rw [hv] at hk
  linarith [hS.nonneg]

lemma mem (k : Fin (m + 1)) : 0 ≤ σ k ∧ σ k < 1 :=
  ⟨hS.nonneg.trans (hS.mono.monotone (Fin.zero_le k)),
    (hS.mono.monotone (Fin.le_last k)).trans_lt hS.lt_one⟩

omit hS in
lemma snext_of_ne {k : Fin (m + 1)} (hk : k ≠ Fin.last m) :
    snext σ k = σ (finRotate (m + 1) k) := by
  simp [snext, hk]

lemma snext_last : snext σ (Fin.last m) = 1 := by
  simp [snext, hS.zero_eq]

lemma lt_snext (k : Fin (m + 1)) : σ k < snext σ k := by
  by_cases hk : k = Fin.last m
  · rw [hk, hS.snext_last]; exact hS.lt_one
  · rw [snext_of_ne hk]
    apply hS.mono
    rw [Fin.lt_iff_val_lt_val, coe_finRotate_of_ne_last hk]
    omega

lemma snext_le_one (k : Fin (m + 1)) : snext σ k ≤ 1 := by
  by_cases hk : k = Fin.last m
  · rw [hk, hS.snext_last]
  · rw [snext_of_ne hk]; exact (hS.mem _).2.le

omit hS in
lemma param_snext (k : Fin (m + 1)) : Q.param (snext σ k) = Q.param (σ (finRotate (m + 1) k)) := by
  by_cases hk : k = Fin.last m
  · simp only [snext, hk, if_true]; exact Q.param_add_one _
  · rw [snext_of_ne hk]

/-- **Each sampled edge lies on one edge of `Q`.** -/
lemma piece (k : Fin (m + 1)) : ∃ (i : Fin (Q.n + 1)) (a b : ℝ), 0 ≤ a ∧ a ≤ b ∧ b ≤ 1 ∧
    σ k = ((i : ℝ) + a) / (Q.n + 1) ∧ snext σ k = ((i : ℝ) + b) / (Q.n + 1) := by
  obtain ⟨i, a, ha0, ha1, hk⟩ := Q.exists_piece (hS.mem k).1 (hS.mem k).2
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  refine ⟨i, a, (Q.n + 1) * snext σ k - i, ha0, ?_, ?_, hk, by field_simp; ring⟩
  · have := hS.lt_snext k
    rw [hk, div_lt_iff₀ hN] at this
    linarith
  · suffices h : snext σ k ≤ ((i : ℝ) + 1) / (Q.n + 1) by
      rw [le_div_iff₀ hN] at h; linarith
    by_cases hi : (i : ℕ) + 1 < Q.n + 1
    · obtain ⟨k', hk'⟩ := hS.vert ⟨i + 1, hi⟩
      have hvt : Q.vtime ⟨i + 1, hi⟩ = ((i : ℝ) + 1) / (Q.n + 1) := by simp [vtime]
      rw [hvt] at hk'
      have hlt : σ k < σ k' := by
        rw [hk, hk']; exact (div_lt_div_iff_of_pos_right hN).mpr (by linarith)
      have hkk : k < k' := hS.mono.lt_iff_lt.mp hlt
      have hkl : k ≠ Fin.last m := fun h => by
        rw [h] at hkk; exact absurd hkk (not_lt.mpr (Fin.le_last _))
      rw [snext_of_ne hkl, ← hk']
      apply hS.mono.monotone
      rw [Fin.le_iff_val_le_val, coe_finRotate_of_ne_last hkl]
      rw [Fin.lt_iff_val_lt_val] at hkk
      omega
    · have : (i : ℝ) + 1 = Q.n + 1 := by
        have := i.isLt; norm_cast; omega
      rw [this, div_self hN.ne']; exact hS.snext_le_one k

/-- **Points of a sampled edge are `Q.param` of the matching times.** -/
lemma edge_param (hm : 2 ≤ m) (k : Fin (m + 1)) {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1) :
    (Q.sampled hm σ).v k + r • ((Q.sampled hm σ).v ((Q.sampled hm σ).next k) -
      (Q.sampled hm σ).v k) = Q.param (σ k + r * (snext σ k - σ k)) := by
  obtain ⟨i, a, b, ha0, hab, hb1, hk, hk'⟩ := hS.piece k
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  have hvk : (Q.sampled hm σ).v k = Q.v i + a • (Q.v (Q.next i) - Q.v i) := by
    show Q.param (σ k) = _; rw [hk]; exact Q.param_local i ha0 (hab.trans hb1)
  have hvk' : (Q.sampled hm σ).v ((Q.sampled hm σ).next k) =
      Q.v i + b • (Q.v (Q.next i) - Q.v i) := by
    show Q.param (σ (finRotate (m + 1) k)) = _
    rw [← param_snext k, hk']; exact Q.param_local i (ha0.trans hab) hb1
  have ht : σ k + r * (snext σ k - σ k) = ((i : ℝ) + (a + r * (b - a))) / (Q.n + 1) := by
    rw [hk, hk']; field_simp; ring
  rw [hvk, hvk', ht, Q.param_local i (by nlinarith [mul_nonneg hr0 (sub_nonneg.mpr hab)])
    (by nlinarith [mul_le_mul_of_nonneg_right hr1 (sub_nonneg.mpr hab)])]
  module

/-- **Sampled edges are short.** -/
lemma edge_len (hm : 2 ≤ m) {Lm : ℝ} (hL : ∀ i, ‖Q.v (Q.next i) - Q.v i‖ ≤ Lm)
    (k : Fin (m + 1)) :
    ‖(Q.sampled hm σ).v ((Q.sampled hm σ).next k) - (Q.sampled hm σ).v k‖ ≤
      (Q.n + 1) * Lm * (snext σ k - σ k) := by
  obtain ⟨i, a, b, ha0, hab, hb1, hk, hk'⟩ := hS.piece k
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  have hvk : (Q.sampled hm σ).v k = Q.v i + a • (Q.v (Q.next i) - Q.v i) := by
    show Q.param (σ k) = _; rw [hk]; exact Q.param_local i ha0 (hab.trans hb1)
  have hvk' : (Q.sampled hm σ).v ((Q.sampled hm σ).next k) =
      Q.v i + b • (Q.v (Q.next i) - Q.v i) := by
    show Q.param (σ (finRotate (m + 1) k)) = _
    rw [← param_snext k, hk']; exact Q.param_local i (ha0.trans hab) hb1
  have hg : snext σ k - σ k = (b - a) / (Q.n + 1) := by rw [hk, hk']; ring
  rw [hvk, hvk', show Q.v i + b • (Q.v (Q.next i) - Q.v i) - (Q.v i + a • (Q.v (Q.next i) - Q.v i))
    = (b - a) • (Q.v (Q.next i) - Q.v i) by module, norm_smul, Real.norm_eq_abs,
    abs_of_nonneg (sub_nonneg.mpr hab), hg]
  calc (b - a) * ‖Q.v (Q.next i) - Q.v i‖ ≤ (b - a) * Lm :=
        mul_le_mul_of_nonneg_left (hL i) (sub_nonneg.mpr hab)
    _ = (Q.n + 1) * Lm * ((b - a) / (Q.n + 1)) := by field_simp

/-- **The sampled vertices are distinct.** -/
lemma injective (hQ : Q.IsSimple) (hm : 2 ≤ m) : Function.Injective (Q.sampled hm σ).v := by
  obtain ⟨c, hc0, hc⟩ := hQ.exists_param_lower
  intro k l hkl
  have h : Q.param (σ k) = Q.param (σ l) := hkl
  have hk := hS.mem k
  have hl := hS.mem l
  have h1 := hc (σ k) (σ l) hk.1 hk.2.le hl.1 hl.2.le
  rw [h, sub_self, norm_zero] at h1
  have hlt : |σ k - σ l| < 1 := by rw [abs_lt]; constructor <;> linarith
  have hmin : min |σ k - σ l| (1 - |σ k - σ l|) ≤ 0 := by
    by_contra hne
    push_neg at hne
    have := mul_pos hc0 hne
    linarith
  have h0 : |σ k - σ l| ≤ 0 := by
    rcases min_le_iff.mp hmin with h | h
    · exact h
    · linarith
  exact hS.mono.injective (sub_eq_zero.mp (abs_nonpos_iff.mp h0))

/-- Times on two non-adjacent sampled edges, in order, differ by an amount in `[γ, 1 - γ]`. -/
lemma time_sep (hm : 2 ≤ m) {k l : Fin (m + 1)} (hkl : k < l)
    (h1 : l ≠ finRotate (m + 1) k) (h2 : k ≠ finRotate (m + 1) l) {x y : ℝ}
    (hx0 : σ k ≤ x) (hx1 : x ≤ snext σ k) (hy0 : σ l ≤ y) (hy1 : y ≤ snext σ l) :
    γ ≤ y - x ∧ y - x ≤ 1 - γ := by
  have hk : k ≠ Fin.last m := fun h => by
    rw [h] at hkl; exact absurd hkl (not_lt.mpr (Fin.le_last _))
  have hk1v : ((finRotate (m + 1) k : Fin (m + 1)) : ℕ) = k + 1 := coe_finRotate_of_ne_last hk
  have hlv : (k : ℕ) < l := hkl
  have hne : (l : ℕ) ≠ k + 1 := fun h => h1 (Fin.ext (by rw [hk1v]; exact h))
  have hk1l : finRotate (m + 1) k < l := by rw [Fin.lt_iff_val_lt_val, hk1v]; omega
  have hk1' : finRotate (m + 1) k ≠ Fin.last m := fun h => by
    rw [h] at hk1l; exact absurd hk1l (not_lt.mpr (Fin.le_last _))
  have hk2v : ((finRotate (m + 1) (finRotate (m + 1) k) : Fin (m + 1)) : ℕ) = k + 2 := by
    rw [coe_finRotate_of_ne_last hk1', hk1v]
  have hg1 := hS.gap_ge (finRotate (m + 1) k)
  rw [snext_of_ne hk1'] at hg1
  have hσ2 : σ (finRotate (m + 1) (finRotate (m + 1) k)) ≤ σ l :=
    hS.mono.monotone (by rw [Fin.le_iff_val_le_val, hk2v]; omega)
  rw [snext_of_ne hk] at hx1
  constructor
  · linarith
  · by_cases hl : l = Fin.last m
    · have hl0 : finRotate (m + 1) l = 0 := by rw [hl]; exact finRotate_last
      have hk0 : (k : ℕ) ≠ 0 := fun h => h2 (by rw [hl0]; exact Fin.ext (by simpa using h))
      have h0 : (0 : Fin (m + 1)) ≠ Fin.last m := fun h => by
        have := congrArg Fin.val h; simp at this; omega
      have hg0 := hS.gap_ge 0
      rw [snext_of_ne h0, hS.zero_eq] at hg0
      have h3 : σ (finRotate (m + 1) 0) ≤ σ k := hS.mono.monotone (by
        rw [Fin.le_iff_val_le_val, coe_finRotate_of_ne_last h0]; simp only [Fin.val_zero]; omega)
      rw [hl, hS.snext_last] at hy1
      linarith
    · have hgl := hS.gap_ge (Fin.last m)
      rw [hS.snext_last] at hgl
      rw [snext_of_ne hl] at hy1
      have h3 : σ (finRotate (m + 1) l) ≤ σ (Fin.last m) := hS.mono.monotone (Fin.le_last _)
      have h4 : σ 0 ≤ σ k := hS.mono.monotone (Fin.zero_le _)
      rw [hS.zero_eq] at h4
      linarith

lemma mem_edge_time (hm : 2 ≤ m) {k : Fin (m + 1)} {a : E} (ha : a ∈ (Q.sampled hm σ).edge k) :
    ∃ x, σ k ≤ x ∧ x ≤ snext σ k ∧ a = Q.param x := by
  obtain ⟨r, ⟨hr0, hr1⟩, rfl⟩ := ((Q.sampled hm σ).mem_edge_iff).mp ha
  have hg : 0 ≤ snext σ k - σ k := (sub_pos.mpr (hS.lt_snext k)).le
  refine ⟨σ k + r * (snext σ k - σ k), by nlinarith, by nlinarith, hS.edge_param hm k hr0 hr1⟩

/-- **Non-adjacent sampled edges are separated.** -/
lemma sep (hm : 2 ≤ m) {c : ℝ}
    (hc : ∀ γ s t : ℝ, 0 ≤ γ → γ ≤ t - s → t - s ≤ 1 - γ → c * γ ≤ ‖Q.param s - Q.param t‖)
    (hγ : 0 ≤ γ) (k l : Fin (m + 1)) (hkl : k ≠ l) (h1 : l ≠ (Q.sampled hm σ).next k)
    (h2 : k ≠ (Q.sampled hm σ).next l) :
    ∀ a ∈ (Q.sampled hm σ).edge k, ∀ b ∈ (Q.sampled hm σ).edge l, c * γ ≤ ‖a - b‖ := by
  intro a ha b hb
  obtain ⟨x, hx0, hx1, rfl⟩ := hS.mem_edge_time hm ha
  obtain ⟨y, hy0, hy1, rfl⟩ := hS.mem_edge_time hm hb
  rcases lt_or_gt_of_ne hkl with h | h
  · obtain ⟨h3, h4⟩ := hS.time_sep hm h h1 h2 hx0 hx1 hy0 hy1
    exact hc γ x y hγ h3 h4
  · obtain ⟨h3, h4⟩ := hS.time_sep hm h h2 h1 hy0 hy1 hx0 hx1
    rw [norm_sub_rev]; exact hc γ y x hγ h3 h4

/-- **A uniform angle bound at every sampled vertex.** -/
lemma angle (hm : 2 ≤ m) {c Lm : ℝ} (hc0 : 0 < c) (hLm : 0 < Lm)
    (hc : ∀ γ s t : ℝ, 0 ≤ γ → γ ≤ t - s → t - s ≤ 1 - γ → c * γ ≤ ‖Q.param s - Q.param t‖)
    (hL : ∀ i, ‖Q.v (Q.next i) - Q.v i‖ ≤ Lm) (hΓ : Γ ≤ 1 / 4) (k : Fin (m + 1))
    (α β : ℝ) (hα : 0 ≤ α) (hβ : 0 ≤ β) :
    c / ((Q.n + 1) * Lm) * (α * ‖(Q.sampled hm σ).v k - (Q.sampled hm σ).v
        ((Q.sampled hm σ).next k)‖ + β * ‖(Q.sampled hm σ).v ((Q.sampled hm σ).next
        ((Q.sampled hm σ).next k)) - (Q.sampled hm σ).v ((Q.sampled hm σ).next k)‖) ≤
      ‖α • ((Q.sampled hm σ).v k - (Q.sampled hm σ).v ((Q.sampled hm σ).next k)) -
        β • ((Q.sampled hm σ).v ((Q.sampled hm σ).next ((Q.sampled hm σ).next k)) -
          (Q.sampled hm σ).v ((Q.sampled hm σ).next k))‖ := by
  set P := Q.sampled hm σ with hP
  set k' := P.next k with hk'
  set k'' := P.next k' with hk''
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  set K := (Q.n + 1) * Lm with hK
  have hK0 : 0 < K := by positivity
  set g := snext σ k - σ k with hgdef
  set g' := snext σ k' - σ k' with hg'def
  have hg0 : 0 ≤ g := (sub_pos.mpr (hS.lt_snext k)).le
  have hg'0 : 0 ≤ g' := (sub_pos.mpr (hS.lt_snext k')).le
  have hgΓ : g ≤ Γ := hS.gap_le k
  have hg'Γ : g' ≤ Γ := hS.gap_le k'
  have hu : ‖P.v k - P.v k'‖ ≤ K * g := by
    rw [norm_sub_rev]; exact hS.edge_len hm hL k
  have hw : ‖P.v k'' - P.v k'‖ ≤ K * g' := hS.edge_len hm hL k'
  by_cases hz : max α β = 0
  · have hα0 : α = 0 := le_antisymm (hz ▸ le_max_left α β) hα
    have hβ0 : β = 0 := le_antisymm (hz ▸ le_max_right α β) hβ
    simp [hα0, hβ0]
  have hlam : 0 < max α β := lt_of_le_of_ne (le_max_of_le_left hα) (Ne.symm hz)
  set lam := max α β with hlamdef
  set α' := α / lam
  set β' := β / lam
  have hα'0 : 0 ≤ α' := div_nonneg hα hlam.le
  have hβ'0 : 0 ≤ β' := div_nonneg hβ hlam.le
  have hα'1 : α' ≤ 1 := (div_le_one hlam).mpr (le_max_left _ _)
  have hβ'1 : β' ≤ 1 := (div_le_one hlam).mpr (le_max_right _ _)
  have hαe : α = lam * α' := by simp only [α']; field_simp
  have hβe : β = lam * β' := by simp only [β']; field_simp
  have hp := hS.edge_param hm k (r := 1 - α') (by linarith) (by linarith)
  have hq := hS.edge_param hm k' (r := β') hβ'0 hβ'1
  set x := σ k + (1 - α') * g
  set y := σ k' + β' * g'
  set j : ℝ := if k = Fin.last m then 1 else 0 with hj
  have hsj : snext σ k = σ k' + j := rfl
  have hpx : Q.param (x - j) = Q.param x := by
    by_cases hkl : k = Fin.last m
    · simp only [hj, hkl, if_true]
      have := Q.param_add_one (x - 1); rw [sub_add_cancel] at this; exact this.symm
    · simp only [hj, hkl, if_false, sub_zero]
  set T := α' * g + β' * g'
  have hT : y - (x - j) = T := by simp only [y, x, T, hgdef]; rw [hsj]; ring
  have hT0 : 0 ≤ T := by positivity
  have hT1 : T ≤ 1 / 2 := by
    have : α' * g ≤ Γ := (mul_le_of_le_one_left hg0 hα'1).trans hgΓ
    have : β' * g' ≤ Γ := (mul_le_of_le_one_left hg'0 hβ'1).trans hg'Γ
    simp only [T]; linarith
  have hnear : c * T ≤ ‖Q.param (x - j) - Q.param y‖ :=
    hc T (x - j) y hT0 hT.ge (by rw [hT]; linarith)
  rw [hpx, ← hp, ← hq] at hnear
  have hrhs : α • (P.v k - P.v k') - β • (P.v k'' - P.v k') =
      lam • ((P.v k + (1 - α') • (P.v k' - P.v k)) - (P.v k' + β' • (P.v k'' - P.v k'))) := by
    rw [hαe, hβe]; module
  rw [hrhs, norm_smul, Real.norm_eq_abs, abs_of_pos hlam]
  calc c / K * (α * ‖P.v k - P.v k'‖ + β * ‖P.v k'' - P.v k'‖)
      ≤ c / K * (α * (K * g) + β * (K * g')) := by
        gcongr
    _ = lam * (c * T) := by simp only [T]; rw [hαe, hβe]; field_simp
    _ ≤ _ := mul_le_mul_of_nonneg_left hnear hlam.le

end IsSample

end Polygon

end QOU.MathlibExt.PL
