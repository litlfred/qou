/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLVertexSlide
import Mathlib.Topology.MetricSpace.Thickening
import Mathlib.Analysis.Normed.Module.Basic

set_option autoImplicit false

/-!
# Small generic vertex slides are Δ-equivalences (issue #8902, stage 3, part 1)

Stage 3 of #8902 puts a polygonal link in general position with respect to a projection by
moving its vertices one at a time. This file proves the step: **moving one vertex `b` to a point
`c` close to `b`, and off three planes through `b`, is a Δ-equivalence.**

## Vertex positions

To move vertices one at a time without re-indexing, a link is described by its *shape* (the
number of components and the number of vertices of each) and a *position* map from vertex slots
to `E`:

* `Shape` — `k` components, component `i` with `n i + 1 ≥ 3` vertices.
* `Shape.Slot` — a vertex slot `⟨i, j⟩`; `nx` and `pv` are the next and previous slot of the
  same component. Slot `e` also names the edge from vertex `e` to vertex `nx e`.
* `Shape.edgeW W e` — that edge, for positions `W : σ.Slot → E`.
* `Shape.Simple W` — the positions are injective; an edge meets the next edge in their shared
  vertex and is disjoint from every edge that is not adjacent to it. This is the condition that
  all components are simple and pairwise disjoint (`Shape.Simple.isSimple`,
  `Shape.Simple.disjoint`), stated once for the whole link.
* `Shape.link W h` — the polygonal link with these positions; `PolygonalLink.posOf L` recovers
  positions from a link, and `link (posOf L) _ = L` (`link_posOf`).

## What is a THEOREM here

* `Shape.link_carrier` — the point set of `link W h` is the union of the edges `edgeW W e`.
* `Shape.deltaEquiv_update` — moving the vertex in slot `s` to `c` is a Δ-equivalence whenever
  the triangle conditions of `PolygonalLink.deltaEquiv_setLast` hold; this re-indexes the
  component so that `s` is its last vertex and applies that lemma.
* `Shape.Simple.exists_slide` — **the small generic slide.** For simple positions `W` and a slot
  `s` with vertex `b`, neighbours `a = W (pv s)`, `d = W (nx s)` and second neighbours
  `a' = W (pv (pv s))`, `e = W (nx (nx s))`, there is `ε > 0` such that for every `c` with
  `dist c b < ε` and `c - b` outside the three spans `⟨a - b, d - b⟩`, `⟨d - b, e - b⟩`,
  `⟨a - b, a' - b⟩`, the moved positions are simple and the two links are Δ-equivalent.

The distance bound keeps the two swept triangles away from the edges that are not adjacent to
the moved ones (compactness, `IsCompact.exists_thickening_subset_open`); the three span conditions
keep them off the adjacent edges (a linear-algebra argument). Nothing here is specific to `ℝ³`:
`E` is any real normed space. In `ℝ³` each span is a proper subspace, so generic `c` satisfy
the three conditions; that is used in `PLRegularProjection.lean`.

## What is NOT proved here

* Regular projections themselves: `PLRegularProjection.lean`.
-/

namespace QOU.MathlibExt.PL

open Set

/-! ## Shapes and slots -/

/-- **The shape of a link**: `k` components, component `i` with `n i + 1 ≥ 3` vertices. -/
structure Shape where
  /-- Number of components. -/
  k : ℕ
  /-- One less than the number of vertices of each component. -/
  n : Fin k → ℕ
  /-- Each component has at least three vertices. -/
  two_le : ∀ i, 2 ≤ n i

namespace Shape

variable (σ : Shape)

/-- A vertex slot: component `i`, vertex `j`. Slot `e` also names the edge starting at `e`. -/
abbrev Slot := Σ i : Fin σ.k, Fin (σ.n i + 1)

variable {σ}

/-- The next slot of the same component. -/
def nx (e : σ.Slot) : σ.Slot := ⟨e.1, finRotate _ e.2⟩

/-- The previous slot of the same component. -/
def pv (e : σ.Slot) : σ.Slot := ⟨e.1, (finRotate _).symm e.2⟩

@[simp] lemma nx_fst (e : σ.Slot) : (nx e).1 = e.1 := rfl

@[simp] lemma pv_fst (e : σ.Slot) : (pv e).1 = e.1 := rfl

@[simp] lemma nx_pv (e : σ.Slot) : nx (pv e) = e := by
  simp [nx, pv]

@[simp] lemma pv_nx (e : σ.Slot) : pv (nx e) = e := by
  simp [nx, pv]

lemma nx_injective : Function.Injective (nx (σ := σ)) := fun e f h => by
  rw [← pv_nx e, h, pv_nx]

lemma nx_eq_iff {e f : σ.Slot} : nx e = f ↔ e = pv f :=
  ⟨fun h => by rw [← h, pv_nx], fun h => by rw [h, nx_pv]⟩

private lemma coe_finRotate' {m : ℕ} (i : Fin (m + 1)) :
    ((finRotate _ i : Fin (m + 1)) : ℕ) = if (i : ℕ) = m then (0 : ℕ) else (i : ℕ) + 1 := by
  by_cases hi : (i : ℕ) = m
  · have : i = Fin.last m := Fin.ext hi
    subst this
    rw [finRotate_last, if_pos hi]
    rfl
  · rw [if_neg hi]
    exact coe_finRotate_of_ne_last (fun e => hi (by simp [e]))

