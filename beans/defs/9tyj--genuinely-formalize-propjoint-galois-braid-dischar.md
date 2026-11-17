---
# 9tyj
title: Genuinely formalize prop:joint-galois-braid-discharged (replace self-assuming galois_central Lean shell)
status: in-progress
pr: 8243
type: task
priority: low
tags:
    - compute-wiring
    - blocked-domain
    - reorg-2026-10-04
created_at: 2026-07-06T04:31:27Z
updated_at: 2026-10-04T15:25:57Z
parent: qou-6qbv
---

Blocked: Lean joint_action_discharged is sorry-free but SELF-ASSUMING (galois_central asserts commutation vs ALL f; theorem specializes to braid) — a degenerate §3b-cond projection failing proof-statement-integrity. Genuine fix needs disjoint tensor-factor decomposition Cell=A(x)B (galois on A, braid on B) + TensorProduct bifunctoriality; the disjointness of H_q^(n,K) is an unwritten domain gap. Infinite family => no finite probe.

- **Round 54 update (in-progress):** De-vacuified in PR `litlfred/qou#8243` (HEAD `1495a97d0656036c5fc7c664284a44d77939041e`), verified with Lean 4.24.0 (`0` `sorry`, `0` vacuity hits) and 80-dps `mpmath` witness.
