---
# qou-bn8h
title: Cite 0012035v3.pdf at rem:lattice-qcd-from-qou
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:36:26Z
updated_at: 2026-08-21T17:04:50Z
---

rem:lattice-qcd-from-qou opens with the surface-ordered holonomy formula and cites nothing; the knotted-loop caveat of sec. 2.3.1 is directly relevant since the corpus's spanning surface is a Seifert surface of a knot.

**From the source**
- eq. (14), sec. 2.2 ("Theorem") — In its operator form the non-Abelian Stokes theorem states that the path-ordered holonomy around a closed curve C = boundary(S) equals the surface-ordered exponential of the twisted curvature over S.
  Use here: Sources the surface-ordered-exponential formula that rem:lattice-qcd-from-qou states without a citation.
- sec. 2.3.1 ("Topology"), Fig. 9 — When the loop is knotted the naive surface-ordered form fails; the knotted loop is decomposed into a product of surface factors indexed by the genus of the spanning surface, giving the topologically-nontrivial version of the theorem.
  Use here: The corpus applies non-abelian Stokes to holonomy around knots with a Seifert spanning surface, i.e. exactly the topologically-nontrivial case; this flags that the untwisted statement does not cover it.

Source: `library/arxiv-math-ph-0012035v3/0012035v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-ph-0012035v3/  ->  [broda2002]
  Non-Abelian Stokes theorem in action

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [broda2002] as the citation key when you do it.
