---
# qou-c1fz
title: 'CAL-3 dataset: AME-2020 vs CODATA-2022'
status: in-progress
type: task
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-10-04T15:10:19Z
updated_at: 2026-11-16T18:12:00Z
parent: qou-2002
---

Extracted 2026-10-04 from the prose of session log `qou-vyvt` (work had no bean).

## 2026-11-16 — verification assertion & dataset diagnostics wired (PR #8146)

Added `cal3_q_beta_dataset_diagnostics()` and `assert_cal3_q_beta_dataset_consistent()` (plus `__main__` self-test and `M_N_MINUS_P_MEV` exports in `__all__`/`summary()`) in `computations/codata_2022_source.py` (and synced `qou-mass/src/qou_mass/_internal/codata_2022_source.py`):

- **Option 1 (AME-2020, current default):** `Q_BETA_MEV_AME = 0.78233341(61)` MeV (sourced by `build_cal_3_q_beta_witness.py` -> `cal-3-q-beta.witness.json` -> `codata_constants.Q_BETA_MEV`).
- **Option 2 (CODATA-2022 registry):** `Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT = M_N_MEV_CODATA_DIRECT - M_P_MEV - M_E_MEV = M_N_MINUS_P_MEV - M_E_MEV = 0.78233355931(38)` MeV (internal identity verified to `< 1e-11` MeV).
- **Dataset separation:** `+1.4931e-7` MeV (`+190.85 ppb`), `0.207σ` combined (`sqrt(0.61² + 0.38²) × 1e-6` MeV).
- Kept at `status: in-progress` (`needs-owner`) with default unchanged on AME-2020 pending owner dataset decision (`docs/audits/2026-09-08-qbeta-bar-odd-qq-coefficient-leg.md` §5). PR #8146 (`5c6c5fb610a38f0405e9d280b16b0999a8124c8f`).
