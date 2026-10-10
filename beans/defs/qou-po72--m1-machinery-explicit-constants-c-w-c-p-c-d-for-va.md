---
# qou-po72
title: 'M1 machinery: explicit constants C_W, C_P, C_D for Var(Sum c^2), Cov, linearized Var(SumD2)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T01:34:21Z
updated_at: 2026-10-04T15:13:15Z
parent: qou-m6dn
---

2026-08-29 (PR #5969): de-poissonized (CS) leading constants DERIVED in closed form.
  V_A = 8/(9 pi^2) [k>=2 frozen; NOT step-1's poissonized 8/pi^2], Var(omega3) lead 1/3,
  P = 8/(15 pi), rho_P = 2 sqrt(6)/5 EXACT (pi cancels: rho_P^2 = 24/25), V_D = 0.0415975
  (no elementary form found), margin m_inf = 0.300186 > 0 (reproduces #5901).
  Lean CSMarginCorrelationConstant.lean sorry-free (rhoSq=24/25 generic field; rho=2sqrt6/5 over R).
  OPEN tail: finite-n remainder constants C_A/C_D/C_P hit the Olver-Bessel wall (same as qou-tvok).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
