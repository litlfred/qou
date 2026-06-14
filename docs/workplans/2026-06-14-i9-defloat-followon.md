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

## Status

- [x] Compute env built (pyhecke_native wheel + core stack).
- [x] `delta_lambda` + `gap_a4` reclassified as probes → `probes/` (verified).
- [x] Triage of the 125: probe + already-compliant false-positive classes identified.
- [→] Scanner false-positive fixes + genuine-residue de-float — to #2277 (post-merge), with this triage.
