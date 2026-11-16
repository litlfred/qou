---
# inkh
title: Fix muon=4_1 category error + drop-imaginary-part recurrence guards (owner-ruled)
status: in-progress
pr: 8188
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-30T20:10:17Z
updated_at: 2026-11-16T20:23:00Z
parent: qou-2002
---

## Progress Update (2026-11-16, PR #8188)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/CodataTruncationAndQ0AnchorRecentering.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/codata_truncation_and_q0_anchor_recentering_probe.py` and stamped witness `computations/probes/codata-truncation-and-q0-anchor-recentering.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 4f0055fd85b9bb82232f9b87ef757139e895bd6d`).
- [ ] Awaiting merge of PR [`litlfred/qou#8188`](https://github.com/litlfred/qou/pull/8188) (`548ed6acbe88e5772065a0fdb4d623f3472d3430`).

