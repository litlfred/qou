---
# rtkb
title: 'RT-3: Kirby calculus (surgery presentation + Kirby-move invariance of the RT sum)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:20:00Z
updated_at: 2026-10-04T15:24:14Z
parent: qou-o9ge
---

Parent: rtep. TIER: RESEARCH WALL (3-manifold topology, essentially absent from Mathlib). The RT
3-manifold invariant τ(M) = Kirby-colored sum over a surgery link, WELL-DEFINED because it is
invariant under the two Kirby moves (handle slide K1, blow-up/stabilization K2). Needs: surgery
presentation of 3-manifolds, the Kirby-move equivalence, and the invariance proof (uses the Kirby
color ω=Σ d_λ λ and the modular S,T relations). Mathlib has neither 3-manifolds nor Kirby calculus.
This is the deepest input (RT) — the piece that makes the surgery sum a manifold invariant. HONEST:
not achievable without first building a large 3-manifold-topology library. Candidate to cite
(Reshetikhin-Turaev 1991; Turaev 1994) rather than formalize. Owner decision needed on ambition.
