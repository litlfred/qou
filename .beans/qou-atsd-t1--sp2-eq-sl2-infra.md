---
# qou-atsd-t1
title: 'T1: Sp2 constraint infra — symplectic => det^2=1 LANDED; det=+1 (Sp2=SL2) refinement pending (Pfaffian/connectedness, ties to T3/T4)'
status: in-progress
type: task
priority: normal
parent: qou-atsd
created_at: 2026-07-25T20:42:46Z
updated_at: 2026-07-25T20:42:46Z
---

DONE (#4285): symplectic_det_sq_eq_one — any A in symplecticGroup l R has det A^2 = 1
(all dims, any CommRing), via A*J*A^T=J + det, det J a unit. Sorry-free.
PENDING: det A = +1 (excluding -1) => Sp(Fin 1)=SL2; needs the 2x2 identity
A*J*A^T = det A . J (giving det=1 directly) or connectedness/Pfaffian. Feeds T3 m=1 base case.
