---
# qou-4uhn
title: 'Derivation-grade: RT shadow-world 1-loop propagator normalization on genus-4 -> 1/(pi dim H1)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-14T02:13:47Z
updated_at: 2026-11-16T19:01:00Z
parent: qou-3l2l
---

## Progress (2026-11-16, PR `litlfred/qou#8156` — `status: in-progress`)
- **Lean 4 formalization (`0` `sorry`, `0` custom axioms):** Added Part I of `folio/quantum-observable-universe/lean/QOU/AlphaEM/PropagatorHodgeH3GreenAssembly.lean` (complementing `QOU.Archimedean.EmMeasureGaussBonnet` and `QOU.Archimedean.PerLoopMeasureShadowAssembly`, wired into `QOU.lean`, verified with Lean v4.24.0 `-DautoImplicit=false`), proving:
  - `gauss_bonnet_measure_denominator_eq_eight`: `4 * (4 * (g - 1)) = 8 * (2 * g - 2)` for all `g : ℤ` (genus-independence of the Gauss–Bonnet per-loop ratio `|χ(Σ_g)| / (4 Area(Σ_g)) = 1/(8π)`).
  - `propagator_dimH1_eq_eight_iff_g4`: the homology-mode propagator normalization `1/(π dim H₁(Σ_g)) = 1/(2πg)` coincides with `1/(8π)` if and only if `g = 4` (Bring's surface, `dim H₁(Σ₄) = 8`, `4 |χ(Σ₄)| = 3 dim H₁(Σ₄) = 24`).
  - `bring_eight_factorization_disambiguation`: separates the conjugate-pair shadow factorization `8 = 2 × 4` (`pairCount = 2` for `H^{1,0} ⊕ H^{0,1}`, `4π` gauge-loop unit) from the total Betti factorization `8 = 4 × 2` (`4` isogenous elliptic factors in `Jac(Σ₄) ~ E_{5τ₀}³ × E_{τ₀}` of rank `2` each), recording the phase-4 MOC (`Φ`) scope boundary.
- **50-dps / Exact Probe + Witness:** `computations/probes/h3_green_coth_saturation_probe.py` and `.witness.json` (11/11 assertions passed).
