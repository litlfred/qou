---
# qou-2a2o
title: 'Route Z/2: Bring lifting obstruction as w_2-type class (centre of SU(2))'
status: todo
type: task
priority: high
created_at: 2026-10-12T19:30:20Z
updated_at: 2026-10-12T19:30:20Z
parent: qou-vo9t
---

Route 1 of qou-lx8f (owner, 2026-10-12: pursue the Z/2 and Z readings in parallel, final band deferred).

**Reading.** The band is the centre Z/2 of SU(2), and the lift is SU(2) -> SO(3) (or Spin(2) -> SO(2) for a frame). The obstruction is a w_2-type bit in H^2(Sigma_4, Z/2) = Z/2.

**Next honest step.**
1. Identify WHICH principal bundle on Bring the tower lifts. Corpus candidates: the frame bundle, "SU_q(2) frame bundles" (archimedean-lifting-intro.md), and Z(Aut A_n) (brings-is-qou-proof.md).
2. For the tangent frame, w_2 = chi mod 2 = 0, so it lifts (Bring is spin; 2^8 theta characteristics, a unique S_5-invariant one per bean qou-9l0d).

**Lean.** T1 (QOU.CentralExtension) gives the group-level criterion. Instantiating it with Z/2 -> SU(2) -> SO(3) needs those groups as Mathlib GroupExtension values. Mathlib has no Stiefel-Whitney classes, so the sheaf-level statement waits on T2-T4.

**Consequence if adopted.** The `persistence` / perpetual-obstruction claims are false on Bring for the frame bundle.
