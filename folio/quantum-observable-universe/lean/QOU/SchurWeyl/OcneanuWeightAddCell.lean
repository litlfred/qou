import QOU.SchurWeyl.HookLengthAddCell

/-!
# QOU.SchurWeyl.OcneanuWeightAddCell — the weight's two halves under `addCell`

`HookLengthAddCell` supplies how a hook moves when a cell is added.  This file applies it to
`ocneanuWeight` itself, splitting the weight into its numerator and denominator products and
showing how each responds.  It is the second brick toward the **arbitrary-`z`** corner identity
(bean `qou-j7ln`); the convention-D case is closed and merged (`91bf8fcb4`).

| | |
|---|---|
| `ocneanuNumProd`, `ocneanuDenProd` | the two products, as objects |
| `ocneanuNumProd_addCell` | the numerator gains **exactly one factor** |
| `ocneanuDenProd_addCell` | the denominator gains `q² − 1`, and every old factor shifts by one step iff its cell shares the new cell's row or column |

## The asymmetry, which is the whole point

The numerator's proof is `Finset.prod_insert` and nothing else, because each factor depends only on
its own cell's `(i, j)` and not on the diagram.  The denominator cannot be done that way at all:
`hookLength` *is* diagram-dependent, so every surviving factor may move.  That asymmetry is why
arbitrary `z` is harder than convention D, where the ≥3-row weights vanish, only `twoRow` survives,
and `schurPrincipal_twoRow` telescopes the entire hook-content product.

## Naming — cousins, not synonyms

The corpus already has `ocneanuNumFactor_eq_zero_of_content_neg_two` and
`ocneanuNumFactor_conventionD`.  Those are about **one cell's** factor; the definitions here are
the **products over all cells**.  Hence `…Prod`, so the two families cannot be mistaken for each
other.

## What remains

The ratio `w_{ν+s} / w_ν` still needs the arm/leg telescoping of the shifted factors — the `if`
in `ocneanuDenProd_addCell` has to be turned into a product over `s`'s row and column.  That is the
next brick and it has no two-row counterpart.

## Scope (§7c)

Generic `[Field R]` — no ordering, nothing archimedean, no `ℝ`.

LaTeX label: `thm:ocneanu-weight-add-cell`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib YoungDiagram

variable {R : Type*} [Field R]

/-- The numerator of `ocneanuWeight`, as its own object. -/
noncomputable def ocneanuNumProd (q z : R) (mu : YoungDiagram) : R :=
  ∏ c ∈ mu.cells, (q ^ (2 * c.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * c.2 + 1) * z)

/-- The denominator of `ocneanuWeight`, as its own object. -/
noncomputable def ocneanuDenProd (q : R) (mu : YoungDiagram) : R :=
  ∏ c ∈ mu.cells, (q ^ (2 * hookLength mu c) - 1)

theorem ocneanuWeight_eq_numProd_div_denProd (q z : R) (mu : YoungDiagram) :
    ocneanuWeight q z mu = ocneanuNumProd q z mu / ocneanuDenProd q mu := rfl

/-- **The numerator gains exactly one factor.**  Each factor depends only on its own cell, so
adding a cell is `Finset.prod_insert` and nothing more. -/
theorem ocneanuNumProd_addCell (q z : R) (ν : YoungDiagram) (s : ℕ × ℕ) (hs : IsAddableCell ν s) :
    ocneanuNumProd q z (addCell ν s hs)
      = (q ^ (2 * s.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * s.2 + 1) * z) * ocneanuNumProd q z ν := by
  classical
  have hsn : s ∉ ν.cells := fun h => hs.1 ((YoungDiagram.mem_cells s).mp h)
  show (∏ c ∈ insert s ν.cells, _) = _
  rw [Finset.prod_insert hsn]
  rfl

/-- **The denominator does not.**  The added cell contributes `q² − 1` (its hook is `1`), and every
old cell's factor moves by one step exactly when it shares the new cell's row or column. -/
theorem ocneanuDenProd_addCell (q : R) (ν : YoungDiagram) (s : ℕ × ℕ) (hs : IsAddableCell ν s) :
    ocneanuDenProd q (addCell ν s hs)
      = (q ^ 2 - 1)
        * ∏ c ∈ ν.cells,
            (q ^ (2 * (hookLength ν c + if c.1 = s.1 ∨ c.2 = s.2 then 1 else 0)) - 1) := by
  classical
  have hsn : s ∉ ν.cells := fun h => hs.1 ((YoungDiagram.mem_cells s).mp h)
  show (∏ c ∈ insert s ν.cells, (q ^ (2 * hookLength (addCell ν s hs) c) - 1)) = _
  rw [Finset.prod_insert hsn, hookLength_addCell_self ν s hs]
  congr 1
  refine Finset.prod_congr rfl fun c hc => ?_
  rw [hookLength_addCell_of_mem ν s hs c ((YoungDiagram.mem_cells c).mp hc)]

end QOU.SchurWeyl
