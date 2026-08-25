---
# qou-mcty
title: Add reference for s40687-023-00400-3.pdf at computations/probes/borromean_nz_adjoint_torsion.py
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:37:01Z
updated_at: 2026-08-21T17:03:46Z
---

The corpus's NZ-matrix arc was corrected one day before this triage and its audit states the multi-cusp case is absent from the literature it had; this paper is the systematic NZ-matrix treatment it lacks, and has no entry.

**From the source**
- Abstract and the construction of twisted NZ matrices from triangulation combinatorics — Twisted Neumann--Zagier matrices are defined, shown to retain the symplectic properties of the untwisted ones, and computed directly from the combinatorics of an ideal triangulation.
  Use here: The reference construction against which the corpus's corrected NZ determinant should be checked, in a form that is explicitly combinatorial and therefore testable for the retriangulation invariance the corpus's earlier version failed.

Source: `library/s40687-023-00400-3/s40687-023-00400-3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/s40687-023-00400-3/  ->  [garoufalidis2021]
  TWISTED NEUMANN–ZAGIER MATRICES

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
