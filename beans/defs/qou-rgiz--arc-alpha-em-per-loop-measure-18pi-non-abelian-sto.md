---
# qou-rgiz
title: 'Arc: alpha_EM per-loop measure 1/(8pi) — non-abelian Stokes germ route (owner-gated on MOC/Phi, low program-value)'
status: todo
type: feature
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
created_at: 2026-08-29T16:24:57Z
updated_at: 2026-10-04T15:11:13Z
parent: qou-3l2l
blocked_by:
    - 08a2
    - qou-aemx
---

State 2026-08-29: 1/(8pi) OPEN/phase-4, owner-gated on MOC/Phi (=E(q) Gauss-Manin keystone, epic 08a2), proved not-derivable-from-abelian-model, multi-week. NOT a ranked L2 lever (last-correction -8.4ppm). New observation recorded (docs/audits/2026-08-29-alpha-em-measure-arc-workplan-update.md): F-construction=discrete q=i shadow (no germ, = the MOC obstruction); Yekutieli holonomy prod sigma_i(q)=germ by construction (the owner's non-abelian-Stokes steer). Retired: Chowla-Selberg (E=Bring/S4 proved non-CM), flat-torus Maxwell (qou-0rzk scrapped), abelian Hodge/Prym as primary. theta-graph qou-i7rk stays gated.

## 🔥 Roast (2026-09-03, qou-bsu0) — the per-term view

(i) Closing needs the per-loop measure 1/(8π) derived (phase-4, owner-gated on MOC/Φ, epic `08a2`) and the archimedean two-loop Δ₂ (weight 3, ζ(3)-type, c₂ ≈ 8.1e-4) computed; three classes stay unproved (`ArchimedeanLimit`, `BlochSuslinUniqueness`, `BringZeroModeBlochClass`).
(ii) Proved: no anchor-blind affine term absorbs the 78.84 ppb μ–p spread (`FormLadderAnchorDominance.no_anchor_blind_affine_correction_closes_gap`); the `[10]_q` linchpin δ_q(T_{3,5}) = q¹⁰ − q⁻¹⁰ is asserted, not derived (`qou-15sj`).
(iii) Trap: three rival constructions differ by 470 ppb (`qou-aemx`) and the smallest residual (+2.59 ppb, κ = 8q) is the PSLQ-ruled-out empirical one — never promote by residual; the L2 dashboard consumes the −467.6 ppb CS form, not the ladder the appendix states.
(iv) Next: adjudicate which construction is canonical (`qou-aemx`), then the germ route now that the EM holonomy germ is live (`2026-08-29-alpha-em-germ-viability-live.md`) — necessary, not sufficient.
(v) Forecast: stays `partial`; 0.313 ppb is 209× short of L2 and will not close by adding terms.
Tower status [reading: qou-ggdk]: MIXED — the ladder is order-by-order, truncated at cubic with Δ₂ uncomputed; `[2]_q(1 − h²α)` is fibre-level (Habiro); the CS resummation 1/(1 − δκ) is all-orders but κ is conjectural. No full-tower derivation of the measure exists.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
