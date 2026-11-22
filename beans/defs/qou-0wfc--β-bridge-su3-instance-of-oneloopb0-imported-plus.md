---
# qou-0wfc
title: 'β₀ bridge: SU(3) instance of oneLoopB0 (IMPORTED) plus C_A from the N = 3 braid representation'
status: todo
type: task
created_at: 2026-11-22T16:16:14Z
updated_at: 2026-11-22T16:16:14Z
parent: qou-8lxd
---

ElectroweakVevGaps.lean oneLoopB0 takes C_A as input; SU(3) instance gives -7 at n_f=6 but is an IMPORTED SM formula and must be labelled so. Bridge: obtain C_A=3 (and C_F=4/3, already reproduced by the U_q(sl3) crossing, #8804 §48) from the N=3 braid representation (R-beta1 + R-beta2). The braid-only beta0 maps of #8804 §52 all missed (scope a); n_f cannot enter a three-strand word. Colour action on qou's own state space is open (qou-ni4b; ThreeStrandColourTowerCP.lean: H3(q) too small). Source: computations/probes/mn_own_identity/GAP-STUDY-qcd-scales.md §6 (main, merged via PR #8804); CORPUS-GREP-gluon-dynamics.md. Owner chose 'Both' 2026-11-22 (create beans + start heat-kernel route). Anti-fit: CAL-1/2/3 only; no selection against PDG/lattice values.
