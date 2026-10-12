---
# qou-e8ks
title: 'T1: central group extension lifting obstruction in H^2 (lift iff class = 0)'
status: completed
type: task
priority: high
created_at: 2026-10-12T19:14:51Z
updated_at: 2026-10-12T19:22:58Z
parent: qou-533l
---

Tier T1 of qou-533l.

Formalize central extensions of groups (1 -> A -> E -> G -> 1, A central) and the obstruction to lifting a homomorphism G' -> G to G' -> E as a class in H^2(G', A).

Theorem: a lift exists iff that class vanishes.

First check what Mathlib already has (groupCohomology, H2 and extensions, GroupExtension). Sorry-free and generic.

## 2026-10-12: done (group level)
`QOU/MathlibExt/CentralExtensionObstruction.lean` is sorry-free; lean-direct `-DautoImplicit=false -s 65536` exits 0. Axioms are only `[propext, Classical.choice, Quot.sound]`. It proves three things, for any central abelian kernel:
- `obstruction_cocycle`: the obstruction is a 2-cocycle.
- `obstruction_section_change`: the class is independent of the chosen section.
- `exists_lift_iff_coboundary`: φ lifts iff the obstruction is a coboundary.
The Eightfold ℤ/3 H² files are cited, not duplicated. Next: T2 (Čech level).
