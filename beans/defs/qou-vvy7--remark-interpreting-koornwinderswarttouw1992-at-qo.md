---
# qou-vvy7
title: Remark interpreting [koornwinderswarttouw1992] at QOU.BraidKnot.Keystone
status: todo
pr: 8425
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:47Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-vva9
---

Soften the 'on E_q(2)' clause at KeystoneSelfDualSpectralNarrowing.lean:59: the self-reciprocal pair is this document's, but the quantum-group-of-plane-motions setting belongs to the paper it cites rather than to it.

**From the source**
- transform pair, pp. 9-10 — A q-Hankel transform pair with the same third-q-Bessel kernel in both directions, hence self-reciprocal, degenerating to the classical Hankel pair as q -> 1.
  Use here: The analytic prototype of the self-reciprocality the keystone narrowing formalizes as S^4 = 1, and the reason a free-scale q-Bessel family is a duality template rather than a zero-dof node screen.

Source: `library/arxiv-1208.2521v1/1208.2521v1.pdf` (`koornwinderswarttouw1992`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Implementation Progress (PR #8425)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/PadicPolylogSelfReciprocalVortexPotentialRound71.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round71_padic_polylog_self_reciprocal_vortex_potential_probe.py` with 2-commit witness `computations/probes/round71-padic-polylog-self-reciprocal-vortex-potential.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8425 (`ready: e9a0477369d852fec1b713ba0fbbc441b552fa75`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8425, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
