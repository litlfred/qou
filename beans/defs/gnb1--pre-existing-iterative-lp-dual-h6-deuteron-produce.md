---
# gnb1
title: 'Pre-existing: iterative-lp-dual-h6-deuteron producer un-runnable (IndentationError from broken 3-input anomaly-fixer block) + tr_M_cross_validation_within_1e-6 already failing on main (0.00018235)'
status: completed
type: task
created_at: 2026-06-29T17:35:28Z
updated_at: 2026-06-30T01:45:00Z
---

> **CLOSED 2026-06-30** — both halves resolved. (1) IndentationError: fixed on main by the 3-input-purge (`ca475e2f`/`1e22e4e0`); producer parses. (2) tr_M cross-validation: fixed in PR #3143 (`28ea745e`) — the reference was a hardcoded value from the now-deprecated `wenzl_n6_closed_form.witness.json`; the script's own Frobenius sum agrees with the canonical markov-peel tr_M to 4.8e-8. Reference now loads dynamically from `markov-peel-atomic-tr-m.witness.json`; assertion passes (allPassed=true).

## Re-scoped 2026-06-29 — IndentationError FIXED; only the cross-validation remains

The un-runnable blocker is gone: `computations/iterative_lp_dual_h6_deuteron.py` parses cleanly
(the broken 3-input anomaly-fixer block that raised `IndentationError` was removed by the purge,
`ca475e2f`/`1e22e4e0`). Remaining open item (research-grade, NOT mechanical): the witness assertion
`tr_M_cross_validation_within_1e-6` fails — computed `0.00018235144298500055` vs the `1e-6` threshold
(~1.8e-4 cross-method tr_M disagreement on the deuteron H₆ frame), pre-existing and independent of the
purge. Audit: `docs/audits/2026-06-29-bean-hygiene-data-integrity-verified-resolved.md`.

