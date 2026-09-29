import QOU.Mathlib.SchenstedRecordingTrunc

/-!
# QOU.Mathlib.SchenstedShapeOfPositions — the positions build the recording tableau's shape

Brick 37 of epic `qou-nrex` (RSK inverse).

Brick 32 takes the two tableaux of a pair as related by
`hshape : tableauShape P = addCellSteps [] (qPositions Q n)` — the shape `Q`'s positions *build*.
For a pair of standard tableaux the hypothesis one actually has is that `P` and `Q` share a shape.
This file identifies the two:

**`addCellSteps_qPositions`** — `addCellSteps [] (qPositions Q n) = tableauShape Q`.

Row `i` of the built shape has one cell per position equal to `i` (brick 22's `getD_addCellSteps`),
which is the number of `Q`'s row-`i` entries below the horizon (brick 26's `count_qPositions`) —
and once the horizon clears every entry, that is the row's length. Off the end both sides vanish:
every position is a genuine row index, so it contributes no count there.

The two lists are then equal by `eq_of_getD_eq`: lists of *positive* naturals agreeing at every
index are equal. Positivity is what supplies the lengths — a longer list would read positive where
the shorter reads the default `0` — and both sides have it, `tableauShape Q` because `Q` has no
empty rows and the built shape because `addCell` only ever adds.

## Scope

The shape hypothesis of brick 32, discharged from "the pair shares a shape". It does not run brick
32, and `rskPair` surjectivity still needs its `Σ`-equality threaded through `rskPair`'s definition.
`RSKBurnsideHolds` for general `n` remains open.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

/-- **Lists of positive naturals agreeing at every index are equal.** Positivity is what pins the
lengths: past the shorter list `getD` reads the default `0`, which the longer one cannot. -/
theorem eq_of_getD_eq : ∀ {l m : List ℕ}, (∀ a ∈ l, 0 < a) → (∀ a ∈ m, 0 < a) →
    (∀ i, l.getD i 0 = m.getD i 0) → l = m := by
  intro l m hl hm h
  have hlen : l.length = m.length := by
    by_contra hne
    rcases Nat.lt_or_ge l.length m.length with hlt | hge
    · have h1 : m.getD l.length 0 = 0 := by rw [← h l.length, getD_past (le_refl _)]
      have h2 : 0 < m.getD l.length 0 := hm _ (getD_mem hlt)
      omega
    · have hlt : m.length < l.length := by omega
      have h1 : l.getD m.length 0 = 0 := by rw [h m.length, getD_past (le_refl _)]
      have h2 : 0 < l.getD m.length 0 := hl _ (getD_mem hlt)
      omega
  refine List.ext_getElem hlen (fun i h1 h2 => ?_)
  have := h i
  rwa [getD_eq_getElem_mem h1, getD_eq_getElem_mem h2] at this

/-- An addable run builds a Young shape. -/
theorem youngShape_addCellSteps : ∀ (is : List ℕ) (l : List ℕ), YoungShape l → AddableAlong l is →
    YoungShape (addCellSteps l is)
  | [], _, hy, _ => hy
  | i :: rest, l, hy, haa => by
      obtain ⟨hadd, haaRest⟩ := haa
      rw [addCellSteps_cons]
      exact youngShape_addCellSteps rest (addCell l i) (youngShape_addCell hy hadd) haaRest

/-- Every recorded position is a genuine row index, so no position lands past the last row. -/
theorem count_qPositions_past {Q : List (List ℕ)} {n i : ℕ} (hi : Q.length ≤ i)
    (hrange : ∀ t, t < n → t ∈ Q.flatten) : (qPositions Q n).count i = 0 := by
  rw [List.count_eq_zero]
  intro hmem
  rw [qPositions, List.mem_map] at hmem
  obtain ⟨t, ht, hti⟩ := hmem
  rw [List.mem_range] at ht
  obtain ⟨r, hr⟩ := qRowOf_isSome_of_mem_flatten Q t (hrange t ht)
  rw [hr, Option.getD_some] at hti
  have := qRowOf_lt_length Q t r hr
  omega

/-- **The positions build the shape.** Row `i` gains one cell per position equal to `i`, which is
the count of row-`i` entries below the horizon — the row's whole length, once the horizon clears
every entry. -/
theorem addCellSteps_qPositions {Q : List (List ℕ)} (hQc : ColStrict Q)
    (hQstrict : ∀ row ∈ Q, row.Sorted (· < ·)) (hQnd : Q.flatten.Nodup) (hQn : NoEmptyRows Q)
    {n : ℕ} (hrange : ∀ t, t < n → t ∈ Q.flatten) (hlt : ∀ a ∈ Q.flatten, a < n) :
    addCellSteps [] (qPositions Q n) = tableauShape Q := by
  have haa : AddableAlong [] (qPositions Q n) :=
    addableAlong_qPositions hQc hQstrict hQnd n hrange
  refine eq_of_getD_eq (youngShape_addCellSteps _ [] ⟨List.sorted_nil, by simp⟩ haa).2
    (tableauShape_pos hQn) (fun i => ?_)
  rw [getD_addCellSteps _ [] haa i, List.getD_nil, Nat.zero_add, getD_tableauShape Q i]
  by_cases hi : i < Q.length
  · rw [count_qPositions hQnd hi hrange, countLt,
      filter_lt_eq_self _ (fun a ha => hlt a (getD_mem_flatten (r := i) ha))]
  · rw [count_qPositions_past (Nat.not_lt.mp hi) hrange, getD_row_past (Nat.not_lt.mp hi)]
    simp

end QOU.Mathlib.Schensted
