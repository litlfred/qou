# Grading the 783 lost edges by corroboration, not by loss count

Generated 2026-08-10. Companion to
[`2026-08-10-transitive-prune-overreach.md`](2026-08-10-transitive-prune-overreach.md)
(bean `prn1`, PR #4910). Bean: `fwr11`, PR #4921.

`prn1` established the damage — two bulk transitive prunes removed **783**
dependencies that no surviving path replaces, across **335** blocks — and left
it unfixed on the correct grounds that *bulk restoration repeats the original
error*. It proposed working the backlog **highest-loss first**.

This audit argues for a different ordering, and supplies it.

## Loss count is the wrong priority key

A block that lost 15 edges is not thereby better evidence than a block that
lost 4. What distinguishes a restorable edge is **whether a second, independent
source still attests to it** — and one exists: the block's own prose. If the
prune removed `A → B` *and* A's narrative still names B by label, two unrelated
records agree that A leans on B. If the prune removed `A → B` and A's prose
never mentions B, the git history is the only witness.

Those are different evidentiary situations and should not share a queue.

## The measurement

Every still-unreachable edge from the `prn1` audit, intersected with the labels
each source block still names in its own `.md` (inline `](#label)` links and
`` `label` `` mentions, resolved against the corpus):

| | edges | blocks |
|---|---|---|
| **Corroborated** — pruned *and* still named in the source's prose | **170** (21.7 %) | 82 |
| Prune-record only — no prose mention survives | 613 (78.3 %) | 253 |
| total | 783 | 335 |

Blocks whose loss is *fully* corroborated are the strongest restoration
candidates in the corpus:

| corroborated / lost | block |
|---|---|
| 8 / 8 | `rem:yang-mills-surreal-bound` |
| 8 / 8 | `rem:p-vs-np-surreal-bound` |
| 9 / 10 | `rem:bsd-surreal-bound` |
| 8 / 9 | `rem:rh-surreal-bound` |
| 4 / 4 | `rem:hecke-charge-mass-duality` |
| 4 / 4 | `prf:quantum-dilogarithm-stratified` |
| 4 / 4 | `prf:phi-q-categorical-truncation` |
| 10 / 15 | `rem:millennium-unification` |
| 5 / 6 | `rem:q-metric-contact-deformation` |
| 4 / 5 | `prop:delta-max-uniform-bound` |

## This also closes a detection gap `prn1` identified

`prn1` observed that `rem:millennium-unification` lost 15 edges and *is not
empty*, so **no completeness scan would ever have surfaced it**. That is true of
the scan `fwr10` uses, which selects blocks with an **empty** `uses[]`. It is
not true in general.

A "declares some, names more" scan — blocks with a non-empty `uses[]` that still
name undeclared labels in prose — surfaces **944** blocks corpus-wide, 289 of
them naming three or more undeclared. `rem:millennium-unification` is its
top row. Coverage of the prune victims:

| scan | victims surfaced |
|---|---|
| empty-`uses[]` (the `fwr10` scope) | 29 / 80 now-empty |
| declares-some-names-more (this audit) | 116 / 255 non-empty |
| neither | 190 / 335 |

So the block `prn1` named as undetectable is detectable; but **57 % of the
affected blocks are genuinely not**, and for those the prune record is the only
evidence there is.

## What corroboration is not

Prose corroboration is **evidence for a reading, never a licence to populate.**
The standing rule on this axis is that *relatedness is not dependency*: a
mention is a weaker claim than "the reader must go read that first," and prior
passes rejected candidates on exactly that distinction. A corroborated edge has
earned a *reading*, not a restoration. Two records agreeing that A mentions B
still does not establish that a reader of A must have read B first.

Nor is the 21.7 % a measure of how much of the prune was wrong. `prn1` already
established that all 783 destroyed reachability. Corroboration measures only
how much of it can be adjudicated **from the corpus as it stands today**,
without reconstructing intent from git history.

## Recommended tranches

1. **170 corroborated edges, 82 blocks** — read each against its prose; restore
   what survives the relatedness-is-not-dependency test. Two sources, and the
   fully-corroborated blocks above are the natural head.
2. **613 prune-record-only edges** — read against the block's argument, not its
   mentions. Slower, no corroboration, and the honest place to accept that some
   will not be recoverable by reading at all.

Ordering within (1) should be by *fraction* corroborated, not by absolute loss:
`rem:yang-mills-surreal-bound` at 8/8 is a cleaner case than
`rem:millennium-unification` at 10/15.

## Separately: the dead-field defect does not overlap this one

`fwr11` found 12 proof blocks declaring their parent through a field nothing
reads (`of`, `proofOf`). Three of those blocks were also hit by the prune —
but **none of the nine edges `fwr11` added were among the pruned ones**. The
two defects co-occur in the same neighbourhood without sharing a single edge.
They are independent wounds and want independent fixes.
