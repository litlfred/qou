---
# qou-c7lf
title: Cite 1003.4808v2.pdf at prop:phi-q-aj-machinery-identification
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:21Z
updated_at: 2026-11-21T13:32:29Z
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

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8325, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

prop:phi-q-aj-machinery-identification now cites dimofte-gukov2010 §2.2 eqs. (2.15)-(2.17) and §3.2.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

PR #8828 merged 2026-11-21 (rebased onto main as a8b394e108). Completed.
