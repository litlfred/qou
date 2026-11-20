---
# qou-2pp7
title: Cross-check 9811173v1.pdf at computations/binding_link_volumes.py
status: todo
pr: 8347
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:38Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8hur
---

Cross-check the corpus's computed link/knot hyperbolic volumes against the published a/b rational invariants for the same complements. This is a cross-check only: any agreement corroborates, and no external number may be adopted into a witness on the strength of a match.

**From the source**
- abstract (the a/b formula) + the census tables — For a hyperbolic 3-manifold whose invariant trace field has a single complex place, the volume equals a rational multiple a/b of a normalised Dedekind zeta value at 2 for that field; 152 distinct such zeta values are identified across the censuses, with 91 manifolds having volumes reducible to pairs of them.
  Use here: A published table of volume-to-zeta rational invariants to cross-check the corpus's link/knot volume computations and the Bring-natural number fields of the depth correspondence against.

Source: `library/arxiv-hep-th-9811173v1/9811173v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-th-9811173v1/  ->  [broadhurst1998]
  Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [broadhurst1998] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8347, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
