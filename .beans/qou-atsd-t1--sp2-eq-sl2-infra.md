---
# qou-atsd-t1
title: 'T1: Sp2=SL2 matrix infra — det^2=1 (all dims) + det=+1 dim-2 accident (sp2_mem_iff_det_one) LANDED; reindex to Mathlib symplecticGroup (Fin 1) remains'
status: completed
type: task
priority: normal
created_at: 2026-07-26T00:32:07Z
updated_at: 2026-08-03T15:17:21Z
parent: qou-atsd
---

DONE (#4285, AtomicityFromSelfDuality.lean, sorry-free):
- symplectic_det_sq_eq_one: A in symplecticGroup l R => det A^2 = 1 (all dims, CommRing).
- mul_J2_mul_transpose: A * J2 * A^T = det A . J2 for 2x2 (J2 = [[0,-1],[1,0]]).
- sp2_mem_iff_det_one: A * J2 * A^T = J2 <-> det A = 1 — the Sp2=SL2 dim-2 accident (det=+1).
PENDING: reindex Fin 1 (+) Fin 1 ~ Fin 2 to connect J2 to Mathlib's J (Fin 1) R /
symplecticGroup (Fin 1) R (bridge lemma). Feeds T3 m=1 base case.

Completed: title says LANDED (bean-hygiene-drain 2026-08-03)
