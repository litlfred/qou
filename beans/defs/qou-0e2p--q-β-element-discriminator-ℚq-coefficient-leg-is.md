---
# qou-0e2p
title: 'Q_β element discriminator, ℚ(q)-coefficient leg: is Δ_L bar-odd under ANY ℚ(q)-linear combination of the admissible traces; fix codata_constants.Q_BETA_MEV 8-sig-fig truncation (continues qou-99qc / #7118)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:26:20Z
updated_at: 2026-10-04T15:13:36Z
parent: qou-avtq
---

Continues qou-99qc / #7118 (branch claude/qbeta-bar-odd-element-discriminator-2026-09-07). Landed there: Δ_S bar-odd under every admissible trace in the 2-dim span; Δ_L bar-odd only under the zero trace (defects non-proportional, ratio (q²+1)²/(q⁴+1)). Open leg: ℚ(q)-linear coefficients — bar acts on coefficients, so a·A + b·B with a,b ∈ ℚ(q) is a functional equation in two unknowns; scaling by f(q) rescales Q_β so it is a different physical claim — state that. Also #7115 (augmentation IS a Markov trace; D7 decides ε). Second, cheap item: codata_constants.Q_BETA_MEV = 0.78233341 is 8 sig figs against the witness's 0.7823334093099085 — fix at the registry with the CODATA 2022 value + uncertainty, drain consumers.


---

**2026-09-08 — both halves measured; the second half's premise was wrong.**

*Leg 1, ℚ(q) coefficients* — `qbeta_bar_odd_qq_coefficient_leg_probe.py` (24/24, exact). With `F = ℚ(q+1/q)` the bar-fixed field, `S(Δ) = {(a,b) ∈ ℚ(q)²: bar(aA+bB) = −(aA+bB)}` is an `F`-space of dimension 3 for BOTH elements — over ℚ(q) the criterion is VACUOUS (`(h/A, 0)` always works). Restricted to bar-even coefficients (`a, b ∈ F`): Δ_S all of F², Δ_L exactly ONE line `(a:b) = (B_e:−A_e)`, `A_e/B_e = (q²+1)²/(q⁴+1)`, q-dependent. Restricted to ℚ: reproduces #7118. The unique normalised bar-odd functional on Δ_L over F is `a = −(q⁴+1)/(2q²)`, `b = (q²+1)²/(2q²)`, a mixture with `ab ≠ 0`, and the Markov property at two levels forces `ab(q−z_D)² = 0` — so it is NOT a Markov trace (Option-G territory). Readout, diagnostic only: `Q_β = 0.22356 MeV`, −71.42 % vs AME. Audit: `docs/audits/2026-09-08-qbeta-bar-odd-qq-coefficient-leg.md`.

*Leg 2, "Q_BETA_MEV 8-sig-fig truncation"* — **the premise (#7118 §5) was inverted.** `Q_BETA_MEV = 0.78233341(61)` is σ-limited (AME quotes to σ/6), not truncated. The witness's reference `0.7823334093099085` is `qou_substrate.constants.Q_NEUTRON_MEV`, a float64 `M_N − M_P − M_E` whose `M_N = 939.56542179` is the AME-derived sum rounded to 8 decimals (drops 0.69e-9 MeV = the whole 8.8e-10). So the precision defect is the float path in `qou_substrate.constants` (M_N_MEV, M_P_MEV, M_E_MEV, Q_NEUTRON_MEV are all `float`) — exemption-1 fix, that module's arc, NOT done here. What the registry does offer is `Q_β = 1.29333251(38) − m_e = 0.78233355931(38)` (CODATA 2022 `m_n−m_p`): +191 ppb, 0.2σ — a DATASET choice, 116 consumer files, `Δc₃ ≈ +0.309` (15 %) through 1/u³. Put to the owner (audit §5, six-part frame, recommendation = registry). Stale docstrings on `Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT` / `_FROM_AME` (CODATA-2018-proton figures) corrected in `codata_2022_source.py`; no number moved.

Still open (owner): the CAL-3 dataset decision. Still open (mechanical, other arc): `qou_substrate.constants` float64 constants.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
