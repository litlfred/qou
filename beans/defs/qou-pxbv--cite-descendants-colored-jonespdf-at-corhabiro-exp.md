---
# qou-pxbv
title: Cite descendants_colored_jones.pdf at cor:habiro-expansion-atomic
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:05Z
updated_at: 2026-10-04T15:17:49Z
parent: qou-ysb7
---

The atomic Habiro expansion block constructs colored-Jones/Markov-trace data as a Habiro-ring element; this document states exactly that realization and links it to the pentagon-R-matrix route the corpus also formalises.

**From the source**
- Abstract / §1 — The colored Jones polynomials admit two realizations: one via quantum R-matrices at roots of unity obtained from solutions of the pentagon identity, and one as a sequence of elements of the Habiro ring arising in the Refined Quantum Modularity Conjecture.
  Use here: Directly joins the two routes QOU treats separately — the dilogarithm/pentagon associator line and the Habiro-ring cyclotomic-expansion line — and would source the Habiro-element framing used by the Q_beta blocks.

Source: `library/descendants-colored-jones/descendants_colored_jones.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/descendants-colored-jones/  ->  [garoufalidis-kashaev-descendants2023]
  The descendant colored Jones polynomials

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis-kashaev-descendants2023] as the citation key when you do it.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

cor:habiro-expansion-atomic now cites garoufalidis-kashaev-descendants2023 §2.2 eqs. (2)-(4) and §3, scoped to knots. Ruling check: the block's 'magic-shell' wording sits near the withdrawn T(2,n_s) shell rule; the added paragraph does not use it, and the block body was left as is.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.
