# Placeholder Checklist — Lean Formalization

Audit date: 2026-03-20

Items marked `[ ]` need real proofs or typed statements.
Items marked `[x]` are done.

---

## `True := by trivial` placeholders (19 total)

These fields have type `True` as a stand-in for a proper Prop/proof.
Each needs to be replaced with the correct mathematical statement and proof.

### Torsion.lean

| # | Line | Field | Intended meaning | Status |
|---|------|-------|------------------|--------|
| 1 | 62 | `ascent_preserves_mul` | `ℓ ≫ jet.mul = base.mul ≫ (ℓ ⊗ ℓ)` | [ ] |
| 2 | 64 | `restriction_preserves_comul` | restriction is coalgebra map | [ ] |
| 3 | 91 | `connection_unique` | prolonged connection uniquely determined | [ ] |
| 4 | 131 | `obstructs_collapse` | char classes obstruct spectral collapse | [ ] |
| 5 | 171 | `invariant` | `ω(g · a) = ω(a)` for all `g ∈ SU(2)` | [ ] |
| 6 | 173 | `unique` | uniqueness from adjoint vanishing | [ ] |
| 7 | 241 | `preserves_qou` | descent preserves QOU structure | [ ] |
| 8 | 342 | `codim_ge_two` | boundary has codimension ≥ 2 | [ ] |
| 9 | 344 | `exceptional_divisor_CP1` | kernel ≅ CP¹ ≅ S² | [ ] |
| 10 | 355 | `involution_restricts` | τ restricts to ∂E_n | [ ] |
| 11 | 357 | `chirality_interface` | boundary separates chirality at n=1 | [ ] |
| 12 | 408 | `dim_one` | dim M = 1 | [ ] |
| 13 | 410 | `holonomy_U1` | connection reduces to U(1) holonomy | [ ] |
| 14 | 412 | `no_bosonic_modes` | no bosonic modes survive | [ ] |
| 15 | 421 | `discrete_base` | dim M = 0 | [ ] |
| 16 | 425 | `curvature_vanishes` | curvature vanishes identically | [ ] |

### QuantumObservableUniverse.lean

| # | Line | Field | Intended meaning | Status |
|---|------|-------|------------------|--------|
| 17 | 256 | `yang_mills_minimises` | `δ_A YM(A) = 0` | [ ] |
| 18 | 337 | `q_laplacian_vanishes` | `Δ_q α = 0` | [ ] |
| 19 | 418 | `tangent_in_horizontal` | `T_p L ⊂ H_p` | [ ] |

---

## `sorry` markers (10 total)

These are proofs or definitions left incomplete with `sorry`.

### Torsion.lean

| # | Line | Declaration | Notes | Status |
|---|------|-------------|-------|--------|
| 1 | 380 | `qNumber_pos` | q-number positivity for q > 0, q ≠ 1; needs geometric series argument | [ ] |

### QuantumObservableUniverse.lean

| # | Line | Declaration | Notes | Status |
|---|------|-------------|-------|--------|
| 2 | 154 | `gaugeGroup` | Aut⊗(ω) via Tannaka–Krein; blocked on Mathlib monoidal nat trans | [ ] |
| 3 | 461 | `self_dual_curvature` | Bogomolny decomposition argument | [ ] |
| 4 | 476 | `main_commutative_diagram` | deferred to Chapter 11 | [ ] |

### Calculations.lean

| # | Line | Declaration | Notes | Status |
|---|------|-------------|-------|--------|
| 5 | 118 | `substrate_error_bound` | `|derived_q - 1.1097| < 0.0001`; needs interval arithmetic | [ ] |
| 6 | 125 | `h_q_squared_pos` | positivity of vol/ratio | [ ] |
| 7 | 131 | `h_q_value_in_unit_interval` | `0 < ℏ_q < 1` | [ ] |
| 8 | 138 | `derived_q_gt_one` | `q > 1` | [ ] |
| 9 | 159 | `full_derivation_chain` | complete chain witness | [ ] |

### MassDerivation.lean

| # | Line | Declaration | Notes | Status |
|---|------|-------------|-------|--------|
| 10 | 140 | `derive_substrate_q` | `|q - 1.1097| < 0.0001`; needs certified interval arith | [ ] |

---

## Priority triage

**High priority** (blocks downstream proofs):
- `qNumber_pos` (Torsion:380) — used by dilogarithm convergence
- `yang_mills_minimises` (QOU:256) — instanton definition completeness
- `q_laplacian_vanishes` (QOU:337) — particle definition completeness

**Medium priority** (structural completeness):
- All `True := by trivial` fields — need proper types replacing `True`
- `self_dual_curvature` (QOU:461)
- `h_q_squared_pos`, `derived_q_gt_one` (Calculations) — provable with `norm_num`

**Low priority / blocked**:
- `gaugeGroup` (QOU:154) — blocked on Mathlib API
- `main_commutative_diagram` (QOU:476) — deferred to Ch 11
- `full_derivation_chain` (Calculations:159) — needs interval arithmetic
