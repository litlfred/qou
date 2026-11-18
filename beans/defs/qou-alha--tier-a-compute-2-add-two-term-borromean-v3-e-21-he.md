---
# qou-alha
title: 'Tier A Compute 2: Add Two-Term Borromean V^3 & e_(2,1) Helpers to derived_masses.py, canonical_mass.py, level1-qvalues.py, and free-neutron-decay.py'
status: completed
type: task
priority: high
created_at: 2026-11-18T21:22:35Z
updated_at: 2026-11-18T21:43:01Z
parent: qou-7xl8
---

Implement Tier A non-breaking compute updates from Section 6.2.3, 6.2.4, and 6.2.7 of `docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md`:
1. `computations/derived_masses.py`:
   - Add `e_0_scale_hierarchy_matter_mev(q=None)`, `borromean_v3_e21_strong_qcd_diff_mev(q=None, scale='E0_full')`, `borromean_v3_connected_qed_proton_mev(q=None, k_weighted=False)`, `borromean_v3_connected_qed_diff_mev(q=None, weighting='plain')`, and `q_beta_kashiwara_n2_two_term_mev(q=None, weighting='plain')`.
   - Include in `derivation_summary()` under `two_term_borromean_diagnostics` and export in `__all__`.
2. `computations/canonical_mass.py`:
   - Add `proton_qed_self_energy_borromean_mev(k_weighted=False)`, `np_qed_splitting_borromean_conn_mev(weighting='plain')`, and `neutron_mass_two_term_mev(weighting='plain')` with 50-dps fallback.
3. `computations/level1-qvalues.py` & `computations/free-neutron-decay.py`:
   - Add additive diagnostic sub-blocks `borromean_v3_two_term_diagnostics` and `two_term_borromean_qed_dressing` to their witness generators and re-verify.



## Completion Record (2026-11-18)
- Added 5 two-term Borromean V^3 & e_(2,1) helpers to `computations/derived_masses.py` and 3 accessors to `computations/canonical_mass.py`.
- Added additive diagnostic blocks to `computations/level1-qvalues.py` (`level1-qvalues.witness.json`) and `computations/free-neutron-decay.py` (`free-neutron-decay.witness.json`).
- Adversarially audited (`qou-xib5`, `lane-7b4f`): PASS (`0` regressions, 100% formula fidelity at 100 dps).
