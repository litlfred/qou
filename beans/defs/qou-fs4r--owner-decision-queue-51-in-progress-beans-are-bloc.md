---
# qou-fs4r
title: 'Owner-decision queue: 51 in-progress beans are blocked on a ruling, uncounted until now'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T10:28:57Z
updated_at: 2026-10-04T15:13:27Z
parent: qou-5vkl
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


## Pass 3 (2026-09-05) — the 19 Class B collapse to 7 clusters; one already has its answer measured

**CLUSTER 1 retires FOUR asks with one ruling** — `qou-goc9`, `qou-im4m`, `t7qv`,
and Q4 of the 2026-09-05 analysis are the SAME question: chain (`A-1`) vs
all-pairs (`C(A,2)`) inter-nucleon topology.

**`t7qv` RESULT 4 already measured it** (AME read-only, no fit):

    model              2H/3He             3H/3He
    chain (adjacent)   0.50000 (+73.5%)   1.17024 (+6.5%)
    all pairs          0.40361 (+40.0%)   1.20327 (+9.5%)
    EXPERIMENT         0.28823            1.09896

**But `t7qv` RESULT 5 says NEITHER IS RIGHT**: solving each ratio for one
distance-2 weight gives `f = +2.030134` (A-scaling) against `f = -0.696951`
(mirror) — inconsistent, one negative, **a one-parameter falloff refuted
outright**. So all-pairs is the better of two topologies that are both wrong, and
quoting RESULT 4 without RESULT 5 turns a preference between refuted options into
a result.

What this needs is not "pick one" but a ruling on **whether the two builders may
keep disagreeing silently** — one reaches the paper (`demand-stability.ts` ->
all-pairs), the other the binding numbers (`binding_canonical` -> chain).

**CLUSTER 2 — `qou-1jw9` should LEAVE the veto queue.** It reports a **fourth
calibration**: `0.6870125 x 27.2961432 x 0.2387911 = 4.478000 eV`, H2's measured
bond energy, where the same witness's `H2_cross_check` records the uncalibrated
`18.75279 eV` and `4.478/18.753 = 0.23879` exactly. Under the standing NO FITTING
EXCEPT CAL-1/2/3 directive that is a discipline violation to adjudicate, not a
preference. Two riders: `E_hartree_eV` is +0.31% off CODATA (so not the Hartree),
and the witness contradicts its own content block on which of sigma/pi carries the
largest |V|.

Remaining clusters: 3 convention-D spend (`qou-cds1`, `qou-2tuv`); 4 Lean
class/axiom shape (`qou-t7mt`, `qou-w1g8`, `qou-octr` — the last PROVES 8 of 8
context-class sorries unclosable in current form, so not optional); 5 notation
(`qou-d7h1`, cheapest); 6 `qou-aemx` (its own later entry withdraws its earlier
"nothing argues for one"); 7 seven one-offs, of which **`gm4q` is decision-ready**
with a full options doc and recommendation already written.

**The queue is now drained to decisions.** Nothing further is triageable without
owner rulings.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
