---
# qou-d30z
title: Add reference for 2109.00379v1.pdf at computations/one_loop_torsion.py
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:11Z
updated_at: 2026-08-21T17:03:30Z
---

No ref() entry; the corpus's NZ-matrix work is live and recently corrected, and this is the current reference for the matrices' symplectic structure and their computation from a triangulation.

**From the source**
- Sects. 1.3 and 2 — Neumann-Zagier matrices and their twisted version, with the symplectic properties proved and an explicit recipe for computing them from the combinatorics of an ideal triangulation.
  Use here: A clean modern statement of the symplectic constraints the corpus's determinant must respect; relevant precisely because a wrong matrix was in production until 2026-08-07 and the corrected one still inherits an unpinned constant at c >= 2.
- Sects. 3.1 and 5.1 (the knot 4_1) — Fully worked NZ matrices and 1-loop invariant for the figure-eight knot.
  Use here: An independent published 4_1 value to regression-test computations/one_loop_torsion.py against, which matters because the corpus's 4_1 calibration was previously off by exactly a factor of two.

Source: `library/arxiv-2109.00379v1/2109.00379v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-2109.00379v1/  ->  [garoufalidis2021]
  TWISTED NEUMANN–ZAGIER MATRICES

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
