---
# qou-hlx8
title: 'Does a bar-odd part of the ruled Q_beta trace carry the sinh role (pairing CAL-2 with CAL-3) under z_D?'
status: todo
type: task
priority: normal
tags:
    - qbeta
    - bar-involution
    - calibration
parent: qou-qs0e
created_at: 2026-11-15T09:50:00Z
updated_at: 2026-11-15T09:50:00Z
---

Owner decision D-W2 (relayed by coordinator session_01M5GA1LmsEf8tSMxFjMkmnn, 2026-11-15).
Origin: qou-hlx7, audit docs/audits/2026-11-15-one-sided-weak-vertex.md §4.

Question: the ruled cell (eps = Markov trace at z_D on nuc11_interleaved) has NO definite bar
parity. Does a bar-odd projection, e.g. f_odd(q) = (f(q) - f(1/q))/2, carry the "sinh partner"
role that pairs CAL-2 (D_beta) with CAL-3's cosh meson scale?

Measured so far (exact, sympy):
- f(q) = (q^2-1)(q^4+1) P12(q) / (4 q^7 (q^2+1)^2),
  P12 = 2q^12 - 6q^10 + 3q^8 - 6q^6 + 5q^4 - 5q^2 + 2. It carries the factor q*h, so f(1) = 0.
- even part = -h^2 [2]_q (q^2 + q^-2)/8 (nonzero); odd part = (q^2-1)(q^4+1) P'(q)/(8q^7(q^2+1)^2).
- Neither the retired Form A nor the retired z = 1 trace is bar-odd either (audit §4,
  corrected). So no Q_beta functional on record has ever been literally bar-odd.

🛑 ANTI-FIT RISK. Choosing a bar projection BECAUSE it restores the cosh/sinh pairing, or
because |f_odd| E_0 lands nearer CODATA, is selection against the target. Any projection
must be motivated structurally BEFORE its value is computed:
- the bar involution is the flavour flip (u <-> d letters, ud letter fixed; qou-hlx6/hlx7);
- Delta = n - p is a flavour difference.
The test is whether bar(Delta) is related to -Delta (or to the p <-> n swap) at the element
level. Measured: tr^{z_D(q)}(bar Delta) = f(1/q), so the trace intertwines bar with q -> 1/q,
but bar(Delta) != -Delta. A derivation must explain why the decay width would read only the
odd part. Report the value whatever it is.

Note also: the order-zero E_0 = m_e/(q(q-1)) is itself not bar-covariant, so "bar-odd Q_beta"
needs a statement of which factor carries the parity.
