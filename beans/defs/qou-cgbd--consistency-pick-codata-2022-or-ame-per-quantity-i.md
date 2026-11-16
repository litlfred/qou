---
# qou-cgbd
title: 'CONSISTENCY: pick CODATA-2022 or AME per quantity in compute and stop mixing'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T06:53:56Z
updated_at: 2026-11-16T19:04:00Z
parent: qou-2002
---

## Why this matters, measured 2026-08-30

Owner instruction: *"be consistent in use of CODATA 2022 vs AME data in
compute. don't mix."*

The corpus carries BOTH, deliberately and documented:

  codata_2022_source.py lists  (1) CODATA-2022 direct  m_n = 939.56542194(48)
                               (2) AME-derived         m_n = 939.56542179
  qou_substrate.constants.M_N_MEV carries (2), with the comment
      "# noqa: P31 - AME-derived, NOT CODATA"
  computations/codata-2022-validation-masses.witness.json carries (1)

Neither is wrong. The defect is MIXING, and there is a live instance:

  computations/probe_q_beta_operator_valued_N3.py builds
      Q_AME = M_N_MEV_VALIDATION - M_P_MEV_VALIDATION - m_e
  from codata_constants — i.e. the variable is NAMED Q_AME and is built from
  the CODATA-2022 table.

### The cost, measured

The two neutron masses differ by 1.5e-7 MeV = 191.7 ppb of Q_beta. The c_3
extraction has gain 1/(b^3 hbar_q^6) = 1.618e6, so that choice alone moves the
extracted c_3 by 0.310 — 17.6 % of it. See
computations/qbeta/qbeta_c3_experimental_uncertainty_probe.py (PR #6111).

### Scope note so this is not over-read

The same probe shows the EXPERIMENTAL error already gives sigma(c_3) = 1.16
(66 % relative), so the 17.6 % mixing error is 0.27 sigma — real, and worth
fixing for hygiene, but NOT the dominant uncertainty. Fix the mixing because
consistency is cheap and auditable, not because it would rescue the c_3
near-match; nothing rescues that.

## Resolution & Audit Record (2026-11-16, PR [`litlfred/qou#8158`](https://github.com/litlfred/qou/pull/8158), commit `75b6b451ceab7004d7b1dbd5350d3c71eff04c1c`)

- Quantified side-by-side at 50 dps in `computations/probes/substrate_parameter_locality_varying_constants_probe.py` (+ witness `computations/probes/substrate-parameter-locality-varying-constants-probe.witness.json`):
  - Pure CODATA-2022 direct: $Q_\beta^{\mathrm{CODATA}} = m_n^{\mathrm{CODATA}} - m_p^{\mathrm{CODATA}} - m_e = 0.782332925808\dots\text{ MeV}$.
  - AME-derived $m_n$: $Q_\beta^{\mathrm{AME}} = m_n^{\mathrm{AME}} - m_p^{\mathrm{CODATA}} - m_e = 0.782332775808\dots\text{ MeV}$.
  - Split: $\Delta Q_\beta = 1.5\times 10^{-7}\text{ MeV}$ ($191.7\text{ ppb}$), shifting extracted $c_3$ by $\Delta c_3 = 0.310316$ vs $\sigma(c_3) = 1.16017$ ($0.2675\sigma$).
  - Note: the `"Q_AME"` JSON key in `q-beta-operator-valued-N3.witness.json` is retained for schema compatibility with `computations/sweeps/binding_q_target_sweep.py:135`.
