---
# qou-pgd0
title: Add reference for 1003.4808v2.pdf at prop:phi-q-aj-machinery-identification
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:37:20Z
updated_at: 2026-08-21T17:03:50Z
---

Cited by bare arXiv URL in two audit docs with no ref() entry; a reference key is needed before it can be cited from a block.

**From the source**
- Sec. 2.2 (Quantum VC) + Sec. 3.2 (Quantization) — The quantum volume conjecture organizes the full 1/N expansion of the colored Jones polynomial, and its structure is governed by the quantization of the A-polynomial (the operator A-hat_K annihilating J_N).
  Use here: Gives a citable framing for the corpus's claim that Phi_q and Li_2^q are two archimedean saddles of one AJ operator, which prop:phi-q-aj-machinery-identification currently states with no source.

Source: `library/arxiv-1003.4808v2/1003.4808v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-1003.4808v2/  ->  [dimofte-gukov2010]
  Quantum field theory and the volume conjecture

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
