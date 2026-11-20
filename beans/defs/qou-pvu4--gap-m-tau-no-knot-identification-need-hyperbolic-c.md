---
# qou-pvu4
title: 'GAP: m_tau — no knot identification; need hyperbolic candidate + Vol check vs m_tau/m_e (appendix-standard-model)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - sm-26
    - 8f-mass
created_at: 2026-07-31T20:15:07Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
blocked_by:
    - 08a2
    - qou-htk4
    - qou-lsp9
    - qou-se9w
---

## 🔥 Roast (2026-09-03, qou-bsu0)

(i) Needs a carrier and a mass map that is NOT an H₂(q)-linear readout.
(ii) Excluded: every positive linear functional of H₂(q), canonical tr_M included (scope-b, `lepton_continuant_binet.lean` `markovReadout_pos`); positive two-mode additive sums — log-convex against the log-concave observed bend 12.295 (scope-b, `lepton_tower_log_convexity.lean`); direct Vol(K)/ℏ_q^k over 25 census knots at 1 % (scope-a, `rem:m-tau-knot-prediction`), sharpened by 14.5 bits of census entropy (#4591). Koide is a CAL-4 fit (`k9td`).
(iii) Trap: a census knot near Vol ≈ 34.137 (k=2), or a node placed just under the electron winding — both land 3477.23 by selection.
(iv) Next: test whether the electron can sit at a genuine zero of a T(2,n)→4₁ coupling (`qou-htk4`); Path A ξ_ℓ·Vol_q^tower is underdetermined (`mtxi`), gated on epic `08a2`. Not near-term.
(v) Forecast: no number this year; a proved node-exclusion is the likelier product.
Tower status [reading: qou-ggdk]: MIXED — the exclusions are exact in q but confined to H₂(q); the census search is the order-zero volume term; the only tower-level formulation is the partition-indexed ℓ-branching e→(3,1,1), μ→(3,2), τ = ℓ=3 (`S5SO3FiberAction.lean`; scaffold, no instance).

## Round 66 Update (PR #8239)
- Formalized in `WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.lean` and verified via 80-dps `mpmath` witness in PR #8239.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8239, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
