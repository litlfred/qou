/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLSurfaceSlice
import QOU.MathlibExt.PLPolygonalLink
import Mathlib.Combinatorics.SimpleGraph.Matching

set_option autoImplicit false

/-!
# A 2-regular 1-complex is a disjoint union of simple polygons (issue #8902, part B)

The slice of a closed surface is 2-regular (`slice_vertex_degree`). This file turns such a
complex into polygons: its vertex graph is a disjoint union of cycles (Mathlib's
`SimpleGraph.IsCycles`), and a cycle read off as a vertex sequence is a simple polygon whose edges
are faces of the complex.

## What is a DEFINITION here

* `complexGraph S` — the graph on the vertices of `S` whose edges are the 2-element faces.
* `cyclePolygon p hp` — the polygon whose vertices are the vertices of a graph cycle `p`.

## What is a THEOREM here

* `Polygon.isSimple_of_faces` — a polygon with distinct vertices whose edges are faces of one
  simplicial complex is simple.
* `complexGraph_ncard_neighborSet` — in a 2-regular complex every vertex has two neighbours.
* `cyclePolygon_isSimple`.
* `exists_polygons_of_twoRegular` — **a finite 2-regular 1-complex is the union of finitely many
  simple polygons with pairwise disjoint carriers.**
-/

namespace QOU.MathlibExt.PL

open Set Geometry

universe u

