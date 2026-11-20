---
# qou-9lew
title: Derive the site-vs-bond factor 2 in the Borromean volume term (measured 1.966)
status: todo
pr: 8219
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T08:56:24Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

First forward result on the extended-Bloch route, hyperbolicity granted by owner. Prediction stated BEFORE evaluating: B_volume(A) = E0 * Vol_per_nucleon * A with E0 = m_e/(q0(q0-1)) = 4.185981 MeV and the canonical no-choice reading Vol_per_nucleon = Vol(B_3) = 7.327724753 (the framework's nucleon IS the Borromean link). Result: 30.674 MeV/nucleon vs a_V ~ 15.6 => MISSES by 1.966x. The Vol(B_3)/2 = V_oct reading gives 15.337 (0.983x) but selecting it post hoc is convention-shopping -- NOT predicted in advance, flagged as rationalisation. WHY IT MATTERS ANYWAY: the discrepancy is a DISCRETE structural factor ~2, not a continuous knob, so it is a well-posed derivable question. Two independent readings each predict EXACTLY 2: (a) the Borromean complement decomposes into exactly two regular ideal octahedra, Vol(B_3) = 2*V_oct, so half-a-Borromean is a geometric cell not an arbitrary halving; (b) summing a per-BOND volume over SITES double-counts every shared interface. Either predicts exactly 2 vs measured 1.966 => a real 1.7% residual, which is the honest deliverable. TASK: derive the factor from atomic-braid combinatorics; it must come out EXACTLY 2 (or exactly (A-1)/A-like), never 1.966. THEN evaluate against B_D/B_T/B_3He/B_4He, NOT against a_V (a_V is itself a fitted SEMF coefficient with ~2% spread across parametrisations, so 1.7% agreement is weak evidence either way).


## Progress Update (PR #8219)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`ThermodynamicTemperatureAndRepinBound.lean`, `SiteVsBondVolumeFactorTwo.lean`, `TwoDimensionalInterfaceCollapseAndOrdering.lean`, `WritheSignOppositionEndpointSplit.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` probe (`computations/probes/kt_repin_octahedron_interface_writhe_probe.py`) and stamped witness (`computations/probes/kt-repin-octahedron-interface-writhe-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8219 (`ready: 0004396c02a14ba756cc43c66855073b0a08f82d`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8219, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
