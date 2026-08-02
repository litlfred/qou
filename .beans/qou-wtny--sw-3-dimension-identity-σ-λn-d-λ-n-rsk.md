---
# qou-wtny
title: 'SW-3: dimension identity Σ_{λ⊢n} d_λ² = n! (RSK)'
status: todo
type: task
priority: normal
created_at: 2026-08-02T19:30:46Z
updated_at: 2026-08-02T19:33:07Z
parent: qou-59vq
blocked_by:
    - qou-rsbf
---

Depends SW-2. The Robinson-Schensted-Knuth count Σ_λ (#SYT λ)² = n!. Mathlib may have RSK (Combinatorics.RSK?). This is the surjectivity/dimension anchor for the Wedderburn iso. Ref: [macdonald1995].

## Refinement (2026-08-02, from SW-2 agent)
Partly done in-repo: `QOU.Mathlib.rskBurnsideHolds_le12` proves Σ_{λ⊢n} dimSYT²=n!
for n≤12 by `decide` (via hook-length bridge dimSYT_eq_dimHLF); Schensted stack
(SchenstedInsertion/Recording/RSKBridge) exists. General RSK (S_n ≃ Σ_λ SYT²) is
the missing piece — NOT in Mathlib v4.24.0. `sum_dLambda_sq_eq_iff` (YoungTableaux.lean)
connects the SW `dLambda` form to `QOU.Mathlib.RSKBurnsideHolds n`.
