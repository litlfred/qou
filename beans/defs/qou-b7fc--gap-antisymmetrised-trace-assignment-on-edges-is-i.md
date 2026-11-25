---
# qou-b7fc
title: 'GAP: antisymmetrised trace assignment on edges - is it a chain map, from which complex?'
status: todo
type: task
priority: normal
created_at: 2026-11-25T15:52:42Z
updated_at: 2026-11-25T16:40:04Z
parent: qou-qrrb
---

The essay's edge value tr(psi w_e) is not a 1-cochain (tr sigma + tr sigma^-1 = (q^4+1)/(q(q^2+1)) > 0 under convention D; Lean trace_add_inverse_conventionD_pos), and a constant face value is never a coboundary (const_eq_zero_of_coboundary). Open: does (tr(psi w_e) - tr(psi w_e^-1))/2 commute with d for some source complex, and is it gauge-invariant given #9415's mirror automorphism? Open conjecture-class bean: do not close until settled (rule 13a).

2026-11-25: non-abelian (Yekutieli) route, done for its first part. Holonomy-level map well-defined (gauge -> conjugation); per-face class-function traces are gauge- and basepoint-invariant; traces of products are not determined by factor traces (S3), so no linear Pi2 = d Pi1 survives tracing. Lean: QOU/BringsSurface/NonabelianStokesTrace.lean (sorry-free). OPEN, keep open: the explicit Bring closed-surface identity prod_f conj(hol_f) = prod_{i=1..4} [A_i, B_i] via a fundamental-polygon spanning tree; and whether a non-class-function (e.g. a tensor-network contraction) observable survives.
