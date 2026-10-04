---
# qou-m117
title: 'B (BACKUP): bypass convention via CM theory — Bring Jacobian ~ E^4, compute E period ratio from its Weierstrass model (CM point documented independent of B-N normalization); self-certifies vs the (1,5,5,5) gate'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T12:02:29Z
updated_at: 2026-10-04T15:11:56Z
parent: qou-3l2l
---


---
OUTCOME (2026-07-25, branch claude/alpha-em-cm-weierstrass-scale-2026-07-25, NOT closed — closing is human-only):
- CM leg REFUTED honestly (scope-(a)): j(tau0) = -121945/32 and j(5tau0) = -25/2 are non-integral rationals; CM j-invariants are algebraic integers => neither 50a factor has CM. The literal 'CM point' mechanism is closed.
- Q-model leg EXECUTED: exact Q-rational Weierstrass models from j alone (Fraction round-trip exact); AGM periods from the models == independent j-inversion to ~1e-58; tau0 recovered at 50 dps by the exact SL2(Z) word: tau0 = -1/2 + i/(4*Im tau_A_fund) = -0.5 + 0.18667646246...i (corpus 6-digit match).
- (1,5,5,5) GATE SELF-CERTIFIED: reduce(5*tau0) == tau_B_fund to 7.8e-62 (X0(5) + j-labelling confirmed); Im-ratio = 5 EXACT at 50 dps — Braden-Northover convention certified with zero period-matrix input.
- Tau-scale gate NARROWED to a discrete set (Neron per-curve normalization; residual freedom = isogeny-degree pullbacks through Jac(Bring) -> E_{5tau0}^3 x E_{tau0}).
- OBSERVATION (double-gated, OPEN, owner-level, no ID): route-C gate ratio 24.9997244717 is within 1.1e-5 of 25 = deg(5-isogeny)^2; ratio is normalization-carrying per route C itself.
- Deliverables: computations/alpha_em/alpha_em_b2_cm_weierstrass_scale_probe.py (+witness 7/7), docs/audits/2026-07-25-alpha-em-b2-cm-weierstrass-scale.md, ledger row in docs/coordination/alpha-em.md. Nothing wired; 1/(8pi) stays phase-4.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
