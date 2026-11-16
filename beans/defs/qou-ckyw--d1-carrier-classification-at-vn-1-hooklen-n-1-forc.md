---
# qou-ckyw
title: 'D1: carrier classification at v=n-1 — hookLen = n-1 forces two-corner (a,2,1^c) at (0,0), row (n) at (0,1), or column (1^n) at (1,0)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:45:17Z
updated_at: 2026-10-04T15:12:15Z
parent: qou-10v9
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 47 Implementation (PR #8153, `status: in-progress`)

- **Lean formalization (`folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DepthOneHookClassification.lean`, wired into `QOU.lean`, `0` `sorry`)**:
  - `eq_singleRow_of_carrier_zero_one`, `eq_singleCol_of_carrier_one_zero`, `eq_twoCorner_of_carrier_zero_zero`, and `carrier_classification_depth_one` prove that `hookLen l p + 1 = l.sum` on a sorted positive partition `l` forces two-corner `(a, 2, 1^c)` at `(0, 0)`, single row `[n]` at `(0, 1)`, or single column `1^n` at `(1, 0)`.
- **PR**: https://github.com/litlfred/qou/pull/8153 (`95e28f261d9c08b118bd02c63a82c44dafe6174c`).
