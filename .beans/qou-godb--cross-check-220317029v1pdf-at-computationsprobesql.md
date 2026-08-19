---
# qou-godb
title: Cross-check 2203.17029v1.pdf at computations/probes/qlift_routeB_connection_matrix_probe.py
status: todo
type: task
created_at: 2026-08-08T16:13:19Z
updated_at: 2026-08-08T16:13:19Z
---

The empirical theta-growth q^{m^2/4} recorded for the GGM connection matrix should be checked against the closed-form theta-quotient monodromy entries of Thm 1.6/1.7 rather than left as a numeric observation. This is a cross-check to run, not a number to adopt.

**From the source**
- Thm 1.6(a) and Thm 1.7(a) (Sec 1.5) — For the Chern-Simons q-holonomic modules the monodromy matrix M(t,lambda,mu,q)=V^{-1}U is unipotent (resp. -1/1 diagonal) with the single non-trivial entry M_{2,1} an explicit ratio/product of Jacobi theta functions theta(qt;q)theta(t*lambda;q)....
  Use here: Gives a closed-form theta-function expression for the connection/monodromy matrix entries in exactly the class the qlift Route-B probe measured numerically as 'connection-matrix theta-growth q^{m^2/4}'. The probe's empirical growth exponent can be checked against these theta entries instead of being left as a numeric observation.

Source: `library/arxiv-2203.17029v1/2203.17029v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
