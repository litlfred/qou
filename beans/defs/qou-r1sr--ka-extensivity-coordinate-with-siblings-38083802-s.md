---
# qou-r1sr
title: 'k(A) extensivity: coordinate with siblings #3808/#3802, scope b4-Ursell A=4 / deuteron alien-calculus wall (post gate-reversal)'
status: completed
type: task
priority: normal
created_at: 2026-07-17T20:38:37Z
updated_at: 2026-11-15T08:30:00Z
---


## 2026-11-15 — the magnitude lead does not survive the canonical traces (tracker #7735, item J)

Both perknot probes ran on typed nucleon traces `1.0653062 / 0.9232333`, which are the
retired convention-C traces (bean `qou-am5t`). Re-pointed at the owning witness
`atomic-tr-m-mpfr-50dps-proton.witness.json` (borromean word, convention D, proton pin:
`0.6293284022 / 0.4751335172`) and the live μ targets:

- `perknot_pn_bond_mayer_grounding_probe`: `(tr_p/tr_n)² = 1.7544` vs target `1.3671`,
  **+28.33 %**, the 5 % gate FAILS (was −2.61 % PASS). Fitted exponent 1.112 (was 2.184).
- `perknot_pn_bond_resolved_extensivity_probe`: no screened combo passes; best `sum:inv`
  −11.73 %; verdict LEAD → PRUNE (scope-(a)).

Gate not widened, nothing tuned. Still standing: the exact `(tr_p/tr_n)²` reduction
(`BondWeightIsospinSplit.lean`) and the sign. The magnitude claim is a scope-(a) negative.
