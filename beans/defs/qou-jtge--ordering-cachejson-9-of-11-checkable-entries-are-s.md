---
# qou-jtge
title: 'ordering-cache.json: 9 of 11 checkable entries are stale, and a plain re-run TRUNCATES it 270 to 11'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T02:59:18Z
updated_at: 2026-10-04T15:21:53Z
parent: qou-5vkl
---


## Measured 2026-08-16 — two separate problems, and the second is a trap

Found via the `resume-cache-unvalidated` axis and the delete-and-re-run test
that resolved `qou-7bv5`.

**1. It is stale.** `ordering_cache.py` resumes from `ordering-cache.json` with
no guard of any kind — no q₀, no source hash. Of the 11 entries a fresh run
recomputes, **9 differ** from the committed values.

**2. A plain re-run TRUNCATES it, 270 → 11.** This is the part to be careful
with. The committed cache holds **270** keys; `ordering_cache.py`'s warm path
covers **11 nuclei**, so deleting and re-running produces an 11-key file and
silently drops 259 entries. I restored the committed file rather than commit
that, and verified it byte-identical to HEAD.

So the obvious repair — delete and re-run, which was correct for the deuteron χ
cache — is **wrong here** and would destroy data.

## How to attack

* Do **not** regenerate by deletion. Establish first which of the 270 keys are
  reachable from a producer at all; 259 of them are not produced by the default
  warm path and may be orphaned by an earlier, wider sweep.
* Add a guard so stale entries are discarded per-entry rather than wholesale —
  the shape `chi_at_q0_via_hoefsmit_mpfr` uses (compare a stored provenance key,
  discard on mismatch) rather than the all-or-nothing delete.
* Then regenerate the 11 warm entries and re-check the other 259 against
  whatever produced them.

**Consumers first.** Before any of that, grep what reads `ordering-cache.json`
and whether the 9 changed entries feed anything committed. The staleness is
established; the blast radius is not.
