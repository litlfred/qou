---
# qou-mmq7
title: Cross-check 0103325v4.pdf at computations/lepton_t2n_torus_tower.py
status: in-progress
pr: 8380
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:44Z
updated_at: 2026-10-04T15:18:14Z
parent: qou-8hur
---

The identity [n]_q - [n-1]_q = Delta_q{(2,2n-1)} is q-generic and parameter-free, so it can be verified symbolically against the corpus's own q-integers and Alexander-polynomial machinery. This is an algebraic cross-check, not an adoption of any numerical value; the root-of-unity q of the source must NOT be substituted for the substrate q_0.

**From the source**
- Sec. 2, 'Labelling flavors by knots invariants' — The q-polynomials [n]_q - [n-1]_q coincide with the Alexander polynomials Delta_q of the (2, 2n-1) torus knots ([2]_q - 1 = Delta{3_1}, [3]_q - [2]_q = Delta{5_1}, [4]_q - [3]_q = Delta{7_1}), and the torus knots 5_1, 7_1, 9_1, 11_1 are placed in correspondence with the vector quarkonia s-sbar, c-cbar, b-bbar, t-tbar.
  Use here: A parameter-free algebraic identity between the corpus's own q-integers and Alexander polynomials of the T(2, odd) tower, plus a competing assignment of that tower to quarkonia rather than leptons -- both belong in the T(2,n) lepton-tower probe and in the consistency ledger.

Source: `library/arxiv-hep-ph-0103325v4/0103325v4.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-ph-0103325v4/  ->  [arxiv-hep-ph-0103325v4]
  Quantum algebras in phenomenological description of particle properties

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-hep-ph-0103325v4] as the citation key when you do it.

## Progress (2026-11-18, PR #8380)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`35b03645ad735c533bdb60a9a19a56165e5833fa`, `scriptHash: 197841ead85d03085a06e8bf1a078fa708f1da7e60c96d98a12ad24512b472a1`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8380`
