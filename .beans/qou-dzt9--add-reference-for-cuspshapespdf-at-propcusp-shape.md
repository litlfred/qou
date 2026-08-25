---
# qou-dzt9
title: Add reference for CuspShapes.pdf at prop:cusp-shape-bar-parity
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:38Z
updated_at: 2026-08-21T17:03:32Z
---

No ref() entry, and no source anywhere in the corpus for the notion of cusp shape despite three blocks depending on it.

**From the source**
- sec. 3 ("Recall that the Teichmuller space of the torus is the space of similarity classes...") + Def. 2.1-2.4 — The cusp shape of a hyperbolic 3-manifold with torus boundary is the similarity class of the Euclidean structure induced on a neighbourhood of that boundary, i.e. a point of the Teichmuller space of the torus.
  Use here: Supplies the standard definition for a term the corpus uses in at least three blocks with no source, and against which its value for the figure-eight should be checked.
- Thm 1.1 — Cusp shapes of hyperbolic tunnel-number-one manifolds are dense in the Teichmuller space of the torus.
  Use here: Background only: it says the cusp shape is not constrained by low tunnel number, so no structural conclusion can be drawn from a particular knot's cusp shape being special.

Source: `library/cuspshapes/CuspShapes.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/cuspshapes/  ->  [dang-purcell]
  Cusp shape and tunnel number

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
