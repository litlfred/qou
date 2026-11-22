/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLRegularNbhd
import QOU.MathlibExt.PLCone

set_option autoImplicit false

/-!
# Stars, links, and regular neighbourhoods of a point (issue #8902, Moise build A)

## What is a DEFINITION here

* `linkComplex K v` — the link of `v` in `K`: the faces `σ` of `K` with `v ∉ σ` and
  `insert v σ` a face of `K`.
* `vertexStar K v` — the closed star of `v`: the union of the faces of `K` containing `v`.

## What is a THEOREM here

* `notMem_linkComplex_space` — `v` is not in the space of its link.
* `raysMeetOnce_linkComplex` — every ray from `v` meets the link at most once.
* `vertexStar_eq` — **the closed star of a vertex is the cone on its link**:
  `vertexStar K v = insert v (convexJoin ℝ {v} (linkComplex K v).space)`.
* `simplicialNbhd_eq_vertexStar` — the simplicial neighbourhood of a subcomplex whose space is
  `{v}` is the closed star of `v`.
* `IsRegularNbhd.eq_cone` — **a regular neighbourhood of a point is a cone**: if `N` is a regular
  neighbourhood of `{p}` in `M`, then `N = insert p (convexJoin ℝ {p} Lk.space)` for a finite
  complex `Lk` with `Lk.space ⊆ M`, `p ∉ Lk.space` and every ray from `p` meeting `Lk.space` at
  most once; so `N` is the space of `coneComplex Lk p`.

## What is NOT proved here

That the link of an interior point of a PL `3`-manifold is a PL `2`-sphere, and so that the cone
is a PL `3`-ball (Rourke–Sanderson Ch. 2–3).
-/

namespace QOU.MathlibExt.PL

open Set Geometry

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

section Link

variable [DecidableEq E]

/-- **The link** of `v` in `K`. -/
def linkComplex (K : SimplicialComplex ℝ E) (v : E) : SimplicialComplex ℝ E where
  faces := {s | s ∈ K.faces ∧ v ∉ s ∧ insert v s ∈ K.faces}
  empty_notMem h := K.empty_notMem h.1
  indep h := K.indep h.1
  down_closed hs hts ht := ⟨K.down_closed hs.1 hts ht, fun h => hs.2.1 (hts h),
    K.down_closed hs.2.2 (Finset.insert_subset_insert v hts) (Finset.insert_ne_empty _ _)⟩
  inter_subset_convexHull hs ht := K.inter_subset_convexHull hs.1 ht.1

/-- **The closed star** of `v` in `K`. -/
def vertexStar (K : SimplicialComplex ℝ E) (v : E) : Set E :=
  ⋃ s ∈ {s | s ∈ K.faces ∧ v ∈ s}, convexHull ℝ (s : Set E)

variable {K : SimplicialComplex ℝ E} {v : E}

lemma mem_linkComplex_faces {s : Finset E} :
    s ∈ (linkComplex K v).faces ↔ s ∈ K.faces ∧ v ∉ s ∧ insert v s ∈ K.faces := Iff.rfl

lemma isSubcomplex_linkComplex : IsSubcomplex (linkComplex K v) K := fun _ h => h.1

lemma linkComplex_faces_finite (hK : K.faces.Finite) : (linkComplex K v).faces.Finite :=
  hK.subset fun _ h => h.1

/-- A vertex outside a face is outside its affine span when the two span a face. -/
theorem notMem_affineSpan_of_insert {s : Finset E} (hK : insert v s ∈ K.faces) (hv : v ∉ s) :
    v ∉ affineSpan ℝ (s : Set E) := by
  have h := (K.indep hK).notMem_affineSpan_diff ⟨v, Finset.mem_insert_self v s⟩ Set.univ
  have he : ((↑) : ↥(insert v s) → E) '' (Set.univ \ {⟨v, Finset.mem_insert_self v s⟩}) =
      (s : Set E) := by
    ext y
    constructor
    · rintro ⟨⟨x, hx⟩, ⟨-, hxi⟩, rfl⟩
      rcases Finset.mem_insert.mp hx with rfl | h
      · exact absurd rfl hxi
      · exact h
    · intro hy
      refine ⟨⟨y, Finset.mem_insert_of_mem hy⟩, ⟨trivial, fun h => hv ?_⟩, rfl⟩
      have := congrArg Subtype.val (mem_singleton_iff.mp h)
      simp only at this
      exact this ▸ hy
  rw [he] at h
  exact h

