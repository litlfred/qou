import Mathlib.Data.Nat.Basic

/-!
# Placement of knot-indexed convolutions in the bi-filtration grid

Compiled formalisation of `prop:knot-indexed-convolution-grid`.
Sibling docstub at `braids-and-knots/knot-indexed-convolution-grid.lean`.

This proposition records the row-placement of the paper's knot-
indexed convolutions in the bar-class × depth bi-filtration grid.
Each knot-indexed convolution lands at a unique (bar_class, depth)
cell — the placement function is well-defined.
-/

namespace QOU.BraidKnot.KnotIndexedConvolutionGrid

/-- Abstract context for `prop:knot-indexed-convolution-grid`. -/
class KnotIndexedConvolutionGridContext where
  /-- A knot-indexed convolution, indexed by ℕ. -/
  KnotConvolution : Type
  /-- Bar-class assigned to each convolution. -/
  bar_class : KnotConvolution → ℕ
  /-- Bi-filtration depth assigned to each convolution. -/
  depth : KnotConvolution → ℕ
  /-- Manuscript claim — placement is injective into the bi-filtration grid
      (each convolution occupies a distinct `(bar_class, depth)` cell):
      if two convolutions land at the same `(bar_class, depth)` pair, they are equal. -/
  claim_placement_well_defined : ∀ k₁ k₂ : KnotConvolution,
    (bar_class k₁, depth k₁) = (bar_class k₂, depth k₂) → k₁ = k₂


/-! ### Removed 2026-08-30 — self-assuming projections

- `grid_placement` — body was `ctx.claim_placement_well_defined`: the conclusion was the projected
  field verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content is not lost: it stays in the class field each
declaration projected, which asserts the same proposition under the same
hypotheses. Only the restatement goes. That is the disposition the vacuity
ledger records for this category — *"drop the pseudo-theorem and project the
field at use sites"* — and there were no use sites: each had **zero references
anywhere in the corpus**, including in this file. A caller wanting the fact
writes the projection directly, which is what the removed body did.
Bean `qou-z9ws`.
-/

end QOU.BraidKnot.KnotIndexedConvolutionGrid
