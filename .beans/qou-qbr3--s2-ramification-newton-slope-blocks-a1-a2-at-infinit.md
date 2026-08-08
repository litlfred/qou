---
# qou-qbr3
title: 'S2: ramification — Newton slope blocks A1,A2 at infinity and their square roots B1,B2 (gated on S1)'
status: todo
type: task
priority: normal
created_at: 2026-08-08T08:05:00Z
updated_at: 2026-08-08T08:05:00Z
---

Compute the slope blocks `A1, A2` from the Newton polygon of
`L1 = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1)` at `infinity` (single edge
(2,0)->(0,1), slope 1/2), then their `d`-th roots -- here **square roots**
`B1, B2`, the ramification intrinsic to a non-integral slope (RSZ §3.3).

Concrete linear algebra over a suitable extension. Exactly checkable, and no
resummation is involved yet.

**Deliverable:** explicit `A_i`; explicit `B_i`; `B_i^2 = A_i` verified
symbolically (exact arithmetic, not float).

**GATED on `qou-qbg2` (S1)** -- if S1 shows the slope->level mapping or the input
normalization is different, the blocks to root change.

Plan: `docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md` (stage S2).
