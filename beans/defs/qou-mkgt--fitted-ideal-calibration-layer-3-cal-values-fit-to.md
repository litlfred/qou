---
# qou-mkgt
title: 'Fitted-ideal calibration layer: 3 CAL values fit to low-isotope binding'
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T03:59:40Z
updated_at: 2026-11-16T18:12:00Z
parent: qou-2002
---

PAUSED by owner ruling 2026-08-26: 'the large q_0 fitted variation means model is not correct enough yet to do this... we are missing term in binding.' The fitted-ideal layer is on hold as a CALIBRATION (its diagnostic measurements stand). Unblocking condition is the missing super-pairwise additive extensive term in B, NOT more fitting. Do not open follow-ons that fit harder: the 4He outlier (-59.2%) and the m_K/m_pi CAL-3 option are both on hold.

## 2026-11-16 — state verification on `origin/main` (PR #8146)

Verified on `origin/main` (`dc12b128cc`):

- `computations/fitted_ideal_low_isotope_calibration.py`, `computations/fitted-ideal-low-isotope-calibration.witness.json`, and `docs/coordination/calibration-layers.md` carry the PAUSED banner and `anti_fit_label: {"is_a_fit": true, "may_be_wired_to_production": false}` with all 3 witness assertions green (`gate_reproduces_committed_sweep`, `three_calibration_points`, `fitted_not_derived`).
- Remains paused per 2026-08-26 owner ruling pending the super-pairwise additive extensive binding term; kept at `status: in-progress`. PR #8146 (`5c6c5fb610a38f0405e9d280b16b0999a8124c8f`).
