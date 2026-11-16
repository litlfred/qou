---
# qou-5ipv
title: 'ROAST: m_K/m_pi ''meets 100x'' leans on experimental alpha_em (derived alpha_em=609 -> 157000 ppb miss); EM factor full-log fits WORSE than the 2-term truncation — re-scope claim'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T16:03:25Z
updated_at: 2026-11-16T19:56:51Z
parent: qou-3l2l
---

See docs/audits/2026-08-02-ppq-attack-vectors-roast.md §Roast 1.
m_K^2/m_pi^2 = [3]_q[4]_q + (alpha_em/pi)(3q^2-1)/(2q^2). Findings:
- Core [3]_q[4]_q exact/Lean-proved (~99.98%). EM term ~203 ppm.
- alpha_em=137.035944 HARDCODED (experimental). Derived alpha_em (q[9][10] = 136.82, -1553 ppm from CODATA) degrades m_K/m_pi
  from ~47 to ~363 ppb (~8x) => "meets 100x" imports the measured alpha_em (dependence
  real but ~8x, not catastrophic). [CORRECTION: earlier '609/157000 ppb' used wrong
  hbar^2 numerator vs (q-q^-1)^2; corrected per alpha_EM per-loop agent 2026-08-02.]
- (3q^2-1)/(2q^2) is a 2-term truncation of 1+log(1+hbar_q); the FULL log fits WORSE
  (+103 vs +47 ppb) => the "truncated-log/3-generations" justification is numerology.
- Residual structure-dominated (137.035944 vs CODATA 137.035999 barely moves it).
Action: re-scope the corpus claim (alpha_em-anchored, not parameter-free); a genuine
ppq m_K/m_pi needs a DERIVED alpha_em (bean qou-5et6) + derived EM factor.

## Round 50 Formalization & 50-dps Witness (PR #8177)
- **Lean 4 Module (`0 sorry`, `0 axiom`, `0 vacuity`):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/ChernSimonsTowerAndT35Linchpin.lean`
  - `mK_mPi_em_coupling_difference`: exact factored identity $R(\alpha_1) - R(\alpha_2) = (2 - r_0)\,T(q)\,(\alpha_1 - \alpha_2)$ isolating the $+157.97\text{ ppb}$ shift ($+5564.9\text{ ppm}$ vs PDG vs $+5406.0\text{ ppm}$ with experimental $\alpha_{\mathrm{em}}$) when bare $q[9]_q[10]_q = 609.0079...$ replaces experimental $\alpha_{\mathrm{em}}^{-1} = 137.035999177$.
  - `trunc_exceeds_log_cubic_bound`: $(1+x) - \bigl(1 + (x - x^2/2 + x^3/3)\bigr) = x^2(3 - 2x)/6 > 0$ for $0 < x < 3/2$, proving the 2-term linear truncation $(3q^2-1)/(2q^2) = 1+x$ strictly exceeds the logarithmic series at $x = (q^2-1)/(2q^2) \approx 0.14579$ by $+1.0086\%$, so replacing the linear truncation by $1 + \ln((q^2+1)/(2q^2))$ worsens the PDG residual from $+5406.0\text{ ppm}$ to $-4696.3\text{ ppm}$.
- **50-dps Witness:** `computations/probes/round50-zeta4-bridge-and-alpha-em-cs-tower.witness.json` (`scriptHash: e7bf4a93b887`, `scriptCommitSha: cf283b8e199f4643fb9e0259ec0a2702096bdd9b`).
- **PR:** `litlfred/qou#8177` (`https://github.com/litlfred/qou/pull/8177`, head SHA `3fdbeeb87a6b1821ff8d57a95f95d4d20cf72628`).
- **Status:** Kept at `status: in-progress` per reviewer-separated closure discipline.
