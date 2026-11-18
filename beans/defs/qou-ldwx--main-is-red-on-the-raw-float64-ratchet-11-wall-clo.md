---
# qou-ldwx
title: 'main is RED on the raw-float64 ratchet: 11 wall-clock ''seconds'' fields in an otherwise exemplary NO-FLOAT64 witness'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T14:35:27Z
updated_at: 2026-10-04T15:21:24Z
parent: qou-9nnz
---

---

## UPDATE 2026-09-13T16:20Z — it is a RECURRING SOURCE, not one file

A second witness from the same arc landed on `main` within hours and trips the
ratchet identically:

| witness | fields | path | landed |
|---|---:|---|---|
| `deltalambda/rev-excess-scaling-exponent.witness.json` | 11 | `/scaling_R2/[]/seconds` | `7a85ddf411e` |
| `deltalambda/rev-exact-maximiser-small-n.witness.json` | **6** | `/exact_rows/[]/seconds` | `786bd7d4c2b` |

Both verified main's by the same three checks: byte-identical to `origin/main`'s
copy (`git diff origin/main --` empty), **absent from main's own baseline**, and
landed by `qou-hok7` commits. Neither is any branch's.

**Both are bare producers** — `scriptFile: None`, no `WitnessBuilder` envelope.
That is the part worth acting on: the arc is writing witnesses by hand, so each
new one re-introduces the same field and nothing in the producer path can stop
it. The count will keep climbing as the arc runs.

So the recommendation in the original entry — *"`qou-hok7`'s author fixes it on
their next run, zero marginal cost"* — is now **too weak**. It fixes the two on
disk and not the third. The fix belongs at whatever writes these files: either
route them through `WitnessBuilder` (which would also give them provenance they
currently lack), or serialise `seconds` as a string in the hand-rolled writer.

**Still not fixing it here**, and the reason is unchanged and now stronger: it
is another arc's live work, moving hour by hour, and `rev-excess-scaling-exponent`
alone costs ~40 min to regenerate. Touching a producer whose author is actively
iterating on it would collide.

**Total inherited-red on the ratchet: 17 fields across 2 witnesses.** Any branch
rebasing onto `main` now sees `NEW: 2`. Both are `qou-hok7`'s.


## 2026-09-14 08:10 — count check #5: 4 → 1, and I OVERSTATED this bean's own finding

**Correcting my own entry from three hours ago.** Check #4 recorded the count
going 2 → 3 → 4 and called it *"the ordinary rate at which `main` adds
raw-float64 fields that no producer-side fix catches"*. The last clause is
wrong, and the evidence is main's next 80 commits.

Measured on `origin/main` `8b7b663b566`:

    NEW: 1   (was 4)
      1  computations/audits/braid-encoding-audit.witness.json   main-identical

All **three** `qou-hok7` entries are gone, and they were **drained at the
producer, not baselined** — `dirty_now = 0` AND `in_baseline = None` for each,
by `a6716329856` *"witness(qou-hok7): regenerate the three producers behind
the corrections"*.

**So the population CHURNS; it does not accumulate.** Entries arrive from
ordinary `main` work and the owning arc drains them, here within ~14 hours.
What this bean legitimately establishes is that **a NEW-count snapshot is
not a backlog** — it is a rate measurement, and reading one as evidence of
neglect (which check #4's wording invites) is wrong.

Trajectory, complete:

    2026-09-13 ~16:00   2 entries, 17 fields
    2026-09-13 ~19:15   3 entries, 24 fields
    2026-09-14 ~06:05   4 entries, 25 fields
    2026-09-14 ~08:10   1 entry,   1 field    <- three drained at the producer

**What this does NOT change:** every one of these was correctly identified as
*not this branch's* and correctly left alone. The operational rule stands —
verify byte-identity against `origin/main`, do not drain another branch's
fresh output, record and move on.

**Where the wrong framing reached:** check #4's text in this bean, and the
commit message of `f024eebdd22` on
`claude/raw-float64-drain-2026-09-13`, which repeats "the ordinary rate at
which main adds raw-float64 fields that no producer-side fix catches". The
commit is immutable; this entry is the correction of record. The PR body for
#7318 says only that the entries are inherited and byte-identical, which is
accurate and needs no change.
