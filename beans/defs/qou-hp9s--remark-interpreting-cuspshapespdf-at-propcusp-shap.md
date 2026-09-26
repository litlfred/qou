---
# qou-hp9s
title: Remark interpreting CuspShapes.pdf at prop:cusp-shape-bar-parity
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:36:39Z
updated_at: 2026-08-21T17:04:56Z
---

Pin down which object 'cusp shape' names in prop:cusp-shape-bar-parity -- the Teichmuller modulus of the cusp torus, or the ideal-tetrahedron shape parameter tiling it -- and confirm the figure-eight value against the standard one. Deliberately a remark and not aid-proof: I could not settle the numerical question in this session, and the downstream cusp lattice Z<1, omega> depends on the answer.

**From the source**
- sec. 3 ("Recall that the Teichmuller space of the torus is the space of similarity classes...") + Def. 2.1-2.4 — The cusp shape of a hyperbolic 3-manifold with torus boundary is the similarity class of the Euclidean structure induced on a neighbourhood of that boundary, i.e. a point of the Teichmuller space of the torus.
  Use here: Supplies the standard definition for a term the corpus uses in at least three blocks with no source, and against which its value for the figure-eight should be checked.
- Thm 1.1 — Cusp shapes of hyperbolic tunnel-number-one manifolds are dense in the Teichmuller space of the torus.
  Use here: Background only: it says the cusp shape is not constrained by low tunnel number, so no structural conclusion can be drawn from a particular knot's cusp shape being special.

Source: `library/cuspshapes/CuspShapes.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/cuspshapes/  ->  [dang-purcell]
  Cusp shape and tunnel number

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [dang-purcell] as the citation key when you do it.
