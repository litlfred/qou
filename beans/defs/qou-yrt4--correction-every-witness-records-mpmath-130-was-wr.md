---
# qou-yrt4
title: 'CORRECTION: ''every witness records mpmath 1.3.0'' was wrong -- 703 already record 1.4.1, and a migration is in flight'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T20:20:48Z
updated_at: 2026-10-04T15:18:12Z
parent: qou-5vkl
---

WRITTEN INTO A COMMIT MESSAGE, so correcting it here where a reviewer can find it.

6b6f823381 says: 'Every witness in the corpus records 1.3.0, so a regeneration
under 1.4.1 would have written a different environment block into four audits
for no reason connected to the audit.'

The premise is FALSE. Measured on the merged tree, 3066 witnesses:

    mpmath 1.3.0        1184
    (no env block)      1176
    mpmath 1.4.1         703
    mpmath 0.0.0           2

So 1.3.0 is the plurality among witnesses that record an environment at all,
but 703 already carry 1.4.1 -- not zero, and not a rounding error.

There is also a DELIBERATE, TRACKED migration toward 1.4.1 that I did not know
about when I wrote that: computations/audits/regen-mpmath141-ledger.json,
schema regen-mpmath141-ledger/v1, "target": "1.4.1", 9 producers so far
(6 ok, 2 nonzero, 1 timeout), landed as 'regen batch 1' (9523fac27f) and
'regen batch 2 ... 1 HELD BACK at a 3.3x unexplained move' (a1be1d0c29). And
1.4.1 is known to break producers: 17bf432f9e fixes an mpf reaching an f-string
:.4f, and 046614da3d records that the crash is mpmath-version-dependent.

THE ACTION WAS STILL RIGHT, FOR A DIFFERENT REASON THAN I GAVE. Restoring
1.3.0 and re-measuring was correct because the change was UNTRACKED and landed
MID-MEASUREMENT -- an accidental Requirement already satisfied: py-spy in /usr/local/lib/python3.11/dist-packages (0.4.2) side effect that silently
straddled a baseline and its conversion. It was NOT correct because 1.4.1 is
wrong; the corpus is moving there on purpose.

WHAT THIS BRANCH SHOULD NOT DO: carry half of that migration inside a
convention-C branch. The sibling is doing it producer-by-producer with a ledger
and holding back moves it cannot explain. Silently regenerating witnesses at
1.4.1 here would put two causes in one measured diff, which is the specific
error this branch's method exists to prevent. Staying at 1.3.0 for the
duration is the right call -- but as a scoping decision, not because 703
witnesses are wrong.

Found while checking whether my v-hat conversion broke a consumer control arm
(PR #5669's detector, merged). It did not: the only Python file naming
v-hat-z-transfer-phase5d-4.witness.json is its own producer.

- **Round 96 PR (`litlfred/qou#8510`)**: Formalized `EnvironmentVersionCensusLedger`, `canonicalEnvironmentVersionCensusLedger`, `environment_census_polarization`, and `environment_census_diff_sq` in `QOU.Foundations.AnchorRefillArrivalPartitionUnifiedIterativeTableOrphanAuditEnvironmentVersionCensusNoncommutativeTacticSiteAuditScriptSweeperRootDiscrepancy` with 80-dps witness (`HEAD = 9861bd624187df98849a08e324f09311a00ff969`).
