---
# qou-enyo
title: Inspect the residual shadow stubs the mechanical drain cannot clear
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:12:11Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
---


## Residue after two drain passes

Of the 13 shadow stubs remaining from the 2026-06-14 manifest's 147:
**11 are now deleted** (7 in PR #4831, 4 in the follow-on). What is left
needs per-item judgement, not a sweep:

- `mass-theory/reidemeister-mass-invariance.lean` — **must stay.** It
  matched only on a shared decl name; it carries a real proof
  (`obtain` / `refine` / `div_pos` over
  `ReidemeisterMassInvarianceContext`). Recorded so a future sweep does
  not delete it.
- The remainder need the ref-leaf check plus a read of the sibling
  before any action.

## Standing rule this bean exists to enforce

**"A library twin exists" is not sufficient grounds to delete a
sibling.** The sibling must independently be verified vacuous by
reading it. This is the same failure shape as the comment-stripping
trap: the cheap signal is directionally right and specifically wrong.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8403, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
