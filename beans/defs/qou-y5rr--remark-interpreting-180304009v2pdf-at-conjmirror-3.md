---
# qou-y5rr
title: Remark interpreting 1803.04009v2.pdf at conj:mirror-3d-3d-correspondence
status: todo
pr: 8438
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:09Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-aqfj
---

The T^DGG-realises-only-a-subset-of-flat-connections caveat should be stated in the folio rather than left implicit, since the conjecture's whole content is an equality of partition functions. NOT proposed as aid-proof: the enhancement criterion is stated for one torus boundary and B_3 has three cusps, so its applicability to the corpus's manifold is unchecked.

**From the source**
- Sect. 2.3 — T^DGG[M,K] realises only some subset of the irreducible flat SL(2,C) connections on the knot complement as its vacua, unlike the 6d theory T^6d[M,K]; the proposed relation T^6d -> T_irred -> T^DGG explains why T^DGG generically carries only a U(1) flavour symmetry.
  Use here: Qualifies conj:mirror-3d-3d-correspondence's stated equality between the squashed-sphere partition function and the state-integral invariant, and qualifies its Open Question 1: identifying T[B_3] by the DGG recipe does not by itself deliver the 6d object the conjecture's dictionary assumes.
- Sect. 3 + Table 1 — A topological criterion on the knot complement for when the U(1)_{X_A} flavour symmetry of T^DGG enhances to SU(2)/SO(3).
  Use here: The precondition the corpus would have to check before applying any closing/filling operation to the Borromean complement; note the criterion is stated for a single torus boundary, and B_3 has three cusps, so transporting it is exactly the thing that would need checking.
- Sect. 4.1 — Identification of the field-theoretic operation on T^DGG corresponding to Dehn filling, giving a construction of theories attached to closed 3-manifolds and predicting infinitely many 3d dualities from surgery calculus.
  Use here: The concrete route for Open Question 1 (identify T[B_3]); the corpus currently has only 'DGG 2014 provides the construction' with no closing procedure.

Source: `library/arxiv-1803.04009v2/1803.04009v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1803.04009v2/  ->  [arxiv-1803.04009v2]
  Symmetry enhancement and closing of knots in 3d/3d correspondence

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-1803.04009v2] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8438, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
