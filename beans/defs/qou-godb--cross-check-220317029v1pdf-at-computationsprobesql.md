---
# qou-godb
title: Cross-check 2203.17029v1.pdf at computations/probes/qlift_routeB_connection_matrix_probe.py
status: todo
pr: 8355
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:19Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8hur
---

The empirical theta-growth q^{m^2/4} recorded for the GGM connection matrix should be checked against the closed-form theta-quotient monodromy entries of Thm 1.6/1.7 rather than left as a numeric observation. This is a cross-check to run, not a number to adopt.

**From the source**
- Thm 1.6(a) and Thm 1.7(a) (Sec 1.5) — For the Chern-Simons q-holonomic modules the monodromy matrix M(t,lambda,mu,q)=V^{-1}U is unipotent (resp. -1/1 diagonal) with the single non-trivial entry M_{2,1} an explicit ratio/product of Jacobi theta functions theta(qt;q)theta(t*lambda;q)....
  Use here: Gives a closed-form theta-function expression for the connection/monodromy matrix entries in exactly the class the qlift Route-B probe measured numerically as 'connection-matrix theta-growth q^{m^2/4}'. The probe's empirical growth exponent can be checked against these theta entries instead of being left as a numeric observation.

Source: `library/arxiv-2203.17029v1/2203.17029v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2203.17029v1/  ->  [garoufalidis-wheeler-modular]
  Modular q-holonomic modules

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis-wheeler-modular] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8355, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
