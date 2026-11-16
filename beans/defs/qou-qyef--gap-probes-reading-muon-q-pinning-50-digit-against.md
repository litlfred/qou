---
# qou-qyef
title: 'GAP: probes reading muon q-pinning-50-digit against proton-pinned inputs — straddle sweep + SDP-witness pin provenance'
status: in-progress
pr: 8182
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T10:34:15Z
updated_at: 2026-10-04T15:20:19Z
parent: qou-2002
---

Found while resolving qou-2364 (PR #6596, 2026-09-04). Two related provenance/straddle defects, both wider than the one probe that was fixed.

## The straddle pattern
qbeta_markov_trace_norm_probe.py read q_0 from computations/q-pinning-50-digit.witness.json (q0Anchor: MUON, value 1.109978595642739...) to build A(q) and evaluate a constraint, while its upstream input (qbeta-decay-sdp-knot-operator.witness.json) supplied S + L2 coords computed at the PROTON pin (1.1099785827513808...). Evaluating proton-pinned coords against A(q_muon) inflated the L2 residual to 3.48e-9 (the mu-p tension ~1.15e-8 scaled by dS/dlnq ~ -21), which read as a 50000x 'regression'. Fixed there by switching the probe to Q_50_DIGIT_STR (proton, owner default 2026-08-07).

## The sweep (not yet done)
Other probes that read q-pinning-50-digit.witness.json (muon) to build q-dependent objects while consuming proton-pinned witness inputs would carry the SAME straddle silently — passing or failing at the mu-p tension scale (~1e-8) rather than the true residual. Candidate finder:
  grep -rln 'q-pinning-50-digit' computations/ --include=*.py
Then for each: does it ALSO read a proton-pinned witness (q0Anchor: proton, or containing 1.1099785827)? If so, it straddles. Fix = read Q_50_DIGIT_STR (proton) unless the probe is a deliberate muon/ideal-CAL comparison (owner exception E1/E2, AGENTS.md 2026-08-30).

## The provenance gap that hid it
qbeta-decay-sdp-knot-operator.witness.json records NO q0Anchor / q0Value (both null). That is exactly what let the straddle hide — a reader cannot tell which pin its coords were computed at without grepping the raw value 1.1099785827 out of the blob. Its producer should record q0Anchor/q0Value at save(). Same likely true of other older qbeta witnesses. A witness-provenance audit keyed on 'has q0-dependent data but no q0Anchor field' would surface the class.

Priority: normal. Not blocking anything; it is a correctness-hygiene sweep.


## Progress Update — 2026-11-16 (PR litlfred/qou#8182)

- [x] **Lean 4 Formalization (`0` `sorry`, `0` vacuity audit hits/advisories)**:
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/CrossAnchorStraddleAndSelfCertification.lean` (wired into `QOU.lean`) proves:
    - `stageB_truncation_bias_and_coxeter_trace` (`qou-2t9y`)
    - `detector_union_and_truncation_secant` (`qou-2whe`)
    - `operator_input_straddle_residual_and_amplification` (`qou-qyef`)
    - `env_diff_confound_and_true_pin_swing` (`qou-o922`)
    - `cal2_self_certification_roundtrip_and_discrepancy` (`qou-tekx`)
- [x] **50-dps Verification Probe & Witness (`0` raw `float64` fields)**:
  - `computations/probes/cross_anchor_straddle_and_self_certification_probe.py` -> `computations/probes/cross-anchor-straddle-and-self-certification-probe.witness.json` (`allPassed: true`, 5/5 assertions, `scriptHash: ccf81d198aee`, `scriptCommitSha: aa5f4d7a1cb250599dfceca8aa1274da33800a1a`).
- [x] **PR**: `litlfred/qou#8182` (`e87dd879c9ba7ce8a4dbb4751ce6e8dadbaf371b`).
