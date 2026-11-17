---
# qou-5isd
title: Cite 9504020v1.pdf at qou:QOU.QBeta.CyclicDilogPentagon
status: in-progress
pr: 8289
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:34Z
updated_at: 2026-10-04T15:17:22Z
parent: qou-ysb7
---

Once registered, CyclicDilogPentagon.lean should cite the cyclic-dilogarithm R-matrix paper directly rather than only the 1994 quantum-dilogarithm paper, since the cyclic construction is what that file formalises.

**From the source**
- Abstract / main theorem — The link invariant obtained from the cyclic quantum dilogarithm by the given R-matrix construction coincides with the invariant of triangulated links in S^3; the R-matrix is the cyclic analogue of the U_q(sl(2)) universal R-matrix.
  Use here: Primary source for the cyclic-dilogarithm R-matrix that QOU/QBeta/CyclicDilogPentagon.lean works with, currently referenced only through faddeev_kashaev1994 and kashaev1997.

Source: `library/arxiv-q-alg-9504020v1/9504020v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

<!-- re-issued 2026-08-23: this bean and
     `qou-x4qm--gap-three-generation-structure-...` both claimed id `qou-x4qm`.
     Unrelated beans that collided on a random id; the older three-generation
     bean keeps `qou-x4qm`, this newer citation task takes a fresh id.
     Flagged in bean `qou-xqno`. -->

## Round 57 Implementation Progress (PR #8289)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8289 (head `b1d29c3ac9e8ff1013e87a6f368591fb977a1ff3`, Commit 1 `85cf34f4dd33fa831b7480e3f2c9e1ff2e2f5c6d`)
- **Lean 4 Module & Theorems:** `QOU/QBeta/CyclicDilogPentagonAndDGLZStateIntegralLattice.lean` (`kashaev_cyclic_dilog_rmatrix_pentagon_charge_conservation` citing `9504020v1.pdf`, `[faddeev_kashaev1994]`, `[kashaev1997]`)
- **80-dps Witness:** `computations/probes/round57-fivetwo-discriminant-habiro-dilog-dglz-pentagon.witness.json` (`scriptHash: 3ee733fedb99`, `allPassed: true`, `0` raw `float64`)
