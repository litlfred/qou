---
# gnb1
title: 'Pre-existing: iterative-lp-dual-h6-deuteron producer un-runnable (IndentationError from broken 3-input anomaly-fixer block) + tr_M_cross_validation_within_1e-6 already failing on main (0.00018235)'
status: todo
type: task
created_at: 2026-06-29T17:35:28Z
updated_at: 2026-06-29T20:30:00Z
---

## Re-scoped 2026-06-29 — IndentationError FIXED; only the cross-validation remains

The un-runnable blocker is gone: `computations/iterative_lp_dual_h6_deuteron.py` parses cleanly
(the broken 3-input anomaly-fixer block that raised `IndentationError` was removed by the purge,
`ca475e2f`/`1e22e4e0`). Remaining open item (research-grade, NOT mechanical): the witness assertion
`tr_M_cross_validation_within_1e-6` fails — computed `0.00018235144298500055` vs the `1e-6` threshold
(~1.8e-4 cross-method tr_M disagreement on the deuteron H₆ frame), pre-existing and independent of the
purge. Audit: `docs/audits/2026-06-29-bean-hygiene-data-integrity-verified-resolved.md`.

