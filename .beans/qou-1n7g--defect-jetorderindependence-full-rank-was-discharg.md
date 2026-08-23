---
# qou-1n7g
title: 'DEFECT: JetOrderIndependence full_rank was discharged by fabricated constant jetPivots = fun _ => (1/4,2,1/8) across ALL orders; the constant extension IS the open conjecture (instance removed PR #4884)'
status: todo
type: bug
created_at: 2026-08-09T22:14:20Z
updated_at: 2026-08-09T22:14:20Z
---


## 2026-08-22 — VERIFIED RESOLVED as a defect; residue is open math (no body existed, so recording it)
Checked on main. The fabricated-constant instance is GONE: the only instance left in
QOU/Archimedean/JetOrderIndependence.lean is `trivialError_bound`; there is no
`instance ... JetOrderIndependence` applying `ofPivots` to the constant `jetPivots`.

`jetPivots : N -> Q x Q x Q := fun _ => (1/4, 2, 1/8)` survives at L305 as a plain `def`, which is
correct and not the defect -- it is the witnessed BASE-ORDER pivot data. The defect was using it to
discharge `full_rank` at every order.

The file documents this at L408-416 in its own words: "the instance fabricated its data ... a
constant extension of the order-3 pivots to every order, thereby asserting full_rank at all N >= 3
-- which *is* the open conjecture", and lists what is retained (jetOrder3_certificate, prod pivots =
1/16 != 0, sorry-free; jetJacobianBase_rank = 3; eliminationDet_ne_zero; ofPivots;
jacobianRank_eq_three_of_base) versus what is dropped (only the step from base-order certification
to all orders). That is the honest disposition the anti-laundering rule asks for.

So there is NO code fix outstanding. What remains is the genuine open conjecture -- extending the
certified base-order full_rank to all N >= 3 -- plus the separate open item noted just above it in
the file: supplying the `E` that comes from the categorical connection still needs a Lean definition
of the transport error. Recommend re-scoping this bean from `type: bug` to a research item, or
closing it and tracking the conjecture separately. Not closed here (owner call).
