/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLPolygonalLink

set_option autoImplicit false

/-!
# Deleting a vertex (issue #8902, isotopy-to-Δ bridge, local stability)

Stage 1 builds a Δ-move forwards: `deltaMove` inserts a vertex and proves the result simple. Read
backwards, a Δ-move deletes a vertex, and then the *smaller* polygon has to be shown simple. This
file does that. Let `Q = M.subdivideLast c` be simple, with `M`'s closing edge `[x, y]`. If the
triangle `convexHull {x, y, c}` meets each non-closing edge of `M` only in `{x, y}`, then `M` is
simple.

## What is a THEOREM here

* `Polygon.IsSimple.eq_or_next_eq_of_v_mem_edge` — in a simple polygon, vertex `j` lies on edge
  `i` only when `i = j` or `next i = j`.
* `Polygon.isSimple_of_isSimple_subdivideLast` — deleting the last vertex keeps simplicity under
  the triangle condition.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

namespace Polygon

/-- **A vertex lies only on its own two edges.** -/
lemma IsSimple.eq_or_next_eq_of_v_mem_edge {P : Polygon E} (h : P.IsSimple)
    {i j : Fin (P.n + 1)} (hv : P.v j ∈ P.edge i) : i = j ∨ P.next i = j := by
  by_contra hcon
  push_neg at hcon
  have hmem : P.v j ∈ P.edge i ∩ P.edge j := ⟨hv, left_mem_segment ℝ _ _⟩
  rw [h.2 i j hcon.1] at hmem
  split_ifs at hmem with h1 h2
  · exact hcon.2 h1.symm
  · exact hcon.1 (h.1 (Set.mem_singleton_iff.mp hmem)).symm
  · exact hmem

/-- A point on two distinct edges of a simple polygon is their shared vertex. -/
lemma IsSimple.mem_inter_edge {P : Polygon E} (h : P.IsSimple) {i j : Fin (P.n + 1)}
    (hij : i ≠ j) {z : E} (hz : z ∈ P.edge i ∩ P.edge j) :
    (j = P.next i ∧ z = P.v j) ∨ (i = P.next j ∧ z = P.v i) := by
  rw [h.2 i j hij] at hz
  split_ifs at hz with h1 h2
  · exact Or.inl ⟨h1, hz⟩
  · exact Or.inr ⟨h2, hz⟩
  · exact absurd hz (Set.notMem_empty z)

variable (M : Polygon E) (c : E)

