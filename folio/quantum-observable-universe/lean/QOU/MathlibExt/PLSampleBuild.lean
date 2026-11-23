/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLSampleGeom

set_option autoImplicit false

/-!
# Building a sample (issue #8902, C¹ bridge)

A finite set `S ⊆ [0, 1)` of times, enumerated in order, is a sample in the sense of
`Polygon.IsSample` once its points are `γ`-separated, stay below `1 - γ`, contain `0` and the
vertex times, and each is followed within `Γ` by another point or by `1`.

## What is a THEOREM here

* `Polygon.isSample_of_finset` — the criterion above.
* `Polygon.ofFn_sampled` — the vertex list of the sampled polygon is `Q.sampleVerts S`.
* `Polygon.exists_fill` — a `2/p`-separated set of times extends, by a grid of step `1/p`, to a
  set meeting the criterion with `γ = 1/p`, `Γ = 3/p`.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

namespace Polygon

variable {Q : Polygon E}

/-- **A separated finite set of times is a sample.** -/
theorem isSample_of_finset (S : Finset ℝ) {m : ℕ} (hcard : S.card = m + 1) {γ Γ : ℝ}
    (hγ : 0 < γ) (hS : ∀ x ∈ S, 0 ≤ x ∧ x ≤ 1 - γ) (h0 : (0 : ℝ) ∈ S)
    (hV : Q.vertexTimes ⊆ S) (hsep : ∀ x ∈ S, ∀ y ∈ S, x < y → γ ≤ y - x)
    (hnext : ∀ x ∈ S, ∃ y, x < y ∧ y ≤ x + Γ ∧ (y ∈ S ∨ y = 1)) :
    Q.IsSample (fun k => S.orderEmbOfFin hcard k) γ Γ := by
  set σ : Fin (m + 1) → ℝ := fun k => S.orderEmbOfFin hcard k with hσ
  have hmono : StrictMono σ := (S.orderEmbOfFin hcard).strictMono
  have hmem : ∀ k, σ k ∈ S := fun k => S.orderEmbOfFin_mem hcard k
  have hrange : ∀ x ∈ S, ∃ k, σ k = x := fun x hx => by
    have : x ∈ Set.range (S.orderEmbOfFin hcard) := by
      rw [S.range_orderEmbOfFin hcard]; exact hx
    obtain ⟨k, hk⟩ := this
    exact ⟨k, hk⟩
  have hz : σ 0 = 0 := by
    obtain ⟨k, hk⟩ := hrange 0 h0
    have h1 : σ 0 ≤ σ k := hmono.monotone (Fin.zero_le k)
    have h2 := (hS _ (hmem 0)).1
    linarith
  refine ⟨hmono, (hS _ (hmem 0)).1, ?_, ?_, ?_, ?_⟩
  · linarith [(hS _ (hmem (Fin.last m))).2]
  · intro i
    exact hrange _ (hV (Finset.mem_image_of_mem _ (Finset.mem_univ i)))
  · intro k
    by_cases hk : k = Fin.last m
    · simp only [snext, hk, if_true, finRotate_last, hz]
      linarith [(hS _ (hmem (Fin.last m))).2]
    · rw [IsSample.snext_of_ne hk]
      refine hsep _ (hmem k) _ (hmem _) (hmono ?_)
      rw [Fin.lt_iff_val_lt_val, coe_finRotate_of_ne_last hk]; omega
  · intro k
    obtain ⟨y, hy1, hy2, hy3⟩ := hnext _ (hmem k)
    by_cases hk : k = Fin.last m
    · simp only [snext, hk, if_true, finRotate_last, hz]
      rcases hy3 with hy | rfl
      · obtain ⟨j, rfl⟩ := hrange y hy
        rw [hk] at hy1
        exact absurd (hmono.lt_iff_lt.mp hy1) (not_lt.mpr (Fin.le_last j))
      · rw [hk] at hy2; linarith
    · rw [IsSample.snext_of_ne hk]
      have hle : σ (finRotate (m + 1) k) ≤ y := by
        rcases hy3 with hy | rfl
        · obtain ⟨j, rfl⟩ := hrange y hy
          apply hmono.monotone
          have := hmono.lt_iff_lt.mp hy1
          rw [Fin.le_iff_val_le_val, coe_finRotate_of_ne_last hk]
          rw [Fin.lt_iff_val_lt_val] at this; omega
        · linarith [(hS _ (hmem (finRotate (m + 1) k))).2]
      linarith

