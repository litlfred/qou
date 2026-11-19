---
# qou-rhfk
title: 'N2 [Heavy Nuclei ^56Fe -> ^208Pb -> ^238U Compute + Lean]: 3D Simplicial Multi-Crossing Saturation, Pauli Content-Sum Asymmetry & Discrete Step-Graph Coulomb Audit'
status: todo
type: task
priority: high
created_at: 2026-11-19T09:36:33Z
updated_at: 2026-11-19T09:36:33Z
parent: qou-8ffl
---

Parent Epic: `qou-8ffl`. Deduplicates and extends `qou-n0so`, `qou-usft`, `qou-mumr`, `qou-4waf` (without re-opening closed steps in `qou-usft`/`qou-mumr`).

## Scope (Lane N2 — Heavy Nuclei Saturation, Pauli Content-Sum Asymmetry & Discrete Step-Graph Coulomb)

1. **Lean 4 + 80-dps Heavy-Nuclide Extension (`^56Fe`, `^120Sn`, `^197Au`, `^208Pb`, `^238U`):**
   - Combine the `N1` multi-crossing `H_4(Delta_4^2)` + GPMT `alpha`-cell operator on the balanced `A_core = 2 min(Z, N)` simplicial complex with:
     * Formalized 4-row `SU(4)` Young-diagram content-sum quadratic isospin-asymmetry penalty `Delta C_2(Z, N) = (9/4)(N - Z)^2 / A + O(1)` (`qou-n0so`) side-by-side with Pauli excess attachment Regimes A/B (`pauliBridge`, `pauliTriangle`),
     * Explicit side-by-side comparison of CAL-3 continuum `E_C(Z, A)` (`coulomb_energy.py`, preserving `qou-usft` / `qou-mumr` model-boundary disclosures) against discrete simplicial-graph / Connes shortest-path step-distance Coulomb sums on `K_A` / `C_A`.
2. **Deliverables:**
   - Dedicated `0-sorry`, `0-axiom` Lean module under `QOU/Nuclear/` and 80-dps `0`-float64 probe + witness covering `^2H .. ^238U` with zero fitted parameters.
