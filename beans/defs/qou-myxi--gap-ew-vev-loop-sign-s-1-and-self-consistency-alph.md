---
# qou-myxi
title: 'GAP: EW vev loop sign s=-1 and self-consistency alpha_loop = m_p/v are not derived'
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

The EW fixed point `1/a = T - a H (1 - hbar^2 a)` differs from the EM relation
`1/a = T + a H (1 - h^2 a)` (`EmCouplingBringZeroMode`) in three discrete slots.

1. **Sign s = -1.** `loop_sign_both_imp` (sorry-free) shows the two signs are
   incompatible unless c*a = 1. Transcribing the EM sign gives N_v = 262.41877855,
   **+2294 ppb (+8.9 sigma)**. The published value is -29 ppb. The only justification
   on record is the label "anti-screening" in `BringSchwingerNormalizationDerivation`.
2. **c = hbar_q^2 vs the corpus-derived h^2** (`hecke_skein_bar_contraction`).
   Numerically inert (0.15 ppb). Exemption-2 candidate to align with the corpus, but
   that is an owner call.
3. **Self-consistency a_loop = 1/N_v = m_p/v.** In EM, a is the coupling being looped.
   In the EW sector, m_p/v is not a gauge coupling (alpha_W ~ 1/30), and no mechanism is
   stated.

Proved: given the relation, the root is unique in (0, 2/T)
(`ewShapeCubic_existsUnique_root`, `ew_vev_unique_in_window`).

Zero-mode counting rule (related): `no_single_zero_mode_rule` shows that the EM rule
(surface b1) and the EW rule (carrier Seifert genera) are different rules. Each fails in
the other sector.

Audit: `docs/audits/2026-11-20-ew-vev-fixed-point-derivation.md`.
