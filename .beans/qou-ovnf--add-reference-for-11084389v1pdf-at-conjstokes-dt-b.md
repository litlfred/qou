---
# qou-ovnf
title: Add reference for 1108.4389v1.pdf at conj:stokes-dt-bps-bridge
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:28Z
updated_at: 2026-08-21T17:03:49Z
---

No ref() entry. Distinct paper from dimofte-gaiotto-gukov2013 (which is the 3d-index sequel).

**From the source**
- sec. 4.1 ("Definition") and sec. 4.6 — A 3d N=2 theory T_M is assigned to an ideally-triangulated 3-manifold, with the figure-eight knot complement worked out explicitly; triangulation-independence corresponds to mirror symmetry of the resulting theories.
  Use here: Defines T[K], the object conj:stokes-dt-bps-bridge quantifies over; fixes the attribution of 'the 3d-3d dictionary' that the block currently assigns to the 3d-index paper.
- sec. 6.3 — The S_b^3 partition function of T_M is assembled from tetrahedron factors and computed for the figure-eight knot.
  Use here: This is the state integral whose resurgent Stokes constants the corpus's bridge conjecture identifies with DT/BPS counts; the corpus currently has no citation for the state integral's construction.

Source: `library/arxiv-1108.4389v1/1108.4389v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-1108.4389v1/  ->  [dimofte-gaiotto2011]
  Gauge theories labelled by three-manifolds

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
