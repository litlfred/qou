---
# aciw
title: 'Q_β P-C15 survivor: 4_1 order-2 qZeilberger operator clears bar-parity gate as fibre kernel R(q,ξ) candidate; gated next = H4 Hoefsmit c4^even build (8we6)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-03T19:12:19Z
updated_at: 2026-10-10T08:30:00Z
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


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: BLOCKED.** The P-C15 structural result (the 4₁ Casoratian ratio is exactly bar-self-reciprocal) is convention-independent and reproduces. Everything it is compared against (W2, c2^even, c3^even) is convention C. The next step waits on 8we6 and on the D-frame ladder re-derivation (qou-cds1). Separately, the witness's a1_note contradicts its own a1 field and should be reconciled.

Evidence: `computations/qbeta/qbeta_pc15_casoratian_bar_parity_probe.py` re-run: exit 0, payload reproduces (twist = 1, exact sympy). The witness `qbeta-pc15-casoratian-bar-parity.witness.json` has a stale `scriptHash` (f80535476adf vs live db2068a05d67), and its `a1_note` ("a1 bar-ratio is x^7/q^5") contradicts its own `coeff_bar_ratios.a1 = x**9/q**3`. Gate bean `8we6` is still `todo`. The "consistent with W2 = +102.674" comparison uses c_k^even from the KC21 net-route ladder, which evaluates z_C (`qou-cds1` §"Live C sites": `qbeta_ck_sseries_exact_rational.py:20,248`).

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
