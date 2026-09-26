---
# qou-h72x
title: 'GAP: sin²θ_W — 64 % vs 0.127 % (inconclusive); the U(1)_Y normalisation inherits open Y and N=3'
status: todo
type: task
priority: normal
tags:
    - sm-26
created_at: 2026-09-03T08:31:35Z
updated_at: 2026-09-03T08:32:40Z
blocked_by:
    - qou-q377
    - qou-y7vg
    - qou-fbrp
---

Per-term bean for the weak mixing angle (session qou-ggdk, bean qou-bsu0). Tier: conjectural (`conj:weinberg-angle-categorical`). Reconciliation of the two numbers is in-paper (qou-s2pl). Gates: qou-q377 (hypercharge Y) and, via qou-tnho, the N = 3 object qou-y7vg. qou-fbrp ("wire T₃ into Y and the normalisation") is a child whose premise is this bean's blocker.

## 🔥 Roast (2026-09-03)

(i) Needs the relative normalisation of the two U(1)s: μ̄₁₂₃ separates them (`SecondCrossingInvariant.lean`, sorry-free), but Y is open (`qou-q377`) and the whole Y programme is blocked upstream by N = 3 (`qou-tnho`, 2026-08-29).
(ii) Negatives: the pure-pattern eigenvalue ratio gives cot θ_W = q₀⁻⁴ = 0.6588 vs 1.823 (64 %); the (3,2,1) construction's 0.127 % is the best of 74 swept candidates, its witness says `path_c_status: inconclusive` (`close-321-weinberg-gap.witness.json`, float64 end-to-end); the writhe map is falsified as Y (p, n share Y = 1).
(iii) Trap: citing 0.127 % as accuracy; `1 − ([10]_q/[11]_q)² = 0.22998` (`docs/beta-decay-handoff.md:182`) is a bracket-pair scan; any h_corner exponent chosen after the sweep.
(iv) Next: not near-term. The honest lead is `su5-hypercharge-n3-gate.md` — under a 2⊕3 block structure the determinant forces U(1)_Y, so Y and N = 3 may be one gap.
(v) Forecast: conjectural until 4-A moves.
Tower status [reading: qou-ggdk]: ORDER-ZERO-ONLY — both numbers read one Hecke block's eigenvalue ratio at q₀, not the full Frobenius pairing; μ̄₁₂₃ is a degree-2 Vassiliev invariant of one link. No full-tower formulation.
