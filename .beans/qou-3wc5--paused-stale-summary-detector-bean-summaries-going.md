---
# qou-3wc5
title: 'PAUSED: stale-summary detector — bean summaries going stale against corpus work'
status: todo
type: task
created_at: 2026-08-08T19:21:07Z
updated_at: 2026-08-08T19:21:07Z
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
