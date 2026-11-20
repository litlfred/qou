---
# qou-njry
title: Cite nrarith.pdf at folio/quantum-observable-universe/braids-and-knots/self-dual-higgs-real-vol…
status: todo
pr: 8386
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:18Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-19m0
---

self-dual-higgs-real-volume leans on 4_1's amphichirality as a structural fact with no source; the amphicheirality criterion supplies one.

**From the source**
- Prop. 3.4 — If a hyperbolic orbifold is amphicheiral then its invariant trace field is closed under complex conjugation (and correspondingly for the quaternion algebra), giving an effective amphicheirality and commensurable-amphicheirality test.
  Use here: A cited, checkable criterion behind the corpus's structural use of 4_1's amphichirality, which is currently asserted in several blocks with no source.

Source: `library/nrarith/nrarith.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/nrarith/  ->  [neumann-reid]
  Arithmetic of hyperbolic manifolds

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [neumann-reid] as the citation key when you do it.

## Progress (2026-11-18, PR #8386)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`dc2e35b36f4ebb7e9b1575a73bdbe33cb67ee130`, `scriptHash: 2ebaf0631eb0504b9d6d5bd79a3a8425d49d4ffed0fadf6b52c241edb18846dc`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8386`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8386, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
