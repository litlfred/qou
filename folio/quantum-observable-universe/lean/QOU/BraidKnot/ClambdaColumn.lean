import QOU.BraidKnot.SeminormalCharacterConnector
import QOU.Mathlib.SYTHookGNW

/-!
# QOU.BraidKnot.ClambdaColumn — the tabulated `c_λ ∈ {1,3,8,10}` of `symbolic_character_table`

The `prop:symbolic-character-table` self-conjugate column
`c_λ ∈ {1, 3, 8, 10}` for `λ ∈ {[2,1], [3,1,1], [3,2,1], [4,1,1,1]}` is exactly
`#SYT(λ)/2`: for the single generator `σ₁` on a self-conjugate shape,
`c_λ = |R_row| = #SYT(λ)/2` (`SeminormalCharacterConnector.two_mul_card_rowClass_eq_card`
+ `sigmaOneCharacter_eq_card_mul`), and the Frame–Robinson–Thrall hook-length formula
(`QOU.Mathlib.SYTEnum.numSYTenum_eq_dimHLF`, proved) gives `#SYT` in closed form. This
file discharges all four tabulated values (extending the `[2,1]` case of
`SytSmallShapeCounts`) — the four are `{2, 6, 16, 20}/2`.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.BraidKnot.ClambdaColumn

open YoungDiagram QOU.Mathlib QOU.BraidKnot.SeminormalCharacterConnector

/-- **`2·|R_row| = dimHLF`** for a self-conjugate `ofRowLens l`: composes the seminormal
    count `2·|R_row| = #SYT` with the proved list-form HLF `#SYT = dimHLF l`. -/
theorem two_mul_card_rowClass_eq_dimHLF (l : List ℕ) (hl : l.Sorted (· ≥ ·))
    (hpos : ∀ a ∈ l, 0 < a)
    (hsc : (ofRowLens l hl).transpose = ofRowLens l hl)
    (hn : 2 ≤ (ofRowLens l hl).cells.card) :
    2 * (rowClass (ofRowLens l hl)).card = QOU.BraidKnot.IdentityI.dimHLF l := by
  rw [two_mul_card_rowClass_eq_card hsc hn, ← Nat.card_eq_fintype_card]
  show numStandardYoungTableaux (ofRowLens l hl) = QOU.BraidKnot.IdentityI.dimHLF l
  rw [← QOU.Mathlib.SYTEnum.numSYTenum_eq_numStandardYoungTableaux l hl,
    QOU.Mathlib.SYTEnum.numSYTenum_eq_dimHLF l hl hpos]

/-- `c_λ([2,1]) = 1` (`#SYT = 2`). -/
theorem clambda_21 : (rowClass (ofRowLens [2, 1] (by decide))).card = 1 := by
  have h := two_mul_card_rowClass_eq_dimHLF [2, 1] (by decide) (by decide)
    (by apply YoungDiagram.ext; decide) (by decide)
  rw [show QOU.BraidKnot.IdentityI.dimHLF [2, 1] = 2 from by decide] at h; omega

/-- `c_λ([3,1,1]) = 3` (`#SYT = 6`; H₅ Wigner). -/
theorem clambda_311 : (rowClass (ofRowLens [3, 1, 1] (by decide))).card = 3 := by
  have h := two_mul_card_rowClass_eq_dimHLF [3, 1, 1] (by decide) (by decide)
    (by apply YoungDiagram.ext; decide) (by decide)
  rw [show QOU.BraidKnot.IdentityI.dimHLF [3, 1, 1] = 6 from by decide] at h; omega

/-- `c_λ([3,2,1]) = 8` (`#SYT = 16`; H₆ dominant, 36% Plancherel = 16²/720). -/
theorem clambda_321 : (rowClass (ofRowLens [3, 2, 1] (by decide))).card = 8 := by
  have h := two_mul_card_rowClass_eq_dimHLF [3, 2, 1] (by decide) (by decide)
    (by apply YoungDiagram.ext; decide) (by decide)
  rw [show QOU.BraidKnot.IdentityI.dimHLF [3, 2, 1] = 16 from by decide] at h; omega

/-- `c_λ([4,1,1,1]) = 10` (`#SYT = 20`; H₇ self-conjugate). -/
theorem clambda_4111 : (rowClass (ofRowLens [4, 1, 1, 1] (by decide))).card = 10 := by
  have h := two_mul_card_rowClass_eq_dimHLF [4, 1, 1, 1] (by decide) (by decide)
    (by apply YoungDiagram.ext; decide) (by decide)
  rw [show QOU.BraidKnot.IdentityI.dimHLF [4, 1, 1, 1] = 20 from by decide] at h; omega

/-- Subtracting the hook-length dimension from twice the row-class cardinality cancels to zero (`qou-fs4r`). -/
theorem two_mul_card_rowClass_sub_dimHLF_eq_zero (l : List ℕ) (hl : l.Sorted (· ≥ ·))
    (hpos : ∀ a ∈ l, 0 < a)
    (hsc : (ofRowLens l hl).transpose = ofRowLens l hl)
    (hn : 2 ≤ (ofRowLens l hl).cells.card) :
    2 * (rowClass (ofRowLens l hl)).card - QOU.BraidKnot.IdentityI.dimHLF l = 0 := by
  rw [two_mul_card_rowClass_eq_dimHLF l hl hpos hsc hn, Nat.sub_self]

end QOU.BraidKnot.ClambdaColumn
