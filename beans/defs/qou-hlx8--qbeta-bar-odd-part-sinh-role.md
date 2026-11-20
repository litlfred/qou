---
# qou-hlx8
title: Does a bar-odd part of the ruled Q_beta trace carry the sinh role (pairing CAL-2 with CAL-3) under z_D?
status: todo
type: task
priority: normal
tags:
    - qbeta
    - bar-involution
    - calibration
created_at: 2026-11-15T09:50:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-qs0e
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


## 2026-11-15 gap-routes sibling (session_01Qmmkt8pE46F2YNM5QTVpHa)
Route-4 derived: tr_z intertwines bar with q->1/q iff z(q)-z(1/q)=h (z_D yes, z_C no). Exactly f = h*g, so f_odd = h*g_even and f_even = h*g_odd with g_odd = -h[2]_q(q^2+q^-2)/8. f_odd(q0)*E0 = 0.556939460557 MeV (-28.811 %), reported, not proposed. Audit docs/audits/2026-11-15-bar-parity-split-gap-routes.md. Stays todo: the conjecture is open (qou-2djn, qou-z08b).

## 2026-11-15 the motivating premise is contested (weak-vertex thread)
The structural motivation above, "the bar involution is the flavour flip", is exactly the reading
qou-hlxt flags as contested. PR #7952 found that two of three corpus sources (the Breit–Wheeler block and
the colour-tube sign rule) read σ⁻¹ as the antiparticle contact, not as d. PR #7960 adds that the bar flip
is the only letter map preserving the D trace exactly (z_D is bar-fixed, n = 2, 3, 4). So a bar-odd
projection of the ruled cell has no settled flavour meaning until hlxt is decided. No value is proposed.
Status stays todo.

## Progress (PR #8457)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PairingSpaceActionRetypeRuledOddProjectionLetterInvolutionPullbackQuotientKernelMultiplierSlope.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_h0ou_hlx8_hlxp_i9gk_slpd_probe.witness.json` (`Commit 1` = `6615e05829d98e7dc8f3151a6136022620b0fa75`, `HEAD` = `87f824354a46b08a4af8436ed872967b2f3dfc59`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8457, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
