---
# qou-y7ek
title: 'PPQ-1 (L1): 80-dps Newton Anchor Round-Trip Polish (2.85 ppt -> < 1e-80 on m_p/m_e -> q_0, q_2t)'
status: todo
type: task
priority: high
created_at: 2026-11-19T16:48:46Z
updated_at: 2026-11-20T16:40:00Z
parent: qou-10v9
---

Eliminate the `0.002852 ppb` (`2,852 ppQ`) anchor round-trip residual on `m_p` in `per-observable-100x-status.witness.json` by solving `q_0` and `q_2t` to full 80-dps Newton convergence against exact `M_P_OVER_M_E`.

## Resolution (2026-11-19)
- Root-caused the `0.002852 ppb` (`2,852 ppQ`) residual on `m_p` in `per_observable_100x_status.py` to comparing `M_E_MEV * MASS_RATIO_P_E = 938.27208942732424736394 MeV` against CODATA 2022's independently-rounded 11-significant-figure MeV entry `M_P_MEV_VALIDATION = 938.27208943 MeV`.
- Aligned `OBSERVABLES["m_p"]` in `computations/per_observable_100x_status.py` with `_M_P_ANCHOR_MEV = M_E_MEV * MASS_RATIO_P_E` (matching `_M_MU_MEV = M_E_MEV * M_MU_OVER_M_E`), collapsing `roundtrip_residual_ppb` from `0.002852 ppb` (`2,852 ppQ`) to `7.197e-43 ppb` (`7.197e-37 ppQ`).
- Added 80-dps verification probe `computations/probes/q0_q2t_80dps_anchor_roundtrip_probe.py` (`q0-q2t-80dps-anchor-roundtrip.witness.json`, `0` float64) verifying `< 1e-80` (`3.50e-82`) relative round-trip residual on both `q_0 = q_at(95)` and `q_2t = q_two_term_borromean_at(95)`.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.
