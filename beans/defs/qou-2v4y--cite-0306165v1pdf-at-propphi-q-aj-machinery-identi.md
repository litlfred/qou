---
# qou-2v4y
title: Cite 0306165v1.pdf at prop:phi-q-aj-machinery-identification
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:27Z
updated_at: 2026-11-17T11:44:32Z
pr: 8325
parent: qou-ysb7
---

prop:phi-q-aj-machinery-identification's saddle-point framing is uncited; garoufalidis2004 covers the q-difference operator, not the Chern-Simons asymptotics that make 'saddle regime' meaningful.

**From the source**
- sec. 3.1 + sec. 5.2, eq. (5.12) — The classical A-polynomial's zero locus is the Lagrangian of the SL(2,C) Chern-Simons phase space, and its quantisation governs a one-parameter family of colored-Jones asymptotics (Vol(l,m) + i 2 pi^2 CS(l,m)) that contains the volume conjecture at m = 1.
  Use here: Supplies the Chern-Simons saddle-point reading of the AJ operator that prop:phi-q-aj-machinery-identification asserts but sources only on the algebraic side.

Source: `library/arxiv-hep-th-0306165v1/0306165v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-th-0306165v1/  ->  [arxiv-hep-th-0306165v1]
  Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-hep-th-0306165v1] as the citation key when you do it.

### Progress (Round 61)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8325 (`5b31e8e9599f35d940975c6c2937ae31bf0eaa65`). Status kept `in-progress` pending PR merge.
