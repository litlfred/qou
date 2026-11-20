---
# qou-8mmq
title: He4 two-row signed sum is suppressed 29,000x — exact identity at some q, or coincidence?
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T09:56:22Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

Measured 2026-08-07 by binding_row_length_stratification.py (0 free params, 60dps decimal over committed 50dps witnesses, no float64). The 4He two-row stratum carries 37.6% of the total l1 mass = 4.3196 MeV, but its SIGNED sum survives as only 0.000149 MeV -- a ~29,000x cancellation. The same |sum|/sum|.| ratio at the other three isotopes is ordinary: D 0.346, T 0.425, 3He 0.308. So 4He is FOUR ORDERS OF MAGNITUDE more cancelled than its neighbours, at the doubly-magic nucleus that is also the unique A=4 Wigner-SU(4) [1^4] singlet (SU4SupermultipletGate.lean). NOT EXACT: signed sum is -2.918e-4 against l1 8.4532, and inputs are 50-dps, so a genuine selection rule would leave a residual near 1e-50, not 1e-4. So this is strong suppression, NOT a proved selection rule, and must not be reported as one. Three untested readings: (a) an exact identity at some nearby q != q0, (b) an approximate symmetry of the 4He braid word, (c) an artifact of the averaged-crossing convention. NEXT TEST: evaluate the two-row signed sum across a range of q and look for a zero crossing -- an exact zero at q != q0 would make this a real identity rather than a coincidence.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8308, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
