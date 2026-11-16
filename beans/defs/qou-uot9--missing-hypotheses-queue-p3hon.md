---
# qou-uot9
title: Missing-hypotheses queue (P3.HON)
status: in-progress
type: feature
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:18:02Z
updated_at: 2026-11-16T20:28:25Z
parent: qou-6qbv
pr: 8189
---

Groups the machine-generated 'Missing-hypotheses queue' beans for P3.HON (owner decision 4, 2026-10-04: group, do not close). Each child is one queue item.

## Progress (PR #8189, 2026-11-16T20:28:25Z)

- [x] Advanced 4 children (`confinement_categorical`, `confinement_frobenius_reciprocity`, `four_term_pair_nucleon`, `parity_regime_selection`) in PR #8189 (`8a01e69797fd39964625747271958c7e8b76cc65`).
- [x] Verified with Lean v4.24.0 (`lean -DautoImplicit=false -s 65536`: 0 errors, 0 warnings, 0 `sorry`) and all 6 static vacuity audits (0 findings).
- [x] Verified with 80-dps `mpmath` probe (`computations/probes/round50_devacuify_6qbv_probe.py`) and 2-commit stamped witness (`computations/probes/round50-devacuify-6qbv.witness.json`, `scriptCommitSha: 357a63280dd6b77b067855dfd2ebaeb6340b2c28`, `scriptHash: 3ff73a87c2af`).
- [ ] Awaiting review and merge of PR https://github.com/litlfred/qou/pull/8189 (`status: in-progress` maintained per repo rule).
