/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLPolygonalLink

set_option autoImplicit false

/-!
# Collinear vertices are free (issue #8902, stage 2, isotopy-to-Δ bridge)

Inserting a vertex in the interior of an edge does not change a link's point set, and it is a
degenerate Δ-move: the triangle `convexHull {a, b, c}` with `c` on `[a, b]` is the edge itself.
So a polygonal link is Δ-equivalent to every subdivision of itself, and deleting a vertex that
lies between its two neighbours is a Δ-equivalence too.

This is the bookkeeping step at both ends of the C¹-isotopy bridge: at time `0` the inscribed
polygon is a subdivision of `L`, and at time `1` it is `L'` with extra collinear vertices.

## What is a THEOREM here

* `convexHull_triple_of_mem_segment` — `c ∈ [a, b]` gives `convexHull {a, b, c} = [a, b]`.
* `segment_inter_segment_subset_of_mem_openSegment` — for `c` strictly between `a ≠ b`,
  `[a, c] ∩ [c, b] ⊆ {c}`.
* `PolygonalLink.move_insertCollinear` — inserting a point of the open closing edge is a `Move`.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- **A degenerate triangle is its long edge.** -/
theorem convexHull_triple_of_mem_segment {a b c : E} (h : c ∈ segment ℝ a b) :
    convexHull ℝ {a, b, c} = segment ℝ a b := by
  apply Subset.antisymm
  · refine convexHull_min ?_ (convex_segment a b)
    intro x hx
    rcases hx with rfl | rfl | rfl
    · exact left_mem_segment ℝ _ _
    · exact right_mem_segment ℝ _ _
    · exact h
  · rw [← convexHull_pair]
    exact convexHull_mono (by intro x hx; rcases hx with rfl | rfl <;> simp)

/-- **The two halves of a split segment meet only at the split point.** -/
theorem segment_inter_segment_subset_of_mem_openSegment {a b c : E} (hab : a ≠ b)
    (h : c ∈ openSegment ℝ a b) : segment ℝ a c ∩ segment ℝ c b ⊆ {c} := by
  obtain ⟨α, β, hα, hβ, hαβ, rfl⟩ := h
  rintro x ⟨⟨s₁, s, hs₁, hs, hss, rfl⟩, ⟨r₁, r, hr₁, hr, hrr, hx⟩⟩
  have hα' : α = 1 - β := by linarith
  have hs₁' : s₁ = 1 - s := by linarith
  have hr₁' : r₁ = 1 - r := by linarith
  subst hα' hs₁' hr₁'
  have key : ((1 - r) * β + r - s * β) • (b - a) = 0 := by
    have : (1 - s) • a + s • ((1 - β) • a + β • b) =
        (1 - r) • ((1 - β) • a + β • b) + r • b := hx.symm
    have e1 : (1 - s) • a + s • ((1 - β) • a + β • b) = a + (s * β) • (b - a) := by
      simp only [smul_add, smul_sub, smul_smul, sub_smul, one_smul]; abel
    have e2 : (1 - r) • ((1 - β) • a + β • b) + r • b = a + ((1 - r) * β + r) • (b - a) := by
      simp only [smul_add, smul_sub, smul_smul, sub_smul, one_smul, sub_mul, one_mul, add_smul]
      abel
    rw [e1, e2] at this
    rw [sub_smul, sub_eq_zero]
    exact (add_left_cancel this).symm
  have hba : b - a ≠ 0 := sub_ne_zero.mpr (Ne.symm hab)
  have hcoef : (1 - r) * β + r - s * β = 0 := (smul_eq_zero.mp key).resolve_right hba
  have hr0 : r = 0 := by nlinarith
  subst hr0
  simp only [sub_zero, one_smul, zero_smul, add_zero] at hx
  exact hx.symm

namespace Polygon

variable (P : Polygon E)

/-- The last vertex and the first are distinct in a simple polygon. -/
lemma IsSimple.v_last_ne_v_zero {P : Polygon E} (h : P.IsSimple) :
    P.v (Fin.last P.n) ≠ P.v 0 := by
  intro he
  have := h.1 he
  have : (Fin.last P.n).val = (0 : Fin (P.n + 1)).val := congrArg Fin.val this
  simp at this
  have := P.two_le
  omega

end Polygon

namespace PolygonalLink

variable (L : PolygonalLink E)

variable {L} in
lemma insertCollinear_hca {m : Fin L.k} {c : E}
    (hc : c ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) :
    c ≠ (L.comp m).v (Fin.last _) := fun h =>
  (L.simple m).v_last_ne_v_zero (left_mem_openSegment_iff.mp (h ▸ hc))

variable {L} in
lemma insertCollinear_hcb {m : Fin L.k} {c : E}
    (hc : c ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) :
    c ≠ (L.comp m).v 0 := fun h =>
  (L.simple m).v_last_ne_v_zero (right_mem_openSegment_iff.mp (h ▸ hc))

variable {L} in
lemma insertCollinear_htri {m : Fin L.k} {c : E}
    (hc : c ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) :
    convexHull ℝ {(L.comp m).v (Fin.last _), (L.comp m).v 0, c} ∩ L.carrier =
      segment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0) := by
  rw [convexHull_triple_of_mem_segment (openSegment_subset_segment ℝ _ _ hc)]
  refine inter_eq_left.mpr ?_
  rw [← Polygon.edge_last]
  exact ((L.comp m).edge_subset_carrier _).trans (L.comp_carrier_subset m)

/-- **Inserting a collinear vertex.** A point `c` strictly inside the closing edge `[a, b]` of
component `m` can be inserted as a new vertex: the conditions of `deltaMove` all hold. -/
noncomputable def insertCollinear (m : Fin L.k) (c : E)
    (hc : c ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) : PolygonalLink E :=
  L.deltaMove m c (insertCollinear_hca hc) (insertCollinear_hcb hc)
    (segment_inter_segment_subset_of_mem_openSegment (L.simple m).v_last_ne_v_zero hc)
    (insertCollinear_htri hc)

/-- The new component is the subdivided one; the others are unchanged. -/
lemma insertCollinear_comp (m : Fin L.k) (c : E)
    (hc : c ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) :
    (L.insertCollinear m c hc).comp = Function.update L.comp m ((L.comp m).subdivideLast c) :=
  rfl

/-- **Inserting a collinear vertex is a move.** -/
theorem move_insertCollinear (m : Fin L.k) (c : E)
    (hc : c ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) :
    Move L (L.insertCollinear m c hc) :=
  L.move_deltaMove m c _ _ _ (insertCollinear_htri hc)

/-- **Inserting a collinear vertex is a Δ-equivalence.** -/
theorem deltaEquiv_insertCollinear (m : Fin L.k) (c : E)
    (hc : c ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) :
    DeltaEquiv L (L.insertCollinear m c hc) :=
  Relation.EqvGen.rel _ _ (L.move_insertCollinear m c hc)

end PolygonalLink

end QOU.MathlibExt.PL
