---
# qou-o29t
title: 'PROVE(lean): covariance_kernel_conjecture — theorem covariance_kernel_conjecture (k : ℕ) : kernelValue k ≤ 0  [cited manuscript]'
status: scrapped
type: task
priority: normal
tags:
    - paper-qou
    - infra-blocked
    - reorg-2026-10-04
    - lean
    - cited-sorry
created_at: 2026-08-01T23:31:04Z
updated_at: 2026-10-04T15:22:26Z
parent: qou-k1mq
---

**File:** `QOU/BraidsAndKnots/YoungDiagramKernel.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean

### `covariance_kernel_conjecture`  —  line 295  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem covariance_kernel_conjecture (k : ℕ) : kernelValue k ≤ 0 `
- **Cited:** `[manuscript]`
  - [manuscript] docs/audits/2026-07-18-deltalambda-covariance-kernel-frontier.md
- **Tractability:** kernelValue k ≤ 0 stated as a conjecture (covariance-kernel negativity); open QOU claim.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.


## RE-TRIAGED 2026-08-31 — OPEN QOU CONJECTURE — not a Mathlib gap

The `Next step` line above ("Infra-blocked: needs Mathlib theory that does not exist. Track
upstream") is one verdict that was stamped on fourteen beans in six seconds, and is wrong here.
Full audit: `docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md`.

`covariance_kernel_conjecture`'s own docstring reads "**CONJECTURE (OPEN).** ... verified
k <= 30 computationally. Not proved.", and its carrier is
`class CovarianceKernelConjecture : Prop where nonpos : forall k, kernelValue k <= 0` with NO
instance -- precisely the honest representation AGENTS.md section-3b prescribes for an open
primary conjecture.

Nothing here is waiting on Mathlib, so "Track upstream" is wrong advice: no upstream release
closes a QOU conjecture. What would close it is a proof (or a refutation) of the conjecture.

The original text is kept above, not deleted: the Tractability line is per-item and is accurate;
only the Next-step verdict is being corrected.



## Reasons for Scrapping

Duplicate of `qou-085a` (work-plan reorganisation 2026-10-04). Evidence: same decl covariance_kernel_conjecture in YoungDiagramKernel.lean [B]
Content is untouched; only this work item is closed.
