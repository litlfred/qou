---
# qou-atsd-t3-lie
title: 'T3-lie (THE closeable route): rank(sl2)<=1 via Mathlib LieAlgebra.rank — compute natTrailingDegree(charpoly(ad h))=1 for the regular diagonal h in sl 2'
status: completed
type: task
priority: normal
parent: qou-atsd
created_at: 2026-07-26T01:03:32Z
updated_at: 2026-07-26T12:10:00Z
---

CLOSED (#4285, AtomicityLieRank.lean, sorry-free, lean-direct exit 0):
`sl2_rank_le_one {K} [Field K] (h2 : (2:K) ≠ 0) : LieAlgebra.rank K (sl (Fin 2) K) ≤ 1`.
The full brick chain landed: sl2 basis (h,e,f) + trace-zero spanning + linindep;
ad h eigenvector eqs [h,e]=2e,[h,f]=−2f,[h,h]=0; toMatrix(ad h)=diag(0,2,−2);
charpoly = X³−4X (via LinearMap.charpoly_toMatrix + Matrix.charpoly_diagonal);
coeff 1 = −4 ≠ 0 (needs 2≠0) ⇒ natTrailingDegree ≤ 1 ⇒ frame ⇒ rank ≤ 1.
This is the atomicity UPPER bound on the Lie side — the piece the elementary
group-rank route could not reach.

REMAINING (follow-up, not this bean): rank ≥ 1 (h regular) to get rank(sl2)=1;
the rank G = rank Lie(G) identification note tying back to atomicity rankG.

--- original plan below ---

STRATEGIC WIN: algebraic-GROUP rank is not in Mathlib, but LIE-ALGEBRA rank IS
(LieAlgebra.rank + rank_le_natTrailingDegree_charpoly_ad). rank G = rank Lie(G),
so the atomicity upper bound rank G <= 1 reframes to rank(sl2) <= 1 — REACHABLE.

DONE (#4285, AtomicityLieRank.lean, sorry-free): the frame
rank_le_one_of_ad_charpoly_trailing — (ad x).charpoly.natTrailingDegree <= 1 => rank <= 1.

REMAINING CORE (this bean): the concrete sl2 computation.
- h = singleSubSingle(0,1) = diag(1,-1) in sl 2 R (basis h, e=single(0,1), f=single(1,0)).
- brackets: [h,e]=2e, [h,f]=-2f, [h,h]=0 => ad h = diag(0,2,-2) in basis (h,e,f).
- charpoly(ad h) = X(X-2)(X+2) = X^3 - 4X ; natTrailingDegree = 1.
- apply frame => rank(sl 2 R) <= 1 (over a field / suitable R).
- rank >= 1 (h regular): isRegular_iff_natTrailingDegree_charpoly_eq_rank + natTrailingDegree=1.
Then rank(sl2)=1. Connect to atomicity rankG (rank G = rank Lie G — identification note).
Feasible multi-step; the sl2 basis + bracket + charpoly is the work.
