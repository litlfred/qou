---
# qou-2q85
title: Depth-0 to depth-2 bridge - six attack routes for the convolution/volume gap
status: in-progress
type: feature
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T20:42:08Z
updated_at: 2026-11-18T07:49:45Z
parent: qou-n4nr
---

THE GAP. bowtie_K and the whole knot-convolution layer sit at TRANSCENDENCE DEPTH 0 (algebraic, no polylogarithms); the volume functor sits at DEPTH 2 (P_2/P_1, real). Measured: 44 files build the convolution layer, 9 build the quantum-function layer, ZERO files mention both. The disconnection is a DEPTH GAP, not an oversight.

THE MECHANISM EXISTS. def:hq-bi-filtration's compatibility table: H_q^(n1,K1) *_q H_q^(n2,K2) subset of + H_q^(n1+n2,K'). The q-shuffle is depth-ADDITIVE - exactly one of its five listed operations moves depth and it is the product. So a quadratic maps n -> 2n. What is missing is a depth-1 INPUT, since 0+0 = 0.

Children: ROUTE A qou-jopk, ROUTE B qou-wnhk, ROUTE C (DEAD, see qou-hnri/qou-wjbd), ROUTE D qou-blla, ROUTE E qou-960k, ROUTE F qou-zovy.
Audit: docs/audits/2026-09-04-depth-one-is-empty.md. Parent epic: qou-8lxd.

ROAST 2026-09-04: docs/audits/2026-09-04-roast-of-the-six-attack-routes.md. Revised ranking - A first (the only route agnostic about R1), B demoted (settle R1 first; 'square it' is the vanishing case of an antisymmetric map), C dead, D template only, E the ONLY route aimed at flavour rather than volume, F cheap regardless.

SCOPE CORRECTION the epic did not state: routes A, B and D all target VOLUME. This epic sits under qou-8lxd, 'eightfold way / SM derived from QOU', whose goal is FLAVOUR - and bean qou-52fu already established the volume route cannot get there (the complement's holonomy is rho: pi_1 -> PSL(2,C), rank 1, more SL(2) not SU(3)). So four of six routes work a SUB-GOAL. Defensible - volume feeds mass and binding, which are real targets - but it should be said, and it was not.

FIRST MOVE IS NOW qou-ox7v (the graded-algebra reading question), not a construction.

R1 SETTLED 2026-09-04 (qou-ox7v, completed) AND IT CLOSED ROUTE B (qou-wnhk, completed).

The answer: the shuffle filtration and the K-theory tower are CONSISTENT - my R1 worry was wrong and is retracted. Weight 2 splits into DECOMPOSABLE (products of weight-1, infinite rank) and INDECOMPOSABLE (K_3^ind = Bloch-Wigner = volume, rank r_2). The shuffle-square lands in the decomposable part; 'ind' is defined as the quotient BY products. So squaring cannot reach the volume by construction.

LIVE ROUTES NOW: A (qou-jopk) - the ONLY surviving depth-crossing route, and the prune explicitly does not touch it, since the coproduct's 2=2+0 split is not a product of two degree-1 elements. E (qou-960k) - the only route aimed at flavour. F (qou-zovy) - cheap hygiene. D (qou-blla) - template only. B and C are now both closed.

So the epic is down from six routes to TWO substantive ones (A and E) plus one hygiene item.

ROUTE A SETTLED 2026-09-04 (qou-jopk, completed) - AND THE EPIC NOW HAS NO SURVIVING DEPTH-CROSSING ROUTE.

A's action exists (from the PRODUCT, 0+2=2 - my 'coproduct 2=2+0' framing was wrong), is well-defined on the volume stratum (proved: it preserves decomposables, so it descends to the indecomposable quotient), and is TRIVIAL: def:hq-bi-filtration's own grid gives H_q^(0,K) as the central idempotent e_{lambda_K} (or scalars) at every tabulated cell, and H_q^(2,K) is the e_K-isotypic piece, so the acting element is the UNIT and acts as the identity.

TALLY: B closed by qou-ox7v (shuffle-square lands in the decomposable part, which is what 'ind' discards). C closed three weeks before this session (all three readings of J^bullet excluded, qou-wjbd). A closed here (well-defined, trivial). D is a template that does not cross depth. So of the four routes that targeted VOLUME, all four are now closed or non-crossing.

WHAT REMAINS: E (qou-960k) - PGL(3)/Fock-Goncharov, 35 held library dirs and zero content blocks, and per roast R3 the ONLY route aimed at FLAVOUR, which is what the parent epic qou-8lxd is actually named for. F (qou-zovy) - hygiene, cheap, do regardless.

AND ONE THING THIS EPIC LEARNED THE HARD WAY: three of the four closures came from reading the corpus's own definitions rather than from new mathematics. The 'ind' gloss, the low-(n,K) grid's explicit H_q^(0,K) column, and the three-readings-of-J audit were all already written. The epic's real cost was not derivation; it was that nobody had put those three sentences next to each other.



Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: depth-0 to depth-2 bridge - six attack routes for the convolution/volume gap

## Round 83 Progress (PR #8392)
- Branch: `feat/round83-lambdasum-taupos-pairenergy-c1eval-nobranch-43c1`
- Commit 1 (code + probe): `e226ba66ce53cea91430549ce1efc48cd1eeef24`
- Commit 2 (witness): `17c21a76b062fd76e16d4f84b23687e02fc0050c` (`scriptSha256 = 0635fcc96bfd3bd66e7452f9553ce1314e6829b0b1a6b7202ea86d48b4b232a6`)
