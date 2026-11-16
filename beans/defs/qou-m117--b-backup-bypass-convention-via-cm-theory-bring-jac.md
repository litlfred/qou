---
# qou-m117
title: 'B (BACKUP): bypass convention via CM theory — Bring Jacobian ~ E^4, compute E period ratio from its Weierstrass model (CM point documented independent of B-N normalization); self-certifies vs the (1,5,5,5) gate'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T12:02:29Z
updated_at: 2026-11-16T17:58:00Z
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

## 2026-11-16 — On-`main` Verification & `Q-3L2L-1 = 1` Cross-Link (`litlfred/qou#8141`)

- **Verified on `main`:** `computations/alpha_em/alpha_em_b2_cm_weierstrass_scale_probe.py`, `computations/alpha_em/alpha-em-b2-cm-weierstrass-scale.witness.json` (7/7 assertions PASS at 50 dps, provenance-hardened in `138ab4aa9a`, `f66e72840e`, `a6d6952090`), and `docs/audits/2026-07-25-alpha-em-b2-cm-weierstrass-scale.md` are all landed on `main`.
- **Cross-linked with `qou-mxnu` & `qou-vbz4` (`litlfred/qou#8141`):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` (`non_vacuity_unaligned_not_proportional`) and `computations/alpha_em/std_block_hoefsmit_markov_schur_probe.py` (commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`) formalize why the raw isogeny-frame diagonal $(5, 5, 5, 1)$ certified here requires the $S_5$-equivariant intertwiner $W$ before comparing against the Hoefsmit diagonal $(576, 432, 384, 360)$.
- Kept at `status: in-progress` per owner governance.
