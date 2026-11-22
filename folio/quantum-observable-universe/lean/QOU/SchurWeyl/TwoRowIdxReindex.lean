/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.WtraceRadicalSemisimple
import QOU.SchurWeyl.MarkovConventionD

/-!
# Reindexing the at-most-two-row partitions by second-row length

`WtraceRadicalSemisimple.finrank_traceQuot` sums over `TwoRowIdx n`, the at-most-two-row
partitions of `n + 1`.  `QOU.Mathlib.TwoRowDimCatalan.dimHLF_two_row_sq_sum` sums over
`Finset.range (n / 2 + 1)`, indexed by the **second-row length**.  This file supplies the
bijection between the two index sets, so the two sums can be compared.

## Why this is worth its own file

It is bean `qou-7vht` item 2, and its point is subtractive: with it, the only thing standing
between `finrank_traceQuot` and `catalan (n+1)` is the **hook length formula at general `n`** —
absent from Mathlib, and proved in this corpus only for `n ≤ 4` (`shapesLE4`, by `decide`) plus
`n = 5`.  Before it there were two gaps and it was easy to mistake the bounded one for the hard
one; after it there is one, and it is named.

## Nothing here closes that gap

🛑 The bijection is finite combinatorics and says nothing about tableau counts.  It does not
prove `finrank_traceQuot = catalan (n+1)`, and the sum it produces is still over
`Fintype.card (StandardYoungTableau …)`, not over `dimHLF`.

-- Ref: [leitner2026] beans qou-7vht, qou-7wf6, qou-8iru.
-/

namespace QOU.SchurWeyl.TwoRowIdxReindex

open QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep
open QOU.SchurWeyl.WtraceRadicalIdeal QOU.SchurWeyl.WtraceRadicalSemisimple
open QOU.QBeta.MarkovTraceQuotient

variable {m k : ℕ}

/-! ## The third row of a `twoRow` is empty -/

/-- **`twoRow` has no third row.**  Not in `OcneanuWeightBranching`, which stops at
`rowLen_twoRow_one`; three lines off `mem_twoRow`. -/
theorem rowLen_twoRow_two (h : k ≤ m) : (twoRow m k h).rowLen 2 = 0 := by
  by_contra hne
  have hmem : (2, 0) ∈ twoRow m k h :=
    YoungDiagram.mem_iff_lt_rowLen.mpr (by omega)
  rw [mem_twoRow] at hmem
  omega

