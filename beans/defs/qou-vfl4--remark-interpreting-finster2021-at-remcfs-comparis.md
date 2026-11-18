---
# qou-vfl4
title: Remark interpreting [finster2021] at rem:cfs-comparison-summary
status: in-progress
pr: 8420
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:08Z
updated_at: 2026-11-18T10:09:26Z
parent: qou-vva9
---

The three structural claims in the CFS comparison (type II_1 embedding, the causal-Lagrangian eigenvalue-difference form, and the G_2 - ||x.y||_1^2 decomposition) carry no inline source; the only inline citation is to a document that contains none of them. Record which of the .ts-listed sources actually backs each claim, or mark them as the folio's own reconstruction.

Source: `finster2021` (bib key; PDF not committed to this repo)
Relevance: **tangential** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Implementation Progress (PR #8420)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HyperbolicGreenConormalFoldedTraceRound70.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round70_hyperbolic_green_conormal_folded_trace_probe.py` with 2-commit witness `computations/probes/round70-hyperbolic-green-conormal-folded-trace.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8420 (`ready: f49a1cf2981f96f2f1ad64b7c08e14fa43ef96ca`).
