/-
# The weak vertex on an inverse letter

Bean `qou-wkcd`. The corpus vertex `weakVertex q σ` (`LeftLineDefinition.lean`) is
defined for a letter `σ` at parameter `q`. An inverse letter `σ⁻¹ = flip q σ` is itself
a letter, at parameter `q⁻¹` (`Helicity.flip_hecke`), so the same definition applies to
it with no new choice. This file computes what it gives.

## What this file proves

1. **The vertex does not see the letter's sign** (`weakVertex_inverse_letter`):
   `weakVertex q⁻¹ σ⁻¹ = weakVertex q σ` when `|q| ≠ 1`. The left line of `σ⁻¹` is the
   right line of `σ` (`LeftLine.leftLine_mirror`), and on each line the two vertices act
   by the same scalar.
2. **The insertion on an inverse letter lives on the right line**
   (`inverse_insertion`): `weakVertex q⁻¹ σ⁻¹ − σ⁻¹ = h • rightLine q σ`, with
   `h = q − q⁻¹`. Compare `WeakVertexLeftProjector.weakVertex_sub_letter`:
   on a positive letter the insertion is `−h • leftLine q σ`. So in any word, a vertex on
   a positive letter changes the left line of that letter and a vertex on a negative
   letter changes its right line. The two insertions differ by `h • 1`
   (`insertion_sign_difference`).

## Scope

Derived from the owner-ruled definition of `leftLine` and the corpus `weakVertex`; no new
input. Nothing here identifies `weakVertex` with a physical coupling (scope (a)).
Base ring as in `LeftLineDefinition.lean` (ordered field, needed by `|q|`); generic algebra.
No `sorry`, no axiom.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.QuarkState.WeakVertexLeftProjector

namespace QOU.QuarkState.WeakVertexInverseLetter

open QOU.QuarkState.Helicity QOU.QuarkState.LeftLine

variable {K A : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  [Ring A] [Algebra K A]
variable {q : K} {σ : A}

/-- The right line of `σ⁻¹` (at `q⁻¹`) is the left line of `σ`. -/
theorem rightLine_mirror (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (h1 : |q| ≠ 1) :
    rightLine q⁻¹ (flip q σ) = leftLine q σ := by
  have hq2' : q⁻¹ + (q⁻¹)⁻¹ ≠ 0 := by rw [inv_inv, add_comm]; exact hq2
  have e1 := leftLine_add_rightLine (σ := flip q σ) hq2'
  have e2 := leftLine_add_rightLine (σ := σ) hq2
  rw [leftLine_mirror h1 hq] at e1
  have : rightLine q⁻¹ (flip q σ) = 1 - rightLine q σ := eq_sub_of_add_eq' e1
  rw [this, ← e2, add_sub_cancel_right]

/-- **The vertex does not depend on the sign of the letter.** -/
theorem weakVertex_inverse_letter (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (h1 : |q| ≠ 1)
    (hs : IsLetter q σ) : weakVertex q⁻¹ (flip q σ) = weakVertex q σ := by
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
  have hq2' : q⁻¹ + (q⁻¹)⁻¹ ≠ 0 := by rw [inv_inv, add_comm]; exact hq2
  have ht : IsLetter q⁻¹ (flip q σ) := flip_hecke hs
  set W' := weakVertex q⁻¹ (flip q σ)
  set W := weakVertex q σ
  -- on the right line of σ (= left line of σ⁻¹) both act as σ
  have hR : W' * rightLine q σ = W * rightLine q σ := by
    have a := weakVertex_mul_leftLine hqi hq2' ht
    rw [leftLine_mirror h1 hq, flip_flip] at a
    rw [a, weakVertex_mul_rightLine hq hq2 hs]
  -- on the left line of σ (= right line of σ⁻¹) both act as σ⁻¹
  have hL : W' * leftLine q σ = W * leftLine q σ := by
    have b := weakVertex_mul_rightLine hqi hq2' ht
    rw [rightLine_mirror hq hq2 h1] at b
    rw [b, weakVertex_mul_leftLine hq hq2 hs]
  calc W' = W' * (leftLine q σ + rightLine q σ) := by
        rw [leftLine_add_rightLine hq2, mul_one]
    _ = W * (leftLine q σ + rightLine q σ) := by rw [mul_add, mul_add, hL, hR]
    _ = W := by rw [leftLine_add_rightLine hq2, mul_one]

/-- **The insertion on an inverse letter is `h` times the right line of the letter.** -/
theorem inverse_insertion (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (h1 : |q| ≠ 1)
    (hs : IsLetter q σ) :
    weakVertex q⁻¹ (flip q σ) - flip q σ = (q - q⁻¹) • rightLine q σ := by
  rw [weakVertex_inverse_letter hq hq2 h1 hs]
  have e := WeakVertexLeftProjector.weakVertex_sub_letter hq hq2 hs
  have f : flip q σ = σ - (q - q⁻¹) • (1 : A) := rfl
  have g : leftLine q σ = 1 - rightLine q σ :=
    eq_sub_of_add_eq (leftLine_add_rightLine hq2)
  rw [f, sub_sub_eq_add_sub, ← sub_add_eq_add_sub, e, g]
  module

/-- The two insertions (positive and inverse letter) differ by `h • 1`. -/
theorem insertion_sign_difference (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (h1 : |q| ≠ 1)
    (hs : IsLetter q σ) :
    (weakVertex q⁻¹ (flip q σ) - flip q σ) - (weakVertex q σ - σ) =
      (q - q⁻¹) • (1 : A) := by
  have e := leftLine_add_rightLine hq2 (σ := σ)
  rw [inverse_insertion hq hq2 h1 hs, WeakVertexLeftProjector.weakVertex_sub_letter hq hq2 hs,
    ← e]
  module

end QOU.QuarkState.WeakVertexInverseLetter
