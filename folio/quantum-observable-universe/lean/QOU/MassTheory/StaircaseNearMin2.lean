import QOU.MassTheory.StaircaseNearMin

/-!
# Shapes two steps above the minimum, and `a₂`

Third step of the partition count behind `conj:cyclotomic-boundary-at-keystone`, after
`QOU.MassTheory.StaircaseNearMin` (the `δ = 1` count behind `a₁`). Here `m = k + 1`,
`n = T_m + r` and `N_min = N(stair m) + r m`.

* `nearMin2_classify`, `card_nearMin2`: every Young diagram with `N = N_min + 2` is
  `(stair m \ B) ∪ R ∪ C` with `C` on antidiagonal `m + 1`, `B` on antidiagonal `m - 1`,
  `|C| + |B| = 2`, `R` on antidiagonal `m` containing the cells below `C` and none above `B`.
  Nothing further out can occur.
* `sum_fill_20`, `sum_fill_11`, `sum_fill_02`, `card_nearMin2_eq`: the three families
  `(|C|, |B|) = (2,0), (1,1), (0,2)` counted in closed form.
* `sum_corners_minimisers`: the minimisers have `r C(m+1, r) + m C(m-1, r)` corners in total.
* `coeff_sum_expand_two`, `coeff_sum_sym_qHook_two`: in the symmetric normalisation the
  coefficient two steps below the top of `∑ q^(C(n,2)) dim_q λ` is
  `∑_{minimisers} (corners - 1) + #{N = N_min + 2}`, given the `q`-hook quotient `g λ` as a
  hypothesis (as in `coeff_sum_sym_qHook_of_eq`).

All counts are exact identities in `ℕ`; no numerical input enters.
-/

namespace QOU.Mass.StaircaseMinimisers

open Finset Finset.Nat

section Window

/-- The cells of antidiagonal `m` below some cell of `C`. -/
def predsSet (m : ℕ) (C : Finset (ℕ × ℕ)) : Finset (ℕ × ℕ) := C.biUnion (predsOf m)

/-- The cells of antidiagonal `m` above some cell of `B`. -/
def succsSet (m : ℕ) (B : Finset (ℕ × ℕ)) : Finset (ℕ × ℕ) := B.biUnion (succsOf m)

/-- Triples `(C, B, R)`: `C` on antidiagonal `m + 1`, `B` on `m - 1`, `R` on `m`, with
`|C| + |B| = 2`, `|R| + |C| = r + |B|`, `C` resting on `R`, and nothing of `R` above `B`. -/
def win2 (m r : ℕ) : Finset (Finset (ℕ × ℕ) × Finset (ℕ × ℕ) × Finset (ℕ × ℕ)) :=
  ((antidiagonal (m + 1)).powerset ×ˢ ((antidiagonal (m - 1)).powerset ×ˢ
    (antidiagonal m).powerset)).filter
    (fun t => t.1.card + t.2.1.card = 2 ∧ t.2.2.card + t.1.card = r + t.2.1.card ∧
      predsSet m t.1 ⊆ t.2.2 ∧ Disjoint (succsSet m t.2.1) t.2.2)

/-- The shape `(stair m \ B) ∪ R ∪ C`. -/
def shapeW (m : ℕ) (t : Finset (ℕ × ℕ) × Finset (ℕ × ℕ) × Finset (ℕ × ℕ)) : Finset (ℕ × ℕ) :=
  (stair m \ t.2.1 ∪ t.2.2) ∪ t.1

/-- The defining set of the `δ = 2` count. -/
noncomputable def nearMin2 (m r : ℕ) : Finset (Finset (ℕ × ℕ)) := by
  classical
  exact (shapes ((stair m).card + r)).filter (fun s => N s = N (stair m) + r * m + 2)

theorem mem_nearMin2 {m r : ℕ} {s : Finset (ℕ × ℕ)} :
    s ∈ nearMin2 m r ↔ s.card = (stair m).card + r ∧ IsLowerSet (s : Set (ℕ × ℕ)) ∧
      N s = N (stair m) + r * m + 2 := by
  classical
  simp [nearMin2, mem_shapes_iff, and_assoc]

theorem mem_win2 {m r : ℕ} {t : Finset (ℕ × ℕ) × Finset (ℕ × ℕ) × Finset (ℕ × ℕ)} :
    t ∈ win2 m r ↔ t.1 ⊆ antidiagonal (m + 1) ∧ t.2.1 ⊆ antidiagonal (m - 1) ∧
      t.2.2 ⊆ antidiagonal m ∧ t.1.card + t.2.1.card = 2 ∧
      t.2.2.card + t.1.card = r + t.2.1.card ∧
      predsSet m t.1 ⊆ t.2.2 ∧ Disjoint (succsSet m t.2.1) t.2.2 := by
  simp only [win2, mem_filter, mem_product, mem_powerset, and_assoc]

theorem sum_const_on {m : ℕ} {R : Finset (ℕ × ℕ)} (hR : R ⊆ antidiagonal m) :
    N R = R.card * m := by
  rw [N, sum_congr rfl (g := fun _ => m)
    (fun c hc => show val c = m from mem_antidiagonal.1 (hR hc)), sum_const, smul_eq_mul]

theorem shapeW_mem {m r : ℕ} (hm : 1 ≤ m) {t} (ht : t ∈ win2 m r) : shapeW m t ∈ nearMin2 m r := by
  obtain ⟨hC, hB, hR, h2, hcard, hpred, hdis⟩ := mem_win2.1 ht
  obtain ⟨C, B, R⟩ := t
  simp only at hC hB hR h2 hcard hpred hdis
  have hBst : B ⊆ stair m := fun b hb => mem_stair.2 (by
    have := mem_antidiagonal.1 (hB hb); simp only [val]; omega)
  have hd1 : Disjoint (stair m \ B) R :=
    Finset.disjoint_of_subset_left sdiff_subset (disjoint_stair hR)
  have hd2 : Disjoint (stair m \ B ∪ R) C := by
    rw [Finset.disjoint_left]
    intro x hx hxC
    have hv := mem_antidiagonal.1 (hC hxC)
    rcases mem_union.1 hx with h | h
    · have := mem_stair.1 (mem_sdiff.1 h).1; simp only [val] at this; omega
    · have := mem_antidiagonal.1 (hR h); omega
  have hNB : N (stair m \ B) + B.card * (m - 1) = N (stair m) := by
    have := sum_sdiff (f := val) hBst
    rw [← N, ← N] at this
    change _ = ∑ x ∈ stair m, val x
    rw [← this, sum_const_on hB]
  rw [mem_nearMin2, shapeW]
  simp only
  refine ⟨?_, ?_, ?_⟩
  · rw [card_union_of_disjoint hd2, card_union_of_disjoint hd1, card_sdiff_of_subset hBst]
    have : B.card ≤ (stair m).card := card_le_card hBst
    omega
  · intro a d hda ha
    simp only [coe_union, coe_sdiff, Set.mem_union, Set.mem_diff, mem_coe] at ha ⊢
    rcases eq_or_ne d a with rfl | hne
    · exact ha
    have hlt := val_lt_of_lt hda hne
    -- `d` is never in `B`
    have hdB : d ∈ B → False := by
      intro hdB
      have hdv := mem_antidiagonal.1 (hB hdB)
      rcases ha with (⟨ha, haB⟩ | ha) | ha
      · have := mem_stair.1 ha; simp only [val] at this hlt; omega
      · have hav := mem_antidiagonal.1 (hR ha)
        exact (Finset.disjoint_left.1 hdis) (mem_biUnion.2 ⟨d, hdB,
          mem_filter.2 ⟨mem_antidiagonal.2 hav, hda⟩⟩) ha
      · have hav := mem_antidiagonal.1 (hC ha)
        -- a cell between `d` and `a` on antidiagonal `m`
        obtain ⟨h1, h2⟩ := hda
        have : ∃ p : ℕ × ℕ, d ≤ p ∧ p ≤ a ∧ p.1 + p.2 = m := by
          by_cases hx : d.1 < a.1
          · exact ⟨(d.1 + 1, d.2), ⟨by simp, by simp⟩, ⟨by simp; omega, by simp; omega⟩,
              by simp; omega⟩
          · exact ⟨(d.1, d.2 + 1), ⟨by simp, by simp⟩, ⟨by simp; omega, by simp; omega⟩,
              by simp; omega⟩
        obtain ⟨p, hdp, hpa, hp⟩ := this
        have hpR : p ∈ R := hpred (mem_biUnion.2 ⟨a, ha, mem_filter.2 ⟨mem_antidiagonal.2 hp, hpa⟩⟩)
        exact (Finset.disjoint_left.1 hdis) (mem_biUnion.2 ⟨d, hdB,
          mem_filter.2 ⟨mem_antidiagonal.2 hp, hdp⟩⟩) hpR
    rcases Nat.lt_or_ge (val d) m with hdv | hdv
    · exact Or.inl (Or.inl ⟨mem_stair.2 hdv, hdB⟩)
    · -- `val d = m`, so `a ∈ C` and `d` is one of its predecessors
      rcases ha with (⟨ha, -⟩ | ha) | ha
      · have := mem_stair.1 ha; omega
      · have := mem_antidiagonal.1 (hR ha); simp only [val] at hlt hdv; omega
      · have hav := mem_antidiagonal.1 (hC ha)
        refine Or.inl (Or.inr (hpred (mem_biUnion.2 ⟨a, ha, mem_filter.2 ⟨?_, hda⟩⟩)))
        rw [mem_antidiagonal]; simp only [val] at hlt hdv; omega
  · rw [N, sum_union hd2, sum_union hd1, ← N, ← N, ← N, sum_const_on hR, sum_const_on hC]
    have hc : (R.card : ℤ) + C.card = r + B.card := by exact_mod_cast hcard
    have h2' : (C.card : ℤ) + B.card = 2 := by exact_mod_cast h2
    have hNB' : (N (stair m \ B) : ℤ) + B.card * ((m : ℤ) - 1) = N (stair m) := by
      have := congrArg (Nat.cast : ℕ → ℤ) hNB
      push_cast [Nat.cast_sub hm] at this
      exact this
    have : ((N (stair m \ B) + R.card * m + C.card * (m + 1) : ℕ) : ℤ) =
        ((N (stair m) + r * m + 2 : ℕ) : ℤ) := by
      push_cast
      linear_combination hNB' + (m : ℤ) * hc + h2'
    exact_mod_cast this

