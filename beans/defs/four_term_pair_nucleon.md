---
# four_term_pair_nucleon
title: four term pair nucleon missing hypotheses
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

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean`
The `four_term_pair_nucleon` theorem is unprovable. `FourTermPairNucleonContext` provides `confinedNet` as a free function without constraining its evaluations at q_0 for proton and neutron to actually equal the targets 0.999 and 0.811.



Also known as `ftpn` (its former front-matter header id; the beans CLI uses the filename id `four_term_pair_nucleon`). Recorded 2026-10-04.

## Progress (PR #8189, 2026-11-16T20:28:25Z)

- [x] Replaced the 2-tuple self-assuming projection in `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean` with matrix-trace conjugation invariance (`QOU.MathlibExt.MarkovTrace.trace_conj_of_mul_eq_one` -> `confinedNet_eq_base_trace`) composed with proved Table 2 (`proton_nf_channel_sum = 0.999`) and Table 3 (`neutron_nf_channel_sum = 0.811`) 6-channel NF sums, plus inhabited instance `canonicalFourTermPairNucleonContext`.
- [x] Verified with Lean v4.24.0 (`lean -DautoImplicit=false -s 65536`: 0 errors, 0 warnings, 0 `sorry`) and all 6 static vacuity audits (0 findings).
- [x] Verified with 80-dps `mpmath` probe (`computations/probes/round50_devacuify_6qbv_probe.py`) and 2-commit stamped witness (`computations/probes/round50-devacuify-6qbv.witness.json`, `scriptCommitSha: 357a63280dd6b77b067855dfd2ebaeb6340b2c28`, `scriptHash: 3ff73a87c2af`).
- [ ] Awaiting review and merge of PR https://github.com/litlfred/qou/pull/8189 (`status: in-progress` maintained per repo rule).
