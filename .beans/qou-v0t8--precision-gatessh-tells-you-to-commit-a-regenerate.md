---
# qou-v0t8
title: precision-gates.sh tells you to commit a regenerated audit witness without checking whether your branch is behind main
status: todo
type: task
created_at: 2026-08-26T04:51:58Z
updated_at: 2026-08-26T04:51:58Z
---

## The instruction

`scripts/precision-gates.sh` regenerates the tree-measuring audit
witnesses, and when one moves it prints:

    STALE COMMITTED AUDIT WITNESSES — a substantive field moved:
      computations/audits/q0-anchor-consistency-audit.witness.json
      computations/q0-value-drift-audit.witness.json
      computations/witness-raw-float64-audit.witness.json
      The committed copy was stale. Commit the regenerated one AND say
      which count changed — and check whether the movement is yours or
      main's before claiming it (git log the newly-listed entries).

The last clause is the right instinct and the wrong discriminator. It
asks *which commit* moved the number. The question that actually decides
it is *which tree was measured*.

## What it misses

These audits count things across the working tree. On a branch that is
**behind** main, the working tree is missing main's newer commits, so
regenerating them yields a number that is correct for the branch and
**wrong for main** — and committing it silently walks main's recorded
progress backwards.

Measured here, on a branch 46 behind / 19 ahead:

    witness-raw-float64-audit   drained_files   913 -> 888
    q0-anchor-consistency       Q0_OK           972 -> 973
                                Q0_ANCHOR_MISSING 1649 -> 1648
    q0-value-drift              proton-pin     1682 -> 1683
                                plus ~4200 row-order shifts

`drained_files` is the one that shows the shape plainly. The baseline
drains and never grows — that is the whole mechanism. Committing 888 over
913 would have recorded 25 files as *re-dirtied* when nothing was; they
were drained by main commits this branch does not have. The gate would
have walked the ratchet backwards while reporting green.

And the "is it yours or main's?" check does not catch it: `git log` on the
newly-listed entries finds main commits, which reads as "main's movement,
so commit it" — the exact opposite of the right action.

## Both committed copies agree, which is the tell

    HEAD                913
    origin/main         913
    regenerated here    888

The committed value is not stale at all. Only *this tree* is.

## Suggested fix

Before printing the STALE banner, check `git rev-list --count HEAD..origin/main`.
If it is non-zero, say so and suppress the "commit the regenerated one"
instruction: on a behind-main branch the correct action is to rebase and
re-run, never to commit. Same shape as the `b28296c0d` class (an audit
witness regenerated in a session measures that session's tree), but a
distinct mechanism — branch lag rather than session artifacts — so the
existing `b28296c0d` guidance does not cover it.

Not fixed here: this bean is the finding. The three witnesses were
reverted rather than committed.