/-- **`twoRow` depends only on its two row lengths.**  The `k ≤ m` argument is a `Prop`, so
proof irrelevance closes it after `subst`; needed because `rw` cannot rewrite inside that
argument (the motive stops being type correct). -/
theorem twoRow_congr {m m' k k' : ℕ} (h : k ≤ m) (h' : k' ≤ m') (hm : m = m') (hk : k = k') :
    twoRow m k h = twoRow m' k' h' := by
  subst hm; subst hk; rfl

/-! ## The two row lengths of an at-most-two-row partition of `n+1` -/

/-- The two row lengths sum to `n + 1`.  `eq_twoRow_of_rowLen_two_eq_zero` turns the shape into
a `twoRow`, and `card_twoRow` then reads the cell count off it. -/
theorem rowLen_add {n : ℕ} (lam : TwoRowIdx n) :
    (partitionShape lam.1).rowLen 0 + (partitionShape lam.1).rowLen 1 = n + 1 := by
  have hc : (partitionShape lam.1).cells.card = n + 1 := partitionShape_card_succ lam.1
  rw [eq_twoRow_of_rowLen_two_eq_zero _ lam.2, card_twoRow] at hc
  exact hc

/-- The second row is at most half of `n + 1` — it is the shorter of two rows summing to
`n + 1`. -/
theorem secondRow_le {n : ℕ} (lam : TwoRowIdx n) :
    (partitionShape lam.1).rowLen 1 ≤ (n + 1) / 2 := by
  have h1 := rowLen_add lam
  have h2 : (partitionShape lam.1).rowLen 1 ≤ (partitionShape lam.1).rowLen 0 :=
    YoungDiagram.rowLen_anti _ 0 1 (by omega)
  omega

/-! ## The inverse: a second-row length determines the partition -/

/-- **The at-most-two-row partition of `n + 1` with second row `k`.**  Obtained from
`exists_partitionShape_eq` on `twoRow (n + 1 - k) k`; the choice is harmless because
`partitionShape` is injective, which is what `ofSecondRow_secondRow` below spends. -/
noncomputable def ofSecondRow (n k : ℕ) (hk : 2 * k ≤ n + 1) : TwoRowIdx n :=
  ⟨(exists_partitionShape_eq (twoRow (n + 1 - k) k (by omega))
      (by rw [card_twoRow]; omega)).choose,
   by
     rw [(exists_partitionShape_eq (twoRow (n + 1 - k) k (by omega))
       (by rw [card_twoRow]; omega)).choose_spec]
     exact rowLen_twoRow_two _⟩

@[simp] theorem shape_ofSecondRow (n k : ℕ) (hk : 2 * k ≤ n + 1) :
    partitionShape (ofSecondRow n k hk).1 = twoRow (n + 1 - k) k (by omega) :=
  (exists_partitionShape_eq (twoRow (n + 1 - k) k (by omega))
    (by rw [card_twoRow]; omega)).choose_spec

@[simp] theorem secondRow_ofSecondRow (n k : ℕ) (hk : 2 * k ≤ n + 1) :
    (partitionShape (ofSecondRow n k hk).1).rowLen 1 = k := by
  rw [shape_ofSecondRow, rowLen_twoRow_one]

/-- The round trip the other way: a partition is recovered from its second-row length.  This is
where `partitionShape_injective` is spent, and it is why the `choose` above is harmless. -/
theorem ofSecondRow_secondRow {n : ℕ} (lam : TwoRowIdx n) :
    ofSecondRow n ((partitionShape lam.1).rowLen 1)
        (by have := secondRow_le lam; omega) = lam := by
  refine Subtype.ext (partitionShape_injective ?_)
  rw [shape_ofSecondRow]
  refine (twoRow_congr _ _ ?_ rfl).trans (eq_twoRow_of_rowLen_two_eq_zero _ lam.2).symm
  have := rowLen_add lam
  omega

/-! ## The bijection -/

/-- **`TwoRowIdx n ≃ Fin ((n+1)/2 + 1)`**, by second-row length.

Forward is "read off the second row"; backward is `ofSecondRow`.  The two round trips are
`secondRow_ofSecondRow` and `ofSecondRow_secondRow`, the second of which is where
`partitionShape_injective` is spent. -/
noncomputable def twoRowIdxEquiv (n : ℕ) : TwoRowIdx n ≃ Fin ((n + 1) / 2 + 1) where
  toFun lam := ⟨(partitionShape lam.1).rowLen 1, by have := secondRow_le lam; omega⟩
  invFun k := ofSecondRow n k.1 (by have := k.2; omega)
  left_inv lam := ofSecondRow_secondRow lam
  right_inv k := Fin.ext (by simp [rowLen_twoRow_one])

@[simp] theorem twoRowIdxEquiv_apply {n : ℕ} (lam : TwoRowIdx n) :
    (twoRowIdxEquiv n lam : ℕ) = (partitionShape lam.1).rowLen 1 := rfl

/-! ## The dimension, as a total function of the two row lengths -/

/-- The standard-tableau count of `twoRow m k`, extended by `0` off `k ≤ m` so that it is a
total function of `(m, k)` and can be summed over a bare `Finset.range`. -/
noncomputable def twoRowDim (m k : ℕ) : ℕ :=
  if h : k ≤ m then numStandardYoungTableaux (twoRow m k h) else 0

theorem twoRowDim_eq (h : k ≤ m) :
    twoRowDim m k = numStandardYoungTableaux (twoRow m k h) := by
  rw [twoRowDim, dif_pos h]

/-! ## The reindexed dimension -/

/-- **`finrank_traceQuot`, reindexed by second-row length.**

    finrank R (H_n(q)/rad(wtrace)) = Σ_{k ≤ ⌊(n+1)/2⌋} (#SYT (n+1−k, k))²

the shape `QOU.Mathlib.TwoRowDimCatalan.dimHLF_two_row_sq_sum` sums in, so the two are now
directly comparable.

🛑 **This is still a tableau COUNT, not `dimHLF`.**  Comparing it to `catalan (n+1)` needs the
hook length formula at general `n`, which is absent from Mathlib and proved in this corpus only
for `n ≤ 4` plus `n = 5`.  That is the single remaining gap, and it is the whole point of this
file that it is now single. -/
theorem finrank_traceQuot_eq_range_sum {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    Module.finrank ℝ (TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n))
      = ∑ k ∈ Finset.range ((n + 1) / 2 + 1), twoRowDim (n + 1 - k) k ^ 2 := by
  rw [finrank_traceQuot hq0 hq2 hq21 hgen n,
    ← Fin.sum_univ_eq_sum_range (fun k => twoRowDim (n + 1 - k) k ^ 2) ((n + 1) / 2 + 1)]
  refine Fintype.sum_equiv (twoRowIdxEquiv n) _ _ ?_
  intro lam
  have hle : (partitionShape lam.1).rowLen 1 ≤ n + 1 - (partitionShape lam.1).rowLen 1 := by
    have := rowLen_add lam
    have h2 : (partitionShape lam.1).rowLen 1 ≤ (partitionShape lam.1).rowLen 0 :=
      YoungDiagram.rowLen_anti _ 0 1 (by omega)
    omega
  have hshape : twoRow (n + 1 - (partitionShape lam.1).rowLen 1)
      ((partitionShape lam.1).rowLen 1) hle = partitionShape lam.1 := by
    refine (twoRow_congr _ _ ?_ rfl).trans (eq_twoRow_of_rowLen_two_eq_zero _ lam.2).symm
    have := rowLen_add lam
    omega
  have hnum : numStandardYoungTableaux (partitionShape lam.1)
      = Fintype.card (StandardYoungTableau (partitionShape lam.1)) :=
    Nat.card_eq_fintype_card
  rw [twoRowIdxEquiv_apply, twoRowDim_eq hle, hshape, hnum, sq]


/-- **The reindexed sum is strictly positive**, so the identity above is not `0 = 0`.
Inherited from `finrank_traceQuot_pos`, which in turn reuses `traceQuot_one_ne_zero`. -/
theorem range_sum_pos {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    0 < ∑ k ∈ Finset.range ((n + 1) / 2 + 1), twoRowDim (n + 1 - k) k ^ 2 := by
  rw [← finrank_traceQuot_eq_range_sum hq0 hq2 hq21 hgen n]
  exact finrank_traceQuot_pos hq0 hq2 hq21 hgen n

end QOU.SchurWeyl.TwoRowIdxReindex
