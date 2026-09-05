---
# qou-fs4r
title: 'Owner-decision queue: 51 in-progress beans are blocked on a ruling, uncounted until now'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T10:28:57Z
updated_at: 2026-09-05T07:31:43Z
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


## Pass 2 (2026-09-05) — four MORE false positives, same root cause as the 18

Of the 33 "pending", **4 were already answered inside their own bean**:

- `qou-zzwm` — its ask was "either the dashboard records the frame, or the ladder
  is re-derived under D". **The first branch was taken.** Verified live:
  `per-observable-100x-status.witness.json` carries `convention_frame_qbeta`,
  `reproducible_under_canonical_convention`, and text naming the C frame and the
  2026-08-15 ruling. Live remainder is `qou-cds1`.
- `qou-zdz5` — its own text: "a name is not revising a finding, so no ruling was
  needed. HAD any site carried a wrong value ... that WOULD HAVE BEEN the owner's
  call." Conditional, condition not met.
- `qou-52i4` — "the 4459-vs-7268 obstacle predicted above is NOT ACTUALLY
  ENFORCED". Moot.
- `qou-e9pp` — answered by the owner ruling of 2026-08-30 (proton unless E1/E2).

**So 22 of the original 81 were stale sentences, not open questions** — 18 citing
a past ruling, 4 answered inside their own bean. ~27 % noise, and each would have
cost a round-trip to a physically-disabled author.

**The cheap fix is a convention, not a tool: when a bean answers its own
owner-ask, EDIT THE ASKING SENTENCE rather than appending the answer below it.**
A grep sees the first sentence.

### Where the 33 landed

    A  default proposed   10   veto to change; silence applies
    B  NO DEFAULT         19   physics / convention / claim change
    C  not pending         6   close or reclassify

Class A veto list: 9h6x qou-agvb qou-jvav qou-pwut qou-7yj0 qou-52i4 qou-58zw
qou-9xla qou-qflp qou-r765

Pass 3: options for the 19 Class B.
