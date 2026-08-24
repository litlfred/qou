import QOU.Mathlib.SYTHookFormulaBetaProdMonoid

/-!
# QOU.Mathlib.SYTBetaZeroPadding — padding a partition with empty rows

**The trap this file exists for.**  `SYTBeta.betaNum l i = l[i] + (|l| − 1 − i)` measures the
β-numbers against `|l|`, the number of **nonzero** rows.  The β-numbers of the level-`r` principal
specialisation are measured against **`r`**, the number of variables: the partition is padded with
`r − |l|` empty rows first.  The two disagree by the constant `r − |l|` on every row, and — worse —
the padded version has extra rows `β = r−1−|l|, …, 0` that the unpadded one does not have at all.

Differences `β_i − β_j` between real rows are unaffected, so the *Vandermonde* is the same up to the
new rows; but nothing else transfers for free, and a proof that quietly uses `|l|` where `r` belongs
is wrong in a way no type error catches.

What *does* transfer for free is the hook side, and that is what this file proves: empty rows
contribute no cells and are counted by no column, so

`prodHooksF f (l ++ replicate m 0) = prodHooksF f l`.

Pad first, then apply the β-number machinery at `r`.

## Base ring (§7c)

Generic `[CommMonoid M]`.  Pure `ℕ` combinatorics otherwise.

LaTeX label: `lem:syt-beta-zero-padding`
-/

namespace QOU.Mathlib.SYTBeta

open QOU.BraidKnot.IdentityI (colLen)

variable {M : Type*} [CommMonoid M]

/-- Out of range, `getD` is the default. -/
theorem getD_eq_zero_of_le {l : List ℕ} {i : ℕ} (hi : l.length ≤ i) : l.getD i 0 = 0 := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none hi]
  rfl

/-- Padding with empty rows changes no row length — including the padded positions, where both
sides are `0`. -/
theorem getD_append_replicate_zero (l : List ℕ) (m i : ℕ) :
    (l ++ List.replicate m 0).getD i 0 = l.getD i 0 := by
  rcases lt_or_ge i l.length with hi | hi
  · rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD,
      List.getElem?_append_left hi]
  · rw [getD_eq_zero_of_le hi, List.getD_eq_getElem?_getD,
      List.getElem?_append_right hi, List.getElem?_replicate]
    split_ifs <;> rfl

/-- Padding with empty rows changes no column length: `colLen` counts parts `> j`, and `0` is never
`> j`. -/
theorem colLen_append_replicate_zero (l : List ℕ) (m j : ℕ) :
    colLen (l ++ List.replicate m 0) j = colLen l j := by
  unfold colLen
  rw [List.filter_append, List.length_append]
  have : (List.replicate m 0).filter (fun p => decide (j < p)) = [] := by
    rw [List.filter_eq_nil_iff]
    intro p hp
    rw [List.eq_of_mem_replicate hp]
    simp
  rw [this]
  simp

/-- **Empty rows do not change the hook product.**  Pad the partition out to `r` rows, then apply the
β-number machinery at `r` — the hook side is unaffected. -/
theorem prodHooksF_append_replicate_zero (f : ℕ → M) (l : List ℕ) (m : ℕ) :
    prodHooksF f (l ++ List.replicate m 0) = prodHooksF f l := by
  unfold prodHooksF
  rw [list_range_map_prod', list_range_map_prod', List.length_append,
    List.length_replicate, Finset.prod_range_add]
  have hpad : ∀ x ∈ Finset.range m,
      ((List.range ((l ++ List.replicate m 0).getD (l.length + x) 0)).map
        (fun j => f (((l ++ List.replicate m 0).getD (l.length + x) 0 - j)
          + (colLen (l ++ List.replicate m 0) j - (l.length + x)) - 1))).prod = 1 := by
    intro x _
    rw [getD_append_replicate_zero, getD_eq_zero_of_le (by omega)]
    simp
  rw [Finset.prod_congr rfl hpad, Finset.prod_const_one, mul_one]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [getD_append_replicate_zero]
  congr 1
  refine List.map_congr_left fun j _ => ?_
  rw [colLen_append_replicate_zero]

end QOU.Mathlib.SYTBeta
