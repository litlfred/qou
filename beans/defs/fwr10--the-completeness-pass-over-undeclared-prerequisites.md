---
# fwr10
title: completeness pass over blocks that declare no prerequisites
status: todo
type: task
priority: normal
created_at: 2026-08-10T03:35:00Z
updated_at: 2026-09-26T11:03:26Z
parent: fwr6
---

Branch `claude/fwr10-completeness-pass-2026-08-10`. `fwr6` item 6.

The forward-reference arc was about edges that exist and point the wrong way.
This is the opposite defect: dependencies a reader needs that `uses[]` never
declares. It is the `uses-editorial-completeness` axis.

**Scoped by evidence, and it is much smaller than feared.** 510 blocks declare
no prerequisites, but only **110** name another block in their own prose, and
**41** name three or more. The other 400 name nobody — which is what a genuine
standalone looks like, and most of them will be exactly that.

| prose refs, none declared | blocks |
|---|---|
| 3 or more | 41 |
| 1-2 | 69 |
| none | 400 |

Among the 110, the kinds skew as you would expect if this is real: 37 prose, 27
remark, 22 proposition, 7 definition, 5 proof. A `-proof` block with an empty
`uses[]` is already an anomaly — proofs conventionally declare their parent.

**The prose-reference count prioritises a reading. It is never a source to
populate from.** Inferring `uses[]` from prose mentions is the failure the axis
exists to prevent, and a mention is a weaker claim than "the reader must go read
that first". `fwr5` rejected two of its eight candidates on exactly that
distinction — relatedness is not dependency.

Standard of evidence, from `fwr5` and `fwr7`: adding an edge asserts a reader
must go elsewhere first, so it carries a real burden, and one reading is not the
bar. `fwr7`'s two independent readers overturned eight of eight proposals that a
single earlier reader had reported.

---

**Status 2026-08-15: readings done, verification incomplete, nothing applied.**

Three readers covered the 41 high-signal blocks and returned **22
correctly-empty, 19 add, 37 proposed additions** — 0 unresolvable targets, 4
that would create a forward reference, 0 already transitively reachable.

The adversarial pass over those 37 **failed on the weekly API limit** partway
through. So every proposed addition has exactly one reading behind it, which is
below the standard `uses-editorial-review` now carries, and **nothing was
applied**. That is the correct state, not a stalled one.

## `prn1` compromises four of the correctly-empty verdicts

`prn1` established that two bulk prunes destroyed reachability for 856 edges,
785 still lost. Sibling parity — "every member of this family declares nothing,
so declaring here would be the anomaly" — cannot survive that, because a bulk
edit produces parity by construction.

Cross-checking the 22 `correctly-empty` verdicts against the prune-damage list:
**5 sit on blocks the prune stripped edges from.** Four need re-examination:

| block | edges the prune removed | verdict rested on |
|---|---|---|
| `rem:bsd-surreal-bound` | 10 | sibling parity across the five-member family |
| `rem:rh-surreal-bound` | 9 | sibling parity, called "unanimous" |
| `rem:yang-mills-surreal-bound` | 8 | "same template and same judgement as bsd" |
| `rem:archimedean-stpart-strategy` | 7 | anchor declared via `interprets`, redundancy |

The fifth, `def:adelic-substrate`, **stands**. Its reader did not use parity —
it found the owner decision in `78a570365d` that removed the edge deliberately
to break a mutual pair, and noted that restoring it re-opens a cycle. Right
answer, for a reason the prune cannot undermine.

**17 of 22 are untouched**, so the readings were mostly sound and the damage is
concentrated exactly where `prn1` predicted it would be.

## What remains

1. Re-verify the 37 additions with two readers who cannot see each other.
2. Re-read the four blocks above **without** the parity argument, checking the
   family's history first.
3. Only then apply. `prn1`'s restoration is the larger, separate question.