/-- The vertex list of the sampled polygon is `Q.sampleVerts S`. -/
theorem ofFn_sampled (S : Finset ℝ) {m : ℕ} (hcard : S.card = m + 1) (hm : 2 ≤ m) :
    List.ofFn (Q.sampled hm (fun k => S.orderEmbOfFin hcard k)).v = Q.sampleVerts S := by
  apply List.ext_getElem
  · simp [sampleVerts, sampled, hcard]
  · intro n h1 h2
    rw [List.getElem_ofFn]
    simp only [sampleVerts, sampled, Finset.orderEmbOfFin_apply, List.getElem_map]
    rfl

/-- **Filling a separated set of times with a grid.** A finite `R ⊆ [0, 1 - 2/p]` containing
`0` with points `2/p` apart extends to a `1/p`-separated `S ⊆ [0, 1 - 1/p]` in which every point
is followed within `3/p` by another point or by `1`. -/
theorem exists_fill (R : Finset ℝ) {p : ℕ} (hp : 0 < p)
    (hR : ∀ x ∈ R, 0 ≤ x ∧ x ≤ 1 - 2 / p) (hRsep : ∀ x ∈ R, ∀ y ∈ R, x < y → 2 / p ≤ y - x) :
    ∃ S : Finset ℝ, R ⊆ S ∧ (∀ x ∈ S, 0 ≤ x ∧ x ≤ 1 - 1 / p) ∧
      (∀ x ∈ S, ∀ y ∈ S, x < y → 1 / p ≤ y - x) ∧
      (∀ x ∈ S, ∃ y, x < y ∧ y ≤ x + 3 / p ∧ (y ∈ S ∨ y = 1)) := by
  classical
  have hpR : (0 : ℝ) < p := by exact_mod_cast hp
  set γ : ℝ := 1 / p with hγ
  have hγ0 : 0 < γ := by positivity
  have h2γ : 2 / (p : ℝ) = 2 * γ := by rw [hγ]; ring
  have h3γ : 3 / (p : ℝ) = 3 * γ := by rw [hγ]; ring
  rw [h2γ] at hR hRsep
  rw [h3γ]
  set R' := insert (1 : ℝ) R with hR'
  have hR'sep : ∀ a ∈ R', ∀ b ∈ R', a < b → 2 * γ ≤ b - a := by
    intro a ha b hb hab
    rcases Finset.mem_insert.mp ha with rfl | ha <;> rcases Finset.mem_insert.mp hb with rfl | hb
    · exact absurd hab (lt_irrefl _)
    · linarith [(hR b hb).2]
    · linarith [(hR a ha).2]
    · exact hRsep a ha b hb hab
  set G := (Finset.range p).image fun j : ℕ => (j : ℝ) / p with hG
  set keep : ℝ → Prop := fun g => ∀ r ∈ R', γ ≤ |g - r| with hkeep
  set S := R ∪ G.filter keep with hS
  have hgrid : ∀ j : ℕ, j < p → (j : ℝ) / p ∈ G := fun j hj =>
    Finset.mem_image.mpr ⟨j, Finset.mem_range.mpr hj, rfl⟩
  have hjγ : ∀ j : ℕ, (j : ℝ) / p = j * γ := fun j => by rw [hγ]; ring
  have hmemS : ∀ g ∈ G, keep g → g ∈ S := fun g hg hk =>
    Finset.mem_union_right _ (Finset.mem_filter.mpr ⟨hg, hk⟩)
  refine ⟨S, Finset.subset_union_left, ?_, ?_, ?_⟩
  · intro x hx
    rcases Finset.mem_union.mp hx with hx | hx
    · exact ⟨(hR x hx).1, by linarith [(hR x hx).2]⟩
    · obtain ⟨hxG, hxk⟩ := Finset.mem_filter.mp hx
      obtain ⟨j, hj, rfl⟩ := Finset.mem_image.mp hxG
      have hj' : (j : ℝ) < p := by exact_mod_cast Finset.mem_range.mp hj
      have h1 := hxk 1 (Finset.mem_insert_self _ _)
      have hlt : (j : ℝ) / p < 1 := by rw [div_lt_one hpR]; exact hj'
      rw [abs_of_neg (by linarith)] at h1
      exact ⟨by positivity, by linarith⟩
  · intro x hx y hy hxy
    rcases Finset.mem_union.mp hx with hx | hx <;> rcases Finset.mem_union.mp hy with hy | hy
    · linarith [hRsep x hx y hy hxy]
    · have := (Finset.mem_filter.mp hy).2 x (Finset.mem_insert_of_mem hx)
      rwa [abs_of_pos (by linarith)] at this
    · have := (Finset.mem_filter.mp hx).2 y (Finset.mem_insert_of_mem hy)
      rwa [abs_of_neg (by linarith), neg_sub] at this
    · obtain ⟨i, -, rfl⟩ := Finset.mem_image.mp (Finset.mem_filter.mp hx).1
      obtain ⟨j, -, rfl⟩ := Finset.mem_image.mp (Finset.mem_filter.mp hy).1
      rw [hjγ, hjγ] at hxy ⊢
      have hij : (i : ℝ) < j := lt_of_mul_lt_mul_right hxy hγ0.le
      have : i < j := by exact_mod_cast hij
      have : (i : ℝ) + 1 ≤ j := by exact_mod_cast this
      nlinarith
  · intro x hx
    have hx1 : x ≤ 1 - γ := by
      rcases Finset.mem_union.mp hx with hx | hx
      · linarith [(hR x hx).2]
      · obtain ⟨hxG, hxk⟩ := Finset.mem_filter.mp hx
        obtain ⟨j, hj, rfl⟩ := Finset.mem_image.mp hxG
        have hj' : (j : ℝ) < p := by exact_mod_cast Finset.mem_range.mp hj
        have h1 := hxk 1 (Finset.mem_insert_self _ _)
        have hlt : (j : ℝ) / p < 1 := by rw [div_lt_one hpR]; exact hj'
        rw [abs_of_neg (by linarith)] at h1
        linarith
    have hx0 : 0 ≤ x := by
      rcases Finset.mem_union.mp hx with hx | hx
      · exact (hR x hx).1
      · obtain ⟨j, -, rfl⟩ := Finset.mem_image.mp (Finset.mem_filter.mp hx).1; positivity
    set j := ⌊x * p⌋₊ + 1 with hjdef
    have hj1 : x * p < j := by rw [hjdef]; push_cast; exact Nat.lt_floor_add_one _
    have hj2 : (j : ℝ) ≤ x * p + 1 := by
      rw [hjdef]; push_cast; linarith [Nat.floor_le (mul_nonneg hx0 hpR.le)]
    have hg1a : x < j * γ := by rw [hγ, ← div_eq_mul_one_div, lt_div_iff₀ hpR]; exact hj1
    have hg1b : (j : ℝ) * γ ≤ x + γ := by
      rw [hγ, ← div_eq_mul_one_div, div_le_iff₀ hpR, add_mul, one_div_mul_cancel hpR.ne']; linarith
    -- a helper: a grid point below `1` that is not kept has a nearby point of `R'`
    have hcase : ∀ i : ℕ, x < i * γ → (i : ℝ) * γ ≤ x + 3 * γ →
        (∃ y, x < y ∧ y ≤ x + 3 * γ ∧ (y ∈ S ∨ y = 1)) ∨
          ∃ r ∈ R', |(i : ℝ) * γ - r| < γ := by
      intro i hi1 hi2
      by_cases hip : i < p
      · by_cases hk : keep ((i : ℝ) / p)
        · exact Or.inl ⟨i * γ, hi1, hi2, Or.inl (by rw [← hjγ]; exact hmemS _ (hgrid i hip) hk)⟩
        · right
          simp only [keep, not_forall, not_le] at hk
          obtain ⟨r, hr, hr'⟩ := hk
          exact ⟨r, hr, by rwa [← hjγ]⟩
      · have : (p : ℝ) ≤ i := by exact_mod_cast not_lt.mp hip
        have h1 : 1 ≤ (i : ℝ) * γ := by
          rw [hγ, ← div_eq_mul_one_div, le_div_iff₀ hpR]; linarith
        exact Or.inl ⟨1, by linarith, by linarith, Or.inr rfl⟩
    have hR'S : ∀ r ∈ R', r ∈ S ∨ r = 1 := fun r hr => by
      rcases Finset.mem_insert.mp hr with rfl | hr
      · exact Or.inr rfl
      · exact Or.inl (Finset.mem_union_left _ hr)
    rcases hcase j hg1a (by linarith) with h | ⟨r, hr, hrj⟩
    · exact h
    rw [abs_lt] at hrj
    by_cases hrx : x < r
    · exact ⟨r, hrx, by linarith, hR'S r hr⟩
    push_neg at hrx
    have hg2a : x < ((j + 1 : ℕ) : ℝ) * γ := by push_cast; linarith
    have hg2b : ((j + 1 : ℕ) : ℝ) * γ ≤ x + 3 * γ := by push_cast; linarith
    rcases hcase (j + 1) hg2a hg2b with h | ⟨r', hr', hrj'⟩
    · exact h
    push_cast at hrj'
    rw [abs_lt] at hrj'
    have hne : r < r' := by
      by_contra hle
      push_neg at hle
      rcases hle.lt_or_eq with hlt | heq
      · have := hR'sep r' hr' r hr hlt; linarith
      · rw [heq] at hrj'; linarith
    have := hR'sep r hr r' hr' hne
    exact ⟨r', by linarith, by linarith, hR'S r' hr'⟩

end Polygon

end QOU.MathlibExt.PL
