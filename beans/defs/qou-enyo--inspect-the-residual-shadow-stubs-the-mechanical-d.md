---
# qou-enyo
title: Inspect the residual shadow stubs the mechanical drain cannot clear
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:12:11Z
updated_at: 2026-10-04T15:20:55Z
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
