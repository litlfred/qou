---
# qou-9g14
title: Remark interpreting 1909.06744v1.pdf at folio/quantum-observable-universe/appendix-mass-binding…
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:17Z
updated_at: 2026-10-04T15:23:35Z
parent: qou-aqfj
---

The transpose convention for d_x = dim B_x vs n(lambda) is not settled in the folio and the proved Lean value depends on which one is meant; record the convention check rather than silently asserting the identification. Explicitly not aid-proof — the Lean theorem is already proved by other means and this citation does not enter its proof.

**From the source**
- Thm 2.1 (i)-(iv), §2 eq. (2.3)-(2.4) — For the Springer resolution of the unipotent variety of GL_n, the top cohomology H^{2d_x}(B_x) of the Springer fibre B_x = pi^{-1}(x) carries an irreducible S_n-action, and for x in the class O_lambda one has H^{2d_x}(B_x) ≅ V_lambda, giving the bijection between unipotent classes and Irr(S_n).
  Use here: Supplies the citation for calling Delta_lambda a 'signed Springer dimension': the magnitude dim V_lambda is the top-cohomology dimension of the Springer fibre and the sign exponent is that fibre's dimension d_x, which in type A is n(lambda) up to the standard transpose convention. Flag rather than assume that convention — the folio should record which of n(lambda)/n(lambda') its d_x matches before leaning on the identification.

Source: `library/arxiv-1909.06744v1/1909.06744v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1909.06744v1/  ->  [shoji2019]
  Springer correspondence for symmetric spaces

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [shoji2019] as the citation key when you do it.
