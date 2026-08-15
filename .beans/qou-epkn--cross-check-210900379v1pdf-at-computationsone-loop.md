---
# qou-epkn
title: Cross-check 2109.00379v1.pdf at computations/one_loop_torsion.py
status: todo
type: task
created_at: 2026-08-08T23:36:11Z
updated_at: 2026-08-08T23:36:11Z
---

Regression-check computations/one_loop_torsion.py's 4_1 output against this paper's worked 4_1 example. This is a cross-check only: no external number may be adopted, and a match does not pin the c >= 2 constant the producer's own caveat flags as unpinned.

**From the source**
- Sects. 1.3 and 2 — Neumann-Zagier matrices and their twisted version, with the symplectic properties proved and an explicit recipe for computing them from the combinatorics of an ideal triangulation.
  Use here: A clean modern statement of the symplectic constraints the corpus's determinant must respect; relevant precisely because a wrong matrix was in production until 2026-08-07 and the corrected one still inherits an unpinned constant at c >= 2.
- Sects. 3.1 and 5.1 (the knot 4_1) — Fully worked NZ matrices and 1-loop invariant for the figure-eight knot.
  Use here: An independent published 4_1 value to regression-test computations/one_loop_torsion.py against, which matters because the corpus's 4_1 calibration was previously off by exactly a factor of two.

Source: `library/arxiv-2109.00379v1/2109.00379v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
