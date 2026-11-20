---
# qou-w5go
title: Remark interpreting [madison2000] at folio/quantum-observable-universe/observations/bec-vortex-…
status: todo
pr: 8425
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:42Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-vva9
---

Same block as gauthier2019: bec-vortex-data.md rests on two experimental papers, neither of which is present in the tree, and neither citation carries a figure or section locator. Re-obtain both and add locators in one pass.

Source: `madison2000` (bib key; PDF not committed to this repo)
Relevance: **undetermined** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Implementation Progress (PR #8425)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/PadicPolylogSelfReciprocalVortexPotentialRound71.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round71_padic_polylog_self_reciprocal_vortex_potential_probe.py` with 2-commit witness `computations/probes/round71-padic-polylog-self-reciprocal-vortex-potential.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8425 (`ready: e9a0477369d852fec1b713ba0fbbc441b552fa75`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8425, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
