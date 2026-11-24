/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLVertexSlide

set_option autoImplicit false

/-!
# Polygons from vertex lists (issue #8902, isotopy-to-Δ bridge, bookkeeping)

Local stability chains several insertions, deletions and re-indexings of one component. Written
with `Fin` indices the intermediate polygons are hard to compare; written as vertex **lists** they
are `l ++ [c]` and `l.rotate r`, and two constructions agree when two lists do.

## What is a DEFINITION here

* `Polygon.ofList l h` — the polygon with vertex list `l` (`3 ≤ l.length`).
* `pathCarrier l` — the union of the segments between consecutive entries of `l`.

## What is a THEOREM here

* `Polygon.ext'` — polygons agree when their sizes and vertices do.
* `Polygon.ofList_ofFn` — every polygon is `ofList` of its vertex list.
* `Polygon.ofList_subdivideLast`, `Polygon.ofList_rotateBy` — insertion is `++ [c]`, re-indexing
  is `List.rotate`.
* `Polygon.carrier_ofList` — the point set is `pathCarrier l ∪ [last, first]`.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- The union of the segments between consecutive entries of a list. -/
def pathCarrier : List E → Set E
  | [] => ∅
  | [_] => ∅
  | x :: y :: t => segment ℝ x y ∪ pathCarrier (y :: t)

@[simp] lemma pathCarrier_nil : pathCarrier ([] : List E) = ∅ := rfl
@[simp] lemma pathCarrier_single (x : E) : pathCarrier [x] = ∅ := rfl
@[simp] lemma pathCarrier_cons_cons (x y : E) (t : List E) :
    pathCarrier (x :: y :: t) = segment ℝ x y ∪ pathCarrier (y :: t) := rfl

