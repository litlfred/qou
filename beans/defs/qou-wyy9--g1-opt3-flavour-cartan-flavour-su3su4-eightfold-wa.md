---
# qou-wyy9
title: 'G1-opt3 (flavour Cartan): flavour SU(3)/SU(4) eightfold-way weight lattice from the Bring/icosahedral SUBSTRATE geometry (qou-d7h1 #4600; Elliott SU(3) q=1 corner). S,C = weights in the framework''s own geometry. Framework-native, harder.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-02T20:19:12Z
updated_at: 2026-11-16T19:05:33Z
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


## Progress Update — 2026-11-16 (`litlfred/qou#8159`, `4a5bd83fa5c08b2011cfb42b8d918e41431e6d96`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/Eightfold/MagnusTripleLinkingAndFlavourGradings.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Proves `su4_flavour_cube_and_charm_branching`: formalizes the root counts $|R(A_2)| = 6$ ($\mathrm{SU}(3)_f$) and $|R(A_3)| = 12$ ($\mathrm{SU}(4)_f$), the $N = 4$ Schur–Weyl cube identity $20 \times 1 + 20 \times 2 + 4 \times 1 = 64 = 4^3$, and the exact charm-stratum branching under $\mathrm{SU}(3)_f \times \mathrm{U}(1)_C \subset \mathrm{SU}(4)_f$:
    * $\mathbf{20}_S = 10_{C=0} + 6_{C=1} + 3_{C=2} + 1_{C=3} = 20$ ($J = 3/2$ charmed baryon tower),
    * $\mathbf{20}_M = 8_{C=0} + (6 + \bar{3})_{C=1} + 3_{C=2} = 8 + 9 + 3 = 20$ ($J = 1/2$ charmed baryon tower),
    * $\mathbf{4}_A = 1_{C=0} + 3_{C=1} = 4$.
- **Witness (`computations/probes/magnus-triple-linking-and-flavour-gradings.witness.json`)**: `allPassed: true` (`q0Anchor: "independent"`).
