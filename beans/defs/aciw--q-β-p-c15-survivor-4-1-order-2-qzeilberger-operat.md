---
# aciw
title: 'Q_β P-C15 survivor: 4_1 order-2 qZeilberger operator clears bar-parity gate as fibre kernel R(q,ξ) candidate; gated next = H4 Hoefsmit c4^even build (8we6)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-03T19:12:19Z
updated_at: 2026-10-04T15:22:55Z
parent: qou-avtq
---


Probe P-C15 (2026-07-03, main @ 746a5091): the 4_1 order-2 colored-Jones
qZeilberger operator (aj_figure_eight_certificate.py, exact N=1..12) is a
candidate for the Q_β fibre kernel R(q,ξ). Its Casoratian ratio
W_{N+1}/W_N = a0/a2 = (q^3 x^3 − q^3 x^2 − x + 1)/(q^3 x^3 − q^2 x − q x^2 + 1)
is EXACTLY bar-self-reciprocal (twist=1) under q→1/q, x→1/x, and its q→1
classical shadow = 1 > 0 (consistent with measured even-channel W2 = +102.674).
Bar-parity gate PASSED → NOT excluded. First survivor vs all refuted C1–C14.
Scope-(a) positive: NOT a closure, NOT a c_k value, nothing wired.

GATED NEXT STEP (this bean): the H4 Hoefsmit c4^even build (bean 8we6) supplies a
genuine c4 rung, which plugs into the already-machine-checked sibling gate
sigma3_lift_kill_test (StageCSigma3LiftObligation.lean) to evaluate the anchor
Casoratian W3/W2. P-C15 de-risks that build. Do NOT run an anchor sweep before c4.

Refs:
- computations/qbeta/qbeta_pc15_casoratian_bar_parity_probe.py (+ .witness.json)
- docs/audits/2026-07-03-qbeta-pc15-casoratian-bar-parity.md
- docs/coordination/1ppq-qbeta.md (P-C15 section)
- Part of the 2026-07-03 path-to-1ppQ reanalysis (artifact): Identity I ≠ keystone
  unlock; Σ(2,3,5) WRT geometric leg refuted 2026-07-02; Q_β is the one near-term
  needle-mover above the CAL-2 floor.
