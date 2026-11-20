---
# qou-zyr2
title: Cite 1604.02688v1.pdf at computations/probes/figure_eight_3d_index.py
status: todo
pr: 8445
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:22Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-19m0
---

The Prop A.3 pairing and Cor 10.21 criterion are asserted in the probe and its witness with no reference key; once the entry exists the probe docstring and the audit lineage should cite it.

**From the source**
- Def. 8.1 / Cor. 8.2 — The 3D-index I^0_T(0) is a generating series summed over normal-surface classes of the ideal triangulation.
  Use here: The stated shape of the candidate collective binding term (idea B3) and the structure the corpus's Borromean/figure-eight index computations assume.
- Cor. 10.21 — For a 1-efficient ideal triangulation the index sum is a genuine power series (no negative powers of q).
  Use here: This is self-test (i) of the corpus's Borromean 3D-index validation gate, currently cited as 'GHHR Cor 10.21' with no bibliography entry.

Source: `library/arxiv-1604.02688v1/1604.02688v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1604.02688v1/  ->  [garoufalidis-hodgson-hoffman-rubinstein2016]
  The 3D-index and normal surfaces

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis-hodgson-hoffman-rubinstein2016] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8445, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
