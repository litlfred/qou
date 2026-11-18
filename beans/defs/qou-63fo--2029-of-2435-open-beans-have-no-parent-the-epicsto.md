---
# qou-63fo
title: 2029 of 2435 open beans have no parent — the epic/story layer is 10 epics deep
status: in-progress
type: task
priority: normal
tags:
    - beans-hygiene
    - reorg-2026-10-04
created_at: 2026-09-26T10:52:40Z
updated_at: 2026-10-04T15:16:00Z
parent: qou-5vkl
---

**Measured 2026-09-26. This bean exists to hold a DECISION, not to be worked
silently. Nothing here has been done.**

## The measurement

```
total beans                5336
open (todo/in-progress/draft/open/'')   2435
  of those, NO parent      2029   (83%)

open by type   task 2202 | milestone 127 | epic 17 | bug 77 | feature 11 | research 1
epics          21  — only 10 have any child
milestones    374  — only 117 have any child
```

So the hierarchy exists but is thin: **2,029 open beans sit at the root**, and
the structure that does exist is mostly unused (11 of 21 epics and 257 of 374
milestones are childless).

## Why it is like this, and it is not carelessness

`AGENTS.md` work-plan §1 tells every session to create a **session milestone**
plus child tasks. That produces the 374 milestones. What it does not produce is a
layer ABOVE the session: a session milestone is per-branch and per-day, so
long-running arcs (the Φ₁ work, the convention-D excision, the Lean vacuity
drain) accumulate as sibling milestones with no common epic. The 21 epics that do
exist were created by hand, ad hoc.

Note also `qou-b2cl`: 13 of the orphans were parented and lost their parent to a
deletion. So "orphan" is at least two populations.

## The decision, and the four options

**(A) Do nothing.** The default. Cost: nothing now. What it leaves: `beans list`
returns 2,435 open items in no hierarchy, the §4 idle-backlog policy ranks them
without structure, and the next agent re-reads the same flat list. This is
survivable — it has been for months — and it is the honest baseline.

**(B) Fix only the known-broken structure.** The 13 broken parents (`qou-b2cl`),
the 4 off-vocabulary types (`qou-144c`), the 47 off-vocabulary statuses
(`qou-20vg`). ~64 beans, each needing a read. Cost: bounded, an hour or two.
Risk: low, and `beans check` → 0 verifies it. Commits to nothing further. **This
is already scoped as three sibling beans and does not need this one.**

**(C) Build an epic layer over the live arcs only.** Identify the ~10-20
long-running themes, create one epic each, and parent the open beans that clearly
belong. Cost: real judgement per bean, so it cannot be scripted; a few hundred
beans at most if restricted to `in-progress` (578 repo-wide). Risk: a wrong
parent is worse than no parent — it hides a bean under a theme nobody is reading.
Commits to maintaining the epic layer, or it rots like the 11 childless epics.

**(D) Mass-reparent all 2,029.** Cost: a large mechanical sweep. Risk: high, and
this is squarely what the 2026-09-07 **ASK-THE-OWNER** directive gates — it is
neither a precision increase nor corpus-derived, because no artifact in the repo
decides which epic a given bean belongs to. **Not recommended and not started.**

## Recommendation — agent judgement, not a finding

**(B) now, and (C) only for `in-progress` beans, if at all.** B is bounded and
verifiable; C is where the value is but it is also where a bad call does damage,
and 578 in-progress beans is already a lot of individual judgement. D should not
happen: an orphan bean is findable by search, whereas a mis-parented bean is
findable only by someone who guesses the wrong epic.

The cheapest real improvement may not be reparenting at all: `AGENTS.md` §1 could
ask a session to name an **existing epic** as its milestone's parent when one
applies, which stops the problem growing without touching the 2,029. That is a
one-paragraph docs change and is an owner call.

## Blast radius in real terms

Who reads this structure: the `session-start-coord-sweep.sh` hook (prints the
active bean work-plan every session), the §4 idle-backlog policy (picks what an
idle agent works on), `todo-manager` / `bean-coordination` skills, and the
`work_plan_prime` MCP tool in folio-assistant, which exposes the work plan to any
MCP agent. A hierarchy change is therefore visible to every future session, which
is the argument both for doing it well and for not doing it fast.

- **Round 95 (`litlfred/qou#8426`)**: Advanced in `feat/round95-layout-lowerbound-bondrule-maxcontact-simplex-43c1` (Commit 1 `d482ea2750e00fbd6e9e74457e935101b2f8b093`, Commit 2 `8ed5dd0ff69b4804c5e40f393e7c9157a2067a42`, probe sha256 `8b786124c3dfda15d0d1672a05f3bc16f486d17a5f41250533162305ad901679`).
