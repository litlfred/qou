# Mass-table fitting audit — what's derived, what's fitted, what's open

**Date:** 2026-05-09
**Branch:** `claude/nuclear-physics-data-viz-D7GMv` (PR #600)
**Scope:** every quantity in the current canonical mass / binding /
β-decay tables for `{p, n, ²H, ³H, ³He, ⁴He}` plus the cluster-extended
`{⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca}`. Identifies for each value whether
it is **derived end-to-end**, depends on a **calibration anchor**, uses
a **census-assigned knot**, depends on an **open conjecture**, or is a
**pure fit / numerology / heuristic**.

This doc summarises the scan that produced the per-flag findings in PR
#600 and complements the existing
[`derivation-audit-report.md`](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md)
(which catalogs the 10 categorical-derivation gaps GAP-A-1 .. GAP-D-1).

## Pre-approved CAL inputs (NOT flagged)

| Input | CODATA 2022 | Role |
|-------|------------|------|
| `m_e` | 0.51099895 MeV | Leptonic mass scale (sets MeV unit) |
| `m_μ/m_e` | 206.7682830 | Fixes substrate parameter `q_0` |
| `Q_β(n)` | 0.78233341 MeV | Hadronic energy scale `E_0` |

The Q_β value is **derived arithmetically** as `m_n − m_p − m_e`, so
its uncertainty floor is propagated from CODATA m_n: ~783 ppb. Every
E_0-dependent quantity inherits this floor (see
[`e0-calibration-audit.witness.json`](../../computations/audits/e0-calibration-audit.witness.json)).

## Latest canonical witness sources

| Witness | computedAt | Status |
|---------|-----------|--------|
| [`atomic-mass-via-rho-k.witness.json`](../../computations/atomic-mass-via-rho-k.witness.json) | 2026-05-09 01:03 | fresh — ρ_K^LO mass-table (3 paths agree to 1e-13) |
| [`tr-m-q-hecke-seminormal.witness.json`](../../computations/tr-m-q-hecke-seminormal.witness.json) | 2026-05-09 00:16 | fresh — partition-sum / canonical-reducer agreement |
| [`atomic-tr-m-mpfr-50dps.witness.json`](../../computations/atomic-tr-m-mpfr-50dps.witness.json) | 2026-05-09 03:07 | fresh — anchor for all five {p, n, D, T, ³He} traces |
| [`mass-table-ppb.witness.json`](../../computations/mass-table-ppb.witness.json) | 2026-05-09 (regen) | Kashaev-law table; **flagged** — census-assigned knots |
| [`low-isotope-mass-table.witness.json`](../../computations/low-isotope-mass-table.witness.json) | 2026-05-09 (regen) | mass-excess table; same census-assignment caveat |
| [`binding-canonical.witness.json`](../../computations/binding-canonical.witness.json) | 2026-05-09 (regen) | Direction-1 canonical Markov binding |
| [`codata-reconciliation.witness.json`](../../computations/codata-reconciliation.witness.json) | 2026-05-09 01:07 | 0 ppb on all 5 anchor rows |
| [`derivation-chain-audit.witness.json`](../../computations/derivation-chain-audit.witness.json) | 2026-05-09 04:33 | walks every `*.derivation.json` |

## Per-value flags

Legend: ✅ derived, ⚠ calibration-floor inherited, ⛔ census/numerology,
🔎 open conjecture, ❌ pure fit / broken.

| Quantity | Source script(s) | Flag | Notes |
|----------|---------------|:----:|-------|
| **m_e MeV** | `codata_constants.py`, `experimental_constants.py` | CAL | hardcoded CODATA 2022 |
| **m_p MeV** | `codata_constants.py` | CAL | hardcoded CODATA 2022 |
| **m_n MeV** | `codata_constants.py` | CAL | hardcoded CODATA 2022 |
| **Q_β = 0.782 MeV** | `codata_constants.py` (derived as m_n − m_p − m_e) | ✅ | exact arithmetic; 783 ppb uncertainty floor |
| **q_0 = 1.10998…** | various; literal at 50-dps | CAL | substrate parameter; what fixes it from `m_μ/m_e` is partial — see [`m-mu-over-m-e-calibration.md`](../../content/quantum-observable-universe/braids-and-knots/m-mu-over-m-e-calibration.md) |
| **\|tr_M(K)\|** for K ∈ {p,n,D,T,³He} | `markov_trace_recursive.py` + `tr_m_q_hecke_seminormal.py` + `rho_k_h3a_refinement.py` | ✅ | three independent paths agree to 1e-13 (PR #572 closure) |
| **\|tr_M(⁴He)\|** | `atomic_tr_m_helium4.py` (canonical 50-dps) | ✅ (single path) | cross-check deferred (`eea97e9f` 5/9) |
| **shift_NF(β_p) = 19** | `per_irrep_pole_proton_h3.py` + `shift_from_nf_basis.py` | ✅ | two symbolic methods agree (Path A 5/9) |
| **shift_NF(β_D) = 40** | `per_irrep_pole_deuteron_h6.py` | ✅ | Path A multi-nucleon closure (5/9) |
| **M_pred(K) at LO** | `atomic_mass_via_rho_k.py` | ⚠ | tautology — ρ_K^LO is *defined* by `(Z m_p + N m_n)/(m_e\|tr_M\|)`, the \|tr_M\| factor cancels, predicting back the constituent sum exactly. The 0.119 / 0.302 / 0.275 / 0.759 % "errors" on D / T / ³He / ⁴He = the actual binding energies (the framework's null prediction). |
| **B_pred(²H) = 2.249 MeV** | `mass_table_ppb.py` (Kashaev law `B = m_e · Vol(6_2)`) | ⛔ | knot-census matched (²H ↔ 6_2 with ρ_F=m_e is hand-picked); 1.09 % residual vs AME |
| **B_pred(³H) = 8.469 MeV** | `mass_table_ppb.py` (`B = 2m_e · Vol(8_11)`) | ⛔ | census-assigned knot + ad-hoc ρ-factor (2 m_e); 0.156 % residual |
| **B_pred(³He) = 7.489 MeV** | `mass_table_ppb.py` (`B = 2m_e · Vol(L6a4)`) | ⛔ | census-assigned + ad-hoc; 2.97 % residual |
| **B_pred(⁴He) = 29.96 MeV** | `mass_table_ppb.py` (`A·8G` magic rule) | 🔎 | "magic A·8G" rule asserted, no Lean/categorical backing; 5.87 % residual |
| **B_pred(⁸Be⁺) cluster** | `mass_table_ppb.py` (n_α-cluster + c_αα = m_e·Vol(7²₁)) | 🔎 | cluster ansatz; 10–20 % residuals heavy nuclei |
| **fits in `binding_ladder_catalog.py`** | per-rank α back-fit to AME | ❌ | pure curve-fit (err_ppb ~10⁻¹⁰ = LP solver tol); α is whatever makes B = AME |
| **`unified_low_isotope_predictor.py`** | sums 6 derived terms; uses E_0_per_cat = 3.13 (calibrated) | ❌ broken | D, T errors ~−10⁵ %; **also broken on main**: `atom_canonical_crossings()` 2/3-arg signature mismatch (`fc7c11e0` 5/8 fallout) |
| **`4he-binding-full-pipeline.witness.json`** | tower-MeV path | ❌ broken | returns 1.99 × 10⁶ MeV vs 28.3 MeV AME; tower scale wrong (see `tower-mev-calibration-finding.md` 5/3) |
| **`free_neutron_decay.py` (NF coefficients)** | symbolic Hecke NF | ✅ | dimensionless coefficients are exact rationals in q |
| **`beta_decay_energy_scale.py` E_0_from_net = 4.155 MeV** | E_0 = Q_observed / Δ(net) | ❌ tautology | `verification.match = true` is by construction; not a prediction |
| **G_F decomposition** | `beta_decay_from_q.py` | 🔎 | "N_v is a topological invariant to be derived from the brane tower structure. OPEN COMPUTATION." |
| **g_A target = 1.27**, **C_geom = 14.25**, **λ_shell** | `beta_decay_from_q.py` open_computations | 🔎 | listed as targets, not derived |
| **Δ_λ(K) per-block binding fractions** | `rho_k_h3a_refinement.py` | ❌ heuristic | Occam single-partition pick (1 eq, 11 unknowns; "single-support + min \|Δ\|"). 5 sibling PRs (#602 #603 + Options C/E/F in flight) propose derived alternatives — all currently fail or reproduce Occam |
| **ρ(Z,N) SDP multiplicity** | conjectured `ρ = ⌊dim_q(λ*)⌉` | 🔎 | GAP-A-4 (`conj:rho-prefactor-structural`) — case-by-case SDP search, no general rule |

## Δ_λ derivation status (the central open compute)

The atomic-mass formula at the order required for 1 ppb is

$$\rho_K(q) = \rho_K^{\mathrm{LO}}(Z, N) + \frac{1}{|\mathrm{tr}_M(\beta_K)|} \sum_{\lambda \vdash 3A} y_\lambda(q)\,\chi^\lambda(\beta_K)\,\Delta_\lambda(K).$$

The current state of each Δ_λ proposal **on the deuteron (n=6, 11 partitions)**:

| Option | PR | Selector | Outcome |
|--------|------|----------|---------|
| Occam (status quo) | (in `rho_k_h3a_refinement.py`) | min \|Δ\| over single-support solutions | underdetermined; arbitrary choice of single partition + magnitude criterion |
| **B** Frob co-Casimir = 1/dim_q(λ) | [#602](https://github.com/litlfred/qou/pull/602) | theorem-forced (no free params) | fails — residual −2.30 MeV (wrong sign, vortex-blind) |
| **C** Demazure-fiber y_λ·D_w/D_w₀ | (sibling) | from e77a4b4d (5/8) Demazure-functional | fails — Δ_λ ~10⁻⁵; reproduces M^LO |
| **D** LP shadow prices (Plancherel cost) | [#603](https://github.com/litlfred/qou/pull/603) | LP dual at min Σ \|Δ_λ\|·w_λ | reproduces Occam exactly (L∞ = 1.91e-15); **moves the underdetermination to the choice of cost** rather than eliminating it |
| **D** LP shadow prices (Frobenius cost) | [#603](https://github.com/litlfred/qou/pull/603) | alt cost | picks different singleton (λ = [6], Δ = -47.16) |
| **E** crystal-graph weight | (in flight; uses PR #599 / #601 primitives) | Kashiwara crystal at q→1 | TBD |
| **F** Wenzl-bridge augmented Markov | (in flight) | augment Markov axioms with binding-energy datum | TBD (closure-pickle bug on first attempt) |

**Honest verdict:** the Δ_λ closed form in the paper is correct at the
formal level, but `M_λ(K)` (the per-block mass-functor component) is
defined by the *Archimedean realization functor's* per-block action,
which has no derived structural rule yet. This is precisely **GAP-A-3**
(brane-tower level selection) and **GAP-A-4** (ρ general rule) in the
[derivation audit report](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md).
Each of B / C / D / E / F supplies a *heuristic* model for
M_λ(K); none is the "correct" categorical answer.

The user-suggested next step (Δ_λ as a **GB-graded sum over jet
positions**, indexed by Coxeter-length k) is consistent with the
paper's bound `MAE(k) ≤ C_0 · [2]_q^{−2(k−3)}` (4× residual reduction
per level → 9 levels → 1 ppb). Implementing this requires building the
Hoefsmit-pipeline level-k map on top of `gb_filtration_jet_tracker.py`
— **deferred** until the 5 sibling PRs land (so the meta-framework can
ingest each option's `M_λ(K)` ansatz uniformly).

## β-decay status

| Quantity | Source | Flag |
|----------|--------|------|
| Q_β(n) free-neutron Q-value | `codata_constants.py` (derived) | CAL |
| E_0 = Q_β | `hecke_core.E_0_CALIBRATION_MEV` | CAL (== Q_β) |
| Q-values for A > 4 | `beta_decay_from_q.py` | 🔎 open |
| g_A, C_geom, λ_shell | `beta_decay_from_q.py` open_computations | 🔎 open |
| n → p + e⁻ + ν̄_e NF coefficients | `free_neutron_decay.py` | ✅ exact rationals in q |
| `beta_decay_energy_scale.py` E_0_from_net | tautological reconstruction | ❌ |

## Recommended priority for next session

1. **Resolve the Δ_λ derivation race** — wait for sibling PRs E + F to land, then write the cross-comparison + (if any) equivalence proof. If none of B/C/D/E/F closes, escalate GAP-A-3 / GAP-A-4 to a focused conjecture-resolution effort.
2. **Fix the broken `unified_low_isotope_predictor.py`** (1-line fix: 2-arg vs 3-arg adapter signature) so the 6-term decomposition can be re-evaluated honestly.
3. **Decommission `4he-binding-full-pipeline.witness.json`** or mark it explicitly broken in its own audit doc — its current 53000× error is misleading if anyone scrapes the witness.
4. **WitnessBuilder migration** (40 scripts) is a structural prerequisite — currently underway in a sibling agent's branch.

## Cross-references

- [`derivation-audit-report.md`](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md) — the 10 enumerated open gaps
- [`recomputed-low-isotope-mass-table.md`](../../content/quantum-observable-universe/braids-and-knots/recomputed-low-isotope-mass-table.md) — the current ρ_K^LO table (3-path machine-ε agreement)
- [`rho-k-h3a-refinement.md`](../../content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.md) — the Δ_λ closed form
- [`conj-rho-prefactor-structural.md`](../../content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.md) — GAP-A-4 conjecture
- [`pre-archimedean-derivation-chain.md`](../../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) — full step-by-step derivation chain (clean through Step 8; Steps 9–11 carry CAL inputs + open conjectures)
- [`docs/audits/2026-05-08-rho-k-mass-table-audit.md`](2026-05-08-rho-k-mass-table-audit.md) — pre-q-Hecke audit at 0.23 % MAE
- [`docs/coordination/1ppb.md`](../coordination/1ppb.md) — 1ppb coordination ledger
