---
# qou-wxey
title: 'N6 [Z=0..118 Valley of Stability, Magic Numbers & Drip-Line Sweep]: 80-dps Isobar & Demand Audit Across 1 <= A <= 238 via O(A^2) Simplicial + Transfer-Matrix Groebner-Shirshov'
status: completed
type: task
priority: normal
created_at: 2026-11-19T11:13:48Z
updated_at: 2026-11-19T12:46:11Z
parent: qou-8ffl
---

Parent Epic: `qou-8ffl`. Coordinates with `qou-yd54` (*Z=0..118 isotope atlas wiring*) and depends on `N1` (`qou-ki22`) + `N2` (`qou-rhfk`).

## Scope (Lane N6 — Periodic-Table Valley of Stability, Magic Closures & Drip-Line Audit Across `1 <= A <= 238`)

1. **Isobar & Demand Sweep (`conj:periodic-table-demand`, `periodic-table-demand-conjecture.md:30-51`):**
   - Using the `O(A^2)` inductive `2x2` transfer-matrix Groebner-Shirshov normal form (`crossingChain_eq_tmProduct_nf`) together with the multi-crossing `H_4(q_2t)` + GPMT simplicial + Pauli Young-diagram content-sum + two-term QED + Coulomb functional (`N1` + `N2`), evaluate all `(Z, A - Z)` isobar chains across `1 <= A <= 238` at 80 dps (`0` float64, zero fitting).
2. **Deliverables:**
   - Machine-counted 80-dps witness comparing parameter-free isobar minimizers `Z_*(A)` against AME2020 stable isotopes, testing palindromic normal-form / shell-gap signatures at `(2, 8, 20, 28, 50, 82, 126)`, and recording proton/neutron drip-line demand behavior transparently without post-hoc tuning.



## Completed (Checkpoint 4 — 2026-11-19)
- Executed full 80-dps parameter-free periodic-table synthesis and valley-of-stability / magic-number / drip-line sweep across `1 <= A <= 238` in `computations/probes/nuclear_wave3_periodic_table_synthesis_probe.py` (`computations/probes/nuclear-wave3-periodic-table-synthesis.witness.json`, `scriptHash: 6bd3aabab90f`, `0` float64).