/-- `finRotate` has no fixed point on `Fin (m + 1)`, `m ≥ 1`. -/
private lemma finRotate_ne_self {m : ℕ} (hm : 1 ≤ m) (j : Fin (m + 1)) : finRotate _ j ≠ j := by
  intro h
  have := congrArg Fin.val h
  rw [coe_finRotate'] at this
  have hj := j.isLt
  split_ifs at this <;> omega

/-- Two rotations never return to the start when there are at least three vertices. -/
private lemma finRotate_finRotate_ne_self {m : ℕ} (hm : 2 ≤ m) (j : Fin (m + 1)) :
    finRotate _ (finRotate _ j) ≠ j := by
  intro h
  have := congrArg Fin.val h
  rw [coe_finRotate', coe_finRotate'] at this
  have hj := j.isLt
  split_ifs at this <;> omega

lemma nx_ne (e : σ.Slot) : nx e ≠ e := by
  intro h
  have h2 : (nx e).2 = e.2 := by
    obtain ⟨i, j⟩ := e
    simp only [nx, Sigma.mk.inj_iff, heq_eq_eq, true_and] at h
    exact h
  exact finRotate_ne_self (by have := σ.two_le e.1; omega) _ h2

lemma pv_ne (e : σ.Slot) : pv e ≠ e := fun h => nx_ne (pv e) (by rw [nx_pv, h])

lemma nx_nx_ne (e : σ.Slot) : nx (nx e) ≠ e := by
  intro h
  obtain ⟨i, j⟩ := e
  simp only [nx, Sigma.mk.inj_iff, heq_eq_eq, true_and] at h
  exact finRotate_finRotate_ne_self (σ.two_le i) j h

lemma nx_ne_pv (e : σ.Slot) : nx e ≠ pv e := fun h => nx_nx_ne (pv e) (by rw [nx_pv, h])

lemma pv_pv_ne (e : σ.Slot) : pv (pv e) ≠ e := by
  intro h
  have := congrArg (fun x => nx (nx x)) h
  simp only [nx_pv] at this
  exact nx_nx_ne e this.symm

/-! ## Positions -/

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- The edge in slot `e`: from vertex `e` to vertex `nx e`. -/
def edgeW (W : σ.Slot → E) (e : σ.Slot) : Set E := segment ℝ (W e) (W (nx e))

/-- **Simple positions**: the vertices are distinct, an edge meets the next one exactly in their
shared vertex, and non-adjacent edges are disjoint. -/
def Simple (W : σ.Slot → E) : Prop :=
  Function.Injective W ∧
    ∀ e f, e ≠ f →
      edgeW W e ∩ edgeW W f = if f = nx e then {W f} else if e = nx f then {W e} else ∅

/-- The `i`-th component as a polygon. -/
def poly (W : σ.Slot → E) (i : Fin σ.k) : Polygon E where
  n := σ.n i
  two_le := σ.two_le i
  v j := W ⟨i, j⟩

lemma poly_edge (W : σ.Slot → E) (i : Fin σ.k) (j : Fin (σ.n i + 1)) :
    (poly W i).edge j = edgeW W ⟨i, j⟩ := rfl

lemma poly_carrier (W : σ.Slot → E) (i : Fin σ.k) :
    (poly W i).carrier = ⋃ j, edgeW W ⟨i, j⟩ := rfl

variable {W : σ.Slot → E}

lemma Simple.adj (h : Simple W) (e : σ.Slot) : edgeW W e ∩ edgeW W (nx e) = {W (nx e)} := by
  rw [h.2 e (nx e) (nx_ne e).symm, if_pos rfl]

lemma Simple.disj (h : Simple W) {e f : σ.Slot} (hef : e ≠ f) (h1 : f ≠ nx e) (h2 : e ≠ nx f) :
    Disjoint (edgeW W e) (edgeW W f) := by
  rw [disjoint_iff_inter_eq_empty, h.2 e f hef, if_neg h1, if_neg h2]

lemma Simple.isSimple (h : Simple W) (i : Fin σ.k) : (poly W i).IsSimple := by
  refine ⟨fun j j' hj => ?_, fun j j' hjj => ?_⟩
  · have := h.1 hj
    simpa using this
  · have hne : (⟨i, j⟩ : σ.Slot) ≠ ⟨i, j'⟩ := fun e => hjj (by simpa using e)
    rw [poly_edge, poly_edge, h.2 _ _ hne]
    have e1 : ((⟨i, j'⟩ : σ.Slot) = nx ⟨i, j⟩) ↔ j' = (poly W i).next j := by
      simp [nx, Polygon.next, poly]
    have e2 : ((⟨i, j⟩ : σ.Slot) = nx ⟨i, j'⟩) ↔ j = (poly W i).next j' := by
      simp [nx, Polygon.next, poly]
    simp only [e1, e2]
    rfl

lemma Simple.disjoint (h : Simple W) :
    Pairwise fun i j => Disjoint (poly W i).carrier (poly W j).carrier := by
  intro i i' hii
  rw [poly_carrier, poly_carrier, Set.disjoint_iUnion_left]
  intro j
  rw [Set.disjoint_iUnion_right]
  intro j'
  have hne : (⟨i, j⟩ : σ.Slot) ≠ ⟨i', j'⟩ := fun e => hii (congrArg Sigma.fst e)
  refine h.disj hne (fun e => hii ?_) (fun e => hii ?_)
  · exact (congrArg Sigma.fst e).symm
  · exact congrArg Sigma.fst e

/-- **The link with positions `W`.** -/
def link (W : σ.Slot → E) (h : Simple W) : PolygonalLink E where
  k := σ.k
  comp := poly W
  simple := h.isSimple
  disjoint := h.disjoint

lemma link_carrier (h : Simple W) : (link W h).carrier = ⋃ e, edgeW W e := by
  ext x
  simp only [PolygonalLink.carrier, link, poly_carrier, mem_iUnion]
  exact ⟨fun ⟨i, j, hx⟩ => ⟨⟨i, j⟩, hx⟩, fun ⟨⟨i, j⟩, hx⟩ => ⟨i, j, hx⟩⟩

lemma edgeW_subset_carrier (h : Simple W) (e : σ.Slot) : edgeW W e ⊆ (link W h).carrier := by
  rw [link_carrier]; exact subset_iUnion (edgeW W) e

/-! ## Moving one vertex is a Δ-equivalence under the triangle conditions -/

private lemma mod_of_lt_two_mul {a m : ℕ} (h : a < 2 * m) :
    a % m = if a < m then a else a - m := by
  split_ifs with h1
  · exact Nat.mod_eq_of_lt h1
  · rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]

private lemma sh_val {n r : ℕ} (i : Fin (n + 1)) : (sh n r i).val = (i.val + r) % (n + 1) := rfl

private lemma sh_last {n : ℕ} (j : Fin (n + 1)) : sh n (j.val + 1) (Fin.last n) = j := by
  apply Fin.ext
  rw [sh_val, Fin.val_last, mod_of_lt_two_mul (by omega)]
  split_ifs <;> omega

private lemma sh_zero {n : ℕ} (j : Fin (n + 1)) : sh n (j.val + 1) 0 = finRotate _ j := by
  apply Fin.ext
  rw [sh_val, coe_finRotate', Fin.val_zero, mod_of_lt_two_mul (by omega)]
  split_ifs <;> omega

private lemma sh_penult {n : ℕ} (h2 : 2 ≤ n) (j : Fin (n + 1)) :
    sh n (j.val + 1) ⟨n - 1, by omega⟩ = (finRotate _).symm j := by
  rw [Equiv.eq_symm_apply]
  apply Fin.ext
  rw [coe_finRotate', sh_val, mod_of_lt_two_mul (by omega)]
  split_ifs <;> simp_all <;> omega

private lemma sh_ne_sh_last {n : ℕ} (j : Fin (n + 1)) {i : Fin (n + 1)} (hi : i ≠ Fin.last n) :
    sh n (j.val + 1) i ≠ j := by
  intro h
  apply hi
  apply Fin.ext
  have hv := congrArg Fin.val h
  rw [sh_val, mod_of_lt_two_mul (by omega)] at hv
  have hi' : i.val ≠ n := fun e => hi (Fin.ext e)
  have := i.isLt
  have := j.isLt
  rw [Fin.val_last]
  split_ifs at hv <;> omega

variable {E : Type*} [AddCommGroup E] [Module ℝ E] {σ : Shape}

lemma poly_update_of_ne (W : σ.Slot → E) (s : σ.Slot) (c : E) {i : Fin σ.k} (hi : i ≠ s.1) :
    poly (Function.update W s c) i = poly W i := by
  simp only [poly, Polygon.mk.injEq, heq_eq_eq, true_and]
  funext j
  exact Function.update_of_ne (fun e => hi (congrArg Sigma.fst e)) _ _

lemma rot_poly_update (W : σ.Slot → E) (s : σ.Slot) (c : E) :
    (poly (Function.update W s c) s.1).rot (s.2.val + 1) =
      ((poly W s.1).rot (s.2.val + 1)).setLast c := by
  obtain ⟨m, j⟩ := s
  simp only [poly, Polygon.rot, Polygon.setLast, Polygon.mk.injEq, heq_eq_eq, true_and]
  funext i
  by_cases hi : i = Fin.last _
  · subst hi
    rw [Function.update_self, sh_last]
    exact Function.update_self _ _ _
  · rw [Function.update_of_ne hi, Function.update_of_ne]
    intro e
    apply sh_ne_sh_last j hi
    rw [Sigma.mk.inj_iff] at e
    exact eq_of_heq e.2

/-- **Moving the vertex in slot `s` to `c` is a Δ-equivalence** when `c ∉ {b, d}`,
`[b, c] ∩ [c, d] ⊆ {c}`, the triangle `{b, d, c}` meets the link only in `[b, d]`, and the
triangle `{a, c, b}` meets the moved link only in `[a, c]`; here `b = W s`, `d = W (nx s)`,
`a = W (pv s)`. -/
theorem deltaEquiv_update (W : σ.Slot → E) (hW : Simple W) (s : σ.Slot) (c : E)
    (hW' : Simple (Function.update W s c))
    (hca : c ≠ W s) (hcb : c ≠ W (nx s))
    (hseg : segment ℝ (W s) c ∩ segment ℝ c (W (nx s)) ⊆ {c})
    (htri₁ : convexHull ℝ {W s, W (nx s), c} ∩ (⋃ e, edgeW W e) = segment ℝ (W s) (W (nx s)))
    (htri₂ : convexHull ℝ {W (pv s), c, W s} ∩ (⋃ e, edgeW (Function.update W s c) e) =
      segment ℝ (W (pv s)) c) :
    DeltaEquiv (link W hW) (link _ hW') := by
  set W' := Function.update W s c with hW'_def
  set L := link W hW
  set L' := link W' hW'
  set m := s.1
  set r := s.2.val + 1
  set L₁ := L.rotateComp m r
  set L₂ := L'.rotateComp m r
  have h1 : Move L L₁ := L.move_rotateComp m r
  have h2 : Move L' L₂ := L'.move_rotateComp m r
  have hL₁m : L₁.comp m = (poly W m).rot r := by
    show Function.update (poly W) m ((poly W m).rotateBy r) m = _
    rw [Function.update_self, Polygon.rotateBy_eq_rot]
  have hL₂m : L₂.comp m = (poly W' m).rot r := by
    show Function.update (poly W') m ((poly W' m).rotateBy r) m = _
    rw [Function.update_self, Polygon.rotateBy_eq_rot]
  have hlast : ((poly W m).rot r).v (Fin.last _) = W s := by
    show W ⟨m, sh _ r (Fin.last _)⟩ = W s
    rw [sh_last]
  have hzero : ((poly W m).rot r).v 0 = W (nx s) := by
    show W ⟨m, sh _ r 0⟩ = W (nx s)
    rw [sh_zero]
    rfl
  have hpen : ((poly W m).rot r).v ((poly W m).rot r).penult = W (pv s) := by
    show W ⟨m, sh _ r ⟨σ.n m - 1, _⟩⟩ = W (pv s)
    rw [sh_penult (σ.two_le m)]
    rfl
  have hc₁ : L₁.carrier = ⋃ e, edgeW W e := by
    rw [PolygonalLink.rotateComp_carrier, link_carrier]
  have hc₂ : L₂.carrier = ⋃ e, edgeW W' e := by
    rw [PolygonalLink.rotateComp_carrier, link_carrier]
  have key : DeltaEquiv L₁ L₂ := by
    refine PolygonalLink.deltaEquiv_setLast L₁ L₂ (Equiv.refl _) m c (fun i hi => ?_) ?_ ?_ ?_
      ?_ ?_ ?_
    · show Function.update (poly W') m ((poly W' m).rotateBy r) i =
        Function.update (poly W) m ((poly W m).rotateBy r) i
      rw [Function.update_of_ne hi, Function.update_of_ne hi]
      exact poly_update_of_ne W s c hi
    · show L₂.comp m = _
      rw [hL₂m, hL₁m]
      exact rot_poly_update W s c
    · rw [hL₁m, hlast]; exact hca
    · rw [hL₁m, hzero]; exact hcb
    · rw [hL₁m, hlast, hzero]; exact hseg
    · rw [hL₁m, hlast, hzero, hc₁]; exact htri₁
    · rw [hL₁m, hlast, hpen, hc₂]; exact htri₂
  exact Relation.EqvGen.trans _ _ _ (Relation.EqvGen.rel _ _ h1)
    (Relation.EqvGen.trans _ _ _ key (Relation.EqvGen.symm _ _ (Relation.EqvGen.rel _ _ h2)))

/-! ## A criterion for simple positions -/

section Criterion

variable {E : Type*} [AddCommGroup E] [Module ℝ E] {σ : Shape} {W : σ.Slot → E}

lemma right_mem_edgeW (e : σ.Slot) : W (nx e) ∈ edgeW W e := right_mem_segment ℝ _ _

lemma left_mem_edgeW (e : σ.Slot) : W e ∈ edgeW W e := left_mem_segment ℝ _ _

/-- Simplicity from its halves: injective positions, adjacent edges meet only in the shared
vertex, non-adjacent edges are disjoint. -/
theorem simple_of (hinj : Function.Injective W)
    (hadj : ∀ e, edgeW W e ∩ edgeW W (nx e) ⊆ {W (nx e)})
    (hdisj : ∀ e f, e ≠ f → f ≠ nx e → e ≠ nx f → Disjoint (edgeW W e) (edgeW W f)) :
    Simple W := by
  refine ⟨hinj, fun e f hef => ?_⟩
  split_ifs with h1 h2
  · subst h1
    exact Subset.antisymm (hadj e)
      (singleton_subset_iff.mpr ⟨right_mem_edgeW e, left_mem_edgeW _⟩)
  · subst h2
    rw [inter_comm]
    exact Subset.antisymm (hadj f)
      (singleton_subset_iff.mpr ⟨right_mem_edgeW f, left_mem_edgeW _⟩)
  · exact disjoint_iff_inter_eq_empty.mp (hdisj e f hef h1 h2)

lemma edgeW_update_of_ne (s : σ.Slot) (c : E) {f : σ.Slot} (h1 : f ≠ s) (h2 : nx f ≠ s) :
    edgeW (Function.update W s c) f = edgeW W f := by
  simp only [edgeW, Function.update_of_ne h1, Function.update_of_ne h2]

lemma edgeW_update_self (s : σ.Slot) (c : E) :
    edgeW (Function.update W s c) s = segment ℝ c (W (nx s)) := by
  simp only [edgeW, Function.update_self, Function.update_of_ne (nx_ne s)]

lemma edgeW_update_pv (s : σ.Slot) (c : E) :
    edgeW (Function.update W s c) (pv s) = segment ℝ (W (pv s)) c := by
  rw [edgeW, nx_pv, Function.update_self, Function.update_of_ne (pv_ne s)]

lemma edgeW_pv (s : σ.Slot) : edgeW W (pv s) = segment ℝ (W (pv s)) (W s) := by
  simp only [edgeW, nx_pv]

end Criterion

/-! ## Convex geometry of the two swept triangles -/

section Geometry

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

private lemma isCompact_segment'' (x y : E) : IsCompact (segment ℝ x y) := by
  rw [segment_eq_image]
  exact isCompact_Icc.image (((continuous_const.sub continuous_id).smul continuous_const).add
    (continuous_id.smul continuous_const))

lemma mem_convexHull_triple {p q r x : E} (hx : x ∈ convexHull ℝ {p, q, r}) :
    ∃ α β γ : ℝ, 0 ≤ α ∧ 0 ≤ β ∧ 0 ≤ γ ∧ α + β + γ = 1 ∧ x = α • p + β • q + γ • r := by
  let C : Set E := {x | ∃ α β γ : ℝ, 0 ≤ α ∧ 0 ≤ β ∧ 0 ≤ γ ∧ α + β + γ = 1 ∧
    x = α • p + β • q + γ • r}
  have hC : Convex ℝ C := by
    rintro _ ⟨α, β, γ, hα, hβ, hγ, hs, rfl⟩ _ ⟨α', β', γ', hα', hβ', hγ', hs', rfl⟩ a b ha hb hab
    refine ⟨a * α + b * α', a * β + b * β', a * γ + b * γ', by positivity, by positivity,
      by positivity, by linear_combination a * hs + b * hs' + hab, ?_⟩
    simp only [smul_add, smul_smul, add_smul]; abel
  have hsub : ({p, q, r} : Set E) ⊆ C := by
    intro y hy
    simp only [mem_insert_iff, mem_singleton_iff] at hy
    rcases hy with rfl | rfl | rfl
    · exact ⟨1, 0, 0, by norm_num, le_rfl, le_rfl, by norm_num, by simp⟩
    · exact ⟨0, 1, 0, le_rfl, by norm_num, le_rfl, by norm_num, by simp⟩
    · exact ⟨0, 0, 1, le_rfl, le_rfl, by norm_num, by norm_num, by simp⟩
  exact convexHull_min hsub hC hx

lemma segment_subset_convexHull_triple (p q r : E) :
    segment ℝ p q ⊆ convexHull ℝ {p, q, r} :=
  segment_subset_convexHull (by simp) (by simp)

/-- A point of the triangle `{p, q, c}` is within `dist c q` of the side `[p, q]`. -/
lemma exists_near_of_mem_convexHull {p q c x : E} (hx : x ∈ convexHull ℝ {p, q, c}) :
    ∃ y ∈ segment ℝ p q, dist x y ≤ dist c q := by
  obtain ⟨α, β, γ, hα, hβ, hγ, hs, rfl⟩ := mem_convexHull_triple hx
  refine ⟨α • p + (β + γ) • q, ⟨α, β + γ, hα, by positivity, by linarith, rfl⟩, ?_⟩
  have e : α • p + β • q + γ • c - (α • p + (β + γ) • q) = γ • (c - q) := by
    simp only [smul_sub, add_smul]; abel
  rw [dist_eq_norm, e, norm_smul, Real.norm_of_nonneg hγ, ← dist_eq_norm]
  have hγ1 : γ ≤ 1 := by linarith
  calc γ * dist c q ≤ 1 * dist c q := mul_le_mul_of_nonneg_right hγ1 dist_nonneg
    _ = dist c q := one_mul _

/-- If `γ • C` lies in a submodule `S` and `C ∉ S`, then `γ = 0`. -/
lemma eq_zero_of_smul_mem {S : Submodule ℝ E} {C : E} (hC : C ∉ S) {γ : ℝ}
    (h : γ • C ∈ S) : γ = 0 := by
  by_contra hγ
  apply hC
  have : C = γ⁻¹ • (γ • C) := by rw [smul_smul, inv_mul_cancel₀ hγ, one_smul]
  rw [this]
  exact S.smul_mem _ h

/-- A point of a segment, seen from a base point `o`, is in any submodule containing both
endpoints seen from `o`. -/
lemma sub_mem_of_mem_segment {S : Submodule ℝ E} {p q x o : E} (hx : x ∈ segment ℝ p q)
    (hp : p - o ∈ S) (hq : q - o ∈ S) : x - o ∈ S := by
  obtain ⟨a, b, -, -, hab, rfl⟩ := hx
  have : a • p + b • q - o = a • (p - o) + b • (q - o) := by
    have : a = 1 - b := by linarith
    subst this
    simp only [smul_sub, sub_smul, one_smul]; abel
  rw [this]
  exact S.add_mem (S.smul_mem _ hp) (S.smul_mem _ hq)

/-- **The algebraic clearance step.** If `x` is in the triangle `{p, q, c}`, `x - p` and
`q - p` lie in a submodule `S`, and `c - p` does not, then `x` is on the side `[p, q]`. -/
lemma mem_segment_of_mem_convexHull {S : Submodule ℝ E} {p q c x : E}
    (hx : x ∈ convexHull ℝ {p, q, c}) (hxs : x - p ∈ S) (hq : q - p ∈ S) (hc : c - p ∉ S) :
    x ∈ segment ℝ p q := by
  obtain ⟨α, β, γ, hα, hβ, hγ, hs, rfl⟩ := mem_convexHull_triple hx
  have e : γ • (c - p) = (α • p + β • q + γ • c - p) - β • (q - p) := by
    have : α = 1 - β - γ := by linarith
    subst this
    simp only [smul_sub, sub_smul, one_smul]; abel
  have hγ0 : γ = 0 := eq_zero_of_smul_mem hc (by rw [e]; exact S.sub_mem hxs (S.smul_mem _ hq))
  subst hγ0
  exact ⟨α, β, hα, hβ, by linarith, by simp⟩

lemma mem_span_left (u w : E) : u ∈ Submodule.span ℝ {u, w} :=
  Submodule.subset_span (by simp)

lemma mem_span_right (u w : E) : w ∈ Submodule.span ℝ {u, w} :=
  Submodule.subset_span (by simp)

end Geometry

/-! ## The small generic slide -/

section Slide

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] {σ : Shape} {W : σ.Slot → E}

/-- **No spike at a vertex**: in simple positions, `d - b` is not a non-negative multiple of
`a - b`, where `a, b, d` are consecutive vertices. -/
lemma Simple.no_spike (hW : Simple W) (s : σ.Slot) {μ : ℝ} (hμ : 0 ≤ μ) :
    W (nx s) - W s ≠ μ • (W (pv s) - W s) := by
  intro h
  have hadj := hW.adj (pv s)
  rw [nx_pv, edgeW_pv] at hadj
  rcases le_or_gt μ 1 with h1 | h1
  · have hd : W (nx s) ∈ segment ℝ (W (pv s)) (W s) := by
      refine ⟨μ, 1 - μ, hμ, by linarith, by ring, ?_⟩
      rw [sub_eq_iff_eq_add] at h
      rw [h]
      simp only [smul_sub, sub_smul, one_smul]; abel
    have : W (nx s) ∈ ({W s} : Set E) := hadj ▸ ⟨hd, right_mem_edgeW s⟩
    exact nx_ne s (hW.1 this)
  · have hμ0 : μ ≠ 0 := by positivity
    have ha : W (pv s) ∈ segment ℝ (W s) (W (nx s)) := by
      refine ⟨1 - μ⁻¹, μ⁻¹, by
        have : μ⁻¹ < 1 := inv_lt_one_of_one_lt₀ h1
        linarith, by positivity, by ring, ?_⟩
      have : W (pv s) = W s + μ⁻¹ • (W (nx s) - W s) := by
        rw [h, smul_smul, inv_mul_cancel₀ hμ0, one_smul]; abel
      rw [this]
      simp only [smul_sub, sub_smul, one_smul]; abel
    have : W (pv s) ∈ ({W s} : Set E) := hadj ▸ ⟨left_mem_segment ℝ _ _, ha⟩
    exact pv_ne s (hW.1 this)

/-- **The small generic slide.** For simple positions `W` and a slot `s` there is `ε > 0` such
that moving the vertex `b = W s` to any `c` with `dist c b < ε` and `c - b` outside the three
spans `⟨a - b, d - b⟩`, `⟨d - b, e - b⟩`, `⟨a - b, a' - b⟩` keeps the positions simple and is a
Δ-equivalence. Here `a, d` are the neighbours of `b` and `a', e` the second neighbours. -/
theorem Simple.exists_slide (hW : Simple W) (s : σ.Slot) :
    ∃ ε > 0, ∀ c : E, dist c (W s) < ε →
      c - W s ∉ Submodule.span ℝ {W (pv s) - W s, W (nx s) - W s} →
      c - W s ∉ Submodule.span ℝ {W (nx s) - W s, W (nx (nx s)) - W s} →
      c - W s ∉ Submodule.span ℝ {W (pv s) - W s, W (pv (pv s)) - W s} →
      ∃ h' : Simple (Function.update W s c), DeltaEquiv (link W hW) (link _ h') := by
  classical
  -- clearance of `[b, d]` from the edges not adjacent to it
  obtain ⟨δ₁, hδ₁, hth₁⟩ : ∃ δ, 0 < δ ∧ Metric.thickening δ (edgeW W s) ⊆
      (⋃ f : {f : σ.Slot // f ≠ s ∧ f ≠ pv s ∧ f ≠ nx s}, edgeW W f.1)ᶜ := by
    refine (isCompact_segment'' _ _).exists_thickening_subset_open
      (isClosed_iUnion_of_finite fun f => (isCompact_segment'' _ _).isClosed).isOpen_compl ?_
    intro x hx hx'
    obtain ⟨⟨f, hf1, hf2, hf3⟩, hxf⟩ := mem_iUnion.mp hx'
    exact Set.disjoint_left.mp
      (hW.disj (Ne.symm hf1) hf3 (fun e => hf2 (nx_eq_iff.mp e.symm))) hx hxf
  -- clearance of `[a, b]` from the edges not adjacent to it
  obtain ⟨δ₂, hδ₂, hth₂⟩ : ∃ δ, 0 < δ ∧ Metric.thickening δ (edgeW W (pv s)) ⊆
      (⋃ f : {f : σ.Slot // f ≠ pv s ∧ f ≠ s ∧ f ≠ pv (pv s)}, edgeW W f.1)ᶜ := by
    refine (isCompact_segment'' _ _).exists_thickening_subset_open
      (isClosed_iUnion_of_finite fun f => (isCompact_segment'' _ _).isClosed).isOpen_compl ?_
    intro x hx hx'
    obtain ⟨⟨f, hf1, hf2, hf3⟩, hxf⟩ := mem_iUnion.mp hx'
    exact Set.disjoint_left.mp
      (hW.disj (Ne.symm hf1) (fun e => hf2 (e.trans (nx_pv s)))
        (fun e => hf3 (nx_eq_iff.mp e.symm))) hx hxf
  refine ⟨min δ₁ δ₂, lt_min hδ₁ hδ₂, fun c hc hS1 hS2 hS3 => ?_⟩
  have hc₁ : dist c (W s) < δ₁ := hc.trans_le (min_le_left _ _)
  have hc₂ : dist c (W s) < δ₂ := hc.trans_le (min_le_right _ _)
  have hcT1 : c ∈ convexHull ℝ {W s, W (nx s), c} := subset_convexHull ℝ _ (by simp)
  have hcd_T1 : segment ℝ c (W (nx s)) ⊆ convexHull ℝ {W s, W (nx s), c} :=
    segment_subset_convexHull (by simp) (by simp)
  have hac_T2 : segment ℝ (W (pv s)) c ⊆ convexHull ℝ {W (pv s), c, W s} :=
    segment_subset_convexHull (by simp) (by simp)
  have hzero : W s - W s ∈ Submodule.span ℝ {W (pv s) - W s, W (nx s) - W s} := by
    rw [sub_self]; exact Submodule.zero_mem _
  -- (F1) the triangle `{b, d, c}` meets every other edge only inside `[b, d]`
  have F1 : ∀ f, f ≠ s → ∀ x ∈ convexHull ℝ {W s, W (nx s), c}, x ∈ edgeW W f →
      x ∈ edgeW W s := by
    intro f hf x hxT hxf
    by_cases hfp : f = pv s
    · rw [hfp, edgeW_pv] at hxf
      exact mem_segment_of_mem_convexHull hxT
        (sub_mem_of_mem_segment hxf (mem_span_left _ _) hzero) (mem_span_right _ _) hS1
    · by_cases hfn : f = nx s
      · rw [hfn] at hxf
        exact mem_segment_of_mem_convexHull hxT
          (sub_mem_of_mem_segment hxf (mem_span_left _ _) (mem_span_right _ _))
          (mem_span_left _ _) hS2
      · exfalso
        have hxT' : x ∈ convexHull ℝ {W (nx s), W s, c} := by rwa [Set.insert_comm] at hxT
        obtain ⟨y, hy, hxy⟩ := exists_near_of_mem_convexHull hxT'
        have hy' : y ∈ edgeW W s := by rw [edgeW, segment_symm]; exact hy
        have : x ∈ Metric.thickening δ₁ (edgeW W s) :=
          Metric.mem_thickening_iff.mpr ⟨y, hy', hxy.trans_lt hc₁⟩
        exact hth₁ this (mem_iUnion.mpr ⟨⟨f, hf, hfp, hfn⟩, hxf⟩)
  -- (F2) the triangle `{a, c, b}` meets an edge other than `[a, b]`, `[b, d]` only in `a`,
  -- and only when the edge is `[a', a]`
  have F2 : ∀ f, f ≠ pv s → f ≠ s → ∀ x ∈ convexHull ℝ {W (pv s), c, W s}, x ∈ edgeW W f →
      f = pv (pv s) ∧ x = W (pv s) := by
    intro f hf1 hf2 x hxT hxf
    by_cases hfp : f = pv (pv s)
    · refine ⟨hfp, ?_⟩
      rw [hfp] at hxf
      have hxT' : x ∈ convexHull ℝ {W s, W (pv s), c} := by
        have : ({W (pv s), c, W s} : Set E) = {W s, W (pv s), c} := by
          ext y; simp only [mem_insert_iff, mem_singleton_iff]; tauto
        rwa [this] at hxT
      have hxf' := hxf
      rw [edgeW_pv] at hxf'
      have hx1 : x ∈ segment ℝ (W s) (W (pv s)) :=
        mem_segment_of_mem_convexHull hxT'
          (sub_mem_of_mem_segment hxf' (mem_span_right _ _) (mem_span_left _ _))
          (mem_span_left _ _) hS3
      have hadj := hW.adj (pv (pv s))
      rw [nx_pv] at hadj
      have : x ∈ ({W (pv s)} : Set E) :=
        hadj ▸ ⟨hxf, by rw [edgeW_pv, segment_symm]; exact hx1⟩
      exact this
    · exfalso
      have hxT' : x ∈ convexHull ℝ {W (pv s), W s, c} := by
        rwa [Set.pair_comm] at hxT
      obtain ⟨y, hy, hxy⟩ := exists_near_of_mem_convexHull hxT'
      have hy' : y ∈ edgeW W (pv s) := by rw [edgeW_pv]; exact hy
      have : x ∈ Metric.thickening δ₂ (edgeW W (pv s)) :=
        Metric.mem_thickening_iff.mpr ⟨y, hy', hxy.trans_lt hc₂⟩
      exact hth₂ this (mem_iUnion.mpr ⟨⟨f, hf1, hf2, hfp⟩, hxf⟩)
  -- (F3) the triangle `{a, c, b}` meets the new edge `[c, d]` only in `c`
  have F3 : ∀ x ∈ convexHull ℝ {W (pv s), c, W s}, x ∈ segment ℝ c (W (nx s)) → x = c := by
    intro x hxT hxs
    obtain ⟨α, β, γ, hα, hβ, hγ, hs, hx⟩ := mem_convexHull_triple hxT
    obtain ⟨μ, ν, hμ, hν, hμν, hx'⟩ := hxs
    have key : μ • c + ν • W (nx s) = α • W (pv s) + β • c + γ • W s := hx'.trans hx
    have e : (μ - β) • (c - W s) = α • (W (pv s) - W s) - ν • (W (nx s) - W s) := by
      have h0 : (μ - β) • (c - W s) - (α • (W (pv s) - W s) - ν • (W (nx s) - W s)) =
          (μ • c + ν • W (nx s)) - (α • W (pv s) + β • c + γ • W s) +
            ((α + β + γ) - (μ + ν)) • W s := by
        simp only [smul_sub, sub_smul, add_smul]; abel
      rw [key, hs, hμν, sub_self, sub_self, zero_smul, add_zero] at h0
      exact sub_eq_zero.mp h0
    have hμβ : μ - β = 0 := eq_zero_of_smul_mem hS1 (by
      rw [e]; exact Submodule.sub_mem _ (Submodule.smul_mem _ _ (mem_span_left _ _))
        (Submodule.smul_mem _ _ (mem_span_right _ _)))
    rw [hμβ, zero_smul] at e
    rcases hν.eq_or_lt with hν0 | hν0
    · subst hν0
      rw [← hx']
      have : μ = 1 := by linarith
      rw [this, one_smul, zero_smul, add_zero]
    · exfalso
      apply hW.no_spike s (div_nonneg hα hν0.le)
      have e' : ν • (W (nx s) - W s) = α • (W (pv s) - W s) := (sub_eq_zero.mp e.symm).symm
      calc W (nx s) - W s = ν⁻¹ • (ν • (W (nx s) - W s)) := by
            rw [smul_smul, inv_mul_cancel₀ hν0.ne', one_smul]
        _ = (α / ν) • (W (pv s) - W s) := by rw [e', smul_smul, div_eq_inv_mul]
  -- the two side conditions of the move
  have hca : c ≠ W s := fun h => hS1 (by rw [h]; exact hzero)
  have hcd : c ≠ W (nx s) := fun h => hS1 (by rw [h]; exact mem_span_right _ _)
  have hseg : segment ℝ (W s) c ∩ segment ℝ c (W (nx s)) ⊆ {c} := by
    rintro x ⟨⟨μ, ν, hμ, hν, hμν, rfl⟩, ⟨μ', ν', hμ', hν', hμν', hx⟩⟩
    have e : (ν - μ') • (c - W s) = ν' • (W (nx s) - W s) := by
      have h0 : (ν - μ') • (c - W s) - ν' • (W (nx s) - W s) =
          (μ • W s + ν • c) - (μ' • c + ν' • W (nx s)) + ((μ' + ν') - (μ + ν)) • W s := by
        simp only [smul_sub, sub_smul, add_smul]; abel
      rw [hx, hμν, hμν', sub_self, sub_self, zero_smul, add_zero] at h0
      exact sub_eq_zero.mp h0
    have h0 : ν - μ' = 0 := eq_zero_of_smul_mem hS1 (by
      rw [e]; exact Submodule.smul_mem _ _ (mem_span_right _ _))
    rw [h0, zero_smul] at e
    have hdb : W (nx s) - W s ≠ 0 := sub_ne_zero.mpr fun h => nx_ne s (hW.1 h)
    have hν' : ν' = 0 := by
      rcases smul_eq_zero.mp e.symm with h | h
      · exact h
      · exact absurd h hdb
    have hμ'1 : μ' = 1 := by linarith
    rw [mem_singleton_iff, ← hx, hν', hμ'1, one_smul, zero_smul, add_zero]
  -- the triangle conditions
  have htri₁ : convexHull ℝ {W s, W (nx s), c} ∩ (⋃ e, edgeW W e) =
      segment ℝ (W s) (W (nx s)) := by
    apply Subset.antisymm
    · rintro x ⟨hxT, hx⟩
      obtain ⟨f, hf⟩ := mem_iUnion.mp hx
      by_cases hfs : f = s
      · rw [hfs] at hf; exact hf
      · exact F1 f hfs x hxT hf
    · intro x hx
      exact ⟨segment_subset_convexHull_triple _ _ _ hx, mem_iUnion.mpr ⟨s, hx⟩⟩
  have htri₂ : convexHull ℝ {W (pv s), c, W s} ∩ (⋃ e, edgeW (Function.update W s c) e) =
      segment ℝ (W (pv s)) c := by
    apply Subset.antisymm
    · rintro x ⟨hxT, hx⟩
      obtain ⟨f, hf⟩ := mem_iUnion.mp hx
      by_cases hfp : f = pv s
      · rw [hfp, edgeW_update_pv] at hf; exact hf
      · by_cases hfs : f = s
        · rw [hfs, edgeW_update_self] at hf
          rw [F3 x hxT hf]; exact right_mem_segment ℝ _ _
        · rw [edgeW_update_of_ne s c hfs (fun e => hfp (nx_eq_iff.mp e))] at hf
          obtain ⟨-, rfl⟩ := F2 f hfp hfs x hxT hf
          exact left_mem_segment ℝ _ _
    · intro x hx
      refine ⟨hac_T2 hx, mem_iUnion.mpr ⟨pv s, ?_⟩⟩
      rw [edgeW_update_pv]; exact hx
  -- the moved positions are simple
  have hW' : Simple (Function.update W s c) := by
    refine simple_of ?_ ?_ ?_
    · intro x y hxy
      by_cases hx : x = s <;> by_cases hy : y = s
      · rw [hx, hy]
      · exfalso
        rw [hx, Function.update_self, Function.update_of_ne hy] at hxy
        have h3 := F1 y hy c hcT1 (hxy ▸ left_mem_edgeW y)
        exact hS1 (sub_mem_of_mem_segment h3 hzero (mem_span_right _ _))
      · exfalso
        rw [hy, Function.update_self, Function.update_of_ne hx] at hxy
        have h3 := F1 x hx c hcT1 (hxy.symm ▸ left_mem_edgeW x)
        exact hS1 (sub_mem_of_mem_segment h3 hzero (mem_span_right _ _))
      · rw [Function.update_of_ne hx, Function.update_of_ne hy] at hxy
        exact hW.1 hxy
    · intro e x ⟨hx1, hx2⟩
      by_cases he : e = s
      · rw [he] at hx1 hx2 ⊢
        rw [edgeW_update_self] at hx1
        rw [edgeW_update_of_ne s c (nx_ne s) (nx_nx_ne s)] at hx2
        have h3 := F1 (nx s) (nx_ne s) x (hcd_T1 hx1) hx2
        have : x ∈ ({W (nx s)} : Set E) := hW.adj s ▸ ⟨h3, hx2⟩
        rw [Function.update_of_ne (nx_ne s)]; exact this
      · by_cases hep : e = pv s
        · rw [hep, nx_pv] at hx2 ⊢
          rw [hep, edgeW_update_pv] at hx1
          rw [edgeW_update_self] at hx2
          rw [Function.update_self]; exact F3 x (hac_T2 hx1) hx2
        · by_cases hepp : e = pv (pv s)
          · rw [hepp, nx_pv] at hx2 ⊢
            rw [hepp, edgeW_update_of_ne s c (pv_pv_ne s) (by rw [nx_pv]; exact pv_ne s)] at hx1
            rw [edgeW_update_pv] at hx2
            obtain ⟨-, rfl⟩ := F2 (pv (pv s)) (pv_ne _) (pv_pv_ne s) x (hac_T2 hx2) hx1
            rw [Function.update_of_ne (pv_ne s)]; rfl
          · have hne1 : nx e ≠ s := fun h => hep (nx_eq_iff.mp h)
            have hne2 : nx (nx e) ≠ s := fun h => hepp (by
              rw [nx_eq_iff, nx_eq_iff] at h; exact h)
            rw [edgeW_update_of_ne s c he hne1] at hx1
            rw [edgeW_update_of_ne s c hne1 hne2] at hx2
            rw [Function.update_of_ne hne1]
            exact (hW.adj e).subset ⟨hx1, hx2⟩
    · have D1 : ∀ f, f ≠ s → f ≠ pv s → f ≠ nx s →
          Disjoint (edgeW (Function.update W s c) s) (edgeW (Function.update W s c) f) := by
        intro f h1 h2 h3
        rw [edgeW_update_self, edgeW_update_of_ne s c h1 (fun e => h2 (nx_eq_iff.mp e)),
          Set.disjoint_left]
        intro x hx hxf
        have := F1 f h1 x (hcd_T1 hx) hxf
        exact Set.disjoint_left.mp
          (hW.disj (Ne.symm h1) h3 (fun e => h2 (nx_eq_iff.mp e.symm))) this hxf
      have D2 : ∀ f, f ≠ pv s → f ≠ s → f ≠ pv (pv s) →
          Disjoint (edgeW (Function.update W s c) (pv s)) (edgeW (Function.update W s c) f) := by
        intro f h1 h2 h3
        rw [edgeW_update_pv, edgeW_update_of_ne s c h2 (fun e => h1 (nx_eq_iff.mp e)),
          Set.disjoint_left]
        intro x hx hxf
        exact h3 (F2 f h1 h2 x (hac_T2 hx) hxf).1
      intro e f hef h1 h2
      by_cases he : e = s
      · rw [he] at h1 h2 hef ⊢
        exact D1 f (Ne.symm hef) (fun h => h2 (by rw [h, nx_pv])) h1
      by_cases hep : e = pv s
      · rw [hep] at h1 h2 hef ⊢
        rw [nx_pv] at h1
        exact D2 f (Ne.symm hef) h1 (fun h => h2 (by rw [h, nx_pv]))
      by_cases hf : f = s
      · rw [hf] at h1 h2 hef ⊢
        exact (D1 e he hep h2).symm
      by_cases hfp : f = pv s
      · rw [hfp] at h1 h2 hef ⊢
        rw [nx_pv] at h2
        exact (D2 e hep he (fun h => h1 (by rw [h, nx_pv]))).symm
      rw [edgeW_update_of_ne s c he (fun h => hep (nx_eq_iff.mp h)),
        edgeW_update_of_ne s c hf (fun h => hfp (nx_eq_iff.mp h))]
      exact hW.disj hef h1 h2
  exact ⟨hW', deltaEquiv_update W hW s c hW' hca hcd hseg htri₁ htri₂⟩

end Slide

end Shape

/-! ## From a link to positions -/

namespace PolygonalLink

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- The shape of a link. -/
def shape (L : PolygonalLink E) : Shape where
  k := L.k
  n i := (L.comp i).n
  two_le i := (L.comp i).two_le

/-- The vertex positions of a link. -/
def posOf (L : PolygonalLink E) : L.shape.Slot → E := fun e => (L.comp e.1).v e.2

theorem simple_posOf (L : PolygonalLink E) : Shape.Simple L.posOf := by
  refine ⟨fun e f hef => ?_, fun e f hef => ?_⟩
  · obtain ⟨i, j⟩ := e
    obtain ⟨i', j'⟩ := f
    by_cases hi : i = i'
    · subst hi
      have := (L.simple i).1 hef
      simp only at this
      subst this
      rfl
    · exfalso
      have h1 : L.posOf ⟨i, j⟩ ∈ (L.comp i).carrier := (L.comp i).vertex_mem_carrier j
      have h2 : L.posOf ⟨i', j'⟩ ∈ (L.comp i').carrier := (L.comp i').vertex_mem_carrier j'
      rw [← hef] at h2
      exact Set.disjoint_left.mp (L.disjoint hi) h1 h2
  · obtain ⟨i, j⟩ := e
    obtain ⟨i', j'⟩ := f
    by_cases hi : i = i'
    · subst hi
      have hj : j ≠ j' := fun e => hef (by rw [e])
      have := (L.simple i).2 j j' hj
      have e1 : ((⟨i, j'⟩ : L.shape.Slot) = Shape.nx ⟨i, j⟩) ↔ j' = (L.comp i).next j := by
        simp [Shape.nx, Polygon.next, shape]
      have e2 : ((⟨i, j⟩ : L.shape.Slot) = Shape.nx ⟨i, j'⟩) ↔ j = (L.comp i).next j' := by
        simp [Shape.nx, Polygon.next, shape]
      simp only [e1, e2]
      exact this
    · have hne1 : ¬ ((⟨i', j'⟩ : L.shape.Slot) = Shape.nx ⟨i, j⟩) :=
        fun e => hi (congrArg Sigma.fst e).symm
      have hne2 : ¬ ((⟨i, j⟩ : L.shape.Slot) = Shape.nx ⟨i', j'⟩) :=
        fun e => hi (congrArg Sigma.fst e)
      rw [if_neg hne1, if_neg hne2]
      apply Set.eq_empty_of_forall_notMem
      rintro x ⟨h1, h2⟩
      exact Set.disjoint_left.mp (L.disjoint hi) ((L.comp i).edge_subset_carrier j h1)
        ((L.comp i').edge_subset_carrier j' h2)

theorem link_posOf (L : PolygonalLink E) : Shape.link L.posOf L.simple_posOf = L := rfl

end PolygonalLink

end QOU.MathlibExt.PL
