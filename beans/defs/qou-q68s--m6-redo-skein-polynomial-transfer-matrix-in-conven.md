---
# qou-q68s
title: 'M6: redo skein-polynomial-transfer-matrix in convention D'
status: completed
type: task
priority: normal
created_at: 2026-10-10T08:58:07Z
updated_at: 2026-10-10T09:01:50Z
parent: qou-d8c7
---

mass-theory/skein-polynomial-transfer-matrix.md:26 defines the Markov parameter as z_C (6 users). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: restated in D on PR #7562. Under z_D the z denominator does not cancel (pp crossing: V0 = (q^4+1)/(q^2+1)), so P_N is rational with denominator dividing (q^2+1)^(A-1); numerator span <= (A-1)(A+3), sympy-checked tight for A<=5 random crossings. Degree table recomputed (5,12,21,221,3245,44517). Lean sibling already D. Also coefficients live in Z[1/2][q^+-1] (mixed crossing), corrected.
