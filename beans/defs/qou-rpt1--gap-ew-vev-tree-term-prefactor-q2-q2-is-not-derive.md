---
# qou-rpt1
title: 'GAP: EW vev tree term prefactor q*[2]_q/2 is not derived (only [4][6][8] is carrier-reachable)'
status: todo
type: task
priority: normal
tags:
    - 8f-ew
created_at: 2026-11-20T17:51:02Z
updated_at: 2026-11-20T17:51:02Z
parent: qou-20sx
---

## What is open

The electroweak vev formula in `ElectroweakVevFixedPointClass`
(`QOU/StandardModel/ElectroweakBringSchwingerBridge.lean`) uses the tree term
`T_tree = q * ([2]_q/2) * [4]_q[6]_q[8]_q`.

- **Proved:** the product `[4][6][8]` is the sigma1*sigma3*sigma5 coefficient of the
  carrier word sigma1^4 sigma3^6 sigma5^8 up to a fixed scale:
  `a4 a6 a8 [2]^3 = h^3 [4][6][8]` (`carrier_coeff_product_qInt`,
  `QOU/StandardModel/ElectroweakVevFixedPointDecomposition.lean`, sorry-free).
- **Not derived:** the scale `q*[2]_q/2`. The carrier route gives `([2]/h)^3`. The
  "2-strand dressing" `[2]/2` is applied once, not once per carrier (`([2]/2)^3` misses by
  +4.2e4 sigma). It is also not applied to the 2-strand EM carrier T(2,9):
  `q([2]/2)[9][10] = 137.5687` vs 137.0360. The factor `q` is shared with the EM tree
  `q[9][10]`, whose own `[10]_q` is unverified (qou-15sj).

Dropping the dressing moves N_v by -5.41e6 ppb (-2.1e4 sigma). The 29 ppb agreement
depends on this choice.

## Next honest step

Find a categorical object (Markov trace at z_D of the carrier word, a Frobenius pairing,
or the joint idempotent traces of `prop:weak-spectral-completeness`) whose value is
`q([2]/2)[4][6][8]`, or record that none of these gives it. Do not choose the
dressing by matching v/m_p.

Audit: `docs/audits/2026-11-20-ew-vev-fixed-point-derivation.md`.
Probe: `computations/probes/ew_vev_fixed_point_slot_sensitivity_probe.py`.
