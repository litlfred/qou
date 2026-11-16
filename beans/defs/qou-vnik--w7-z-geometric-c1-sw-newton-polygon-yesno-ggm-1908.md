---
# qou-vnik
title: 'W7: z-geometric C1<->SW Newton-polygon yes/no (GGM 1908.07065)'
status: in-progress
pr: 8201
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T15:53:20Z
updated_at: 2026-10-04T15:25:31Z
parent: qou-frzo
---

## Progress Note (2026-11-16, PR #8201)
- Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/C1ConnectionThetaAndKSWallCrossing.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 7 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/c1_connection_theta_and_ks_wall_crossing_probe.py` and witness `computations/probes/c1-connection-theta-and-ks-wall-crossing.witness.json` (`scriptCommitSha: 6a7d9973a198adec786d4227a4bfc12f4785934e`, `scriptHash: c4713523ced0`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8201 (`671820c7c233d2a9562f6f72f68cfb5b01b9b764`).