variable {E : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [DecidableEq E]

namespace Polygon

lemma next_val_ite (P : Polygon E) (i : Fin (P.n + 1)) :
    (P.next i : ℕ) = if (i : ℕ) = P.n then 0 else (i : ℕ) + 1 := by
  have hi := i.2
  unfold next
  rw [coe_finRotate]
  split_ifs with h1 h2 h2
  · rfl
  · exact absurd (by rw [h1]; rfl) h2
  · exact absurd (Fin.ext (by rw [h2]; rfl)) h1
  · rfl

lemma next_next_ne (P : Polygon E) (i : Fin (P.n + 1)) : P.next (P.next i) ≠ i := by
  intro h
  have h2 := P.two_le
  have hi := i.2
  have := congrArg Fin.val h
  rw [next_val_ite, next_val_ite] at this
  split_ifs at this <;> omega

lemma edge_eq_convexHull (P : Polygon E) (i : Fin (P.n + 1)) :
    P.edge i = convexHull ℝ ((({P.v i, P.v (P.next i)} : Finset E)) : Set E) := by
  rw [coe_pair_convexHull]; rfl

/-- **Distinct vertices and edges that are faces of one complex give a simple polygon.** -/
theorem isSimple_of_faces (P : Polygon E) (K : SimplicialComplex ℝ E)
    (hinj : Function.Injective P.v)
    (hface : ∀ i, ({P.v i, P.v (P.next i)} : Finset E) ∈ K.faces) : P.IsSimple := by
  have hint : ∀ i j, P.edge i ∩ P.edge j = convexHull ℝ
      (((({P.v i, P.v (P.next i)} : Finset E) ∩ {P.v j, P.v (P.next j)} : Finset E)) : Set E) := by
    intro i j
    rw [edge_eq_convexHull, edge_eq_convexHull, K.convexHull_inter_convexHull (hface i) (hface j),
      Finset.coe_inter]
  have hne := P.next_ne
  have hnn := P.next_next_ne
  have hninj := P.next_injective
  refine P.isSimple_of hinj (fun i => ?_) (fun i j hij h1 h2 => ?_)
  · rw [hint]
    have : (({P.v i, P.v (P.next i)} : Finset E) ∩ {P.v (P.next i), P.v (P.next (P.next i))}) =
        {P.v (P.next i)} := by
      ext z
      simp only [Finset.mem_inter, Finset.mem_insert, Finset.mem_singleton]
      constructor
      · rintro ⟨rfl | rfl, h'⟩
        · rcases h' with h' | h'
          · exact absurd (hinj h') (hne i).symm
          · exact absurd (hinj h') (hnn i).symm
        · rfl
      · rintro rfl; exact ⟨Or.inr rfl, Or.inl rfl⟩
    rw [this, Finset.coe_singleton, convexHull_singleton]
  · rw [Set.disjoint_iff_inter_eq_empty, hint]
    have : (({P.v i, P.v (P.next i)} : Finset E) ∩ {P.v j, P.v (P.next j)}) = ∅ := by
      ext z
      simp only [Finset.mem_inter, Finset.mem_insert, Finset.mem_singleton,
        Finset.notMem_empty, iff_false, not_and]
      rintro (rfl | rfl) (h' | h')
      · exact hij (hinj h')
      · exact h2 (hinj h')
      · exact h1 (hinj h').symm
      · exact hij (hninj (hinj h'))
    rw [this, Finset.coe_empty, convexHull_empty]

end Polygon

/-! ### The vertex graph of a complex -/

/-- The graph on the vertices of `S` with an edge for each 2-element face. -/
def complexGraph (S : SimplicialComplex ℝ E) : SimpleGraph S.vertices where
  Adj x y := x ≠ y ∧ ({x.1, y.1} : Finset E) ∈ S.faces
  symm := fun x y ⟨h, h'⟩ => ⟨h.symm, by rwa [Finset.pair_comm]⟩
  loopless := fun _ ⟨h, _⟩ => h rfl

lemma complexGraph_adj {S : SimplicialComplex ℝ E} {x y : S.vertices} :
    (complexGraph S).Adj x y ↔ x ≠ y ∧ ({x.1, y.1} : Finset E) ∈ S.faces := Iff.rfl

/-- **2-regular complexes give 2-regular graphs.** -/
theorem complexGraph_ncard_neighborSet {S : SimplicialComplex ℝ E}
    (hdeg : ∀ x, {x} ∈ S.faces → {σ | σ ∈ S.faces ∧ x ∈ σ ∧ σ.card = 2}.ncard = 2)
    (x : S.vertices) : ((complexGraph S).neighborSet x).ncard = 2 := by
  rw [← hdeg x.1 x.2]
  have himage : {σ | σ ∈ S.faces ∧ x.1 ∈ σ ∧ σ.card = 2} =
      (fun y : S.vertices => ({x.1, y.1} : Finset E)) '' (complexGraph S).neighborSet x := by
    ext σ
    constructor
    · rintro ⟨hσ, hxσ, h2⟩
      obtain ⟨a, b, hab, rfl⟩ := Finset.card_eq_two.mp h2
      rw [Finset.mem_insert, Finset.mem_singleton] at hxσ
      rcases hxσ with h | h
      · have hb : b ∈ S.vertices := S.down_closed hσ (by simp) (by simp)
        refine ⟨⟨b, hb⟩, ⟨fun he => hab (by rw [← h, he]), by rw [h]; exact hσ⟩, ?_⟩
        simp [h]
      · have ha : a ∈ S.vertices := S.down_closed hσ (by simp) (by simp)
        refine ⟨⟨a, ha⟩, ⟨fun he => hab (by rw [← h, he]), by rw [h, Finset.pair_comm]; exact hσ⟩,
          ?_⟩
        simp [h, Finset.pair_comm]
    · rintro ⟨y, ⟨hxy, hface⟩, rfl⟩
      refine ⟨hface, by simp, Finset.card_pair fun h => hxy (Subtype.ext h)⟩
  rw [himage, Set.ncard_image_of_injOn]
  intro y _ y' _ h
  have : y.1 ∈ ({x.1, y'.1} : Finset E) := by
    have : y.1 ∈ ({x.1, y.1} : Finset E) := by simp
    simp only at h
    rwa [h] at this
  simp only [Finset.mem_insert, Finset.mem_singleton] at this
  rcases this with h1 | h1
  · -- y = x is impossible as y is a neighbour
    rename_i hy _
    exact absurd (Subtype.ext h1).symm hy.1
  · exact Subtype.ext h1

/-! ### The polygon of a cycle -/

variable {S : SimplicialComplex ℝ E}

/-- The polygon with the vertices of a cycle of `complexGraph S`, in order. -/
noncomputable def cyclePolygon {x : S.vertices} (p : (complexGraph S).Walk x x)
    (hp : p.IsCycle) : Polygon E where
  n := p.length - 1
  two_le := by have := hp.three_le_length; omega
  v := fun i => (p.getVert i).1

lemma cyclePolygon_v_next {x : S.vertices} (p : (complexGraph S).Walk x x) (hp : p.IsCycle)
    (i : Fin ((cyclePolygon p hp).n + 1)) :
    (cyclePolygon p hp).v ((cyclePolygon p hp).next i) = (p.getVert ((i : ℕ) + 1)).1 := by
  have h3 := hp.three_le_length
  have hn : (cyclePolygon p hp).n = p.length - 1 := rfl
  show (p.getVert ((cyclePolygon p hp).next i : ℕ)).1 = _
  rw [Polygon.next_val_ite]
  split_ifs with h
  · rw [show (i : ℕ) + 1 = p.length by omega, SimpleGraph.Walk.getVert_length,
      SimpleGraph.Walk.getVert_zero]
  · rfl

lemma cyclePolygon_v (x : S.vertices) (p : (complexGraph S).Walk x x) (hp : p.IsCycle)
    (i : Fin ((cyclePolygon p hp).n + 1)) : (cyclePolygon p hp).v i = (p.getVert i).1 := rfl

lemma cyclePolygon_lt {x : S.vertices} (p : (complexGraph S).Walk x x) (hp : p.IsCycle)
    (i : Fin ((cyclePolygon p hp).n + 1)) : (i : ℕ) < p.length := by
  have h3 := hp.three_le_length
  have := i.2
  have hn : (cyclePolygon p hp).n = p.length - 1 := rfl
  omega

lemma cyclePolygon_face {x : S.vertices} (p : (complexGraph S).Walk x x) (hp : p.IsCycle)
    (i : Fin ((cyclePolygon p hp).n + 1)) :
    ({(cyclePolygon p hp).v i, (cyclePolygon p hp).v ((cyclePolygon p hp).next i)} : Finset E) ∈
      S.faces := by
  rw [cyclePolygon_v_next]
  exact (p.adj_getVert_succ (cyclePolygon_lt p hp i)).2

theorem cyclePolygon_isSimple {x : S.vertices} (p : (complexGraph S).Walk x x) (hp : p.IsCycle) :
    (cyclePolygon p hp).IsSimple := by
  refine (cyclePolygon p hp).isSimple_of_faces S (fun i j h => ?_) (cyclePolygon_face p hp)
  have hi := cyclePolygon_lt p hp i
  have hj := cyclePolygon_lt p hp j
  exact Fin.ext (hp.getVert_injOn' (show (i : ℕ) ≤ p.length - 1 by omega)
    (show (j : ℕ) ≤ p.length - 1 by omega) (Subtype.ext h))

/-- A vertex of a cycle polygon is a vertex on the cycle. -/
lemma cyclePolygon_v_mem {x : S.vertices} (p : (complexGraph S).Walk x x) (hp : p.IsCycle)
    (i : Fin ((cyclePolygon p hp).n + 1)) :
    ∃ y : S.vertices, y ∈ p.support ∧ (cyclePolygon p hp).v i = y.1 :=
  ⟨p.getVert i, p.getVert_mem_support _, rfl⟩

lemma cyclePolygon_v_next_mem {x : S.vertices} (p : (complexGraph S).Walk x x) (hp : p.IsCycle)
    (i : Fin ((cyclePolygon p hp).n + 1)) :
    ∃ y : S.vertices, y ∈ p.support ∧ (cyclePolygon p hp).v ((cyclePolygon p hp).next i) = y.1 :=
  ⟨p.getVert ((i : ℕ) + 1), p.getVert_mem_support _, cyclePolygon_v_next p hp i⟩

/-- A point of the carrier of a cycle polygon lies in the hull of a face spanned by cycle
vertices. -/
lemma mem_cyclePolygon_carrier {x : S.vertices} (p : (complexGraph S).Walk x x) (hp : p.IsCycle)
    {z : E} (hz : z ∈ (cyclePolygon p hp).carrier) :
    ∃ a b : S.vertices, a ∈ p.support ∧ b ∈ p.support ∧
      z ∈ convexHull ℝ ((({a.1, b.1} : Finset E)) : Set E) ∧
      ({a.1, b.1} : Finset E) ∈ S.faces := by
  obtain ⟨i, hi⟩ := mem_iUnion.mp hz
  obtain ⟨a, ha, hav⟩ := cyclePolygon_v_mem p hp i
  obtain ⟨b, hb, hbv⟩ := cyclePolygon_v_next_mem p hp i
  have hf := cyclePolygon_face p hp i
  rw [Polygon.edge_eq_convexHull, hav, hbv] at hi
  rw [hav, hbv] at hf
  exact ⟨a, b, ha, hb, hi, hf⟩

/-- **A finite 2-regular 1-complex is a disjoint union of simple polygons.** -/
theorem exists_polygons_of_twoRegular (hfin : S.faces.Finite) (hdim : ∀ s ∈ S.faces, s.card ≤ 2)
    (hdeg : ∀ x, {x} ∈ S.faces → {σ | σ ∈ S.faces ∧ x ∈ σ ∧ σ.card = 2}.ncard = 2) :
    ∃ (ι : Type u) (_ : Finite ι) (P : ι → Polygon E), (∀ i, (P i).IsSimple) ∧
      Pairwise (fun i j => Disjoint (P i).carrier (P j).carrier) ∧ ⋃ i, (P i).carrier = S.space := by
  classical
  set G := complexGraph S with hG
  haveI : Finite S.vertices := by
    rw [SimplicialComplex.vertices_eq]
    exact (hfin.biUnion fun k _ => k.finite_toSet).to_subtype
  have hdeg2 := complexGraph_ncard_neighborSet hdeg
  have hcyc : G.IsCycles := fun v _ => hdeg2 v
  have hne : ∀ v, (G.neighborSet v).Nonempty := fun v =>
    Set.nonempty_of_ncard_ne_zero (by rw [hdeg2 v]; omega)
  have hex : ∀ c : G.ConnectedComponent, ∃ (p : G.Walk c.out c.out), p.IsCycle ∧
      p.toSubgraph.verts = c.supp := fun c =>
    hcyc.exists_cycle_toSubgraph_verts_eq_connectedComponentSupp
      ((c.mem_supp_iff _).mpr (Quot.out_eq c)) (hne _)
  choose p hp hverts using hex
  refine ⟨G.ConnectedComponent, inferInstance, fun c => cyclePolygon (p c) (hp c),
    fun c => cyclePolygon_isSimple _ _, ?_, ?_⟩
  · intro c c' hcc'
    refine Set.disjoint_left.mpr fun z hz hz' => ?_
    obtain ⟨a, b, ha, hb, hzab, hfab⟩ := mem_cyclePolygon_carrier (p c) (hp c) hz
    obtain ⟨a', b', ha', hb', hzab', hfab'⟩ := mem_cyclePolygon_carrier (p c') (hp c') hz'
    have hmem := S.inter_subset_convexHull hfab hfab' ⟨hzab, hzab'⟩
    rw [← Finset.coe_inter] at hmem
    have hemp : (({a.1, b.1} : Finset E) ∩ {a'.1, b'.1}) = ∅ := by
      have hsupp : ∀ (u : S.vertices), u ∈ (p c).support → ∀ (u' : S.vertices),
          u' ∈ (p c').support → u.1 ≠ u'.1 := by
        intro u hu u' hu' h
        have h1 : u ∈ c.supp := by rw [← hverts c, SimpleGraph.Walk.mem_verts_toSubgraph]; exact hu
        have h2 : u' ∈ c'.supp := by
          rw [← hverts c', SimpleGraph.Walk.mem_verts_toSubgraph]; exact hu'
        rw [Subtype.ext h] at h1
        exact hcc' (((c.mem_supp_iff _).mp h1).symm.trans ((c'.mem_supp_iff _).mp h2))
      ext w
      simp only [Finset.mem_inter, Finset.mem_insert, Finset.mem_singleton,
        Finset.notMem_empty, iff_false, not_and]
      rintro (rfl | rfl) (h | h)
      · exact hsupp a ha a' ha' h
      · exact hsupp a ha b' hb' h
      · exact hsupp b hb a' ha' h
      · exact hsupp b hb b' hb' h
    rw [hemp, Finset.coe_empty, convexHull_empty] at hmem
    exact hmem
  · apply Subset.antisymm
    · intro z hz
      obtain ⟨c, hc⟩ := mem_iUnion.mp hz
      obtain ⟨a, b, -, -, hzab, hfab⟩ := mem_cyclePolygon_carrier (p c) (hp c) hc
      exact S.convexHull_subset_space hfab hzab
    intro z hz
    obtain ⟨σ, hσ, hzσ⟩ := (SimplicialComplex.mem_space_iff).mp hz
    -- every vertex lies on its cycle
    have hvert : ∀ a : S.vertices,
        a.1 ∈ (cyclePolygon (p (G.connectedComponentMk a)) (hp _)).carrier := by
      intro a
      set c := G.connectedComponentMk a
      have ha : a ∈ (p c).support := by
        rw [← SimpleGraph.Walk.mem_verts_toSubgraph, hverts c]; rfl
      obtain ⟨i, hi, hil⟩ := SimpleGraph.Walk.mem_support_iff_exists_getVert.mp ha
      have h3 := (hp c).three_le_length
      have hn : (cyclePolygon (p c) (hp c)).n = (p c).length - 1 := rfl
      by_cases hl : i = (p c).length
      · refine mem_iUnion.mpr ⟨⟨0, by omega⟩, ?_⟩
        have : (cyclePolygon (p c) (hp c)).v ⟨0, by omega⟩ = a.1 := by
          rw [cyclePolygon_v]
          simp only
          rw [SimpleGraph.Walk.getVert_zero, ← SimpleGraph.Walk.getVert_length (p c), ← hl, hi]
        rw [← this]; exact left_mem_segment ℝ _ _
      · refine mem_iUnion.mpr ⟨⟨i, by omega⟩, ?_⟩
        have : (cyclePolygon (p c) (hp c)).v ⟨i, by omega⟩ = a.1 := by
          rw [cyclePolygon_v]; simp only; rw [hi]
        rw [← this]; exact left_mem_segment ℝ _ _
    rcases Nat.lt_or_ge σ.card 2 with h1 | h2
    · obtain ⟨a, rfl⟩ := Finset.card_eq_one.mp (show σ.card = 1 by
        have := Finset.card_pos.mpr (S.nonempty_of_mem_faces hσ); omega)
      rw [Finset.coe_singleton, convexHull_singleton, mem_singleton_iff] at hzσ
      subst hzσ
      exact mem_iUnion.mpr ⟨_, hvert ⟨z, hσ⟩⟩
    obtain ⟨a, b, hab, rfl⟩ := Finset.card_eq_two.mp (le_antisymm (hdim σ hσ) h2)
    have ha : a ∈ S.vertices := S.down_closed hσ (by simp) (by simp)
    have hb : b ∈ S.vertices := S.down_closed hσ (by simp) (by simp)
    set A : S.vertices := ⟨a, ha⟩
    set B : S.vertices := ⟨b, hb⟩
    have hAB : G.Adj A B := ⟨fun h => hab (congrArg Subtype.val h), hσ⟩
    set c := G.connectedComponentMk A
    have hA : A ∈ (p c).support := by
      rw [← SimpleGraph.Walk.mem_verts_toSubgraph, hverts c]; rfl
    have hnb : (p c).toSubgraph.neighborSet A = G.neighborSet A :=
      Set.eq_of_subset_of_ncard_le ((p c).toSubgraph.neighborSet_subset A)
        (by rw [hdeg2, (hp c).ncard_neighborSet_toSubgraph_eq_two hA]) (Set.toFinite _)
    have hsub : (p c).toSubgraph.Adj A B := by
      have : B ∈ (p c).toSubgraph.neighborSet A := by rw [hnb]; exact hAB
      exact this
    obtain ⟨i, hi, hil⟩ := (SimpleGraph.Walk.toSubgraph_adj_iff _).mp hsub
    have h3 := (hp c).three_le_length
    have hn : (cyclePolygon (p c) (hp c)).n = (p c).length - 1 := rfl
    set j : Fin ((cyclePolygon (p c) (hp c)).n + 1) := ⟨i, by omega⟩
    refine mem_iUnion.mpr ⟨c, mem_iUnion.mpr ⟨j, ?_⟩⟩
    have hv1 : (cyclePolygon (p c) (hp c)).v j = ((p c).getVert i).1 := rfl
    have hv2 := cyclePolygon_v_next (p c) (hp c) j
    unfold Polygon.edge
    rw [hv1, hv2, ← convexHull_pair]
    rcases Sym2.eq_iff.mp hi with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · rw [h1, show (j : ℕ) = i from rfl, h2]
      simpa using hzσ
    · rw [h1, show (j : ℕ) = i from rfl, h2, Set.pair_comm]
      simpa using hzσ

end QOU.MathlibExt.PL
