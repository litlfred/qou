---
# qou-yslf
title: 'GAP (Antigravity): G-equivariant triangulation of a compact Riemann surface (Rado), to supply the map in GenusFourFromEquivariantMap'
status: todo
type: task
priority: high
tags:
    - for-antigravity
    - bring-foundations
    - lean
    - mathlib-gap
created_at: 2026-11-21T07:30:00Z
updated_at: 2026-11-21T07:30:00Z
parent: qou-m3tr
---
Created 2026-11-21 by W9 (session_01VQDpPcjxVSqN8ELUBjiBHk). The owner ruling of 2026-11-21 says resource-limited work goes to a bean for Antigravity.

**Target.** `QOU.BringsSurface.GenusFourFromEquivariantMap.chi_eq_neg_six_of_equivariant_map` (merged, #8719) starts from a connected combinatorial map (darts D, rotation σ, fixed-point-free involution α) with G-actions. Its hypotheses: the actions commute with σ and α, act freely on edges and faces, and have cyclic vertex stabilisers.

**What to prove.** A compact connected Riemann surface X with a finite group G acting holomorphically carries such a map. More precisely, X has a G-invariant triangulation with every branch point a vertex, and its flag/dart encoding gives (D, σ, α). The map's genus must also equal the topological genus of X.

**Ingredients, none in Mathlib:**
- Radó's theorem (every Riemann surface is triangulable);
- the equivariant refinement: lift a triangulation of X/G, with the branch values as vertices, along the branched cover;
- the identification of the combinatorial χ with the topological one.

**Must not:** use an axiom or class standing in for the triangulation. Until proved, it stays the theorem's starting data.
