---
# qou-fs4r
title: 'Owner-decision queue: 51 in-progress beans are blocked on a ruling, uncounted until now'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T10:28:57Z
updated_at: 2026-09-05T07:22:48Z
---

## Owner ruled 2026-09-05: triage + propose a default, owner vetoes (Q2 option 3)

Ledger: [`docs/coordination/2026-09-05-owner-gated-bean-triage.md`](../docs/coordination/2026-09-05-owner-gated-bean-triage.md).

**The count was wrong three times, and the correction is the useful part.** I
quoted 51, then 67, then 81 — three keyword scans, three patterns, none
authoritative. Split by whether the owner-phrase is a LIVE ASK or a CITATION of a
past ruling:

    PENDING (live ask)          33
    HISTORICAL ONLY             18   <- "by owner decision", "Owner ruling 2026-08-15"
    (pending + citing history)   3   <- counted in PENDING

So **18 of the apparent backlog was the owner being quoted back to himself.** The
real queue is 33.

**One adjustment to the chosen option, applied deliberately.** Where a default
would land a PHYSICS OR CONVENTION claim, no default is proposed — those are
marked NO DEFAULT and get options instead. Silence-as-assent is right for
mechanics and is exactly the laundering route for a physics ruling.

Pass 1: 6 Class A (default proposed), 17 Class B (no default), 2 Class C (close),
10 unclassified. Two Class B items are already in front of the owner by another
route: `qou-goc9` is the SAME question as today's Q4 (chain A-1 vs complete graph
C(A,2)), and `qou-cds1` is authorisation-to-spend rather than a judgement.

`qou-zzwm` flagged out of band: it reports the C->D excision left PUBLISHED
accuracy figures behind. If true that is a correctness defect in reader-facing
numbers and does not belong in a veto queue at all. First item of pass 2.
