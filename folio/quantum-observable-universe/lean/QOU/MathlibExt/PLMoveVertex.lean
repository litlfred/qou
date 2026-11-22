/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLDropVertex
import QOU.MathlibExt.PLListPolygon
import QOU.MathlibExt.PLCollinear

set_option autoImplicit false

/-!
# Moving one vertex by Δ-moves (issue #8902, isotopy-to-Δ bridge, local stability)

Let one component of a link have vertex list `b :: s ++ [a, v]`, so `v` is its last vertex with
neighbours `a` and `b`. This file moves `v` to a new point `w` by a chain of ten moves:

1. put a buffer vertex `p` on the edge `[v, b]` and a buffer `q` on `[a, v]`;
2. cut the corner `v` (delete it), leaving the edge `[q, p]`;
3. put `w` on the edge `[q, p]`;
4. delete the buffers `q` and `p`.

Each step is a `Move` or the reverse of one, and its hypotheses are stated pointwise below. The
point of the buffers: every hypothesis is about triangles that stay non-degenerate as `w → v`,
so a compactness argument (`PLStability`) discharges them for `w` near `v`.

## What is a DEFINITION here

* `PolygonalLink.rest L m` — the point set of the components other than `m`.
* `PolygonalLink.Reaches L m P` — some Δ-equivalent link equals `L` with component `m`
  replaced by `P`.

## What is a THEOREM here

* `PolygonalLink.Reaches.trans'` — chaining.
* `reaches_insert`, `reaches_rotate`, `reaches_delta`, `reaches_drop` — the four steps in list
  form.
* `PolygonalLink.reaches_moveLast` — the ten-step chain.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-! ## List carriers -/

lemma pathCarrier_cons_append_pair (x y z : E) (l : List E) :
    pathCarrier (x :: (l ++ [y, z])) = pathCarrier (x :: (l ++ [y])) ∪ segment ℝ y z := by
  induction l generalizing x with
  | nil => simp [union_comm]
  | cons u l ih =>
    simp only [List.cons_append, pathCarrier_cons_cons, ih, union_assoc]

lemma pathCarrier_cons_append_cons_cons (x y z : E) (l r : List E) :
    pathCarrier (x :: (l ++ y :: z :: r)) =
      pathCarrier (x :: (l ++ [y])) ∪ pathCarrier (y :: z :: r) := by
  induction l generalizing x with
  | nil => simp
  | cons u l ih =>
    simp only [List.cons_append, pathCarrier_cons_cons] at ih ⊢
    rw [ih, union_assoc]

namespace Polygon

lemma ofList_v_zero (x : E) (l : List E) (h : 3 ≤ (x :: l).length) :
    (ofList (x :: l) h).v 0 = x := rfl

lemma ofList_v_last (x y : E) (t : List E) (h : 3 ≤ (x :: (t ++ [y])).length) :
    (ofList (x :: (t ++ [y])) h).v (Fin.last _) = y := by
  simp [ofList]

lemma carrier_ofList_cons (x y : E) (t : List E) (h : 3 ≤ (x :: (t ++ [y])).length) :
    (ofList (x :: (t ++ [y])) h).carrier = pathCarrier (x :: (t ++ [y])) ∪ segment ℝ y x := by
  rw [carrier_ofList]
  simp

end Polygon

namespace PolygonalLink

/-! ## Replacing one component, up to Δ-equivalence -/

/-- The point set of the components other than `m`. -/
def rest (L : PolygonalLink E) (m : Fin L.k) : Set E :=
  ⋃ (i : Fin L.k) (_ : i ≠ m), (L.comp i).carrier

lemma carrier_eq_union (L : PolygonalLink E) (m : Fin L.k) :
    L.carrier = (L.comp m).carrier ∪ L.rest m := by
  ext z
  simp only [carrier, rest, mem_iUnion, mem_union, exists_prop]
  constructor
  · rintro ⟨i, hi⟩
    by_cases him : i = m
    · subst him; exact Or.inl hi
    · exact Or.inr ⟨i, him, hi⟩
  · rintro (h | ⟨i, -, hi⟩)
    · exact ⟨m, h⟩
    · exact ⟨i, hi⟩

/-- **Reaching a component.** Some link Δ-equivalent to `L` is `L` with component `m` replaced
by `P` (the components keep their indices). -/
def Reaches (L : PolygonalLink E) (m : Fin L.k) (P : Polygon E) : Prop :=
  ∃ L' : PolygonalLink E, DeltaEquiv L L' ∧
    ∃ hk : L.k = L'.k, ∀ i, L'.comp (Fin.cast hk i) = Function.update L.comp m P i

