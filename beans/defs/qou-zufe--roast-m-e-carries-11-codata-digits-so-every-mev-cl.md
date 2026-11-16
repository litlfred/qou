---
# qou-zufe
title: 'ROAST: m_e carries 11 CODATA digits so every MeV claim in the corpus is capped at ~11 - audit how many quote more'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T18:37:52Z
updated_at: 2026-11-16T19:28:00Z
parent: qou-2002
---

## 2026-11-16 — CODATA m_e Relative Uncertainty Floor & Dimensionless Ratio Cancellation Formalized (PR #8169)

- **Lean 4 formalization** (`folio/quantum-observable-universe/lean/QOU/MassTheory/PlancherelNormalisationAndScaleBounds.lean`, `0` `sorry`):
  - `relVarProduct_ge_me_floor`: proves that for any dimensional MeV observable `M = m_e · R`, `(σ_M/M)² = (σ_{m_e}/m_e)² + (σ_R/R)² ≥ (σ_{m_e}/m_e)²`.
  - `dimensionless_mass_ratio_cancels_me`: proves `(m_e · R₁) / (m_e · R₂) = R₁ / R₂` for `m_e ≠ 0`.
- **50-dps verification probe**: `computations/probes/plancherel_normalisation_and_scale_bounds_probe.py` (`σ(m_e)/m_e = 16 / 51099895069 ≈ 3.13112188946675e-10`, effective decimal digits `-log₁₀(σ_{m_e}/m_e) = 9.50430002568`, PR `litlfred/qou#8169`, head `32d6039de208cfa3dab898932c88023a55ef3267`).
