---
# qou-8km0
title: 'T2: Čech-level central-extension lifting obstruction (torsor over a cover)'
status: todo
type: task
priority: high
created_at: 2026-10-12T19:23:37Z
updated_at: 2026-10-12T19:23:37Z
parent: qou-533l
---

Tier T2 of qou-533l.

**Goal.** Čech level: a central extension of sheaves of groups 1 -> A -> E -> G -> 1 on a space or site, a G-torsor given by a Čech 1-cocycle on a cover, and the obstruction to lifting it to an E-torsor as a Čech 2-cocycle in A. Prove "lifts on that cover iff the 2-cocycle is a Čech coboundary", reusing T1's algebra pointwise on overlaps.

**Missing from Mathlib.** Mathlib has CechNerve, hypercovers, and NonabelianCohomology.H1 (H¹ over a family; its TODO is exactly this obstruction class). It has no Čech H² of sheaves. Start from NonabelianCohomology.H1, i.e. `Mathlib.CategoryTheory.Sites.NonabelianCohomology.H1`, and check how much of its 1-cochain API can carry the obstruction.

**Discipline.** Generic, sorry-free, and no iff as a field.
