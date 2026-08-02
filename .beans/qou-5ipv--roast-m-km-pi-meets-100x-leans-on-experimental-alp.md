---
# qou-5ipv
title: 'ROAST: m_K/m_pi ''meets 100x'' leans on experimental alpha_em (derived alpha_em=609 -> 157000 ppb miss); EM factor full-log fits WORSE than the 2-term truncation — re-scope claim'
status: todo
type: task
created_at: 2026-08-02T16:03:25Z
updated_at: 2026-08-02T16:03:25Z
---

See docs/audits/2026-08-02-ppq-attack-vectors-roast.md §Roast 1.
m_K^2/m_pi^2 = [3]_q[4]_q + (alpha_em/pi)(3q^2-1)/(2q^2). Findings:
- Core [3]_q[4]_q exact/Lean-proved (~99.98%). EM term ~203 ppm.
- alpha_em=137.035944 HARDCODED (experimental). Derived alpha_em (q[9][10], ~1/609)
  gives -157000 ppb miss => "meets 100x" imports the measured alpha_em, not parameter-free.
- (3q^2-1)/(2q^2) is a 2-term truncation of 1+log(1+hbar_q); the FULL log fits WORSE
  (+103 vs +47 ppb) => the "truncated-log/3-generations" justification is numerology.
- Residual structure-dominated (137.035944 vs CODATA 137.035999 barely moves it).
Action: re-scope the corpus claim (alpha_em-anchored, not parameter-free); a genuine
ppq m_K/m_pi needs a DERIVED alpha_em (bean qou-5et6) + derived EM factor.
