---
# qou-xuc4
title: 'Probe: qbeta_dladder_ecalle_acceleration (Borel-Leroy + q-Borel + parity-split, estimator gate)'
status: scrapped
type: task
created_at: 2026-07-17T15:03:41Z
updated_at: 2026-08-14T19:46:00Z
---

**Consolidated into `qou-dri7` and scrapped 2026-08-14.** Body was empty from
creation.

This was the *probe* form of the same item as `qou-dri7` and `qou-b00b` —
Borel–Leroy + q-Borel acceleration of the bar-odd D-ladder. The probe was never
written, which is fortunate: it would have been a resummation probe against a
series that does not diverge.

**Reason for the scrap:** the D-ladder was proved **convergent** on 2026-08-09
([`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](../docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md),
`ρ = 0.142799996644689…`, `κ = 0`). Borel–Leroy summation assigns a value to a
divergent asymptotic series; here the series already converges on `|w| < ρ`, and
KC22 supplies the closed form `D(w) = φ(w)log(1−w/ρ) + ψ(w)` and the asymptotic
`d_k = −(1/(2h*_ρ))ρ^{−k}/k(1+O(1/k))` with no free parameters — which is what
the "estimator gate" in the title was to have measured.

Full reasoning, the scope-(a) caveat, and the contrast with the still-live
`qou-vkg5`: see `qou-dri7`.
