---
# qou-atsd-t3
title: 'T3: rank Sp(2m)=m — m=1 LOWER bound (rank SL2>=1, faithful Gm diagonal torus) LANDED; UPPER bound (rank<=1, no larger torus / maximality) is the atomicity-relevant HARD open direction'
status: in-progress
type: task
priority: normal
parent: qou-atsd
created_at: 2026-07-26T00:41:31Z
updated_at: 2026-07-26T00:41:31Z
---

DONE (#4285, AtomicityFromSelfDuality.lean, sorry-free): the m=1 base torus, LOWER bound.
- diagMat/diagMat_det/diagMat_one/diagMat_mul + diagEmbedHom : Rˣ →* SL2(R) (group hom).
- diagEmbedHom_injective: faithful Gm diagonal torus => rank SL2 >= 1.

OPEN (the atomicity-relevant direction): rank SL2 <= 1 (UPPER bound) — this Gm is
MAXIMAL, SL2 has no 2-parameter torus. Needs the root-count / no-larger-torus fact.
This is the genuinely hard part; the lower bound above does NOT establish it.
Also open: general m (Sp(2m) torus (Rˣ)^m, rank m — lower bound elementary, upper hard);
the ≃*-onto-range upgrade (routine).
