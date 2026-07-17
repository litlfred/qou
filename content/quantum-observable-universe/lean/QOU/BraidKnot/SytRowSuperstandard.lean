import QOU.Mathlib.StandardYoungTableau

/-!
# QOU.BraidKnot.SytRowSuperstandard — the row-superstandard standard Young tableau

The **row-superstandard** (row-reading) tableau of shape `μ`: fill the cells with `1, 2, …, |μ|`
reading each row left-to-right, top row first. Its entry at `(i, j) ∈ μ` is

> `rowPrefix μ i + j + 1`,   where   `rowPrefix μ i = ∑_{i' < i} μ.rowLen i'`

(the number of cells in the rows strictly above `i`, plus the position `j` within row `i`, plus 1).

This file builds it in two stages:

1. **The underlying semistandard tableau** `rowSuperstandardSsyt μ` — proved sorry-free. Rows are
   (weakly) increasing because `j` grows; columns are *strictly* increasing because
   `rowPrefix` strictly increases with the row index (each skipped row contributes at least one
   cell — `rowLen` is positive down to the bottom row by `rowLen_anti`).

2. **Nonemptiness of `StandardYoungTableau μ`** (the `BijOn` onto `{1, …, |μ|}`) — the base-tableau
   existence brick the Okounkov–Vershik exchange argument (`syt_all_connect_to_some`) needs. *(Stage
   2 is developed incrementally; see the tracked cores.)*

Pure combinatorics on `ℕ` (`§7c`-clean: no `ℝ`, no ordering on a ring, no `Real.*`). Reusable
independently of the seminormal machinery.

Ref: [sagan2001] (The Symmetric Group, §3.9 — the superstandard / row-reading tableau).
-/

namespace QOU.BraidKnot

open YoungDiagram Finset

variable (μ : YoungDiagram)

/-- `rowPrefix μ i` = number of cells in the rows strictly above row `i`
(`∑_{i' < i} μ.rowLen i'`). This is the label offset of the first cell of row `i` in the
row-reading order. -/
def rowPrefix (i : ℕ) : ℕ := ∑ i' ∈ Finset.range i, μ.rowLen i'

@[simp] theorem rowPrefix_zero : rowPrefix μ 0 = 0 := by simp [rowPrefix]

theorem rowPrefix_succ (i : ℕ) : rowPrefix μ (i + 1) = rowPrefix μ i + μ.rowLen i := by
  simp [rowPrefix, Finset.sum_range_succ]

/-- `rowPrefix` is monotone in the row index (a sum of the nonnegative row lengths over a larger
initial range). -/
theorem rowPrefix_mono {i1 i2 : ℕ} (h : i1 ≤ i2) : rowPrefix μ i1 ≤ rowPrefix μ i2 := by
  induction i2, h using Nat.le_induction with
  | base => exact le_refl _
  | succ n _ ih => rw [rowPrefix_succ]; omega

/-- If row `i2` is nonempty (some `(i2, j) ∈ μ`) then any earlier row `i1 ≤ i2` is strictly longer
than the prefix gap allows: `rowPrefix μ i1 < rowPrefix μ i2` whenever `i1 < i2` and row `i1`
contains a cell. Here we get positivity of `rowLen i1` from `rowLen_anti`. -/
theorem rowPrefix_strictMono_of_mem {i1 i2 j : ℕ} (hlt : i1 < i2) (hcell : (i2, j) ∈ μ) :
    rowPrefix μ i1 < rowPrefix μ i2 := by
  have hrl2 : 0 < μ.rowLen i2 := by
    have := mem_iff_lt_rowLen.mp hcell; omega
  have hrl1 : 0 < μ.rowLen i1 :=
    lt_of_lt_of_le hrl2 (μ.rowLen_anti i1 i2 (le_of_lt hlt))
  have hstep : rowPrefix μ (i1 + 1) = rowPrefix μ i1 + μ.rowLen i1 := rowPrefix_succ μ i1
  have hmono : rowPrefix μ (i1 + 1) ≤ rowPrefix μ i2 := rowPrefix_mono μ hlt
  omega

/-- The row-reading entry: `rowPrefix μ i + j + 1` on cells of `μ`, `0` off the diagram. -/
def rowSuperstandardEntry (i j : ℕ) : ℕ :=
  if (i, j) ∈ μ then rowPrefix μ i + j + 1 else 0

/-- **The row-superstandard semistandard Young tableau of shape `μ` (sorry-free).** Rows increase
(weakly) because the position `j` grows; columns increase *strictly* because the row-prefix offset
strictly increases with the row index (`rowPrefix_strictMono_of_mem`). -/
def rowSuperstandardSsyt : SemistandardYoungTableau μ where
  entry := rowSuperstandardEntry μ
  row_weak' := by
    intro i j1 j2 hj hcell
    have hcell1 : (i, j1) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt hj) hcell
    simp only [rowSuperstandardEntry, if_pos hcell, if_pos hcell1]
    omega
  col_strict' := by
    intro i1 i2 j hi hcell
    have hcell1 : (i1, j) ∈ μ := μ.up_left_mem (le_of_lt hi) (le_refl j) hcell
    simp only [rowSuperstandardEntry, if_pos hcell, if_pos hcell1]
    have := rowPrefix_strictMono_of_mem μ hi hcell
    omega
  zeros' := by
    intro i j hnc
    simp only [rowSuperstandardEntry, if_neg hnc]

@[simp] theorem rowSuperstandardSsyt_apply (i j : ℕ) :
    (rowSuperstandardSsyt μ) i j = rowSuperstandardEntry μ i j := rfl

end QOU.BraidKnot
