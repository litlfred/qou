---
# qou-1ccx
title: 'GAP (detector): lean-self-assuming-audit.py rule 2 misses the ANONYMOUS instance binder - [C X] + ClassName.field. Successor cause to qou-24m2, which fixed the NAMED [ctx : C] case'
status: in-progress
pr: 8350
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-15T06:44:54Z
updated_at: 2026-10-04T15:19:29Z
parent: qou-5vkl
---

## MEASURED 2026-09-15 — three probes, one variable each

Found while running the required self-assuming audit on new work for bean
`qou-h0ou`. This is the SUCCESSOR cause to `qou-24m2`, not a duplicate of it:
`qou-24m2` (fixed 2026-08-22) taught rule 2 to parse `[name : T]` and `{name : T}`
binders and to match a projection APPLICATION. That fix works — probe C below
confirms it live. The residual case is an instance binder with NO NAME AT ALL.

Identical mathematics in all three probes (same class, same conclusion); only the
binder spelling and the projection differ:

| probe | binder | proof term | audit verdict |
|---|---|---|---|
| A | `(ctx : HasClaim X)` round, named | `ctx.claim` | 1 class-field-is-conclusion |
| C | `[ctx : HasClaim X]` instance-implicit, NAMED (the qou-24m2 fix) | `ctx.claim` | 1 class-field-is-conclusion |
| B | `[HasClaim X]` ANONYMOUS | `HasClaim.claim` | **0 candidates** |

Mechanism: with an anonymous binder there is no name to enter the binder map, so
rule 2's `binders.get(bname)` is handed the CLASS name, misses, and `continue`s.
`ClassName.field` is the only way to write the projection when the instance has
no name.

## What it hides, confirmed by hand

`QOU/QuantumObservableUniverse/GaugeTheory.lean`'s whole equation-of-motion
apparatus is spelled that way, so the audit scores 0 candidates on that file:

  variational_einstein    := HasCategoricalEOM.einstein      (:197 vs field :159)
  variational_yang_mills  := HasCategoricalEOM.yang_mills
  variational_transport   := HasCategoricalEOM.transport

Each class field's declared type is character-for-character the theorem's
conclusion — AGENTS.md §3b-cond item 5's vacuous self-assuming projection.
Verified by reading :159 against :197, NOT by the detector.

## Scale — LOWER BOUND, and it is a count of the SHAPE not of defects

A narrow scan (class declared in the same file, binder anonymous, proof term
`ClassName.field`) finds **91 declarations across 2898 .lean files** in the QOU
library. Calibrated against the three probes: flags B, correctly ignores A and C.

🛑 Rule 2 additionally compares the field's declared TYPE against the conclusion,
and a class carrying genuine HYPOTHESES that a theorem composes is legitimate
(`q_bkm_criterion` is the verified exemplar). `qou-qf8t` measured and REFUTED the
tempting shortcut that counting distinct field projections discriminates the two.
The scan makes no type comparison. Read 91 as "candidates the audit cannot even
consider", never as 91 violations.

## Deliberately NOT fixed here

Row 43 of `docs/audits/2026-08-15-detector-blindness-taxonomy.md` records that
fixing this same script's scan scope destroyed 106 of 329 committed
adjudications. Widening rule 2 re-classifies the whole
`docs/audits/lean-vacuity-review-ledger.json` — an owner call, not a side effect
of a branch sent to do something else.

Cross-ref: `qou-24m2` (the named-binder cause, fixed), `qou-sa5c` (adjudication
of the 5 that fix surfaced), `qou-qf8t` (type-equality half, completed),
`qou-h0ou` (the branch this was found on),
`docs/audits/2026-09-15-rank-two-field-space-for-the-variational-derivative.md` §4.


## Round 57 Implementation (PR #8350)
- Implemented on branch `claude/round57-trd0-9nnz-fixes` (commit `35175f892e4827e826a23a3d007073dd800ff733`, https://github.com/litlfred/qou/pull/8350).
