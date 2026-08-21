---
# qou-h56b
title: 'DEFECT: Mathlib/HeckeAlgebra.WedderburnDecomposition asserts nothing (Prop-variable fields) and has a registered global trivial instance'
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:25:51Z
updated_at: 2026-08-21T15:26:38Z
---

Found while scoping the TL_n route for the Wenzl 1988 discharge (PR #5358).
Not on the Wenzl path, so not fixed there.

Three distinct objects share the name:

| Name | Where | What it is |
|---|---|---|
| `Hecke.WedderburnDecomp` | `Hecke/Wedderburn.lean:72` | content-bearing class, NO instance anywhere |
| `Mathlib.WedderburnDecomposition` | `Mathlib/HeckeAlgebra.lean:118` | class with Prop-VARIABLE fields |
| `HeckeAlgebra.WedderburnDecomposition` | `HeckeAlgebra/Wedderburn.lean:68` | an `abbrev` for a Type |

The middle one is the defect. Its fields are

    blocks_sum_to_one : Prop
    blocks_sum_holds  : blocks_sum_to_one

i.e. a Prop *variable* plus a proof of it, not the proposition it names.
`instance triv_wedderburn` (same file, ~line 167) then discharges it globally
with `True` over `carrier := PUnit`. So the class asserts nothing and is found
automatically by typeclass search. `WenzlBridge.bridge_identity : Prop` +
`bridge_holds` has the identical shape.

This is `proof-claims-unencoded` / `true-class-field` (AGENTS.md §3b-tax), and
it is exactly what `IsOcneanuWeightSystem` was designed to avoid — that class's
docstring says its satisfiability witness is "deliberately **not** registered as
an `instance`, so typeclass search can never silently discharge the hypothesis."

Verified: `grep -rnE '(instance|example|def)[^:]*:\s*WedderburnDecomp\b'` over
content/**/lean/QOU returns EMPTY, so `Hecke.WedderburnDecomp.y_lambda` — the
corpus's only algebra-attached Ocneanu weight — is an unconstructed class field.

Fix direction: give the Prop-variable fields their actual propositions (they are
statable: the idempotents and the carrier are already in scope), and drop
`triv_wedderburn`. Renaming at least one of the three is a separate call.
