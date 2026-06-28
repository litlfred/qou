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

/-! ### The row-major index map and the inverse SYT -/

/-- The row-major flat index of cell `(i,j)`: `(l.take i).sum + j`. -/
def idx (l : List ℕ) (i j : ℕ) : ℕ := (l.take i).sum + j

/-- Step law for the partial sums of `l`. -/
theorem take_sum_succ (l : List ℕ) (i : ℕ) (hi : i < l.length) :
    (l.take (i + 1)).sum = (l.take i).sum + l[i]'hi := by
  have hsplit : l.take (i + 1) = l.take i ++ [l[i]'hi] := by
    rw [List.take_succ]; congr; rw [List.getElem?_eq_getElem hi]; rfl
  rw [hsplit, List.sum_append]; simp

/-- Partial sums of `l` are monotone in the prefix length. -/
theorem take_sum_mono (l : List ℕ) (i k : ℕ) (h : i ≤ k) :
    (l.take i).sum ≤ (l.take k).sum := by
  have hsub : l.take i <+ l.take k := (List.take_prefix_take_left h).sublist
  exact List.Sublist.sum_le_sum hsub (fun x _ => Nat.zero_le x)

/-- The row-major index of a cell is `< ∑l`. -/
theorem idx_lt_sum (l : List ℕ) (i j : ℕ) (hi : i < l.length) (hj : j < l[i]'hi) :
    idx l i j < l.sum := by
  unfold idx
  have := take_sum_add_le l i hi
  omega

/-- The row-major index map is injective on cells: distinct cells get distinct flat indices. -/
theorem idx_injOn (l : List ℕ) (i1 j1 i2 j2 : ℕ)
    (hi1 : i1 < l.length) (hj1 : j1 < l[i1]'hi1) (hi2 : i2 < l.length) (hj2 : j2 < l[i2]'hi2)
    (heq : idx l i1 j1 = idx l i2 j2) : i1 = i2 ∧ j1 = j2 := by
  unfold idx at heq
  -- WLOG i1 ≤ i2; rule out i1 < i2 by the gap bound.
  have key : ∀ x1 y1 x2, (hx1 : x1 < l.length) → y1 < l[x1]'hx1 →
      x1 < x2 → (l.take x1).sum + y1 < (l.take x2).sum := by
    intro x1 y1 x2 hx1 hy1 hlt
    have hstep : (l.take (x1 + 1)).sum = (l.take x1).sum + l[x1]'hx1 := take_sum_succ l x1 hx1
    have hmono : (l.take (x1 + 1)).sum ≤ (l.take x2).sum := take_sum_mono l (x1 + 1) x2 (by omega)
    omega
  rcases lt_trichotomy i1 i2 with h | h | h
  · have := key i1 j1 i2 hi1 hj1 h; omega
  · subst h; exact ⟨rfl, by omega⟩
  · have := key i2 j2 i1 hi2 hj2 h; omega

/-- The entry map equals `a` precomposed with the row-major index, on cells (given `a.length = ∑l`). -/
theorem entryFn_eq_a_idx (l a : List ℕ) (i j : ℕ) (hi : i < l.length) (hj : j < l[i]'hi)
    (hlen : a.length = l.sum) :
    entryFn l a i j = a[idx l i j]'(by rw [hlen]; exact idx_lt_sum l i j hi hj) := by
  rw [entryFn_eq_getD l a i j hi hj (by rw [hlen]; exact take_sum_add_le l i hi)]
  rw [getD_of_lt]
  rfl

/-- A flat filling that is a permutation of `[1,…,∑l]` has entries in `[1,∑l]`. -/
theorem a_getElem_mem_Icc (l a : List ℕ) (hp : a.Perm ((List.range l.sum).map (· + 1)))
    (k : ℕ) (hk : k < a.length) : 1 ≤ a[k] ∧ a[k] ≤ l.sum := by
  have hmem : a[k] ∈ a := List.getElem_mem hk
  rw [hp.mem_iff] at hmem
  simp only [List.mem_map, List.mem_range] at hmem
  obtain ⟨x, hx, hxe⟩ := hmem
  omega

/-- `a` is `Nodup` (a permutation of the `Nodup` list `[1,…,∑l]`). -/
theorem a_nodup (l a : List ℕ) (hp : a.Perm ((List.range l.sum).map (· + 1))) : a.Nodup := by
  have hrng : ((List.range l.sum).map (· + 1)).Nodup :=
    List.Nodup.map (by intro x y hxy; simpa using hxy) List.nodup_range
  exact (hp.nodup_iff).mpr hrng

/-! ### The inverse: a flat filling gives a standard Young tableau -/

variable {l : List ℕ}

/-- The semistandard Young tableau reshaped from a flat standard filling `a`. -/
def listToSsyt (hl : List.Sorted (· ≥ ·) l) (a : List ℕ)
    (hstd : isStdFilling l a = true) (hlen : a.length = l.sum) :
    SemistandardYoungTableau (YoungDiagram.ofRowLens l hl) where
  entry := entryFn l a
  row_weak' := by
    intro i j1 j2 hj hmem
    rw [YoungDiagram.mem_ofRowLens] at hmem
    obtain ⟨hi, hj2⟩ := hmem
    exact le_of_lt (isStdFilling_row l a hstd hlen i j1 j2 hi hj hj2)
  col_strict' := by
    intro i1 i2 j hi hmem
    rw [YoungDiagram.mem_ofRowLens] at hmem
    obtain ⟨hi2, hj⟩ := hmem
    exact isStdFilling_col l a hstd hlen hl i1 i2 j hi hi2 hj
  zeros' := by
    intro i j hmem
    rw [YoungDiagram.mem_ofRowLens] at hmem
    push_neg at hmem
    by_cases hi : i < l.length
    · exact entryFn_zero_of_col l a i j hi (hmem hi)
    · exact entryFn_zero_of_row l a i j (by omega)

/-- The standard Young tableau reshaped from a flat standard filling `a` (a permutation of
`[1,…,∑l]`): its entry map bijects the cells onto `{1,…,∑l}`. -/
def listToSYT (hl : List.Sorted (· ≥ ·) l) (a : List ℕ)
    (hp : a.Perm ((List.range l.sum).map (· + 1))) (hstd : isStdFilling l a = true) :
    QOU.Mathlib.StandardYoungTableau (YoungDiagram.ofRowLens l hl) where
  toSsyt := listToSsyt hl a hstd (hp.length_eq.trans (by simp))
  bijOn := by
    set μ := YoungDiagram.ofRowLens l hl with hμ
    have hlen : a.length = l.sum := hp.length_eq.trans (by simp)
    have hcard : μ.cells.card = l.sum := QOU.Mathlib.SYTEnum.card_cells_ofRowLens l hl
    set f : ℕ × ℕ → ℕ := fun c => (listToSsyt hl a hstd hlen).entry c.1 c.2 with hf
    -- entry on a cell equals a[idx]
    have hentry : ∀ i j, (hi : i < l.length) → (hj : j < l[i]'hi) →
        f (i, j) = a[idx l i j]'(by rw [hlen]; exact idx_lt_sum l i j hi hj) := by
      intro i j hi hj; exact entryFn_eq_a_idx l a i j hi hj hlen
    -- MapsTo
    have hmaps : Set.MapsTo f (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
      intro c hc
      rw [Finset.mem_coe, YoungDiagram.mem_cells, hμ, YoungDiagram.mem_ofRowLens] at hc
      obtain ⟨hi, hj⟩ := hc
      rw [Set.mem_Icc, hcard, hentry c.1 c.2 hi hj]
      exact a_getElem_mem_Icc l a hp _ _
    -- InjOn
    have hinj : Set.InjOn f (μ.cells : Set (ℕ × ℕ)) := by
      intro c1 hc1 c2 hc2 heq
      rw [Finset.mem_coe, YoungDiagram.mem_cells, hμ, YoungDiagram.mem_ofRowLens] at hc1 hc2
      obtain ⟨hi1, hj1⟩ := hc1
      obtain ⟨hi2, hj2⟩ := hc2
      rw [hentry c1.1 c1.2 hi1 hj1, hentry c2.1 c2.2 hi2 hj2] at heq
      have hidx : idx l c1.1 c1.2 = idx l c2.1 c2.2 :=
        (List.Nodup.getElem_inj_iff (a_nodup l a hp)).mp heq
      obtain ⟨h1, h2⟩ := idx_injOn l c1.1 c1.2 c2.1 c2.2 hi1 hj1 hi2 hj2 hidx
      exact Prod.ext h1 h2
    -- SurjOn via Finset double-counting (inj + card ⇒ surj on equal-card finsets)
    have hsurj : Set.SurjOn f (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
      rw [show (Set.Icc 1 μ.cells.card) = (↑(Finset.Icc 1 μ.cells.card) : Set ℕ) by
        simp [Finset.coe_Icc]]
      intro b hb
      simp only [Finset.coe_Icc, Set.mem_Icc] at hb
      have hmaps' : ∀ c ∈ μ.cells, f c ∈ Finset.Icc 1 μ.cells.card := by
        intro c hc
        have : c ∈ (μ.cells : Set (ℕ × ℕ)) := by rw [Finset.mem_coe]; exact hc
        have := hmaps this
        rw [Set.mem_Icc] at this
        simp only [Finset.mem_Icc]; exact this
      have hinj' : ∀ c1 ∈ μ.cells, ∀ c2 ∈ μ.cells, f c1 = f c2 → c1 = c2 := by
        intro c1 hc1 c2 hc2 heq
        exact hinj (by rw [Finset.mem_coe]; exact hc1) (by rw [Finset.mem_coe]; exact hc2) heq
      have hcardle : (Finset.Icc 1 μ.cells.card).card ≤ μ.cells.card := by
        rw [Nat.card_Icc]; omega
      have := Finset.surj_on_of_inj_on_of_card_le (s := μ.cells)
        (t := Finset.Icc 1 μ.cells.card) (fun c _ => f c) (fun c hc => hmaps' c hc)
        (fun c1 c2 h1 h2 he => hinj' c1 h1 c2 h2 he) hcardle b (by
          simp only [Finset.mem_Icc]; exact hb)
      obtain ⟨c, hc, hce⟩ := this
      exact ⟨c, by rw [Finset.mem_coe]; exact hc, hce.symm⟩
    exact ⟨hmaps, hinj, hsurj⟩

/-! ### The forward map: a standard Young tableau gives a flat filling -/

/-- Reshaping `chunk` is a left inverse of flattening rows of the right lengths. -/
theorem chunk_flatten (l : List ℕ) (rs : List (List ℕ)) (h : rs.map (·.length) = l) :
    chunk l rs.flatten = rs := by
  induction rs generalizing l with
  | nil => simp at h; subst h; simp [chunk]
  | cons r rest ih =>
    cases l with
    | nil => simp at h
    | cons len ls =>
      simp only [List.map_cons, List.cons.injEq] at h
      obtain ⟨hlen, hrest⟩ := h
      simp only [List.flatten_cons, chunk]
      rw [List.take_append_of_le_length (by omega), List.take_of_length_le (by omega)]
      rw [List.drop_append_of_le_length (by omega), List.drop_of_length_le (by omega),
        List.nil_append]
      rw [ih ls hrest]

/-- Row `i` of the flatten is `[e i 0, …, e i (l[i]-1)]`. -/
def rowsOf (l : List ℕ) (e : ℕ → ℕ → ℕ) : List (List ℕ) :=
  (List.finRange l.length).map (fun i => (List.range (l.get i)).map (e i.val))

/-- **Row-major flatten** of an entry map `e` over shape `l`. -/
def sytToList (l : List ℕ) (e : ℕ → ℕ → ℕ) : List ℕ := (rowsOf l e).flatten

theorem rowsOf_map_length (l : List ℕ) (e : ℕ → ℕ → ℕ) :
    (rowsOf l e).map (·.length) = l := by
  unfold rowsOf
  rw [List.map_map]
  have : ((fun x => x.length) ∘ fun i : Fin l.length => (List.range (l.get i)).map (e i.val))
      = fun i : Fin l.length => l.get i := by funext i; simp
  rw [this, List.finRange_map_get]

theorem chunk_sytToList (l : List ℕ) (e : ℕ → ℕ → ℕ) :
    chunk l (sytToList l e) = rowsOf l e :=
  chunk_flatten l (rowsOf l e) (rowsOf_map_length l e)

theorem sytToList_length (l : List ℕ) (e : ℕ → ℕ → ℕ) : (sytToList l e).length = l.sum := by
  unfold sytToList
  rw [List.length_flatten, rowsOf_map_length]

/-- **Entry roundtrip**: reshaping the flatten recovers the original entry map on cells. -/
theorem entryFn_sytToList (l : List ℕ) (e : ℕ → ℕ → ℕ) (i j : ℕ) (hi : i < l.length)
    (hj : j < l[i]'hi) : entryFn l (sytToList l e) i j = e i j := by
  unfold entryFn
  rw [chunk_sytToList]
  have hrow : (rowsOf l e).getD i [] = (List.range (l[i]'hi)).map (e i) := by
    unfold rowsOf
    rw [getD_of_lt _ (by rw [List.length_map, List.length_finRange]; exact hi)]
    rw [List.getElem_map, List.getElem_finRange]; simp
  rw [hrow, getD_of_lt _ (by rw [List.length_map, List.length_range]; exact hj)]
  rw [List.getElem_map, List.getElem_range]

/-! ### Reverse: building `isStdFilling` from entry-level row/column strictness -/

/-- Row `i` of `chunk l a` is `[entry i 0, …, entry i (l[i]-1)]` (given `a.length = ∑l`). -/
theorem chunk_row_eq_map (l a : List ℕ) (i : ℕ) (hi : i < l.length) (hlen : a.length = l.sum) :
    (chunk l a).getD i [] = (List.range (l[i]'hi)).map (entryFn l a i) := by
  apply List.ext_getElem
  · rw [chunk_row_length l a i hi hlen, List.length_map, List.length_range]
  · intro k hk1 _
    rw [chunk_row_length l a i hi hlen] at hk1
    rw [List.getElem_map, List.getElem_range, entryFn_eq_row_getElem l a i k hi hk1 hlen]

/-- `(range n).map f` is `strictInc` when `f` is strictly monotone on `[0,n)`. -/
theorem strictInc_map_range (n : ℕ) (f : ℕ → ℕ)
    (hf : ∀ j1 j2, j1 < j2 → j2 < n → f j1 < f j2) :
    strictInc ((List.range n).map f) = true := by
  rw [strictInc_iff_chain, List.isChain_iff_get]
  intro k hk
  simp only [List.length_map, List.length_range] at hk
  rw [List.get_eq_getElem, List.get_eq_getElem, List.getElem_map, List.getElem_map,
    List.getElem_range, List.getElem_range]
  exact hf k (k + 1) (by omega) (by omega)

/-- `colsOK` from a per-adjacent-pair column inequality. -/
theorem colsOK_of (rows : List (List ℕ))
    (h : ∀ i (hi : i + 1 < rows.length) j
      (hj2 : j < (rows[i + 1]'hi).length) (hj1 : j < (rows[i]'(by omega)).length),
      (rows[i]'(by omega))[j]'hj1 < (rows[i + 1]'hi)[j]'hj2) :
    colsOK rows = true := by
  induction rows with
  | nil => rfl
  | cons r1 rest ih =>
    cases rest with
    | nil => rfl
    | cons r2 rest' =>
      simp only [colsOK, Bool.and_eq_true]
      refine ⟨?_, ?_⟩
      · rw [List.all_eq_true]
        intro p hp
        obtain ⟨k, hk, hpe⟩ := List.mem_iff_getElem.mp hp
        rw [List.length_zip] at hk
        have h0 := h 0 (by simp) k (by simpa using (by omega : k < r2.length))
          (by simpa using (by omega : k < r1.length))
        simp only [List.getElem_cons_zero, List.getElem_cons_succ] at h0
        rw [List.getElem_zip] at hpe
        rw [← hpe]; simpa using h0
      · apply ih
        intro i hi j hj2 hj1
        have := h (i + 1) (by simpa using hi) j (by simpa using hj2) (by simpa using hj1)
        simpa using this

/-- **Reverse of `isStdFilling_row`/`adjcol`.** A flat list whose reshaped rows are strictly
increasing and whose adjacent columns are strictly increasing is a standard filling. -/
theorem isStdFilling_of_entry (l a : List ℕ) (hlen : a.length = l.sum)
    (hrow : ∀ i j1 j2, (hi : i < l.length) → j1 < j2 → j2 < l[i]'hi →
      entryFn l a i j1 < entryFn l a i j2)
    (hcol : ∀ i j, (hi : i + 1 < l.length) → j < l[i + 1]'hi →
      entryFn l a i j < entryFn l a (i + 1) j) :
    isStdFilling l a = true := by
  unfold isStdFilling
  rw [Bool.and_eq_true]
  refine ⟨?_, ?_⟩
  · rw [List.all_eq_true]
    intro r hr
    obtain ⟨i, hi, hre⟩ := List.mem_iff_getElem.mp hr
    rw [chunk_length] at hi
    have hr_eq : r = (List.range (l[i]'hi)).map (entryFn l a i) := by
      rw [← hre, ← getD_of_lt (chunk l a) (by rw [chunk_length]; exact hi) []]
      exact chunk_row_eq_map l a i hi hlen
    rw [hr_eq]
    exact strictInc_map_range _ _ (fun j1 j2 hj hj2 => hrow i j1 j2 hi hj hj2)
  · apply colsOK_of
    intro i hi j hj2 hj1
    rw [chunk_length] at hi
    have hi0 : i < l.length := by omega
    have hrl0 : ((chunk l a)[i]'(by omega)).length = l[i]'hi0 := by
      rw [← getD_of_lt (chunk l a) (by omega) []]; exact chunk_row_length l a i hi0 hlen
    have hrl1 : ((chunk l a)[i + 1]'(by rw [chunk_length]; exact hi)).length = l[i + 1]'hi := by
      rw [← getD_of_lt (chunk l a) (by rw [chunk_length]; exact hi) []]
      exact chunk_row_length l a (i + 1) hi hlen
    have hj2' : j < l[i + 1]'hi := by rw [← hrl1]; exact hj2
    have hcolfact := hcol i j hi hj2'
    have e0 : ((chunk l a)[i]'(by omega))[j]'hj1 = entryFn l a i j := by
      rw [entryFn_eq_row_getElem l a i j hi0 (by rw [hrl0] at hj1; exact hj1) hlen]
      congr 1
      rw [getD_of_lt (chunk l a) (by omega) []]
    have e1 : ((chunk l a)[i + 1]'(by rw [chunk_length]; exact hi))[j]'hj2
        = entryFn l a (i + 1) j := by
      rw [entryFn_eq_row_getElem l a (i + 1) j hi hj2' hlen]
      congr 1
      rw [getD_of_lt (chunk l a) (by rw [chunk_length]; exact hi) []]
    rw [e0, e1]; exact hcolfact

end QOU.Mathlib.SYTEnum
