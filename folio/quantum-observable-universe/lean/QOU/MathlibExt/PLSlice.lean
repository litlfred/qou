/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLTriangulation
import Mathlib.Analysis.Convex.Combination
import Mathlib.Tactic.Module

set_option autoImplicit false

/-!
# Slicing by a hyperplane (issue #8902, Moise build part A, for part B's Schoenflies)

A hyperplane `{ψ = c}` that misses the vertices of a simplex cuts it in the convex hull of the
points where it crosses the edges.

## What is a DEFINITION here

* `crossPt ψ c u v` — the point of the line `u v` where `ψ = c`:
  `(ψ v - ψ u)⁻¹ • ((ψ v - c) • u - (ψ u - c) • v)`.
* `crossSet ψ c s` — the crossing points `crossPt ψ c u v` over `u, v ∈ s` with
  `ψ u < c < ψ v`.

## What is a THEOREM here

* `map_crossPt`, `crossPt_mem_segment` — `crossPt` lies on the hyperplane and on the segment.
* `convexHull_inter_hyperplane` — **the slice of a simplex**: if `ψ ≠ c` at every point of `s`,
  `convexHull s ∩ {ψ = c} = convexHull (crossSet ψ c s)`. No affine independence is needed. For
  `x = ∑ w v • v` on the hyperplane put `A = ∑_{ψ v > c} w v (ψ v - c) = ∑_{ψ u < c} w u (c - ψ u)`;
  then `x = ∑_{u, v} (w u w v (ψ v - ψ u) / A) • crossPt u v`, with weights summing to `1`.
* `sliceComplex K hdim hgen` — for `K` of dimension at most two (faces with at most three
  vertices) and a hyperplane missing every vertex, the crossing sets of the faces of `K` form a
  simplicial complex of dimension at most one (`sliceComplex_card_le_two`), finite when `K` is
  (`sliceComplex_faces_finite`), with space `K.space ∩ {ψ = c}` (`sliceComplex_space`).
* `sliceComplex_vertex` — each vertex of the slice is `crossPt u v` for an edge `{u, v}` of `K`
  with `ψ u < c < ψ v`.
* `sliceComplex_edge` — each edge of the slice is the crossing set of a triangle of `K`, and lies
  in it.

In dimension three a tetrahedron can cross a plane in four coplanar points, which are not affinely
independent; that case needs a subdivision and is not treated here.
-/

namespace QOU.MathlibExt.PL

open Set Geometry

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] (ψ : E →L[ℝ] ℝ) (c : ℝ)

/-- The point of the line through `u` and `v` where `ψ = c`. -/
noncomputable def crossPt (u v : E) : E :=
  (ψ v - ψ u)⁻¹ • ((ψ v - c) • u - (ψ u - c) • v)

/-- The crossing points of the edges of `s` with the hyperplane `{ψ = c}`. -/
noncomputable def crossSet [DecidableEq E] (s : Finset E) : Finset E :=
  ((s.filter fun u => ψ u < c) ×ˢ (s.filter fun v => c < ψ v)).image fun p => crossPt ψ c p.1 p.2

variable {ψ c}

lemma map_crossPt {u v : E} (h : ψ u ≠ ψ v) : ψ (crossPt ψ c u v) = c := by
  have h' : ψ v - ψ u ≠ 0 := sub_ne_zero.mpr (Ne.symm h)
  simp only [crossPt, map_smul, map_sub, smul_eq_mul]
  field_simp
  ring

lemma crossPt_mem_segment {u v : E} (hu : ψ u < c) (hv : c < ψ v) :
    crossPt ψ c u v ∈ segment ℝ u v := by
  have hd : 0 < ψ v - ψ u := by linarith
  refine ⟨(ψ v - c) / (ψ v - ψ u), (c - ψ u) / (ψ v - ψ u), div_nonneg (by linarith) hd.le,
    div_nonneg (by linarith) hd.le, by field_simp; ring, ?_⟩
  simp only [crossPt, div_eq_inv_mul, mul_smul]
  module

