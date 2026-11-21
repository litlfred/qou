---
# qou-godb
title: Cross-check 2203.17029v1.pdf at computations/probes/qlift_routeB_connection_matrix_probe.py
status: completed
pr: 8355
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:19Z
updated_at: 2026-11-21T15:02:16Z
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

## 2026-11-21T15:02:16Z cross-check result

Probe computations/probes/gw_modular_monodromy_vs_routeB_probe.py (branch claude/expo-cite-xcheck-wave2-2026-11-21, head 9aaf050ca84). ALL PASS. The finding is a premise mismatch: the cross-check the bean asks for cannot be made as stated.
- Exact (sympy): the corpus GGM eq 49, z_{m+1} = (2 - q^m) z_m - z_{m-1}, is Garoufalidis-Wheeler's 4_1 module eq (28) with q -> p = 1/q, on the lattice t = p^m, under the diagonal gauge f(p^m) = q^m z_m (factor exactly 1). The source does cover the corpus equation.
- The non-trivial monodromy entries M_21 of Thm 1.6 (eq 25) and Thm 1.7 (eq 31) are q-elliptic in t: M(qt) = M(t) to 3e-49 at q = 2/5. Their growth exponent along any lattice t = q^m t_0 is therefore 0.
- The Route-B witness records gamma_est = 0.274 (q = 1.05) and 0.249 (q = 1.10998) in its asymptotic window. That is the q-Gevrey mismatch between two different recurrences (C1 decays ~ q^{-m^2/4}, eq 49 grows ~ q^{+m^2/2}), as that probe's own Newton-polygon note predicts. It is not a monodromy V^{-1}U of one module.
So the "theta-growth q^{m^2/4}" is not a property the Thm 1.6/1.7 theta entries can confirm or refute. What the source does supply for the corpus is a fundamental matrix pair (U at t = 0, V at t = infinity) for eq 49 itself. That could replace the corpus's raw-initial-data fundamental matrix Y_m in a follow-up; not attempted here.
Harness note: a coding slip in check A (comparing with corpus/q) was fixed after the first run. The statement and thresholds are unchanged, and this is documented as an amendment.
