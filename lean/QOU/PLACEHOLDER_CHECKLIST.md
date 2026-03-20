# Placeholder Checklist — Lean Formalization

Audit date: 2026-03-20

All 19 `True := by trivial` placeholders have been replaced.
Items marked `[x]` are typed with real propositions.
Items marked `[~]` use `axiomPlaceholder` (sorry-backed, visible in axiom audits).
Items marked `[ ]` still need real proofs (sorry markers).

---

## Former `True := by trivial` placeholders (19 total, all fixed)

### Torsion.lean

| # | Line | Field | Fix applied | Status |
|---|------|-------|-------------|--------|
| 1 | 62 | `ascent_preserves_mul` | Real type: `tensorHom ℓ ℓ ≫ μ_J = μ_A ≫ ℓ` | [x] typed, sorry proof |
| 2 | 64 | `restriction_preserves_comul` | Real type: `r ≫ Δ_A = Δ_J ≫ tensorHom r r` | [x] typed, sorry proof |
| 3 | 91 | `connection_unique` | `axiomPlaceholder` (needs connection identity infra) | [~] |
| 4 | 131 | `obstructs_collapse` | Real type: `∃ n, Nonempty (classAt n)` | [x] typed, sorry proof |
| 5 | 171 | `invariant` | `axiomPlaceholder` (needs group action on 𝒜_∞) | [~] |
| 6 | 173 | `unique` | `axiomPlaceholder` (needs invariance predicate) | [~] |
| 7 | 241 | `preserves_qou` | `axiomPlaceholder` (needs restricted-tuple QOU proof) | [~] |
| 8 | 342 | `codim_ge_two` | `axiomPlaceholder` (needs codimension infra) | [~] |
| 9 | 344 | `exceptional_divisor_CP1` | `axiomPlaceholder` (needs projective space infra) | [~] |
| 10 | 355 | `involution_restricts` | `axiomPlaceholder` (needs `τ(∂E_n) ⊆ ∂E_n`) | [~] |
| 11 | 357 | `chirality_interface` | `axiomPlaceholder` (needs chirality decomposition) | [~] |
| 12 | 408 | `dim_one` | `axiomPlaceholder` (needs manifold dimension infra) | [~] |
| 13 | 410 | `holonomy_U1` | `axiomPlaceholder` (needs holonomy infra) | [~] |
| 14 | 412 | `no_bosonic_modes` | `axiomPlaceholder` (needs Boson-emptyness proof) | [~] |
| 15 | 421 | `discrete_base` | `axiomPlaceholder` (needs manifold dimension infra) | [~] |
| 16 | 425 | `curvature_vanishes` | `axiomPlaceholder` (needs curvature-on-discrete infra) | [~] |

### QuantumObservableUniverse.lean

| # | Line | Field | Fix applied | Status |
|---|------|-------|-------------|--------|
| 17 | 256 | `yang_mills_minimises` | `axiomPlaceholder` (needs variational calc) | [~] |
| 18 | 337 | `q_laplacian_vanishes` | `axiomPlaceholder` (needs q-Laplacian defn) | [~] |
| 19 | 418 | `tangent_in_horizontal` | `axiomPlaceholder` (needs tangent bundle infra) | [~] |

### Also fixed

| File | Line | Declaration | Fix |
|------|------|-------------|-----|
| Torsion.lean | 181 | `vacuum_state_exists` | Construction now uses `sorry` (was `trivial`) |
| Torsion.lean | 271 | `descent_preserves_qou` | Return type changed from `True` to `axiomPlaceholder` |
| QOU.lean | 476 | `main_commutative_diagram` | Return type changed from `True` to `axiomPlaceholder` |

---

## `sorry` markers (10 total, unchanged)

### Torsion.lean

| # | Line | Declaration | Notes |
|---|------|-------------|-------|
| 1 | 380 | `qNumber_pos` | q-number positivity; needs geometric series argument |

### QuantumObservableUniverse.lean

| # | Line | Declaration | Notes |
|---|------|-------------|-------|
| 2 | 154 | `gaugeGroup` | Aut⊗(ω) via Tannaka–Krein; blocked on Mathlib |
| 3 | 461 | `self_dual_curvature` | Bogomolny decomposition argument |
| 4 | 476 | `main_commutative_diagram` | Deferred to Chapter 11 |

### Calculations.lean

| # | Line | Declaration | Notes |
|---|------|-------------|-------|
| 5 | 118 | `substrate_error_bound` | Needs interval arithmetic |
| 6 | 125 | `h_q_squared_pos` | Positivity of vol/ratio |
| 7 | 131 | `h_q_value_in_unit_interval` | `0 < ℏ_q < 1` |
| 8 | 138 | `derived_q_gt_one` | `q > 1` |
| 9 | 159 | `full_derivation_chain` | Complete chain witness |

### MassDerivation.lean

| # | Line | Declaration | Notes |
|---|------|-------------|-------|
| 10 | 140 | `derive_substrate_q` | Needs certified interval arithmetic |

---

## Priority for next steps

**High** — replace `axiomPlaceholder` with real types:
- `yang_mills_minimises` (when variational calculus lands in Mathlib)
- `q_laplacian_vanishes` (define q-Laplacian operator first)
- VacuumState `invariant`/`unique` (add group action to DirectLimitAlgebra)

**Medium** — prove sorry'd real-typed fields:
- `ascent_preserves_mul`, `restriction_preserves_comul` (monoidal coherence)
- `obstructs_collapse` (spectral sequence argument)
- `qNumber_pos` (geometric series)

**Low / blocked**:
- `gaugeGroup` (blocked on Mathlib monoidal nat trans)
- `main_commutative_diagram` (deferred to Ch 11)
- Calculations sorry markers (need interval arithmetic tactic)
