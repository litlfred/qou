/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Analysis.Convex.Segment
import Mathlib.Analysis.Convex.Hull
import Mathlib.Logic.Relation
import Mathlib.Logic.Equiv.Fin.Rotate
import Mathlib.Data.Fin.Tuple.Basic
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Polygonal links and Reidemeister's Δ-moves (issue #8902, stage 1)

**Mathlib has no piecewise-linear topology, no links and no Δ-moves.** This file starts the
combinatorial foundation of knot theory, in the classical form of Reidemeister (1932) and
Burde–Zieschang (*Knots*, Ch. 1): a link is a finite family of disjoint simple closed polygons,
and two links are equivalent when one can be turned into the other by Δ-moves.

## Setting

Everything happens in an arbitrary real vector space `E`; the knot-theoretic case is
`E = Fin 3 → ℝ`, used in the non-vacuity section. Only the affine structure is used (segments and
convex hulls); no norm, no topology, no metric appears in any definition here.

## What is a DEFINITION here

* `Polygon E` — a closed polygon: `n + 1 ≥ 3` vertices `v : Fin (n+1) → E`, read cyclically. The
  successor of a vertex index is `next i = finRotate _ i`, and the `i`-th edge is the closed
  segment `[v i, v (next i)]`. The vertex list carries the **orientation**.
* `Polygon.IsSimple` — the vertices are pairwise distinct, consecutive edges meet only in their
  shared vertex, and non-consecutive edges are disjoint.
* `PolygonalLink E` — finitely many simple polygons with pairwise disjoint carriers.
* `Polygon.rotate`, `Polygon.subdivideLast` — re-choosing the starting vertex, and inserting a new
  vertex `c` on the closing edge `[v n, v 0]`.
* `Move` — the one-step relation on links, two clauses:
  * **relabel**: the components are permuted and each is cyclically re-indexed (the same oriented
    link, written down differently);
  * **delta**: one component's closing edge `[a, b]` is replaced by `[a, c] ∪ [c, b]`, provided
    the triangle `convexHull {a, b, c}` meets the whole link only in `[a, b]`. This is
    Reidemeister's Δ-move. Its inverse is the reversed step, which the equivalence closure adds.
* `DeltaEquiv` — the equivalence closure `Relation.EqvGen Move`.

Restricting the Δ-move to the closing edge loses nothing: `relabel` rotates any edge into the
closing position, and `DeltaEquiv` composes the two. A degenerate triangle (`c` inside `[a, b]`)
is allowed, so subdividing an edge is a special case of the move, as in Burde–Zieschang.

## What is a THEOREM here

* `Polygon.edge_rotate`, `Polygon.carrier_rotate`, `Polygon.isSimple_rotate` — re-indexing does
  not change the edges as a family, the point set, or simplicity.
* `Polygon.carrier_subdivideLast` — the point set after a subdivision is the old edges other than
  the closing one, together with `[a, c]` and `[c, b]`.
* `PolygonalLink.carrier_of_relabel` — a relabelling does not change the link's point set.
* `Move.card_eq`, `DeltaEquiv.card_eq` — **the number of components is a Δ-invariant.**
* Non-vacuity in `ℝ³` (`Fin 3 → ℝ`): `stdTriangle_isSimple` (an explicit triangle is a simple
  polygon), `unknot` and `unlink₂` (explicit 1- and 2-component links), and
  `unknot_not_deltaEquiv_unlink₂`, so `DeltaEquiv` is a proper relation.
  `move_unknot_unknotSkew` is an explicit Δ-move, out of the plane, from the triangle to a skew
  quadrilateral (`skewSquare_isSimple`), so `Move.delta` is not vacuous either.

## What is NOT proved here

