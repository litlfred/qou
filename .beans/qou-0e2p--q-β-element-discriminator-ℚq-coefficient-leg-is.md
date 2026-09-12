---
# qou-0e2p
title: 'Q_β element discriminator, ℚ(q)-coefficient leg: is Δ_L bar-odd under ANY ℚ(q)-linear combination of the admissible traces; fix codata_constants.Q_BETA_MEV 8-sig-fig truncation (continues qou-99qc / #7118)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T18:26:20Z
updated_at: 2026-09-12T00:00:00Z
parent: qou-vyvt
---

Continues qou-99qc / #7118 (branch claude/qbeta-bar-odd-element-discriminator-2026-09-07). Landed there: Δ_S bar-odd under every admissible trace in the 2-dim span; Δ_L bar-odd only under the zero trace (defects non-proportional, ratio (q²+1)²/(q⁴+1)). Open leg: ℚ(q)-linear coefficients — bar acts on coefficients, so a·A + b·B with a,b ∈ ℚ(q) is a functional equation in two unknowns; scaling by f(q) rescales Q_β so it is a different physical claim — state that. Also #7115 (augmentation IS a Markov trace; D7 decides ε). Second, cheap item: codata_constants.Q_BETA_MEV = 0.78233341 is 8 sig figs against the witness's 0.7823334093099085 — fix at the registry with the CODATA 2022 value + uncertainty, drain consumers.


---

**2026-09-08 — both halves measured; the second half's premise was wrong.**

*Leg 1, ℚ(q) coefficients* — `qbeta_bar_odd_qq_coefficient_leg_probe.py` (24/24, exact). With `F = ℚ(q+1/q)` the bar-fixed field, `S(Δ) = {(a,b) ∈ ℚ(q)²: bar(aA+bB) = −(aA+bB)}` is an `F`-space of dimension 3 for BOTH elements — over ℚ(q) the criterion is VACUOUS (`(h/A, 0)` always works). Restricted to bar-even coefficients (`a, b ∈ F`): Δ_S all of F², Δ_L exactly ONE line `(a:b) = (B_e:−A_e)`, `A_e/B_e = (q²+1)²/(q⁴+1)`, q-dependent. Restricted to ℚ: reproduces #7118. The unique normalised bar-odd functional on Δ_L over F is `a = −(q⁴+1)/(2q²)`, `b = (q²+1)²/(2q²)`, a mixture with `ab ≠ 0`, and the Markov property at two levels forces `ab(q−z_D)² = 0` — so it is NOT a Markov trace (Option-G territory). Readout, diagnostic only: `Q_β = 0.22356 MeV`, −71.42 % vs AME. Audit: `docs/audits/2026-09-08-qbeta-bar-odd-qq-coefficient-leg.md`.

