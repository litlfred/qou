---
# qou-innq
title: 'q-NS classical: remaining WALLS (Clay-level, not code-closable)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-07-24T15:49:33Z
updated_at: 2026-10-04T15:22:53Z
parent: qou-a3n3
---

Open after the T1-T9 tractable tranche (categorical mechanism fully formalized; framing fixed). Genuine walls, none code-closable: (1) Bridge B2 — functor from categorical q-NS flow on Ω¹(A) to Leray-Hopf on ℝ³ (q=1 identification); (2) Bridge B3 = conj:regularity-breakdown R1/R2 — existence of smooth finite-energy v₀ with finite-T enstrophy blowup (= Clay); (3) Levi branch value — compute β=limsup log C_L/log κ (which trichotomy regime); (4) DSS/Type-II existence — nontrivial discretely-self-similar Leray profile (finite-dim ODE shooting problem, hardest tractable target); (5) true α from actual q-NS spectrum; (6) prove DSS space-time singular set within CKN parabolic ≤1. Most tractable = (4). See docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md.

## Round 72 Progress (PR #8491)
- De-vacuified and proved genuine Lean 4.24.0 theorems in PR `litlfred/qou#8491` (C1 `0a93eba0e8b5b8ee92b4af6972a325d2dc1a28fd`, C2 `a9b922df9d2baa717878dbac10e60b5a5c341c6e`, 80-dps mpmath witness verified, 0 static audit findings).
