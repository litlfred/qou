# Audit: unjustified least-squares fits across compute (2026-06-16)

**Scope.** `computations/` (this repo's top-level compute tree) and its
subdirs (`a_operator/`, `substrate/`, `markov/`, `alpha/`, `habiro/`,
`qbeta/`, `probes/`, `phase5/`, …), excluding `computations/_deprecated/`.
Rust fits in `tools/hecke-engine/` noted but not deep-dived.

**Motivation.** The rank-deficient `A^λ_{ξν}(I)` least-squares extract in
[`computations/a_operator/A_operator_extract_at_level.py`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/a_operator/A_operator_extract_at_level.py)
(uses `np.linalg.lstsq` over an **underdetermined** panel → min-norm
artifact → 21–42 % error at A ≥ 3) is being replaced by an analytic
construction (closure path b,
[`computations/a_operator/a_operator_analytic.py`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/a_operator/a_operator_analytic.py),
PRs **#2353** merged / **#2360**). The owner asked which OTHER such fits
exist. This audit is **doc-only** — no compute was modified.

**Method.** Grepped the tree for `np.linalg.lstsq`, `np.polyfit`,
`scipy.optimize.{curve_fit,least_squares,minimize,leastsq,nnls,linprog}`,
`np.linalg.pinv`-as-fit, `sklearn`, PSLQ-as-fit, and the keyword set
`fit`/`fitted`/`regression`/`least.squares`/`min-norm`/`tune`/`calibrate`.
For every genuine fit-function hit, the *consumer chain* was traced
(witness-JSON output → importing scripts → canonical/dashboard scripts)
before assigning a verdict, per the corpus-grep discipline. A least-squares
solve is classified per the prompt's three classes:

- **Justified** — determined (full-rank square) system, an exact algebraic
  solve (incl. exact Vandermonde interpolation where #samples = deg+1), or
  clearly exploratory (probe/audit-only, **not** consumed by production).
- **Suspect** — rank-deficient/overdetermined min-norm solution treated as
  canonical, or a fitted constant feeding a production observable.
- **Unclear** — needs owner judgement.

"Production" = consumed by a `canonical_*.py` / `*_50dps.py` script, the
mass dashboards (`per-observable-100x-status.witness.json`,
`onepb-status-dashboard.witness.json`), or a `LAMBDA_*`/`ALPHA_*`/`Q_*`
named constant.

---

## Executive summary

**Fit-function hits classified (non-deprecated):** 29 call sites across the
fan-out of `lstsq` / `polyfit` / `least_squares` / `pinv` / `minimize`
(the `scipy.optimize.linprog` LP/SDP-dual family is treated as a separate,
justified category — see below).

| Class | Count |
|---|---|
| **Suspect / unjustified** | **5** |
| **Justified** | **24** |
| **Unclear** | **0** |

Plus **14** `scipy.optimize.linprog`/SDP files — these are the LP-dual
confinement infra (shadow-price / active-set / Frobenius-positivity LPs),
explicitly first-class per AGENTS.md §"LP / SDP duals". They are
constrained optimisations, **not** least-squares fits, and are out of
scope of this pattern. Not enumerated individually.

### The 5 suspect offenders

All four most-concerning ones are the **same root cause as the motivating
exemplar**: underdetermined min-norm `A^λ_{ξν}(I)` interface-operator
extracts at H_9 / H_12 that feed the canonical tr_M branching chain
([`canonical_tr_m_via_branching.py`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/canonical_tr_m_via_branching.py),
which is consumed by
[`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/canonical_mass_table_extended.py)).
The fifth is a fitted per-nucleon cancellation coefficient presented under a
derivation banner (contained — no production consumer).

**Top 3 most concerning** (production-consumed, rank-deficient):

1. `A_operator_extract_at_level.py:351` — the exemplar's level-generic
   sibling; underdetermined min-norm extract, feeds the canonical chain.
2. `sublemma_2_1_A_operator_extract_h9.py:416` — the H_9 extract the
   canonical script's own comment (lines 232–243) blames for the 21–42 %
   A = 3 error.
3. `sublemma_2_1_A_operator_extract_h12_nn.py:309` (+ its streamed twin
   `…_h12_nn_streamed.py:259`) — underdetermined H_12 extracts wired into
   the canonical `(12, *)` slots.

The recommended fix for all four is the **closure-path-(b) analytic
construction** already prototyped in `a_operator/a_operator_analytic.py`
(PRs #2353/#2360): replace the min-norm `lstsq` with the isotypic
projection `A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}`, which is universal by
construction (test-word-independent). Note: as of this branch **no
consumer yet imports `a_operator_analytic`**, so the suspect min-norm
witnesses remain the live production inputs.

---

## Verdict table

| file:line | pattern | feeds | verdict | rationale |
|---|---|---|---|---|
| `a_operator/A_operator_extract_at_level.py:351` | `np.linalg.lstsq` (underdet; `underdet = n_unknowns > n_eq` computed, min-norm taken) | **PROD** — emits `A-operator-extract-h{n}-{iface}.witness.json` → `canonical_tr_m_via_branching.py` → `canonical_mass_table_extended.py` | **SUSPECT** | Min-norm `lstsq` on the underdetermined H_9+ panel; the level-generic sibling of the motivating exemplar. |
| `sublemma_2_1_A_operator_extract_h9.py:416` | `np.linalg.lstsq` (underdet flagged, status "under") | **PROD** — `sublemma-2-1-A-operator-extract-h9-nn.witness.json` (+ pp/pn) → canonical chain | **SUSPECT** | Exactly the H_9 extract blamed for 21–42 % A = 3 error in `canonical_tr_m_via_branching.py:232–243`. |
| `sublemma_2_1_A_operator_extract_h12_nn.py:309` | `np.linalg.lstsq` (underdet flagged) | **PROD** — `…-h12-nn.witness.json` in canonical `EXTRACT_FILES` map | **SUSPECT** | Underdetermined H_12 min-norm extract wired into the canonical `(12,"nn")` slot. |
| `sublemma_2_1_A_operator_extract_h12_nn_streamed.py:259` | `np.linalg.lstsq` (underdet flagged) | **PROD** — same `…-h12-{iface}.witness.json` target | **SUSPECT** | Streamed/checkpoint producer of the same underdetermined H_12 extract. |
| `per_nucleon_shift_derivation.py:354` | `np.linalg.lstsq` (overdetermined) | none (no importer; `linear_fit_cancellation` witness only) | **SUSPECT** | Fits `c_adj`/`c_avg` cancellation coefficients under a "derivation" title while the body concedes the closed form is OPEN. Contained (no production consumer) — framing/discipline flag. |
| `a_operator/A_operator_extract_general.py:308` | `np.linalg.lstsq` (guards `if n_eq < n_unknowns: continue`) | audit witness only | justified | Skips the underdetermined branch before solving; `# polynomial_q_not_applicable` marker; no canonical consumer. |
| `a_operator/A_operator_extract_kron.py:108,118` | `np.linalg.lstsq` (Kron-factorised) | none | justified | `# polynomial_q_not_applicable` marker; single-multiplicity fallback; no production consumer. |
| `sublemma_2_1_A_operator_extract.py:187` | `np.linalg.lstsq` (overdetermined, full-rank, residual ~1e-15) | **PROD** — deuteron `(6,"pn")` extract → canonical chain | justified | The H_6 deuteron extract IS full-rank; `lstsq` returns the exact solve. Feeds production legitimately — rank, not consumption, is what matters. |
| `sublemma_2_1_alpha_shift_extract.py:142` | `np.linalg.lstsq` (guards `K<N`; reports `system_well_posed`) | audit only | justified | Refuses underdetermined case; abandoned scalar-α probe; no production consumer. |
| `probes/A_operator_per_interface_probe.py:137` | `np.linalg.lstsq` | none | justified | `probes/` dir + `# polynomial_q_not_applicable`; tests A_pn=(A_pp+A_nn)/2 linearity; audit only. |
| `delta_lambda_feed_analysis.py:80,83,89,100` | `np.linalg.lstsq` (overdetermined regression) | none | justified | EXPLORATORY header; regressions *characterise* the Δ_λ gate (R² of crossing-count law) — a refutation, not a closure. |
| `habiro/habiro_coefficients_interpolate.py:201` | `np.linalg.lstsq` (exact Vandermonde, round-to-int, residual O(1e-40)) | not imported by downstream binding scripts (scaffolded) | justified | Exact integer-coefficient polynomial recovery; the fit fn is unwired into production. |
| `torus_knot_markov_trace_generalized.py:119` | `np.linalg.lstsq` (Vandermonde, n_samples ≈ deg+1) | none | justified | Exact interpolation of a known polynomial h-expansion; standalone catalogue script. |
| `option_e_phase1_h3_cross_check.py:131` | `np.linalg.lstsq` (6×3) | none | justified | Cross-check that per-block data reassembles the published H_3 Gram; validated against `pyhecke.gram`, not exported. |
| `vhat_per_crossing_chain.py:129` | `np.linalg.lstsq` (exact 2-dim solve in span{σ,I}) | none (falsification test) | justified | Recovers (a,b) of an element guaranteed in span{σ,I} by the Hecke quadratic — exact, not a free fit. |
| `pyhecke_jones_markov_atlas.py:132` | `np.linalg.lstsq` (singular fallback behind `np.linalg.solve`) | atlas infra | justified | Canonical path is the exact square `np.linalg.solve` (P partitions = P cycle types); `lstsq` is a dead-code singularity fallback. |
| `crt_markov.py:416` | `np.polyfit` (5 q-points, deg ≤ 3) | not on canonical path | justified | DEPRECATION-CANDIDATE + Class-A banner; polyfit superseded in-file by direct mpmath eval; `canonical_tower.py` only mentions it in a comment. |
| `sigma_all_symbolic_decay.py:136` | `np.polyfit` (deg 1) | none | justified | Feeds only a printed precision schedule; the canonical decay rate is the symbolic `asym_ratio_sym`. |
| `path_b_open_questions.py:371` | `np.linalg.lstsq` (overdetermined) | conjecture probe | justified | Used to *refute* (R² < 0.2: "no SYT-level linear invariant predicts diag(M)") — a negative result. |
| `probes/qbeta_habiro_recursion_probe.py:155` | `A.solve_least_squares` (rank-deficient, sympy) | none | justified | `probes/` + "INTEGER coefficients only"; candidate accepted only if residual==0 and integer. |
| `alpha/alpha_k_jones_markov_h4.py:203` | `np.linalg.lstsq` (fallback behind `np.linalg.solve`) | H-ladder (`alpha_k_jones_markov_h12.py`) | justified | Canonical path is the exact square 5×5 Markov-constraint solve; `lstsq` runs only on singularity (doesn't occur). |
| `gram_h3_symbolic_regression.py` | (no fit; `add_assertion` ≤1e-14) | audit | justified | "Regression GUARD" — recomputes 36 Gram entries and asserts equality to pyhecke; a drift test, not a statistical fit. |
| `four_unwired_theorems_regression.py` | (no fit; `add_assertion` ≤1e-40) | audit | justified | Bundled regression *guard* verifying 4 Lean-proved identities at q₀. |
| `branch_phase_fit_to_mass_tower.py` | scalar `math.sin` sums (no lstsq/minimize) | exploratory `rem:` probe | justified | `archimedean_by_design` + "exploratory branch-phase fitting" banner; consumer terminates in an interpretive remark, never a dashboard. |
| `delta_lambda_empirical_tabulation.py` | builds Δ_λ targets from CODATA RHS | only `_deprecated/*` + probes | justified (exploratory) | Genuine CODATA fit but correctly Class-A `auditOnly` banner-tagged; Δ_λ values stated as *targets*, not predictions. Banner integrity is load-bearing. |
| `casimir_beta_2_derivation.py` | (no fit; "15 fit hits" are substring noise) | probe | justified | Structural argument that β_k=0, not a numerical fit. |
| `molecular_angle_*.py`, `h2o_*.py` (`:34`/`:40`/`:44`/`:21`, …) | `scipy.optimize.minimize` (Nelder-Mead) | chemistry-side bond-angle tables | justified | VSEPR Coulomb energy minimisation over electron-domain positions on a sphere (a physical geometry solve); the `q²` weight is derived (`prop:symmetric-block-domain-weight`), not fitted; no mass/binding dashboard consumer. |
| `molecular_angle_symmetric_block_general.py:34` (+related) | `scipy.optimize.minimize` | chemistry-side | justified | Same VSEPR family as above. |
| `*_lp_dual.py`, `*_active_set*.py`, `deuteron_real_sdp.py`, … (14 files) | `scipy.optimize.linprog` / SDP | confinement LP-dual infra | justified (category) | Constrained optimisation (shadow-price/active-set), first-class per AGENTS.md §"LP / SDP duals" — not a least-squares fit. |

---

## Per-offender detail (suspect class)

### 1–4. The underdetermined A-operator interface extracts (H_9 / H_12)

**Files / lines.**
- [`a_operator/A_operator_extract_at_level.py:351`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/a_operator/A_operator_extract_at_level.py)
- [`sublemma_2_1_A_operator_extract_h9.py:416`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/sublemma_2_1_A_operator_extract_h9.py)
- [`sublemma_2_1_A_operator_extract_h12_nn.py:309`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/sublemma_2_1_A_operator_extract_h12_nn.py)
- [`sublemma_2_1_A_operator_extract_h12_nn_streamed.py:259`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/sublemma_2_1_A_operator_extract_h12_nn_streamed.py)

**Pattern.** Each builds a bilinear system `M @ A_flat = chi_lam` over a
small set of H_3 inner test-words, computes `underdet = n_unknowns > n_eq`,
and then takes the **min-norm** `np.linalg.lstsq` solution **anyway** when
`underdet` is True. For partitions λ with d_λ > 1 the system is
rank-deficient (e.g. λ=[8,1]: n_unknowns=30, n_eq=144, rank=14;
λ=[4,3,1,1]: n_unknowns=3390, rank=66 — per the canonical script's own
comment).

**Feeds.** Each emits an `…-A-operator-extract-h{n}-{iface}.witness.json`
listed in the `EXTRACT_FILES` map of
[`canonical_tr_m_via_branching.py:83–95`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/canonical_tr_m_via_branching.py),
which is imported by
[`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/canonical_mass_table_extended.py),
`tr_m_atom_via_transfer.py`, and the binding-comparison scripts — a clear
**production/canonical** chain.

**Why suspect.** The min-norm solution is fit to the H_3 inner-test-words;
it is **not** a universal interface operator. The canonical script
documents the harm itself (`canonical_tr_m_via_branching.py:232–243`):
*"A=2 deuteron matches markov_peel at 7e-15 (H_6 extract IS full-rank);
A=3 tritium/³He differ from markov_peel by 21–42 % (H_9 extracts are
under-fitted)."* This is a min-norm-artifact masquerading as a canonical
quantity, identical in kind to the motivating exemplar.

**Recommended action.** Regenerate these extracts via the **closure-path-(b)
analytic construction** prototyped in
[`a_operator/a_operator_analytic.py`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/a_operator/a_operator_analytic.py)
(PRs #2353/#2360): `A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}` (isotypic
projection of the seminormal bridge-generator matrix), which is universal
by construction. Until a consumer imports the analytic path, the suspect
min-norm witnesses remain the live production inputs — track wiring as the
closure follow-up. The H_6 deuteron extract
(`sublemma_2_1_A_operator_extract.py`) is **already correct** (full-rank,
overdetermined) and needs no change.

### 5. Fitted per-nucleon cancellation coefficients under a derivation banner

**File / line.**
[`per_nucleon_shift_derivation.py:354`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/per_nucleon_shift_derivation.py)

**Pattern.** `np.linalg.lstsq` fits cancellation coefficients
`c_adj`/`c_avg` (overdetermined: atoms × 2 columns) and serialises them to
the witness as `linear_fit_cancellation`.

**Feeds.** No Python script imports it; not referenced by any
`canonical_*` / `*_50dps` / dashboard. **Risk is contained.**

**Why suspect.** The script title frames this as *deriving* the (18, 21, 1)
per-nucleon shift, while the body concedes *"OPEN: closed-form derivation
of c_adj … requires explicit Ocneanu-weight tracking."* A fitted constant
presented under a derivation banner is a framing/discipline flag, not an
active hidden-calibration leak.

**Recommended action.** Re-label the script and witness as EXPLORATORY
(per `production-vs-exploratory-discipline.md` Step 7 banner), or add an
explicit `# CONJECTURE — linear fit, closed form OPEN` note at the
`linear_fit_cancellation` emission, so the fit is not mistaken for a
derivation if a future consumer wires it. Owner call on whether to demote
the title.

---

## Cross-reference: the A-operator closure-(b) exemplar fix

The four production-consumed suspect extracts (offenders 1–4) are the
same class of defect the owner already moved to fix:

- **Defect:** min-norm `np.linalg.lstsq` over an underdetermined panel,
  treated as a canonical operator.
- **Fix:** analytic isotypic projection
  `A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}` — universal by construction, no
  test-word dependence — in
  [`a_operator/a_operator_analytic.py`](https://github.com/litlfred/qou/blob/claude/least-squares-fit-audit-2026-06-16/computations/a_operator/a_operator_analytic.py)
  (closure path b, PRs **#2353** merged / **#2360**).

This audit confirms that closure-(b) should be propagated to **all** of the
H_9 / H_12 (and the not-yet-generated H_15 / H_18) interface-operator
slots in the `EXTRACT_FILES` map, not just the level the exemplar
addressed. No other unjustified production fit was found in the tree.

## Rust note (`tools/hecke-engine/`)

A keyword scan of `tools/hecke-engine/src` surfaced only substring noise
(`benefit`, `fit in 4 bits`, `regression test`) and one
`bin/clarabel_h3_exact_lp.rs` whose header says *"the fit … integer
coefficients (placeholder Pochhammer-style)"* — an LP feasibility binary,
not a least-squares fit, and `matrix_m_mpfr.rs:42` explicitly states *"No
new ansatz, no fit, no calibration parameter."* No Rust least-squares fit
feeds production.
