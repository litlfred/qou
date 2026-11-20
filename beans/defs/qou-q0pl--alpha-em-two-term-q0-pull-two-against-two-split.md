---
# qou-q0pl
title: 'alpha_em vs the two-term q0 re-pin: q0 determinations split two-against-two ({m_p 1-term, alpha_B} vs {m_p 2-term, m_mu})'
status: in-progress
type: task
priority: high
tags:
    - alpha-em
    - q0
    - two-term-qed
created_at: 2026-11-20T16:00:00Z
updated_at: 2026-11-20T16:00:00Z
parent: qou-3l2l
---

Owner question (Carl, 2026-11-20): why did the two-term make alpha worse?
Audit: docs/audits/2026-11-20-alpha-em-two-term-q0-pull.md. Probe:
computations/probes/alpha_em_two_term_q0_pull_probe.py (70 dps, 5/5). PR #8562.

Measured: form-B d ln(1/alpha)/d ln q = 6.833390293 (bare q[9][10]: 1 + 2.6296
+ 3.2144 = 6.8440; d ln[n]_q/d ln q = n coth(n lam) - coth(lam)). Two-term pin
+11.170941 ppb => form-B resid -0.36523 -> +75.97018 ppb (linear account exact
to 5e-6 ppb). q* (alpha = CODATA 2022): form B +0.0534 ppb from one-term pin
(2.38 sigma_q, sigma_q = 0.02243 ppb), -11.117 ppb from two-term (-495.7 sigma),
-11.561 from muon. Pairs: m_mu vs m_p two-term 0.443 ppb (0.36 sigma); alpha_B vs
m_p one-term 2.38 sigma. CS tower q* +68.1 ppb (sides with neither).
Muon relation would need delta_mu = -211.2058 ppb (diagnostic only; -9.09e-5
alpha/pi, -3.97e-3 alpha^2) — no corpus object found supplying it.

Open:
- Owner decision (also qou-aemx): which alpha functional is canonical. Form B
  and CS tower are DIFFERENT functions of q (8/(12 pi) const vs pi^2(98/45)
  [2]_q/2 hbar^2; agree 2.3e-4 at q0, factor 0.23/2.9 at q=1.05/1.2).
- Owner decision: keep #8554 two-term re-pin (selection-scoped term) vs one-term.
- np_two_term_qed_mup_tension_probe.py docstring calls the RULED-OUT
  45[3]_q(1+dCS+8q dCS^2) PSLQ form 'QOU derived'; 2026-11-18 audit quotes it.
- alpha_em_anchor_preference_probe.py docstring/witness source carry the
  CODATA-2018 '0.245 ppb' (form A); 2022 value is -0.145 ppb.
- Not formalised: monotonicity of the form-B root in q on q > 1.
