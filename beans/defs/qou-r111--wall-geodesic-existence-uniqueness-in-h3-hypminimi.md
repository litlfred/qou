---
# qou-r111
title: 'WALL: geodesic existence + uniqueness in H3 (HypMinimizerUnique conjecture)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T11:11:36Z
updated_at: 2026-10-04T15:25:32Z
parent: qou-n4nr
---

Origin: PR #5211. The single genuinely-open Mathlib-scale wall of the T2 hyperbolic development: geodesic existence + uniqueness in H³. Represented HONESTLY as the content-bearing conjecture class QOU.Archimedean.HypMinimizerUnique (QOU/Archimedean/HyperbolicGeodesic.lean) with NO instance — its field states pointwise uniqueness of constant-speed minimizers. The totally-geodesic classification (verticalPlaneFix/hemisphereFix_isTotallyGeodesic) is PROVED conditional on it, sorry-free (#print axioms: no sorryAx, only the class hypothesis). Closing it needs a hyperbolic-geometry library Mathlib does not have (no metric/exp/geodesics). Existence of minimizers is part of the same wall.

## Progress Update (PR litlfred/qou#8238)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8238 (`dcfad8a84dddbefde9a4efb59eba72ba663b1d84`, scriptCommitSha `2b4b5612016793df004e2f2990d7681285f78653`)
- **Summary**: Added `isTotallyGeodesic_inter` and `verticalPlane_inter_hemisphere_isTotallyGeodesic` in `QOU/Archimedean/HyperbolicGeodesic.lean`, verified by 80-dps mpmath probe `interface_kappa_geodesic_em_connsum_probe.py` (`scriptHash: 5c337ec3fbc3`).
