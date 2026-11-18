---
# qou-25oc
title: Remark interpreting 0302267v2.pdf at conj:gb-depth-period-correspondence
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:37Z
updated_at: 2026-10-04T15:23:25Z
parent: qou-aqfj
---

Record the §6.2 caveat that the D-degree grading refining the depth filtration exists only in the omega-realisation and is not stable under the involution u -> u^{-1} — relevant to whether the corpus's GS-depth <-> period-depth correspondence should be stated at the level of the filtration or the grading. This is a caveat to flag, not a proof aid; I have not checked which side the corpus intends.

**From the source**
- §6.1, eqs. (6.1.1)-(6.1.2) — The depth filtration D on the motivic fundamental group of X = P^1 minus {0, infinity, mu_N}: D^0 pi_1 = pi_1, D^1 pi_1 = ker(pi_1(X,x) -> pi_1(A*,x)), and D^n the n-th lower central series term of D^1; induced on Lie algebras, enveloping algebras and torsor affine algebras.
  Use here: This is the definition of the 'Goncharov period-depth' half of conj:gb-depth-period-correspondence, which the corpus's keystone correlates with GS-depth. The conjecture is currently stated against an undefined-in-corpus notion of depth; citing §6.1 fixes what the right-hand side of the correspondence means, including the caveat (§6.2) that the D-degree grading exists only in the omega-realisation and is not stable under u -> u^{-1}.

Source: `library/arxiv-math-0302267v2/0302267v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0302267v2/  ->  [deligne-goncharov2005]
  Groupes fondamentaux motiviques de Tate mixte

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [deligne-goncharov2005] as the citation key when you do it.