/-- **Deleting a vertex keeps a polygon simple**, when the triangle it cuts off is clear. -/
theorem isSimple_of_isSimple_subdivideLast (hQ : (M.subdivideLast c).IsSimple)
    (hT : ∀ k : Fin (M.n + 1), k ≠ Fin.last M.n →
      convexHull ℝ {M.v (Fin.last M.n), M.v 0, c} ∩ M.edge k ⊆
        {M.v (Fin.last M.n), M.v 0}) :
    M.IsSimple := by
  set Q := M.subdivideLast c with hQdef
  set x := M.v (Fin.last M.n)
  set y := M.v 0
  have h2 := M.two_le
  have hxy_T : segment ℝ x y ⊆ convexHull ℝ {x, y, c} :=
    segment_subset_convexHull (by simp) (by simp)
  have hvx : x = Q.v (Fin.last M.n).castSucc := (M.subdivideLast_v_castSucc c _).symm
  have hvy : y = Q.v 0 := (M.subdivideLast_v_castSucc c 0).symm
  have hlast0 : (Fin.last M.n : Fin (M.n + 1)) ≠ 0 := by
    intro h; have := congrArg Fin.val h; simp at this; omega
  -- `x` and `y` on a non-closing edge `k`
  have hx_edge : ∀ k : Fin (M.n + 1), k ≠ Fin.last M.n → x ∈ M.edge k →
      M.next k = Fin.last M.n := by
    intro k hk hx
    rw [← M.subdivideLast_edge_castSucc c hk, hvx] at hx
    rcases hQ.eq_or_next_eq_of_v_mem_edge hx with h | h
    · exact absurd (Fin.castSucc_injective _ h) hk
    · rw [M.subdivideLast_next_castSucc c hk] at h
      exact Fin.castSucc_injective _ h
  have hy_edge : ∀ k : Fin (M.n + 1), k ≠ Fin.last M.n → y ∈ M.edge k → k = 0 := by
    intro k hk hy
    rw [← M.subdivideLast_edge_castSucc c hk, hvy] at hy
    rcases hQ.eq_or_next_eq_of_v_mem_edge hy with h | h
    · exact Fin.castSucc_injective _ (h.trans rfl)
    · rw [M.subdivideLast_next_castSucc c hk] at h
      have : M.next k = 0 := Fin.castSucc_injective _ (h.trans rfl)
      exfalso; apply hk
      exact M.next_injective (this.trans M.next_last.symm)
  -- the closing edge meets a non-closing edge `k` only in `{x, y}`
  have hcl : ∀ k : Fin (M.n + 1), k ≠ Fin.last M.n → ∀ z, z ∈ M.edge k →
      z ∈ M.edge (Fin.last M.n) → z = x ∨ z = y := by
    intro k hk z hzk hzl
    rw [M.edge_last] at hzl
    have := hT k hk ⟨hxy_T hzl, hzk⟩
    simpa using this
  have hnext_ne : ∀ k : Fin (M.n + 1), k ≠ Fin.last M.n → M.next k ≠ Fin.last M.n →
      (Q.next k.castSucc) = (M.next k).castSucc := fun k hk _ =>
    M.subdivideLast_next_castSucc c hk
  refine M.isSimple_of ?_ ?_ ?_
  · intro i j he
    have : Q.v i.castSucc = Q.v j.castSucc := by
      rw [M.subdivideLast_v_castSucc, M.subdivideLast_v_castSucc]; exact he
    exact Fin.castSucc_injective _ (hQ.1 this)
  · intro i
    by_cases hi : i = Fin.last M.n
    · -- closing edge, then edge `0`
      subst hi
      rw [M.next_last]
      have h0 : (0 : Fin (M.n + 1)) ≠ Fin.last M.n := hlast0.symm
      apply Subset.antisymm
      · rintro z ⟨hzl, hz0⟩
        rcases hcl 0 h0 z hz0 hzl with rfl | rfl
        · exfalso
          have := hx_edge 0 h0 hz0
          have hv : (M.next 0).val = 1 := by
            simp only [next, coe_finRotate]; split_ifs with h <;> simp_all
          have := congrArg Fin.val this; simp at this; omega
        · rfl
      · rintro z rfl
        exact ⟨by rw [M.edge_last]; exact right_mem_segment ℝ _ _, left_mem_segment ℝ _ _⟩
    · by_cases hn : M.next i = Fin.last M.n
      · rw [hn]
        apply Subset.antisymm
        · rintro z ⟨hzi, hzl⟩
          rcases hcl i hi z hzi hzl with rfl | rfl
          · rfl
          · exfalso
            have hi0 := hy_edge i hi hzi
            subst hi0
            have hv : (M.next 0).val = 1 := by
              simp only [next, coe_finRotate]; split_ifs with h <;> simp_all
            have := congrArg Fin.val hn; simp at this; omega
        · rintro z rfl
          refine ⟨?_, by rw [M.edge_last]; exact left_mem_segment ℝ _ _⟩
          have : M.edge i = segment ℝ (M.v i) (M.v (M.next i)) := rfl
          rw [this, hn]; exact right_mem_segment ℝ _ _
      · have hadj := hQ.adj i.castSucc
        rw [M.subdivideLast_next_castSucc c hi, M.subdivideLast_edge_castSucc c hi,
          M.subdivideLast_edge_castSucc c hn, M.subdivideLast_v_castSucc] at hadj
        exact hadj
  · intro i j hij h1 h2
    by_cases hi : i = Fin.last M.n
    · subst hi
      have hj : j ≠ Fin.last M.n := Ne.symm hij
      refine Set.disjoint_left.mpr fun z hzl hzj => ?_
      rcases hcl j hj z hzj hzl with rfl | rfl
      · exact h2 (hx_edge j hj hzj).symm
      · exact h1 (by rw [hy_edge j hj hzj, M.next_last])
    · by_cases hj : j = Fin.last M.n
      · subst hj
        refine Set.disjoint_left.mpr fun z hzi hzl => ?_
        rcases hcl i hi z hzi hzl with rfl | rfl
        · exact h1 (hx_edge i hi hzi).symm
        · exact h2 (by rw [hy_edge i hi hzi, M.next_last])
      · have e1 : j.castSucc ≠ Q.next i.castSucc := by
          rw [M.subdivideLast_next_castSucc c hi]
          exact fun h => h1 (Fin.castSucc_injective _ h)
        have e2 : i.castSucc ≠ Q.next j.castSucc := by
          rw [M.subdivideLast_next_castSucc c hj]
          exact fun h => h2 (Fin.castSucc_injective _ h)
        have hd := hQ.disj (fun h => hij (Fin.castSucc_injective _ h)) e1 e2
        rwa [M.subdivideLast_edge_castSucc c hi, M.subdivideLast_edge_castSucc c hj] at hd

