---
# i5p0
title: 'xi_ell(q) Path A: per-braid Phi_q tower ratio m(mu)/m(e) at q0 — does full tower reproduce 206.77 w/o scalar?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-30T18:27:40Z
updated_at: 2026-11-16T19:04:00Z
parent: qou-2002
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-06-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Resolution (2026-11-16, PR [`litlfred/qou#8158`](https://github.com/litlfred/qou/pull/8158), commit `75b6b451ceab7004d7b1dbd5350d3c71eff04c1c`)

- **Verdict: NO (scope-(b) falsification of Path A without an asymmetric $\hbar_q^{-2}$ grading).**
- Measured in `computations/xi_ell_phi_q_probe.py` (`computations/xi-ell-phi-q-probe.witness.json`) and verified in `computations/probes/substrate_parameter_locality_varying_constants_probe.py`:
  - Additive $\log \Phi_q$ tower gives `1.847` on `muon T(2,5) / electron T(2,3)` and `10.637` on `muon 4_1 / electron T(2,3)` (vs CODATA `206.7683`) because the $1/\hbar_q$ enhancement in $\log \Phi_q(z) \sim \mathrm{Li}_2(z)/\hbar_q$ multiplies both numerator and denominator and cancels in the ratio (`homogeneous_hbar_scaling_cancels` in `QOU/Observations/SubstrateParameterLocality.lean`, `0` `sorry`).
  - Direct $\Phi_q$ tower gives `13.990` on $T(2,5)/T(2,3)$ and `124,860.88` on $4_1/T(2,3)$ (and `9.978` / `13,207.14` when rescaled by $1/q_0$).
  - Hence the `206.77` scale separation requires an asymmetric $\hbar_q^{-2}$ grading between the hyperbolic $4_1$ ($\mathrm{Vol}(4_1) > 0$) and torus-knot $T(2,3)$ ($\mathrm{Vol}_{\mathrm{hyp}} = 0$).
