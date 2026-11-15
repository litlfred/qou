import QOU.Mathlib.SchenstedAddable
import QOU.Mathlib.SchenstedCornersAlong

/-!
# QOU.Mathlib.SchenstedReinsertRow — the re-inserted letter goes back to the row it came from

Bricks 28 and 29 of epic `qou-nrex` (RSK inverse).

Brick 10 showed the reverse cascade is a right inverse of insertion: re-inserting the ejected letter
rebuilds the tableau. It said nothing about *where* the rebuilt cell landed. This file closes that
gap, and then runs it along a whole peel.

* `addCell_removeCorner` — the shape-level statement: adding a cell back at a corner you just
  removed returns the shape you started from. Its proof is the two-case anatomy of `removeCorner`
  (`removeCorner_eq`): away from length one the filter is inert and the operation is a `set`; at
  length one the corner is the final row and the filter deletes it.
* **`newRowIndex_uninsert`** — the tableau-level statement: `newRowIndex (uninsert T i).1 z = i`.
  It follows from the shape statement because `addCell` moves exactly one entry, so a shape
  determines the index that produced it.
* **`rowIndices_uninsertSteps`** — along a run: the recovered word's row-index record is the list of
  positions the run peeled at, unchanged.

## Why this is the Q side

Brick 4 (`insertWordRecAux_snd_eq_qAppendSteps`) identified the recording tableau as the record of
`rowIndices`. Brick 14 recovered a word whose *insertion* tableau is `P`. Neither said the recovered
word records the positions it was recovered from — without which the recording tableau of the
recovered word is unconstrained. `rowIndices_uninsertSteps` is that missing step.

## Scope

The index bookkeeping only. Nothing here rebuilds a recording tableau from its positions — that is
`qAppendSteps`, and inverting it is the next brick. `rskPair` bijectivity and `RSKBurnsideHolds` for
general `n` are past both and are not claimed.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.Schensted

/-- Setting the final entry rewrites the list as its prefix with that entry replaced. -/
theorem set_last_eq_take : ∀ (l : List ℕ) {i a : ℕ}, i + 1 = l.length →
    l.set i a = l.take i ++ [a]
  | [], i, a, h => by simp at h
  | b :: t, 0, a, h => by
      simp only [List.length_cons] at h
      have ht : t = [] := List.eq_nil_of_length_eq_zero (by omega)
      subst ht; simp
  | b :: t, j + 1, a, h => by
      simp only [List.length_cons] at h
      rw [List.set_cons_succ, set_last_eq_take t (by omega), List.take_succ_cons,
        List.cons_append]

/-- Reading the final entry back off the prefix reassembles the list. -/
theorem take_append_last : ∀ (l : List ℕ) {i : ℕ}, i + 1 = l.length →
    l.take i ++ [l.getD i 0] = l
  | [], i, h => by simp at h
  | b :: t, 0, h => by
      simp only [List.length_cons] at h
      have ht : t = [] := List.eq_nil_of_length_eq_zero (by omega)
      subst ht; simp
  | b :: t, j + 1, h => by
      simp only [List.length_cons] at h
      rw [List.take_succ_cons, List.getD_cons_succ, List.cons_append,
        take_append_last t (by omega)]

