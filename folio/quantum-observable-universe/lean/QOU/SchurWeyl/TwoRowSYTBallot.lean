/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.TwoRowCorners
import QOU.Mathlib.YoungLatticeUpOperator
import QOU.Mathlib.BallotNumbers
import QOU.Mathlib.StandardYoungTableauBot
import QOU.Mathlib.TwoRowDimCatalan

/-!
# The two-row standard-tableau count is the ballot number

**Bean `qou-7vht` item 1**, on its narrowed target.  The goal is

    numStandardYoungTableaux (twoRow m k) = ballot (m + k) k

i.e. the **two-row** case of the hook length formula, not the general theorem.

## Why the two-row case suffices, and why it is much smaller

`QOU.Mathlib.TwoRowDimCatalan.dimHLF_two_row_eq_ballot` already identifies the
hook-length-formula *value* `dimHLF [n-k, k]` with `ballot n k`.  So identifying the genuine
tableau count with the same ballot number closes the gap between
`WtraceRadicalSemisimple.finrank_traceQuot` (a count) and `dimHLF_two_row_sq_sum` (formula
values) — **without** proving Frame–Robinson–Thrall in general, which is absent from Mathlib and
proved in this corpus only for `n ≤ 4` (by `decide`) plus `n = 5`.

## The route: a recursion, not a bijection

The textbook argument is a bijection with ballot sequences.  That is not the cheap route in
Lean, because the corpus already has the *branching rule* as a `Finset` sum
(`QOU.Mathlib.YoungLatticeUpOperator.branching_finset`) and `ballot` already has the matching
recursion (`ballot_succ_succ`).  So the whole content is:

1. evaluate `cornerCells (twoRow m k)` — two cells, one cell, or none;
2. identify the two corner-erased shapes as `twoRow (m-1) k` and `twoRow m (k-1)`;
3. induct, with `ballot_succ_succ` on the generic step.

The `k = m` boundary is where it could have gone wrong and does not: there `(0, m-1)` is **not**
a corner (the cell below it is present), so only one term survives — and on the `ballot` side
the term that must vanish is `ballot (2j+1) (j+1)`, which is exactly `ballot_boundary_zero`,
already proved for a different purpose.  Bean `qou-7wf6` noted that one lemma resolves both; this
is the second use.

-- Ref: [leitner2026] beans qou-7vht, qou-7wf6.
-/

namespace QOU.SchurWeyl.TwoRowSYTBallot

open QOU.Mathlib QOU.SchurWeyl
open QOU.BraidKnot.IdentityI (dimHLF)

variable {m k : ℕ}

/-! ## The removable corners of `twoRow m k`, as an explicit finset -/

/-- The removable corners of `twoRow m k`.  Mirrors `addableTwoRow`. -/
def cornerTwoRow (m k : ℕ) : Finset (ℕ × ℕ) :=
  (if k < m then {((0 : ℕ), m - 1)} else ∅) ∪ (if 0 < k then {((1 : ℕ), k - 1)} else ∅)

theorem mem_cornerTwoRow (r : ℕ × ℕ) :
    r ∈ cornerTwoRow m k ↔ (r = (0, m - 1) ∧ k < m) ∨ (r = (1, k - 1) ∧ 0 < k) := by
  unfold cornerTwoRow
  split_ifs <;> simp_all [Prod.ext_iff] <;> omega

theorem cornerCells_twoRow (h : k ≤ m) :
    cornerCells (twoRow m k h) = cornerTwoRow m k := by
  ext r
  rw [mem_cornerCells, isCornerCell_twoRow_iff h, mem_cornerTwoRow]

theorem sum_cornerTwoRow_expand {M : Type*} [AddCommMonoid M] (f : ℕ × ℕ → M) :
    ∑ r ∈ cornerTwoRow m k, f r
      = (if k < m then f (0, m - 1) else 0) + (if 0 < k then f (1, k - 1) else 0) := by
  unfold cornerTwoRow
  split_ifs <;>
    simp [Finset.sum_insert, Prod.ext_iff] <;> abel

/-! ## Erasing each corner gives the next `twoRow` -/

/-- Erasing the end of row 0 shortens row 0. -/
theorem eraseCornerOrSelf_twoRow_row0 (h : k ≤ m) (hkm : k < m) :
    eraseCornerOrSelf (twoRow m k h) (0, m - 1) = twoRow (m - 1) k (by omega) := by
  have hc : IsCornerCell (twoRow m k h) (0, m - 1) :=
    (isCornerCell_twoRow_iff h _).mpr (Or.inl ⟨rfl, hkm⟩)
  rw [eraseCornerOrSelf_of hc]
  ext c
  obtain ⟨i, j⟩ := c
  rw [show ((i, j) ∈ (eraseCorner (twoRow m k h) (0, m - 1) hc).cells)
      ↔ ((i, j) ∈ eraseCorner (twoRow m k h) (0, m - 1) hc) from Iff.rfl,
    mem_eraseCorner _ _ hc,
    show ((i, j) ∈ (twoRow (m - 1) k (by omega : k ≤ m - 1)).cells)
      ↔ ((i, j) ∈ twoRow (m - 1) k (by omega : k ≤ m - 1)) from Iff.rfl,
    mem_twoRow, mem_twoRow]
  simp only [ne_eq, Prod.mk.injEq, not_and]
  omega

