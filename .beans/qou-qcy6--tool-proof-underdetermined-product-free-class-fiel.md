---
# qou-qcy6
title: 'TOOL: proof-underdetermined-product — free class fields that occur only as a product'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T07:09:37Z
updated_at: 2026-08-30T07:14:18Z
---

Raised by a sibling on PR #6097, relayed as a coordination comment on #6093,
and VERIFIED here before being accepted (a sibling's comment is not a primary
source — AGENTS.md §corpus-grep).

## The shape

A conditional class carries two free fields that appear together in exactly one
equation, multiplied. An equation on the PRODUCT `y_λ · χ^λ` pins NEITHER
factor, so an instance can realise any value at all. #6097 machine-checked it:

```lean
theorem yLambda_not_pinned (n : ℕ) (c : ℚ) (hc : c ≠ 0) :
    ∃ WD : WedderburnDecomp (R := ℚ) n 1 ℚ, ∀ lam, WD.y_lambda lam = c
```

Every nonzero rational is realised as the weight at every partition, by a
witness satisfying the whole class.

## Why it needs a new criterion — measured, not assumed

The carrier is not empty, not `: True`, not under-specified against its
docstring, and every field is a true sentence about a genuine Wedderburn
decomposition. So `proof-no-empty-prop-carrier`, `proof-claims-unencoded` and
the trivial-true detector all pass it, CORRECTLY. Confirmed by measurement on
2026-08-30: `WedderburnDecomp` appears **0 times** in the 368-entry vacuity
ledger and **0 times** among the audit's 133 candidates.

It is also outside what THIS session added. `valueOnlyProjects` (PR #6093, batch
9) reads the PROOF TERM; this defect is in the CLASS'S FIELD STRUCTURE, with no
proof term involved. Three distinct detectors now, on three distinct halves of a
declaration: statement (`defeqCollapse`), value (`valueOnlyProjects`), and
class-field graph (this one).

## Second instance, found while verifying the first

`QOU.Mathlib.HeckeAlgebra.WedderburnDecomposition` (line 118) is a different
member of the same family and is ALSO uncaught:

```lean
  /-- The sum `Σ_λ p_λ = 1`. -/
  blocks_sum_to_one : Prop
  blocks_sum_holds : blocks_sum_to_one
  /-- Pairwise orthogonality: `p_λ · p_μ = 0` for `λ ≠ μ`. -/
  blocks_orthogonal : Prop
  blocks_orthogonal_holds : blocks_orthogonal
```

The docstring states the equation; the field is an UNCONSTRAINED `Prop`
variable, so an instance may take `blocks_sum_to_one := True` and discharge
`blocks_sum_holds := trivial`. The audit reports 0 candidates for this file, so
this shape is invisible too. Whether one criterion covers both or they are two
(`underdetermined-product` vs `prop-valued-field-plus-its-own-proof`) is the
first design question.

## What is mechanical here

Both are decidable from the class's field graph without an agent verdict, which
makes this unusually cheap for this audit family:

- a field of type `Prop` (not a Prop-VALUED proposition, a bare `Prop`) whose
  only use is as the type of one sibling field;
- a field occurring in exactly one equation, multiplied by another field that
  also occurs only there.

## Note on where the verdict lives

Both classes are library Lean under `content/**/lean/QOU/**`, so neither has a
`.qa.json` sidecar and the verdict has nowhere to live except
`docs/audits/lean-vacuity-review-ledger.json`.

Deliberately NOT done on #6093: that PR drains the borrowed-name tiers and adds
two kernel predicates; a third detector is new scope.
