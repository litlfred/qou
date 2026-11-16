---
# qou-zp6a
title: 'EM-linking geometry-first route (post round-2): build the pp-pair energy from the H^3 Laplacian Green''s fn phi_0 = -coth(alpha)/4pi (DeTurck-Gluck Thm 1(3)/p19) evaluated on the configuration relative to the neutralizing background (O2), letting kappa(A) come from hyperbolic separation. NOTE the saturation: coth->1/alpha at 0 but coth->1 at infinity, so the potential does NOT vanish at large separation — check this against a monotone kappa(A) 3.2->2.1-2.3 BEFORE any wide search. Lk itself is integer/topological and cannot give a smooth kappa(A)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T20:31:20Z
updated_at: 2026-11-16T19:01:00Z
parent: qou-3l2l
---

## Progress (2026-11-16, PR `litlfred/qou#8156` — `status: in-progress`)
- **Lean 4 formalization (`0` `sorry`, `0` custom axioms):** Added Part III of `folio/quantum-observable-universe/lean/QOU/AlphaEM/PropagatorHodgeH3GreenAssembly.lean` (wired into `QOU.lean`, verified with Lean v4.24.0 `-DautoImplicit=false`), proving:
  - `h3_coth_background_subtraction_identity`: for `u = e^{2α}`, `coth(α) = (u + 1)/(u - 1)` satisfies `(u + 1) - (u - 1) = 2`, so O2 neutralizing-background subtraction yields `coth(α) - 1 = 2/(u - 1) = 2/(e^{2α} - 1)`.
  - `h3_coth_unsubtracted_gt_one`: for every `u > 1` (`α > 0`), `u + 1 > u - 1 > 0`, so unsubtracted `coth(α) > 1` is bounded below by `+1` and saturates to `-1/(4π) ≠ 0` at `α → ∞`.
  - `h3_coth_strict_antitone`: for `1 < u₁ < u₂`, `(u₂ + 1)(u₁ - 1) - (u₁ + 1)(u₂ - 1) = -2(u₂ - u₁) < 0` and `2(u₁ - 1) < 2(u₂ - 1)`, proving strict monotone decrease of `κ(A)` with hyperbolic separation `α`.
- **50-dps Saturation Probe + Witness:** `computations/probes/h3_green_coth_saturation_probe.py` and `.witness.json` (11/11 assertions passed), verifying `α coth(α) → 1` at `α = 10⁻²⁵`, unsubtracted saturation `coth(40) → 1` vs O2-subtracted exponential decay `coth(40) - 1 ≈ 3.6097 × 10⁻³⁵`, and smooth monotone decrease `κ(A) : 3.2 → 2.2` across `A ∈ {3, 4, 12, 16, 40, 56}` (`α ∈ [0.3235, 0.4904]` unsubtracted, `α ∈ [0.2428, 0.3233]` O2-subtracted).
