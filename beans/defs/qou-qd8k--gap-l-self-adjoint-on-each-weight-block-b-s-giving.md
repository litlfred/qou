---
# qou-qd8k
title: 'GAP: L self-adjoint on each weight block B_s, giving the alpha=s little q-Jacobi basis'
status: todo
type: task
created_at: 2026-11-27T22:02:56Z
updated_at: 2026-11-27T22:02:56Z
blocking:
    - qou-pa7n
---

From PR #9746. Block pairings proved nondegenerate (q_ns_block_pairing_nondegenerate.lean); #9714 gives h(X+a.X-b) = -q^{2(s-1)} h(a.Lb). Open: L self-adjoint for the block pairing, so eigenpolynomials on B_s are orthogonal (expected little q-Jacobi, alpha = s). Model: OqSU2LittleQJacobiBasis.lean (s = 0). Feeds qou-pa7n (q-NS Part A).
