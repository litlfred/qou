---
# qou-wf2v
title: 'canonical-scale-ratio: normalization-independent restatement of 25=deg^2 — outcome (iii) recorded; conditional theta_5 restatement + matching condition; Hodge pin blocked on Riera-Rodriguez Z'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T13:41:58Z
updated_at: 2026-11-16T17:58:00Z
parent: qou-wp3h
---


Status 2026-07-25 (branch claude/alpha-em-canonical-scale-ratio-2026-07-25):
OUTCOME (iii) — the restatement cannot be made fully normalization-free.
- K1: three-scale gauge group (Markov λ, Hodge μ, intertwiner s² — Lean
  invariantForm_pullback_smul); two canonical pins never suffice.
- K2: surviving CONDITIONAL restatement: θ₅ = frac(log₅(c·8π)) = 0 under
  hypothesis H₅ (5-power-graded gauges); measured θ₅ = −6.85e-6, k = 2.
- K3: H₅'s Markov leg FAILS for declared pins (y_λ / w_Wedderburn /
  cellular [4]_{q²}! mutually inequivalent mod 5^ℤ; trace pins
  module-scale-blind).
- K4: 25 does not survive any declared pin (scope-(a), per-pin rows).
- K5: matching condition frac(log₅(μ_H·s²)) = frac(log₅ λ_M) recorded.
- K6: Hodge canonical pin blocked — Riera–Rodríguez Z absent; non-CM
  Néron periods; 50a minimal models not corpus data.
Deliverables: probe + witness (8/8), audit
docs/audits/2026-07-25-alpha-em-b2-canonical-scale-ratio.md, ledger row.
LEFT OPEN (do not close): the deg²=25 observation itself (owner-level,
double-gated); the cellular pin's two unverified convention legs; the
Hodge-side canonical evaluation (needs Z).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — On-`main` Verification & `Q-3L2L-1 = 1` Cross-Link (`litlfred/qou#8141`)

- **Verified on `main`:**
  - Audit `docs/audits/2026-07-25-alpha-em-b2-canonical-scale-ratio.md` (landed in `6e83109287`), probe `computations/alpha_em/alpha_em_b2_canonical_scale_ratio_probe.py`, witness `computations/alpha_em/alpha-em-b2-canonical-scale-ratio.witness.json` (8/8 PASS at 50 dps), and Lean module `folio/quantum-observable-universe/lean/QOU/Archimedean/GaugeGroupThreeScale.lean` (`0` `sorry`).
  - Companion formalization in `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` (`qou-mxnu`, `qou-vbz4`, commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`, PR `https://github.com/litlfred/qou/pull/8141`) proves `qFact5_eq_qDim41_mul_qHookProd41` (the algebraic identity underlying pin (b) $w_{(4,1)}(q) = d_q(4,1)^2 / [5]_q!$) and the 1D Schur line proportionality `schur_invariantForm_proportional`.
- Kept at `status: in-progress` per owner governance.
