import QOU.Mathlib.SchenstedReverseCascade

/-!
# QOU.Mathlib.SchenstedWordRecovery — recovering the word (RSK inverse, brick 3)

Brick 2 undid **one** insertion. This file iterates it: given the final insertion tableau and the
list of rows where each step placed its new cell, the whole word comes back.

* `rowIndices T w` — the row indices, one per letter, in insertion order. Built by running the
  same recursion `insertWord` runs, so it is a record of the fold, not a search.
* `uninsertSteps T is` — undo the steps of `is` from the final tableau `T`, recovering the word.
  The recursion is structural in the *forward* index list: `uninsertSteps T (i :: rest)` undoes
  the later steps first (`rest`) and only then step `i`, which is what makes it a plain structural
  recursion rather than a fold over a reversed list.
* **`uninsertSteps_foldl`** — the inversion law, and **`uninsertSteps_insertWord`** — its
  specialisation at the empty tableau: `uninsertSteps (insertWord w) (rowIndices [] w) = ([], w)`.

So the insertion tableau together with the row-index list determines the word. **That is the whole
content of the RSK inverse on the `P` side**; what remains is that the *recording tableau* encodes
exactly that index list, which is brick 4.

## Scope

The `P` side only, and conditional on being handed the index list. Nothing here says the recording
tableau supplies it, nothing here proves `rskPair` bijective, and `RSKBurnsideHolds` for general
`n` stays open. (It is proved for `n ≤ 12` by an unrelated route —
`PartitionsOfBridge.rskBurnsideHolds_le12` — with no RSK in it.)

Pure combinatorics on `ℕ`; nothing archimedean.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

/-- **The row-index record.** For each letter of `w`, the row where its insertion appended the new
cell — computed along the same fold `insertWord` performs. -/
def rowIndices : List (List ℕ) → List ℕ → List ℕ
  | _, [] => []
  | T, x :: rest => newRowIndex T x :: rowIndices (insert T x) rest

@[simp] theorem rowIndices_nil (T : List (List ℕ)) : rowIndices T [] = [] := rfl

theorem rowIndices_cons (T : List (List ℕ)) (x : ℕ) (rest : List ℕ) :
    rowIndices T (x :: rest) = newRowIndex T x :: rowIndices (insert T x) rest := rfl

/-- **Undo a run of insertions.** `uninsertSteps T is` treats `T` as the tableau *after* all the
steps recorded in `is` (in insertion order) and peels them off, returning the starting tableau and
the recovered word.

Note the order: `i :: rest` undoes `rest` — the *later* steps — before `i`. That is what keeps this
a structural recursion on the forward list. -/
def uninsertSteps : List (List ℕ) → List ℕ → List (List ℕ) × List ℕ
  | T, [] => (T, [])
  | T, i :: rest =>
      match uninsertSteps T rest with
      | (T', w) =>
          match uninsert T' i with
          | (T'', some x) => (T'', x :: w)
          | (T'', none) => (T'', w)

@[simp] theorem uninsertSteps_nil (T : List (List ℕ)) : uninsertSteps T [] = (T, []) := rfl

theorem uninsertSteps_cons (T : List (List ℕ)) (i : ℕ) (rest : List ℕ) :
    uninsertSteps T (i :: rest) =
      match uninsertSteps T rest with
      | (T', w) =>
          match uninsert T' i with
          | (T'', some x) => (T'', x :: w)
          | (T'', none) => (T'', w) := rfl

/-- **The word-recovery law.** Running the insertions of `w` into a well-formed `T` and then
undoing them at their recorded rows returns `T` and `w` exactly.

The induction is the mirror of `insertWord`'s fold: the outer step of `w` is undone *last*, which
is where `uninsertSteps`' order pays off — the inductive hypothesis applies to the inner fold
unchanged, and brick 2's `uninsert_insert` closes the outer step. -/
theorem uninsertSteps_foldl : ∀ (w : List ℕ) (T : List (List ℕ)),
    RowsSorted T → NoEmptyRows T →
    uninsertSteps (w.foldl insert T) (rowIndices T w) = (T, w)
  | [], T, _, _ => rfl
  | x :: rest, T, hs, hne => by
      rw [rowIndices_cons, List.foldl_cons, uninsertSteps_cons,
        uninsertSteps_foldl rest (insert T x) (insert_rowsSorted hs x) (insert_noEmptyRows hne x)]
      simp only
      rw [uninsert_insert T hs hne x]

/-- **Word recovery from the empty tableau** — the form the RSK inverse consumes:
`insertWord w` together with `rowIndices [] w` determines `w`. -/
theorem uninsertSteps_insertWord (w : List ℕ) :
    uninsertSteps (insertWord w) (rowIndices [] w) = ([], w) :=
  uninsertSteps_foldl w [] rowsSorted_nil noEmptyRows_nil

/-- **The `P` side of RSK is injective, given the index list.** Two words with the same insertion
tableau *and* the same row-index record are equal.

This is the shape brick 4 will discharge: the recording tableau determines `rowIndices`, so equal
`(P, Q)` pairs force equal words. -/
theorem word_eq_of_insertWord_eq (w w' : List ℕ)
    (hP : insertWord w = insertWord w') (hI : rowIndices [] w = rowIndices [] w') : w = w' := by
  have h := uninsertSteps_insertWord w
  rw [hP, hI, uninsertSteps_insertWord w'] at h
  exact (Prod.mk.injEq _ _ _ _ ▸ h).2.symm

end QOU.Mathlib.Schensted
