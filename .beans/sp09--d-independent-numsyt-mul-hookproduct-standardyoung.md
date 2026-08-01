---
# sp09
title: 'D [independent]: numSYT_mul_hookProduct (StandardYoungTableau.lean:113) — FRT hook-length'
status: todo
type: task
priority: low
parent: sp00
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-07-05T16:30:00Z
---

Frame-Robinson-Thrall: numSYT(lam).prod(hooks)=n!. Needs NPS hook-walk (probability layer) or RSK. Famous, absent.

Parent: sp00.

## Precise bridge scope (2026-08-01, from PieceA general-n completion)

`numSYT_mul_hookProduct` (`QOU.BraidKnot`, StandardYoungTableau.lean) is NOT a
from-scratch HLF: the FRT formula is ALREADY sorry-free at
`QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct`
(HookLengthFormula.lean). Closing sp09 = two bridges:

  (1) hookProduct μ = QOU.Mathlib.hookLengthProduct μ  [TRACTABLE, ~40 lines]
      per-cell: StandardYoungTableau.hookLength (filter-arm-card + filter-leg-card
      + 1) = HookLengthFormula.hookLength (rowLen i - j - 1)+(colLen j - i - 1)+1,
      on cells. This is exactly PieceA.armZ_eq_card / legZ_eq_card (ℕ form) —
      filter-arm-card = rowLen i - j - 1. Product over μ.cells ⇒ cell-agreement
      suffices.

  (2) numSYT μ = QOU.Mathlib.numStandardYoungTableaux μ  [MODERATE, ~120-150 lines]
      Nat.card equality between two SYT encodings:
      - QOU.BraidKnot.StandardYoungTableau: standalone, entries 0-based {0..n-1},
        explicit inj_on/row_strict/col_strict.
      - QOU.Mathlib.StandardYoungTableau: 1-based {1..n}, wraps Mathlib
        SemistandardYoungTableau (toSsyt) + injOn_cells/mapsTo_cells.
      Build Equiv both directions (entry shift ±1; derive SSYT weak-row from
      strict, and strict from SSYT-weak+injOn). Then Nat.card_congr.

  Then numSYT_mul_hookProduct := numStandardYoungTableaux_mul_hookLengthProduct
  transported by (1)+(2). Part (2) is the real work; part (1) reuses PieceA.
