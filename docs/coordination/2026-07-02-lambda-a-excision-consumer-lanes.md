# λ_A excision — consumer lane classification (execution ledger)

**Parent ruling:** [`2026-06-24-lambda-a-fit-excised-per-knot-density.md`](2026-06-24-lambda-a-fit-excised-per-knot-density.md)
(λ_A is a CODATA-implied fit — excised; absolute mass routes through the
muon-anchored [`canonical_mass.py`](../../computations/canonical_mass.py) facade;
per-knot `vol_density_per_block` is valid for **binding/ratios only**).

**Bean:** `4f2d` (λ_A excision: per-knot Hecke density across QOU).
**Branch:** `claude/4f2d-lambda-a-excision-672zpe`.

## Why the previous attempt stalled (bean `0voz`)

`0voz` framed the excision as a uniform swap
`vol_density_borromean → vol_density_per_block` across ~64 scripts. Per the
🔵 CORRECTION in the parent ledger, that swap is **wrong for absolute mass**
(m_p ≈ 406 MeV, −57%): the per-knot density fixes the *density*, but the
`1/ℏ_q²` still lands on `Vol(𝓑₃)` instead of the muon anchor `Vol(4₁)`.
The blind swap broke every absolute-mass producer, so the migration stalled.

The unblocker is a **per-file lane classification**: each consumer gets the
replacement appropriate to what it computes, and files that reference λ_A
*in order to document or refute it* keep the reference.

## Lanes

| Lane | Meaning | Action |
|------|---------|--------|
| `INFRA` | defines / re-exports the deprecated functions | keep (deprecation warnings already in place) |
| `AUDIT-KEEP` | audits / probes / refutations *about* λ_A or global-vs-per-knot | keep — the reference is the subject |
| `ABS-MASS-MIGRATE` | computes an absolute mass (MeV) via the λ_A path as a live input | route through the `canonical_mass` functions `proton_mass_mev()` / `neutron_mass_mev()` / `nucleon_mass_mev(species)` |
| `BINDING-OK` | density used only where scale cancels (binding / trace ratios) | `vol_density_per_block` (per-knot `tr_M(K)`) |
| `GATED` | GAP-A-4 per-knot absolute-density frontier probes | **do not touch** (owner-gated; "no seventh fit ansatz" stands) |
| `DOC-ONLY` | name appears only in comment / docstring / deprecation notice | no action |

## Classification table

Per-file classification (call sites verified 2026-07-02, all 47 Python
consumers of `vol_density_borromean` / `linking_weight_family_a` /
`density_borromean`). Counts: INFRA 4 · ABS-MASS-MIGRATE 4 ·
AUDIT-KEEP 29 · GATED 5 · DOC-ONLY 5 · BINDING-OK 0 (per-block binding
uses appear only inside comparison testbeds or the already-migrated
`mass_table_comprehensive`).

