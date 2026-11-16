---
# qou-jlto
title: 'C (SUPPORT): explicit numerical pin — Hodge Gram from Braden-Northover τ₀·C vs Markov Gram on std block at q₀ (Hoefsmit); extract/falsify scale c'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:54:55Z
updated_at: 2026-11-16T17:58:00Z
parent: qou-3l2l
---


## 2026-07-24 — Option C Markov-side pin landed (PR #4168)
- (i) contravariant-form space nullity = 1 → scalar-commutant/Schur premise of #4160 CONFIRMED for the actual (4,1) block at q₀.
- (ii) unique invariant form symmetric + diagonal (seminormal Gram) → IsSymm premise confirmed.
- (iii) w_(4,1)(q₀) = d_q²/[5]_q! ≈ 0.128620 = Markov-side pin of c.
- OPEN remaining: Hodge-polarization normalization (Braden–Northover period matrix); c = markov_norm/hodge_norm. Also sub-piece (ii) S₅-equivariance of τ-image. No fabrication; 1/(8π) phase-4.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — On-`main` Verification & `Q-3L2L-1 = 1` Cross-Link (`litlfred/qou#8141`)

- **Verified on `main`:**
  - `folio/quantum-observable-universe/lean/QOU/Archimedean/TauS5EquivarianceReduction.lean` (landed in `15f0d73c8a`, `29f9a7462a`, moved to `folio/` in `114b24ba5b`, updated in `e389b33b05`), together with `folio/quantum-observable-universe/lean/QOU/Archimedean/CanonicalTitsIso.lean` and `folio/quantum-observable-universe/lean/QOU/Archimedean/PeriodMapWeightReduction.lean` (`0` `sorry`).
  - Probes & witnesses on `main`: `computations/alpha_em/alpha_em_b2_tau_id_c_pin_probe.py` (`computations/alpha_em/alpha-em-b2-tau-id-c-pin.witness.json`), `computations/alpha_em_b2_scalar_c_probe.py` (`computations/alpha-em-b2-scalar-c.witness.json`), `computations/alpha_em_b2_tits_deformation_probe.py` (`computations/alpha-em-b2-tits-deformation.witness.json`), `computations/alpha_em_b2_period_intertwiner_probe.py` (`computations/alpha-em-b2-period-intertwiner.witness.json`), and audit `docs/audits/2026-07-25-alpha-em-b2-tau-id-consolidation.md`.
- **Companion algebraic formalization (`qou-mxnu`, `qou-vbz4`):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` and `computations/alpha_em/std_block_hoefsmit_markov_schur_probe.py` (commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`, PR `https://github.com/litlfred/qou/pull/8141`) formalize the `SYT(4,1)` Hoefsmit diagonal Gram and the exact intertwiner transport $W^T M_S W = 10 \cdot \mathrm{diag}(1, 3/4, 2/3, 5/8)$ onto $M_S = 5 I_4 - J_4$.
- Kept at `status: in-progress` per owner governance.
