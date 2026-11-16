---
# parity_regime_selection
title: parity regime selection missing hypotheses
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-11-16T20:28:25Z
parent: qou-uot9
pr: 8189
---

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/parity_regime_selection.lean`
The `parity_regime_selection` theorem is unprovable. The context class `ParityRegimeSelectionContext` provides data fields but no hypotheses relating them. It needs axioms to derive the Q-value and parity regimes.



Also known as `prsm` (its former front-matter header id; the beans CLI uses the filename id `parity_regime_selection`). Recorded 2026-10-04.

## Progress (PR #8189, 2026-11-16T20:28:25Z)

- [x] Replaced the 4-tuple self-assuming projection in `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/parity_regime_selection.lean` with the factored spectator-sign derivation (`sign_identity_of_factored` via `← pow_add` and `Z + (N - 1) = A - 1`), dimensionless regime scaling (`odd_regime_of_dimless`, `even_regime_of_dimless`, `neutron_regime_of_dimless`), proved `spectator_asymmetry_num_pos` for `1 < q`, and exhibited `tritiumParityRegimeContext`.
- [x] Verified with Lean v4.24.0 (`lean -DautoImplicit=false -s 65536`: 0 errors, 0 warnings, 0 `sorry`) and all 6 static vacuity audits (0 findings).
- [x] Verified with 80-dps `mpmath` probe (`computations/probes/round50_devacuify_6qbv_probe.py`) and 2-commit stamped witness (`computations/probes/round50-devacuify-6qbv.witness.json`, `scriptCommitSha: 357a63280dd6b77b067855dfd2ebaeb6340b2c28`, `scriptHash: 3ff73a87c2af`).
- [ ] Awaiting review and merge of PR https://github.com/litlfred/qou/pull/8189 (`status: in-progress` maintained per repo rule).
