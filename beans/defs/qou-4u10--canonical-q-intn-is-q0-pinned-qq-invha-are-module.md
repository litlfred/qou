---
# qou-4u10
title: canonical q_int(n) is q0-PINNED (Q/Q_INV/HA are module globals) — add a q-parametric form so the 187 q-parametric local copies have something to import
status: completed
type: task
priority: normal
created_at: 2026-09-07T14:02:19Z
updated_at: 2026-09-07T17:42:02Z
---

IMPLEMENTED 2026-09-07, commit 872db2009. qou_substrate/constants.py gains q_int_at(n, q=None, dps) and q_int_classical_at(n, q=None, dps) inside the mpmath tier, with f64 fallbacks in the except-ImportError branch. Both take q as an ARGUMENT rather than reading the module global, which is the whole point: the 187 q-parametric local copies now have something to import.

PURELY ADDITIVE, verified rather than asserted: all 61 pre-existing public names still resolve; Q, HBAR_Q and q_int(9) are byte-unchanged; y_lambda_at(3, q0) sum still 0.752702113252. q=None defaults to q_at(dps+10), so the pinned behaviour is reachable without a caller change.

First consumer landed the same day: term7_chi5_basis.py (qou-263a) now delegates instead of carrying its own bracket, taking the local-definition count 366 -> 365.

Mechanical API addition, no conjecture in scope, so AGENTS.md 13a does not gate closing it.

CORRECTION 2026-09-07: I wrote '61 pre-existing public names' here, in the PR body and in a PR comment. Measured against the merge-base by importing both versions and diffing dir(): base 62, new 64, REMOVED empty, ADDED exactly {q_int_at, q_int_classical_at}. The additive claim holds; the number was wrong.

FOLLOW-UP LANDED (af6c21e53), owner directive: the f64 fallbacks these two carried in the no-mpmath branch are EXCISED. They now raise, matching the four functions already in that branch (vol_4_1_at, q_at, q_str, q_muon_frozen_at), all of which raise. My versions were the only two in the branch that computed — a NO-FLOAT64 violation and a break with the file's own convention. Also fixes a placement defect: the f64 versions sat after the module-level 'Experimental observable anchors' comment block, reading as module-level while being inside the except.

term7_chi5_basis re-run after the excision: witness BYTE-IDENTICAL, so no number moved.
