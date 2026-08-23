---
# qou-cmx2
title: Add reference for 1302.0342v1.pdf at rem:breit-wheeler-vertex-literature
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:29Z
updated_at: 2026-08-21T17:03:29Z
---

No ref() entry; the corpus has scheeler2014 and kleckner2013 for fluid helicity but nothing for knotted electromagnetic field lines.

**From the source**
- abstract + Fig. 2-4 (construction via Bateman variables on S^3) — There is a family of null free-space Maxwell fields whose field lines encode all torus knots and links, with the knot/link topology preserved by the evolution (a geodesic, shear-free flow along the Poynting vector).
  Use here: Extends the 'photonic hopfions' alignment paragraph from Hopf links to the torus-knot family the corpus's knot-particle dictionary actually uses.

Source: `library/arxiv-1302.0342v1/1302.0342v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-1302.0342v1/  ->  [arxiv-1302.0342v1]
  Tying knots in light fields

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
