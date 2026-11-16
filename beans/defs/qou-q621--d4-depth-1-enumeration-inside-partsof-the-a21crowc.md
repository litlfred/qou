---
# qou-q621
title: 'D4: depth-1 enumeration inside partsOf — the (a,2,1^c)+row+column family, membership + nodup'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:45:20Z
updated_at: 2026-10-04T15:18:33Z
parent: qou-wp3h
---

## Round 47 Implementation (PR #8153, `status: in-progress`)

- **Lean formalization (`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DepthOneHookClassification.lean`, wired into `QOU.lean`, `0` `sorry`)**:
  - `twoCornerShapes`, `depthOneShapes`, `depthOneShapes_mem_partsOf`, `depthOneShapes_nodup`, `depthOneShapes_length`, `mem_depthOneShapes_of_isDepthOneShape`, `sum_partsOf_eq_sum_depthOneShapes`, and `depthOne_mixedMoment_eq_depthOneShapes_sum` formalize the `(a, 2, 1^c) + row + column` family inside `partsOf k` and the Plancherel sum restriction.
- **PR**: https://github.com/litlfred/qou/pull/8153 (`95e28f261d9c08b118bd02c63a82c44dafe6174c`).
