/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLMoveVertexNear

set_option autoImplicit false

/-!
# Moving the last vertex of a link component (issue #8902, isotopy-to-Δ bridge)

Glue between the list form of `PolygonalLink.reaches_moveLast` and the vertex-function form
`polyOf V` of `eventually_moveConds`.

## What is a THEOREM here

* `pathCarrier_ofFn` — the path through `f 0, …, f n` is the union of its `n` edges.
* `ofFn_split` — the vertex list of `polyOf V` is `b :: (s ++ [a, v])`.
* `PolygonalLink.reaches_polyOf_update` — if component `m` is `polyOf V` and the move
  conditions hold, the link reaches the component with its last vertex replaced by `w`.
* `PolygonalLink.reaches_moveAt` — the same for any vertex `k` (re-index, move, re-index back).
* `PolygonalLink.eventually_reaches_polyOf` — **moving every vertex of one component a little
  is a Δ-equivalence**: near a simple configuration whose rest is a continuous finite family of
  segments, the component at `x₀` reaches the component at `x`. The vertices are moved one at
  a time through the hybrid configurations `hybrid V x₀ k x`.
-/

namespace QOU.MathlibExt.PL

open Set Fin.CommRing Topology

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

lemma pathCarrier_ofFn {n : ℕ} (f : Fin (n + 1) → E) :
    pathCarrier (List.ofFn f) = ⋃ k : Fin n, segment ℝ (f k.castSucc) (f k.succ) := by
  ext z
  simp only [mem_pathCarrier, List.length_ofFn, List.getElem_ofFn, mem_iUnion]
  constructor
  · rintro ⟨i, hi, hz⟩
    exact ⟨⟨i, by omega⟩, hz⟩
  · rintro ⟨k, hz⟩
    exact ⟨k.val, by omega, hz⟩

variable {N : ℕ}

/-- The interior vertices `V 1, …, V N` of the path `b = V 0, …, a = V (N + 1)`. -/
def midList (V : Fin (N + 3) → E) : List E :=
  List.ofFn fun k : Fin N => V k.succ.castSucc.castSucc

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma ofFn_path (V : Fin (N + 3) → E) :
    List.ofFn (fun k : Fin (N + 2) => V k.castSucc) = V 0 :: (midList V ++ [V (iA N)]) := by
  rw [List.ofFn_succ_last, List.ofFn_succ]
  rfl

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma ofFn_split (V : Fin (N + 3) → E) :
    List.ofFn V = V 0 :: (midList V ++ [V (iA N), V (Fin.last (N + 2))]) := by
  rw [List.ofFn_succ_last, ofFn_path]
  simp

lemma pathCarrier_path (V : Fin (N + 3) → E) :
    pathCarrier (V 0 :: (midList V ++ [V (iA N)])) = coreSet V := by
  rw [← ofFn_path, pathCarrier_ofFn]
  rfl

lemma polyOf_eq_ofList (V : Fin (N + 3) → E) :
    polyOf V = Polygon.ofList (List.ofFn V) (by simp) :=
  (Polygon.ofList_ofFn (polyOf V)).symm


