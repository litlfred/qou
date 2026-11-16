---
# qou-72rd
title: 'GAP: two probes label the MUON value A as proton_q0; their anchor-stability claims are 3-4 orders of magnitude off'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T09:37:35Z
updated_at: 2026-10-04T15:20:30Z
parent: qou-2002
---

Found while classifying the hardcoded-q0 literals (PR #5535). NOT fixed there, deliberately -- fixing it means committing a witness regeneration whose numbers move 3-4 orders of magnitude for a reason unrelated to that PR's diff.

THE DEFECT. computations/probes/flavor_split_alpha_bond_dilog_probe.py and computations/probes/binding_qgaussian_ell1_ceiling_measurement.py each evaluate at two anchors:
    analyze(mpf(Q_50_DIGIT_STR), 'proton_q0')
    analyze(_muon_q0(),          'muon_q0')
In the committed witnesses (2026-06-29) the leg labelled proton_q0 carries the MUON value A = 1.10997859555733471989..., because q_parameter.Q_50_DIGIT_STR was muon-valued when they ran. It is the proton pin now.

CONSEQUENCE. Their 'Anchor-stable' claim was measured between A and B -- two MUON values 2.8e-12 apart -- not across the 11.5 ppb proton-muon separation. Re-run today:
    flavor-split-alpha-bond-dilog   alpha_true_anchor_drift  5.8e-8  -> 2.4e-4   (~4000x)
    binding-qgaussian-ell1-ceiling  inflation_anchor_drift   6.9e-11 -> 2.3e-7   (~3350x)
    A_bond_sensitivity              0.1324 -> 0.1029 (22 %)
The witness descriptions still assert 'Anchor-stable'; that wording does not survive the re-measurement even though both verdicts (RULED OUT / the ceiling) do.

SECOND DEFECT, blocking the fix. A fresh run also DROPS q0Anchor and q0Value from both witnesses -- fields q0_anchor_consistency_audit reads. Find out why q0_anchor_is_declared no longer resolves for these producers BEFORE regenerating, or the refresh trades a stale number for lost provenance.

RELATED, same shape, separate cause: deltalambda/mu3_anchor_consistency_probe re-runs with d2 0.4225 -> 0.3278 (22 %) and rel_shift_vs_mixed -> exactly 0.0. Verified by stashing the edit and re-running the UNMODIFIED file: same numbers, so it is main-side drift in the y_lambda / chi caches since 2026-08-07, not a mislabel.


## Progress Update — 2026-11-16 (PR litlfred/qou#8176)

- **Lean 4 Formalization (`0` `sorry`, `0` vacuity audit hits/advisories)**:
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/MuonAnchorInversionAndStraddleClassification.lean` (wired into `QOU.lean`) proves:
    - `cal2MuonQ_roundtrip_and_excess`, `cal2MuonQ_secant_and_rel_shift`, and `cal2MuonQ_strict_three_value_ordering` (`qou-5op4`)
    - `crossAnchor_drift_magnification_and_inv_hbar_sq_secant` (`qou-72rd`)
    - `habiroSymbolicPayload_stamp_independent_and_secant` (`qou-mha1`)
    - `markovZD_over_markovZC_and_diff` and `fourMethod_straddle_cross_ratio_and_rel_delta` (`qou-3zby`, `qou-dau6`)
- **50-dps Verification Probe & Witness (`0` raw `float64` fields)**:
  - `computations/probes/muon_anchor_inversion_and_straddle_classification_probe.py` -> `computations/probes/muon-anchor-inversion-and-straddle-classification-probe.witness.json` (`allPassed: true`, 4/4 assertions, `scriptHash: 3b8c800c79a2`, `scriptCommitSha: 80719a03fb31a87a5718702e605db5cbed1f57ce`).
- **PR**: `litlfred/qou#8176` (`0e75c0ddb6a55fd2ce17a4041ac822379106c89c`).
