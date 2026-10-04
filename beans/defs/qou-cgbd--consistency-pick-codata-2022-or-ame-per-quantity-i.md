---
# qou-cgbd
title: 'CONSISTENCY: pick CODATA-2022 or AME per quantity in compute and stop mixing'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T06:53:56Z
updated_at: 2026-10-04T15:18:07Z
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
