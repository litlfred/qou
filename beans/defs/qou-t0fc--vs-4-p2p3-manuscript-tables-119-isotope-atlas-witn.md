---
# qou-t0fc
title: 'VS-4 (P2/P3 Manuscript Tables & 119 Isotope Atlas Witnesses): Migrate 440 Unwired Table-Data Blocks and Regenerate Z00..Z118 Isotope Witnesses'
status: todo
type: task
priority: high
created_at: 2026-11-19T07:06:02Z
updated_at: 2026-11-20T08:30:00Z
parent: qou-v6so
---

## Audit Provenance

Grounded in `computations/audits/paper-status-variable-substitution-and-staleness-audit.witness.json` (`computations/audits/paper_status_variable_substitution_and_staleness_audit.py`), linked to `qou-v6so` and `qou-trd0`.

## Defects Identified by the End-to-End Audit

1. **`440 / 443` (`99.32%`) `*-table*-data.md` files and `120 / 365` inline numeric pipe-table `.md` files are unwired static literals:**
   - Only `3 / 443` `*-table*-data.md` files in the entire manuscript (`recomputed-low-isotope-mass-table-table1-data.md`, `master-bond-order-table-table1-data.md`, `predicted-bond-angles-table1-data.md`) use `{{ qou.computations... }}`.
   - High-visibility prose/table blocks carry stale pre-Wave-2 or CODATA-2018 literals:
     - `folio/quantum-observable-universe/standard-model-lagrangians/sm-params-gauge-couplings.md`: cites `137.035999127` against CODATA-2018 `137.035999084` (`+0.313 ppb`, `+0.39 sigma`) instead of CODATA-2022 `137.035999177(21)` (`-0.365 ppb`, `-2.38 sigma`).
     - `folio/quantum-observable-universe/standard-model-lagrangians/em-coupling-bring-zero-mode.md`: stops at 1-loop quadratic Form A (`137.035999313`, `+0.99 ppb`) and omits the Form-B Schwinger cubic (`137.0359991270`, `-0.365 ppb`).
     - `folio/quantum-observable-universe/standard-model-lagrangians/neutron-proton-splitting.md`: hardcodes 1-term `Q_beta = 0.78365 MeV` (`+1330 eV`, `+1700 ppm`) instead of the 2-term Borromean QED result (`0.782468 MeV`, `+139.2 eV`, `+178.5 ppm`).
     - `folio/quantum-observable-universe/appendix-recursive-atlas/recursive-atom-knot-atlas-registry.md`: 4,782-line static table emitted by `atlas_render_canonical_table.py` with CODATA-2018 proton/neutron masses and 1-term QED formulas.
2. **`368` witnesses on disk have stale `scriptHash` and `254` have stale `upstream_witness_hashes` (`sha256` drift):**
   - In particular, all `119` `.ts`-wired `computations/canonical-isotope-witness-Z00.witness.json` .. `Z118.witness.json` files (produced by `computations/canonical_isotope_witness.py`) have stale upstream `sha256` against `m-p-substrate-identity-50dps.witness.json` and `m-p-borromean-verification-50dps.witness.json` and use 1-term QED masses.

## Required Deliverables

1. Upgrade P2/P3 table producers (`borromean_binding_recompute.py`, `atom_electron_mass.py`, `canonical_isotope_witness.py`, `canonical_mass_table_extended.py`, `atlas_render_canonical_table.py`, `mass_table_ppb.py`, `level1-qvalues.py`, `free-neutron-decay.py`, `b_over_a_evaluator.py`, `coulomb_mirror_killswitch_probe.py`, `wlambda_binding_a3_mirror_selection.py`) to the Wave-2 P0 facade (`q_2t`, Form-B $\alpha_{\mathrm{EM}}^{-1}$, 2-term QED + Coulomb/mirror splittings, $E_0^{(\infty)}$, GPMT, and 4-row Hankel $Z_{3A}^{(4)}(q_0)$).
2. Regenerate `canonical-isotope-witness-Z00..Z118.witness.json` and the `368` scriptHash-drifted / `254` upstream-drifted witnesses.
3. Wire `sm-params-gauge-couplings.md`, `em-coupling-bring-zero-mode.md`, `neutron-proton-splitting.md`, and the `*-table*-data.md` files to Liquid `{{ qou.computations... }}` variable substitution.


## 2026-11-20 W13 (#8526, PR #8539)

Correction: 2/443 table-data files use Liquid (not 3; wired ones are recomputed-low-isotope-mass-table-table1-data and sigma-shell-from-beta-chain-derivation-table-data). 119 Z-witnesses confirmed. Blocked on the facade owner ask on #8526. Not touched.
