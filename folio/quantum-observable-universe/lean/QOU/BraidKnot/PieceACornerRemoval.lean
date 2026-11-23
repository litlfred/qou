import QOU.MathlibExt.YoungDiagramCells
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination

/-!
# Piece A: the corner-removal identity

Content block `lem:piece-a-corner-removal-obligation`.

Let `μ` be a Young diagram with `n` cells and let `(r, s)` be a removable corner,
so `s + 1 = μ.rowLen r` and `μ.rowLen (r + 1) ≤ s`. Deleting the corner changes
the hook of the corner itself, of the `s` cells of row `r` to its left and of the
`r` cells of column `s` above it. The identity is

  `1 + Σ_{j<s} (2 h(r,j) - 1) + Σ_{i<r} (2 h(i,s) - 1) = (s - r)² + 2n - 1`,

with `h = YoungDiagramCells.hook` (arm + leg + 1, over `ℤ`).

## Proof

Write `c_j = colLen j`. The corner hypotheses give `colLen s = r + 1`, so
`h(r,j) = s - j + c_j - r` and `h(i,s) = λ_i - s + r - i`. Split the cells by
column: those in columns `< s` number `Σ_{j<s} c_j`; those in columns `≥ s` lie in
rows `≤ r` (a lower row has length `≤ s`), and row `i ≤ r` contributes
`λ_i - s` of them. So `n = Σ_{j<s} c_j + Σ_{i<r} λ_i + 1 - r s`, and the identity
is then two Gauss sums and `ring`.

The statement is purely combinatorial; nothing here is evaluated at `q₀`.
-/

namespace QOU.BraidKnot.PieceACornerRemoval

open Finset QOU.MathlibExt.YoungDiagramCells

/-- Twice the Gauss sum, over `ℤ`. -/
theorem two_mul_sum_range_id (s : ℕ) :
    2 * ∑ j ∈ range s, (j : ℤ) = (s : ℤ) * ((s : ℤ) - 1) := by
  induction s with
  | zero => simp
  | succ k ih => rw [sum_range_succ, mul_add, ih]; push_cast; ring

variable {μ : YoungDiagram} {r s : ℕ}

/-- At a removable corner `(r, s)`, column `s` has exactly `r + 1` cells. -/
theorem colLen_corner (hrow : s + 1 = μ.rowLen r) (hnext : μ.rowLen (r + 1) ≤ s) :
    μ.colLen s = r + 1 := by
  have hin : r < μ.colLen s := by
    rw [← YoungDiagram.mem_iff_lt_colLen, YoungDiagram.mem_iff_lt_rowLen]; omega
  have hout : ¬ (r + 1 < μ.colLen s) := by
    rw [← YoungDiagram.mem_iff_lt_colLen, YoungDiagram.mem_iff_lt_rowLen]; omega
  omega

/-- A cell in a column `≥ s` lies in a row `≤ r`, because row `r + 1` and every
row below it have length `≤ s`. -/
theorem row_le_of_col_ge (hnext : μ.rowLen (r + 1) ≤ s) {c : ℕ × ℕ} (hc : c ∈ μ)
    (hcs : s ≤ c.2) : c.1 < r + 1 := by
  by_contra h
  have h1 : μ.rowLen c.1 ≤ μ.rowLen (r + 1) := μ.rowLen_anti _ _ (by omega)
  have h2 : c.2 < μ.rowLen c.1 := (YoungDiagram.mem_iff_lt_rowLen).mp hc
  omega

/-- The cells of `μ` in column `j`. -/
theorem card_col_fiber (j : ℕ) :
    (μ.cells.filter (fun c => c.2 = j)).card = μ.colLen j := by
  have : μ.cells.filter (fun c => c.2 = j) = (range (μ.colLen j)).image (fun i => (i, j)) := by
    ext ⟨a, b⟩
    simp only [mem_filter, YoungDiagram.mem_cells, mem_image, mem_range, Prod.mk.injEq]
    constructor
    · rintro ⟨hc, rfl⟩
      exact ⟨a, YoungDiagram.mem_iff_lt_colLen.mp hc, rfl, rfl⟩
    · rintro ⟨i, hi, rfl, rfl⟩
      exact ⟨YoungDiagram.mem_iff_lt_colLen.mpr hi, rfl⟩
  rw [this, card_image_of_injective _ (fun a b h => by simpa using h), card_range]

/-- The cells of `μ` in row `i` at columns `≥ s`. -/
theorem card_row_tail_fiber (i : ℕ) :
    (μ.cells.filter (fun c => ¬ c.2 < s ∧ c.1 = i)).card = μ.rowLen i - s := by
  have : μ.cells.filter (fun c => ¬ c.2 < s ∧ c.1 = i) =
      (Ico s (μ.rowLen i)).image (fun j => (i, j)) := by
    ext ⟨a, b⟩
    simp only [mem_filter, YoungDiagram.mem_cells, mem_image, mem_Ico, Prod.mk.injEq]
    constructor
    · rintro ⟨hc, hb, rfl⟩
      exact ⟨b, ⟨by omega, YoungDiagram.mem_iff_lt_rowLen.mp hc⟩, rfl, rfl⟩
    · rintro ⟨j, ⟨hj1, hj2⟩, rfl, rfl⟩
      exact ⟨YoungDiagram.mem_iff_lt_rowLen.mpr hj2, by omega, rfl⟩
  rw [this, card_image_of_injective _ (fun a b h => by simpa using h), Nat.card_Ico]

