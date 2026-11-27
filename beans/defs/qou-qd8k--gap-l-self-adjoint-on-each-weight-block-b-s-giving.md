---
# qou-qd8k
title: 'GAP: L self-adjoint on each weight block B_s, giving the alpha=s little q-Jacobi basis'
status: todo
type: task
priority: normal
created_at: 2026-11-27T22:02:56Z
updated_at: 2026-11-27T22:18:48Z
blocking:
    - qou-pa7n
---

From PR #9746. Block pairings proved nondegenerate (q_ns_block_pairing_nondegenerate.lean); #9714 gives h(X+a.X-b) = -q^{2(s-1)} h(a.Lb). Open: L self-adjoint for the block pairing, so eigenpolynomials on B_s are orthogonal (expected little q-Jacobi, alpha = s). Model: OqSU2LittleQJacobiBasis.lean (s = 0). Feeds qou-pa7n (q-NS Part A).



2026-11-27: Self-adjointness proved, sorry-free, in PR #9785 (QOU/FluidDynamics/q_ns_block_self_adjoint.lean). lap_block_self_adjoint gives <Lb P,Q>_s = <P,Lb Q>_s for every s = r+1, and lap_block_eigen_orthogonal gives orthogonality of eigenvectors with distinct eigenvalues. Still open, so the bean stays open: distinctness of the diagonal of Lb r, which gives the polynomial eigenbasis (little q-Jacobi with alpha = s).