lemma crossSet_subset [DecidableEq E] (s : Finset E) :
    (crossSet ψ c s : Set E) ⊆ convexHull ℝ ↑s ∩ {x | ψ x = c} := by
  intro x hx
  simp only [crossSet, Finset.coe_image, mem_image, Finset.mem_coe, Finset.mem_product,
    Finset.mem_filter] at hx
  obtain ⟨⟨u, v⟩, ⟨⟨hus, hu⟩, hvs, hv⟩, rfl⟩ := hx
  refine ⟨segment_subset_convexHull hus hvs (crossPt_mem_segment hu hv), ?_⟩
  exact map_crossPt (by linarith)

/-- **The slice of a simplex** by a hyperplane missing its vertices. -/
theorem convexHull_inter_hyperplane [DecidableEq E] (s : Finset E) (hgen : ∀ v ∈ s, ψ v ≠ c) :
    convexHull ℝ ↑s ∩ {x | ψ x = c} = convexHull ℝ ↑(crossSet ψ c s) := by
  apply Subset.antisymm
  · rintro x ⟨hx, hψ⟩
    obtain ⟨w, hw0, hw1, rfl⟩ := Finset.mem_convexHull'.mp hx
    simp only [mem_setOf_eq, map_sum, map_smul, smul_eq_mul] at hψ
    set N := s.filter fun u => ψ u < c
    set P := s.filter fun v => c < ψ v
    have hP : s.filter (fun v => ¬ ψ v < c) = P := by
      refine Finset.filter_congr fun v hv => ?_
      constructor
      · intro h; exact lt_of_le_of_ne (not_lt.mp h) (hgen v hv).symm
      · intro h; exact not_lt.mpr h.le
    have hsplit : ∀ f : E → ℝ, ∑ v ∈ s, f v = ∑ u ∈ N, f u + ∑ v ∈ P, f v := fun f => by
      rw [← Finset.sum_filter_add_sum_filter_not s (fun v => ψ v < c), hP]
    have hsplitE : ∀ f : E → E, ∑ v ∈ s, f v = ∑ u ∈ N, f u + ∑ v ∈ P, f v := fun f => by
      rw [← Finset.sum_filter_add_sum_filter_not s (fun v => ψ v < c), hP]
    set A := ∑ v ∈ P, w v * (ψ v - c) with hAdef
    have hbal : ∑ u ∈ N, w u * (c - ψ u) = A := by
      have h0 : ∑ v ∈ s, w v * (ψ v - c) = 0 := by
        simp only [mul_sub, Finset.sum_sub_distrib, ← Finset.sum_mul, hw1, hψ]
        ring
      rw [hsplit] at h0
      have : ∑ u ∈ N, w u * (c - ψ u) = -∑ u ∈ N, w u * (ψ u - c) := by
        rw [← Finset.sum_neg_distrib]
        exact Finset.sum_congr rfl fun u _ => by ring
      rw [this]
      linarith
    have hPnn : ∀ v ∈ P, 0 ≤ w v * (ψ v - c) := fun v hv =>
      mul_nonneg (hw0 v (Finset.mem_filter.mp hv).1)
        (by linarith [(Finset.mem_filter.mp hv).2])
    have hNnn : ∀ u ∈ N, 0 ≤ w u * (c - ψ u) := fun u hu =>
      mul_nonneg (hw0 u (Finset.mem_filter.mp hu).1)
        (by linarith [(Finset.mem_filter.mp hu).2])
    have hApos : 0 < A := by
      rcases (Finset.sum_nonneg hPnn).lt_or_eq with h | h
      · exact h
      exfalso
      have hP0 : ∀ v ∈ P, w v = 0 := fun v hv => by
        have := (Finset.sum_eq_zero_iff_of_nonneg hPnn).mp h.symm v hv
        rcases mul_eq_zero.mp this with h' | h'
        · exact h'
        · linarith [(Finset.mem_filter.mp hv).2]
      have hN0 : ∀ u ∈ N, w u = 0 := fun u hu => by
        have := (Finset.sum_eq_zero_iff_of_nonneg hNnn).mp (by rw [hbal, hAdef]; exact h.symm) u hu
        rcases mul_eq_zero.mp this with h' | h'
        · exact h'
        · linarith [(Finset.mem_filter.mp hu).2]
      rw [hsplit, Finset.sum_eq_zero hN0, Finset.sum_eq_zero hP0] at hw1
      norm_num at hw1
    -- weights on pairs
    let μ : E × E → ℝ := fun p => w p.1 * w p.2 * (ψ p.2 - ψ p.1) / A
    have hμ0 : ∀ p ∈ N ×ˢ P, 0 ≤ μ p := by
      rintro ⟨u, v⟩ hp
      obtain ⟨hu, hv⟩ := Finset.mem_product.mp hp
      have := (Finset.mem_filter.mp hu).2
      have := (Finset.mem_filter.mp hv).2
      exact div_nonneg (mul_nonneg (mul_nonneg (hw0 u (Finset.mem_filter.mp hu).1)
        (hw0 v (Finset.mem_filter.mp hv).1)) (by linarith)) hApos.le
    have hμ1 : ∑ p ∈ N ×ˢ P, μ p = 1 := by
      rw [Finset.sum_product]
      have : ∀ u ∈ N, ∑ v ∈ P, μ (u, v) = w u + w u * (c - ψ u) * (∑ v ∈ P, w v) / A := by
        intro u _
        simp only [μ]
        rw [show (fun v => w u * w v * (ψ v - ψ u) / A) =
          fun v => w u / A * (w v * (ψ v - c)) + w u * (c - ψ u) / A * w v by
            funext v; ring]
        rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum, ← hAdef]
        field_simp
      rw [Finset.sum_congr rfl this, Finset.sum_add_distrib]
      rw [show (fun u => w u * (c - ψ u) * (∑ v ∈ P, w v) / A) =
        fun u => (w u * (c - ψ u)) * ((∑ v ∈ P, w v) / A) by funext u; ring]
      rw [← Finset.sum_mul, hbal, mul_div_cancel₀ _ hApos.ne', ← hsplit, hw1]
    have hcomb : ∑ p ∈ N ×ˢ P, μ p • crossPt ψ c p.1 p.2 = ∑ v ∈ s, w v • v := by
      have hterm : ∀ u ∈ N, ∀ v ∈ P, μ (u, v) • crossPt ψ c u v =
          (w u / A * (w v * (ψ v - c))) • u + (w v / A * (w u * (c - ψ u))) • v := by
        intro u hu v hv
        have hd : ψ v - ψ u ≠ 0 := by
          have := (Finset.mem_filter.mp hu).2
          have := (Finset.mem_filter.mp hv).2
          intro h; linarith
        simp only [μ, crossPt, smul_smul]
        rw [show w u * w v * (ψ v - ψ u) / A * (ψ v - ψ u)⁻¹ = w u * w v / A by
          field_simp]
        module
      rw [Finset.sum_product, Finset.sum_congr rfl fun u hu =>
        Finset.sum_congr rfl fun v hv => hterm u hu v hv]
      simp only [Finset.sum_add_distrib]
      rw [Finset.sum_comm (s := N) (t := P) (f := fun u v =>
        (w v / A * (w u * (c - ψ u))) • v)]
      simp only [← Finset.sum_smul, ← Finset.mul_sum, ← hAdef, hbal]
      rw [hsplitE]
      congr 1
      · exact Finset.sum_congr rfl fun u _ => by rw [div_mul_cancel₀ _ hApos.ne']
      · exact Finset.sum_congr rfl fun v _ => by rw [div_mul_cancel₀ _ hApos.ne']
    rw [← hcomb, ← Finset.centerMass_eq_of_sum_1 _ _ hμ1]
    refine Finset.centerMass_mem_convexHull _ hμ0 (by rw [hμ1]; exact one_pos) fun p hp => ?_
    simp only [crossSet, Finset.coe_image]
    exact mem_image_of_mem _ hp
  · refine convexHull_min (crossSet_subset s) ?_
    exact (convex_convexHull ℝ _).inter (convex_hyperplane ψ.isLinear c)

/-! ### Combinatorics of `crossSet` -/

lemma mem_crossSet [DecidableEq E] {s : Finset E} {x : E} :
    x ∈ crossSet ψ c s ↔ ∃ u ∈ s, ∃ v ∈ s, ψ u < c ∧ c < ψ v ∧ crossPt ψ c u v = x := by
  simp only [crossSet, Finset.mem_image, Finset.mem_product, Finset.mem_filter, Prod.exists]
  constructor
  · rintro ⟨u, v, ⟨⟨hu, hu'⟩, hv, hv'⟩, rfl⟩
    exact ⟨u, hu, v, hv, hu', hv', rfl⟩
  · rintro ⟨u, hu, v, hv, hu', hv', rfl⟩
    exact ⟨u, v, ⟨⟨hu, hu'⟩, hv, hv'⟩, rfl⟩

lemma crossSet_mono [DecidableEq E] {s t : Finset E} (h : s ⊆ t) :
    crossSet ψ c s ⊆ crossSet ψ c t := by
  intro x hx
  obtain ⟨u, hu, v, hv, hu', hv', rfl⟩ := mem_crossSet.mp hx
  exact mem_crossSet.mpr ⟨u, h hu, v, h hv, hu', hv', rfl⟩

lemma crossSet_pair [DecidableEq E] {u v : E} (hu : ψ u < c) (hv : c < ψ v) :
    crossSet ψ c {u, v} = {crossPt ψ c u v} := by
  ext x
  rw [mem_crossSet, Finset.mem_singleton]
  constructor
  · rintro ⟨a, ha, b, hb, ha', hb', rfl⟩
    simp only [Finset.mem_insert, Finset.mem_singleton] at ha hb
    rcases ha with rfl | rfl
    · rcases hb with rfl | rfl
      · exact absurd ha' (not_lt.mpr hb'.le)
      · rfl
    · exact absurd ha' (not_lt.mpr hv.le)
  · rintro rfl
    exact ⟨u, by simp, v, by simp, hu, hv, rfl⟩

lemma card_filter_add_le (s : Finset E) :
    (s.filter fun u => ψ u < c).card + (s.filter fun v => c < ψ v).card ≤ s.card := by
  classical
  have h := Finset.filter_card_add_filter_neg_card_eq_card (s := s) (fun x => ψ x < c)
  have : (s.filter fun v => c < ψ v).card ≤ (s.filter fun x => ¬ ψ x < c).card :=
    Finset.card_le_card fun x hx => by
      simp only [Finset.mem_filter] at hx ⊢
      exact ⟨hx.1, not_lt.mpr hx.2.le⟩
  omega

lemma card_crossSet_le_mul [DecidableEq E] (s : Finset E) :
    (crossSet ψ c s).card ≤
      (s.filter fun u => ψ u < c).card * (s.filter fun v => c < ψ v).card :=
  Finset.card_image_le.trans (Finset.card_product _ _).le

/-- A face with at most three vertices crosses a hyperplane in at most two points. -/
lemma card_crossSet_le_two [DecidableEq E] {s : Finset E} (hs : s.card ≤ 3) :
    (crossSet ψ c s).card ≤ 2 := by
  have h1 := card_crossSet_le_mul (ψ := ψ) (c := c) s
  have h2 := card_filter_add_le (ψ := ψ) (c := c) s
  have key : ∀ a b : ℕ, a + b ≤ 3 → a * b ≤ 2 := by
    intro a b h
    have : a ≤ 3 := by omega
    interval_cases a <;> omega
  exact h1.trans (key _ _ (h2.trans hs))

/-- Two crossing points need at least three vertices. -/
lemma three_le_card_of_card_crossSet [DecidableEq E] {s : Finset E}
    (hs : 2 ≤ (crossSet ψ c s).card) : 3 ≤ s.card := by
  have h1 := card_crossSet_le_mul (ψ := ψ) (c := c) s
  have h2 := card_filter_add_le (ψ := ψ) (c := c) s
  have key : ∀ a b : ℕ, 2 ≤ a * b → 3 ≤ a + b := by
    intro a b h
    by_contra hab
    have : a ≤ 2 := by omega
    interval_cases a <;> omega
  exact (key _ _ (hs.trans h1)).trans h2

/-- A finite set of at most two points is affinely independent. -/
lemma affineIndependent_of_card_le_two {t : Finset E} (ht : t.card ≤ 2) :
    AffineIndependent ℝ ((↑) : t → E) := by
  classical
  rcases Nat.lt_or_ge t.card 2 with h | h
  · haveI : Subsingleton t := Finset.card_le_one_iff_subsingleton_coe.mp (by omega)
    exact affineIndependent_of_subsingleton ℝ _
  · obtain ⟨a, b, hab, rfl⟩ := Finset.card_eq_two.mp (le_antisymm ht h)
    refine (affineIndependent_of_ne ℝ hab).range.mono ?_
    intro x hx
    have hx' : x ∈ ({a, b} : Finset E) := hx
    rw [Finset.mem_insert, Finset.mem_singleton] at hx'
    rcases hx' with rfl | rfl
    · exact ⟨0, rfl⟩
    · exact ⟨1, rfl⟩

/-! ### The slice of a complex of dimension at most two -/

/-- **The slice complex**: the faces are the crossing sets of the faces of `K`. For `K` of
dimension at most two (faces with at most three vertices) these are points and segments. -/
noncomputable def sliceComplex [DecidableEq E] (K : SimplicialComplex ℝ E)
    (hdim : ∀ s ∈ K.faces, s.card ≤ 3) (hgen : ∀ s ∈ K.faces, ∀ v ∈ s, ψ v ≠ c) :
    SimplicialComplex ℝ E where
  faces := {σ | ∃ τ ∈ K.faces, crossSet ψ c τ = σ ∧ σ.Nonempty}
  empty_notMem := fun ⟨_, _, _, h⟩ => Finset.not_nonempty_empty h
  indep := by
    rintro σ ⟨τ, hτ, rfl, -⟩
    exact affineIndependent_of_card_le_two (card_crossSet_le_two (hdim τ hτ))
  down_closed := by
    rintro σ t ⟨τ, hτ, rfl, hne⟩ hts ht
    by_cases heq : t = crossSet ψ c τ
    · exact ⟨τ, hτ, heq.symm, heq ▸ hne⟩
    have hlt : t.card < (crossSet ψ c τ).card :=
      Finset.card_lt_card (Finset.ssubset_iff_subset_ne.mpr ⟨hts, heq⟩)
    have h2 := card_crossSet_le_two (ψ := ψ) (c := c) (hdim τ hτ)
    have hpos : 0 < t.card := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr ht)
    obtain ⟨x, rfl⟩ := Finset.card_eq_one.mp (show t.card = 1 by omega)
    obtain ⟨u, hu, v, hv, hu', hv', rfl⟩ := mem_crossSet.mp (hts (Finset.mem_singleton_self x))
    refine ⟨{u, v}, K.down_closed hτ ?_ (by simp), crossSet_pair hu' hv',
      Finset.singleton_nonempty _⟩
    exact Finset.insert_subset hu (Finset.singleton_subset_iff.mpr hv)
  inter_subset_convexHull := by
    rintro _ _ ⟨τ, hτ, rfl, -⟩ ⟨τ', hτ', rfl, -⟩
    rw [← convexHull_inter_hyperplane τ (hgen τ hτ),
      ← convexHull_inter_hyperplane τ' (hgen τ' hτ')]
    rintro x ⟨⟨hx, hxψ⟩, hx', -⟩
    have hint := K.inter_subset_convexHull hτ hτ' ⟨hx, hx'⟩
    rw [← Finset.coe_inter] at hint
    have h2 : x ∈ convexHull ℝ ↑(crossSet ψ c (τ ∩ τ')) := by
      rw [← convexHull_inter_hyperplane _ fun v hv => hgen τ hτ v (Finset.mem_inter.mp hv).1]
      exact ⟨hint, hxψ⟩
    refine convexHull_mono ?_ h2
    rw [← Finset.coe_inter]
    exact Finset.coe_subset.mpr (Finset.subset_inter (crossSet_mono Finset.inter_subset_left)
      (crossSet_mono Finset.inter_subset_right))

section sliceComplex

variable [DecidableEq E] {K : SimplicialComplex ℝ E} {hdim : ∀ s ∈ K.faces, s.card ≤ 3}
  {hgen : ∀ s ∈ K.faces, ∀ v ∈ s, ψ v ≠ c}

lemma mem_sliceComplex_faces {σ : Finset E} :
    σ ∈ (sliceComplex K hdim hgen).faces ↔ ∃ τ ∈ K.faces, crossSet ψ c τ = σ ∧ σ.Nonempty :=
  Iff.rfl

/-- **The slice is a complex of dimension at most one.** -/
lemma sliceComplex_card_le_two {σ : Finset E} (hσ : σ ∈ (sliceComplex K hdim hgen).faces) :
    σ.card ≤ 2 := by
  obtain ⟨τ, hτ, rfl, -⟩ := hσ
  exact card_crossSet_le_two (hdim τ hτ)

lemma sliceComplex_faces_finite (hK : K.faces.Finite) :
    (sliceComplex K hdim hgen).faces.Finite :=
  (hK.image (crossSet ψ c)).subset fun _ ⟨τ, hτ, h, _⟩ => ⟨τ, hτ, h⟩

/-- **The slice of the space**: `S.space = K.space ∩ {ψ = c}`. -/
theorem sliceComplex_space :
    (sliceComplex K hdim hgen).space = K.space ∩ {x | ψ x = c} := by
  ext x
  simp only [SimplicialComplex.mem_space_iff, mem_inter_iff, mem_setOf_eq]
  constructor
  · rintro ⟨_, ⟨τ, hτ, rfl, -⟩, hx⟩
    rw [← convexHull_inter_hyperplane τ (hgen τ hτ)] at hx
    exact ⟨⟨τ, hτ, hx.1⟩, hx.2⟩
  · rintro ⟨⟨τ, hτ, hx⟩, hψ⟩
    have hmem : x ∈ convexHull ℝ ↑(crossSet ψ c τ) := by
      rw [← convexHull_inter_hyperplane τ (hgen τ hτ)]
      exact ⟨hx, hψ⟩
    refine ⟨crossSet ψ c τ, ⟨τ, hτ, rfl, ?_⟩, hmem⟩
    by_contra h
    rw [Finset.not_nonempty_iff_eq_empty] at h
    rw [h, Finset.coe_empty, convexHull_empty] at hmem
    exact hmem

/-- **Each vertex of the slice lies on an edge of `K`**, where that edge crosses `{ψ = c}`. -/
theorem sliceComplex_vertex {x : E} (hx : {x} ∈ (sliceComplex K hdim hgen).faces) :
    ∃ u v, ({u, v} : Finset E) ∈ K.faces ∧ ψ u < c ∧ c < ψ v ∧ x = crossPt ψ c u v := by
  obtain ⟨τ, hτ, h, -⟩ := hx
  obtain ⟨u, hu, v, hv, hu', hv', hx⟩ :=
    mem_crossSet.mp (h ▸ Finset.mem_singleton_self x : x ∈ crossSet ψ c τ)
  exact ⟨u, v, K.down_closed hτ (Finset.insert_subset hu (Finset.singleton_subset_iff.mpr hv))
    (by simp), hu', hv', hx.symm⟩

/-- **Each edge of the slice lies in a triangle of `K`**: it is the crossing set of a face of
`K` with three vertices. -/
theorem sliceComplex_edge {σ : Finset E} (hσ : σ ∈ (sliceComplex K hdim hgen).faces)
    (h2 : σ.card = 2) : ∃ τ ∈ K.faces, τ.card = 3 ∧ crossSet ψ c τ = σ ∧
      convexHull ℝ (σ : Set E) ⊆ convexHull ℝ (τ : Set E) := by
  obtain ⟨τ, hτ, rfl, -⟩ := hσ
  refine ⟨τ, hτ, le_antisymm (hdim τ hτ) (three_le_card_of_card_crossSet h2.ge), rfl, ?_⟩
  rw [← convexHull_inter_hyperplane τ (hgen τ hτ)]
  exact inter_subset_left

end sliceComplex

end QOU.MathlibExt.PL
