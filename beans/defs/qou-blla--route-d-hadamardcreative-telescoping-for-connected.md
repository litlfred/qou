---
# qou-blla
title: 'ROUTE D: Hadamard/creative-telescoping for connected sum - order <= n1*n2, does NOT cross depth'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T20:42:09Z
updated_at: 2026-10-04T15:24:14Z
parent: qou-n4nr
---

ROUTE D of epic qou-2q85. TEMPLATE, NOT AN ANSWER - and its naive form is already EXCLUDED.

EXCLUDED: folio/quantum-observable-universe/lean/QOU/Eightfold/ConnectedSumAnnihilator.lean (6 theorems, sorry-free, lean-direct exit 0) proves the naive map A_{K1} x A_{K2} -> A_{K1#K2} does not exist. Mechanism: the colour shift L is FULLY multiplicative on a pointwise product, L(f*g) = (Lf)(Lg), while M passes to ONE factor, M(f*g) = (Mf)*g. So an L-built operator never sees a tensor product. annihilator_not_monotone: f=1, g=2^n, P=L-1 gives P in A_f but P NOT in A_{f*g}, residual nonzero at EVERY colour.

WHAT SURVIVES: the Hadamard-product / creative-telescoping closure property - the pointwise product of two holonomic sequences is holonomic, with an annihilator of order at most n1*n2. That is a construction on OPERATORS, not a map of ideals, and it raises the ORDER multiplicatively.

WHY IT IS ONLY A TEMPLATE: order is not depth. Creative telescoping operates at fixed transcendence depth - it manipulates the recurrence, not the polylogarithm weight. So this route does NOT cross depth 0 -> 2 and cannot on its own bridge the gap of epic qou-2q85. Its value is as the worked example of an order-raising construction, to be copied by whatever does cross depth.

CAUTION FOR THE NEXT AGENT: 'Hadamard' matches 24 beans in this tracker and NONE of them are this - they are all HadamardFactorization, the entire-function factorization theorem. Different Hadamard. Do not read those as prior work.

- **Round 55 Progress (`2026-11-16T21:09:27Z`)**: Opened [`litlfred/qou#8202`](https://github.com/litlfred/qou/pull/8202) (`61d4706edbc97c195108082e38b072c982ba2984`, Commit 1 `842a8da69cdb997861cc48f6f16593cc33e1e707`). Keeping bean at `status: in-progress` pending owner review.
