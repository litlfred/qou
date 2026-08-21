import QOU.Mathlib.SchenstedCornersAlong

/-!
# QOU.Mathlib.SchenstedMaxCorner — a row holding a maximum entry is a corner (brick 16)

Brick 15 discharged brick 14's `CornersAlong` hypothesis for runs built by **insertion**, which
showed the hypothesis is inhabited. Surjectivity of `rskPair` needs something strictly stronger:
`CornersAlong P is` for an **arbitrary** standard pair `(P, Q)`, with the positions read off `Q`
rather than off an insertion history. This file proves the keystone that argument turns on.

> **`isCorner_of_max_in_row`** — if the last cell of row `i` holds an entry no smaller than every
> entry of the tableau, then row `i` is a corner.

The proof is the one-line contradiction the classical argument uses, and it needs **less than
standardness**. Suppose row `i` were not a corner. `ColStrict`'s length half already forces
`len(row i+1) ≤ len(row i)`, so "not a corner" pins them **equal** — and then row `i + 1` has a cell
directly below the maximum, carrying a strictly larger entry. That contradicts maximality.

No hypothesis that rows increase *strictly* is needed, and no standardness predicate is needed —
`ColStrict` plus knowing where the maximum sits is enough. That is worth recording, because the
corpus has no list-level standardness predicate and I was about to write one.

## The two pieces

* `le_getD_last_of_sorted` — in a weakly-increasing row, the last entry is the largest. This is what
  lets a caller who only knows "the maximum is *somewhere* in row `i`" reach the hypothesis of the
  keystone, which is stated about the last cell.
* `isCorner_of_max_in_row` — the keystone.

## Scope

One step. Wiring this along a whole run — reading the positions off `Q`, showing each step's
removed cell carries the largest *remaining* entry, and assembling `CornersAlong` — is the next
brick of epic `qou-nrex`. Nothing here claims it, nothing here claims `rskPair` is bijective, and
`RSKBurnsideHolds` for general `n` stays open (proved for `n ≤ 12` by an unrelated route,
`PartitionsOfBridge.rskBurnsideHolds_le12`, with no RSK correspondence in it).

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- **In a weakly-increasing row the last entry is the largest.** Brick 10's `dropLast_le_getLast`
covers everything before the last cell; the last cell is `≤` itself. -/
theorem le_getD_last_of_sorted {r : List ℕ} (hs : r.Sorted (· ≤ ·)) (hne : r ≠ []) :
    ∀ v ∈ r, v ≤ r.getD (r.length - 1) 0 := by
  intro v hv
  rw [getD_length_sub_one hne]
  have hsplit : r.dropLast ++ [r.getLast hne] = r := List.dropLast_append_getLast hne
  rw [← hsplit] at hv
  rcases List.mem_append.mp hv with hv' | hv'
  · exact dropLast_le_getLast hs hne v hv'
  · simp only [List.mem_singleton] at hv'
    exact le_of_eq hv'

/-- **A row whose last cell holds a maximum entry is a corner.**

If row `i` were not a corner, `ColStrict`'s length half — which already gives
`len(row i+1) ≤ len(row i)` — would pin the two rows **equal in length**, putting a cell of row
`i + 1` directly below the maximum. Column-strictness makes that cell strictly larger, contradicting
maximality.

Note what is *not* assumed: rows need not increase strictly, and no standardness predicate appears.
`ColStrict` and the position of the maximum are the whole input. -/
theorem isCorner_of_max_in_row {T : List (List ℕ)} (hc : ColStrict T) (hne : NoEmptyRows T)
    {i : ℕ} (hi : i < T.length)
    (hmax : ∀ row ∈ T, ∀ v ∈ row, v ≤ (T.getD i []).getD ((T.getD i []).length - 1) 0) :
    IsCorner T i := by
  have hrne : T.getD i [] ≠ [] := by
    rw [getD_row_eq hi]
    exact hne _ (List.getElem_mem _)
  have hrpos : 0 < (T.getD i []).length := List.length_pos_iff.mpr hrne
  rw [IsCorner]
  by_cases hlast : i + 1 < T.length
  · -- there is a row below; column-strictness supplies the contradiction
    obtain ⟨hlen, hlt⟩ := colStrict_adjacent hc hlast
    by_contra hcon
    push_neg at hcon
    -- not a corner plus the length half pins the two rows equal in length
    have heq : (T.getD (i + 1) []).length = (T.getD i []).length := le_antisymm hlen hcon
    have hidx : (T.getD i []).length - 1 < (T.getD (i + 1) []).length := by omega
    have hstrict := hlt ((T.getD i []).length - 1) hidx
    -- the cell directly below the maximum is strictly larger, yet bounded by it
    have hmem : (T.getD (i + 1) []).getD ((T.getD i []).length - 1) 0 ∈ T.getD (i + 1) [] :=
      getD_mem hidx
    have hrowmem : T.getD (i + 1) [] ∈ T := by
      rw [getD_row_eq hlast]; exact List.getElem_mem _
    exact absurd (hmax _ hrowmem _ hmem) (by omega)
  · -- row `i` is the last row: the row below reads as `[]`
    push_neg at hlast
    rw [getD_row_past hlast]
    simpa using hrpos

/-- The keystone in the form a caller usually has it: the maximum is known to lie **somewhere** in
row `i`, and the row is weakly increasing, so it lies at the end. -/
theorem isCorner_of_max_in_row_sorted {T : List (List ℕ)} (hc : ColStrict T)
    (hne : NoEmptyRows T) (hs : RowsSorted T) {i : ℕ} (hi : i < T.length) {m : ℕ}
    (hmem : m ∈ T.getD i []) (hmax : ∀ row ∈ T, ∀ v ∈ row, v ≤ m) : IsCorner T i := by
  have hrowmem : T.getD i [] ∈ T := by rw [getD_row_eq hi]; exact List.getElem_mem _
  have hrne : T.getD i [] ≠ [] := hne _ hrowmem
  have hle : m ≤ (T.getD i []).getD ((T.getD i []).length - 1) 0 :=
    le_getD_last_of_sorted (hs _ hrowmem) hrne m hmem
  refine isCorner_of_max_in_row hc hne hi (fun row hrow v hv => ?_)
  exact le_trans (hmax row hrow v hv) hle

end QOU.Mathlib.Schensted
