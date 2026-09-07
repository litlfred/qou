---
# qou-4u10
title: canonical q_int(n) is q0-PINNED (Q/Q_INV/HA are module globals) — add a q-parametric form so the 187 q-parametric local copies have something to import
status: completed
type: task
priority: normal
created_at: 2026-09-07T14:02:19Z
updated_at: 2026-09-07T16:16:00Z
---

IMPLEMENTED 2026-09-07, commit 872db2009. qou_substrate/constants.py gains q_int_at(n, q=None, dps) and q_int_classical_at(n, q=None, dps) inside the mpmath tier, with f64 fallbacks in the except-ImportError branch. Both take q as an ARGUMENT rather than reading the module global, which is the whole point: the 187 q-parametric local copies now have something to import.

PURELY ADDITIVE, verified rather than asserted: all 61 pre-existing public names still resolve; Q, HBAR_Q and q_int(9) are byte-unchanged; y_lambda_at(3, q0) sum still 0.752702113252. q=None defaults to q_at(dps+10), so the pinned behaviour is reachable without a caller change.

First consumer landed the same day: term7_chi5_basis.py (qou-263a) now delegates instead of carrying its own bracket, taking the local-definition count 366 -> 365.

Mechanical API addition, no conjecture in scope, so AGENTS.md 13a does not gate closing it.
