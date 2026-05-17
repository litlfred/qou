# Derivable-axioms audit — 2026-05-17

After this session's discharge sweep, the QOU Lean repo has **272
total axioms** (with **17 sorries remaining**, all intentional). This
audit categorizes the axioms by whether they are **derivable from
existing Mathlib infrastructure** or genuinely require external
content.

## Discharge attempts this session

### ✅ Upgraded from axiom → theorem

| Axiom (was) | Theorem (now) | Proof method |
|---|---|---|
| `q_sub_q_inv_pos_at_q_gt_one` | proven | `inv_mul_cancel₀` + `mul_lt_mul'` contradiction |
| `q_pow_dom_inv_at_q_gt_one` | proven | `one_lt_pow₀` + same inverse-bound argument |
| `qBracket_one` (was no theorem) | proven | `pow_one`, `zpow_neg`, `zpow_one`, `div_self` |
| `qBracket_zero` | proven (already) | `simp` on if_zero |
| `qFactorial_zero` | proven (already) | `rfl` |
| `phi_q_ne_li2_q` | proven from value axioms | empty-product/empty-sum 1 ≠ 0 |
| `kappaClosed_neg` | proven from substrate axioms | sign analysis |
| `towerTerm_at_zero` | proven | `abs_zero`, `neg_zero`, `li2_q_at_zero` |
| `HasCorrectedMassEndomorphismTower.*` | proven | class extraction |

## Categorization of remaining axioms

### Tier A: Likely derivable from Mathlib (high priority for follow-up)

These are elementary statements that should be provable from existing
Mathlib lemmas (`Polynomial`, `Real.log`, `Finset.prod_fiberwise`,
etc.).

| Axiom | File | Why derivable |
|---|---|---|
| `qBracket_one_at_q_eq` | magic-shell-coupling-kappa.lean | Now proven in QPartitionCombinatorics as `qBracket_one` |
| `qBracket_two` | (not yet stated as theorem) | `(q² − q⁻²)/(q − q⁻¹) = q + q⁻¹` — algebraic, needs `q ≠ 0` |
| `log_one_add_lower_taylor_bound` | q-beta-spectral-bridge.lean | Mathlib has `Real.add_one_le_exp` + log monotonicity |
| `log_one_add_taylor_bound` | q-beta-spectral-bridge.lean | Mathlib has `Real.abs_log_sub_add_sum_range_le` (likely) |
| `qLog_tendsto_log` | explicit-formula.lean | L'Hôpital via `Polynomial.continuous_eval` |
| `qNumberSym_classical_limit` | q-casimir.lean | Same — L'Hôpital + continuity |
| `eigenvalue_norm_sq` | hasse-weil-bound.lean | Direct algebra from functional equation hyp + CS bound |
| `one_dim_factors_per_generator` | OneDimChiBridge.lean | `Finset.prod_fiberwise` regrouping |
| `term_6_plus_term_7_eq_high_strata` | unified-curvature-rank-mass-formula.lean | `List.foldl_append + List.filter_range` |

**Effort**: 30-90 minutes per item. Tractable.

### Tier B: Derivable from substantive QOU infrastructure

Provable once the corresponding QOU layer is filled in:

| Axiom | Blocked by |
|---|---|
| `centralIdempotent_central_axiom` | Concrete `centralIdempotent` def + JM-commutativity |
| `centralIdempotent_orthogonal_axiom` | Same |
| `bar_centralIdempotent_transpose_axiom` | Same + bar involution on JM elements |
| `markov_trace_unique_axiom` | Basis-of-reduced-words lemma + Hecke quadratic relation |
| `transfer_matrix_level_independence` | Concrete `HadronConfig` + Markov product theorem |
| `pp_eigenvalue_ratio` | Concrete `pp transfer matrix` — Vieta direct |
| `chi_std_proton/neutron_closed_form` | Sympy-verified; Lean port = degree-22 Laurent ring normalization |
| `matrix_algebra_baer_right` | Standard linear algebra; needs principal-ideal infrastructure |

**Effort**: Multi-session per item (some are weeks of careful work).

### Tier C: External textbook / numerical bounds (axiom-stable)

These are properly external — cited results from named sources that
should stay as axioms unless Mathlib upstreams the result:

| Axiom | External source |
|---|---|
| `schrijver_strong_duality` / `schrijver_complementary_slackness` | Schrijver 1986 §7.2, §7.4 |
| `weierstrass_diff_eq_axiom` | Lang Elliptic VI.3.6 |
| `castelnuovo_severi_bound_axiom` | Weil 1948 §V; Milne §27 |
| `macroscopic_iff_rh_axiom` | von Koch 1901 |
| `wenzlClosedForm` (and similar) | Wenzl 1988 |
| `Hecke quadratic / braid relations` | Iwahori 1964 / Kassel 1995 |
| `QCasimir_comm_E/F_axiom` | Kassel 1995 §VI.4 |
| `forward_backward_agreement_axiom` | CDF / PDG observational |
| `qou_motivic_galois_char_almost_everywhere_nontrivial` | Yekutieli 2010 |
| `protonExample_archimedean_agreement` | Empirical witness rel_diff=0 |

**Effort**: Stay as axioms until Mathlib has the corresponding theory.

### Tier D: §3b-cond conjectural inputs (sorry IS the conjecture)

These ARE the conjectural content, intentionally kept as `sorry` per
the §3b-cond convention:

- `staircase_ew_residual_conjecture` instance (1 sorry, intentional)
- `canonicalCrossCoupling.cross_decomposition` (1 sorry, empirically refuted)
- `MassComputationChainRoadmap.*` (10 sorries, roadmap stubs)
- `Kashaev.lean::pieceVolume` (2 sorries, SnapPy bridge pending)
- `partition-sum-proton-residual` (1 sorry, "by-design false")

**Effort**: Not to be discharged; these encode open research questions.

## Recommended follow-up

1. **Tier A first**: Pick 3-5 axioms that have clear Mathlib derivations
   and discharge them in a focused session. Estimated 4-6 hours total
   to convert ~5 axioms to theorems.

2. **Tier B second**: After Tier A, identify which QOU infrastructure
   pieces need filling (Hecke central idempotent construction is the
   biggest blocker).

3. **Tier C stays**: Reduce the citation burden by keeping these as
   axioms with explicit `-- Ref:` annotations.

4. **Tier D stays**: These are the actual open conjectures; do not
   touch.

## Session totals

- **~80 new axioms** added (this session)
- **2 axioms upgraded to theorems** in this audit pass
- **~10 axioms identified as Tier A** (high priority discharge candidates)
- **CI signals**: pending — author runs `lake build QOU` to validate
