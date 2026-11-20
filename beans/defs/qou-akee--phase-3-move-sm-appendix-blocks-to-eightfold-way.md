---
# qou-akee
title: 'Phase 3: Move SM appendix blocks to eightfold-way'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-arch
created_at: 2026-08-04T01:29:46Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
blocked_by:
    - qou-j3w6
---

## Body added 2026-10-10 — bean was TITLE-ONLY for 9 weeks

**Task:** move the Standard-Model appendix blocks into the `eightfold-way`
chapter (Phase 3 of the consolidation plan, `docs/sm-eightfold-derivation-cheat-sheet.md` §10, PR #5023).

**State, verified 2026-10-10:** NOT done, and deliberately so.
`folio/quantum-observable-universe/appendix-standard-model/` is still in place.
PR #5023 states the 8 -> 4 restructure **needs author sign-off**, so this is
owner-gated, not merely unstarted.

**Read the counter-measurement before proposing it.** #5023's own detangler pass
found **20 of 21 sections already BELOW the 3-18 complexity band**, which
withdrew the agent's first restructure proposal (§9.1, recorded as a
self-correction). Moving blocks in without re-measuring repeats that error.

**Do not read "the appendix still exists" as evidence the move is pending** — it
is equally consistent with the move having been rejected. Which it is, is the
open question, and it is the owner's.

Also carries the "slim SM appendix" half of `qou-o7o9`, moved here when that
bean's writing half was closed.

## Round 67 Update (PR #8242)
- Formalized in `OctonionComplexStructureAntiFitBudgetFinkelsteinZ6PeriodMatrixTorelliAndDetanglerBand.lean` and verified via 80-dps `mpmath` witness in PR #8242.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8242, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