lemma mem_pathCarrier {l : List E} {z : E} :
    z ∈ pathCarrier l ↔ ∃ (i : ℕ) (h : i + 1 < l.length), z ∈ segment ℝ (l[i]'(by omega)) l[i + 1] := by
  induction l with
  | nil => simp
  | cons x t ih =>
    cases t with
    | nil => simp
    | cons y t =>
      simp only [pathCarrier_cons_cons, mem_union, ih, List.length_cons]
      constructor
      · rintro (hz | ⟨i, hi, hz⟩)
        · exact ⟨0, by omega, by simpa using hz⟩
        · exact ⟨i + 1, by simp at hi ⊢; omega, by simpa using hz⟩
      · rintro ⟨i, hi, hz⟩
        cases i with
        | zero => exact Or.inl (by simpa using hz)
        | succ i => exact Or.inr ⟨i, by simp at hi ⊢; omega, by simpa using hz⟩

namespace Polygon

/-- **Extensionality** with a size equation. -/
theorem ext' {P Q : Polygon E} (hn : P.n = Q.n)
    (hv : ∀ i : Fin (P.n + 1), P.v i = Q.v (Fin.cast (by rw [hn]) i)) : P = Q := by
  cases P with
  | mk n h v =>
    cases Q with
    | mk n' h' v' =>
      simp only at hn
      subst hn
      simp only [Polygon.mk.injEq, heq_eq_eq, true_and]
      funext i
      exact hv i

/-- The polygon with vertex list `l`. -/
def ofList (l : List E) (h : 3 ≤ l.length) : Polygon E where
  n := l.length - 1
  two_le := by omega
  v i := l[i.val]'(by have := i.isLt; omega)

lemma ofList_v (l : List E) (h : 3 ≤ l.length) (i : Fin ((ofList l h).n + 1)) :
    (ofList l h).v i = l[i.val]'(by have := i.isLt; simp only [ofList] at this; omega) := rfl

lemma ofList_n (l : List E) (h : 3 ≤ l.length) : (ofList l h).n = l.length - 1 := rfl

lemma ofList_congr {l l' : List E} (h : 3 ≤ l.length) (e : l = l') :
    ofList l h = ofList l' (e ▸ h) := by subst e; rfl

/-- **Every polygon is the polygon of its vertex list.** -/
theorem ofList_ofFn (P : Polygon E) :
    ofList (List.ofFn P.v) (by simp only [List.length_ofFn]; have := P.two_le; omega) = P := by
  refine ext' (by simp [ofList]) fun i => ?_
  simp only [ofList_v, List.getElem_ofFn]
  rfl

/-- **Inserting a vertex on the closing edge appends it to the list.** -/
theorem ofList_subdivideLast (l : List E) (h : 3 ≤ l.length) (c : E) :
    (ofList l h).subdivideLast c = ofList (l ++ [c]) (by simp; omega) := by
  refine ext' (by simp [subdivideLast, ofList]; omega) fun i => ?_
  simp only [subdivideLast, ofList_v, Fin.snoc, Fin.coe_cast]
  split_ifs with hi
  · simp only [cast_eq]
    rw [List.getElem_append_left (by simp only [ofList] at hi; omega)]
    rfl
  · simp only [cast_eq]
    have : i.val = l.length := by
      have := i.isLt; simp only [subdivideLast, ofList] at this hi; omega
    simp only [this, List.getElem_append_right (le_refl _), Nat.sub_self,
      List.getElem_cons_zero]

/-- **Re-indexing rotates the list.** -/
theorem ofList_rotateBy (l : List E) (h : 3 ≤ l.length) (r : ℕ) :
    (ofList l h).rotateBy r = ofList (l.rotate r) (by simp; exact h) := by
  rw [rotateBy_eq_rot]
  refine ext' (by simp [rot, ofList]) fun i => ?_
  simp only [rot_v, ofList_v, sh, Fin.coe_cast, List.getElem_rotate]
  congr 1
  simp only [ofList]
  congr 1
  omega

/-- **The point set of a list polygon**: consecutive segments and the closing segment. -/
theorem carrier_ofList (l : List E) (h : 3 ≤ l.length) :
    (ofList l h).carrier =
      pathCarrier l ∪ segment ℝ (l[l.length - 1]'(by omega)) (l[0]'(by omega)) := by
  ext z
  simp only [carrier, mem_iUnion, mem_union, mem_pathCarrier, edge, ofList_v]
  have hnext : ∀ i : Fin ((ofList l h).n + 1), ((ofList l h).next i).val =
      if i.val = l.length - 1 then 0 else i.val + 1 := by
    intro i
    simp only [next, coe_finRotate, Fin.ext_iff, Fin.val_last, ofList]
  constructor
  · rintro ⟨i, hz⟩
    by_cases hi : i.val = l.length - 1
    · right
      have e1 : ((ofList l h).next i).val = 0 := by rw [hnext, if_pos hi]
      convert hz using 2
      · simp only [hi]
      · simp only [e1]
    · left
      have e1 : ((ofList l h).next i).val = i.val + 1 := by rw [hnext, if_neg hi]
      have := i.isLt; simp only [ofList] at this
      exact ⟨i.val, by omega, by convert hz using 2; simp only [e1]⟩
  · rintro (⟨i, hi, hz⟩ | hz)
    · have hi' : i < (ofList l h).n + 1 := by simp only [ofList]; omega
      refine ⟨⟨i, hi'⟩, ?_⟩
      have e1 : ((ofList l h).next ⟨i, hi'⟩).val = i + 1 := by
        rw [hnext, if_neg (by simp; omega)]
      convert hz using 2; simp only [e1]
    · have hi' : l.length - 1 < (ofList l h).n + 1 := by simp only [ofList]; omega
      refine ⟨⟨l.length - 1, hi'⟩, ?_⟩
      have e1 : ((ofList l h).next ⟨l.length - 1, hi'⟩).val = 0 := by
        rw [hnext, if_pos rfl]
      convert hz using 2; simp only [e1]

end Polygon

end QOU.MathlibExt.PL
