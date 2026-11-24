/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLMoveVertex

set_option autoImplicit false

/-!
# Subdividing a component is a Δ-equivalence (issue #8902, isotopy-to-Δ bridge)

A vertex list `l'` *refines* `l` when it is obtained from `l` by re-indexing and by inserting
points of the open closing edge. A refinement of a component's vertex list is reached by a
chain of Δ-moves. The main instance: inserting, on every edge `[v_k, v_{k+1}]`, a chain of points
ordered from `v_k` to `v_{k+1}`.

## What is a DEFINITION here

* `Refines l l'` — inductive: reflexive, closed under rotation and closing-edge insertion.
* `OrderedOn x y cs` — `cs = [c₁, …, c_m]` with `c₁ ∈ (x, y)`, `c₂ ∈ (c₁, y)`, ….
* `sampleList ps` — `v₀ :: I₀ ++ v₁ :: I₁ ++ …` for `ps = [(v₀, I₀), (v₁, I₁), …]`.

## What is a THEOREM here

* `PolygonalLink.Reaches.of_refines` — a refinement of the component is reached.
* `refines_sampleList` — inserting an ordered chain on every edge is a refinement.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- `l'` refines `l`: re-indexings and insertions on the open closing edge. -/
inductive Refines : List E → List E → Prop
  | refl (l : List E) : Refines l l
  | rotate {l l' : List E} (r : ℕ) : Refines l l' → Refines l (l'.rotate r)
  | insert {l l' : List E} (hne : l' ≠ []) (c : E)
      (hc : c ∈ openSegment ℝ (l'.getLast hne) (l'.head hne)) : Refines l l' → Refines l (l' ++ [c])

lemma Refines.length_le {l l' : List E} (h : Refines l l') : l.length ≤ l'.length := by
  induction h with
  | refl => exact le_rfl
  | rotate r _ ih => simpa using ih
  | insert _ _ _ _ ih => simp; omega

lemma Refines.trans {l l' l'' : List E} (h1 : Refines l l') (h2 : Refines l' l'') :
    Refines l l'' := by
  induction h2 with
  | refl => exact h1
  | rotate r _ ih => exact ih.rotate r
  | insert hne c hc _ ih => exact ih.insert hne c hc

/-- `cs` is an ordered chain of points from `x` towards `y`. -/
def OrderedOn (x y : E) : List E → Prop
  | [] => True
  | c :: cs => c ∈ openSegment ℝ x y ∧ OrderedOn c y cs

lemma Refines.append_ordered {l m : List E} (hne : m ≠ []) :
    ∀ cs : List E, OrderedOn (m.getLast hne) (m.head hne) cs → Refines l m → Refines l (m ++ cs)
  | [], _, h => by rw [List.append_nil]; exact h
  | c :: cs, ⟨hc, hcs⟩, h => by
    have h1 := h.insert hne c hc
    have hne' : m ++ [c] ≠ [] := by simp
    have := Refines.append_ordered (m := m ++ [c]) hne' cs
      (by simpa [List.getLast_append, List.head_append_of_ne_nil hne] using hcs) h1
    simpa using this

/-- `v₀ :: I₀ ++ v₁ :: I₁ ++ …`. -/
def sampleList (ps : List (E × List E)) : List E := ps.flatMap fun p => p.1 :: p.2

omit [AddCommGroup E] [Module ℝ E] in
lemma sampleList_take_succ (ps : List (E × List E)) (k : ℕ) (hk : k < ps.length) :
    sampleList (ps.take (k + 1)) = sampleList (ps.take k) ++ (ps[k].1 :: ps[k].2) := by
  rw [List.take_succ, List.getElem?_eq_getElem hk]
  simp only [sampleList, Option.toList_some, List.flatMap_append, List.flatMap_cons,
    List.flatMap_nil, List.append_nil]

omit [AddCommGroup E] [Module ℝ E] in
lemma head_sampleList_take_append (ps : List (E × List E)) (k : ℕ) (hk : k < ps.length) :
    (sampleList (ps.take k) ++ [ps[k].1]).head (by simp) = (ps[0]'(by omega)).1 := by
  cases ps with
  | nil => simp at hk
  | cons p0 rest =>
    cases k with
    | zero => simp [sampleList]
    | succ k => simp [sampleList, List.take_succ_cons]

/-- **Inserting an ordered chain on every edge is a refinement.** For `ps = [(v₀, I₀), …]`,
with `I_k` ordered from `v_k` to `v_{k+1}` (indices mod the length), `sampleList ps` refines
`[v₀, v₁, …]`. -/
theorem refines_sampleList (ps : List (E × List E))
    (hord : ∀ k (hk : k < ps.length),
      OrderedOn ps[k].1 (ps[(k + 1) % ps.length]'(Nat.mod_lt _ (by omega))).1 ps[k].2) :
    Refines (ps.map Prod.fst) (sampleList ps) := by
  have key : ∀ k, k ≤ ps.length →
      Refines (ps.map Prod.fst) ((ps.drop k).map Prod.fst ++ sampleList (ps.take k)) := by
    intro k
    induction k with
    | zero => intro _; simpa [sampleList] using Refines.refl _
    | succ k ih =>
      intro hk
      have hk' : k < ps.length := by omega
      have h0 := ih (by omega)
      rw [List.drop_eq_getElem_cons hk', List.map_cons, List.cons_append] at h0
      have h1 := h0.rotate 1
      rw [List.rotate_cons_succ, List.rotate_zero] at h1
      set m := (ps.drop (k + 1)).map Prod.fst ++ sampleList (ps.take k) ++ [ps[k].1] with hmdef
      have hne : m ≠ [] := by simp [m]
      have hlast : m.getLast hne = ps[k].1 := by simp [m]
      have hhead : m.head hne = (ps[(k + 1) % ps.length]'(Nat.mod_lt _ (by omega))).1 := by
        by_cases hlt : k + 1 < ps.length
        · simp only [Nat.mod_eq_of_lt hlt]
          have e : m = ps[k + 1].1 :: ((ps.drop (k + 2)).map Prod.fst ++
              sampleList (ps.take k) ++ [ps[k].1]) := by
            simp only [m]; rw [List.drop_eq_getElem_cons hlt]; rfl
          generalize hne = hne' at *
          revert hne'; rw [e]; intros; rfl
        · have he : k + 1 = ps.length := by omega
          have hd : ps.drop (k + 1) = [] := List.drop_eq_nil_of_le (by omega)
          simp only [he, Nat.mod_self]
          simp only [m, hd, List.map_nil, List.nil_append]
          exact head_sampleList_take_append ps k hk'
      have h2 := Refines.append_ordered hne ps[k].2 (by rw [hlast, hhead]; exact hord k hk') h1
      rw [sampleList_take_succ ps k hk']
      simpa [m] using h2
  simpa using key ps.length le_rfl

namespace PolygonalLink

variable (L : PolygonalLink E) (m : Fin L.k)

/-- Closing-edge insertion for an arbitrary vertex list. -/
theorem reaches_insert' (l : List E) (h : 3 ≤ l.length) (hm : L.comp m = Polygon.ofList l h)
    (hne : l ≠ []) (c : E) (hc : c ∈ openSegment ℝ (l.getLast hne) (l.head hne)) :
    L.Reaches m (Polygon.ofList (l ++ [c]) (by simp; omega)) := by
  obtain ⟨x, l', rfl⟩ : ∃ x l', l = x :: l' := ⟨l.head hne, l.tail, (List.cons_head_tail hne).symm⟩
  have hl' : l' ≠ [] := by rintro rfl; simp at h
  have e : x :: l' = x :: (l'.dropLast ++ [l'.getLast hl']) := by
    rw [List.dropLast_append_getLast]
  have hm' := hm.trans (Polygon.ofList_congr h e)
  have hc' : c ∈ openSegment ℝ (l'.getLast hl') x := by
    simpa [List.getLast_cons hl'] using hc
  have := reaches_insert L m x (l'.getLast hl') c l'.dropLast (by simpa [← e] using h) hm' hc'
  refine this.congr ?_
  conv_rhs => rw [e]
  simp

/-- **A refinement of a component is reached by Δ-moves.** -/
theorem Reaches.of_refines {l l' : List E} (hr : Refines l l') (h : 3 ≤ l.length)
    (hm : L.comp m = Polygon.ofList l h) :
    L.Reaches m (Polygon.ofList l' (h.trans hr.length_le)) := by
  induction hr with
  | refl => rw [← hm]; exact Reaches.refl L m
  | rotate r hr ih =>
    refine ih.trans' fun L1 m1 h1 _ => ?_
    exact reaches_rotate L1 m1 _ _ h1 r
  | insert hne c hc hr ih =>
    refine ih.trans' fun L1 m1 h1 _ => ?_
    exact reaches_insert' L1 m1 _ _ h1 hne c hc

end PolygonalLink

end QOU.MathlibExt.PL
