---
# qou-mllr
title: Cite 2509.02354v2.pdf at prop:dilog-pentagon-is-associator
status: in-progress
pr: 8380
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:04Z
updated_at: 2026-10-04T15:17:20Z
parent: qou-ysb7
---

The dilogarithm-pentagon-associator block states the dilogarithm-braiding relation abstractly and would be strengthened by the explicit four-dilogarithm factorization of the holonomy R-matrix at a root of unity.

**From the source**
- §4.3 (factorization of the R-matrix) and §4.4 — The normalized holonomy R-matrix of quantum sl2 at a root of unity factorizes as a product of four quantum dilogarithms and satisfies a holonomy Yang-Baxter equation.
  Use here: A concrete realisation of the quantum-dilogarithm-to-braiding relation that prop:dilog-pentagon-is-associator asserts abstractly, in the root-of-unity regime the QBeta pentagon files work in.

Source: `library/arxiv-2509.02354v2/2509.02354v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2509.02354v2/  ->  [mcphail-snyder-reshetikhin2025]
  The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [mcphail-snyder-reshetikhin2025] as the citation key when you do it.

## Progress (2026-11-18, PR #8380)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`35b03645ad735c533bdb60a9a19a56165e5833fa`, `scriptHash: 197841ead85d03085a06e8bf1a078fa708f1da7e60c96d98a12ad24512b472a1`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8380`