* That Δ-equivalence is ambient PL isotopy (stage 2 of #8902), regular projections (stage 3),
  diagrams and the Reidemeister theorem (stages 4–5), Alexander's and Markov's theorems
  (stage 6). None of these is used, cited or assumed below.
* That the triangle condition in `Move.delta` makes the result simple: `Move` is a relation
  **between links**, so both ends are simple by construction. Whether every admissible triangle
  yields a simple polygon is a separate lemma, not needed for the definition.
* Nothing here says any two particular links are *in*equivalent beyond the component count.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-! ## Polygons -/

/-- **A closed polygon** with `n + 1 ≥ 3` vertices, read cyclically; the vertex order is the
orientation. -/
structure Polygon (E : Type*) [AddCommGroup E] [Module ℝ E] where
  /-- One less than the number of vertices. -/
  n : ℕ
  /-- At least three vertices. -/
  two_le : 2 ≤ n
  /-- The vertices, in cyclic order. -/
  v : Fin (n + 1) → E

namespace Polygon

variable (P : Polygon E)

/-- The cyclic successor of a vertex index. -/
def next (i : Fin (P.n + 1)) : Fin (P.n + 1) := finRotate (P.n + 1) i

/-- The `i`-th edge: the closed segment from vertex `i` to the next vertex. -/
def edge (i : Fin (P.n + 1)) : Set E := segment ℝ (P.v i) (P.v (P.next i))

/-- The point set of the polygon: the union of its edges. -/
def carrier : Set E := ⋃ i, P.edge i

/-- **Simplicity.** Distinct vertices; consecutive edges meet exactly in their shared vertex;
non-consecutive edges are disjoint. -/
def IsSimple : Prop :=
  Function.Injective P.v ∧
    ∀ i j, i ≠ j →
      P.edge i ∩ P.edge j =
        if j = P.next i then {P.v j} else if i = P.next j then {P.v i} else ∅

lemma edge_subset_carrier (i : Fin (P.n + 1)) : P.edge i ⊆ P.carrier :=
  subset_iUnion P.edge i

lemma vertex_mem_carrier (i : Fin (P.n + 1)) : P.v i ∈ P.carrier :=
  P.edge_subset_carrier i (left_mem_segment ℝ _ _)

/-! ### Re-indexing -/

/-- Re-index the polygon to start one vertex later. Same oriented curve. -/
def rotate : Polygon E where
  n := P.n
  two_le := P.two_le
  v := P.v ∘ finRotate (P.n + 1)

@[simp] lemma rotate_n : P.rotate.n = P.n := rfl

lemma rotate_v (i : Fin (P.n + 1)) : P.rotate.v i = P.v (P.next i) := rfl

lemma rotate_next (i : Fin (P.n + 1)) : P.rotate.next i = P.next i := rfl

lemma edge_rotate (i : Fin (P.n + 1)) : P.rotate.edge i = P.edge (P.next i) := rfl

lemma next_injective : Function.Injective P.next := (finRotate (P.n + 1)).injective

lemma next_surjective : Function.Surjective P.next := (finRotate (P.n + 1)).surjective

theorem carrier_rotate : P.rotate.carrier = P.carrier := by
  ext x
  simp only [carrier, mem_iUnion, edge_rotate]
  constructor
  · rintro ⟨i, hi⟩; exact ⟨_, hi⟩
  · rintro ⟨i, hi⟩
    obtain ⟨j, rfl⟩ := P.next_surjective i
    exact ⟨j, hi⟩

theorem isSimple_rotate (h : P.IsSimple) : P.rotate.IsSimple := by
  refine ⟨h.1.comp (finRotate (P.n + 1)).injective, fun i j hij => ?_⟩
  have hij' : P.next i ≠ P.next j := fun e => hij (P.next_injective e)
  rw [edge_rotate, edge_rotate, h.2 _ _ hij']
  simp only [rotate_next, rotate_v, P.next_injective.eq_iff]

/-- Iterated rotation. -/
def rotateBy : ℕ → Polygon E
  | 0 => P
  | r + 1 => (rotateBy r).rotate

theorem carrier_rotateBy (r : ℕ) : (P.rotateBy r).carrier = P.carrier := by
  induction r with
  | zero => rfl
  | succ r ih => simp only [rotateBy, carrier_rotate, ih]

theorem isSimple_rotateBy (h : P.IsSimple) (r : ℕ) : (P.rotateBy r).IsSimple := by
  induction r with
  | zero => exact h
  | succ r ih => exact (P.rotateBy r).isSimple_rotate ih

/-! ### Subdividing the closing edge -/

/-- The closing edge runs from the last vertex `v n` back to `v 0`. -/
lemma next_last : P.next (Fin.last P.n) = 0 := finRotate_last

lemma next_castSucc_lt (k : Fin P.n) :
    P.next k.castSucc = k.succ := by
  simp [next, finRotate_succ_apply, Fin.coeSucc_eq_succ]

/-- **Insert a vertex `c` on the closing edge** `[v n, v 0]`: the new vertex list is
`v 0, …, v n, c`. -/
def subdivideLast (c : E) : Polygon E where
  n := P.n + 1
  two_le := P.two_le.trans (Nat.le_succ _)
  v := Fin.snoc P.v c

/-- The new edges: the old non-closing edges are unchanged, the closing edge `[v n, v 0]` is
replaced by `[v n, c]` and `[c, v 0]`. -/
theorem carrier_subdivideLast (c : E) :
    (P.subdivideLast c).carrier =
      (⋃ k : Fin P.n, P.edge k.castSucc) ∪ segment ℝ (P.v (Fin.last P.n)) c ∪
        segment ℝ c (P.v 0) := by
  set Q := P.subdivideLast c
  have hv_cs : ∀ i : Fin (P.n + 1), Q.v i.castSucc = P.v i := fun i => by
    simp [Q, subdivideLast]
  have hv_last : Q.v (Fin.last (P.n + 1)) = c := by simp [Q, subdivideLast]
  -- edges of `Q` indexed by `castSucc (castSucc k)`, `castSucc (last)`, `last`.
  have hE1 : ∀ k : Fin P.n, Q.edge k.castSucc.castSucc = P.edge k.castSucc := fun k => by
    have hn : Q.next k.castSucc.castSucc = k.succ.castSucc := by
      rw [← Fin.succ_castSucc]; exact Q.next_castSucc_lt k.castSucc
    unfold edge
    rw [hn, hv_cs, hv_cs, P.next_castSucc_lt]
  have hE2 : Q.edge (Fin.last P.n).castSucc = segment ℝ (P.v (Fin.last P.n)) c := by
    have hn : Q.next (Fin.last P.n).castSucc = Fin.last (P.n + 1) := by
      rw [← Fin.succ_last]; exact Q.next_castSucc_lt (Fin.last P.n)
    unfold edge
    rw [hn, hv_cs, hv_last]
  have hE3 : Q.edge (Fin.last (P.n + 1)) = segment ℝ c (P.v 0) := by
    have hn : Q.next (Fin.last (P.n + 1)) = 0 := Q.next_last
    have h0 : (0 : Fin (P.n + 2)) = (0 : Fin (P.n + 1)).castSucc := rfl
    unfold edge
    rw [hn, hv_last, h0, hv_cs]
  ext x
  simp only [carrier, mem_iUnion, mem_union]
  constructor
  · rintro ⟨j, hj⟩
    induction j using Fin.lastCases with
    | last => exact Or.inr (hE3 ▸ hj)
    | cast i =>
      induction i using Fin.lastCases with
      | last => exact Or.inl (Or.inr (hE2 ▸ hj))
      | cast k => exact Or.inl (Or.inl ⟨k, hE1 k ▸ hj⟩)
  · rintro ((⟨k, hk⟩ | hx) | hx)
    · exact ⟨_, (hE1 k).symm ▸ hk⟩
    · exact ⟨_, hE2.symm ▸ hx⟩
    · exact ⟨_, hE3.symm ▸ hx⟩

end Polygon

/-! ## Links -/

/-- **A polygonal link**: finitely many simple polygons with pairwise disjoint point sets. The
component order and each component's starting vertex are presentation data; `Move.relabel`
identifies presentations that differ only in them. -/
structure PolygonalLink (E : Type*) [AddCommGroup E] [Module ℝ E] where
  /-- Number of components. -/
  k : ℕ
  /-- The components. -/
  comp : Fin k → Polygon E
  /-- Each component is simple. -/
  simple : ∀ i, (comp i).IsSimple
  /-- Distinct components are disjoint. -/
  disjoint : Pairwise fun i j => Disjoint (comp i).carrier (comp j).carrier

namespace PolygonalLink

/-- The point set of the link. -/
def carrier (L : PolygonalLink E) : Set E := ⋃ i, (L.comp i).carrier

end PolygonalLink

/-- **The one-step moves.**

* `relabel`: permute the components and re-index each cyclically.
* `delta`: Reidemeister's Δ-move on the closing edge `[a, b]` of component `m`: replace it by
  `[a, c] ∪ [c, b]` when the triangle `convexHull {a, b, c}` meets the link only in `[a, b]`. -/
inductive Move : PolygonalLink E → PolygonalLink E → Prop
  | relabel (L L' : PolygonalLink E) (e : Fin L.k ≃ Fin L'.k) (r : Fin L.k → ℕ)
      (h : ∀ i, L'.comp (e i) = (L.comp i).rotateBy (r i)) : Move L L'
  | delta (L L' : PolygonalLink E) (e : Fin L.k ≃ Fin L'.k) (m : Fin L.k) (c : E)
      (hother : ∀ i, i ≠ m → L'.comp (e i) = L.comp i)
      (hm : L'.comp (e m) = (L.comp m).subdivideLast c)
      (htri : convexHull ℝ {(L.comp m).v (Fin.last _), (L.comp m).v 0, c} ∩ L.carrier =
        segment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) : Move L L'

/-- **Δ-equivalence** of polygonal links: the equivalence relation generated by `Move`. -/
def DeltaEquiv : PolygonalLink E → PolygonalLink E → Prop := Relation.EqvGen Move

theorem deltaEquiv_equivalence : Equivalence (DeltaEquiv (E := E)) :=
  Relation.EqvGen.is_equivalence _

/-- The Δ-equivalence setoid, so that link types are `Quotient deltaSetoid`. -/
def deltaSetoid : Setoid (PolygonalLink E) := ⟨DeltaEquiv, deltaEquiv_equivalence⟩

/-- **A relabelling does not change the link's point set.** -/
theorem PolygonalLink.carrier_of_relabel (L L' : PolygonalLink E) (e : Fin L.k ≃ Fin L'.k)
    (r : Fin L.k → ℕ) (h : ∀ i, L'.comp (e i) = (L.comp i).rotateBy (r i)) :
    L'.carrier = L.carrier := by
  ext x
  simp only [PolygonalLink.carrier, mem_iUnion]
  constructor
  · rintro ⟨j, hj⟩
    obtain ⟨i, rfl⟩ := e.surjective j
    rw [h, Polygon.carrier_rotateBy] at hj
    exact ⟨i, hj⟩
  · rintro ⟨i, hi⟩
    exact ⟨e i, by rw [h, Polygon.carrier_rotateBy]; exact hi⟩

/-- **The number of components is preserved by a move.** -/
theorem Move.card_eq {L L' : PolygonalLink E} (h : Move L L') : L.k = L'.k := by
  cases h with
  | relabel e _ _ => simpa using Fintype.card_congr e
  | delta e _ _ _ _ _ => simpa using Fintype.card_congr e

/-- **The number of components is a Δ-invariant.** -/
theorem DeltaEquiv.card_eq {L L' : PolygonalLink E} (h : DeltaEquiv L L') : L.k = L'.k := by
  induction h with
  | rel _ _ h => exact h.card_eq
  | refl => rfl
  | symm _ _ _ ih => exact ih.symm
  | trans _ _ _ _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-! ## Non-vacuity in `ℝ³`

Points of `ℝ³` are `Fin 3 → ℝ`. Every proof below reduces segment membership to coordinates. -/

noncomputable section NonVacuity

/-- A point of `ℝ³`. -/
abbrev R3 := Fin 3 → ℝ

lemma mem_segment_coord {p q x : R3} (hx : x ∈ segment ℝ p q) :
    ∃ t : ℝ, 0 ≤ t ∧ t ≤ 1 ∧ ∀ i, x i = (1 - t) * p i + t * q i := by
  obtain ⟨a, b, ha, hb, hab, rfl⟩ := hx
  refine ⟨b, hb, by linarith, fun i => ?_⟩
  have : a = 1 - b := by linarith
  subst this
  simp [smul_eq_mul]

/-- The triangle with vertices `(0,0,h)`, `(1,0,h)`, `(0,1,h)`. -/
def stdTriangle (h : ℝ) : Polygon R3 where
  n := 2
  two_le := le_rfl
  v := ![![0, 0, h], ![1, 0, h], ![0, 1, h]]

/-- Every point of `stdTriangle h` lies in the plane `x₂ = h`. -/
lemma stdTriangle_coord_two (h : ℝ) {x : R3} (hx : x ∈ (stdTriangle h).carrier) : x 2 = h := by
  simp only [Polygon.carrier, mem_iUnion] at hx
  obtain ⟨i, hi⟩ := hx
  obtain ⟨t, -, -, hx⟩ := mem_segment_coord hi
  have := hx 2
  fin_cases i <;> simp [stdTriangle, Polygon.next] at this <;> linarith

/-- **An explicit simple polygon.** -/
theorem stdTriangle_isSimple (h : ℝ) : (stdTriangle h).IsSimple := by
  refine ⟨?_, fun i j hij => ?_⟩
  · intro i j hij
    fin_cases i <;> fin_cases j <;>
      first
      | rfl
      | (exfalso
         have h0 := congrFun hij 0
         have h1 := congrFun hij 1
         simp [stdTriangle] at h0 h1)
  · ext x
    simp only [mem_inter_iff]
    fin_cases i <;> fin_cases j <;> simp only [ne_eq, not_true_eq_false] at hij <;>
      simp [Polygon.next, Polygon.edge, stdTriangle] <;>
      (constructor
       · rintro ⟨h1, h2⟩
         obtain ⟨t, ht0, ht1, hx⟩ := mem_segment_coord h1
         obtain ⟨s, hs0, hs1, hy⟩ := mem_segment_coord h2
         have a0 := hx 0; have a1 := hx 1; have a2 := hx 2
         have b0 := hy 0; have b1 := hy 1; have b2 := hy 2
         simp at a0 a1 a2 b0 b1 b2
         funext k; fin_cases k <;> simp <;> linarith
       · rintro rfl
         first
         | exact ⟨left_mem_segment ℝ _ _, right_mem_segment ℝ _ _⟩
         | exact ⟨right_mem_segment ℝ _ _, left_mem_segment ℝ _ _⟩)

/-- **The unknot**, as the one-component link `stdTriangle 0`. -/
def unknot : PolygonalLink R3 where
  k := 1
  comp := fun _ => stdTriangle 0
  simple := fun _ => stdTriangle_isSimple 0
  disjoint := fun i j hij => absurd (Subsingleton.elim i j) hij

/-- **The two-component unlink**: the triangles at heights `0` and `1`. -/
def unlink₂ : PolygonalLink R3 where
  k := 2
  comp := fun i => stdTriangle (i : ℝ)
  simple := fun i => stdTriangle_isSimple _
  disjoint := by
    intro i j hij
    rw [Set.disjoint_left]
    intro x hi hj
    have e := (stdTriangle_coord_two _ hi).symm.trans (stdTriangle_coord_two _ hj)
    exact hij (Fin.ext (by exact_mod_cast e))

/-- **Δ-equivalence is not the total relation**: the unknot is not Δ-equivalent to the
two-component unlink, because the component count is a Δ-invariant. -/
theorem unknot_not_deltaEquiv_unlink₂ : ¬ DeltaEquiv unknot unlink₂ := by
  intro h
  have := h.card_eq
  simp [unknot, unlink₂] at this

/-- The apex of the example Δ-move: above the closing edge `[(0,1,0), (0,0,0)]`, out of the
plane of the triangle. -/
def apex : R3 := ![0, 1 / 2, 1]

/-- The result of the example Δ-move: the triangle with vertex `apex` inserted on its closing
edge, a skew quadrilateral. -/
def skewSquare : Polygon R3 := (stdTriangle 0).subdivideLast apex

lemma skewSquare_v : skewSquare.v = ![![0, 0, 0], ![1, 0, 0], ![0, 1, 0], ![0, 1 / 2, 1]] := by
  funext i; fin_cases i <;> rfl

lemma skewSquare_next : skewSquare.next = ![1, 2, 3, 0] := by
  funext i; fin_cases i <;> rfl

/-- The edges of `skewSquare`, written with explicit vertices. -/
lemma skewSquare_edge (i : Fin 4) :
    skewSquare.edge i = segment ℝ (![![0, 0, 0], ![1, 0, 0], ![0, 1, 0], ![0, 1 / 2, 1]] i)
      (![![0, 0, 0], ![1, 0, 0], ![0, 1, 0], ![0, 1 / 2, 1]] (![1, 2, 3, 0] i)) := by
  simp only [Polygon.edge, skewSquare_next, skewSquare_v]

set_option maxHeartbeats 1000000 in
theorem skewSquare_isSimple : skewSquare.IsSimple := by
  refine ⟨?_, fun i j hij => ?_⟩
  · intro i j hij
    rw [skewSquare_v] at hij
    fin_cases i <;> fin_cases j <;>
      first
      | rfl
      | (exfalso
         have h0 := congrFun hij 0
         have h1 := congrFun hij 1
         have h2 := congrFun hij 2
         revert h0 h1 h2
         norm_num)
  · have hv := skewSquare_v
    rw [skewSquare_edge, skewSquare_edge, skewSquare_next, hv]
    ext x
    simp only [mem_inter_iff]
    fin_cases i <;> fin_cases j <;> simp only [ne_eq, not_true_eq_false] at hij <;>
      simp (config := { decide := true }) <;>
      first
      | (intro h1 h2
         obtain ⟨t, ht0, ht1, hx⟩ := mem_segment_coord h1
         obtain ⟨s, hs0, hs1, hy⟩ := mem_segment_coord h2
         have a0 := hx 0; have a1 := hx 1; have a2 := hx 2
         have b0 := hy 0; have b1 := hy 1; have b2 := hy 2
         simp at a0 a1 a2 b0 b1 b2
         nlinarith)
      | (constructor
         · rintro ⟨h1, h2⟩
           obtain ⟨t, ht0, ht1, hx⟩ := mem_segment_coord h1
           obtain ⟨s, hs0, hs1, hy⟩ := mem_segment_coord h2
           have a0 := hx 0; have a1 := hx 1; have a2 := hx 2
           have b0 := hy 0; have b1 := hy 1; have b2 := hy 2
           simp at a0 a1 a2 b0 b1 b2
           funext k; fin_cases k <;> simp <;> nlinarith
         · rintro rfl
           first
           | exact ⟨left_mem_segment ℝ _ _, right_mem_segment ℝ _ _⟩
           | exact ⟨right_mem_segment ℝ _ _, left_mem_segment ℝ _ _⟩)

/-- The unknot presented as the skew quadrilateral. -/
def unknotSkew : PolygonalLink R3 where
  k := 1
  comp := fun _ => skewSquare
  simple := fun _ => skewSquare_isSimple
  disjoint := fun i j hij => absurd (Subsingleton.elim i j) hij

/-- The Δ-triangle of the example meets the triangle only in its closing edge. -/
lemma example_triangle_inter :
    convexHull ℝ {(stdTriangle 0).v (Fin.last _), (stdTriangle 0).v 0, apex} ∩
        unknot.carrier =
      segment ℝ ((stdTriangle 0).v (Fin.last _)) ((stdTriangle 0).v 0) := by
  have hcar : unknot.carrier = (stdTriangle 0).carrier := by
    ext x; simp only [unknot, PolygonalLink.carrier, mem_iUnion]
    exact ⟨fun ⟨_, h⟩ => h, fun h => ⟨⟨0, Nat.one_pos⟩, h⟩⟩
  rw [hcar]
  apply Subset.antisymm
  · rintro x ⟨hx, hxL⟩
    have hz : x 2 = 0 := stdTriangle_coord_two 0 hxL
    -- the hull lies in a convex wedge cut out by four linear (in)equalities
    let C : Set R3 := {y | y 0 = 0 ∧ 0 ≤ y 2 ∧ y 2 / 2 ≤ y 1 ∧ y 1 ≤ 1 - y 2 / 2}
    have hC : Convex ℝ C := by
      intro y hy w hw a b ha hb hab
      obtain ⟨hy0, hy2, hy1, hy1'⟩ := hy
      obtain ⟨hw0, hw2, hw1, hw1'⟩ := hw
      simp only [C, Set.mem_setOf_eq, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
      refine ⟨by rw [hy0, hw0]; ring, by positivity, ?_, ?_⟩ <;>
        nlinarith [mul_le_mul_of_nonneg_left hy1 ha, mul_le_mul_of_nonneg_left hw1 hb,
          mul_le_mul_of_nonneg_left hy1' ha, mul_le_mul_of_nonneg_left hw1' hb]
    have hsub : {(stdTriangle 0).v (Fin.last _), (stdTriangle 0).v 0, apex} ⊆ C := by
      intro y hy
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hy
      rcases hy with rfl | rfl | rfl <;> (simp [C, stdTriangle, apex]; try norm_num)
    obtain ⟨h0, -, h1, h1'⟩ := convexHull_min hsub hC hx
    rw [hz] at h1 h1'
    refine ⟨x 1, 1 - x 1, by linarith, by linarith, by ring, ?_⟩
    funext i
    fin_cases i <;> simp [stdTriangle, h0, hz]
  · intro x hx
    refine ⟨segment_subset_convexHull (by simp) (by simp) hx, ?_⟩
    exact (stdTriangle 0).edge_subset_carrier (Fin.last _) (by
      simpa [Polygon.edge, Polygon.next_last] using hx)

/-- **An explicit Δ-move** from the triangle unknot to the skew quadrilateral, so `Move.delta`
is not vacuous. -/
theorem move_unknot_unknotSkew : Move unknot unknotSkew :=
  Move.delta unknot unknotSkew (Equiv.refl _) (⟨0, Nat.one_pos⟩ : Fin 1) apex
    (fun i hi => absurd (Subsingleton.elim (α := Fin 1) i ⟨0, Nat.one_pos⟩) hi) rfl
    example_triangle_inter

end NonVacuity

end QOU.MathlibExt.PL
