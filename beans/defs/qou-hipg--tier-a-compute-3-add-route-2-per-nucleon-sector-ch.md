---
# qou-hipg
title: 'Tier A Compute 3: Add Route 2 Per-Nucleon Sector Characters, GPMT t_D, and Section 7-9 Borromean Checks to qbeta_utils.py & np_two_term_qed_mup_tension_probe.py'
status: in-progress
type: task
priority: high
created_at: 2026-11-18T21:22:35Z
updated_at: 2026-11-18T21:22:35Z
parent: qou-7xl8
---

Implement Tier A non-breaking compute updates from Section 6.2.5 and 6.2.6 of `docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md`:
1. `computations/qbeta/qbeta_utils.py`:
   - Add per-nucleon sector characters `chi_proton_3(q)`, `chi_neutron_3(q)`, `chi_proton_21(q)`, `chi_neutron_21(q)`, `chi_proton_111(q)`, `chi_neutron_111(q)` and GPMT modified trace helpers `d_mod_111_convention_D(q)` and `t_mod_111_convention_D(q, species='diff')` from `NucleonIdempotentModifiedTrace.lean`.
   - Add `borromean_v3_connected_qed_diff_mev(q=None, m_e=None, weighting='plain')`, `c2_target_two_term_at(q=None, weighting='plain')`, and `c3_target_two_term_at(q=None, c2=-1, weighting='plain')`.
2. `computations/probes/np_two_term_qed_mup_tension_probe.py` & mirror `folio/quantum-observable-universe/computations/probes/np_two_term_qed_mup_tension_probe.py`:
   - Extend SymPy & 50-dps verification to check all Section 7 (`e_(3)` and `e_(2,1)` Borromean projections), Section 8 (`L_- = L_+^T` normal-form channel collapse & `c_{L_+} + c_{L_-} = h^4`), and Section 9 (switched 4-term photon factorization `V^3 = (1 + q h V)(1 - q^-1 h V) = 1 + h^2 V - h^2 V^2`) theorems from `NucleonWeightSpaceTwoTerm.lean`, plus Route 2 `NucleonIdempotentModifiedTrace.lean` per-sector characters and GPMT modified trace.
   - Run the probe and verify exit 0.
