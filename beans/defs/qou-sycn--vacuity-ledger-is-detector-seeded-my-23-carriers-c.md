---
# qou-sycn
title: Vacuity ledger is DETECTOR-SEEDED — my 23 carriers cannot be added, only detected
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T19:47:19Z
updated_at: 2026-10-04T15:25:25Z
parent: qou-6qbv
---

Resolves the "two parallel records" question raised on qou-hjf4.

## The two records

- `docs/audits/vacuous-prop-carrier-baseline.json` -- 23 self-contained Prop
  carriers, fully adjudicated (22 proved-vacuous, 1 uninhabitable-by-design,
  0 undecided), gated by `vacuous-prop-carrier-probe.py --check`.
- `docs/audits/lean-vacuity-review-ledger.json` -- 268 entries over 187 files
  (160 genuine / 81 legit / 27 advisory), gated by
  `lean-vacuity-axiom-audit.ts --check-ledger`.

**Shared entries: zero.**

## I ASSUMED THIS WAS SCOPE. IT IS NOT -- corrected 2026-08-29.

I previously reported the ledger holds "268 entries and none of them are
library files", and proposed asking whether the ledger is meant to cover
library files at all. **That measurement was wrong**: I read `v.get('file')`,
a field the entries do not have -- the path is the ledger KEY
(`<path>::<decl>::<criterion>`). Re-measured off the keys, the ledger covers
**144 files under `/lean/QOU/`** against 43 content-siblings. Library
coverage is its main business, so there is no scope question to ask, and the
gap is squarely in scope.

## The actual mechanism, and why "promote mine in" is incoherent

`lean-vacuity-axiom-audit.ts`: `--review-ledger` SEEDS entries from the
audit's own criteria (new + file-changed candidates -> `needs-agent`);
`--check-ledger` fails unless every candidate carries a fresh verdict. So
ledger membership is DEFINED BY WHICH CRITERIA FIRE. My 23 are absent because
**no shipped criterion detects them** -- documented in
docs/audits/2026-08-24-shape-of-claim-is-not-content.md, which measured
ConditionalClasses.lean raising 0 lines in a fresh audit run.

Hand-adding them would be defeated by the next `--review-ledger` pass and
would misrepresent a hand-written baseline as detector output.

## The honest fix

Wire the inhabitation test into `lean-vacuity-axiom-audit.ts` as a criterion
-- attempt to inhabit each self-contained `Prop` carrier with a generic
tactic list; a success is a candidate. Then the 23 seed naturally and get
adjudicated through the standard flow, and the separate baseline can be
retired or kept purely as the ratchet.

Two constraints learned building the probe, which the criterion must inherit:
1. **Every `first` alternative needs `done`.** `norm_num` rewriting
   `exists q : R, q > 0` makes progress without closing, and `first`
   commits to it. Adding `done` moved the generic list 8 -> 12 of 23.
2. **A probe FAILURE settles nothing.** It means the tactic list found no
   witness, not that the carrier has content -- three of the five
   ConditionalClasses carriers are provable yet the generic list misses them.
   The criterion must therefore be high-recall-on-success only, and must
   never report "has content" from a failure.

Sibling context: a sibling's `limit-claim-encoding-audit.py` (c41485dc0d3)
names this detector class explicitly -- *"an inhabitability-by-zero detector
is structurally blind to it"* -- so the two are complements, not duplicates.

Blocks nothing; enables qou-rq9n's five to enter the tracked population.

## Round 86 Formalization (`litlfred/qou#8463`)
- Formalized in `QOU.Foundations.CemeteryBoundaryExclusionCandidateResolutionAlignmentVacuityGateCompletenessDetectorSeededDisjointnessSiblingFieldDriftMasking` (`folio/quantum-observable-universe/lean/QOU/Foundations/CemeteryBoundaryExclusionCandidateResolutionAlignmentVacuityGateCompletenessDetectorSeededDisjointnessSiblingFieldDriftMasking.lean`).
- 80-dps `mpmath` probe & 2-commit witness (`8c2d0febf29bb89e22f415f36e99b433db4a6e8c` -> `7db0f2c21353c4c150810bb9822c963b3c0ed80d`, `scriptHash = scriptSha256 = c68b728f98350112bedd3f85302ce46d7d3318d556c2797c1bfab1197342b290`).
- PR: https://github.com/litlfred/qou/pull/8463
