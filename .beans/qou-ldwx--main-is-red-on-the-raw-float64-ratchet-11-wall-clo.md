---
# qou-ldwx
title: 'main is RED on the raw-float64 ratchet: 11 wall-clock ''seconds'' fields in an otherwise exemplary NO-FLOAT64 witness'
status: todo
type: task
priority: normal
created_at: 2026-09-13T14:35:27Z
updated_at: 2026-09-13T16:18:07Z
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
