---
# qou-68uk
title: Cross-check s40687-023-00400-3.pdf at computations/probes/borromean_nz_adjoint_torsion.py
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:37:02Z
updated_at: 2026-08-21T17:04:44Z
---

Recompute the 4_1 NZ matrices by the document's combinatorial recipe and compare against the corpus's corrected one-loop torsion producer, including the retriangulation-invariance test the earlier construction failed. This is a verification of the corpus's own corrected value, not an adoption of an external one. Restrict strictly to the one-cusped case; do not extend the comparison to the Borromean complement.

**From the source**
- Abstract and the construction of twisted NZ matrices from triangulation combinatorics — Twisted Neumann--Zagier matrices are defined, shown to retain the symplectic properties of the untwisted ones, and computed directly from the combinatorics of an ideal triangulation.
  Use here: The reference construction against which the corpus's corrected NZ determinant should be checked, in a form that is explicitly combinatorial and therefore testable for the retriangulation invariance the corpus's earlier version failed.

Source: `library/s40687-023-00400-3/s40687-023-00400-3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/s40687-023-00400-3/  ->  [garoufalidis2021]
  TWISTED NEUMANN–ZAGIER MATRICES

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis2021] as the citation key when you do it.