*Leg 2, "Q_BETA_MEV 8-sig-fig truncation"* — **the premise (#7118 §5) was inverted.** `Q_BETA_MEV = 0.78233341(61)` is σ-limited (AME quotes to σ/6), not truncated. The witness's reference `0.7823334093099085` is `qou_substrate.constants.Q_NEUTRON_MEV`, a float64 `M_N − M_P − M_E` whose `M_N = 939.56542179` is the AME-derived sum rounded to 8 decimals (drops 0.69e-9 MeV = the whole 8.8e-10). So the precision defect is the float path in `qou_substrate.constants` (M_N_MEV, M_P_MEV, M_E_MEV, Q_NEUTRON_MEV are all `float`) — exemption-1 fix, that module's arc, NOT done here. What the registry does offer is `Q_β = 1.29333251(38) − m_e = 0.78233355931(38)` (CODATA 2022 `m_n−m_p`): +191 ppb, 0.2σ — a DATASET choice, 116 consumer files, `Δc₃ ≈ +0.309` (15 %) through 1/u³. Put to the owner (audit §5, six-part frame, recommendation = registry). Stale docstrings on `Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT` / `_FROM_AME` (CODATA-2018-proton figures) corrected in `codata_2022_source.py`; no number moved.

Still open (owner): the CAL-3 dataset decision. Still open (mechanical, other arc): `qou_substrate.constants` float64 constants.

---

**2026-09-12 — the dataset decision is STAGED and fully measured (PR #7205, branch `claude/qbeta-dataset-codata-registry-2026-09-12`). NOT merged; the decision remains the owner's.**

*Label first.* This bean and the audit both say "CAL-3". **Q_β is the CAL-2 proxy** (`Q_β = ℏ/𝔇_β`); CAL-3 is `𝔇_π` with proxy `m_π` (AGENTS.md canonical table; owner ruling 2026-06-26). Corrected in the producer — `calibration_id` has two writers and zero readers, so no consumer moved. The witness stem `cal-3-q-beta` is deliberately NOT renamed.

*Blast radius — the 116 was low.* Measured `git grep -l -e Q_BETA_MEV -e cal-3-q-beta` = **187 tracked files**. AST-classified: **120 live `.py` consumers** (of 125 matching; 5 mention-only), **28 `.json`** referencing the symbol or stem, but **126 `.json` carrying a `0.7823334…` literal**, and **27 `.md`** of which 19 are dated `docs/audits` + `docs/coordination` records left alone per the `qou-3nva` precedent. The 126-witness drain is **not** attempted here and should not be.

*Route.* Derived from `M_N_MINUS_P_MEV − M_E_MEV`, not `m_n − m_p − m_e`, so it never touches the proton that the 2026-08-09 vintage-straddle audit found stale. The producer asserts the two routes agree (7.4e-17) and **refuses** rather than pick one if they ever diverge.

*🛑 The direction in the §5 framing is BACKWARDS, and I repeated it before catching it.* Under the registry the L2 `Q_β` miss goes **164.0× → 223.9× — WORSE**, not 139.5×/closer. 139.5× holds the 100× target at the AME σ; the dashboard scores each determination against 1/100 of **its own** σ, and the registry is the *more precise* determination (3.8e-7 vs 6.1e-7), so its target tightens ~1.6× — faster than the residual improves. Two defensible normalisations, opposite signs. Under §NO FITTING neither may pick the dataset, but the improving one is both inadmissible **and** false.

*Measured deltas* (convention C, proton pin): `c_3` −2.0693425771 → −1.7604548585 (−14.93 %); the `c_3 ≈ −2 = J_Hopf(q=1)` near-match **degrades** 3.4671 % → 11.9773 %. Exactly one L2 row moves; headline unchanged at **1/6 scoreable** (0/6 unconditional). L1 substantively identical — neither leg regresses.

*A cost §5 did not name.* `codata_constants`'s `Q_β` vs `m_n − m_p − m_e` check was a real if weak cross-dataset comparison (1.4931e-7 MeV, 190.85 ppb, 0.22 σ). Under the registry both sides are the same quantity, so it is **0 by construction** (7.4e-17). Recorded in-witness as `consistency_check_is_now_circular`; it should be re-pointed at the retained `Q_beta_n_MeV_ame2020` or retired.

*The second open item on this bean is CLOSED* (exemption 1, separate commit `b276ed94b1b`): `qou_substrate.constants` float64. `CodataEntry.value` is **already `mpf`**, so `float(...)` was an active downcast, and `Q_NEUTRON_MEV` ran in binary64 across a catastrophic cancellation — **9.15e-14 MeV = 1.17e-4 ppb = 117× the L1 1-ppQ target**, now 4.24e-59. Public float types unchanged (309 importers); `_STR` companions added per this file's own `MASS_RATIO_P_E_STR` convention. **Correction: `q_at()` returns `mpf`, not float64** — what is float64 is the module constant `Q`, deliberately (`_solve_q_proton_f64`), with `q_at()` / `Q_50_DIGIT_STR` documented beside it as the precise paths; left alone, since retyping it is a public API break and not exemption 1.

**Still open (owner): the dataset decision itself. Nothing is enacted on `main`.**
