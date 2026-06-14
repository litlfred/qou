# I9 CODATA de-float follow-on (PR #2277 tranche-4)

**Branch:** `claude/i9-defloat-followon-2026-06-14` (#2285)
**Parent tranche:** [#2277](https://github.com/litlfred/qou/pull/2277) (`claude/dazzling-mayer-gfuhik`) — scanner repair + 50 production scripts routed (both UNMERGED — not on `main`).

## Owner rule

Production compute must not carry bare floats / hardcoded CODATA-AME
literals — route to `substrate/codata_constants.py` registry symbols;
regenerate witnesses; run-verify. **Probes are out of scope** (float-tolerant
scratch — exclude, don't route).

## Compute env (built this session — reusable)

- `mpmath 1.3.0`, `numpy 2.4.6`, `sympy 1.14.0` (pip).
- `pyhecke_native` (the Rust Hecke core) is **not on PyPI** — built from
  `tools/pyhecke-native/` with `maturin build --release`
  (wheel `pyhecke_native-0.9.0-cp311`, installed). `cargo 1.94.1` present.
- This unblocks run-verification of any compute script in-sandbox.

## Outcome A — 2 "codemod-incompatible" scripts were BOTH probes (DONE)

Moved to `probes/` (scanner-excluded); confirmed absent from the re-run
violation list. `delta_lambda` run-verified end-to-end from `probes/` (full
import chain resolves; its `min() empty sequence` crash is pre-existing probe
behaviour, not the move).

| Script | Evidence it's a probe |
|---|---|
| `delta_lambda_full_variance_phase5e_1.py` | docstring line 2: *"Phase 5e.1 probe"*; failed Δ_λ-closure variants; witness unconsumed |
| `gap_a4_numeric_search.py` | fitting search for `F` s.t. `m_mu_pred·F = m_mu_codata`; unconsumed; superseded by `probes/_gap_a4_qsafe.py` |

## Outcome B — the 125-violation list is NOISY; de-float must be triage-first

Ran #2277's fixed scanner locally (178 scripts → **125 i9_violation**). The
list is contaminated on two axes, so the headline "75 production float-tables"
is an **overcount**:

1. **Probe false-positives (~25%).** Of the top-24 by hits, 6 are exploratory
   probes by name/content: `delta_lambda_k_star_variance_phase5d_5b`,
   `delta_lambda_2row_stratum_analysis`, `delta_lambda_empirical_tabulation`,
   `yekutieli_half_h2_observable_hunt`, `mass_sweep_wiring_status`,
   `build_six_term_substrate_model_b`. Telltale name patterns to exclude:
   `*variance*`, `*analysis*`, `*empirical*`, `*tabulation*`, `*_hunt`,
   `*_search`, `*_status`, `*phase5[a-z]*`, `*model_b*`.
2. **Already-compliant false-positives.** `binding_K_direct.py` **already
   imports** `M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION` from the
   registry (line 76) **and** carries a CLASS-A acknowledged-anchor banner,
   yet the fixed scanner still lists it (4 hits). Likely cause: the 4 hits are
   `mp.mpf(str(witness_value))` conversions being matched as literals, or the
   banner-detection fix is incomplete. **For #2277 to investigate** — its
   scanner over-reports.

**Implication:** the genuine de-float residue (bare-float dict/tuple tables,
not probes, not already-routed) is materially smaller than 75. De-floating the
raw list blind would corrupt probes, redundantly churn compliant scripts, and
shift witnesses that feed content blocks (e.g. `binding_K_direct` →
`mass-endomorphism/recomputed-low-isotope-mass-table.md`).

## Recommendation (coordination)

The de-float belongs with #2277 (owns the scanner + the 50 routed + the
baseline, all unmerged). This branch contributes: the env recipe, the 2 probe
reclassifications, and the triage above. Recommended sequence:
1. #2277 merges (scanner + 50 routed land on `main`).
2. Scanner gets the two false-positive classes fixed (probe-name exclusion
   widened; banner / `mpf(str(...))` over-match for `binding_K_direct`).
3. The genuine float-table residue is de-floated + run-verified (env recipe
   above), 26h `mass_table_ppb` source-de-floated with verification under the
   long-compute logging discipline.

## Outcome C — production de-float (owner: "skip probes, only production")

125 violations → 51 (#2277's already-routed) → 68 residue → after dropping
probe-named + already-compliant + source files, the **genuinely-production**
set is a handful of AME-validation mass tables. All flagged literals are
hardcoded AME binding energies + the m_e divisor — routed to the
`AME_B_*_MEV_VALIDATION` / `M_E_MEV` registry symbols:

| Script | Routed | Verification |
|---|---|---|
| `unified_low_isotope_predictor` | 5 AME (D/T/3He/4He/6Li) | **run-verified** (exit 0); fixed latent `max(errs):.2f`→`float()`; witness regenerated + committed |
| `canonical_mass_table_extended` | 6 AME dict | **run-verified** (f64 fast path prints routed values); fixed `ame_str` `float(ref)`; witness regen deferred to CI (MPFR-50dps) |
| `mass_table_ppb` (26h) | 26 (AME table + 5Li/6Li targets + 14× m_e) | **import-verified** (symbols resolve, top-level mpf divisions execute, `AME_TABLE[0]==mpf('2.224566')`); full numerical run + witness regen deferred (26h, logged) |

**Skipped:** `mass_table_comprehensive` — its AME values are off-canonical
(D `2.22452` vs registry `2.224566`; only 2/6 match within tolerance), so
routing 2 while leaving 4 approximate is incoherent. Needs the author to
decide: correct all to canonical, or leave as an approximate table.

## Status

- [x] Compute env built (pyhecke_native wheel + mpmath/numpy/sympy/scipy).
- [x] `delta_lambda` + `gap_a4` reclassified as probes → `probes/` (verified).
- [x] Triage of the 125: probe + already-compliant false-positive classes identified.
- [x] Production de-float: 3 genuine mass-tables routed (2 run-verified, 1 import-verified).
- [→] Witness regens for canonical (MPFR-50dps) + `mass_table_ppb` (26h) — canonical-env logged runs.
- [→] `mass_table_comprehensive` off-canonical values — author decision.
- [→] Scanner false-positive fixes (probe-name widening + `binding_K_direct` over-report) — to #2277.
