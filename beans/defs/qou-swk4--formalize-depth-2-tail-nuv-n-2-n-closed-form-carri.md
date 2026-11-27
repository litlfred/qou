---
# qou-swk4
title: 'Formalize depth-2 tail: nuV (n-2) n = closed form (carrier classification + collapse)'
status: todo
type: task
priority: normal
created_at: 2026-11-27T22:37:13Z
updated_at: 2026-11-27T23:58:39Z
parent: qou-x631
---

Closed form ν_{n−2}(n) = (n−2)(n−5)Q(n)C(2n−8,n−4)/(6(n−3)n!) derived and verified exactly n=4..26 (docs/audits/2026-11-27-covariance-kernel-depth-two-tail.md). Sign of the closed form proved in BraidKnotOctonion/YoungDiagramTailThirdInstance.lean (onset n₂=10). Open: prove nuV (n−2) n = nuDepthTwoClosedForm n in Lean, following DepthOneHookClassification + YoungDiagramTailSecondInstance (carriers (n−k,3,1^{k−3}) + conjugates, boundary k=0,n−1,n; Vandermonde in falling factorials).


2026-11-27 (PR #9838): nuV n (n-2) = nuDepthTwoClosedForm n PROVED for n>=6, sorry-free, axioms propext/Classical.choice/Quot.sound; sign corollaries nuV_depthTwo_pos_iff, nuV_depthTwo_ne_zero. n=4,5 not connected to nuV in Lean (boundary shapes degenerate).


2026-11-27: n=4,5 cases proved (nuV_depthTwo_closed_form_of_four_le, sign corollaries for n>=4). Formalisation complete for all n>=4.
