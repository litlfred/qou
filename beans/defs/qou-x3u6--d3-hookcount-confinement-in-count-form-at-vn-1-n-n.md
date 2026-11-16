---
# qou-x3u6
title: 'D3: hookCount confinement in count form at v=n-1 (N_{n-1} per shape; 0 elsewhere)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:45:19Z
updated_at: 2026-10-04T15:18:33Z
parent: qou-wp3h
---

## Round 47 Implementation (PR #8153, `status: in-progress`)

- **Lean formalization (`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DepthOneHookClassification.lean`, wired into `QOU.lean`, `0` `sorry`)**:
  - `hookCount_depthOne_singleRow`, `hookCount_depthOne_singleCol`, `hookCount_depthOne_twoCorner`, and `hookCount_sub_one_eq_zero_of_not_isDepthOneShape` prove `N_{n-1} = 1` on each depth-1 carrier shape and `N_{n-1} = 0` elsewhere.
- **PR**: https://github.com/litlfred/qou/pull/8153 (`95e28f261d9c08b118bd02c63a82c44dafe6174c`).
