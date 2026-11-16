---
# qou-amf8
title: 'D5: depth-1 shape data — contentSq/omega3 for two-corner shapes + their sytDim'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:45:21Z
updated_at: 2026-10-04T15:18:34Z
parent: qou-wp3h
---

## Round 47 Implementation (PR #8153, `status: in-progress`)

- **Lean formalization (`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DepthOneHookClassification.lean`, wired into `QOU.lean`, `0` `sorry`)**:
  - `contentSq_twoCorner`, `six_mul_omega3_twoCorner`, `hookProd_twoCorner`, `sytDim_twoCorner`, `sytDim_singleRow`, and `sytDim_singleCol` prove the exact `contentSq`, `6·ω₃`, `hookProd`, and `sytDim` formulas for the depth-1 carrier shapes.
- **PR**: https://github.com/litlfred/qou/pull/8153 (`95e28f261d9c08b118bd02c63a82c44dafe6174c`).
