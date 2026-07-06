import QOU.Mathlib.SYTHookFormulaBeta
import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# QOU.Mathlib.SYTHookFormulaBetaProd — wiring the per-row beta product into the corpus `prodHooks`

`SYTHookFormulaBeta` proved, self-contained, the per-row Frame–Robinson–Thrall hook product
`rowHookProd a t · betaGapProd a t = (a + |t|)!`.  This file connects `rowHookProd` to the corpus
`QOU.BraidKnot.IdentityI.prodHooks` and assembles the **full divisor-free Frame–Robinson–Thrall hook
product**:

    prodHooks l · (∏_i betaGapProd (l[i]) (l.drop (i+1))) = ∏_i (l[i] + (l.drop (i+1)).length)!
                                                          = ∏_i β_i!

(`β_i = l[i] + (k−1−i)`), i.e. `∏_c h_λ(c) = (∏_i β_i!) / ∏_{i<j}(β_i − β_j)` cleared of the
Vandermonde denominator.  This is the hook-side identity (i) of the beta-number route to the general
HLF, sorry-free for every weakly-decreasing positive partition.

Pure `ℕ` combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBeta

open QOU.BraidKnot.IdentityI (colLen prodHooks)

/-- `cnt` (this file's leg count) and the corpus `colLen` are the same `filter`-length. -/
theorem cnt_eq_colLen (t : List ℕ) (j : ℕ) : cnt t j = colLen t j := rfl

/-- **Leg simplification (sorry-free).** For a weakly-decreasing `l`, `i < l.length` and `j < l[i]`,
every row `0,…,i` reaches column `j` (its length is `≥ l[i] > j`), so
`colLen l j = (i + 1) + cnt (l.drop (i+1)) j`.  Hence the corpus leg `colLen l j − i − 1` is exactly
the tail count `cnt (l.drop (i+1)) j`. -/
theorem colLen_eq_succ_add_cnt_drop (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (i j : ℕ)
    (hi : i < l.length) (hj : j < l.getD i 0) :
    colLen l j = (i + 1) + cnt (l.drop (i + 1)) j := by
  -- colLen l j = (l.filter (j < ·)).length; split l = l.take (i+1) ++ l.drop (i+1)
  unfold colLen cnt
  conv_lhs => rw [← List.take_append_drop (i + 1) l]
  rw [List.filter_append, List.length_append]
  congr 1
  -- the (i+1)-prefix is entirely > j: each of rows 0..i has length ≥ l[i] > j
  have hpre : ∀ p ∈ l.take (i + 1), j < p := by
    intro p hp
    obtain ⟨k, hk, hke⟩ := List.mem_iff_getElem.mp hp
    rw [List.length_take] at hk
    have hk' : k < i + 1 := lt_of_lt_of_le hk (min_le_left _ _)
    have hkl : k < l.length := by omega
    rw [List.getElem_take] at hke
    -- l[k] ≥ l[i] (k ≤ i, antitone) and l[i] > j
    have hki : l.getD i 0 ≤ l.getD k 0 :=
      QOU.BraidKnot.IdentityI.getD_antitone l hl (by omega : k ≤ i)
    have hkv : l.getD k 0 = l[k] := by
      rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hkl, Option.getD_some]
    rw [← hke, ← hkv]
    omega
  rw [List.filter_eq_self.mpr (fun p hp => by simp [hpre p hp]),
    List.length_take]
  rw [Nat.min_eq_left (by omega : i + 1 ≤ l.length)]

/-- **Row-`i` factor of `prodHooks` as a `rowHookProd` (sorry-free).** For a weakly-decreasing `l` and
`i < l.length`, the row-`i` hook product appearing in `prodHooks l` equals
`rowHookProd (l.getD i 0) (l.drop (i+1))`. -/
theorem prodHooks_row_eq_rowHookProd (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (i : ℕ)
    (hi : i < l.length) :
    ((List.range (l.getD i 0)).map
        (fun j => ((l.getD i 0 - j) + (colLen l j - i) - 1))).prod
      = rowHookProd (l.getD i 0) (l.drop (i + 1)) := by
  unfold rowHookProd
  congr 1
  apply List.map_congr_left
  intro j hj
  rw [List.mem_range] at hj
  rw [colLen_eq_succ_add_cnt_drop l hl i j hi hj]
  -- (l[i] - j) + ((i+1) + cnt - i) - 1 = (l[i] - j) + cnt
  omega

/-- **`prodHooks` as a product of per-row `rowHookProd` (sorry-free).** For a weakly-decreasing `l`,

    prodHooks l = ∏_{i<|l|} rowHookProd (l[i]) (l.drop (i+1)).

Each outer factor of the corpus `prodHooks` is rewritten by `prodHooks_row_eq_rowHookProd`. -/
theorem prodHooks_eq_prod_rowHookProd (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    prodHooks l
      = ((List.range l.length).map
          (fun i => rowHookProd (l.getD i 0) (l.drop (i + 1)))).prod := by
  unfold prodHooks
  congr 1
  apply List.map_congr_left
  intro i hi
  rw [List.mem_range] at hi
  exact prodHooks_row_eq_rowHookProd l hl i hi

/-- The tail of row `i` is weakly-decreasing (a suffix of a weakly-decreasing list). -/
theorem drop_sorted (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (i : ℕ) :
    List.Sorted (· ≥ ·) (l.drop (i + 1)) :=
  hl.sublist (List.drop_sublist _ _)

/-- Every part of the tail of row `i` is `≤ l[i]` (weakly-decreasing). -/
theorem drop_le_getD (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (i : ℕ) (hi : i < l.length) :
    ∀ p ∈ l.drop (i + 1), p ≤ l.getD i 0 := by
  intro p hp
  obtain ⟨k, hk, hke⟩ := List.mem_iff_getElem.mp hp
  rw [List.length_drop] at hk
  rw [List.getElem_drop] at hke
  have hidx : i < (i + 1) + k := by omega
  have hlen : (i + 1) + k < l.length := by omega
  have := QOU.BraidKnot.IdentityI.getD_antitone l hl (le_of_lt hidx)
  have hkv : l.getD ((i + 1) + k) 0 = l[(i + 1) + k] := by
    rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hlen, Option.getD_some]
  rw [← hke, ← hkv]; exact this

/-- **Full Frame–Robinson–Thrall hook product, divisor-free (sorry-free).** For every
weakly-decreasing partition `l`,

    prodHooks l · (∏_{i<|l|} betaGapProd (l[i]) (l.drop (i+1)))
      = ∏_{i<|l|} (l[i] + (l.drop (i+1)).length)!  =  ∏_i β_i!.

This is the hook-side identity (i) of the beta-number route to the general HLF:
`∏_c h_λ(c) = (∏_i β_i!) / ∏_{i<j}(β_i − β_j)`, cleared of the Vandermonde denominator.  Sorry-free
for every weakly-decreasing positive partition. -/
theorem prodHooks_mul_betaGapProd (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    prodHooks l *
        ((List.range l.length).map
          (fun i => betaGapProd (l.getD i 0) (l.drop (i + 1)))).prod
      = ((List.range l.length).map
          (fun i => Nat.factorial (l.getD i 0 + (l.drop (i + 1)).length))).prod := by
  rw [prodHooks_eq_prod_rowHookProd l hl, list_range_map_prod, list_range_map_prod,
    list_range_map_prod, ← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i hi
  rw [Finset.mem_range] at hi
  exact rowHookProd_mul_betaGapProd (l.getD i 0) (l.drop (i + 1))
    (drop_sorted l hl i) (drop_le_getD l hl i hi)

end QOU.Mathlib.SYTBeta
