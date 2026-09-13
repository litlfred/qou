---
# qou-v0t8
title: precision-gates.sh tells you to commit a regenerated audit witness without checking whether your branch is behind main
status: completed
type: task
priority: normal
created_at: 2026-08-26T04:51:58Z
updated_at: 2026-09-13T13:08:26Z
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


## A THIRD reason not to commit these, and a retraction of my own call

While running prepare-merge on PR #5805 the precision gate flagged
`witness-provenance-audit.witness.json` stale and said to commit the
regenerated copy. I checked this bean's discriminator, found the
conditions inverted, and committed it:

    qou-v0t8 case   tree BEHIND main, ratchet BACKWARDS   913 -> 888
    that case       tree CURRENT (0 behind), FORWARDS     missing 96 -> 82

I also established the movement was main's, not mine — the branch adds
zero witness files and none of its six touched producers appeared among
the 18 changed entries.

**That reasoning was sound and the decision was still wrong.** Within
twenty minutes the PR went `mergeable_state: dirty`, and the conflict
was on exactly that file: main had regenerated it too.

So the rule is stronger than this bean originally stated. It is not only
that a behind-main tree walks the ratchet backwards. It is that a
**tree-measuring audit witness is a CONTENDED file**: main regenerates it
on its own cadence, so any feature branch that commits one acquires a
conflict with main, and the conflict recurs on every subsequent main
landing until the branch merges.

Revised guidance: **never commit a tree-measuring audit witness from a
feature branch**, regardless of ratchet direction or how current the
tree is. Revert it. The correct place to refresh one is a dedicated
chore commit on a branch that merges immediately, or main itself.

The suggested gate guard is unchanged (`rev-list --count
HEAD..origin/main`, suppress when non-zero) but is now known to be
INSUFFICIENT — it would have permitted this commit, since the tree was
current. The guard should suppress the 'commit the regenerated one'
instruction unconditionally on any branch with an open PR.

Resolution here: dropped the commit and rebased. Nothing was lost — the
movement was main's, which main now carries anyway.


## GUARD IMPLEMENTED 2026-08-30 — and the fix this bean proposed was not enough

`scripts/precision-gates.sh` no longer tells a feature branch to commit these.

**The proposed discriminator was `git rev-list --count HEAD..origin/main`, and
this bean's own third section already showed it insufficient** — the PR #5805
case was `0 behind` and still went `mergeable_state: dirty` within twenty
minutes. A behind-count guard would have waved it through. So the guard keys on
**which branch**, not on the behind-count; the behind-count is printed as
context only.

    on main             -> unchanged ("commit the regenerated one")
    on any other branch -> "DO NOT COMMIT THESE. Revert them." + both reasons

It also separates two things the old banner conflated: the **measurement** is
still worth reading (if the movement is the branch's own producer, that is a
real finding about the change), it is the **commit** that is wrong.

**Verified against the live case rather than hypothetically.** A full run on
branch `claude/precision-gates-stale-witness-guard-2026-08-30` flagged four
moved witnesses and printed the branch-mode text at `0 behind origin/main` —
the exact configuration mode 1 cannot catch. Both arms of the conditional were
also exercised in isolation with the branch name stubbed.


---

## SAFETY: the remedy this message prints can destroy a running producer's output (2026-09-13)

`scripts/precision-gates.sh` ends its "TREE-MEASURING AUDIT WITNESSES MOVED"
block by telling the reader:

>   DO NOT COMMIT THESE. Revert them:  `git checkout -- computations/`

**That is a glob over the whole directory, and it reverts files the gate run
never touched.** Hit today with the `qou-uiut` table mid-run: the gates dirtied
12 audit witnesses, but `git status -- computations/` showed **13** — the
thirteenth being `computations/hadron-knot-table.witness.json`, the live
per-atom output of the producer that was running at the time. The printed
command would have reverted it underneath the process.

This is not hypothetical in this repo: the same glob has already destroyed a
verified 40-minute run once, which is why the standing rule is to restore
witnesses **by explicit single path only**.

The message already knows which files moved — it lists them by name two lines
above. The remedy should list those same paths:

```sh
git checkout -- computations/audits/q0-anchor-consistency-audit.witness.json \
                computations/audits/witness-provenance-audit.witness.json \
                ...
```

or, better, the runner should emit the exact command from the list it just
built, so the reader never types a glob at all.

Note the failure is **silent and worst when things are going well**: a
long-running producer is exactly the state in which someone runs the gates to
check on the branch, and exactly the state in which the glob costs the most.
