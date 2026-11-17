---
# mvy6
title: 'Wire prop:joint-galois-braid-figure-8-verified: Hoefsmit (2,2) bar-vs-braid commutation probe + fix vacuous Lean'
status: in-progress
pr: 8243
type: task
priority: low
tags:
    - compute-wiring
    - blocked-domain
    - reorg-2026-10-04
created_at: 2026-07-06T04:31:27Z
updated_at: 2026-10-04T15:26:03Z
parent: qou-6qbv
---

Blocked: claim is operator commutation of bar (q->q^-1, zeta6->zeta6^-1) with braid conjugation on the (2,2) figure-8 cell. Lean figure_8_joint_action is vacuous self-assuming (galois_4_1_central vs all f). Nearest compute metallic_q_symbolic_galois_proofs.py only does character-level bar(chi^lambda)=chi^lambda' (strictly weaker). Faithful probe requires building Hoefsmit (2,2) rep + bar involution + braid conjugation as operators. Domain work; no fabrication.

- **Round 54 update (in-progress):** De-vacuified in PR `litlfred/qou#8243` (HEAD `1495a97d0656036c5fc7c664284a44d77939041e`), verified with Lean 4.24.0 (`0` `sorry`, `0` vacuity hits) and 80-dps `mpmath` witness.
