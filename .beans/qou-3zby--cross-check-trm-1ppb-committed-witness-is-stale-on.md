---
# qou-3zby
title: cross-check-trM-1ppb committed witness is stale on main — C/D straddle across its four methods
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:23:15Z
updated_at: 2026-08-16T13:23:51Z
---

Found during /prepare-merge on PR #5199 (provenance triage). NOT that branch's regression -- cross_check_trM_1ppb.py reads none of its files (inputs are atomic-tr-m-mpfr-50dps, canonical-tr-m-via-chi-cache, habiro-coefficients-extended, markov-peel-atomic-tr-m-muon, q-pinning-50-digit). Confirmed inherited: a pristine origin/main worktree (cbb49a1a35) exits 1 on the same gate.

The regenerated numbers show a C/D straddle ACROSS the four methods -- the chi path moved to D while peel and habiro stayed on C:

  metric            committed        fresh
  hoef_vs_chi         0.481        1.45e-07   <- improved 7 orders
  hoef_vs_peel      0.000182         0.325    <- degraded
  hoef_vs_habiro     6.02e-49        0.325    <- degraded
  rel_delta_max        0.4813        0.4810

6/6 atoms DIVERGE, 0 certified at 1 ppQ. hoef_vs_chi collapsing to 1e-7 is the tell that Hoefsmit and chi are now on the same convention; peel and habiro are not.

The regenerated witness was deliberately NOT committed on #5199: draining another arc's witnesses is that arc's work, and burying a substantive physics-gate change in an unrelated provenance PR hides the signal. This belongs to the convention-D cascade.

L1 impact: this IS the L1 compute-precision gate (AGENTS.md Precision goals). While it is red, 'L1 compute met' is not supportable by this cross-check.
