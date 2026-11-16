---
# qou-wc9f
title: 'GAP: bond_edge_set_selection_probe computes its VERDICTS from rounded float64 — and compares a rounded value against an unrounded one. closable_within_5pct tests 0.95 <= round(miss,3) <= 1.05; best_integer_edge_set picks on abs(log(miss)) < abs(log(best[''miss_x''])) where miss is full-precision but best[''miss_x''] is round(...,3), so the comparison is inconsistent independent of float64. joint_closure_possible derives from closable. Line 66 also does the AGENTS.md-banned q0,h,me = float(q0),float(h),float(me) downcast. Fixing may FLIP verdicts — measure and report flips, do not bundle into a mechanical float64 drain.'
status: in-progress
pr: 8186
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T17:17:11Z
updated_at: 2026-10-04T15:19:46Z
parent: qou-9nnz
---



## Round 51 Progress
- [x] PR https://github.com/litlfred/qou/pull/8186 (`fb4f6926d3f96fd99209ef3cb58128ff0ce2701b`): replaced `_dp` with `_precision.fmt`, evaluated `best` and `closable` directly on unrounded `mpmath.mpf` `miss` values, and regenerated `bond-edge-set-selection.witness.json` (0 raw float64).
