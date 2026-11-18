---
# qou-ohl6
title: Cross-check 0706.2213v3.pdf at computations/one_loop_torsion.py (and the two implementations its …
status: in-progress
pr: 8386
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:54Z
updated_at: 2026-10-04T15:18:15Z
parent: qou-8hur
---

Three in-repo implementations disagree on |tau(4_1)| and the disagreement is documented but not externally adjudicated; DHY Tables 1-2 plus Thm 19 give an independent family of values to check against, once the mu-vs-lambda normalisation is pinned.

Source: `library/arxiv-0706.2213v3/0706.2213v3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0706.2213v3/  ->  [dubois2007]
  NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [dubois2007] as the citation key when you do it.

## Progress (2026-11-18, PR #8386)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`dc2e35b36f4ebb7e9b1575a73bdbe33cb67ee130`, `scriptHash: 2ebaf0631eb0504b9d6d5bd79a3a8425d49d4ffed0fadf6b52c241edb18846dc`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8386`
