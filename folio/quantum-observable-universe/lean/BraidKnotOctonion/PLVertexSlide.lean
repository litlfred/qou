/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLPolygonalLink

set_option autoImplicit false

/-!
# Vertex slides are Δ-equivalences (issue #8902, stage 2, part 2)

A **vertex slide** moves one vertex `b` of a polygonal link to a new position `c`, keeping all
other vertices. If `a` and `d` are the neighbours of `b` (`a` before, `d` after), the slide
replaces the two edges `[a, b] ∪ [b, d]` by `[a, c] ∪ [c, d]`. This file proves that a slide is a
Δ-equivalence when the two triangles it sweeps out are clear of the link:

* `T₁ = convexHull {b, d, c}` meets the link only in the edge `[b, d]`;
* `T₂ = convexHull {a, c, b}` meets the slid link only in its edge `[a, c]`;
* `c ∉ {b, d}` and `[b, c] ∩ [c, d] ⊆ {c}`.

The proof is two Δ-moves and two re-indexings: insert `c` on `[b, d]`, then delete `b` from
`a, b, c`.

Every ambient PL isotopy of a link can be cut into small steps that move one vertex at a time;
this lemma is the combinatorial step those pieces reduce to (Reidemeister's reduction; see
Lickorish 1997, Ch. 1 \[lickorish1997\]). That reduction itself is **not** proved here.

## What is a DEFINITION here

* `Polygon.rot P r` — the polygon re-indexed to start at vertex `r`, with explicit index
  arithmetic `i ↦ i + r`.
* `Polygon.setLast P c` — the polygon with its last vertex replaced by `c`.
* `PolygonalLink.replaceComp` — the link with one component replaced by a simple polygon
  having the same point set.

## What is a THEOREM here

* `Polygon.rotateBy_eq_rot` — `rotateBy` and `rot` agree.
* `PolygonalLink.move_replaceComp_rotateBy` — re-indexing one component is a `Move`.
* `PolygonalLink.deltaEquiv_setLast` — **the vertex slide lemma** (the last vertex of a
  component; any vertex reduces to this by re-indexing, which is a `Move`).

## What is NOT proved here

* That an ambient PL isotopy decomposes into vertex slides, or the converse comparison of
  Δ-equivalence with ambient PL isotopy. These remain open steps of stage 2.
-/

namespace QOU.MathlibExt.PL

open Set

set_option backward.isDefEq.respectTransparency false

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- `(i + m) % (m + 1)` is `i - 1`, cyclically. -/
private lemma add_mod_succ_self {m i : ℕ} (hi : i < m + 1) :
    (i + m) % (m + 1) = if i = 0 then m else i - 1 := by
  rcases i with _ | i
  · simp [Nat.mod_eq_of_lt (Nat.lt_succ_self m)]
  · simp only [Nat.add_eq_zero_iff, one_ne_zero, and_false, if_false, Nat.add_sub_cancel]
    rw [show i + 1 + m = i + (m + 1) by omega, Nat.add_mod_right, Nat.mod_eq_of_lt (by omega)]

/-- The index `i + r`, cyclically. -/
def sh (n r : ℕ) (i : Fin (n + 1)) : Fin (n + 1) :=
  ⟨(i.val + r) % (n + 1), Nat.mod_lt _ (Nat.succ_pos _)⟩

lemma sh_self_val {n : ℕ} (i : Fin (n + 1)) :
    (sh n n i).val = if i.val = 0 then n else i.val - 1 :=
  add_mod_succ_self i.isLt

namespace Polygon

variable (P : Polygon E)


/-- Re-index to start at vertex `r`: `(P.rot r).v i = P.v (i + r)`. -/
def rot (r : ℕ) : Polygon E where
  n := P.n
  two_le := P.two_le
  v i := P.v (sh P.n r i)

lemma rot_v (r : ℕ) (i : Fin (P.n + 1)) : (P.rot r).v i = P.v (sh P.n r i) := rfl