| File | Lane | λ_A-path usage | Witness? | Note |
|---|---|---|---|---|
| `_li_2_q_util.py` | INFRA | defines the functions (+ DeprecationWarning) | no | definition site |
| `canonical_mass.py` | INFRA | facade itself; λ_A named in docstring as documented wrong form | no | |
| `mass_vol_density.py` | INFRA | re-exports `density_borromean` / `density_global` (+ DeprecationWarning) | self-check | |
| `mass_per_knot_density.py` | INFRA | per-knot mirror module wrappers | self-check | |
| `build_proton_mass_50dps_chain.py` | **ABS-MASS-MIGRATE** | `vol_density_borromean` → `M_P_PRED_BORROMEAN_MEV` | yes (`proton-mass-codata-50dps`, `option-b-proton-mass-full-chain`, `mass-formula-6term-mpfr-50dps`) | prediction routes through facade; λ_A value kept as audit column |
| `m_p_borromean_verification_50dps.py` | **ABS-MASS-MIGRATE** | `vol_density_borromean` → `m_avg_pred`, `tower_multiplier` | yes (`m-p-borromean-verification-50dps`, `borromean-volume-propagation-to-m-p`) | headline "verification" witness carries the 966-path value as the framework prediction |
| `meson_vol_density.py` | **ABS-MASS-MIGRATE** | **inline** `λ_A = 5/2 + 3h²/4` → `baryon_geom.m_p_pred`, `geom_ratio` | yes (`meson-vol-density`) | inline reimplementation dodges the DeprecationWarning and function-name greps |
| `meson_per_knot_density.py` | **ABS-MASS-MIGRATE** | **inline** λ_A → `m_p_pred` baryon reference | yes (`meson-per-knot-density`) | twin of above |
| `audits/noncanonical_reentry_audit.py` | AUDIT-KEEP | ban-registry strings only | yes | ⚠ its `canonical_replacement` strings recommend the now-excised λ_A path — stale advice, fixed on this branch |
| `audits/per_knot_density_compute_vs_paper_audit.py` | AUDIT-KEEP | `linking_weight_family_a` | yes | compute-vs-paper cross-check of the production value |
| `audits/vol_density_compute_vs_paper_audit.py` | AUDIT-KEEP | `linking_weight_family_a` | yes | twin of above |
| `binding_selection_rule_tau_closure.py` | AUDIT-KEEP | λ_A as bit-for-bit regression anchor only | yes | not a scale input |
| `derive_m_baryon_volume_form.py` | AUDIT-KEEP | back-outs empirical targets from CODATA ("NOT substrate input") | yes | diagnostic closure targets about the linking weight |
| `e0_lambda_tryall.py` | AUDIT-KEEP | `vol_density_borromean` as candidate 1 of 5 | yes | λ_A is one tested candidate |
| `entanglement_emitted_energy.py` | AUDIT-KEEP | gap-accounting of the Family-A over-prediction | prints | |
| `family_a_per_partition_h_decomposition_50dps.py` | AUDIT-KEEP | reimplements the Σ dim_q decomposition of λ_A | yes | analysis of λ_A itself |
| `gamma_gamma_pair_production_decomposition.py` | AUDIT-KEEP | Family-A vs Jones vs exact-anchor comparison | yes | explicitly audit-only |
| `linking_weight_canonical_object_lwfix.py` | AUDIT-KEEP | production vs canonical-dim_q-object comparison | yes | |
| `m_p_linking_weight_operator_valued_probe.py` | AUDIT-KEEP | docstring baseline it probes | yes | operator-valued replacement probe |
| `mass_table_comprehensive.py` | AUDIT-KEEP | facade live; λ_A "for diagnostics only" | yes | **already migrated** (2026-06-24) |
| `per_knot_density_per_block_wiring.py` | AUDIT-KEEP | global-vs-per-block wiring testbed (RED) | yes | |
| `per_knot_mass_table_demonstration.py` | AUDIT-KEEP | side-by-side uniform vs per-block | yes | validates the RED verdict |
| `probes/bring_color_weighted_base_scale_probe.py` | AUDIT-KEEP | base vs Bring-color-weighted comparison | prints | |
| `probes/markov_stab_trace_axis_probe.py` | AUDIT-KEEP | trace-axis probe vs λ_A | yes | |
| `probes/option_a_vol_per_knot_light_series.py` | AUDIT-KEEP | the canonical global-vs-per-knot light-series comparison | yes | |
| `probes/option_b_h3_h4_bratteli_probe.py` | AUDIT-KEEP | H₃→H₄ Bratteli probe vs λ_A | yes | |
| `probes/per_knot_density_borromean_h4_probe.py` | AUDIT-KEEP | H₄ decomposition of the density | yes | |
| `probes/per_knot_density_borromean_q_locality_probe.py` | AUDIT-KEEP | q-locality slope probe of the density | yes | |
| `probes/vol_density_borromean_h4_probe.py` | AUDIT-KEEP | H₄ decomposition | yes | |
| `probes/vol_density_borromean_q_locality_probe.py` | AUDIT-KEEP | q-dependence probe, gap vs CODATA reported | yes | |
| `skein_proton_canonical.py` | AUDIT-KEEP | λ_A tower baseline in the S(p)-hypothesis panel | yes | panel makes the λ_A absorption explicit ("~29 000 ppm above CODATA") |
| `subgoal_1_per_knot_mass_table_probe.py` | AUDIT-KEEP | uniform-λ_A vs per-knot comparison probe | prints | |
| `substrate/lever1_lambda_sw_no_shortcut.py` | AUDIT-KEEP | tests/refutes integer-τ recurrence vs wired Family-A | yes | |
| `substrate/sw_period_residue.py` | AUDIT-KEEP | SW-period residue ≟ λ_A identification check | yes | |
| `sweeps/mass_table_bring_faddeev_h4_sweep.py` | AUDIT-KEEP | λ_A candidate column (Family-A vs Bring+Faddeev H₄) | yes | ⚠ borderline: witness carries live λ_A-path MeV values; moves to migrate if policy hardens to "no fresh 966-path MeV in any committed witness" |
| `vol_density_per_block_wiring.py` | AUDIT-KEEP | global-vs-per-block wiring testbed (RED twin) | yes | |
| `volume_def_reconcile.py` | AUDIT-KEEP | production reading, one of three compared | yes | |
| `probes/gap_a4_He3_residual_probe.py` | GATED | local sympy λ_A reimpl. | yes | GAP-A-4 — untouched |
| `probes/gap_a4_L1_light_series_probe.py` | GATED | local sympy λ_A reimpl. | yes | GAP-A-4 — untouched |
| `probes/gap_a4_S_K_additive_probe.py` | GATED | local sympy λ_A reimpl. | yes | GAP-A-4 — untouched |
| `probes/gap_a4_T2_per_knot_vol_probe.py` | GATED | docstring convention cite | yes | GAP-A-4 — untouched |
| `probes/gap_a4_T4_schur_weyl_icosahedral_probe.py` | GATED | dim_q sum vs λ_A(q=1)=5/2 | yes | GAP-A-4 — untouched |
| `borromean_markov_trace_h_expansion_50dps.py` | DOC-ONLY | docstring link | yes (non-λ_A) | |
| `m_qclt_approx.py` | DOC-ONLY | docstring note on the +2.89% | yes (non-λ_A) | |
| `multi_layer_gap_decomposition.py` | DOC-ONLY | probe file path in a string | yes (non-λ_A) | |
| `probes/casimir_hoefsmit_additivity_probe.py` | DOC-ONLY | docstring cite; literal `linking_weight = 1` | yes | |
| `substrate/z2bn_prolongation_qdifference_constraint.py` | DOC-ONLY | docstring status-note cite | yes (non-λ_A) | |

## Migration log

*(one entry per migrated file: old call → new call, verified value vs oracle
`canonical_mass.proton_mass_mev() ≈ 938.272 MeV` / `neutron_mass_mev() ≈ 939.565 MeV`)*
