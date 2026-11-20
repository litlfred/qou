---
# qou-tfv2
title: 'GAP: ground_state_ordering_argmin_sweep fails its own cross-check at 28% on main'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T11:05:30Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
---

Found at BASELINE while converting `hecke_core_symbolic` to convention D
(`qou-cds1`, PR #5622). **Not caused by that conversion** — the run below is on
an unmodified tree, before any edit.

## The failure

    python3 computations/probes/ground_state_ordering_argmin_sweep.py
    -> exit 1, "CROSS-CHECK FAILED — aborting."

Its own closed-form-vs-corpus check, worst relative difference **0.283831**:

| word | closed | corpus | rel |
|---|--:|--:|--:|
| `pnnpn`   | -1.82504728389525016   | -2.54834668012442578 | 0.2838 |
| `pne`     | -0.0431071741710609166 | -0.0308107381956574123 | 0.0123 |
| `pnpnee`  | -2.60732294975677777   | -3.6013089037495837  | 0.2760 |
| `npnpnee` | -2.68461227788587562   | -3.65304265405844811 | 0.2651 |

## It is NOT the trace convention — checked, because that was the obvious guess

The corpus/closed ratios are **1.3963, 0.7150, 1.3812, 1.3610**. A convention
C→D discrepancy would show a uniform power of `z_D/z_C = 1.227044`: 1.227 at
length 1, 1.5056 at length 2, 1.8475 at length 3. None of the four match any of
those, and one ratio is *below* 1 while the others are above — a single z
substitution cannot change sign of the effect across words. So the two sides
disagree for some other reason.

Worth noting `pne` (rel 0.0123) is two orders of magnitude better than the other
three, which suggests the disagreement scales with word length or with the
number of `n`/`e` letters rather than being a flat factor.

## Why it matters

The probe is one of the witness-emitting consumers of
`computations/substrate/hecke_core_symbolic.py`, so it sits in the cone of the
`qou-cds1` migration and could not be measured through it — it aborts before
producing anything to compare. It is currently contributing nothing.

## Next honest step

Determine which side is wrong. The `corpus` side reads committed values; the
`closed` side evaluates the closed form in-file. Given `qou-5t68` (a committed
upstream 17–23% stale) the corpus side is not automatically the reference —
establish which is authoritative before "fixing" either to match the other.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8407, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
