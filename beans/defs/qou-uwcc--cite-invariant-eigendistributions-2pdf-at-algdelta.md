---
# qou-uwcc
title: Cite Invariant_eigendistributions_2.pdf at alg:delta-lambda-closure
status: completed
pr: 8420
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:40Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

alg:delta-lambda-closure calls Delta_lambda 'the signed Springer dimension' with nothing behind the name. A citation should be added; a reviewer should also decide whether this construction or a more canonical Springer-correspondence source is the right primary for the sign convention.

**From the source**
- sec. 2 and sec. 4 — Weyl-group representations are constructed on the (Borel-Moore) homology of the conormal variety via an integral formula for invariant eigendistributions, yielding the Springer representations.
  Use here: The geometric backdrop for the phrase 'signed Springer dimension' that alg:delta-lambda-closure uses without a source.
- sec. 12 (Appendix) — The homotopy action constructed here agrees with the Kazhdan-Lusztig construction of the Weyl-group action on the conormal variety.
  Use here: Relevant to the PROBE-4 prune's framing, which contrasts the mixed-sign Delta_lambda target against the non-negativity of Kazhdan-Lusztig multiplicities; the comparison shows the two constructions of the same W-action are not independent sources of a sign.

Source: `library/invariant-eigendistributions-2/Invariant_eigendistributions_2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/invariant-eigendistributions-2/  ->  [rossmann-invariant-eigendistributions-2]
  Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [rossmann-invariant-eigendistributions-2] as the citation key when you do it.


## Implementation Progress (PR #8420)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HyperbolicGreenConormalFoldedTraceRound70.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round70_hyperbolic_green_conormal_folded_trace_probe.py` with 2-commit witness `computations/probes/round70-hyperbolic-green-conormal-folded-trace.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8420 (`ready: f49a1cf2981f96f2f1ad64b7c08e14fa43ef96ca`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8420, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — expo-cite-xcheck drain

Already done on main: mba-sidecar-delta-lambda-closure cites springer1976 and shoji2019 for 'signed Springer dimension' with a name-only disclaimer, which is the more canonical primary the bean asked a reviewer to choose. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.
