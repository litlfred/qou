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

/-! ### `strictInc` / `colsOK` extraction -/

/-- `strictInc r` is exactly the chain `r[0] < r[1] < ⋯`. -/
theorem strictInc_iff_chain (r : List ℕ) : strictInc r = true ↔ List.IsChain (· < ·) r := by
  induction r with
  | nil => simp [strictInc]
  | cons a rest ih =>
    cases rest with
    | nil => simp [strictInc]
    | cons b rest' =>
      simp only [strictInc, Bool.and_eq_true, decide_eq_true_eq, List.isChain_cons_cons]
      rw [ih]

/-- A `strictInc` row is strictly monotone on its indices. -/
theorem strictInc_getElem (r : List ℕ) (h : strictInc r = true) (j1 j2 : ℕ) (hj : j1 < j2)
    (h2 : j2 < r.length) : r[j1]'(by omega) < r[j2]'h2 := by
  have hs : r.Sorted (· < ·) := by rwa [strictInc_iff_chain, List.isChain_iff_pairwise] at h
  exact hs.get_strictMono (show (⟨j1, by omega⟩ : Fin r.length) < ⟨j2, h2⟩ from hj)

/-- `colsOK rows` gives strict column inequality between **adjacent** rows: for every `j` valid in
both rows `i` and `i+1`, `rows[i][j] < rows[i+1][j]`. -/
theorem colsOK_getElem (rows : List (List ℕ)) (h : colsOK rows = true) :
    ∀ i (hi : i + 1 < rows.length) j
      (hj2 : j < (rows[i+1]'hi).length) (hj1 : j < (rows[i]'(by omega)).length),
      (rows[i]'(by omega))[j]'hj1 < (rows[i+1]'hi)[j]'hj2 := by
  induction rows with
  | nil => intro i hi; simp at hi
  | cons r1 rest ih =>
    cases rest with
    | nil => intro i hi; simp at hi
    | cons r2 rest' =>
      simp only [colsOK, Bool.and_eq_true] at h
      obtain ⟨hzip, hrest⟩ := h
      intro i hi j hj2 hj1
      cases i with
      | zero =>
        simp only [List.getElem_cons_zero, List.getElem_cons_succ] at hj2 hj1 ⊢
        rw [List.all_eq_true] at hzip
        have hjm : j < (r2.zip r1).length := by rw [List.length_zip]; omega
        have := hzip _ (List.getElem_mem hjm)
        rw [List.getElem_zip] at this
        simpa using this
      | succ k =>
        simp only [List.getElem_cons_succ] at hj2 hj1 ⊢
        exact ih hrest k (by simpa using hi) j hj2 hj1

/-! ### Clean entry-level facts from `isStdFilling` -/

/-- Partial-sum bound: the row-major offset of row `i` plus its length never exceeds `∑l`. -/
theorem take_sum_add_le (l : List ℕ) (i : ℕ) (hi : i < l.length) :
    (l.take i).sum + l[i]'hi ≤ l.sum := by
  conv_rhs => rw [← List.take_append_drop (i + 1) l]
  have hsplit : l.take (i + 1) = l.take i ++ [l[i]'hi] := by
    rw [List.take_succ]; congr; rw [List.getElem?_eq_getElem hi]; rfl
  rw [List.sum_append, hsplit, List.sum_append]
  simp

/-- Row `i` of `chunk l a` has length exactly `l[i]` when `a` is long enough (`a.length = ∑l`). -/
theorem chunk_row_length (l a : List ℕ) (i : ℕ) (hi : i < l.length) (hlen : a.length = l.sum) :
    ((chunk l a).getD i []).length = l[i]'hi := by
  rw [chunk_getD l a i hi, List.length_take, List.length_drop, hlen]
  have := take_sum_add_le l i hi
  omega

/-- Entry `(i,j)` is exactly element `j` of row `i` of `chunk l a` (for in-range `i`, `j`). -/
theorem entryFn_eq_row_getElem (l a : List ℕ) (i j : ℕ) (hi : i < l.length)
    (hj : j < l[i]'hi) (hlen : a.length = l.sum) :
    entryFn l a i j
      = ((chunk l a).getD i [])[j]'(by rw [chunk_row_length l a i hi hlen]; exact hj) := by
  unfold entryFn
  rw [getD_of_lt]

/-- **Row fact.** A standard filling has strictly increasing rows: for `i < l.length` and
`j1 < j2 < l[i]`, `entry i j1 < entry i j2`. -/
theorem isStdFilling_row (l a : List ℕ) (h : isStdFilling l a = true) (hlen : a.length = l.sum)
    (i j1 j2 : ℕ) (hi : i < l.length) (hj : j1 < j2) (hj2 : j2 < l[i]'hi) :
    entryFn l a i j1 < entryFn l a i j2 := by
  have hrows : (chunk l a).all strictInc = true := by
    unfold isStdFilling at h; rw [Bool.and_eq_true] at h; simpa using h.1
  have hrl : ((chunk l a).getD i []).length = l[i]'hi := chunk_row_length l a i hi hlen
  have hmem : (chunk l a).getD i [] ∈ chunk l a := by
    rw [getD_of_lt (chunk l a) (by rw [chunk_length]; exact hi)]
    exact List.getElem_mem _
  have hsi : strictInc ((chunk l a).getD i []) = true := (List.all_eq_true.mp hrows) _ hmem
  have h2 : j2 < ((chunk l a).getD i []).length := by rw [hrl]; exact hj2
  rw [entryFn_eq_row_getElem l a i j1 hi (by omega) hlen,
      entryFn_eq_row_getElem l a i j2 hi hj2 hlen]
  exact strictInc_getElem _ hsi j1 j2 hj h2

/-- **Adjacent-column fact.** A standard filling has strictly increasing columns between adjacent
rows: for `i+1 < l.length` and `j < l[i+1]` (≤ `l[i]` by the partition condition),
`entry i j < entry (i+1) j`. -/
theorem isStdFilling_adjcol (l a : List ℕ) (h : isStdFilling l a = true) (hlen : a.length = l.sum)
    (hl : List.Sorted (· ≥ ·) l) (i j : ℕ) (hi : i + 1 < l.length) (hj : j < l[i + 1]'hi) :
    entryFn l a i j < entryFn l a (i + 1) j := by
  have hcols : colsOK (chunk l a) = true := by
    unfold isStdFilling at h; rw [Bool.and_eq_true] at h; simpa using h.2
  have hi0 : i < l.length := by omega
  -- partition monotone: l[i+1] ≤ l[i]
  have hmono : l[i + 1]'hi ≤ l[i]'hi0 := by
    have := List.pairwise_iff_getElem.mp hl i (i + 1) hi0 hi (by omega)
    simpa using this
  have hj0 : j < l[i]'hi0 := by omega
  have hrl0 : ((chunk l a).getD i []).length = l[i]'hi0 := chunk_row_length l a i hi0 hlen
  have hrl1 : ((chunk l a).getD (i + 1) []).length = l[i + 1]'hi := chunk_row_length l a (i + 1) hi hlen
  -- chunk index versions
  have hci : i + 1 < (chunk l a).length := by rw [chunk_length]; exact hi
  have hgetD0 : (chunk l a).getD i [] = (chunk l a)[i]'(by omega) :=
    getD_of_lt (chunk l a) (by omega) []
  have hgetD1 : (chunk l a).getD (i + 1) [] = (chunk l a)[i + 1]'hci :=
    getD_of_lt (chunk l a) hci []
  have hj2 : j < ((chunk l a)[i + 1]'hci).length := by rw [← hgetD1, hrl1]; exact hj
  have hj1 : j < ((chunk l a)[i]'(by omega)).length := by rw [← hgetD0, hrl0]; exact hj0
  have hcol := colsOK_getElem (chunk l a) hcols i hci j hj2 hj1
  rw [entryFn_eq_row_getElem l a i j hi0 hj0 hlen,
      entryFn_eq_row_getElem l a (i + 1) j hi hj hlen]
  have e0 : ((chunk l a).getD i [])[j]'(by rw [hrl0]; exact hj0)
      = ((chunk l a)[i]'(by omega))[j]'hj1 := by
    congr 1
  have e1 : ((chunk l a).getD (i + 1) [])[j]'(by rw [hrl1]; exact hj)
      = ((chunk l a)[i + 1]'hci)[j]'hj2 := by
    congr 1
  rw [e0, e1]; exact hcol

/-- Adjacent-column strictness chains to **general** column strictness. -/
theorem isStdFilling_col_aux (l a : List ℕ) (h : isStdFilling l a = true) (hlen : a.length = l.sum)
    (hl : List.Sorted (· ≥ ·) l) (i1 n j : ℕ)
    (hi2 : i1 + n + 1 < l.length) (hj : j < l[i1 + n + 1]'hi2) :
    entryFn l a i1 j < entryFn l a (i1 + n + 1) j := by
  induction n with
  | zero =>
    simpa using isStdFilling_adjcol l a h hlen hl i1 j (by simpa using hi2) (by simpa using hj)
  | succ k ih =>
    have hmid : i1 + k + 1 < l.length := by omega
    have hmono : l[i1 + (k + 1) + 1]'hi2 ≤ l[i1 + k + 1]'hmid := by
      have := List.pairwise_iff_getElem.mp hl (i1 + k + 1) (i1 + (k + 1) + 1) hmid hi2 (by omega)
      simpa using this
    have hjmid : j < l[i1 + k + 1]'hmid := by omega
    have step1 : entryFn l a i1 j < entryFn l a (i1 + k + 1) j := ih hmid hjmid
    have hi2' : (i1 + k + 1) + 1 < l.length := by omega
    have hj' : j < l[(i1 + k + 1) + 1]'hi2' := by
      have he : (i1 + k + 1) + 1 = i1 + (k + 1) + 1 := by omega
      rw [getElem_congr_idx he]; exact hj
    have step2 := isStdFilling_adjcol l a h hlen hl (i1 + k + 1) j hi2' hj'
    rw [show i1 + (k + 1) + 1 = (i1 + k + 1) + 1 by omega]
    exact lt_trans step1 step2

/-- **Column fact.** For `i1 < i2 < l.length` and `j < l[i2]`, `entry i1 j < entry i2 j`. -/
theorem isStdFilling_col (l a : List ℕ) (h : isStdFilling l a = true) (hlen : a.length = l.sum)
    (hl : List.Sorted (· ≥ ·) l) (i1 i2 j : ℕ) (hlt : i1 < i2) (hi2 : i2 < l.length)
    (hj : j < l[i2]'hi2) :
    entryFn l a i1 j < entryFn l a i2 j := by
  obtain ⟨n, rfl⟩ : ∃ n, i2 = i1 + n + 1 := ⟨i2 - i1 - 1, by omega⟩
  exact isStdFilling_col_aux l a h hlen hl i1 n j hi2 hj

end QOU.Mathlib.SYTEnum