theorem rotate_rot (r : ℕ) : (P.rot r).rotate = P.rot (r + 1) := by
  simp only [rotate, rot, Polygon.mk.injEq, heq_eq_eq, true_and]
  funext i
  simp only [Function.comp_apply]
  congr 1
  apply Fin.ext
  simp only [sh, finRotate_apply, Fin.val_add]
  have h1 : (1 : Fin (P.n + 1)).val = 1 := by
    have := P.two_le
    simp [Nat.mod_eq_of_lt (show 1 < P.n + 1 by omega)]
  rw [h1, Nat.mod_add_mod]
  congr 1
  omega

theorem rotateBy_eq_rot (r : ℕ) : P.rotateBy r = P.rot r := by
  induction r with
  | zero =>
    cases P with
    | mk n h v =>
      simp only [rotateBy, rot, sh, Polygon.mk.injEq, heq_eq_eq, true_and, add_zero]
      funext i
      congr 1
      exact Fin.ext (Nat.mod_eq_of_lt i.isLt).symm
  | succ r ih => rw [rotateBy, ih, rotate_rot]

/-- Replace the last vertex by `c`. -/
def setLast (c : E) : Polygon E where
  n := P.n
  two_le := P.two_le
  v := Function.update P.v (Fin.last P.n) c

/-- The vertex before the last one. -/
def penult : Fin (P.n + 1) := ⟨P.n - 1, by omega⟩

lemma setLast_rot_v_zero (c : E) : ((P.setLast c).rot P.n).v 0 = c := by
  have h : sh P.n P.n 0 = Fin.last P.n := Fin.ext (by simp [sh_self_val])
  show Function.update P.v (Fin.last P.n) c (sh P.n P.n 0) = c
  rw [h]
  exact Function.update_self _ _ _

lemma setLast_rot_v_last (c : E) :
    ((P.setLast c).rot P.n).v (Fin.last _) = P.v P.penult := by
  have := P.two_le
  have h : sh P.n P.n (Fin.last _) = P.penult :=
    Fin.ext (by simp [sh_self_val, penult]; omega)
  show Function.update P.v (Fin.last P.n) c (sh P.n P.n (Fin.last P.n)) = _
  rw [h]
  rw [Function.update_of_ne]
  intro hp
  have := congrArg Fin.val hp
  simp [penult] at this
  omega

