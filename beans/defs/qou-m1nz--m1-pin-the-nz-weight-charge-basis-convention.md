---
# qou-m1nz
title: Route C M1 BLOCKER — pin the Neumann-Zagier weight / charge-basis convention so the certified 3d-index reproduces the GGM eq-(61) Stokes tower
status: todo
type: task
priority: high
tags:
    - g3-aomega
    - route-c
    - reorg-2026-10-04
created_at: 2026-08-11T10:30:00Z
updated_at: 2026-11-20T16:06:50Z
parent: b9cj
---

M1 attempted 2026-08-11 (probe: computations/probes/qbeta_m1_index_stokes_dictionary.py, audit-only, 2/3 assertions — the FAIL is the honest negative).

WHAT WORKS: the corpus producer figure_eight_3d_index.py is sound — it reproduces the GHHR (arXiv:1604.02688) Ex 4.1 anchor EXACTLY: I_T(0) = [1,-2,-3,2,8,18,18,14,-12,-52,-106].

WHAT FAILS: no tried summation reproduces the printed GGM eq-(61) descendant tower [1,-8,-9,18,46,90,62]:
  sum_e I(0,e), e in [-E,E], all E<=8  -> [1,-2,-3,4,12,28,22]  (stable, wrong)
  sum_k I_D(k,k)^2                     -> divergent garbage (needs the NZ weight)
  sum_k I_D(k,-k)I_D(-k,k)             -> [1,-4,-5,4,14,32,30]  (stable, wrong)
  sum_k I_D(k,0)I_D(0,k)               -> non-convergent

WHY THIS IS A CONVENTION GAP, NOT A REFUTATION: GGM Conjecture 4 / eq (21) is a THEOREM for 4_1, and the corpus's own g3 probe verified the dictionary NUMERICALLY at the substrate point ([V4]: S+_(s1s1)(q_sub) = sum_e I(0,e)(q_sub) = 0.42764420131745803633). So the identity holds; what is unpinned on the QOU side is the ROTATED-index normalization: the q^{nu.k/2} Neumann-Zagier weight and which (mu,lam) charges are summed. DELIBERATELY NOT TUNED to fit (anti-numerology).

NEXT ACTION (concrete): pin the NZ weight nu from the source — GHHR arXiv:1604.02688 / DGG arXiv:1112.5179 for the m004 2-tetrahedron gluing (or snappy.Manifold('4_1').neumann_zagier_data / the SnapPy 3d-index), then re-run the probe. Route C M2 (BPS cohomology whose dims are these integers) is BLOCKED on this step.

NOTE the tension to resolve: the substrate-point agreement vs the coefficient-wise disagreement means the two computations are using different conventions for "sum_e I(0,e)" — worth diffing the g3 probe's index construction against figure_eight_3d_index.py directly; that diff alone may pin it.


## Round 83 Execution Note (2026-11-17T10:23:09Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8301`](https://github.com/litlfred/qou/pull/8301) (`feat/qou-b9cj-1gkf-gz37-ips1-ized-m1nz`, HEAD `8def28bdd6676a091a84204c0314f39da9ee6d5c`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/GaroufalidisZagierS3BlockAndFiveTwoDiscBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/garoufalidis_zagier_s3_block_and_five_two_disc_brick_probe.py` & `computations/probes/garoufalidis-zagier-s3-block-and-five-two-disc-brick.witness.json` (`scriptCommitSha = d726ce17152d0bdd416fbd50d86ba08930c726e7`, `scriptHash = 1b13751c9d60`, `outputHash = 36c8353af8986ccd33f16fae6cef94ba4dab83e96f5a0e688d772b07b9d32e72`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8301, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