/-- The carrier of `M` lies in that of `M.subdivideLast c` together with `M`'s closing edge. -/
lemma carrier_subset_subdivideLast_union :
    M.carrier ⊆ (M.subdivideLast c).carrier ∪ segment ℝ (M.v (Fin.last M.n)) (M.v 0) := by
  intro z hz
  obtain ⟨k, hk⟩ := Set.mem_iUnion.mp hz
  by_cases hkl : k = Fin.last M.n
  · subst hkl; rw [M.edge_last] at hk; exact Or.inr hk
  · rw [← M.subdivideLast_edge_castSucc c hkl] at hk
    exact Or.inl ((M.subdivideLast c).edge_subset_carrier _ hk)

/-- In `Q = M.subdivideLast c`, a point of a non-closing edge of `M` that also lies on one of the
two new edges `[x, c]`, `[c, y]` is `x` or `y`. -/
lemma mem_new_edges (hQ : (M.subdivideLast c).IsSimple) {k : Fin (M.n + 1)}
    (hk : k ≠ Fin.last M.n) {z : E} (hzk : z ∈ M.edge k)
    (hz : z ∈ segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0)) :
    z = M.v (Fin.last M.n) ∨ z = M.v 0 := by
  set Q := M.subdivideLast c
  rw [← M.subdivideLast_edge_castSucc c hk] at hzk
  rcases hz with hz | hz
  · rw [← M.subdivideLast_edge_castSucc_last c] at hz
    have hne : k.castSucc ≠ (Fin.last M.n).castSucc :=
      fun h => hk (Fin.castSucc_injective _ h)
    rcases hQ.mem_inter_edge hne ⟨hzk, hz⟩ with ⟨-, rfl⟩ | ⟨h1, -⟩
    · exact Or.inl (M.subdivideLast_v_castSucc c _)
    · rw [M.subdivideLast_next_castSucc_last c] at h1
      exact absurd h1 (Fin.castSucc_ne_last _)
  · rw [← M.subdivideLast_edge_last c] at hz
    have hne : k.castSucc ≠ Fin.last (M.n + 1) := Fin.castSucc_ne_last _
    rcases hQ.mem_inter_edge hne ⟨hzk, hz⟩ with ⟨h1, -⟩ | ⟨h1, rfl⟩
    · rw [M.subdivideLast_next_castSucc c hk] at h1
      exact absurd h1.symm (Fin.castSucc_ne_last _)
    · rw [M.subdivideLast_next_last c] at h1
      rw [h1]; exact Or.inr (M.subdivideLast_v_castSucc c 0)

end Polygon

namespace PolygonalLink

variable (L : PolygonalLink E) (m : Fin L.k) (M : Polygon E) (c : E)

/-- **Deleting a vertex from a link.** If component `m` of `L` is `M.subdivideLast c`, and the
triangle `convexHull {x, y, c}` (where `[x, y]` is `M`'s closing edge) meets the link only in the
two edges `[x, c]`, `[c, y]`, then replacing the component by `M` gives a link. -/
noncomputable def dropLast (hm : L.comp m = M.subdivideLast c)
    (hT : convexHull ℝ {M.v (Fin.last M.n), M.v 0, c} ∩ L.carrier ⊆
      segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0)) : PolygonalLink E :=
  have hQ : (M.subdivideLast c).IsSimple := hm ▸ L.simple m
  have hnew : segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0) ⊆ (L.comp m).carrier := by
    rw [hm, ← M.subdivideLast_edge_castSucc_last c, ← M.subdivideLast_edge_last c]
    exact union_subset ((M.subdivideLast c).edge_subset_carrier _)
      ((M.subdivideLast c).edge_subset_carrier _)
  have hxy : segment ℝ (M.v (Fin.last M.n)) (M.v 0) ⊆
      convexHull ℝ {M.v (Fin.last M.n), M.v 0, c} :=
    segment_subset_convexHull (by simp) (by simp)
  have hMs : M.IsSimple := M.isSimple_of_isSimple_subdivideLast c hQ fun k hk z ⟨hzT, hzk⟩ => by
    have hzL : z ∈ L.carrier := L.comp_carrier_subset m (by
      rw [hm]
      exact (M.subdivideLast c).edge_subset_carrier k.castSucc (by
        rw [M.subdivideLast_edge_castSucc c hk]; exact hzk))
    rcases M.mem_new_edges c hQ hk hzk (hT ⟨hzT, hzL⟩) with h | h
    · rw [h]; exact Or.inl rfl
    · rw [h]; exact Or.inr rfl
  { k := L.k
    comp := Function.update L.comp m M
    simple := fun i => by
      by_cases hi : i = m
      · subst hi; rw [Function.update_self]; exact hMs
      · rw [Function.update_of_ne hi]; exact L.simple i
    disjoint := by
      have key : ∀ i, i ≠ m → Disjoint M.carrier (L.comp i).carrier := fun i hi => by
        refine Set.disjoint_left.mpr fun z hzM hzi => ?_
        have hdis := Set.disjoint_left.mp (L.disjoint (Ne.symm hi))
        rcases M.carrier_subset_subdivideLast_union c hzM with hz | hz
        · exact hdis (hm ▸ hz) hzi
        · exact hdis (hnew (hT ⟨hxy hz, L.comp_carrier_subset i hzi⟩)) hzi
      intro i j hij
      by_cases hi : i = m
      · subst hi
        simp only [Function.update_self, Function.update_of_ne (Ne.symm hij)]
        exact key j (Ne.symm hij)
      · by_cases hj : j = m
        · subst hj
          simp only [Function.update_self, Function.update_of_ne hi]
          exact (key i hi).symm
        · simp only [Function.update_of_ne hi, Function.update_of_ne hj]
          exact L.disjoint hij }