/-- **Cell count by the corner's column.** `n = Σ_{j<s} colLen j + Σ_{i≤r} (λ_i - s)`. -/
theorem card_cells_split (hnext : μ.rowLen (r + 1) ≤ s) :
    μ.cells.card = ∑ j ∈ range s, μ.colLen j + ∑ i ∈ range (r + 1), (μ.rowLen i - s) := by
  rw [← filter_card_add_filter_neg_card_eq_card (fun c : ℕ × ℕ => c.2 < s)]
  congr 1
  · rw [card_eq_sum_card_fiberwise (f := fun c : ℕ × ℕ => c.2) (t := range s)
      (fun c hc => mem_range.mpr (mem_filter.mp hc).2)]
    refine sum_congr rfl (fun j hj => ?_)
    rw [filter_filter, ← card_col_fiber j]
    congr 1
    apply filter_congr
    intro c _
    constructor
    · exact fun h => h.2
    · intro h; refine ⟨?_, h⟩; show c.2 < s; rw [h]; exact mem_range.mp hj
  · rw [card_eq_sum_card_fiberwise (f := fun c : ℕ × ℕ => c.1) (t := range (r + 1))
      (fun c hc => by
        have hc' := mem_filter.mp hc
        exact mem_range.mpr (row_le_of_col_ge hnext hc'.1
          (by omega)))]
    refine sum_congr rfl (fun i _ => ?_)
    rw [filter_filter, card_row_tail_fiber i]

/-- **The corner-removal identity** (`lem:piece-a-corner-removal-obligation`).

For a removable corner `(r, s)` of `μ` (so `s + 1 = λ_r` and `λ_{r+1} ≤ s`),
`1 + Σ_{j<s} (2 h(r,j) - 1) + Σ_{i<r} (2 h(i,s) - 1) = (s - r)² + 2 |μ| - 1`. -/
theorem corner_removal (hrow : s + 1 = μ.rowLen r) (hnext : μ.rowLen (r + 1) ≤ s) :
    1 + ∑ j ∈ range s, (2 * hook μ (r, j) - 1) + ∑ i ∈ range r, (2 * hook μ (i, s) - 1)
      = ((s : ℤ) - r) ^ 2 + 2 * (μ.cells.card : ℤ) - 1 := by
  have hcol := colLen_corner hrow hnext
  -- every row `i ≤ r` reaches past column `s`
  have hlong : ∀ i ∈ range (r + 1), s ≤ μ.rowLen i := fun i hi => by
    have := μ.rowLen_anti i r (by have := mem_range.mp hi; omega); omega
  -- the cell count, over `ℤ`
  have hn : (μ.cells.card : ℤ) =
      ∑ j ∈ range s, (μ.colLen j : ℤ) + ∑ i ∈ range r, (μ.rowLen i : ℤ) + 1 - r * s := by
    rw [card_cells_split hnext, Nat.cast_add, Nat.cast_sum, Nat.cast_sum,
      sum_congr rfl (fun i hi => Nat.cast_sub (hlong i hi)), sum_sub_distrib,
      sum_range_succ, sum_const, card_range]
    simp only [nsmul_eq_mul]
    rw [← hrow]; push_cast; ring
  -- rewrite each summand
  have hA : ∑ j ∈ range s, (2 * hook μ (r, j) - 1)
      = ∑ j ∈ range s, ((2 * (s : ℤ) - 2 * r - 1) + 2 * (μ.colLen j : ℤ) - 2 * (j : ℤ)) := by
    refine sum_congr rfl (fun j _ => ?_)
    rw [hook_eq, ← hrow]; push_cast; ring
  have hB : ∑ i ∈ range r, (2 * hook μ (i, s) - 1)
      = ∑ i ∈ range r, ((2 * (r : ℤ) - 2 * s - 1) + 2 * (μ.rowLen i : ℤ) - 2 * (i : ℤ)) := by
    refine sum_congr rfl (fun i _ => ?_)
    rw [hook_eq, hcol]; push_cast; ring
  rw [hA, hB]
  simp only [sum_sub_distrib, sum_add_distrib, sum_const, card_range, nsmul_eq_mul,
    ← Finset.mul_sum]
  have gs := two_mul_sum_range_id s
  have gr := two_mul_sum_range_id r
  linear_combination (-1 : ℤ) * gs - gr - 2 * hn

/-- Subtracting the right-hand corner-removal quadratic expression from the hook-sum corner contribution yields zero. -/
theorem corner_removal_sub_eq_zero (hrow : s + 1 = μ.rowLen r) (hnext : μ.rowLen (r + 1) ≤ s) :
    (1 + ∑ j ∈ range s, (2 * hook μ (r, j) - 1) + ∑ i ∈ range r, (2 * hook μ (i, s) - 1))
      - (((s : ℤ) - r) ^ 2 + 2 * (μ.cells.card : ℤ) - 1) = 0 := by
  rw [corner_removal hrow hnext, sub_self]

end QOU.BraidKnot.PieceACornerRemoval
