---
# qou-kok7
title: Formalize bond-frustration sign-change window κ∈(3/2,3) (Lean, sorry-free)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-26T01:05:25Z
updated_at: 2026-10-04T15:19:17Z
parent: qou-10v9
---

## Progress Update (PR litlfred/qou#8244)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8244 (`457d28e500f11a4249f57fd33fcd18112faef23b`, scriptCommitSha `1086b0ae6f630df61ca513a195514ef5d6137b5c`)
- **Summary**: Added `bondFrust_linear_comb_invariant` and `bondFrust_window_endpoints_and_midpoint` in `QOU/MassTheory/AdditiveSignChangingTerm.lean`, verified by 80-dps mpmath probe `frust_cubic_tower_jhopf_whitehead_probe.py`.