theorem notMem_linkComplex_space : v ∉ (linkComplex K v).space := by
  intro h
  obtain ⟨s, hs, hvs⟩ := SimplicialComplex.mem_space_iff.mp h
  exact notMem_affineSpan_of_insert hs.2.2 hs.2.1 (convexHull_subset_affineSpan _ hvs)

/-- One direction of the ray property, for `t ≤ 1`. -/
theorem ray_aux {s s' : Finset E} (hs : s ∈ (linkComplex K v).faces)
    (hs' : s' ∈ (linkComplex K v).faces) {x y : E} (hx : x ∈ convexHull ℝ (s : Set E))
    (hy : y ∈ convexHull ℝ (s' : Set E)) {t : ℝ} (ht0 : 0 < t) (ht1 : t ≤ 1)
    (h : x - v = t • (y - v)) : x = y := by
  have hx' : x = v + t • (y - v) := by rw [← h]; abel
  -- `x` lies in the face `insert v s'`
  have hx1 : x ∈ convexHull ℝ ((insert v s' : Finset E) : Set E) := by
    refine (convex_convexHull ℝ _).segment_subset
      (subset_convexHull ℝ _ (Finset.mem_coe.mpr (Finset.mem_insert_self v s')))
      (convexHull_mono (by simp) hy) ?_
    rw [segment_eq_image']
    exact ⟨t, ⟨ht0.le, ht1⟩, hx'.symm⟩
  have hx2 : x ∈ convexHull ℝ ((insert v s : Finset E) : Set E) :=
    convexHull_mono (by simp) hx
  have hu : insert v s ∩ insert v s' ∈ K.faces :=
    K.down_closed hs.2.2 Finset.inter_subset_left
      (Finset.nonempty_iff_ne_empty.mp ⟨v, by simp⟩)
  have hx3 : x ∈ convexHull ℝ ((insert v s ∩ insert v s' : Finset E) : Set E) := by
    rw [Finset.coe_inter]
    exact K.inter_subset_convexHull hs.2.2 hs'.2.2 ⟨hx2, hx1⟩
  have hx4 := K.inter_subset_convexHull hu hs.1 ⟨hx3, hx⟩
  -- so `x` lies in the face `s'`
  have hxs' : x ∈ convexHull ℝ (s' : Set E) := by
    refine convexHull_mono ?_ hx4
    rintro w ⟨hw, hws⟩
    have hw' : w ∈ insert v s' := (Finset.mem_inter.mp hw).2
    rcases Finset.mem_insert.mp hw' with rfl | h
    · exact absurd hws hs.2.1
    · exact h
  rcases ht1.lt_or_eq with ht1 | rfl
  · exfalso
    refine notMem_affineSpan_of_insert hs'.2.2 hs'.2.1 ?_
    have hmem := AffineMap.lineMap_mem (Q := affineSpan ℝ (s' : Set E)) (1 / (1 - t))
      (convexHull_subset_affineSpan _ hy) (convexHull_subset_affineSpan _ hxs')
    convert hmem using 1
    rw [AffineMap.lineMap_apply, vsub_eq_sub, vadd_eq_add, hx']
    have e : v + t • (y - v) - y = (1 - t) • (v - y) := by module
    rw [e, smul_smul, one_div, inv_mul_cancel₀ (by linarith), one_smul]
    abel
  · rw [one_smul] at h
    exact sub_left_injective h

/-- **Rays from `v` meet the link at most once.** -/
theorem raysMeetOnce_linkComplex : RaysMeetOnce v (linkComplex K v).space := by
  intro x hx y hy t ht h
  obtain ⟨s, hs, hxs⟩ := SimplicialComplex.mem_space_iff.mp hx
  obtain ⟨s', hs', hys'⟩ := SimplicialComplex.mem_space_iff.mp hy
  rcases le_total t 1 with ht1 | ht1
  · exact ray_aux hs hs' hxs hys' ht ht1 h
  · refine (ray_aux hs' hs hys' hxs (inv_pos.mpr ht) (inv_le_one_of_one_le₀ ht1) ?_).symm
    rw [h, smul_smul, inv_mul_cancel₀ ht.ne', one_smul]

/-- **The closed star of a vertex is the cone on its link.** -/
theorem vertexStar_eq (hv : {v} ∈ K.faces) :
    vertexStar K v = insert v (convexJoin ℝ {v} (linkComplex K v).space) := by
  ext x
  rw [vertexStar, mem_iUnion₂, mem_insert_iff, mem_convexJoin]
  constructor
  · rintro ⟨s, ⟨hs, hvs⟩, hx⟩
    rw [← Finset.insert_erase hvs, Finset.coe_insert, mem_convexHull_insert_iff] at hx
    rcases hx with rfl | ⟨y, hy, b, hb, rfl⟩
    · exact Or.inl rfl
    have hne : s.erase v ≠ ∅ := by
      rintro h
      rw [h, Finset.coe_empty, convexHull_empty] at hy
      exact hy
    have hσ : s.erase v ∈ (linkComplex K v).faces :=
      ⟨K.down_closed hs (Finset.erase_subset v s) hne, Finset.notMem_erase v s,
        by rw [Finset.insert_erase hvs]; exact hs⟩
    refine Or.inr ⟨v, rfl, y, SimplicialComplex.mem_space_iff.mpr ⟨_, hσ, hy⟩, ?_⟩
    rw [segment_eq_image']
    exact ⟨b, hb, rfl⟩
  · rintro (rfl | ⟨a, ha, y, hy, hx⟩)
    · exact ⟨{x}, ⟨hv, Finset.mem_singleton_self x⟩, subset_convexHull ℝ _ (by simp)⟩
    rw [mem_singleton_iff] at ha
    subst ha
    obtain ⟨σ, hσ, hyσ⟩ := SimplicialComplex.mem_space_iff.mp hy
    refine ⟨insert a σ, ⟨hσ.2.2, Finset.mem_insert_self a σ⟩, ?_⟩
    rw [Finset.coe_insert, mem_convexHull_insert_iff]
    rw [segment_eq_image'] at hx
    obtain ⟨b, hb, rfl⟩ := hx
    exact Or.inr ⟨y, hyσ, b, hb, rfl⟩

/-- The simplicial neighbourhood of a subcomplex with space `{v}` is the closed star of `v`. -/
theorem simplicialNbhd_eq_vertexStar {L : SimplicialComplex ℝ E} (hL : IsSubcomplex L K)
    (hLv : L.space = {v}) : {v} ∈ K.faces ∧ simplicialNbhd K L = vertexStar K v := by
  have hv : {v} ∈ K.faces := by
    have hvL : v ∈ L.space := hLv ▸ mem_singleton v
    obtain ⟨s, hs, hvs⟩ := SimplicialComplex.mem_space_iff.mp hvL
    have hsub : (s : Set E) ⊆ {v} := fun w hw =>
      hLv ▸ L.convexHull_subset_space hs (subset_convexHull ℝ _ hw)
    have hsv : s = {v} := by
      refine Finset.eq_singleton_iff_unique_mem.mpr ⟨?_, fun w hw => hsub hw⟩
      by_contra hn
      have : (s : Set E) ⊆ ∅ := fun w hw => by
        have := hsub hw
        rw [mem_singleton_iff] at this
        exact hn (this ▸ hw)
      rw [Set.subset_empty_iff.mp this, convexHull_empty] at hvs
      exact hvs
    exact hsv ▸ hL hs
  refine ⟨hv, ?_⟩
  have hset : {s : Finset E | s ∈ K.faces ∧ (convexHull ℝ (s : Set E) ∩ L.space).Nonempty} =
      {s | s ∈ K.faces ∧ v ∈ s} := by
    ext s
    refine and_congr_right fun hs => ?_
    rw [hLv, ← SimplicialComplex.vertex_mem_convexHull_iff
      (SimplicialComplex.mem_vertices.mpr hv) hs]
    exact ⟨fun ⟨w, hw, hwv⟩ => (mem_singleton_iff.mp hwv) ▸ hw, fun h => ⟨v, h, rfl⟩⟩
  unfold simplicialNbhd vertexStar
  rw [hset]

end Link

/-- **A regular neighbourhood of a point is a cone** on a finite complex in `M`. -/
theorem IsRegularNbhd.eq_cone {N M : Set E} {p : E} (h : IsRegularNbhd N {p} M) :
    ∃ Lk : SimplicialComplex ℝ E, Lk.faces.Finite ∧ Lk.space ⊆ M ∧ p ∉ Lk.space ∧
      RaysMeetOnce p Lk.space ∧ N = insert p (convexJoin ℝ {p} Lk.space) := by
  classical
  obtain ⟨K, K', K'', L'', hK, -, hd', hK', hd'', hK'', hL'', hP, rfl⟩ := h
  obtain ⟨hv, heq⟩ := simplicialNbhd_eq_vertexStar hL'' hP
  refine ⟨linkComplex K'' p, linkComplex_faces_finite (hd''.faces_finite (hd'.faces_finite hK.1)),
    ?_, notMem_linkComplex_space, raysMeetOnce_linkComplex, by rw [heq, vertexStar_eq hv]⟩
  rw [← hK.2, ← hK'.1, ← hK''.1]
  exact (isSubcomplex_linkComplex).space_subset

end QOU.MathlibExt.PL