/-- **Deleting a vertex is the reverse of a move.** -/
theorem move_dropLast (hm : L.comp m = M.subdivideLast c)
    (hT : convexHull ℝ {M.v (Fin.last M.n), M.v 0, c} ∩ L.carrier ⊆
      segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0)) :
    Move (L.dropLast m M c hm hT) L := by
  have hQ : (M.subdivideLast c).IsSimple := hm ▸ L.simple m
  set L₁ := L.dropLast m M c hm hT
  have hL₁m : L₁.comp m = M := Function.update_self _ _ _
  have hL₁i : ∀ i, i ≠ m → L₁.comp i = L.comp i := fun i hi => Function.update_of_ne hi _ _
  refine Move.delta L₁ L (Equiv.refl _) m c (fun i hi => (hL₁i i hi).symm) (by rw [hL₁m]; exact hm)
    ?_
  rw [hL₁m]
  have hnew : segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0) ⊆ (L.comp m).carrier := by
    rw [hm, ← M.subdivideLast_edge_castSucc_last c, ← M.subdivideLast_edge_last c]
    exact union_subset ((M.subdivideLast c).edge_subset_carrier _)
      ((M.subdivideLast c).edge_subset_carrier _)
  apply Subset.antisymm
  · rintro z ⟨hzT, hzL₁⟩
    obtain ⟨i, hi⟩ := Set.mem_iUnion.mp hzL₁
    by_cases him : i = m
    · rw [him, hL₁m] at hi
      obtain ⟨k, hk⟩ := Set.mem_iUnion.mp hi
      by_cases hkl : k = Fin.last M.n
      · subst hkl; rwa [M.edge_last] at hk
      · have hzL : z ∈ L.carrier := L.comp_carrier_subset m (by
          rw [hm]
          exact (M.subdivideLast c).edge_subset_carrier k.castSucc (by
            rw [M.subdivideLast_edge_castSucc c hkl]; exact hk))
        rcases M.mem_new_edges c hQ hkl hk (hT ⟨hzT, hzL⟩) with rfl | rfl
        · exact left_mem_segment ℝ _ _
        · exact right_mem_segment ℝ _ _
    · rw [hL₁i i him] at hi
      exfalso
      exact Set.disjoint_left.mp (L.disjoint him)
        hi (hnew (hT ⟨hzT, L.comp_carrier_subset i hi⟩))
  · intro z hz
    refine ⟨segment_subset_convexHull (by simp) (by simp) hz, ?_⟩
    refine Set.mem_iUnion.mpr ⟨m, ?_⟩
    rw [hL₁m]
    exact M.edge_subset_carrier _ (by rw [M.edge_last]; exact hz)

/-- **Deleting a vertex is a Δ-equivalence.** -/
theorem deltaEquiv_dropLast (hm : L.comp m = M.subdivideLast c)
    (hT : convexHull ℝ {M.v (Fin.last M.n), M.v 0, c} ∩ L.carrier ⊆
      segment ℝ (M.v (Fin.last M.n)) c ∪ segment ℝ c (M.v 0)) :
    DeltaEquiv L (L.dropLast m M c hm hT) :=
  Relation.EqvGen.symm _ _ (Relation.EqvGen.rel _ _ (L.move_dropLast m M c hm hT))

end PolygonalLink

end QOU.MathlibExt.PL
