---
# qou-pkum
title: Add reference for 1104115581.pdf at computations/probes/quillen_anomaly_classification_probe.py
status: todo
type: task
created_at: 2026-08-08T23:36:04Z
updated_at: 2026-08-08T23:36:04Z
---

Quoted by section and equation number in two audit docs and used as the organizing principle of a live research axis, with no ref() entry; its bibliographic data currently lives only in a blockquote in one audit doc.

**From the source**
- Sect. 4, eqs. (4.1)-(4.2) — Quillen's theorem in the form det_zeta = |det D|^2 e^{-q}: the zeta-regularised determinant of a chiral Dirac operator fails to be the modulus-squared of a holomorphic function by an explicit non-holomorphic counterterm.
  Use here: The cited theorem behind the audit's class-(b) assignment: it is what turns 'det'Delta has nonzero partial-partialbar curvature' into 'det'Delta is not |f|^2 for any holomorphic f', which is the corpus's exact-gates-vs-stuck-magnitudes split.
- Sect. 4, eqs. (4.25)-(4.32) and (4.31) — For the family D: L^n -> L^{n+2} the holomorphic-anomaly obstruction carries weight 3(n+1)^2 - 1, with an explicit Weil-Petersson normalisation, and the resulting objects make no reference to a distinguished constant.
  Use here: The spin-content candidate family used by the alpha_EM r^2 Quillen-curvature attack; it is the source of the weight formula that audit enumerates candidates against.
- Sect. 2 (Fermions on a Torus) — The genus-1 special case, in which the spin-structure-dependent determinant is expressed through theta and eta functions.
  Use here: Sources the corpus's genus-1 identity det'Delta(E_tau) = (Im tau)^2 |eta(tau)|^4, which the audit computes the exact Quillen curvature of.
- Sect. 5 (Chiral Dirac Determinants) — The spin-structure dependence of the chiral Dirac determinant on a Riemann surface is given by Riemann's theta function.
  Use here: The audit uses this to identify the interior theta factor as the anomaly-carrying norm sector; it is also the natural literature anchor for the corpus's otherwise unsourced one-sentence rem:sign-as-spin-structure, though that remark's object (a ribbon twist sign on sqrt(q)) is not the same object and should not be conflated with a determinant line bundle.

Source: `library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
