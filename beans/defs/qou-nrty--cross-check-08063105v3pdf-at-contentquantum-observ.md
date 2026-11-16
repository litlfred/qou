---
# qou-nrty
title: Cross-check 0806.3105v3.pdf at folio/quantum-observable-universe/appendix-standard-model/sm-hyp…
status: in-progress
pr: 8216
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:56Z
updated_at: 2026-10-04T15:18:16Z
parent: qou-t6rw
---

Evaluate Q_e = -(e/6)(w + r + 1) and t_0 = -(r+1)/6 on the QOU proton/neutron knot states: the nucleon doublet is the recorded falsification for writhe-only Y, so whether adding r separates it is a one-shot decisive test of the candidate. A pass does not wire it (the correspondence is fitted upstream); a fail prunes the candidate.

Source: `library/arxiv-0806.3105v3/0806.3105v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0806.3105v3/  ->  [finkelstein2008]
  Knots and preons

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [finkelstein2008] as the citation key when you do it.

## Progress (2026-11-16, PR #8216)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/HyperchargeWritheRotationJordanGlobalGroupOctonionAndShellFilling.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`4e815f9543024d961ef648f5d19347ad79739059`, `scriptHash: 34801c11045c`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8216`
