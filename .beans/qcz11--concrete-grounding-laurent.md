---
# qcz11
title: 'qcz11 (ACHIEVABLE): ground the abstract QCollatz theorems in LaurentPolynomial Z'
status: completed
type: task
priority: medium
parent: qcz10
created_at: 2026-07-24T21:52:00Z
updated_at: 2026-07-24T20:59:12Z
---

Non-vacuity / grounding (mirrors the sibling q-ns 'concrete Descartes QOU'
pattern, qou-4xqa). Instantiate the generic-CommRing theorems at
R = LaurentPolynomial Z, q = T 1, qinv = T(-1):
- hq : (T 1) * (T (-1)) = 1  via  rw[<- T_add]; simp[T_zero].
- qcollatz_fundamental_odd_step (T 1) (T (-1)) hq  -> concrete odd step.
- qcollatz_fundamental_even_step (T 1) (T (-1)) hq  -> concrete even step.
- qcollatz_odd_fixed_point / neg_qinv_sq_is_odd_fixed at these -> the negative
  fixed point -T(-2) concretely.
Deliverable: a QCollatz_Laurent.lean (or section) with the fundamental
2-cycle {T(-1), 1+T(-1)} and fixed point -T(-2) realized in the ACTUAL Skein
module. Verifies the abstract cluster is non-vacuous. lean-direct exit 0.

DONE: qcollatz_laurent_qunit (T 1 unit, inv T(-1)) + qcollatz_laurent_fundamental_cycle (2-cycle {T(-1),1+T(-1)}) + qcollatz_laurent_neg_fixed (-T(-2)) — all sorry-free in LaurentPolynomial Z. Abstract cluster grounded in the actual Skein module (non-vacuity).
