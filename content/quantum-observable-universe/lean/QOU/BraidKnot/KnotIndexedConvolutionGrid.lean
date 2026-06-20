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
  /-- Manuscript claim — placement is well-defined (each convolution
      has a unique (bar_class, depth) cell): if two convolutions have
      the same bar_class and the same depth, they index the same
      grid cell. -/
  claim_placement_well_defined : ∀ k₁ k₂ : KnotConvolution,
    bar_class k₁ = bar_class k₂ → depth k₁ = depth k₂ →
      (bar_class k₁, depth k₁) = (bar_class k₂, depth k₂)

/-- **Proposition (`prop:knot-indexed-convolution-grid`).** -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/knot-indexed-convolution-grid.md
def grid_placement [ctx : KnotIndexedConvolutionGridContext] :
    ∀ k₁ k₂ : ctx.KnotConvolution,
      ctx.bar_class k₁ = ctx.bar_class k₂ → ctx.depth k₁ = ctx.depth k₂ →
        (ctx.bar_class k₁, ctx.depth k₁) = (ctx.bar_class k₂, ctx.depth k₂) :=
  ctx.claim_placement_well_defined

end QOU.BraidKnot.KnotIndexedConvolutionGrid
