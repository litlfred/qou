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
