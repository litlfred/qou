---
# 9fnm
title: 'c3^even measurement: Hoefsmit Stage-B order-u^3 extension (1jrh unblock)'
status: todo
type: task
created_at: 2026-07-03T06:15:43Z
updated_at: 2026-07-03T06:15:43Z
---


## Scoping (2026-07-03, from 2026-06-16-hoefsmit-stage-b-attempt-verdict.md)

- c2^even ≈ −8.006 source: computations/qbeta/qbeta_ck_sseries_operator_match_probe.py
  (net-route ladder, mp.taylor 60dps) — c3+ NOT trustworthy there (odd-order
  [s^odd] log R ~ 1e4 instability). Task = EXACT-RATIONAL Taylor.
- Exact object available: Delta(net)(q) = (q^14+2q^13-5q^12-10q^11+10q^10+24q^9
  -16q^8-32q^7+16q^6+24q^5-10q^4-10q^3+5q^2+2q-1)/(4q^7); E0 = 1/(q(q-1));
  numerator has (q-1) zero => finite at q=1, R(1)=1.
- Watch: u = b*hbar_q^2 is QUADRATIC in t=q-1 (sqrt-branch; do s-series, not
  u-reversion). cos(alpha_eff)/sqrt pieces: isolate to keep series rational or
  use exact algebraic extension.
- Then: Casoratian sign test W2 = c2^even*c3^odd − c3^even*c2^odd ≈ 16 + c3^even
  (per 2026-07-02-1jrh; threshold caveat near c3^even ≈ −16); W3 needs c4^even
  AND c4^odd (CAL-anchored tier caveat). AW positivity predicts W3/W2 > 0.
- Production guard: any c_k>=3 wiring needs owner approval + proton+muon
  cross-anchor test (registry §8).

## Implementation plan (2026-07-03, post-review scoping)

Predecessor read: computations/qbeta/qbeta_ck_sseries_operator_match_probe.py.
R(q) = Qb/[Q_A cos(alpha_eff)], Qb = |Delta(net)|*E0 (rational); alpha_eff =
(z-1)h/2 - u/2. All pieces analytic at s=q-1=0 with RATIONAL Taylor
coefficients (rational functions + log/cos/sqrt of rational-coefficient
series). Fix = hand-rolled truncated power-series arithmetic over Q
(lists of Fractions; mul/div/log/cos/sqrt), order ~s^20:
  1. reproduce c2^even (approx -8.006) exactly as gate;
  2. extract c3^even (and c4^even if the triangle stays stable);
  3. Casoratian sign test W2 ~ 16 + c3^even (per 2026-07-02-1jrh; sign call
     near -16 not decisive — report with rung error bars);
  4. tier everything; NO production wiring; owner gate for any c_k>=3 use.
New script: computations/qbeta/qbeta_ck_sseries_exact_rational.py.
