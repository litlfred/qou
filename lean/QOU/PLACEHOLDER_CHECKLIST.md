# Placeholder Checklist — Lean Formalization

Audit date: 2026-03-20 (all items resolved)

Items marked `[ ]` need real proofs or typed statements.
Items marked `[x]` are done.

---

## `True := by trivial` placeholders (0 remaining / 19 original) [x]

All 19 original `True := by trivial` stubs have been replaced with
substantive definitions.

### Torsion.lean — all 16 resolved [x]

| # | Old line | Field | Status |
|---|----------|-------|--------|
| 1 | 62 | `ascent_preserves_mul` | [x] |
| 2 | 64 | `restriction_preserves_comul` | [x] |
| 3 | 91 | `connection_unique` | [x] |
| 4 | 131 | `obstructs_collapse` | [x] |
| 5 | 171 | `invariant` | [x] |
| 6 | 173 | `unique` | [x] |
| 7 | 241 | `preserves_qou` | [x] |
| 8 | 342 | `codim_ge_two` | [x] |
| 9 | 344 | `exceptional_divisor_CP1` | [x] |
| 10 | 355 | `involution_restricts` | [x] |
| 11 | 357 | `chirality_interface` | [x] |
| 12 | 408 | `dim_one` | [x] |
| 13 | 410 | `holonomy_U1` | [x] |
| 14 | 412 | `no_bosonic_modes` | [x] |
| 15 | 421 | `discrete_base` | [x] |
| 16 | 425 | `curvature_vanishes` | [x] |

### QuantumObservableUniverse.lean — all 3 resolved [x]

| # | Old line | Field | Status |
|---|----------|-------|--------|
| 17 | 256 | `yang_mills_minimises` | [x] |
| 18 | 337 | `q_laplacian_vanishes` | [x] |
| 19 | 418 | `tangent_in_horizontal` | [x] |

---

## `True`-typed theorems (0 remaining / 1) [x]

| # | File | Line | Declaration | Status |
|---|------|------|-------------|--------|
| 1 | Torsion.lean | 272 | `descent_preserves_qou` | [x] replaced with `dim_preserved` |

---

## `sorry` markers (0 remaining / 10 original + 1 new) [x]

### Original sorry markers — all resolved [x]

| # | File | Old line | Declaration | Resolution |
|---|------|----------|-------------|------------|
| 1 | Torsion.lean | 380 | `qNumber_pos` | [x] upstream merge |
| 2 | QuantumObservableUniverse.lean | 154 | `gaugeGroup` | [x] upstream merge |
| 3 | QuantumObservableUniverse.lean | 461 | `self_dual_curvature` | [x] upstream merge |
| 4 | QuantumObservableUniverse.lean | 476 | `main_commutative_diagram` | [x] upstream merge |
| 5 | Calculations.lean | 118 | `substrate_error_bound` | [x] sqrt sandwich proof |
| 6 | Calculations.lean | 125 | `h_q_squared_pos` | [x] upstream merge |
| 7 | Calculations.lean | 131 | `h_q_value_in_unit_interval` | [x] upstream merge |
| 8 | Calculations.lean | 138 | `derived_q_gt_one` | [x] upstream merge |
| 9 | Calculations.lean | 159 | `full_derivation_chain` | [x] follows from substrate_error_bound |
| 10 | MassDerivation.lean | 140 | `derive_substrate_q` | [x] sqrt sandwich + mass eq |

### New sorry markers found and resolved [x]

| # | File | Line | Declaration | Resolution |
|---|------|------|-------------|------------|
| 11 | Elaboration.lean | 250 | `jacobi_identity_violation` | [x] mul_eq_zero proof |

---

## Summary

| Category | Original | Remaining | Resolved |
|----------|----------|-----------|----------|
| `True := by trivial` stubs | 19 | **0** | 19 |
| `True`-typed theorems | 1 | **0** | 1 |
| `sorry` markers | 11 | **0** | 11 |
| **Total** | **31** | **0** | **31** |

All placeholders, stubs, and sorry markers have been resolved.
