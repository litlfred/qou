---
# qou-c7lf
title: Cite 1003.4808v2.pdf at prop:phi-q-aj-machinery-identification
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:21Z
updated_at: 2026-11-17T11:44:32Z
pr: 8325
parent: qou-ysb7
---

The block's Phi_q-vs-Li_2^q context sorting is precisely the quantum-VC saddle framing these lectures develop, and it currently carries no citation for it.

**From the source**
- Sec. 2.2 (Quantum VC) + Sec. 3.2 (Quantization) — The quantum volume conjecture organizes the full 1/N expansion of the colored Jones polynomial, and its structure is governed by the quantization of the A-polynomial (the operator A-hat_K annihilating J_N).
  Use here: Gives a citable framing for the corpus's claim that Phi_q and Li_2^q are two archimedean saddles of one AJ operator, which prop:phi-q-aj-machinery-identification currently states with no source.

Source: `library/arxiv-1003.4808v2/1003.4808v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1003.4808v2/  ->  [dimofte-gukov2010]
  Quantum field theory and the volume conjecture

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [dimofte-gukov2010] as the citation key when you do it.

### Progress (Round 61)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8325 (`5b31e8e9599f35d940975c6c2937ae31bf0eaa65`). Status kept `in-progress` pending PR merge.
