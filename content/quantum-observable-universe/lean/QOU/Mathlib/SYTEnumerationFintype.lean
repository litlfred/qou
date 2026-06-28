import QOU.Mathlib.SYTEnumerationBridge
import QOU.Mathlib.RSKBurnsideTarget
import Mathlib.Data.List.Permutation
import Mathlib.Data.List.Perm.Basic
import Mathlib.Data.List.Nodup
import Mathlib.Data.Fintype.List
import Mathlib.SetTheory.Cardinal.Finite

/-!
# QOU.Mathlib.SYTEnumerationFintype — the SYT counting bridge

This closes the second half of the bridge from `SYTEnumerationBridge`: the brute-force list
enumeration `numSYTenum l` equals the structure-level genuine count
`numStandardYoungTableaux (ofRowLens l hl) = Nat.card (StandardYoungTableau _)`.

The proof builds an explicit equivalence

    StandardYoungTableau (ofRowLens l hl)  ≃  { a : List ℕ // a ∈ standardFillings l }

(row-major flatten one way; reshape via `chunk` + the four `SemistandardYoungTableau` obligations
the other), then chases cardinalities:

    numStandardYoungTableaux (ofRowLens l hl)
      = Nat.card (StandardYoungTableau _)
      = Nat.card { a // a ∈ standardFillings l }     (Nat.card_congr the equiv)
      = (standardFillings l).length                  (standardFillings is Nodup)
      = numSYTenum l.                                (numSYTenum_eq_length_standardFillings)

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open List

/-! ### `chunk` row/entry characterisation -/

/-- `chunk l a` has exactly `l.length` rows. -/
theorem chunk_length (l a : List ℕ) : (chunk l a).length = l.length := by
  induction l generalizing a with
  | nil => simp [chunk]
  | cons len ls ih => simp [chunk, ih]

/-- Row `i` of `chunk l a` (as a `getD`) is the length-`l[i]` slice of `a` starting at the partial
sum `(l.take i).sum`. -/
theorem chunk_getD (l a : List ℕ) (i : ℕ) (hi : i < l.length) :
    (chunk l a).getD i [] = (a.drop ((l.take i).sum)).take (l[i]'hi) := by
  induction l generalizing a i with
  | nil => simp at hi
  | cons len ls ih =>
    cases i with
    | zero => simp [chunk]
    | succ k =>
      have hk : k < ls.length := by simpa using hi
      simp only [chunk, List.getD_cons_succ]
      rw [ih (a.drop len) k hk]
      simp only [List.take_succ_cons, List.sum_cons, List.drop_drop, List.getElem_cons_succ]

/-- `getD` of an in-range index. -/
private theorem getD_of_lt {α : Type*} (l : List α) {i : ℕ} (h : i < l.length) (d : α) :
    l.getD i d = l[i] := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h]; rfl

/-- `getD` of an out-of-range index returns the default. -/
private theorem getD_of_ge {α : Type*} (l : List α) {i : ℕ} (h : l.length ≤ i) (d : α) :
    l.getD i d = d := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none h]; rfl

/-- The reshaped entry map of a flat filling `a` for shape `l`: entry `(i,j)` is element `j` of
row `i` of `chunk l a` (off-grid entries default to `0`). -/
def entryFn (l a : List ℕ) (i j : ℕ) : ℕ := ((chunk l a).getD i []).getD j 0

/-- **In-range value of `entryFn`**: when `i < l.length`, `j < l[i]` and `a` is long enough
(`(l.take i).sum + l[i] ≤ a.length`), entry `(i,j)` is the flat element at the row-major index
`(l.take i).sum + j`. -/
theorem entryFn_eq_getD (l a : List ℕ) (i j : ℕ) (hi : i < l.length) (hj : j < l[i]'hi)
    (hlen : (l.take i).sum + l[i]'hi ≤ a.length) :
    entryFn l a i j = a.getD ((l.take i).sum + j) 0 := by
  unfold entryFn
  rw [chunk_getD l a i hi]
  have hjt : j < ((a.drop ((l.take i).sum)).take (l[i]'hi)).length := by
    rw [List.length_take, List.length_drop]; omega
  rw [getD_of_lt _ hjt, List.getElem_take, List.getElem_drop,
    getD_of_lt a (by omega)]

/-- **`entryFn` vanishes off the grid for the wrong row.** If `i ≥ l.length` then row `i` of
`chunk l a` is `[]`, so every entry there is `0`. -/
theorem entryFn_zero_of_row (l a : List ℕ) (i j : ℕ) (hi : l.length ≤ i) :
    entryFn l a i j = 0 := by
  unfold entryFn
  rw [getD_of_ge (chunk l a) (by rw [chunk_length]; exact hi) []]
  rfl

/-- **`entryFn` vanishes past the row length.** If `j ≥ l[i]` (and `i < l.length`) then column `j`
is past the length-`l[i]` row, so the entry is `0`. -/
theorem entryFn_zero_of_col (l a : List ℕ) (i j : ℕ) (hi : i < l.length) (hj : l[i]'hi ≤ j) :
    entryFn l a i j = 0 := by
  unfold entryFn
  rw [chunk_getD l a i hi, getD_of_ge]
  rw [List.length_take, List.length_drop]
  omega

end QOU.Mathlib.SYTEnum