/-- A member of a `set` list is a member of the original or the written value. -/
theorem mem_set_or_eq : ∀ {l : List ℕ} {i a b : ℕ}, b ∈ l.set i a → b ∈ l ∨ b = a
  | [], _, _, _, h => by simp at h
  | c :: t, 0, a, b, h => by
      rw [List.set_cons_zero, List.mem_cons] at h
      rcases h with rfl | h
      · exact Or.inr rfl
      · exact Or.inl (List.mem_cons_of_mem _ h)
  | c :: t, i + 1, a, b, h => by
      rw [List.set_cons_succ, List.mem_cons] at h
      rcases h with rfl | h
      · exact Or.inl (List.mem_cons_self ..)
      · rcases mem_set_or_eq h with h' | h'
        · exact Or.inl (List.mem_cons_of_mem _ h')
        · exact Or.inr h'

/-- **The anatomy of `removeCorner` on a Young shape.** Either the row keeps a cell, in which case
the zero-filter is inert and the operation is a plain `set`; or the row had a single cell, in which
case the corner condition forces it to be the last row and the filter deletes it. -/
theorem removeCorner_eq {l : List ℕ} (hy : YoungShape l) {i : ℕ}
    (hc : QOU.Mathlib.SYTEnum.IsCorner l i) :
    (2 ≤ l.getD i 0 ∧ QOU.Mathlib.SYTEnum.removeCorner l i = l.set i (l.getD i 0 - 1)) ∨
      (l.getD i 0 = 1 ∧ i + 1 = l.length ∧
        QOU.Mathlib.SYTEnum.removeCorner l i = l.take i) := by
  obtain ⟨hi, hnext⟩ := hc
  have hpos : 0 < l.getD i 0 := hy.2 _ (getD_mem hi)
  by_cases h1 : 2 ≤ l.getD i 0
  · refine Or.inl ⟨h1, ?_⟩
    rw [QOU.Mathlib.SYTEnum.removeCorner]
    refine filter_ne_zero_of_pos _ (fun a ha => ?_)
    rcases mem_set_or_eq ha with hmem | rfl
    · exact hy.2 a hmem
    · omega
  · have hone : l.getD i 0 = 1 := by omega
    have hlen : i + 1 = l.length := by
      by_contra hcon
      have hlt : i + 1 < l.length := by omega
      have := hy.2 _ (getD_mem hlt)
      omega
    refine Or.inr ⟨hone, hlen, ?_⟩
    rw [QOU.Mathlib.SYTEnum.removeCorner, hone]
    simp only [Nat.sub_self]
    rw [set_last_eq_take l hlen, List.filter_append]
    have hpre : (l.take i).filter (· != 0) = l.take i :=
      filter_ne_zero_of_pos _ (fun a ha => hy.2 a (List.mem_of_mem_take ha))
    rw [hpre]
    simp

/-- **Adding the cell back at a corner returns the shape.** The exact inverse of `removeCorner`, in
the direction the RSK inverse needs: the peel is undone by the re-insertion. -/
theorem addCell_removeCorner {l : List ℕ} (hy : YoungShape l) {i : ℕ}
    (hc : QOU.Mathlib.SYTEnum.IsCorner l i) :
    addCell (QOU.Mathlib.SYTEnum.removeCorner l i) i = l := by
  have hi : i < l.length := hc.1
  rcases removeCorner_eq hy hc with ⟨h2, heq⟩ | ⟨h1, hlen, heq⟩
  · rw [heq, addCell, if_pos (by simpa using hi), getD_set_self (by simpa using hi),
      List.set_set]
    have : l.getD i 0 - 1 + 1 = l.getD i 0 := by omega
    rw [this, getD_eq_getElem_mem hi, List.set_getElem_self]
  · rw [heq, addCell, if_neg (by simp)]
    have := take_append_last l hlen
    rw [h1] at this
    exact this

/-- The peeled index is still a legal position in the peeled shape — needed to compare it with the
index the re-insertion chose. -/
theorem le_length_removeCorner {l : List ℕ} (hy : YoungShape l) {i : ℕ}
    (hc : QOU.Mathlib.SYTEnum.IsCorner l i) :
    i ≤ (QOU.Mathlib.SYTEnum.removeCorner l i).length := by
  have hi : i < l.length := hc.1
  rcases removeCorner_eq hy hc with ⟨_, heq⟩ | ⟨_, hlen, heq⟩
  · rw [heq, List.length_set]; omega
  · rw [heq, List.length_take]; omega

/-- **`addCell` determines its index.** It moves exactly one entry, so two legal indices producing
the same shape are the same index. -/
theorem addCell_index_inj {m : List ℕ} {i j : ℕ} (hi : i ≤ m.length) (hj : j ≤ m.length)
    (h : addCell m i = addCell m j) : i = j := by
  by_contra hne
  have h1 : (addCell m i).getD i 0 = m.getD i 0 + 1 := getD_addCell_self m hi
  have h2 : (addCell m j).getD i 0 = m.getD i 0 := getD_addCell_ne m hj hne
  rw [h, h2] at h1
  omega

/-- **The re-inserted letter goes back to the row it was peeled from.**

Brick 10 said `insert (uninsert T i).1 z = T`; this says the cell that rebuilt `T` is the cell at
row `i`. The argument is entirely at the level of shapes: the peel takes the shape to
`removeCorner`, the re-insertion takes it back by `addCell` at whatever row it chose, and `addCell`
has only one index that lands on the shape you started from. -/
theorem newRowIndex_uninsert {T : List (List ℕ)} (hs : RowsSorted T) (hc : ColStrict T)
    (hne : NoEmptyRows T) {i : ℕ} (hcorner : IsCorner T i) {x : ℕ}
    (hx : (uninsert T i).2 = some x) :
    newRowIndex (uninsert T i).1 x = i := by
  have hy : YoungShape (tableauShape T) := ⟨tableauShape_sorted hc, tableauShape_pos hne⟩
  have hcs : QOU.Mathlib.SYTEnum.IsCorner (tableauShape T) i := (isCorner_iff_shape T i).mp hcorner
  have hT : insert (uninsert T i).1 x = T := insert_uninsert T i hs hc hne x hx
  have hm : tableauShape (uninsert T i).1 = QOU.Mathlib.SYTEnum.removeCorner (tableauShape T) i :=
    tableauShape_uninsert T i hc hne hcorner
  have h1 := tableauShape_insert (uninsert T i).1 x
  rw [hT, hm] at h1
  have h2 : addCell (QOU.Mathlib.SYTEnum.removeCorner (tableauShape T) i) i = tableauShape T :=
    addCell_removeCorner hy hcs
  have hj : newRowIndex (uninsert T i).1 x
      ≤ (QOU.Mathlib.SYTEnum.removeCorner (tableauShape T) i).length := by
    have := newRowIndex_le (uninsert T i).1 x
    rwa [hm] at this
  exact (addCell_index_inj (le_length_removeCorner hy hcs) hj (h2.trans h1)).symm

/-- **The recovered word records the positions it was recovered from.**

One step of `newRowIndex_uninsert` wrapped around the inductive hypothesis, with brick 10 collapsing
the intermediate tableau back to the one the hypothesis is stated at. -/
theorem rowIndices_uninsertSteps : ∀ (is : List ℕ) (T : List (List ℕ)),
    RowsSorted T → ColStrict T → NoEmptyRows T → CornersAlong T is →
    rowIndices (uninsertSteps T is).1 (uninsertSteps T is).2 = is
  | [], _, _, _, _, _ => rfl
  | i :: rest, T, hs, hc, hne, hca => by
      obtain ⟨hcaRest, hcorner⟩ := hca
      obtain ⟨hs', hc', hne'⟩ := uninsertSteps_invariants rest T hs hc hne hcaRest
      obtain ⟨x, hx⟩ := uninsert_isSome_of_isCorner hc' hne' hcorner
      rw [uninsertSteps_cons_fst, uninsertSteps_cons_snd_some T i rest hx, rowIndices_cons,
        newRowIndex_uninsert hs' hc' hne' hcorner hx,
        insert_uninsert _ i hs' hc' hne' x hx,
        rowIndices_uninsertSteps rest T hs hc hne hcaRest]

end QOU.Mathlib.Schensted
