---
# qou-dau6
title: 'GAP: cross_check_trM_1ppb --strict fails on main — peel witness computed at proton q0 but gate expects the muon pin'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T12:34:43Z
updated_at: 2026-10-04T15:19:53Z
parent: qou-2002
---

## Cross-link — and a retraction of my own framing (2026-08-23)

I appended a note here calling this bean's diagnosis one of **three competing
hypotheses**. That was wrong and never merged; this replaces it.

**This bean and `qou-3zby` are both correct.** `667c9ab3f6` on `main`
(2026-08-21) adjudicated the red and found **two simultaneous causes**: the
C/D convention straddle (`qou-3zby`) *and* the muon/proton pin mismatch
(this bean). The four-method classification, the fix path for each, and the
withdrawal of my spurious third candidate are recorded on `qou-3zby`.

**Relevant to this bean specifically:** the guard gave *false assurance*. It
refused to start off-muon, which made the run look pin-uniform while a
committed input (Habiro) sat at the **proton** pin — matching convention C
there to 2.71e-13, exact rather than near. It survived because the guard
checked one of its four inputs; Habiro has no `q0Value` to compare
(`q0Anchor: ambiguous`) and Hoefsmit has no anchor at all. `667c9ab3f6`
widened the guard to every input that records a q0 and to NAME the ones that
do not.

Fix for this half: regenerate `habiro-coefficients-extended` under
`QOU_Q0_ANCHOR=ideal`. Blocked — see `qou-iayk`.


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
