---
# qou-h56b
title: 'DEFECT: Mathlib/HeckeAlgebra.WedderburnDecomposition asserts nothing (Prop-variable fields) and has a registered global trivial instance'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T15:25:51Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-59vq
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


## 2026-08-30 — the "registered global trivial instance" half is FIXED; the class shape is not

Re-measured while answering a #6097 coordination comment on PR #6053.

**Stale:** *"`instance triv_wedderburn` … discharges it globally with `True` over
`carrier := PUnit`. So the class … is found automatically by typeclass search."*
Both `triv_hecke` and `triv_wedderburn` have been **demoted from `instance` to
`def`**, and the demotion is documented in the file itself with a measured blast
radius — *"**one** error, `triv_wedderburn` below, fixed in place. Nothing else in
the corpus depended on the global resolution"* — plus a probe at
`docs/audits/2026-08-23-trivial-global-instance-probe.lean`.

Verified: `grep -rnE "^\s*(noncomputable )?instance.*(IwahoriHeckeAlgebra|WedderburnDecomposition)"`
over `content/` returns **no live instance** of either. So `#synth` no longer
finds a trivial witness, and the specific inertness this bean was opened for is
gone.

**Still true, and wider than the bean says.** The defect is the class *shape*,
and it is not confined to `WedderburnDecomposition`. `QOU/Mathlib/HeckeAlgebra.lean`
carries **12** bare `: Prop` fields, among them the Hecke algebra's own defining
relations:

```lean
hecke_relation : Prop      hecke_holds : hecke_relation
braid_relation : Prop      braid_holds : braid_relation
far_commute    : Prop      far_commute_holds : far_commute
markov_axiom   : Prop      squares_sum_factorial : Prop
blocks_sum_to_one : Prop   blocks_orthogonal : Prop
bridge_identity   : Prop   …
```

So `IwahoriHeckeAlgebra R n q` **cannot state its own relations** — they are
opaque `Prop` variables, and `triv_hecke` (still present, as a `def`) sets all
three to `True`. Any future instance can do the same, and nothing detects it:
there is no `sorry`, no `axiom`, no `: True := trivial` on a theorem for the
vacuity audit to catch. This is §3b-cond point 5 (the class must axiomatise
*hypotheses*, not carry its conclusion as a field) and §3b-tax
`proof-claims-unencoded`, at the level of a whole file.

**Cross-reference.** #6097 machine-checked the same disease one class over, in
`QOU.Hecke.WedderburnDecomp`: `yLambda_not_pinned` exhibits, for every nonzero
rational `c`, an instance with `y_lambda lam = c` at every partition — because
`block_scaling` constrains a *product* of two free fields, `χ^λ` being a field
rather than a computed trace. That one is **live**; this one's live half was
already drained.

**What would actually fix it, and its prerequisite.** `χ^λ` has to become
`Matrix.trace (ρ_λ x)` for `ρ_λ : H_n(q) → M_{f^λ}(R)`, and the Hoefsmit /
seminormal construction of `ρ_λ` is given by the action on `T_w`. PR #6053's
`basisTwOfField` is that prerequisite, now available over a field. Two cautions
recorded by #6097 and worth keeping: Mathlib's
`exists_algEquiv_pi_matrix_divisionRing` gives an **unindexed** existential
product of matrix rings and supplies none of the `Partition n` indexing that is
the whole difficulty; and `QOU.Hecke.SpechtDimension` is
`{ dim : ℕ, positive : 0 < dim }` — verified — a free natural with the
hook-length formula only in its docstring, so `f^λ` would need tying to `λ`
before `M_{f^λ}` means anything.

- Round 74 (`lane-e667`): Formalized `qou-gd90`, `qou-gzsp`, `qou-h56b`, `qou-hah4`, `qou-luq7` in `QOU.Foundations.PeriodicStateTriangularInversionWeightSpaceEquivarianceBlockScalingWeightedDecomposition` with 80-dps `mpmath` 2-commit witness stamp (`90a852e5501c98f68c32c2d227ae5dc2719d5bb6` -> `ae44845094878bbd65a4bf4b8065339b39d10e57`, `scriptHash=0a79a20314ed167467fce31136d40aeaf330204cb85b728199138a30d69455e2`) in PR `litlfred/qou#8399` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8399, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
