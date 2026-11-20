---
# qou-v56q
title: Cite [geck-lambropoulou-2004] at conj:type-b-folding-cpt
status: todo
pr: 8420
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:42Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1qhv
---

Move or add the citation to the block that actually needs type-B trace theory: conj:type-b-folding-cpt asserts a bar-invariance property of the folded type-B picture with no trace-side source, and Thm 4.3 classifies exactly the Markov traces available there. The existing entry at hecke-markov-interpretation.ts:22 sits on a purely type-A block and should be reconsidered or dropped.

**From the source**
- Thm 4.3 (with Def 4.1) — Full classification of the linear traces on the Iwahori-Hecke algebra of type B satisfying the Markov property.
  Use here: Bounds which trace functionals a folded type-B Hecke picture may use, i.e. constrains the invariant available to the type-B folding conjecture, whose bar-invariance claim currently has no trace-side source.

Source: `library/arxiv-math-0405508v1/0405508v1.pdf` (`geck-lambropoulou-2004`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Implementation Progress (PR #8420)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HyperbolicGreenConormalFoldedTraceRound70.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round70_hyperbolic_green_conormal_folded_trace_probe.py` with 2-commit witness `computations/probes/round70-hyperbolic-green-conormal-folded-trace.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8420 (`ready: f49a1cf2981f96f2f1ad64b7c08e14fa43ef96ca`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8420, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
