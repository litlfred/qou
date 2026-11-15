---
# qou-dgtf
title: 'elliptic_divisor_degree_zero: blocked on the argument principle'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T07:04:16Z
updated_at: 2026-10-04T15:18:58Z
parent: qou-rtxm
---

`QOU/Mathlib/EllipticDivisorDegree.lean:229`.

The boundary-cancellation half IS already formalized (`isElliptic_logDeriv`
is proved). The gap is the argument principle — Σ_{p∈P} ord_p f =
(1/2πi) ∮_{∂P} logDeriv f — which needs residue theory that Mathlib
v4.24.0 does not have.

Effectively blocked on upstream Mathlib gaining contour integration /
the residue theorem, unless someone wants to build that here.
