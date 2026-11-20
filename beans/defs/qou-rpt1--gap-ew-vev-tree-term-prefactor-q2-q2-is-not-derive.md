---
# qou-rpt1
title: 'GAP: EW vev tree term prefactor q*[2]_q/2 is not derived (only [4][6][8] is carrier-reachable)'
status: todo
type: task
priority: normal
tags:
    - 8f-ew
created_at: 2026-11-20T17:51:02Z
updated_at: 2026-11-20T20:10:00Z
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

## 2026-11-20 derivation attempt (branch claude/ew-vev-gaps-2026-11-20, commit 0966480389)

Not derived. The bean stays open. Lean: `QOU/StandardModel/ElectroweakVevGaps.lean`, sorry-free.
Audit: `docs/audits/2026-11-20-ew-vev-gaps.md` §1.

- **Factor q (scope b, bar invariant).** `ewTreeF_bar`: T(1/q)·q² = T(q). `ewTreeF_bar_invariant_imp`:
  T bar-invariant implies q²=1. So q cannot come from quantum integers or quantum dimensions.
  It needs a bar-breaking source (framing, z_D). None found. The EM tree q[9][10] has the same
  factor (`emTreeF_bar`), so this is one item shared by both sectors.
- **Exponent k on [2]/2.** T_k is strictly increasing in k (`treeK_strictMono`). Two rules were found:
  - the EM rule q·∏[n_i] forces k=0: N_v = 260.997870278523, −5.41e6 ppb, −2.1e4σ;
  - one [2]/2 per extra link component forces k=3: +1.09e7 ppb, +4.2e4σ.
  No rule gives k=1 (the published value).
- **Markov trace, conv-D, carrier word** (asked for above): ∏(b_n + a_n z_D) = 3.70244669186027,
  against 262.10 needed. Scope (a).

Remaining hypothesis: `EwVevReducedHypotheses.dressing_exponent : k = 1`, plus the shared q.
