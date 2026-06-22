# 4-input over-count triage (bean j1hg, 2026-06-22)

**Audit:** `computations/audits/canonical_script_input_audit.py` →
witness `canonical-script-input-audit.witness.json`.

The `4-input-mp-and-mn` scheme fires on any script referencing **both**
`M_P_MEV` and `M_N_MEV` — flagged as a hadronic over-count past the
three-calibration discipline (canonical = m_p + Q_β, with m_n *derived*
as m_n = m_p + Q_β + m_e). At baseline this matched **57 scripts**, but
the audit is pure-regex and cannot distinguish *input* from *comparison*,
so the signal was false-positive-heavy.

## Per-script triage

| Class | Count | Disposition |
|-------|------:|-------------|
| **Registry-source** | 7 | False positive — the script *defines/derives* the CODATA masses. Whitelisted. |
| **Comparison-only** | 27 | False positive — m_n appears only in an error %, ratio, print, or output dict; never fed into a mass/binding *prediction*. Whitelisted. |
| **Genuine input** | 23 | Real candidate — m_n is consumed inside a `Z·m_p + N·m_n` constituent sum (or rho_K/binding formula). Left flagged. |

After whitelisting the 34 false positives the audit reports
**over_count_count 57 → 23**.

### Registry-source (7)
`codata_2022_source`, `codata_constants`, `codata_masses`,
`codata_reconciliation`, `experimental_constants`, `hecke_core`,
`cal4_disguise_hunt`.

### Comparison-only (27)
`alpha_blend_tower`, `alpha_high_precision`, `atom_mass_derived`,
`beta-decay-energy-scale`, `bw_chirality_isotopes`, `catalan_binding`,
`compound_binding_via_differences`, `d_from_scratch`, `entanglement_orders`,
`flavor_split_xq_refinement`, `gap_a4_He3_residual_probe`, `hadron_knot_table`,
`hecke_characters`, `inverse-markov-qvalues`, `iterative_lp_dual_levels`,
`mass_formula_6term`, `mn_flavor_split_h3_plancherel`,
`mn_flavor_split_h4_plancherel`, `mn_flavor_split_plancherel_channel`,
`mn_standard_channel_correction`, `neutron_error_diagnostic`,
`path_b_habiro_mass_probe`, `qbeta_h4_em_normalization_probe`,
`qbeta_h4_sign_block_exact`, `qbeta_h4_sign_block_proof_search`,
`reeb_rotation_pn_test`, `sigma_shell_from_beta_chain`.

### Genuine input (23) — the real, owner-gated backlog
`atomic_mass_via_rho_k`, `categorical_q_decay_ba_low_isotopes`,
`channel_product_mass`, `delta_lambda_2row_stratum_analysis`,
`delta_lambda_empirical_tabulation`, `deuteron_binding_plancherel_channel`,
`e0_lambda_composite`, `gap_a4_L1_light_series_probe`,
`gap_a4_S_K_additive_probe`, `gap_a4_T2_per_knot_vol_probe`,
`gap_a4_T3_mass_pochhammer_probe`, `gap_a4_cross_isotope_residual_probe`,
`hecke_core_legacy`, `iterative_lp_dual_h6_deuteron`,
`path_b_defect_binding_probe`, `rho_k_h3a_co_casimir`, `rho_k_h3a_crystal`,
`rho_k_h3a_lp_dual`, `rho_k_h3a_refinement`, `rho_k_h3a_wenzl_bridge`,
`unified-mass-molecular`, `unified_low_isotope_predictor`,
`vol_density_per_block_wiring`.

**These 23 are NOT changed here.** A genuine fix rewrites each to derive
m_n = m_p + Q_β + m_e instead of consuming CODATA m_n directly — a
value-changing, witness-churning, three-calibration-discipline refactor
that must be owner-sequenced (alongside the q₀-repin sweep), not done as
a mechanical pass.

## Mechanism added

`canonical_script_input_audit.py` now reclassifies an over-count hit out
of the finding when **either**:
1. the script name is in the `OVER_COUNT_MN_NOT_INPUT` allowlist (the 34
   triaged here), **or**
2. the script carries a `# noqa: over-count-3-input` comment
   (rename-robust, self-documenting — preferred for new scripts).

Both route to the `m_n-not-an-input (… triaged …)` scheme, which is not
summed into `over_count_count`.