/-- Erasing the end of row 1 shortens row 1. -/
theorem eraseCornerOrSelf_twoRow_row1 (h : k ≤ m) (hk0 : 0 < k) :
    eraseCornerOrSelf (twoRow m k h) (1, k - 1) = twoRow m (k - 1) (by omega) := by
  have hc : IsCornerCell (twoRow m k h) (1, k - 1) :=
    (isCornerCell_twoRow_iff h _).mpr (Or.inr ⟨rfl, hk0⟩)
  rw [eraseCornerOrSelf_of hc]
  ext c
  obtain ⟨i, j⟩ := c
  rw [show ((i, j) ∈ (eraseCorner (twoRow m k h) (1, k - 1) hc).cells)
      ↔ ((i, j) ∈ eraseCorner (twoRow m k h) (1, k - 1) hc) from Iff.rfl,
    mem_eraseCorner _ _ hc,
    show ((i, j) ∈ (twoRow m (k - 1) (by omega : k - 1 ≤ m)).cells)
      ↔ ((i, j) ∈ twoRow m (k - 1) (by omega : k - 1 ≤ m)) from Iff.rfl,
    mem_twoRow, mem_twoRow]
  simp only [ne_eq, Prod.mk.injEq, not_and]
  omega

/-! ## Successor forms

Everything below avoids `m - 1` and `k - 1`.  Truncated subtraction is the whole difficulty here:
`rw` needs a syntactic match, Lean normalises `n + 1 - 1` to `n` in the goal but not inside a
lemma instance, and the `k ≤ m` proof carried by `twoRow` makes the motive ill-typed when the
index is rewritten.  Restating in successor form removes all three at once. -/

theorem eraseCornerOrSelf_twoRow_row0_succ (M k : ℕ) (h : k ≤ M + 1) (hkm : k < M + 1) :
    eraseCornerOrSelf (twoRow (M + 1) k h) (0, M) = twoRow M k (by omega) := by
  simpa using eraseCornerOrSelf_twoRow_row0 h hkm

theorem eraseCornerOrSelf_twoRow_row1_succ (m j : ℕ) (h : j + 1 ≤ m) :
    eraseCornerOrSelf (twoRow m (j + 1) h) (1, j) = twoRow m j (by omega) := by
  simpa using eraseCornerOrSelf_twoRow_row1 h (Nat.succ_pos j)

/-! ## The three recursion cases

Stated as three separate theorems rather than one formula with `if`s: a branch that builds
`twoRow M k` needs the branch condition to supply `k ≤ M`, which an `ite` cannot give it. -/

/-- `twoRow 0 0` is the empty diagram. -/
theorem twoRow_zero_zero : twoRow 0 0 le_rfl = (⊥ : YoungDiagram) := by
  ext c
  obtain ⟨i, j⟩ := c
  rw [show ((i, j) ∈ (twoRow 0 0 le_rfl).cells) ↔ ((i, j) ∈ twoRow 0 0 le_rfl) from Iff.rfl,
    mem_twoRow]
  simp

/-- **One row, one tableau.** -/
theorem numSYT_twoRow_zero (m : ℕ) (h : 0 ≤ m) :
    numStandardYoungTableaux (twoRow m 0 h) = 1 := by
  induction m with
  | zero => rw [twoRow_zero_zero, numStandardYoungTableaux_bot]
  | succ n ih =>
      rw [branching_finset _ (by rw [card_twoRow]; omega), cornerCells_twoRow h,
        sum_cornerTwoRow_expand, if_pos (Nat.succ_pos n),
        if_neg (by omega : ¬ (0 : ℕ) < 0), add_zero]
      rw [show (n + 1 - 1 : ℕ) = n from rfl,
        eraseCornerOrSelf_twoRow_row0_succ n 0 h (Nat.succ_pos n)]
      exact ih (Nat.zero_le n)

/-- **`0 < k < m`: two corners.**  Successor form: `k = j + 1`, `m = M + 1`, `j + 1 ≤ M`. -/
theorem numSYT_twoRow_rec_lt (M j : ℕ) (hjM : j + 1 ≤ M) :
    numStandardYoungTableaux (twoRow (M + 1) (j + 1) (by omega))
      = numStandardYoungTableaux (twoRow M (j + 1) (by omega))
        + numStandardYoungTableaux (twoRow (M + 1) j (by omega)) := by
  rw [branching_finset _ (by rw [card_twoRow]; omega), cornerCells_twoRow (by omega : j + 1 ≤ M + 1),
    sum_cornerTwoRow_expand, if_pos (by omega : j + 1 < M + 1), if_pos (Nat.succ_pos j),
    show (M + 1 - 1 : ℕ) = M from rfl,
    show (j + 1 - 1 : ℕ) = j from rfl,
    eraseCornerOrSelf_twoRow_row0_succ M (j + 1) (by omega) (by omega),
    eraseCornerOrSelf_twoRow_row1_succ (M + 1) j (by omega)]

