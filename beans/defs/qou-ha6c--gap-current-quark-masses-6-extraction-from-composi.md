---
# qou-ha6c
title: 'GAP: m_u, m_d — only m_d − m_u is extractable (δ_QCD = Δ_pn + E_EM); E_EM is gating object 4-B (m_s/m_c, m_b/m_t split out 2026-09-03)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-mass
    - sm-26
created_at: 2026-07-31T20:15:07Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
blocked_by:
    - qou-bn8e
    - qou-o6ml
    - qou-37y0
---

## 🔥 Roast (2026-09-03, qou-bsu0) — scope narrowed to m_u, m_d

(i) Needs the intra-nucleon E_EM in δ_QCD = Δ_pn + E_EM (`quark-mass-extraction-stage1.witness.json`): the bond that the derived ratio h/[2]_q = tanh(ln q₀) = 0.10396 multiplies. m_u + m_d is circular (m_π is CAL-3).
(ii) Excluded: any E_EM odd in μ̄₁₂₃ (scope-b, `MilnorTripleLinkingMagnus.odd_symmetric_functional_vanishes`); pairwise-linking functionals on the Borromean carrier (lk_ij = 0, probe A3); the quadratic-charge ansatz fits the octet rather than constraining it (bijection, det −1/3, `ChargeQuadraticSumRule.lean`); the `H_coth` kernel (O2 zero-mean). Quark charges are asserted, not derived (`qou-a468`).
(iii) Trap: back-solving the coupling k from Δ_pn (`qou-37y0`), or a normalisation from mirror residuals; a fitted carrier (`qou-5vhf`).
(iv) Next: derive the self channel A·Σq² (`qou-bn8e` — A1 disposes of it only in binding energy). Gate: 4-B. Conditional-on-one-bond m_d − m_u is plausible in months; unconditional is not.
(v) Forecast: the first quark number, if any, and conditional.
Tower status [reading: qou-ggdk]: ORDER-ZERO-ONLY — single-crossing pairwise Coulomb ansatz; Δ_pn rides the truncated c_k ladder; the sinh Coulomb channel is *discarded by the canonical projection* (canonical cheat sheet §3.1). Full-tower version — keep the bar-odd sinh channel inside tr_M = Σ_λ y_λ χ_λ — is not formulated anywhere.

## Round 66 Update (PR #8239)
- Formalized in `WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.lean` and verified via 80-dps `mpmath` witness in PR #8239.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8239, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
