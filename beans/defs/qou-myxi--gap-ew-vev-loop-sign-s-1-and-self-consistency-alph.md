---
# qou-myxi
title: 'GAP: EW vev loop sign s=-1 and self-consistency alpha_loop = m_p/v are not derived'
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

## 2026-11-20 derivation attempt (branch claude/ew-vev-gaps-2026-11-20, commit 0966480389)

Neither slot is derived. The bean stays open. Lean: `QOU/StandardModel/ElectroweakVevGaps.lean`,
sorry-free. Audit: `docs/audits/2026-11-20-ew-vev-gaps.md` §3.

- **Sign: reduced.** The rule s = −sgn b₀ gives:
  - SM SU(2)_L: b₀ = −19/6 (`b0_su2_sm`), so s = −1 (`signRule_su2`);
  - abelian groups: b₀ > 0, so s = +1 (`signRule_abelian`), the EM sign.

  One rule covers both sectors once the vev loop is assigned to SU(2)_L (named field `sector_group`).
  The rule uses the sign of b₀ only, not its magnitude.
- **The coupling contradicts that reading.** An SU(2)_L loop carries α₂ = √2 G_F m_W²/π = 0.033914389.
  The self-consistency needs α_loop·N_v = 1, i.e. α_loop ≈ 0.00381. Both cannot hold
  (`su2_coupling_not_selfConsistent`). Values with κ = α₂ and the other slots as published:
  - κ = α₂: −9204.55 ppb (−35.8σ);
  - κ = α_em: −1092 ppb (−4.25σ);
  - κ = m_p/v: −29.4 ppb.
- **The data test the coupling only weakly.** The 1σ band admits κ ∈ [0.7533, 1.1961]·m_p/v
  (`loopShift_identity`), so the agreement places κ in range; it does not force κ = m_p/v.
- **Zero-mode rule (related): reduced.** Z = n_carriers·g(Σ₄)/Area gives both 2/(3π) (EM, n=2) and 1/π
  (EW, n=3). It is the unique genus-affine rule (`genusAffine_unique`). It was found by solving against
  the two corpus values, so it is a consistency result, not a derivation.

For the owner: assigning the vev loop to SU(2)_L fixes the sign and rules out α_loop = m_p/v. Keeping
α_loop = m_p/v leaves the sign with no rule.
