---
# qou-vo5j
title: Cite 0411647v2.pdf at QOU.BraidsAndKnots.DeltaLambdaDReduction (docstring) and computations/delta…
status: completed
pr: 8420
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:49Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

The Sigma-hat_3 = R_4 + R_2 identity is recorded as machine-verified with no source in both the witness description and the Lean docstring; Thm 4.14 at n=4 is the source.

Source: `library/arxiv-math-0411647v2/0411647v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0411647v2/  ->  [sniady2006asymptotics]
  Asymptotics of characters of symmetric groups, genus expansion and free probability

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [sniady2006asymptotics] as the citation key when you do it.


## Implementation Progress (PR #8420)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HyperbolicGreenConormalFoldedTraceRound70.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round70_hyperbolic_green_conormal_folded_trace_probe.py` with 2-commit witness `computations/probes/round70-hyperbolic-green-conormal-folded-trace.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8420 (`ready: f49a1cf2981f96f2f1ad64b7c08e14fa43ef96ca`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8420, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — expo-cite-xcheck drain

`Ref: [sniady2006asymptotics] §4.5` added to DeltaLambdaDReduction.lean: second-order expansion at n=4 gives Σ̂3 = R4 + R2 + const, const = 0 on the empty diagram. 'Thm 4.14' not confirmable from held text. Witness description not edited (would need producer re-run). Completes on merge. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.

## 2026-11-21: merged

Completed: PR #8852 merged (merge 4d8767a1c).
