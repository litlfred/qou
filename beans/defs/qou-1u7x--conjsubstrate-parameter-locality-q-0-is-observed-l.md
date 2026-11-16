---
# qou-1u7x
title: conj:substrate-parameter-locality — q_0 is observed-local (not derived); state d log(O_i)/d log q_0 co-variation as the falsifiable varying-constants signature (Webb alpha / quasar mu bounds). NOT yet in corpus.
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T11:30:59Z
updated_at: 2026-11-16T19:04:00Z
parent: qou-2002
---

## Resolution (2026-11-16, PR [`litlfred/qou#8158`](https://github.com/litlfred/qou/pull/8158), commit `75b6b451ceab7004d7b1dbd5350d3c71eff04c1c`)

- Formalised in Lean 4 at `folio/quantum-observable-universe/lean/QOU/Observations/SubstrateParameterLocality.lean` (wired into `QOU.lean`, `0` `sorry`):
  - `kappaMu_eq_neg_two_cq`: $\kappa_\mu(q) = \frac{d\ln(\hbar_q^{-2})}{d\ln q} = -\frac{2}{q - 1} = -2\,c_q(q)$.
  - `linear_response_covariation_eliminates_dq`: any local perturbation $\delta\ln q_0(x)$ cancels out of $\frac{\delta\ln\mathcal{O}_1}{\delta\ln\mathcal{O}_2} = \frac{\kappa_1(q_0)}{\kappa_2(q_0)}$.
  - `covariation_ratio_alpha3`, `covariation_ratio_alpha2`, and `covariation_ratio_alpha2_pos_of_gt_one`: closed-form co-variation slopes $R_{\mu/\alpha}^{[3]}(q) = \frac{q^2 + 1 + q^{-2}}{(q - 1)(q^2 - q^{-2})}$ and $R_{\mu/\alpha}^{[2]}(q) = \frac{2(q + q^{-1})}{(q - 1)(q - q^{-1})} > 0$ for $q > 1$.
- Verified at 50 dps in `computations/probes/substrate_parameter_locality_varying_constants_probe.py` (+ witness `computations/probes/substrate-parameter-locality-varying-constants-probe.witness.json`):
  - At $q_0$: $\kappa_\mu(q_0) = -18.1853589123\dots$, $\kappa_\alpha^{[3]}(q_0) = -0.276241313056\dots$, $\kappa_\alpha^{[2]}(q_0) = -0.103963709937\dots$, giving $R_{\mu/\alpha}^{[3]}(q_0) = +65.8314236604\dots$ and $R_{\mu/\alpha}^{[2]}(q_0) = +174.920257301\dots$ (with quasar $|\Delta\mu/\mu| < 10^{-7}$ bounding $|\delta q_0 / q_0| < 5.4989 \times 10^{-9}$ and $|\Delta\alpha/\alpha| < 1.519 \times 10^{-9}$).

