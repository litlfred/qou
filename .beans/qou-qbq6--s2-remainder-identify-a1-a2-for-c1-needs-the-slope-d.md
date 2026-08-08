---
# qou-qbq6
title: 'S2 remainder: identify A1,A2 for C1 - needs the slope decomposition, which a single-edge polygon does not supply'
status: scrapped
type: task
priority: high
created_at: 2026-08-08T09:05:00Z
updated_at: 2026-08-08T11:35:00Z
---

Split out of `qou-qbr3` (S2), whose Newton-data half is done.

**Done in `qou-qbr3`:** Newton polygon computed from the operator (single edge
(2,0)->(0,1), slope 1/2); characteristic equation `q^2 t^2 = q-1`; and PROVED
sorry-free that `q-1` is not a square in `Q[q]`, so adjoining `sqrt(q-1)` is
forced (`QOU.QBeta.not_isSquare_newtonEdgeConstant`).

**Open here:** identify RSZ's `A1, A2` -- the leading matrices of the two slope
components `P1, P2` -- for C1. Per RSZ p.39 `B_i` is ONE d-th root of each `A_i`;
the two roots `+/- sqrt(q-1)/q` of the characteristic equation are NOT `A1, A2`
(a flattening error made and corrected this session).

**BLOCKED on `qou-qbp5`.** That bean raises the prior question of whether `A1,A2`
exist for C1 at infinity at all: RSZ's `P_i` are graded pieces of the slope
filtration, one per DISTINCT slope with `mu_1 < ... < mu_k`, and C1 at infinity
has a single slope. If the objection stands there is nothing to identify here,
and this bean should be closed rather than worked.

## VOID 2026-08-08 — see docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md

There is no `A1,A2` to identify: `F(P1,...,Pk)` needs `k >= 2` distinct slopes and
C1 has one at infinity. Bugeaud [14] lifts integrality, not the two-slope
requirement.