section Parts

variable {m : ℕ} {C B R : Finset (ℕ × ℕ)}

theorem shapeW_filter_gt (hC : C ⊆ antidiagonal (m + 1)) (hR : R ⊆ antidiagonal m) :
    (shapeW m (C, B, R)).filter (fun x => m < val x) = C := by
  ext x
  simp only [shapeW, mem_filter, mem_union, mem_sdiff, mem_stair]
  constructor
  · rintro ⟨(⟨h, -⟩ | h) | h, hv⟩
    · omega
    · have := mem_antidiagonal.1 (hR h); simp only [val] at hv; omega
    · exact h
  · intro h
    have := mem_antidiagonal.1 (hC h)
    exact ⟨Or.inr h, by simp only [val]; omega⟩

theorem shapeW_filter_eq (hC : C ⊆ antidiagonal (m + 1)) (hR : R ⊆ antidiagonal m) :
    (shapeW m (C, B, R)).filter (fun x => val x = m) = R := by
  ext x
  simp only [shapeW, mem_filter, mem_union, mem_sdiff, mem_stair]
  constructor
  · rintro ⟨(⟨h, -⟩ | h) | h, hv⟩
    · omega
    · exact h
    · have := mem_antidiagonal.1 (hC h); simp only [val] at hv; omega
  · intro h
    exact ⟨Or.inl (Or.inr h), mem_antidiagonal.1 (hR h)⟩

