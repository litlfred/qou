---
# qou-3wc5
title: 'PAUSED: stale-summary detector — bean summaries going stale against corpus work'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T19:21:07Z
updated_at: 2026-10-04T15:21:59Z
parent: qou-5vkl
---


> **⏸ PAUSED by owner, 2026-08-08.** Captured, not being worked. Do not start
> without checking back — it touches shared tooling.

## The pattern

Three instances in two days, all the same shape: **a summary went stale against
work recorded elsewhere in the same corpus, and the next agent read it as
current.**

| artifact | said | reality | cost |
|---|---|---|---|
| `qou-wgnx` top summary, headed *"read this first"* | Stokes multipliers open, item #1 | its **own entries 21–23** concluded trivial | PR #4790: full re-derivation + a wrong "still open" claim published to a merged PR |
| `qou-c1ln` row 2 | needs "the argument principle, and nothing else" | both halves landed in #4770 (`argument_principle`, `qThetaC_eq_zero_iff`) | a session-recommendation aimed at closed work |
| `qou-c1wr` | recommended by me as the live follow-on | `status: done`, both actions discharged | a wrong recommendation to the owner |

Rough cost: about two sessions.

## Why the existing discipline does not catch it

`qou-wgnx` entry 23 already records the standing lesson — *"grep the corpus
first, especially when the target is phrased as 'open'"* — written by the agent
who had just been bitten. **That lesson has a hole, and all three instances fall
in it:** grepping first does not help when the thing you find is itself the
stale artifact. Two of the three were *found* correctly and still misled,
because the summary at the top of the bean contradicted its own later entries.

The third is simpler and cheaper to catch: I recommended a bean without reading
its `status:` field.

## Shape of a fix (unscoped — do not build without sign-off)

Cheapest first:

1. **`status:` respected at read time.** A recommendation or "next item" that
   names a bean whose status is `done`/`completed`/`scrapped` is a hard error.
   Catches instance 3 outright and costs nothing.
2. **Summary-vs-entries drift.** Flag a bean whose top summary block is older
   than its newest dated entry *and* whose Open list names an item that a later
   entry marks closed. Catches instances 1 and 2. Needs a convention for where
   the summary ends — today it is `## Achieved` / `## Open` by habit, not by
   rule.
3. **Cross-artifact staleness.** A bean row citing a "missing lemma" whose name
   now resolves in the Lean tree. Most valuable, most work; instance 2 is
   exactly this and would have been caught by a name lookup.

## Deliberately not decided here

Whether this belongs in `beans check`, in a watcher skill
(`local/todo-manager`, `local/bean-coordination`), or as a session-start hook.
All three touch shared tooling, which is why this is paused rather than started.

Relates: `qou-wgnx`, `qou-c1ln`, `qou-c1wr`, `qou-vkg5`.

## Measurement 2026-09-14 — a THIRD angle, and it sizes the population

Contributed as data only. **The pause is respected: nothing was built and
nothing was swept.** The shape below is not covered by items 1-3 above — item 1
is a *read-time* check (recommending a bean whose status is done), item 2 keys
on `## Achieved` / `## Open` blocks which this bean itself calls 'habit, not
rule'. This one keys on nothing but the front-matter and a heading.

**The shape:** a bean whose `status:` is `todo`/`in-progress` while its own
body carries a heading saying RESOLVED / FIXED / CLOSED / DONE / COMPLETED.
It is the sibling of qou-sxyr's finding (6 of 10 sp00 bricks open while proved)
with the evidence inside the bean rather than in the Lean tree — so it needs no
environment, no oleans, and no resolution step.

**Measured over all of `.beans/`:**

    candidates (any resolution heading, status still open)   438
      heading is a NEGATION ('not resolved', 'partially')     77
      open language AFTER the last resolution heading        211
      body mentions conjecture / sorry (rule 13a applies)      63
      -> survives all three filters                            87
                                                     todo 229 / in-progress 209 (pre-filter)

**Quote 87, never 438.** The three filters remove 80%, and the raw 438 is what a
naive scan reports — the same over-match the detector-blindness taxonomy
catalogues. 87 is still a CANDIDATE count, not a defect count: each one needs a
per-bean check that the fix is actually on main. Known non-defects already
visible in the 87: `mlnr` is an EPIC (stays open by design while sub-items
close), and `qou-mnrd` ('main is red on its own float64 ratchet') is a class
AGENTS.md records as recurring, so a resolved instance does not close it.

**One verified and closed, as the calibration case:** `qou-rfhj` said RESOLVED
in its body on 2026-09-11 with `status: todo`. Checked `dee94bf5bf` is an
ancestor of main and that the probe's only remaining mention of the stale
premise is a comment describing the fix. Closed. That is 1 of 87 checked; it
says the class is real, not that the other 86 are.

**Not proposed, deliberately.** Automating this is the thing the owner paused,
and sweeping 87 beans is not exempt under the 2026-09-07 ASK-THE-OWNER
directive. The value of this entry is that when the pause lifts, the scope is
already sized.

- **Round 93 (`litlfred/qou#8421`)**: Advanced in `feat/round93-strip-kindratio-kohnokz-resolvent-affinenorm-43c1` (Commit 1 `53341df5af4d7e77e4fbee34d9b0bead3b0b6187`, Commit 2 `2f40c0d2d071ec6bb42d20002fb53171245df01c`, probe sha256 `3d8255f15bbdfc2d9c41114f8ac21a1bec3996e0b1546ef080914210757c628c`).
