---
# qou-abtu
title: Cite [furey2016] at conj:sm-colour-stabilizer-action
status: todo
pr: 8209
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-lit
created_at: 2026-08-08T23:35:01Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

The colour-stabilizer conjecture's prose describes exactly this construction (su(3) = ker(ev_e), the 1 + 3 decomposition of O) and cites dubois-violette-todorov2018 but not this document, which is registered specifically for that purpose and cited nowhere.

**From the source**
- Ch. on C (x) O and the colour stabilizer — SU(3) x U(1) arises as the subgroup of the C (x) O structure stabilizing a chosen unit imaginary octonion, with electric charge given by a number operator producing the correct one-generation charge spectrum.
  Use here: The literature precedent conj:sm-colour-stabilizer-action already paraphrases without citing, and the closest existing route to the hypercharge datum conj:sm-hypercharge-invariant declares missing.

Source: `library/arxiv-1611.09182v1/1611.09182v1.pdf` (`furey2016`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## Progress (2026-11-16, PR #8209)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/RankOneSpinSingletThreeGenerationsLadderChargeAndNearlyKahlerCosets.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`9c4fe9d8065c7167caac7a61ef4becd45df1573f`, `scriptHash: e6bdb7c63ac7`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8209`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8209, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
