import QOU.Mathlib.SYTListCorner
import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# Piece A: Corner-Removal Induction

This file scaffolds the corner-removal induction route for Piece A
(`Σ_c h_c² = Σ_c c(c)² + n²`).

Removing a removable corner `(r,s)` drops the hooks in row `r` (for `j < s`)
and column `s` (for `i < r`) each by 1. The exact obligation for the
induction step is:
  `1 + Σ_{j<s}(2h(r,j)-1) + Σ_{i<r}(2h(i,s)-1) = (s-r)² + (2n-1)`

This file formulates this combinatorial obligation over `List ℕ`.
-/

namespace QOU.Mathlib.PieceA

open QOU.BraidKnot.IdentityI (sz colLen)
open QOU.Mathlib.SYTEnum (IsCorner removeCorner corners mem_corners)

/-- The hook length of cell `(i,j)` before corner removal: `h(i,j) = (λ_i - j) + (colLen j - i) - 1`. -/
def hook (l : List ℕ) (i j : ℕ) : ℕ :=
  (l.getD i 0 - j) + (colLen l j - i) - 1

/-! ### Corner Column Length -/

/-- For a corner `(r,s)` where `s = λ_r - 1`, the column length of `s` is exactly `r + 1`.
This is because row `r` reaches `s`, but row `r+1` is strictly shorter. -/
lemma colLen_corner (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (r : ℕ) (hc : IsCorner l r) :
    colLen l (l.getD r 0 - 1) = r + 1 := by
  have h1 : r < colLen l (l.getD r 0 - 1) := by
    rw [QOU.BraidKnot.IdentityI.colLen_duality l hl r]
    obtain ⟨hr, hnext⟩ := hc
    have : 0 < l.getD r 0 := by omega
    omega
  have h2 : ¬ (r + 1 < colLen l (l.getD r 0 - 1)) := by
    rw [QOU.BraidKnot.IdentityI.colLen_duality l hl (r + 1)]
    obtain ⟨hr, hnext⟩ := hc
    omega
  omega

/-! ### Hook Simplifications at the Corner -/

/-- For a corner row `r`, the arm contribution to the hook simplifies. -/
lemma hook_r_j (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (r : ℕ) (hc : IsCorner l r) {j : ℕ} (hj : j < l.getD r 0 - 1) :
    hook l r j = (l.getD r 0 - 1 - j) + (colLen l j - r) := by
  unfold hook
  have : colLen l j ≥ r + 1 := by
    have hj' : j < l.getD r 0 := by omega
    exact (QOU.BraidKnot.IdentityI.colLen_duality l hl r j).mpr hj'
  omega

/-- For a corner column `s = λ_r - 1`, the leg contribution to the hook simplifies. -/
lemma hook_i_s (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (r : ℕ) (hc : IsCorner l r) {i : ℕ} (hi : i < r) :
    let s := l.getD r 0 - 1
    hook l i s = (l.getD i 0 - s) + (r - i) := by
  unfold hook
  have hcol : colLen l (l.getD r 0 - 1) = r + 1 := colLen_corner l hl r hc
  omega

/-! ### Hook Sums -/

/-- The sum of `2*hook - 1` along the row `r` up to `s`. -/
lemma sum_hook_r (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (r : ℕ) (hc : IsCorner l r) :
    let s := l.getD r 0 - 1
    ∑ j ∈ Finset.range s, (2 * (hook l r j : ℤ) - 1)
      = 2 * ∑ j ∈ Finset.range s, (colLen l j : ℤ) + (s : ℤ)^2 - 2 * (r : ℤ) * (s : ℤ) := by
  sorry

/-- The sum of `2*hook - 1` along the column `s` up to `r`. -/
lemma sum_hook_s (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (r : ℕ) (hc : IsCorner l r) :
    let s := l.getD r 0 - 1
    ∑ i ∈ Finset.range r, (2 * (hook l i s : ℤ) - 1)
      = 2 * ∑ i ∈ Finset.range r, (l.getD i 0 : ℤ) + (r : ℤ)^2 - 2 * (s : ℤ) * (r : ℤ) := by
  sorry

/-! ### Size Decomposition -/

/-- The total number of cells `n` decomposed relative to the corner `(r,s)`:
`n = (cells in rows < r) + (cells in cols < s) - (overlap r * s) + (the corner itself)`. -/
lemma sz_decomposition (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (r : ℕ) (hc : IsCorner l r) :
    let s := l.getD r 0 - 1
    (sz l : ℤ) = (∑ i ∈ Finset.range r, (l.getD i 0 : ℤ)) + (∑ j ∈ Finset.range s, (colLen l j : ℤ)) - (r : ℤ) * (s : ℤ) + 1 := by
  sorry

/-! ### Main Obligation -/

/-- The change obligation when a corner at `(r,s)` is removed.
`s` is the column index of the corner (which is `λ_r - 1`).
We need to show this evaluates to `(s - r)^2 + (2n - 1)`. -/
theorem corner_removal_obligation (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (r : ℕ) (hc : IsCorner l r) :
    let s := l.getD r 0 - 1
    let n := sz l
    (1 : ℤ) + (∑ j ∈ Finset.range s, (2 * (hook l r j : ℤ) - 1))
            + (∑ i ∈ Finset.range r, (2 * (hook l i s : ℤ) - 1))
      = ((s : ℤ) - (r : ℤ))^2 + (2 * (n : ℤ) - 1) := by
  sorry

end QOU.Mathlib.PieceA
