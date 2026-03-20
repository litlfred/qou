# Placeholder Checklist — Lean Formalization

Audit date: 2026-03-20 (post-merge refresh)

Items marked `[ ]` need real proofs or typed statements.
Items marked `[x]` are done.

---

## `True := by trivial` placeholders (0 remaining / 19 original)

All 19 original `True := by trivial` stubs have been replaced with
substantive definitions in the upstream merge.

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

## `sorry` markers (4 remaining / 10 original)

### Resolved in merge [x]

| # | File | Old line | Declaration | Status |
|---|------|----------|-------------|--------|
| 1 | Torsion.lean | 380 | `qNumber_pos` | [x] |
| 2 | QuantumObservableUniverse.lean | 154 | `gaugeGroup` | [x] |
| 3 | QuantumObservableUniverse.lean | 461 | `self_dual_curvature` | [x] |
| 4 | QuantumObservableUniverse.lean | 476 | `main_commutative_diagram` | [x] |
| 5 | Calculations.lean | 125 | `h_q_squared_pos` | [x] |
| 6 | Calculations.lean | 131 | `h_q_value_in_unit_interval` | [x] |
| 7 | Calculations.lean | 138 | `derived_q_gt_one` | [x] |

### Still open [ ]

| # | File | Line | Declaration | Notes |
|---|------|------|-------------|-------|
| 8 | Calculations.lean | 122 | `substrate_error_bound` | Needs certified interval arithmetic for `Real.sqrt` |
| 9 | Calculations.lean | 179 | `full_derivation_chain` | Same; depends on `substrate_error_bound` |
| 10 | MassDerivation.lean | 141 | `substrate_q_certified` | Same; certified interval arith not yet in Mathlib |
| 11 | Elaboration.lean | 250 | `jacobi_identity_violation` | **NEW** — malformed pipe-chain proof term; needs repair |

---

## Remaining `True := by trivial` (structural)

| # | File | Line | Declaration | Notes |
|---|------|------|-------------|-------|
| 1 | Torsion.lean | 272 | `descent_preserves_qou` | Type is `True`; needs proper prop |

---

## Priority triage

**High priority** (new / fixable):
- `jacobi_identity_violation` (Elaboration:250) — malformed proof; should be repairable without new Mathlib API

**Low priority / blocked on Mathlib**:
- `substrate_error_bound` (Calculations:122) — needs certified `Real.sqrt` interval arithmetic
- `full_derivation_chain` (Calculations:179) — depends on above
- `substrate_q_certified` (MassDerivation:141) — same blocker
- `descent_preserves_qou` (Torsion:272) — structural; type needs upgrading from `True`

---

## Summary

| Category | Original | Remaining | Resolved |
|----------|----------|-----------|----------|
| `True := by trivial` stubs | 19 | 0 | 19 |
| `True` theorem types | 1 | 1 | 0 |
| `sorry` markers | 10 | 4 | 6+1 new |
| **Total incomplete** | **29** | **5** | **25** |
