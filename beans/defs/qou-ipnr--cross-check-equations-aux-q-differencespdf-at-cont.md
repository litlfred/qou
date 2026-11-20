---
# qou-ipnr
title: Cross-check Equations_aux_q-differences.pdf at folio/quantum-observable-universe/lean/QOU/QBeta…
status: todo
pr: 8380
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:31Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8hur
---

Re-run the attack plan's degree-budget table against the Sec. 4.4 example: compare the corpus's residual (deg c_n = n^2 against t_n = q^{C(n,2)}) with the 'order exactly two' q-Borel growth Rmk 4.12 computes, and record whether the C1 series is, up to gauge, of the multi-level type that example exhibits. This is a comparison to run, not a result to adopt.

Source: `library/equations-aux-q-differences/Equations_aux_q-differences.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/equations-aux-q-differences/  ->  [divizio-ramis-sauloy-zhang]
  Équations aux q-différences

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [divizio-ramis-sauloy-zhang] as the citation key when you do it.

## Progress (2026-11-18, PR #8380)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`35b03645ad735c533bdb60a9a19a56165e5833fa`, `scriptHash: 197841ead85d03085a06e8bf1a078fa708f1da7e60c96d98a12ad24512b472a1`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8380`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8380, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