/-- **`k = m > 0`: only the row-1 corner.**  `(0, m-1)` is *not* removable here — the cell below
it is present — which is exactly what makes the boundary case work. -/
theorem numSYT_twoRow_rec_eq (j : ℕ) :
    numStandardYoungTableaux (twoRow (j + 1) (j + 1) le_rfl)
      = numStandardYoungTableaux (twoRow (j + 1) j (by omega)) := by
  rw [branching_finset _ (by rw [card_twoRow]; omega), cornerCells_twoRow le_rfl,
    sum_cornerTwoRow_expand, if_neg (by omega : ¬ j + 1 < j + 1), if_pos (Nat.succ_pos j),
    zero_add, show (j + 1 - 1 : ℕ) = j from rfl,
    eraseCornerOrSelf_twoRow_row1_succ (j + 1) j le_rfl]

/-! ## The identification -/

/-- **The two-row standard-tableau count IS the ballot number**, for every `k ≤ m`.

    #SYT (m, k) = ballot (m + k) k

Outer induction on `k`, inner induction on `m` from `k` upward (`Nat.le_induction`): the `k < m`
step needs the result at the *same* `k` with a smaller `m`, which an induction on `k` alone
cannot supply.

The two `ballot` facts consumed are exactly the two the corpus already had: `ballot_succ_succ`
for the generic step, and `ballot_boundary_zero` for the `k = m` boundary, where the term that
must vanish is `ballot (2j+1) (j+1)`. -/
theorem numSYT_twoRow_eq_ballot (m k : ℕ) (h : k ≤ m) :
    (numStandardYoungTableaux (twoRow m k h) : ℤ) = ballot (m + k) k := by
  induction k generalizing m with
  | zero => rw [numSYT_twoRow_zero m h, ballot_zero]; norm_num
  | succ j ihj =>
      induction m, h using Nat.le_induction with
      | base =>
          rw [numSYT_twoRow_rec_eq j, ihj (j + 1) (by omega)]
          have hbs := ballot_succ_succ (2 * j + 1) j
          have hbz := ballot_boundary_zero j
          rw [show (j + 1 + (j + 1) : ℕ) = 2 * j + 1 + 1 from by omega, hbs, hbz, zero_add,
            show (j + 1 + j : ℕ) = 2 * j + 1 from by omega]
      | succ M hjM ihM =>
          rw [numSYT_twoRow_rec_lt M j hjM]
          push_cast
          rw [ihM, ihj (M + 1) (by omega)]
          have hbs := ballot_succ_succ (M + j + 1) j
          rw [show (M + 1 + (j + 1) : ℕ) = M + j + 1 + 1 from by omega,
            show (M + (j + 1) : ℕ) = M + j + 1 from by omega,
            show (M + 1 + j : ℕ) = M + j + 1 from by omega, hbs]

/-- **The two-row tableau COUNT equals the hook-length-formula VALUE**, at general `m, k`.

This is the bridge the corpus was missing.  `dimHLF l := (sz l).factorial / prodHooks l` is the
hook length *formula*; `numStandardYoungTableaux μ := Nat.card (StandardYoungTableau μ)` is the
genuine *count*.  Frame–Robinson–Thrall — the theorem that the two agree for **every** shape — is
absent from Mathlib and is proved in this corpus only for `n ≤ 4` (by `decide`) plus `n = 5`.

For **two-row** shapes it needs none of that: both sides were already identified with the same
ballot number, one side in August (`QOU.Mathlib.dimHLF_two_row_eq_ballot`) and the other by
`numSYT_twoRow_eq_ballot` above, so composing the two identifications suffices at general `m, k`.

Cited by `QOU.Mathlib.TwoRowDimCatalan`'s module docstring, whose claim that
`dimHLF_two_row_sq_sum` is "a statement about actual standard-Young-tableau counts" is true
**because of this theorem** — before it, that file's `dimHLF` was a formula value with no proved
tie to any tableau count at general `n`.

-- Ref: [leitner2026] bean qou-7vht item 1. -/
theorem numSYT_twoRow_eq_dimHLF (m k : ℕ) (h : k ≤ m) :
    (numStandardYoungTableaux (twoRow m k h) : ℤ) = ((dimHLF [m, k] : ℕ) : ℤ) := by
  have hk2 : 2 * k ≤ m + k := by omega
  have hd := dimHLF_two_row_eq_ballot (m + k) k hk2
  rw [show m + k - k = m from by omega] at hd
  rw [numSYT_twoRow_eq_ballot m k h, ← hd]

end QOU.SchurWeyl.TwoRowSYTBallot
