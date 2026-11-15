---
# qou-y48h
title: Triage beans whose status field lags their own recorded outcome
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T13:56:57Z
updated_at: 2026-10-04T15:25:10Z
parent: qou-5vkl
---


## Why this exists

`vred` ("Content validation is RED on main — 32 issues") sat at
`status: todo`, `priority: high`, `type: bug` while its own body carried a
`## 2026-08-08 — RESOLVED` section. An agent picking the backlog by
priority reads it as the highest-value open bug in the repo and re-does
finished work. This one cost ~10 minutes before the body was read.

Verified on `origin/main` @ 21ac80c881 before closing it:

    bun run scripts/run-validate.ts folio/quantum-observable-universe
    → ✓ Valid — 5 issue(s)      (4 ⚠ + 1 ℹ, zero ✗)

Better than the 13 the bean recorded, so the fix held and the corpus
improved since. `vred` is now `completed`.

## Scope — and why this is NOT a bulk status sweep

A scan for open beans whose body contains a resolution-style verdict
heading returns **35** (negations such as "Definition of done", "Why not
done here", "NOT CLOSED" excluded; the unfiltered number is 95 and is
meaningless).

**Most of the 35 are correctly open.** The verdict heading almost always
announces a *sub-item* closing, not the bean:

| bean | heading | actual state |
|---|---|---|
| `qou-orph` | "STEP 1 DONE for 153 of the 757 orphans" | 604 left |
| `qou-7loj` | "CODE FIXED and verified; WITNESSES STILL STALE" | says so itself |
| `qou-krvm` | "PARTIAL — (i) DONE, (ii) REFUTED" | partial |
| `qou-6e88` | "DONE — hypothesis added, `≤` half proved" | one half |
| `qou-gkco` | "CONTINUATION STEP CLOSED; the gap moved" | moved, not gone |
| `qou-htk4` | "Additive direction CLOSED — one shape left" | one shape left |

No regex separates "this bean is finished" from "a step inside it
finished" — only reading the bean does. So this item is a **read-per-bean
triage**, and any agent taking it must not bulk-flip on heading text.

## Method for whoever takes this

1. Read the bean, not just its headings.
2. Re-run the check the bean itself names, against current `main`. A
   recorded outcome is evidence about the past; the gate is evidence
   about now. (For `vred` the two disagreed in the *good* direction —
   13 warnings recorded, 5 measured.)
3. Flip to `completed` only when the bean's own definition of done is
   met in full. Leave partials open and, if useful, add a line naming
   what remains.
4. Genuine sub-item progress that leaves the bean open needs no status
   change at all.

Candidates worth reading first, because their verdicts read as whole-bean
rather than sub-item: `cmiy`, `qou-f7je`, `qou-n1dj`, `qou-58r5`,
`qou-8vt2`, `qou-vhv6`, `qou-z3k1`.

## Priority

Normal, not high. It misleads the §4 idle-backlog policy, which is real
but bounded — unlike the 14,688 duplicate beans (`qou-2ryn`), it does not
drown the signal, and one misread bean costs minutes, not a session.
