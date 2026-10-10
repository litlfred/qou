---
# qou-wyy9
title: 'G1-opt3 (flavour Cartan): flavour SU(3)/SU(4) eightfold-way weight lattice from the Bring/icosahedral SUBSTRATE geometry (qou-d7h1 #4600; Elliott SU(3) q=1 corner). S,C = weights in the framework''s own geometry. Framework-native, harder.'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-02T20:19:12Z
updated_at: 2026-10-10T07:18:33Z
parent: qou-8lxd
blocked_by:
    - qou-8pl3
---

## Body added 2026-10-10 — bean was TITLE-ONLY since 2026-08-02

**Task (reconstructed from the title):** the G1-opt3 route — build the flavour
`SU(3)`/`SU(4)` eightfold-way weight lattice from the flavour Cartan.

**It is downstream, not a front.** The weight lattice follows the fundamental's
dimension. The framework gives `N = 2`, and
`QOU/Eightfold/RowCapObstruction.lean` proves sorry-free that at `N = 2` the
alternating channel `dim V_(1^3) = C(N,3)` **vanishes** — no singlet, hence no
`8 + 1`, for any `q`. Building an `SU(3)` weight lattice before `N = 3` exists
would construct the lattice of a representation the corpus has proved the
substrate does not host.

So `qou-8pl3` (routes to `N = 3`) comes first, and `qou-j3w6` (the owner decision
on condition 5) picks which route.

**Not scrapped, and not a duplicate of `8pl3`:** that one asks *whether* `N = 3`
is reachable; this asks what the lattice looks like once it is. Kept so the
dependency is recorded rather than rediscovered. Siblings on the same option
fan: `qou-yw3v` (opt1), `qou-n6ls` (opt2), `qou-10zv` (opt4).