/-- **Chaining.** The second step only needs to know the new component and the rest. -/
theorem Reaches.trans' {L : PolygonalLink E} {m : Fin L.k} {P Q : Polygon E}
    (h1 : L.Reaches m P)
    (h2 : ∀ (L' : PolygonalLink E) (m' : Fin L'.k), L'.comp m' = P → L'.rest m' = L.rest m →
      L'.Reaches m' Q) : L.Reaches m Q := by
  obtain ⟨L', hd, hk, hc⟩ := h1
  have hm' : L'.comp (Fin.cast hk m) = P := by rw [hc]; simp
  have hoth : ∀ i, i ≠ m → L'.comp (Fin.cast hk i) = L.comp i := fun i hi => by
    rw [hc, Function.update_of_ne hi]
  have hr : L'.rest (Fin.cast hk m) = L.rest m := by
    ext z
    simp only [rest, mem_iUnion, exists_prop]
    constructor
    · rintro ⟨j, hj, hz⟩
      refine ⟨Fin.cast hk.symm j, fun h => hj ?_, ?_⟩
      · rw [← h]; simp
      · rw [← hoth _ fun h => hj (by rw [← h]; simp)]; simpa using hz
    · rintro ⟨i, hi, hz⟩
      exact ⟨Fin.cast hk i, fun h => hi (Fin.cast_injective _ h), by rw [hoth i hi]; exact hz⟩
  obtain ⟨L'', hd', hk', hc'⟩ := h2 L' _ hm' hr
  refine ⟨L'', Relation.EqvGen.trans _ _ _ hd hd', hk.trans hk', fun i => ?_⟩
  have := hc' (Fin.cast hk i)
  rw [Fin.cast_cast] at this
  rw [this]
  by_cases hi : i = m
  · subst hi; simp
  · rw [Function.update_of_ne (fun h => hi (Fin.cast_injective _ h)), Function.update_of_ne hi,
      hoth i hi]

lemma Reaches.congr {L : PolygonalLink E} {m : Fin L.k} {l l' : List E} {h : 3 ≤ l.length}
    (e : l = l') (hr : L.Reaches m (Polygon.ofList l h)) :
    L.Reaches m (Polygon.ofList l' (e ▸ h)) := by
  subst e; exact hr

/-! ## The four steps in list form -/

variable (L : PolygonalLink E) (m : Fin L.k)

/-- Insert a point of the closing edge. -/
theorem reaches_insert (x y c : E) (t : List E) (h : 3 ≤ (x :: (t ++ [y])).length)
    (hm : L.comp m = Polygon.ofList (x :: (t ++ [y])) h) (hc : c ∈ openSegment ℝ y x) :
    L.Reaches m (Polygon.ofList (x :: (t ++ [y, c])) (by simp)) := by
  have hc' : c ∈ openSegment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0) := by
    rw [hm, Polygon.ofList_v_last, Polygon.ofList_v_zero]; exact hc
  refine ⟨L.insertCollinear m c hc', L.deltaEquiv_insertCollinear m c hc', rfl, fun i => ?_⟩
  show Function.update L.comp m ((L.comp m).subdivideLast c) i = _
  rw [hm, Polygon.ofList_subdivideLast]
  congr 2
  simp

/-- Re-index the component. -/
theorem reaches_rotate (l : List E) (h : 3 ≤ l.length) (hm : L.comp m = Polygon.ofList l h)
    (r : ℕ) : L.Reaches m (Polygon.ofList (l.rotate r) (by simp; exact h)) := by
  refine ⟨L.rotateComp m r, Relation.EqvGen.rel _ _ (L.move_rotateComp m r), rfl, fun i => ?_⟩
  show Function.update L.comp m ((L.comp m).rotateBy r) i = _
  rw [hm, Polygon.ofList_rotateBy]

/-- A Δ-move on the closing edge. -/
theorem reaches_delta (x y c : E) (t : List E) (h : 3 ≤ (x :: (t ++ [y])).length)
    (hm : L.comp m = Polygon.ofList (x :: (t ++ [y])) h) (hca : c ≠ y) (hcb : c ≠ x)
    (hseg : segment ℝ y c ∩ segment ℝ c x ⊆ {c})
    (htri : convexHull ℝ {y, x, c} ∩ (pathCarrier (x :: (t ++ [y])) ∪ L.rest m) ⊆
      segment ℝ y x) :
    L.Reaches m (Polygon.ofList (x :: (t ++ [y, c])) (by simp)) := by
  have hv1 : (L.comp m).v (Fin.last _) = y := by rw [hm, Polygon.ofList_v_last]
  have hv0 : (L.comp m).v 0 = x := by rw [hm, Polygon.ofList_v_zero]
  have hca' : c ≠ (L.comp m).v (Fin.last _) := by rw [hv1]; exact hca
  have hcb' : c ≠ (L.comp m).v 0 := by rw [hv0]; exact hcb
  have hseg' : segment ℝ ((L.comp m).v (Fin.last _)) c ∩ segment ℝ c ((L.comp m).v 0) ⊆ {c} := by
    rw [hv1, hv0]; exact hseg
  have htri' : convexHull ℝ {(L.comp m).v (Fin.last _), (L.comp m).v 0, c} ∩ L.carrier =
      segment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0) := by
    rw [hv1, hv0]
    apply Subset.antisymm
    · rintro z ⟨hzT, hzL⟩
      rw [carrier_eq_union, hm, Polygon.carrier_ofList_cons] at hzL
      rcases hzL with (hz | hz) | hz
      · exact htri ⟨hzT, Or.inl hz⟩
      · exact hz
      · exact htri ⟨hzT, Or.inr hz⟩
    · intro z hz
      refine ⟨segment_subset_convexHull (by simp) (by simp) hz, ?_⟩
      rw [carrier_eq_union, hm, Polygon.carrier_ofList_cons]
      exact Or.inl (Or.inr hz)
  refine ⟨L.deltaMove m c hca' hcb' hseg' htri',
    Relation.EqvGen.rel _ _ (L.move_deltaMove m c hca' hcb' hseg' htri'), rfl, fun i => ?_⟩
  show Function.update L.comp m ((L.comp m).subdivideLast c) i = _
  rw [hm, Polygon.ofList_subdivideLast]
  congr 2
  simp

/-- Delete the last vertex. -/
theorem reaches_drop (x y c : E) (t : List E) (ht : t ≠ [])
    (h : 3 ≤ (x :: (t ++ [y, c])).length)
    (hm : L.comp m = Polygon.ofList (x :: (t ++ [y, c])) h)
    (hT : convexHull ℝ {y, x, c} ∩ (pathCarrier (x :: (t ++ [y, c])) ∪ L.rest m) ⊆
      segment ℝ y c ∪ segment ℝ c x) :
    L.Reaches m (Polygon.ofList (x :: (t ++ [y]))
      (by have := List.length_pos_of_ne_nil ht; simp; omega)) := by
  have h3 : 3 ≤ (x :: (t ++ [y])).length := by
    have := List.length_pos_of_ne_nil ht; simp; omega
  set M := Polygon.ofList (x :: (t ++ [y])) h3
  have hm' : L.comp m = M.subdivideLast c := by
    rw [hm, Polygon.ofList_subdivideLast]
    exact Polygon.ofList_congr _ (by simp)
  have hT' : convexHull ℝ {M.v (Fin.last M.n), M.v 0, c} ∩ L.carrier ⊆
      segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0) := by
    have hv1 : M.v (Fin.last M.n) = y := Polygon.ofList_v_last _ _ _ _
    have hv0 : M.v 0 = x := rfl
    rw [hv1, hv0]
    rintro z ⟨hzT, hzL⟩
    have hcar : (Polygon.ofList (x :: (t ++ [y, c])) h).carrier =
        pathCarrier (x :: (t ++ [y, c])) ∪ segment ℝ c x := by
      rw [Polygon.carrier_ofList]; simp
    rw [carrier_eq_union, hm, hcar] at hzL
    rcases hzL with (hz | hz) | hz
    · exact hT ⟨hzT, Or.inl hz⟩
    · exact Or.inr (segment_symm ℝ c x ▸ hz)
    · exact hT ⟨hzT, Or.inr hz⟩
  refine ⟨L.dropLast m M c hm' hT', L.deltaEquiv_dropLast m M c hm' hT', rfl, fun i => ?_⟩
  rfl

/-! ## The ten-step chain -/

/-- **Moving the last vertex.** Component `m` has vertex list `b :: s ++ [a, v]`. Under the
pointwise conditions below, `v` can be replaced by `w`: buffers `p ∈ (v, b)` and `q ∈ (a, v)`
are inserted, the corner `v` is cut, `w` is inserted on `[q, p]`, and the buffers are deleted.
Write `RR` for the path `b, …, a` together with the other components. -/
theorem reaches_moveLast (b a v w p q : E) (s : List E) (h : 3 ≤ (b :: (s ++ [a, v])).length)
    (hm : L.comp m = Polygon.ofList (b :: (s ++ [a, v])) h)
    (hp : p ∈ openSegment ℝ v b) (hq : q ∈ openSegment ℝ a v)
    (hcut : convexHull ℝ {q, p, v} ∩ (pathCarrier (b :: (s ++ [a])) ∪ L.rest m ∪
      segment ℝ a q ∪ segment ℝ p b) ⊆ {q, p})
    (hwq : w ≠ q) (hwp : w ≠ p) (hwseg : segment ℝ q w ∩ segment ℝ w p ⊆ {w})
    (hins : convexHull ℝ {q, p, w} ∩ (pathCarrier (b :: (s ++ [a])) ∪ L.rest m ∪
      segment ℝ a q ∪ segment ℝ p b) ⊆ {q, p})
    (hdq : convexHull ℝ {a, w, q} ∩ (pathCarrier (b :: (s ++ [a])) ∪ L.rest m ∪
      segment ℝ w p ∪ segment ℝ p b) ⊆ {a, w})
    (hdp : convexHull ℝ {w, b, p} ∩ (pathCarrier (b :: (s ++ [a])) ∪ L.rest m ∪
      segment ℝ a w) ⊆ {w, b}) :
    L.Reaches m (Polygon.ofList (b :: (s ++ [a, w])) (by simp)) := by
  -- 1. insert `p` on the closing edge `[v, b]`
  have s1 := (reaches_insert L m b v p (s ++ [a]) (by simp)
    (hm.trans (Polygon.ofList_congr _ (by simp))) hp).congr
    (l' := b :: (s ++ [a, v, p])) (by simp)
  refine s1.trans' fun L1 m1 h1 r1 => ?_
  -- 2. re-index so that `v` comes first
  have s2 := (reaches_rotate L1 m1 _ _ h1 (s.length + 2)).congr
    (l' := v :: p :: b :: (s ++ [a])) (by
      rw [show b :: (s ++ [a, v, p]) = (b :: (s ++ [a])) ++ [v, p] by simp,
        show s.length + 2 = (b :: (s ++ [a])).length by simp, List.rotate_append_length_eq]
      simp)
  refine s2.trans' fun L2 m2 h2 r2 => ?_
  -- 3. insert `q` on the closing edge `[a, v]`
  have s3 := (reaches_insert L2 m2 v a q (p :: b :: s) (by simp)
    (h2.trans (Polygon.ofList_congr _ (by simp))) hq).congr
    (l' := v :: p :: b :: (s ++ [a, q])) (by simp)
  refine s3.trans' fun L3 m3 h3 r3 => ?_
  -- 4. re-index so that `v` comes last
  have s4 := (reaches_rotate L3 m3 _ _ h3 1).congr
    (l' := p :: b :: (s ++ [a, q, v])) (by
      show (v :: p :: b :: (s ++ [a, q])).rotate (0 + 1) = _
      rw [List.rotate_cons_succ, List.rotate_zero]
      simp)
  refine s4.trans' fun L4 m4 h4 r4 => ?_
  have r4' : L4.rest m4 = L.rest m := r4.trans (r3.trans (r2.trans r1))
  -- 5. cut the corner `v`
  have s5 := (reaches_drop L4 m4 p q v (b :: (s ++ [a])) (by simp) (by simp)
    (h4.trans (Polygon.ofList_congr _ (by simp))) (by
      rw [r4']
      rintro z ⟨hzT, hz⟩
      simp only [List.cons_append, List.append_assoc, List.cons_append, List.nil_append,
        pathCarrier_cons_cons, pathCarrier_cons_append_cons_cons, pathCarrier_single,
        union_empty, mem_union] at hz
      by_cases hd : z ∈ segment ℝ q v ∨ z ∈ segment ℝ v p
      · rcases hd with hd | hd
        · exact Or.inl hd
        · exact Or.inr hd
      have hmem := hcut ⟨hzT, by simp only [mem_union]; tauto⟩
      rcases hmem with rfl | rfl
      · exact Or.inl (left_mem_segment ℝ _ _)
      · exact Or.inr (right_mem_segment ℝ _ _))).congr
    (l' := p :: b :: (s ++ [a, q])) (by simp)
  refine s5.trans' fun L5 m5 h5 r5 => ?_
  have r5' : L5.rest m5 = L.rest m := r5.trans r4'
  -- 6. insert `w` on the closing edge `[q, p]`
  have s6 := (reaches_delta L5 m5 p q w (b :: (s ++ [a])) (by simp)
    (h5.trans (Polygon.ofList_congr _ (by simp))) hwq hwp hwseg (by
      rw [r5']
      rintro z ⟨hzT, hz⟩
      simp only [List.cons_append, List.append_assoc, List.nil_append,
        pathCarrier_cons_cons, pathCarrier_cons_append_cons_cons, pathCarrier_single,
        union_empty, mem_union] at hz
      have hmem := hins ⟨hzT, by simp only [mem_union]; tauto⟩
      rcases hmem with rfl | rfl
      · exact left_mem_segment ℝ _ _
      · exact right_mem_segment ℝ _ _)).congr
    (l' := p :: b :: (s ++ [a, q, w])) (by simp)
  refine s6.trans' fun L6 m6 h6 r6 => ?_
  have r6' : L6.rest m6 = L.rest m := r6.trans r5'
  -- 7. re-index so that `q` comes last
  have s7 := (reaches_rotate L6 m6 _ _ h6 (s.length + 4)).congr
    (l' := w :: p :: b :: (s ++ [a, q])) (by
      rw [show p :: b :: (s ++ [a, q, w]) = (p :: b :: (s ++ [a, q])) ++ [w] by simp,
        show s.length + 4 = (p :: b :: (s ++ [a, q])).length by simp,
        List.rotate_append_length_eq]
      simp)
  refine s7.trans' fun L7 m7 h7 r7 => ?_
  have r7' : L7.rest m7 = L.rest m := r7.trans r6'
  -- 8. delete the buffer `q`
  have s8 := (reaches_drop L7 m7 w a q (p :: b :: s) (by simp) (by simp)
    (h7.trans (Polygon.ofList_congr _ (by simp))) (by
      rw [r7']
      rintro z ⟨hzT, hz⟩
      simp only [List.cons_append, 
        pathCarrier_cons_cons, pathCarrier_cons_append_cons_cons, pathCarrier_single,
        union_empty, mem_union] at hz
      by_cases hd : z ∈ segment ℝ a q ∨ z ∈ segment ℝ q w
      · rcases hd with hd | hd
        · exact Or.inl hd
        · exact Or.inr hd
      have hmem := hdq ⟨hzT, by simp only [mem_union]; tauto⟩
      rcases hmem with rfl | rfl
      · exact Or.inl (left_mem_segment ℝ _ _)
      · exact Or.inr (right_mem_segment ℝ _ _))).congr
    (l' := w :: p :: b :: (s ++ [a])) (by simp)
  refine s8.trans' fun L8 m8 h8 r8 => ?_
  have r8' : L8.rest m8 = L.rest m := r8.trans r7'
  -- 9. re-index so that `p` comes last
  have s9 := (reaches_rotate L8 m8 _ _ h8 2).congr
    (l' := b :: (s ++ [a, w, p])) (by
      rw [show w :: p :: b :: (s ++ [a]) = [w, p] ++ (b :: (s ++ [a])) by simp,
        show 2 = [w, p].length by simp, List.rotate_append_length_eq]
      simp)
  refine s9.trans' fun L9 m9 h9 r9 => ?_
  have r9' : L9.rest m9 = L.rest m := r9.trans r8'
  -- 10. delete the buffer `p`
  refine (reaches_drop L9 m9 b w p (s ++ [a]) (by simp) (by simp)
    (h9.trans (Polygon.ofList_congr _ (by simp))) (by
      rw [r9']
      rintro z ⟨hzT, hz⟩
      simp only [List.cons_append, List.append_assoc, List.nil_append,
        pathCarrier_cons_cons, pathCarrier_cons_append_cons_cons, pathCarrier_single,
        union_empty, mem_union] at hz
      by_cases hd : z ∈ segment ℝ w p ∨ z ∈ segment ℝ p b
      · rcases hd with hd | hd
        · exact Or.inl hd
        · exact Or.inr hd
      have hmem := hdp ⟨hzT, by simp only [mem_union]; tauto⟩
      rcases hmem with rfl | rfl
      · exact Or.inl (left_mem_segment ℝ _ _)
      · exact Or.inr (right_mem_segment ℝ _ _))).congr (by simp)

end PolygonalLink

end QOU.MathlibExt.PL