/-- Re-indexing a vertex function: `rotFn V c i = V (i + c)`. -/
def rotFn (V : Fin (N + 3) → E) (c : Fin (N + 3)) : Fin (N + 3) → E := fun i => V (i + c)

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma ofFn_rotFn (V : Fin (N + 3) → E) (c : Fin (N + 3)) :
    List.ofFn (rotFn V c) = (List.ofFn V).rotate c.val := by
  apply List.ext_getElem (by simp)
  intro i h1 h2
  simp only [List.getElem_ofFn, List.getElem_rotate, List.length_ofFn, rotFn]
  congr 1

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma rotFn_rotFn_neg (V : Fin (N + 3) → E) (c : Fin (N + 3)) : rotFn (rotFn V c) (-c) = V := by
  funext i; simp [rotFn]

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma last_eq_neg_one' : (Fin.last (N + 2) : Fin (N + 3)) = -1 :=
  eq_neg_of_add_eq_zero_left (Fin.last_add_one _)

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma update_rotFn (V : Fin (N + 3) → E) (k : Fin (N + 3)) (w : E) :
    Function.update (rotFn V (k + 1)) (Fin.last (N + 2)) w =
      rotFn (Function.update V k w) (k + 1) := by
  funext i
  simp only [rotFn]
  by_cases hi : i = Fin.last (N + 2)
  · subst hi
    have : Fin.last (N + 2) + (k + 1) = k := by rw [last_eq_neg_one']; abel
    rw [Function.update_self, this, Function.update_self]
  · have : i + (k + 1) ≠ k := fun h => hi (by
      rw [last_eq_neg_one']; linear_combination (exp := 1) h)
    rw [Function.update_of_ne hi, Function.update_of_ne this]
    rfl

lemma polyOf_rotFn (V : Fin (N + 3) → E) (c : Fin (N + 3)) :
    polyOf (rotFn V c) = (polyOf V).rotateBy c.val := by
  rw [polyOf_eq_ofList, polyOf_eq_ofList, Polygon.ofList_rotateBy]
  exact Polygon.ofList_congr _ (ofFn_rotFn V c)

lemma isSimple_polyOf_rotFn {V : Fin (N + 3) → E} (h : (polyOf V).IsSimple) (c : Fin (N + 3)) :
    (polyOf (rotFn V c)).IsSimple := by
  rw [polyOf_rotFn]; exact (polyOf V).isSimple_rotateBy h _

lemma carrier_polyOf_rotFn (V : Fin (N + 3) → E) (c : Fin (N + 3)) :
    (polyOf (rotFn V c)).carrier = (polyOf V).carrier := by
  rw [polyOf_rotFn, Polygon.carrier_rotateBy]

namespace PolygonalLink

/-- **Moving the last vertex of a component, vertex-function form.** -/
theorem reaches_polyOf_update (L : PolygonalLink E) (m : Fin L.k) (V : Fin (N + 3) → E)
    (hm : L.comp m = polyOf V) {w p q : E}
    (hc : MoveConds (coreSet V ∪ L.rest m) (V (iA N)) (V 0) (V (Fin.last (N + 2))) w p q) :
    L.Reaches m (polyOf (Function.update V (Fin.last (N + 2)) w)) := by
  have hm' : L.comp m = Polygon.ofList (V 0 :: (midList V ++ [V (iA N), V (Fin.last (N + 2))]))
      (by simp) := by
    rw [hm, polyOf_eq_ofList]; exact Polygon.ofList_congr _ (ofFn_split V)
  have hcore := pathCarrier_path V
  have r := reaches_moveLast L m (V 0) (V (iA N)) (V (Fin.last (N + 2))) w p q (midList V)
    (by simp) hm' hc.hp hc.hq (by rw [hcore]; exact hc.hcut) hc.hwq hc.hwp hc.hwseg
    (by rw [hcore]; exact hc.hins) (by rw [hcore]; exact hc.hdq) (by rw [hcore]; exact hc.hdp)
  set V' := Function.update V (Fin.last (N + 2)) w
  have e : V 0 :: (midList V ++ [V (iA N), w]) = List.ofFn V' := by
    rw [ofFn_split]
    have h0 : V' 0 = V 0 := Function.update_of_ne (by simp [Fin.ext_iff]) _ _
    have hA : V' (iA N) = V (iA N) := Function.update_of_ne iA_ne_last _ _
    have hL : V' (Fin.last (N + 2)) = w := Function.update_self _ _ _
    have hmid : midList V' = midList V := by
      simp only [midList]
      congr 1; funext k
      exact Function.update_of_ne (by simp [Fin.ext_iff]; omega) _ _
    rw [h0, hA, hL, hmid]
  rw [polyOf_eq_ofList]
  exact r.congr e

/-- Re-indexing a component, vertex-function form. -/
theorem reaches_rotFn (L : PolygonalLink E) (m : Fin L.k) (V : Fin (N + 3) → E)
    (hm : L.comp m = polyOf V) (c : Fin (N + 3)) : L.Reaches m (polyOf (rotFn V c)) := by
  have hm' : L.comp m = Polygon.ofList (List.ofFn V) (by simp) := by rw [hm, polyOf_eq_ofList]
  rw [polyOf_eq_ofList]
  exact (reaches_rotate L m _ _ hm' c.val).congr (ofFn_rotFn V c).symm

/-- **Moving vertex `k` of a component.** Re-index so that `k` is last, move it, re-index back.
The conditions are those of `reaches_polyOf_update` for the re-indexed vertex function. -/
theorem reaches_moveAt (L : PolygonalLink E) (m : Fin L.k) (V : Fin (N + 3) → E)
    (hm : L.comp m = polyOf V) (k : Fin (N + 3)) {w p q : E}
    (hc : MoveConds (coreSet (rotFn V (k + 1)) ∪ L.rest m) (rotFn V (k + 1) (iA N))
      (rotFn V (k + 1) 0) (rotFn V (k + 1) (Fin.last (N + 2))) w p q) :
    L.Reaches m (polyOf (Function.update V k w)) := by
  refine (reaches_rotFn L m V hm (k + 1)).trans' fun L1 m1 h1 r1 => ?_
  refine (reaches_polyOf_update L1 m1 _ h1 (r1 ▸ hc)).trans' fun L2 m2 h2 _ => ?_
  rw [update_rotFn] at h2
  have := reaches_rotFn L2 m2 _ h2 (-(k + 1))
  rwa [rotFn_rotFn_neg] at this

lemma Reaches.refl (L : PolygonalLink E) (m : Fin L.k) : L.Reaches m (L.comp m) :=
  ⟨L, Relation.EqvGen.refl _, rfl, fun i => by simp⟩

section Hybrid

variable {X : Type*} [TopologicalSpace X] {x₀ : X}

/-- The configuration with vertices `i < k` at `x` and the others still at `x₀`. -/
def hybrid (V : X → Fin (N + 3) → E) (x₀ : X) (k : ℕ) (x : X) : Fin (N + 3) → E :=
  fun i => if i.val < k then V x i else V x₀ i

omit [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace X] in
lemma hybrid_zero (V : X → Fin (N + 3) → E) (x : X) : hybrid V x₀ 0 x = V x₀ := by
  funext i; simp [hybrid]

omit [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace X] in
lemma hybrid_full (V : X → Fin (N + 3) → E) (x : X) : hybrid V x₀ (N + 3) x = V x := by
  funext i; simp [hybrid, i.isLt]

omit [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace X] in
lemma hybrid_base (V : X → Fin (N + 3) → E) (k : ℕ) : hybrid V x₀ k x₀ = V x₀ := by
  funext i; simp [hybrid]

omit [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace X] in
lemma hybrid_succ (V : X → Fin (N + 3) → E) (x : X) (k : Fin (N + 3)) :
    hybrid V x₀ (k.val + 1) x = Function.update (hybrid V x₀ k.val x) k (V x k) := by
  funext i
  by_cases hi : i = k
  · subst hi; simp [hybrid]
  · rw [Function.update_of_ne hi]
    have : i.val ≠ k.val := fun h => hi (Fin.ext h)
    simp only [hybrid]
    congr 1
    exact propext ⟨fun h => by omega, fun h => by omega⟩

omit [NormedSpace ℝ E] in
lemma continuous_hybrid {V : X → Fin (N + 3) → E} (hV : Continuous V) (k : ℕ) :
    Continuous (hybrid V x₀ k) := by
  refine continuous_pi fun i => ?_
  simp only [hybrid]
  split_ifs
  · exact (continuous_apply i).comp hV
  · exact continuous_const

/-- **Moving all vertices of one component a little is a Δ-equivalence.** Let the vertices
`V x` of a component depend continuously on `x`, simple at `x₀`, and let the rest of the link
be the union of segments `[s j x, t j x]`, continuous in `x` and clear of the component at
`x₀`. For `x` near `x₀`, any link whose component `m` is `polyOf (V x₀)` and whose rest is
`⋃ j, [s j x, t j x]` reaches the component `polyOf (V x)`. -/
theorem eventually_reaches_polyOf {V : X → Fin (N + 3) → E} (hV : Continuous V)
    (hP : (polyOf (V x₀)).IsSimple)
    {J : Type*} [Finite J] {s t : J → X → E} (hs : ∀ j, Continuous (s j))
    (ht : ∀ j, Continuous (t j))
    (hR : ∀ j, Disjoint (segment ℝ (s j x₀) (t j x₀)) (polyOf (V x₀)).carrier) :
    ∀ᶠ x in 𝓝 x₀, ∀ (L : PolygonalLink E) (m : Fin L.k), L.comp m = polyOf (V x₀) →
      L.rest m = (⋃ j, segment ℝ (s j x) (t j x)) → L.Reaches m (polyOf (V x)) := by
  -- one application of `eventually_moveConds` per vertex
  have step : ∀ k : Fin (N + 3), ∃ r : ℝ, ∀ᶠ x in 𝓝 x₀,
      MoveConds (coreSet (rotFn (hybrid V x₀ k.val x) (k + 1)) ∪ ⋃ j, segment ℝ (s j x) (t j x))
        (rotFn (hybrid V x₀ k.val x) (k + 1) (iA N)) (rotFn (hybrid V x₀ k.val x) (k + 1) 0)
        (rotFn (hybrid V x₀ k.val x) (k + 1) (Fin.last (N + 2))) (V x k)
        (ratioPt r (rotFn (hybrid V x₀ k.val x) (k + 1) (Fin.last (N + 2)))
          (rotFn (hybrid V x₀ k.val x) (k + 1) 0))
        (ratioPt r (rotFn (hybrid V x₀ k.val x) (k + 1) (Fin.last (N + 2)))
          (rotFn (hybrid V x₀ k.val x) (k + 1) (iA N))) := by
    intro k
    have hG : Continuous fun x => rotFn (hybrid V x₀ k.val x) (k + 1) :=
      continuous_pi fun i => (continuous_apply _).comp (continuous_hybrid hV k.val)
    have hG0 : rotFn (hybrid V x₀ k.val x₀) (k + 1) = rotFn (V x₀) (k + 1) := by
      rw [hybrid_base]
    obtain ⟨r, -, -, hr⟩ := eventually_moveConds (x₀ := x₀) hG
      (by rw [hG0]; exact isSimple_polyOf_rotFn hP _)
      ((continuous_apply k).comp hV)
      (by
        rw [hG0]; show V x₀ k = V x₀ (Fin.last (N + 2) + (k + 1))
        rw [last_eq_neg_one']; congr 1; abel)
      hs ht (by rw [hG0, carrier_polyOf_rotFn]; exact hR)
    exact ⟨r, hr⟩
  choose r hr using step
  filter_upwards [Filter.eventually_all.mpr hr] with x hx
  -- induction over the number of vertices already moved
  have key : ∀ k, k ≤ N + 3 → ∀ (L : PolygonalLink E) (m : Fin L.k),
      L.comp m = polyOf (V x₀) → L.rest m = (⋃ j, segment ℝ (s j x) (t j x)) →
      L.Reaches m (polyOf (hybrid V x₀ k x)) := by
    intro k
    induction k with
    | zero =>
      intro _ L m hm _
      rw [hybrid_zero, ← hm]; exact Reaches.refl L m
    | succ k ih =>
      intro hk L m hm hrest
      refine (ih (by omega) L m hm hrest).trans' fun L1 m1 h1 r1 => ?_
      have e := hybrid_succ V (x₀ := x₀) x ⟨k, by omega⟩
      simp only at e
      rw [e]
      exact reaches_moveAt L1 m1 _ h1 ⟨k, by omega⟩ (by rw [r1, hrest]; exact hx ⟨k, by omega⟩)
  intro L m hm hrest
  have := key (N + 3) le_rfl L m hm hrest
  rwa [hybrid_full] at this

end Hybrid

end PolygonalLink

end QOU.MathlibExt.PL
