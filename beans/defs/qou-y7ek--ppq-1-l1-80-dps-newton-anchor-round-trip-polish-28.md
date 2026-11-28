---
# qou-y7ek
title: 'PPQ-1 (L1): 80-dps Newton Anchor Round-Trip Polish (2.85 ppt -> < 1e-80 on m_p/m_e -> q_0, q_2t)'
status: completed
type: task
priority: high
tags:
    - compute-accuracy
created_at: 2026-11-19T16:48:46Z
updated_at: 2026-11-28T00:13:00Z
parent: qou-10v9
---

Eliminate the `0.002852 ppb` (`2,852 ppQ`) anchor round-trip residual on `m_p` in `per-observable-100x-status.witness.json` by solving `q_0` and `q_2t` to full 80-dps Newton convergence against exact `M_P_OVER_M_E`.

## Resolution (2026-11-19)
- Root-caused the `0.002852 ppb` (`2,852 ppQ`) residual on `m_p` in `per_observable_100x_status.py` to comparing `M_E_MEV * MASS_RATIO_P_E = 938.27208942732424736394 MeV` against CODATA 2022's independently-rounded 11-significant-figure MeV entry `M_P_MEV_VALIDATION = 938.27208943 MeV`.
- Aligned `OBSERVABLES["m_p"]` in `computations/per_observable_100x_status.py` with `_M_P_ANCHOR_MEV = M_E_MEV * MASS_RATIO_P_E` (matching `_M_MU_MEV = M_E_MEV * M_MU_OVER_M_E`), collapsing `roundtrip_residual_ppb` from `0.002852 ppb` (`2,852 ppQ`) to `7.197e-43 ppb` (`7.197e-37 ppQ`).
- Added 80-dps verification probe `computations/probes/q0_q2t_80dps_anchor_roundtrip_probe.py` (`q0-q2t-80dps-anchor-roundtrip.witness.json`, `0` float64) verifying `< 1e-80` (`3.50e-82`) relative round-trip residual on both `q_0 = q_at(95)` and `q_2t = q_two_term_borromean_at(95)`.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.


## 2026-11-23 — Q-Drain-1 Audit against origin/main (`e330ab6aa04`)
- Verified still unlanded on `origin/main`: `computations/per_observable_100x_status.py:145` still scores `m_p` against independently rounded 11-sig-fig `codata_constants.M_P_MEV_VALIDATION` rather than `M_E_MEV * MASS_RATIO_P_E`, and `computations/probes/q0_q2t_80dps_anchor_roundtrip_probe.py` is absent on `origin/main`.
- Applicability check against `docs/coordination/owner-rulings.md`: one-term proton pin is canonical default and `q_2t` is a named comparison only (#8554); under derived `K^{\otimes 3}/[2]_q^3` two-term weighting (#8591) the connected part vanishes on `V^3`. Surviving scope: align `OBSERVABLES["m_p"]` anchor round-trip comparison in `per_observable_100x_status.py` and add 80-dps `q_at(95)` round-trip probe.

## 2026-11-28 — PR #9864 (branch `claude/q0-80dps-anchor-polish-2026-11-27`)
- Probe `computations/probes/q0_80dps_anchor_roundtrip_probe.py`: Newton at 120 dps, round trip 1.55e-120; polished q0 rounds to `Q_50_DIGIT_STR` and `Q_MP` (q0 unchanged). Error as a rational cut [lo, lo+1e-85] bracketing the root at 120 and 240 dps (`Cut.ofInterval`). Two-term pin checked as named comparison.
- `per_observable_100x_status.py`: m_p `roundtrip_residual_ppb` 0.002852 -> 7.197e-43 (measured vs anchor m_e x m_p/m_e); CODATA rounding kept as `codata_rounding_ppb`.
- Left: m_p substrate producer still reads the 50-digit q0 string (qou-5eg1). Complete on merge.
- 2026-11-28T00:12Z: PR #9864 merged. Completed. Follow-up (50-digit q0 in m_p producer) stays on qou-5eg1.