/-- **The index identity behind the slide**: inserting `c` after the last vertex and
re-indexing to start at `c` is the same as replacing the last vertex by `c`, re-indexing to
start at `c`, and then inserting the old last vertex after the new last vertex. -/
theorem subdivideLast_rot_eq (c : E) :
    (P.subdivideLast c).rot (P.n + 1) =
      ((P.setLast c).rot P.n).subdivideLast (P.v (Fin.last _)) := by
  simp only [subdivideLast, rot, setLast, Polygon.mk.injEq, heq_eq_eq, true_and]
  funext i
  have hsh : ∀ i : Fin (P.n + 1 + 1), (sh (P.n + 1) (P.n + 1) i).val =
      if i.val = 0 then P.n + 1 else i.val - 1 := fun i => sh_self_val i
  refine Fin.lastCases ?_ (fun j => ?_) i
  · rw [Fin.snoc_last]
    have h : sh (P.n + 1) (P.n + 1) (Fin.last (P.n + 1)) = Fin.castSucc (Fin.last P.n) :=
      Fin.ext (by rw [hsh]; simp)
    rw [h]
    exact Fin.snoc_castSucc (α := fun _ => E) _ _ _
  · rw [Fin.snoc_castSucc (α := fun _ => E)]
    by_cases hj : j.val = 0
    · have h : sh (P.n + 1) (P.n + 1) (Fin.castSucc j) = Fin.last (P.n + 1) :=
        Fin.ext (by rw [hsh]; simp [hj])
      have h' : sh P.n P.n j = Fin.last P.n :=
        Fin.ext (by simp [sh_self_val, hj])
      rw [h, Fin.snoc_last (α := fun _ => E)]
      show c = Function.update P.v (Fin.last P.n) c (sh P.n P.n j)
      rw [h', Function.update_self]
    · have h : sh (P.n + 1) (P.n + 1) (Fin.castSucc j) =
          Fin.castSucc ⟨j.val - 1, by omega⟩ :=
        Fin.ext (by rw [hsh]; simp [hj])
      have h' : sh P.n P.n j = ⟨j.val - 1, by omega⟩ :=
        Fin.ext (by simp [sh_self_val, hj])
      rw [h, Fin.snoc_castSucc (α := fun _ => E)]
      show P.v _ = Function.update P.v (Fin.last P.n) c (sh P.n P.n j)
      rw [h', Function.update_of_ne]
      intro hl
      have := congrArg Fin.val hl
      simp at this
      omega

end Polygon

namespace PolygonalLink

variable (L : PolygonalLink E)

/-- Replace component `m` by a simple polygon with the same point set. -/
def replaceComp (m : Fin L.k) (P : Polygon E) (hs : P.IsSimple)
    (hc : P.carrier = (L.comp m).carrier) : PolygonalLink E where
  k := L.k
  comp := Function.update L.comp m P
  simple i := by
    by_cases hi : i = m
    · subst hi; rw [Function.update_self]; exact hs
    · rw [Function.update_of_ne hi]; exact L.simple i
  disjoint i j hij := by
    have hcar : ∀ l, (Function.update L.comp m P l).carrier = (L.comp l).carrier := by
      intro l
      by_cases hl : l = m
      · subst hl; rw [Function.update_self, hc]
      · rw [Function.update_of_ne hl]
    show Disjoint (Function.update L.comp m P i).carrier (Function.update L.comp m P j).carrier
    rw [hcar, hcar]
    exact L.disjoint hij

lemma replaceComp_carrier (m : Fin L.k) (P : Polygon E) (hs : P.IsSimple)
    (hc : P.carrier = (L.comp m).carrier) : (L.replaceComp m P hs hc).carrier = L.carrier := by
  simp only [carrier, replaceComp]
  congr 1
  funext l
  by_cases hl : l = m
  · subst hl; rw [Function.update_self, hc]
  · rw [Function.update_of_ne hl]

/-- Re-index component `m` by `r`. -/
def rotateComp (m : Fin L.k) (r : ℕ) : PolygonalLink E :=
  L.replaceComp m ((L.comp m).rotateBy r) ((L.comp m).isSimple_rotateBy (L.simple m) r)
    ((L.comp m).carrier_rotateBy r)

/-- **Re-indexing one component is a move.** -/
theorem move_rotateComp (m : Fin L.k) (r : ℕ) : Move L (L.rotateComp m r) := by
  refine Move.relabel L _ (Equiv.refl _) (Function.update 0 m r) fun i => ?_
  by_cases hi : i = m
  · subst hi
    simp [rotateComp, replaceComp]
  · simp only [rotateComp, replaceComp, Equiv.refl_apply, Function.update_of_ne hi]
    rfl

lemma rotateComp_carrier (m : Fin L.k) (r : ℕ) : (L.rotateComp m r).carrier = L.carrier :=
  replaceComp_carrier _ _ _ _ _

/-- **The vertex slide lemma.** Let `P = L.comp m` have last vertex `b`, first vertex `d` and
penultimate vertex `a`, and let `L'` be `L` with `b` replaced by `c` (up to relabelling). If

* `c ∉ {b, d}` and `[b, c] ∩ [c, d] ⊆ {c}`,
* the triangle `{b, d, c}` meets `L` only in the edge `[b, d]`, and
* the triangle `{a, c, b}` meets `L'` only in the edge `[a, c]`,

then `L` and `L'` are Δ-equivalent. -/
theorem deltaEquiv_setLast (L' : PolygonalLink E) (e : Fin L.k ≃ Fin L'.k) (m : Fin L.k) (c : E)
    (hother : ∀ i, i ≠ m → L'.comp (e i) = L.comp i)
    (hm : L'.comp (e m) = (L.comp m).setLast c)
    (hca : c ≠ (L.comp m).v (Fin.last _)) (hcb : c ≠ (L.comp m).v 0)
    (hseg : segment ℝ ((L.comp m).v (Fin.last _)) c ∩ segment ℝ c ((L.comp m).v 0) ⊆ {c})
    (htri₁ : convexHull ℝ {(L.comp m).v (Fin.last _), (L.comp m).v 0, c} ∩ L.carrier =
      segment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0))
    (htri₂ : convexHull ℝ {(L.comp m).v (L.comp m).penult, c, (L.comp m).v (Fin.last _)} ∩
      L'.carrier = segment ℝ ((L.comp m).v (L.comp m).penult) c) :
    DeltaEquiv L L' := by
  set P := L.comp m with hP
  -- step 1: insert `c` on the closing edge
  set L₁ := L.deltaMove m c hca hcb hseg htri₁ with hL₁
  have h₁ : Move L L₁ := L.move_deltaMove m c hca hcb hseg htri₁
  have hL₁m : L₁.comp m = P.subdivideLast c := Function.update_self _ _ _
  -- step 2: re-index the new component to start at `c`
  set L₂ := L₁.rotateComp m (P.n + 1) with hL₂
  have h₂ : Move L₁ L₂ := L₁.move_rotateComp m (P.n + 1)
  -- step 3 (backwards): `L'` re-indexed to start at `c`
  set L₃ := L'.rotateComp (e m) P.n with hL₃
  have h₄ : Move L' L₃ := L'.move_rotateComp (e m) P.n
  have hL₃m : L₃.comp (e m) = (P.setLast c).rot P.n := by
    show Function.update L'.comp (e m) ((L'.comp (e m)).rotateBy P.n) (e m) = _
    rw [Function.update_self, hm, Polygon.rotateBy_eq_rot]
  -- step 3: `L₂` is `L₃` with the old last vertex inserted back
  have h₃ : Move L₃ L₂ := by
    refine Move.delta L₃ L₂ e.symm (e m) (P.v (Fin.last _)) (fun i hi => ?_) ?_ ?_
    · have hi' : e.symm i ≠ m := fun h => hi (by rw [← h, Equiv.apply_symm_apply])
      have hne : i ≠ e m := hi
      show Function.update L₁.comp m ((L₁.comp m).rotateBy (P.n + 1)) (e.symm i) =
        Function.update L'.comp (e m) ((L'.comp (e m)).rotateBy P.n) i
      rw [Function.update_of_ne hi', Function.update_of_ne hne]
      rw [show L₁.comp (e.symm i) = L.comp (e.symm i) from Function.update_of_ne hi' _ _]
      rw [← hother _ hi', Equiv.apply_symm_apply]
    · rw [hL₃m]
      show Function.update L₁.comp m ((L₁.comp m).rotateBy (P.n + 1)) (e.symm (e m)) = _
      rw [Equiv.symm_apply_apply]
      rw [Function.update_self, hL₁m, Polygon.rotateBy_eq_rot, Polygon.subdivideLast_rot_eq]
    · have hc3 : L₃.carrier = L'.carrier := L'.rotateComp_carrier _ _
      rw [hc3, hL₃m, Polygon.setLast_rot_v_last, Polygon.setLast_rot_v_zero]
      convert htri₂ using 2
  exact Relation.EqvGen.trans _ _ _ (Relation.EqvGen.rel _ _ h₁)
    (Relation.EqvGen.trans _ _ _ (Relation.EqvGen.rel _ _ h₂)
      (Relation.EqvGen.trans _ _ _ (Relation.EqvGen.symm _ _ (Relation.EqvGen.rel _ _ h₃))
        (Relation.EqvGen.symm _ _ (Relation.EqvGen.rel _ _ h₄))))

end PolygonalLink

end QOU.MathlibExt.PL