theorem stair_sdiff_shapeW (hB : B ⊆ antidiagonal (m - 1)) (hC : C ⊆ antidiagonal (m + 1))
    (hR : R ⊆ antidiagonal m) (hm : 1 ≤ m) : stair m \ shapeW m (C, B, R) = B := by
  ext x
  simp only [shapeW, mem_sdiff, mem_union, mem_stair, not_or, not_and, not_not]
  constructor
  · rintro ⟨hx, ⟨h1, -⟩, -⟩; exact h1 hx
  · intro h
    have hv := mem_antidiagonal.1 (hB h)
    refine ⟨by simp only [val]; omega, ⟨fun _ => h, fun hR' => ?_⟩, fun hC' => ?_⟩
    · have := mem_antidiagonal.1 (hR hR'); omega
    · have := mem_antidiagonal.1 (hC hC'); omega

theorem card_shapeW (hm : 1 ≤ m) (hB : B ⊆ antidiagonal (m - 1)) (hC : C ⊆ antidiagonal (m + 1))
    (hR : R ⊆ antidiagonal m) :
    (shapeW m (C, B, R)).card + B.card = (stair m).card + R.card + C.card := by
  have hBst : B ⊆ stair m := fun b hb => mem_stair.2 (by
    have := mem_antidiagonal.1 (hB hb); simp only [val]; omega)
  have hd1 : Disjoint (stair m \ B) R :=
    Finset.disjoint_of_subset_left sdiff_subset (disjoint_stair hR)
  have hd2 : Disjoint (stair m \ B ∪ R) C := by
    rw [Finset.disjoint_left]
    intro x hx hxC
    have hv := mem_antidiagonal.1 (hC hxC)
    rcases mem_union.1 hx with h | h
    · have := mem_stair.1 (mem_sdiff.1 h).1; simp only [val] at this; omega
    · have := mem_antidiagonal.1 (hR h); omega
  rw [shapeW, card_union_of_disjoint hd2, card_union_of_disjoint hd1, card_sdiff_of_subset hBst]
  have : B.card ≤ (stair m).card := card_le_card hBst
  omega

end Parts

theorem shapeW_injOn {m r : ℕ} (hm : 1 ≤ m) : Set.InjOn (shapeW m) (win2 m r) := by
  rintro ⟨C, B, R⟩ ht ⟨C', B', R'⟩ ht' h
  obtain ⟨hC, hB, hR, -⟩ := mem_win2.1 ht
  obtain ⟨hC', hB', hR', -⟩ := mem_win2.1 ht'
  simp only at hC hB hR hC' hB' hR'
  have e1 := shapeW_filter_gt (B := B) hC hR
  have e2 := shapeW_filter_eq (B := B) hC hR
  have e3 := stair_sdiff_shapeW hB hC hR hm
  rw [h] at e1 e2 e3
  rw [shapeW_filter_gt hC' hR'] at e1
  rw [shapeW_filter_eq hC' hR'] at e2
  rw [stair_sdiff_shapeW hB' hC' hR' hm] at e3
  rw [e1, e2, e3]

/-- **Classification of the shapes two cells above the minimum.** -/
theorem nearMin2_classify {m r : ℕ} (hm : 1 ≤ m) {s : Finset (ℕ × ℕ)} (hs : s ∈ nearMin2 m r) :
    ∃ t ∈ win2 m r, shapeW m t = s := by
  classical
  obtain ⟨hcard, hlow, hN⟩ := mem_nearMin2.1 hs
  have hd := delta_eq hcard
  set X := s.filter (fun c => m < val c) with hX
  set Y := stair m \ s with hY
  set f : ℕ × ℕ → ℤ := fun a => (val a : ℤ) - m with hf
  set g : ℕ × ℕ → ℤ := fun b => (m : ℤ) - val b with hg
  have hsum : ∑ a ∈ X, f a + ∑ b ∈ Y, g b = 2 := by
    rw [← hd, hN]; push_cast; ring
  have hf1 : ∀ a ∈ X, 1 ≤ f a := fun a ha => by
    have := (mem_filter.1 ha).2; simp only [hf]; omega
  have hg1 : ∀ b ∈ Y, 1 ≤ g b := fun b hb => by
    have := mem_stair.1 (mem_sdiff.1 hb).1; simp only [hg]; omega
  have hXn : 0 ≤ ∑ a ∈ X, f a := sum_nonneg (fun a ha => by linarith [hf1 a ha])
  have hYn : 0 ≤ ∑ b ∈ Y, g b := sum_nonneg (fun b hb => by linarith [hg1 b hb])
  -- the window: `X` lies on antidiagonal `m + 1`, `Y` on `m - 1`
  have hXw : ∀ x ∈ X, val x = m + 1 := by
    intro x hx
    have hxs := (mem_filter.1 hx).1
    have hxv := (mem_filter.1 hx).2
    by_contra hne
    have hge : m + 2 ≤ val x := by omega
    obtain ⟨y, hyx, hyne, hyv⟩ : ∃ y : ℕ × ℕ, y ≤ x ∧ y ≠ x ∧ val y + 1 = val x := by
      by_cases h0 : 0 < x.1
      · exact ⟨(x.1 - 1, x.2), ⟨by simp, by simp⟩, by
          intro h; have := congrArg Prod.fst h; simp at this; omega, by simp only [val]; omega⟩
      · have : 0 < x.2 := by simp only [val] at hge; omega
        exact ⟨(x.1, x.2 - 1), ⟨by simp, by simp⟩, by
          intro h; have := congrArg Prod.snd h; simp at this; omega, by simp only [val]; omega⟩
    have hyX : y ∈ X := mem_filter.2 ⟨hlow hyx hxs, by omega⟩
    have hsub : ({x, y} : Finset _) ⊆ X := by
      intro z hz; rcases mem_insert.1 hz with rfl | hz
      · exact hx
      · rw [mem_singleton] at hz; subst hz; exact hyX
    have := sum_le_sum_of_subset_of_nonneg (f := f) hsub (fun z hz _ => by linarith [hf1 z hz])
    rw [sum_pair (Ne.symm hyne)] at this
    have : (3 : ℤ) ≤ f x + f y := by simp only [hf]; omega
    linarith
  have hYw : ∀ y ∈ Y, val y + 1 = m := by
    intro y hy
    have hyst := mem_stair.1 (mem_sdiff.1 hy).1
    have hys := (mem_sdiff.1 hy).2
    by_contra hne
    set z : ℕ × ℕ := (y.1 + 1, y.2) with hz
    have hzv : val z = val y + 1 := by simp only [hz, val]; omega
    have hzY : z ∈ Y := by
      refine mem_sdiff.2 ⟨mem_stair.2 (by omega), fun hzs => hys ?_⟩
      exact hlow (show y ≤ z from ⟨by simp [hz], by simp [hz]⟩) hzs
    have hzne : z ≠ y := by intro h; have := congrArg Prod.fst h; simp [hz] at this
    have hsub : ({y, z} : Finset _) ⊆ Y := by
      intro w hw; rcases mem_insert.1 hw with rfl | hw
      · exact hy
      · rw [mem_singleton] at hw; subst hw; exact hzY
    have := sum_le_sum_of_subset_of_nonneg (f := g) hsub (fun w hw _ => by linarith [hg1 w hw])
    rw [sum_pair (Ne.symm hzne)] at this
    have : (3 : ℤ) ≤ g y + g z := by simp only [hg]; omega
    linarith
  have hXs : ∑ a ∈ X, f a = X.card := by
    rw [card_eq_sum_ones, Nat.cast_sum]
    exact sum_congr rfl (fun a ha => by simp only [hf]; rw [hXw a ha]; push_cast; ring)
  have hYs : ∑ b ∈ Y, g b = Y.card := by
    rw [card_eq_sum_ones, Nat.cast_sum]
    exact sum_congr rfl (fun b hb => by
      simp only [hg]; have := hYw b hb; push_cast; omega)
  have h2 : X.card + Y.card = 2 := by
    have : ((X.card + Y.card : ℕ) : ℤ) = 2 := by push_cast; linarith
    exact_mod_cast this
  set R := s.filter (fun x => val x = m) with hRdef
  have hXa : X ⊆ antidiagonal (m + 1) := fun x hx => mem_antidiagonal.2 (hXw x hx)
  have hYa : Y ⊆ antidiagonal (m - 1) := fun y hy => mem_antidiagonal.2 (by
    have := hYw y hy; simp only [val] at this; omega)
  have hRa : R ⊆ antidiagonal m := fun x hx => mem_antidiagonal.2 (mem_filter.1 hx).2
  have hseq : shapeW m (X, Y, R) = s := by
    ext x
    simp only [shapeW, mem_union, mem_sdiff]
    constructor
    · rintro ((⟨hx, hxY⟩ | hx) | hx)
      · by_contra hxs; exact hxY (mem_sdiff.2 ⟨hx, hxs⟩)
      · exact (mem_filter.1 hx).1
      · exact (mem_filter.1 hx).1
    · intro hx
      rcases lt_trichotomy (val x) m with h | h | h
      · exact Or.inl (Or.inl ⟨mem_stair.2 h, fun hxY => (mem_sdiff.1 hxY).2 hx⟩)
      · exact Or.inl (Or.inr (mem_filter.2 ⟨hx, h⟩))
      · exact Or.inr (mem_filter.2 ⟨hx, h⟩)
  refine ⟨(X, Y, R), mem_win2.2 ⟨hXa, hYa, hRa, h2, ?_, ?_, ?_⟩, hseq⟩
  · have := card_shapeW hm hYa hXa hRa
    rw [hseq, hcard] at this
    simp only
    omega
  · intro p hp
    obtain ⟨c, hc, hpc⟩ := mem_biUnion.1 hp
    rw [predsOf, mem_filter, mem_antidiagonal] at hpc
    exact mem_filter.2 ⟨hlow hpc.2 (mem_filter.1 hc).1, hpc.1⟩
  · rw [Finset.disjoint_left]
    intro d hd hdR
    obtain ⟨b, hb, hdb⟩ := mem_biUnion.1 hd
    rw [succsOf, mem_filter] at hdb
    exact (mem_sdiff.1 hb).2 (hlow hdb.2 (mem_filter.1 hdR).1)

/-- The `δ = 2` diagrams are in bijection with `win2 m r`. -/
theorem card_nearMin2 {m r : ℕ} (hm : 1 ≤ m) : (nearMin2 m r).card = (win2 m r).card := by
  classical
  have heq : nearMin2 m r = (win2 m r).image (shapeW m) := by
    ext s
    rw [mem_image]
    constructor
    · intro hs; exact nearMin2_classify hm hs
    · rintro ⟨t, ht, rfl⟩; exact shapeW_mem hm ht
  rw [heq, card_image_of_injOn (shapeW_injOn hm)]

section Count

/-- Number of `R ⊆ U` of size `k` containing `P` and avoiding `S`. -/
theorem card_filter_superset_disjoint {U P S : Finset (ℕ × ℕ)} (hP : P ⊆ U) (hS : S ⊆ U) (k : ℕ) :
    ((U.powersetCard k).filter (fun R => P ⊆ R ∧ Disjoint S R)).card =
      if Disjoint P S ∧ P.card ≤ k then (U.card - P.card - S.card).choose (k - P.card) else 0 := by
  classical
  by_cases hPS : Disjoint P S
  · have hPU : P ⊆ U \ S := fun x hx =>
      mem_sdiff.2 ⟨hP hx, fun hxS => Finset.disjoint_left.1 hPS hx hxS⟩
    have e : (U.powersetCard k).filter (fun R => P ⊆ R ∧ Disjoint S R) =
        ((U \ S).powersetCard k).filter (fun R => P ⊆ R) := by
      ext R
      simp only [mem_filter, mem_powersetCard, subset_sdiff]
      constructor
      · rintro ⟨⟨h1, h2⟩, h3, h4⟩; exact ⟨⟨⟨h1, h4.symm⟩, h2⟩, h3⟩
      · rintro ⟨⟨⟨h1, h4⟩, h2⟩, h3⟩; exact ⟨⟨h1, h2⟩, h3, h4.symm⟩
    rw [e, card_powersetCard_filter_superset hPU, card_sdiff_of_subset hS]
    by_cases hk : P.card ≤ k
    · rw [if_pos hk, if_pos ⟨hPS, hk⟩]; congr 1; omega
    · rw [if_neg hk, if_neg (fun h => hk h.2)]
  · rw [if_neg (fun h => hPS h.1), card_eq_zero, filter_eq_empty_iff]
    rintro R - ⟨h1, h2⟩
    exact hPS (Finset.disjoint_of_subset_left h1 h2.symm)

/-- The number of `R` that complete a given `(C, B)`. -/
def fill (m r : ℕ) (C B : Finset (ℕ × ℕ)) : ℕ :=
  if Disjoint (predsSet m C) (succsSet m B) ∧ (predsSet m C).card + C.card ≤ r + B.card then
    (m + 1 - (predsSet m C).card - (succsSet m B).card).choose
      (r + B.card - C.card - (predsSet m C).card)
  else 0

theorem predsSet_subset (m : ℕ) (C : Finset (ℕ × ℕ)) : predsSet m C ⊆ antidiagonal m :=
  biUnion_subset.2 (fun c _ => predsOf_subset m c)

theorem succsSet_subset (m : ℕ) (B : Finset (ℕ × ℕ)) : succsSet m B ⊆ antidiagonal m :=
  biUnion_subset.2 (fun b _ => succsOf_subset m b)

theorem card_fill (m r : ℕ) (C B : Finset (ℕ × ℕ)) :
    ((antidiagonal m).powerset.filter (fun R => R.card + C.card = r + B.card ∧
      predsSet m C ⊆ R ∧ Disjoint (succsSet m B) R)).card = fill m r C B := by
  classical
  by_cases hc : C.card ≤ r + B.card
  · have e : (antidiagonal m).powerset.filter (fun R => R.card + C.card = r + B.card ∧
        predsSet m C ⊆ R ∧ Disjoint (succsSet m B) R) =
        ((antidiagonal m).powersetCard (r + B.card - C.card)).filter
          (fun R => predsSet m C ⊆ R ∧ Disjoint (succsSet m B) R) := by
      ext R
      simp only [mem_filter, mem_powerset, mem_powersetCard]
      constructor
      · rintro ⟨h1, h2, h3⟩; exact ⟨⟨h1, by omega⟩, h3⟩
      · rintro ⟨⟨h1, h2⟩, h3⟩; exact ⟨h1, by omega, h3⟩
    rw [e, card_filter_superset_disjoint (predsSet_subset m C) (succsSet_subset m B),
      Nat.card_antidiagonal, fill]
    by_cases h : Disjoint (predsSet m C) (succsSet m B) ∧ (predsSet m C).card ≤ r + B.card - C.card
    · rw [if_pos h, if_pos ⟨h.1, by omega⟩]
    · rw [if_neg h, if_neg (fun h' => h ⟨h'.1, by omega⟩)]
  · rw [fill, if_neg (fun h => hc (by omega)), card_eq_zero, filter_eq_empty_iff]
    rintro R - ⟨h, -⟩; omega

/-- `win2 m r` split by the sizes of `C` and `B`. -/
theorem card_win2 (m r : ℕ) :
    (win2 m r).card =
      ∑ C ∈ (antidiagonal (m + 1)).powersetCard 2, fill m r C ∅ +
      ∑ c ∈ antidiagonal (m + 1), ∑ b ∈ antidiagonal (m - 1), fill m r {c} {b} +
      ∑ B ∈ (antidiagonal (m - 1)).powersetCard 2, fill m r ∅ B := by
  classical
  rw [win2, card_filter_product]
  simp only []
  have hin : ∀ C ∈ (antidiagonal (m + 1)).powerset,
      (((antidiagonal (m - 1)).powerset ×ˢ (antidiagonal m).powerset).filter
        (fun b => C.card + b.1.card = 2 ∧ b.2.card + C.card = r + b.1.card ∧
          predsSet m C ⊆ b.2 ∧ Disjoint (succsSet m b.1) b.2)).card =
      ∑ B ∈ (antidiagonal (m - 1)).powerset, if C.card + B.card = 2 then fill m r C B else 0 := by
    intro C _
    rw [card_filter_product]
    refine sum_congr rfl (fun B _ => ?_)
    split_ifs with h
    · rw [← card_fill]; congr 1; ext R; simp [h]
    · rw [card_eq_zero, filter_eq_empty_iff]; rintro R - ⟨h', -⟩; exact h h'
  rw [sum_congr rfl hin]
  have hsc : ∀ (U : Finset (ℕ × ℕ)) (k : ℕ) (f : Finset (ℕ × ℕ) → ℕ),
      ∑ C ∈ U.powerset, (if C.card = k then f C else 0) = ∑ C ∈ U.powersetCard k, f C := by
    intro U k f; rw [← sum_filter, powersetCard_eq_filter]
  have per : ∀ C : Finset (ℕ × ℕ),
      ∑ B ∈ (antidiagonal (m - 1)).powerset, (if C.card + B.card = 2 then fill m r C B else 0) =
        (if C.card = 2 then fill m r C ∅ else 0) +
        (if C.card = 1 then ∑ b ∈ antidiagonal (m - 1), fill m r C {b} else 0) +
        (if C.card = 0 then ∑ B ∈ (antidiagonal (m - 1)).powersetCard 2, fill m r ∅ B else 0) := by
    intro C
    rcases Nat.lt_or_ge C.card 3 with h3 | h3
    · interval_cases hC : C.card
      · rw [card_eq_zero] at hC; subst hC
        have : ∀ B : Finset (ℕ × ℕ), (if 0 + B.card = 2 then
            fill m r ∅ B else 0) = if B.card = 2 then fill m r ∅ B else 0 := by
          intro B; simp
        rw [sum_congr rfl (fun B _ => this B), hsc]; simp
      · have : ∀ B : Finset (ℕ × ℕ), (if 1 + B.card = 2 then fill m r C B else 0) =
            if B.card = 1 then fill m r C B else 0 := by
          intro B; congr 1; apply propext; omega
        rw [sum_congr rfl (fun B _ => this B), hsc, powersetCard_one, sum_map]; simp
      · have : ∀ B : Finset (ℕ × ℕ), (if 2 + B.card = 2 then fill m r C B else 0) =
            if B.card = 0 then fill m r C B else 0 := by
          intro B; congr 1; apply propext; omega
        rw [sum_congr rfl (fun B _ => this B), hsc, powersetCard_zero, sum_singleton]; simp
    · rw [if_neg (by omega), if_neg (by omega), if_neg (by omega)]
      apply sum_eq_zero; intro B _; rw [if_neg (by omega)]
  simp only [per, sum_add_distrib]
  rw [hsc, hsc, hsc, powersetCard_one, sum_map, powersetCard_zero, sum_singleton]
  rfl

end Count

end Window

theorem sum_powersetCard_two_range {M : Type*} [AddCommMonoid M] (f : Finset ℕ → M) (n : ℕ) :
    ∑ T ∈ (range n).powersetCard 2, f T = ∑ j ∈ range n, ∑ i ∈ range j, f {i, j} := by
  induction n with
  | zero => rw [range_zero, powersetCard_eq_empty.2 (by simp)]; simp
  | succ n ih =>
    rw [range_add_one, powersetCard_succ_insert (by simp), sum_union, ih, sum_insert (by simp),
      add_comm, sum_image]
    · congr 1
      rw [powersetCard_one, sum_map]
      refine sum_congr rfl (fun i hi => ?_)
      simp [pair_comm]
    · intro x hx y hy hxy
      simp only [coe_map, Set.mem_image, mem_coe, powersetCard_one] at hx hy
      obtain ⟨a, ha, rfl⟩ := hx; obtain ⟨b, hb, rfl⟩ := hy
      simp only [Function.Embedding.coeFn_mk] at hxy
      have : a ∈ insert n ({b} : Finset ℕ) := by rw [← hxy]; simp
      simp only [mem_insert, mem_singleton] at this
      rcases this with h | h
      · simp at ha; omega
      · rw [h]
    · rw [disjoint_left]
      intro T hT hT'
      rw [mem_image] at hT'
      obtain ⟨U, -, rfl⟩ := hT'
      have := (mem_powersetCard.1 hT).1 (mem_insert_self n U)
      simp at this

theorem sum_powersetCard_two_antidiagonal {M : Type*} [AddCommMonoid M]
    (f : Finset (ℕ × ℕ) → M) (L : ℕ) :
    ∑ T ∈ (antidiagonal L).powersetCard 2, f T =
      ∑ j ∈ range (L + 1), ∑ i ∈ range j, f {(i, L - i), (j, L - j)} := by
  rw [antidiagonal_eq_map, powersetCard_map, sum_map, sum_powersetCard_two_range]
  refine sum_congr rfl fun j _ => sum_congr rfl fun i _ => ?_
  congr 1; show map _ {i, j} = _; simp [map_insert]

theorem card_succsSet_pair {k i j : ℕ} (hij : i < j) (hj : j ≤ k) :
    (succsSet (k + 1) {(i, k - i), (j, k - j)}).card = if j = i + 1 then 3 else 4 := by
  rw [succsSet, biUnion_insert, singleton_biUnion, succsOf_eq (by omega : i + (k - i) + 1 = k + 1),
    succsOf_eq (by omega : j + (k - j) + 1 = k + 1), insert_union, singleton_union]
  split_ifs with h
  · subst h
    rw [card_insert_of_mem (by simp [Prod.ext_iff]; omega),
      card_insert_of_notMem (by simp [Prod.ext_iff]; omega), card_pair (by simp [Prod.ext_iff])]
  · rw [card_insert_of_notMem (by simp [Prod.ext_iff]; omega),
      card_insert_of_notMem (by simp [Prod.ext_iff]; omega), card_pair (by simp [Prod.ext_iff])]

theorem sum_adj_split (a b k : ℕ) :
    ∑ j ∈ range (k + 1), ∑ i ∈ range j, (if j = i + 1 then a else b) = k * a + k.choose 2 * b := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, ih, sum_range_succ, if_pos rfl]
    have : ∑ i ∈ range k, (if k + 1 = i + 1 then a else b) = k * b := by
      rw [sum_congr rfl (fun i hi => if_neg (by simp at hi; omega))]; simp
    rw [this, Nat.choose_succ_succ, Nat.choose_one_right]; ring

theorem predsSet_empty (m : ℕ) : predsSet m ∅ = ∅ := by simp [predsSet]
theorem succsSet_empty (m : ℕ) : succsSet m ∅ = ∅ := by simp [succsSet]

/-- **The `(0, 2)` family**: two cells of antidiagonal `m - 1` removed, `m = k + 1`. -/
theorem sum_fill_02 (k r : ℕ) :
    ∑ B ∈ (antidiagonal k).powersetCard 2, fill (k + 1) r ∅ B =
      k * (k - 1).choose (r + 2) + k.choose 2 * (k - 2).choose (r + 2) := by
  rw [sum_powersetCard_two_antidiagonal, ← sum_adj_split]
  refine sum_congr rfl fun j hj => sum_congr rfl fun i hi => ?_
  simp only [mem_range] at hi hj
  have hc : ({(i, k - i), (j, k - j)} : Finset (ℕ × ℕ)).card = 2 :=
    card_pair (by simp [Prod.ext_iff]; omega)
  rw [fill, predsSet_empty, card_empty, hc, if_pos ⟨disjoint_empty_left _, by omega⟩,
    card_succsSet_pair (by omega) (by omega)]
  split_ifs <;> congr 1

section Fst

theorem card_eq_card_image_fst {P : Finset (ℕ × ℕ)} {L : ℕ} (hP : P ⊆ antidiagonal L) :
    P.card = (P.image Prod.fst).card := by
  refine (card_image_of_injOn fun x hx y hy h => ?_).symm
  have hx' := mem_antidiagonal.1 (hP hx); have hy' := mem_antidiagonal.1 (hP hy)
  exact Prod.ext h (by have : x.1 = y.1 := h; omega)

theorem disjoint_iff_image_fst {P S : Finset (ℕ × ℕ)} {L : ℕ} (hP : P ⊆ antidiagonal L)
    (hS : S ⊆ antidiagonal L) : Disjoint P S ↔ Disjoint (P.image Prod.fst) (S.image Prod.fst) := by
  constructor
  · intro h
    rw [disjoint_left]
    intro x hx hx'
    obtain ⟨p, hp, rfl⟩ := mem_image.1 hx
    obtain ⟨s', hs, hps⟩ := mem_image.1 hx'
    have h1 := mem_antidiagonal.1 (hP hp); have h2 := mem_antidiagonal.1 (hS hs)
    have : s' = p := Prod.ext hps (by omega)
    exact disjoint_left.1 h hp (this ▸ hs)
  · intro h
    rw [disjoint_left]
    intro x hx hx'
    exact disjoint_left.1 h (mem_image_of_mem _ hx) (mem_image_of_mem _ hx')

theorem predsOf_image_fst {k i : ℕ} (hi : i ≤ k + 2) :
    (predsOf (k + 1) (i, k + 2 - i)).image Prod.fst = Icc (i - 1) (min i (k + 1)) := by
  ext x
  simp only [predsOf, mem_image, mem_filter, mem_antidiagonal, Prod.le_def, mem_Icc]
  constructor
  · rintro ⟨⟨a, b⟩, ⟨h1, h2, h3⟩, rfl⟩; simp only at *; omega
  · intro h; exact ⟨(x, k + 1 - x), ⟨by simp only; omega, by simp only; omega,
      by simp only; omega⟩, rfl⟩

theorem succsOf_image_fst {k b : ℕ} (hb : b ≤ k) :
    (succsOf (k + 1) (b, k - b)).image Prod.fst = Icc b (b + 1) := by
  ext x
  simp only [succsOf, mem_image, mem_filter, mem_antidiagonal, Prod.le_def, mem_Icc]
  constructor
  · rintro ⟨⟨a, c⟩, ⟨h1, h2, h3⟩, rfl⟩; simp only at *; omega
  · intro h; exact ⟨(x, k + 1 - x), ⟨by simp only; omega, by simp only; omega,
      by simp only; omega⟩, rfl⟩

end Fst

section Class20

theorem card_predsSet_pair {k i j : ℕ} (hij : i < j) (hj : j ≤ k + 2) :
    (predsSet (k + 1) {(i, k + 2 - i), (j, k + 2 - j)}).card =
      if j = i + 1 then min j (k + 1) + 1 - (i - 1)
      else (min i (k + 1) + 1 - (i - 1)) + (min j (k + 1) + 1 - (j - 1)) := by
  rw [predsSet, biUnion_insert, singleton_biUnion,
    card_eq_card_image_fst (union_subset (predsOf_subset _ _) (predsOf_subset _ _)), image_union,
    predsOf_image_fst (by omega), predsOf_image_fst hj]
  split_ifs with h
  · have : Icc (i - 1) (min i (k + 1)) ∪ Icc (j - 1) (min j (k + 1)) =
        Icc (i - 1) (min j (k + 1)) := by ext x; simp only [mem_union, mem_Icc]; omega
    rw [this, Nat.card_Icc]
  · rw [card_union_of_disjoint (by rw [disjoint_left]; intro x; simp only [mem_Icc]; omega),
      Nat.card_Icc, Nat.card_Icc]

theorem sum_F_split (G : ℕ → ℕ) (k : ℕ) :
    ∑ j ∈ range (k + 2), ∑ i ∈ range j,
      G (if j = i + 1 then j + 1 - (i - 1) else (i + 1 - (i - 1)) + (j + 1 - (j - 1))) =
      G 2 + 2 * k * G 3 + k.choose 2 * G 4 := by
  induction k with
  | zero => simp [sum_range_succ]
  | succ k ih =>
    rw [sum_range_succ, ih, sum_range_succ, sum_range_succ', if_pos rfl,
      if_neg (by omega : ¬ (k + 1 + 1 = 0 + 1))]
    have : ∑ i ∈ range k, G (if k + 1 + 1 = i + 1 + 1 then k + 1 + 1 + 1 - (i + 1 - 1)
        else (i + 1 + 1 - (i + 1 - 1)) + (k + 1 + 1 + 1 - (k + 1 + 1 - 1))) = k * G 4 := by
      rw [sum_congr rfl (fun i hi => (show _ = G 4 by
        simp only [mem_range] at hi; rw [if_neg (by omega)]; congr 1; omega))]
      simp
    rw [this, Nat.choose_succ_succ, Nat.choose_one_right]
    have e1 : k + 1 + 1 + 1 - (k + 1 - 1) = 3 := by omega
    have e2 : 0 + 1 - (0 - 1) + (k + 1 + 1 + 1 - (k + 1 + 1 - 1)) = 3 := by omega
    rw [e1, e2]; ring

/-- The value of `fill` on a pair of added cells and nothing removed. -/
def g20 (k r p : ℕ) : ℕ := if p + 2 ≤ r then (k + 2 - p).choose (r - 2 - p) else 0

theorem fill_C_empty {k r : ℕ} {C : Finset (ℕ × ℕ)} (hC : C.card = 2) :
    fill (k + 1) r C ∅ = g20 k r (predsSet (k + 1) C).card := by
  simp only [fill, g20, succsSet_empty, card_empty, disjoint_empty_right, true_and, hC]
  simp only [add_zero, Nat.sub_zero]

/-- **The `(2, 0)` family**: two cells of antidiagonal `m + 1` added, `m = k + 1`. -/
theorem sum_fill_20 (k r : ℕ) :
    ∑ C ∈ (antidiagonal (k + 2)).powersetCard 2, fill (k + 1) r C ∅ =
      3 * g20 k r 2 + 3 * k * g20 k r 3 + k.choose 2 * g20 k r 4 := by
  rw [sum_powersetCard_two_antidiagonal]
  have h1 : ∀ j ∈ range (k + 2 + 1), ∀ i ∈ range j,
      fill (k + 1) r {(i, k + 2 - i), (j, k + 2 - j)} ∅ =
        g20 k r (if j = i + 1 then min j (k + 1) + 1 - (i - 1)
          else (min i (k + 1) + 1 - (i - 1)) + (min j (k + 1) + 1 - (j - 1))) := by
    intro j hj i hi
    simp only [mem_range] at hi hj
    rw [fill_C_empty (card_pair (by simp [Prod.ext_iff]; omega)),
      card_predsSet_pair (by omega) (by omega)]
  rw [sum_congr rfl fun j hj => sum_congr rfl fun i hi => h1 j hj i hi, sum_range_succ]
  have h2 : ∀ j ∈ range (k + 2), ∑ i ∈ range j, g20 k r (if j = i + 1 then min j (k + 1) + 1 - (i - 1)
          else (min i (k + 1) + 1 - (i - 1)) + (min j (k + 1) + 1 - (j - 1))) =
      ∑ i ∈ range j, g20 k r (if j = i + 1 then j + 1 - (i - 1)
          else (i + 1 - (i - 1)) + (j + 1 - (j - 1))) := by
    intro j hj
    refine sum_congr rfl fun i hi => ?_
    simp only [mem_range] at hi hj
    rw [min_eq_left (by omega : i ≤ k + 1), min_eq_left (by omega : j ≤ k + 1)]
  rw [sum_congr rfl h2, sum_F_split, sum_range_succ, sum_range_succ', if_pos rfl,
    if_neg (by omega : ¬ (k + 2 = 0 + 1))]
  have h3 : ∑ i ∈ range k, g20 k r (if k + 2 = i + 1 + 1 then min (k + 2) (k + 1) + 1 - (i + 1 - 1)
      else (min (i + 1) (k + 1) + 1 - (i + 1 - 1)) + (min (k + 2) (k + 1) + 1 - (k + 2 - 1))) =
      k * g20 k r 3 := by
    rw [sum_congr rfl (fun i hi => (show _ = g20 k r 3 by
      simp only [mem_range] at hi
      rw [if_neg (by omega), min_eq_left (by omega : i + 1 ≤ k + 1),
        min_eq_right (by omega : k + 1 ≤ k + 2)]
      congr 1; omega))]
    simp
  rw [h3, min_eq_right (by omega : k + 1 ≤ k + 2), min_eq_left (by omega : 0 ≤ k + 1)]
  have e1 : k + 1 + 1 - (k + 1 - 1) = 2 := by omega
  have e2 : 0 + 1 - (0 - 1) + (k + 1 + 1 - (k + 2 - 1)) = 2 := by omega
  rw [e1, e2]; ring

end Class20

section Class11

theorem sum_pred_range (k : ℕ) : ∑ t ∈ range (k + 1), (t - 1) = k.choose 2 := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, ih, show (k + 1).choose 2 = k.choose 1 + k.choose 2 from
      Nat.choose_succ_succ k 1, Nat.choose_one_right]; omega

theorem sum_pred_range' (k : ℕ) : ∑ t ∈ range (k + 1), (k - 1 - t) = k.choose 2 := by
  rw [← sum_pred_range, ← sum_range_reflect]
  refine sum_congr rfl fun t ht => ?_
  simp only [mem_range] at ht; omega

theorem card_filter_gap {k t : ℕ} (ht : t ≤ k) :
    ((range (k + 1)).filter (fun b => b + 1 < t ∨ t + 1 < b)).card = (t - 1) + (k - 1 - t) := by
  have : (range (k + 1)).filter (fun b => b + 1 < t ∨ t + 1 < b) = range (t - 1) ∪ Ioc (t + 1) k := by
    ext b; simp only [mem_filter, mem_range, mem_union, mem_Ioc]; omega
  have hd : Disjoint (range (t - 1)) (Ioc (t + 1) k) := by
    rw [disjoint_left]; intro b; simp only [mem_range, mem_Ioc]; omega
  rw [this, card_union_of_disjoint hd, card_range, Nat.card_Ioc]
  omega

/-- The value of `fill` on one added and one removed cell. -/
def h11 (k r p : ℕ) : ℕ := if p ≤ r then (k - p).choose (r - p) else 0

theorem fill_one_one {k r i b : ℕ} (hi : i ≤ k + 2) (hb : b ≤ k) :
    fill (k + 1) r {(i, k + 2 - i)} {(b, k - b)} =
      if b + 1 < i - 1 ∨ min i (k + 1) < b then h11 k r (min i (k + 1) + 1 - (i - 1)) else 0 := by
  have hS : (succsSet (k + 1) {(b, k - b)}).card = 2 := by
    rw [succsSet, singleton_biUnion, card_eq_card_image_fst (succsOf_subset _ _),
      succsOf_image_fst hb, Nat.card_Icc]; omega
  have hP : (predsSet (k + 1) {(i, k + 2 - i)}).card = min i (k + 1) + 1 - (i - 1) := by
    rw [predsSet, singleton_biUnion, card_eq_card_image_fst (predsOf_subset _ _),
      predsOf_image_fst hi, Nat.card_Icc]
  have hD : Disjoint (predsSet (k + 1) {(i, k + 2 - i)}) (succsSet (k + 1) {(b, k - b)}) ↔
      b + 1 < i - 1 ∨ min i (k + 1) < b := by
    rw [predsSet, succsSet, singleton_biUnion, singleton_biUnion,
      disjoint_iff_image_fst (predsOf_subset _ _) (succsOf_subset _ _), predsOf_image_fst hi,
      succsOf_image_fst hb, disjoint_left]
    simp only [mem_Icc]
    constructor
    · intro h
      by_contra hc
      push_neg at hc
      by_cases h' : i - 1 ≤ b
      · exact h ⟨h', by omega⟩ ⟨le_refl b, by omega⟩
      · exact h ⟨le_refl (i - 1), by omega⟩ ⟨by omega, by omega⟩
    · intro h x hx hx'; omega
  rw [fill, hS, hP, card_singleton, card_singleton, h11]
  by_cases hd : b + 1 < i - 1 ∨ min i (k + 1) < b
  · rw [if_pos hd]
    by_cases hr : min i (k + 1) + 1 - (i - 1) ≤ r
    · rw [if_pos ⟨hD.2 hd, by omega⟩, if_pos hr]; congr 1; omega
    · rw [if_neg (fun h => hr (by omega)), if_neg hr]
  · rw [if_neg hd, if_neg (fun h => hd (hD.1 h.1))]

/-- **The `(1, 1)` family**: one cell added on antidiagonal `m + 1`, one removed on `m - 1`. -/
theorem sum_fill_11 (k r : ℕ) :
    ∑ c ∈ antidiagonal (k + 2), ∑ b ∈ antidiagonal k, fill (k + 1) r {c} {b} =
      2 * k * h11 k r 1 + 2 * k.choose 2 * h11 k r 2 := by
  rw [antidiagonal_eq_map (k + 2), sum_map]
  simp only [antidiagonal_eq_map k, sum_map, Function.Embedding.coeFn_mk]
  have h1 : ∀ i ∈ range (k + 2 + 1), ∑ b ∈ range (k + 1), fill (k + 1) r {(i, k + 2 - i)} {(b, k - b)} =
      ((range (k + 1)).filter (fun b => b + 1 < i - 1 ∨ min i (k + 1) < b)).card *
        h11 k r (min i (k + 1) + 1 - (i - 1)) := by
    intro i hi
    simp only [mem_range] at hi
    rw [sum_congr rfl fun b hb => fill_one_one (by omega) (by simp at hb; omega), ← sum_filter,
      sum_const, smul_eq_mul]
  rw [sum_congr rfl h1, sum_range_succ, sum_range_succ']
  have hlast : ((range (k + 1)).filter (fun b => b + 1 < k + 2 - 1 ∨ min (k + 2) (k + 1) < b)).card
      = k := by
    rw [show (range (k + 1)).filter (fun b => b + 1 < k + 2 - 1 ∨ min (k + 2) (k + 1) < b) =
      range k by ext b; simp only [mem_filter, mem_range]; omega, card_range]
  have hfirst : ((range (k + 1)).filter (fun b => b + 1 < 0 - 1 ∨ min 0 (k + 1) < b)).card = k := by
    rw [show (range (k + 1)).filter (fun b => b + 1 < 0 - 1 ∨ min 0 (k + 1) < b) =
      Icc 1 k by ext b; simp only [mem_filter, mem_range, mem_Icc]; omega, Nat.card_Icc]; omega
  have hmid : ∀ t ∈ range (k + 1),
      ((range (k + 1)).filter (fun b => b + 1 < t + 1 - 1 ∨ min (t + 1) (k + 1) < b)).card *
        h11 k r (min (t + 1) (k + 1) + 1 - (t + 1 - 1)) = ((t - 1) + (k - 1 - t)) * h11 k r 2 := by
    intro t ht
    simp only [mem_range] at ht
    rw [min_eq_left (by omega : t + 1 ≤ k + 1), show t + 1 - 1 = t by omega,
      show t + 1 + 1 - t = 2 by omega, ← card_filter_gap (by omega : t ≤ k)]
  rw [hlast, hfirst, sum_congr rfl hmid, ← sum_mul, sum_add_distrib, sum_pred_range,
    sum_pred_range', min_eq_right (by omega : k + 1 ≤ k + 2), min_eq_left (by omega : 0 ≤ k + 1)]
  rw [show k + 1 + 1 - (k + 2 - 1) = 1 by omega, show 0 + 1 - (0 - 1) = 1 by omega]
  ring

end Class11

/-- **The number of shapes two steps above the minimum**, `m = k + 1`. -/
theorem card_nearMin2_eq (k r : ℕ) :
    (nearMin2 (k + 1) r).card =
      (3 * g20 k r 2 + 3 * k * g20 k r 3 + k.choose 2 * g20 k r 4) +
      (2 * k * h11 k r 1 + 2 * k.choose 2 * h11 k r 2) +
      (k * (k - 1).choose (r + 2) + k.choose 2 * (k - 2).choose (r + 2)) := by
  rw [card_nearMin2 (by omega), card_win2, Nat.add_sub_cancel, show k + 1 + 1 = k + 2 from rfl,
    sum_fill_20, sum_fill_11, sum_fill_02]

section Corners

theorem hook_eq_one_iff {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ))) (c : ℕ × ℕ) :
    hook s c = 1 ↔ (c.1, c.2 + 1) ∉ s ∧ (c.1 + 1, c.2) ∉ s := by
  have low : ∀ {a b : ℕ × ℕ}, b ≤ a → a ∈ s → b ∈ s := fun h ha => hs h ha
  rw [hook, arm, leg]
  constructor
  · intro h
    have h1 : (s.filter (fun d => d.1 = c.1 ∧ c.2 < d.2)).card = 0 := by omega
    have h2 : (s.filter (fun d => d.2 = c.2 ∧ c.1 < d.1)).card = 0 := by omega
    rw [card_eq_zero, filter_eq_empty_iff] at h1 h2
    exact ⟨fun hm => h1 hm ⟨rfl, by omega⟩, fun hm => h2 hm ⟨rfl, by omega⟩⟩
  · rintro ⟨h1, h2⟩
    have e1 : (s.filter (fun d => d.1 = c.1 ∧ c.2 < d.2)).card = 0 := by
      rw [card_eq_zero, filter_eq_empty_iff]
      rintro d hd ⟨hd1, hd2⟩
      exact h1 (low (Prod.le_def.2 ⟨hd1.ge, by omega⟩) hd)
    have e2 : (s.filter (fun d => d.2 = c.2 ∧ c.1 < d.1)).card = 0 := by
      rw [card_eq_zero, filter_eq_empty_iff]
      rintro d hd ⟨hd1, hd2⟩
      exact h2 (low (Prod.le_def.2 ⟨by omega, hd1.ge⟩) hd)
    omega

/-- The corners of a minimiser `stair m ∪ R` are the cells of `R` and the cells of antidiagonal
`m - 1` neither of whose two successors lies in `R`. -/
theorem corners_stair_union {k : ℕ} {R : Finset (ℕ × ℕ)} (hR : R ⊆ antidiagonal (k + 1)) :
    (stair (k + 1) ∪ R).filter (fun c => hook (stair (k + 1) ∪ R) c = 1) =
      R ∪ (antidiagonal k).filter (fun b => Disjoint (succsOf (k + 1) b) R) := by
  have hlow := isLowerSet_stair_union hR
  ext c
  simp only [mem_filter, hook_eq_one_iff hlow, mem_union, mem_stair, val, mem_antidiagonal]
  have hRv : ∀ {d : ℕ × ℕ}, d ∈ R → d.1 + d.2 = k + 1 := fun hd => mem_antidiagonal.1 (hR hd)
  constructor
  · rintro ⟨hc | hc, h1, h2⟩
    · right
      have hk : c.1 + c.2 = k := by
        by_contra hne
        exact h1 (Or.inl (by omega))
      refine ⟨hk, ?_⟩
      rw [succsOf_eq (by omega : c.1 + c.2 + 1 = k + 1), disjoint_left]
      intro d hd hdR
      simp only [mem_insert, mem_singleton] at hd
      rcases hd with rfl | rfl
      · exact h2 (Or.inr hdR)
      · exact h1 (Or.inr hdR)
    · left; exact hc
  · rintro (hc | ⟨hk, hd⟩)
    · have := hRv hc
      refine ⟨Or.inr hc, ?_, ?_⟩ <;> rintro (h | h)
      · omega
      · have := hRv h; omega
      · omega
      · have := hRv h; omega
    · rw [succsOf_eq (by omega : c.1 + c.2 + 1 = k + 1), disjoint_left] at hd
      refine ⟨Or.inl (by omega), ?_, ?_⟩ <;> rintro (h | h)
      · omega
      · exact hd (by simp) h
      · omega
      · exact hd (by simp) h

theorem card_corners_stair_union {k : ℕ} {R : Finset (ℕ × ℕ)} (hR : R ⊆ antidiagonal (k + 1)) :
    ((stair (k + 1) ∪ R).filter (fun c => hook (stair (k + 1) ∪ R) c = 1)).card =
      R.card + ((antidiagonal k).filter (fun b => Disjoint (succsOf (k + 1) b) R)).card := by
  rw [corners_stair_union hR, card_union_of_disjoint]
  rw [disjoint_left]
  intro c hc hc'
  have h1 := mem_antidiagonal.1 (hR hc)
  have h2 := mem_antidiagonal.1 (mem_filter.1 hc').1
  omega

/-- The minimisers are exactly `stair m ∪ R` for `R` an `r`-subset of antidiagonal `m`. -/
theorem minimisers_eq_image {m r : ℕ} (hr : r ≤ m + 1) :
    (shapes ((stair m).card + r)).filter (fun s => N s = N (stair m) + r * m) =
      ((antidiagonal m).powersetCard r).image (stair m ∪ ·) := by
  ext s
  rw [mem_filter, mem_image, mem_shapes_iff]
  constructor
  · rintro ⟨⟨hc, -⟩, hN⟩
    obtain ⟨R, hR, hRc, rfl⟩ := (N_eq_iff hr hc).1 hN
    exact ⟨R, mem_powersetCard.2 ⟨hR, hRc⟩, rfl⟩
  · rintro ⟨R, hR, rfl⟩
    rw [mem_powersetCard] at hR
    refine ⟨⟨by rw [card_union_of_disjoint (disjoint_stair hR.1), hR.2],
      isLowerSet_stair_union hR.1⟩, by rw [N_stair_union hR.1, hR.2]⟩

/-- **Total number of corners over the minimisers**, `m = k + 1`. -/
theorem sum_corners_minimisers {k r : ℕ} (hr : r ≤ k + 2) :
    ∑ s ∈ (shapes ((stair (k + 1)).card + r)).filter
        (fun s => N s = N (stair (k + 1)) + r * (k + 1)),
      (s.filter (fun c => hook s c = 1)).card = r * (k + 2).choose r + (k + 1) * k.choose r := by
  rw [minimisers_eq_image (by omega), sum_image]
  · rw [sum_congr rfl fun R hR => card_corners_stair_union (mem_powersetCard.1 hR).1,
      sum_add_distrib, sum_congr rfl fun R hR => (mem_powersetCard.1 hR).2, sum_const,
      card_powersetCard, Nat.card_antidiagonal, smul_eq_mul]
    simp only [card_eq_sum_ones, sum_filter]
    rw [sum_comm]
    simp only [← sum_filter, ← card_eq_sum_ones]
    rw [sum_congr rfl fun b hb => (show _ = k.choose r by
      rw [card_powersetCard_filter_disjoint (succsOf_subset _ _) r,
        succsOf_eq (by have := mem_antidiagonal.1 hb; omega : b.1 + b.2 + 1 = k + 1),
        card_pair (by simp [Prod.ext_iff]), Nat.card_antidiagonal]; congr 1)]
    rw [sum_const, Nat.card_antidiagonal, smul_eq_mul, mul_comm r]
  · intro R hR R' hR' h
    have d1 := disjoint_stair (mem_powersetCard.1 (mem_coe.1 hR)).1
    have d2 := disjoint_stair (mem_powersetCard.1 (mem_coe.1 hR')).1
    have : (stair (k + 1) ∪ R) \ stair (k + 1) = (stair (k + 1) ∪ R') \ stair (k + 1) := by
      simp only at h; rw [h]
    rwa [union_sdiff_left, union_sdiff_left, d1.sdiff_eq_right, d2.sdiff_eq_right] at this

end Corners

section Coeff2

open Polynomial

/-- **The coefficient two steps below the top, symmetric normalisation.** With
`F i = X^(N i) · g i (X²)` as in `coeff_sum_expand_eq_card`, the coefficient of `∑ F i` at
`2M - N_min - 2` is the sum of the next coefficients of the `g i` over the minimisers, plus the
number of `i` with `N i = N_min + 2`. -/
theorem coeff_sum_expand_two {ι : Type*} (I : Finset ι) (Nf : ι → ℕ) (g : ι → ℤ[X])
    (M Nmin : ℕ) (hlt : Nmin + 1 ≤ M) (hM : ∀ i ∈ I, Nf i ≤ M) (hmin : ∀ i ∈ I, Nmin ≤ Nf i)
    (hmon : ∀ i ∈ I, (g i).Monic) (hdeg : ∀ i ∈ I, (g i).natDegree = M - Nf i) :
    (∑ i ∈ I, X ^ Nf i * expand ℤ 2 (g i)).coeff (2 * M - Nmin - 2) =
      ∑ i ∈ I.filter (fun i => Nf i = Nmin), (g i).nextCoeff +
        ((I.filter (fun i => Nf i = Nmin + 2)).card : ℤ) := by
  classical
  rw [finset_sum_coeff, card_eq_sum_ones, Nat.cast_sum, sum_filter, sum_filter, ← sum_add_distrib]
  refine sum_congr rfl (fun i hi => ?_)
  have h1 := hM i hi
  have h2 := hmin i hi
  have h3 := hdeg i hi
  rw [coeff_X_pow_mul', coeff_expand (by norm_num)]
  by_cases h : Nf i = Nmin
  · have e1 : Nf i ≤ 2 * M - Nmin - 2 := by omega
    have e2 : 2 ∣ 2 * M - Nmin - 2 - Nf i := ⟨M - Nmin - 1, by omega⟩
    have e3 : ¬ (Nf i = Nmin + 2) := by omega
    rw [if_pos e1, if_pos e2, if_pos h, if_neg e3, add_zero, nextCoeff,
      if_neg (by omega)]
    congr 1; omega
  · rw [if_neg h, zero_add]
    by_cases h' : Nf i = Nmin + 2
    · have e1 : Nf i ≤ 2 * M - Nmin - 2 := by omega
      have e2 : 2 ∣ 2 * M - Nmin - 2 - Nf i := ⟨M - Nf i, by omega⟩
      rw [if_pos e1, if_pos e2, if_pos h']
      have : (2 * M - Nmin - 2 - Nf i) / 2 = (g i).natDegree := by omega
      rw [this, (hmon i hi).coeff_natDegree]; simp
    · rw [if_neg h']
      split_ifs with ha hb
      · apply coeff_eq_zero_of_natDegree_lt
        rcases Nat.lt_or_ge (Nf i) (Nmin + 2) with hlt' | hge
        · exfalso
          have hN : Nf i = Nmin + 1 := by omega
          obtain ⟨c, hc⟩ := hb
          omega
        · omega
      · rfl
      · rfl

/-- `N_min + 1 ≤ C(n, 2)` once `n ≥ 3`. -/
theorem Nmin_succ_le {k r : ℕ} (h3 : 2 ≤ k + r) :
    N (stair (k + 1)) + r * (k + 1) + 1 ≤
      ((stair (k + 1)).card + r) * ((stair (k + 1)).card + r - 1) / 2 := by
  have hN := three_mul_N_stair k
  have hT := two_mul_card_stair (k + 1)
  set T := (stair (k + 1)).card
  set Nn := N (stair (k + 1))
  rw [Nat.le_div_iff_mul_le (by norm_num)]
  have hT1 : 1 ≤ T := by nlinarith
  obtain ⟨p, hp⟩ : ∃ p, T + r = p + 1 := ⟨T + r - 1, by omega⟩
  rw [hp, Nat.add_sub_cancel]
  rcases Nat.eq_zero_or_pos k with rfl | hk
  · have hT1 : T = 1 := by omega
    have hN0 : Nn = 0 := by omega
    nlinarith
  · have hB : 3 ≤ T := by nlinarith
    have hA : 4 * k + 5 ≤ 3 * T := by nlinarith
    have hC : 6 * k + 9 ≤ 6 * T := by nlinarith
    have h6 : 6 * Nn = 4 * k * T := by nlinarith
    nlinarith [Nat.mul_le_mul hA hB, Nat.mul_le_mul_left r hC]

/-- **`a₂` as a coefficient**, `m = k + 1`, `n = T_m + r`, `n ≥ 3`. With `g λ` the quotient
`[n]! / ∏ [h]` (given as the hypothesis `hg`), the coefficient of `∑ X^(N λ) g λ (X²)` two steps
below the top is `∑_{minimisers} (corners - 1)` plus the number of shapes with
`N = N_min + 2`. -/
theorem coeff_sum_sym_qHook_two (k r : ℕ) (hr : 1 ≤ r) (hr' : r ≤ k + 2) (h3 : 2 ≤ k + r)
    (g : Finset (ℕ × ℕ) → ℤ[X])
    (hg : ∀ s ∈ shapes ((stair (k + 1)).card + r),
      qfact ((stair (k + 1)).card + r) = g s * hookProd s) :
    (∑ s ∈ shapes ((stair (k + 1)).card + r), X ^ N s * expand ℤ 2 (g s)).coeff
        (2 * (((stair (k + 1)).card + r) * ((stair (k + 1)).card + r - 1) / 2) -
          (N (stair (k + 1)) + r * (k + 1)) - 2) =
      ((r * (k + 2).choose r + (k + 1) * k.choose r : ℕ) : ℤ) - ((k + 2).choose r : ℤ) +
      (((3 * g20 k r 2 + 3 * k * g20 k r 3 + k.choose 2 * g20 k r 4) +
        (2 * k * h11 k r 1 + 2 * k.choose 2 * h11 k r 2) +
        (k * (k - 1).choose (r + 2) + k.choose 2 * (k - 2).choose (r + 2)) : ℕ) : ℤ) := by
  classical
  set n := (stair (k + 1)).card + r with hn
  have key : ∀ s ∈ shapes n, (g s).Monic ∧ (g s).natDegree = n * (n - 1) / 2 - N s ∧
      N s ≤ n * (n - 1) / 2 := by
    intro s hs
    obtain ⟨hcard, hlow⟩ := mem_shapes_iff.1 hs
    have := qHook_top_of_eq hlow (hcard ▸ hg s hs)
    rw [hcard] at this
    exact this
  rw [coeff_sum_expand_two _ N g _ _ (Nmin_succ_le h3) (fun s hs => (key s hs).2.2)
    (fun s hs => le_N_of_card (by omega) (mem_shapes_iff.1 hs).1) (fun s hs => (key s hs).1)
    (fun s hs => (key s hs).2.1)]
  have hnext : ∀ s ∈ (shapes n).filter (fun s => N s = N (stair (k + 1)) + r * (k + 1)),
      (g s).nextCoeff = ((s.filter (fun c => hook s c = 1)).card : ℤ) - 1 := by
    intro s hs
    have hs' := (mem_filter.1 hs).1
    obtain ⟨hcard, hlow⟩ := mem_shapes_iff.1 hs'
    have hne : s.Nonempty := card_pos.1 (by omega)
    exact qHook_nextCoeff_of_eq hlow hne (hcard ▸ hg s hs')
  rw [sum_congr rfl hnext, sum_sub_distrib, ← Nat.cast_sum, sum_corners_minimisers hr', sum_const,
    nsmul_eq_mul, mul_one, card_minimisers hr hr', ← card_nearMin2_eq k r]
  rfl

end Coeff2

end QOU.Mass.StaircaseMinimisers
