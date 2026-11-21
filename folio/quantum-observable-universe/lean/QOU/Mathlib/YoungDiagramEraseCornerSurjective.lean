/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.Mathlib.YoungDiagramAddCell

/-!
# QOU.Mathlib.YoungDiagramEraseCornerSurjective — every diagram is an erased corner

Bean `qou-ejde` records, as the one gap in its route to `heckeIncl` injectivity:

> Step 3 quantifies over partitions of `m+1` obtained as `eraseCorner` of a partition of `m+2`.
> That IS all of them (add a corner cell to any partition of `m+1`), but the surjectivity of
> `eraseCorner` onto partitions of `m+1` must be STATED and proved, not assumed.

This file states and proves it. Two lines of new mathematics, both of which reduce to pieces
already on `main`:

| | |
|---|---|
| `isAddableCell_rowLen_zero` | the cell just past the end of row `0` is addable to **any** diagram |
| `exists_eraseCorner_eq` | every diagram is `μ ∖ c` for some `μ` and removable corner `c` of it |

## Why row `0` and not a new bottom row

`addable_iff` characterises an addable cell as one sitting just past the end of its row, in a row
that is either the first or strictly shorter than the row above. At `i = 0` the second conjunct is
`0 = 0`, discharged by `rfl` — so row `0` needs no side condition at all, whereas a new bottom row
would need `rowLen` strict-decrease bookkeeping. The empty diagram is covered without a case split:
`rowLen 0 = 0` there, and `(0, 0)` is addable to `⊥`.

## What this does NOT claim

Only that **some** `(μ, c)` erases to `ν` — not that it is unique (it is not; a diagram generally
has several addable cells), and nothing about cardinalities beyond what `card_eraseCorner` already
gives. `cornerAddEquiv` in `YoungDiagramAddCell` is the sharper statement, a bijection of *pairs*;
this file is the bare surjectivity, which is what a `∀ ν` quantifier needs to be discharged by
`subst`.

Nothing archimedean; no ring; no fit.

-- Ref: [leitner2026] bean qou-ejde, step 3's stated gap.
-/

namespace QOU.Mathlib

open YoungDiagram

variable {μ : YoungDiagram}

/-- The cell just past the end of row `0` is addable to any diagram. -/
theorem isAddableCell_rowLen_zero (ν : YoungDiagram) :
    IsAddableCell ν (0, ν.rowLen 0) :=
  (addable_iff ν 0 (ν.rowLen 0)).mpr ⟨rfl, Or.inl rfl⟩

/-- **Corner removal is surjective.** Every Young diagram `ν` is obtained from some strictly larger
diagram by deleting a removable corner — take `ν` with the cell past the end of its first row
adjoined. Together with `card_eraseCorner` this is what lets a `∀ ν` statement about diagrams of
size `m+1` be proved by working upstairs at `m+2`. -/
theorem exists_eraseCorner_eq (ν : YoungDiagram) :
    ∃ (μ : YoungDiagram) (c : ℕ × ℕ) (hc : IsCornerCell μ c), eraseCorner μ c hc = ν :=
  ⟨addCell ν _ (isAddableCell_rowLen_zero ν), (0, ν.rowLen 0),
    isCornerCell_addCell _ (isAddableCell_rowLen_zero ν),
    eraseCorner_addCell _ (isAddableCell_rowLen_zero ν)⟩

end QOU.Mathlib
