---
# qou-wupb
title: Remark interpreting 04procbryden.pdf at docs/coordination/s5-so3-keystone.md
status: todo
pr: 8431
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:10:44Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-aqfj
---

Record in the keystone ledger that the Ohtsuki series of Sigma(2,3,5) is Gevrey-1 with slope pi^2 sigma = ±30 = P = h(E8), so the h-expansion has zero radius of convergence and the bar-involution route into the disk is forced rather than merely convenient. This interprets an external result for the folio; it does not discharge any Lean hypothesis, so it is a remark and not an aid-proof.

**From the source**
- Section 4.3, p. 65 — Defines the slope sigma(M) = lim_{n->inf} lambda_n(M) / (n lambda_{n-1}(M)); cites Lawrence-Rozansky that the slope exists for Seifert fibred manifolds and equals sigma(Sigma(Q_1/P_1,...,Q_N/P_N)) = ±P/pi^2 = ±(1/pi^2)(sum_i Q_i/P_i)^{-1}, so pi^2 sigma(M) is in Q for such manifolds and in Z when they are additionally integer homology spheres.
  Use here: For Sigma(2,3,5) both readings of P give |pi^2 sigma| = 30 = p1 p2 p3, the same 30 the keystone's McKay 2I <-> affine E8 derivation uses as h(E8) = sum of Coxeter marks (docs/coordination/s5-so3-keystone.md, 2026-07-12 row). So the growth rate of the perturbative coefficients is that same P: lambda_n grows like (30/pi^2)^n n!, i.e. Z_inf(Sigma(2,3,5)) is Gevrey-1 with zero radius of convergence. That is a quantitative reason why the keystone's h = q-1 expansion cannot simply be evaluated at the substrate (h_0 ~ 0.11) and why the bar-involution route into the disk (q -> 1/q, where the false theta converges) is the correct one — it corroborates a route the ledger already chose, and supplies the divergence rate the ledger currently does not record.
- Section 4.2, p. 64-65 — Z_K(Mbar)(q) = Z_K(M)(q^{-1}) at all roots of unity, hence Z_inf(Mbar) is obtained from Z_inf(M) by q -> q^{-1}, i.e. h -> -h/(1+h); together with lambda_1 = 6 lambda_Casson and explicit degree-2m polynomials for lambda_m(S,T).
  Use here: States the q -> q^{-1} bar involution at the level of the 3-manifold WRT/Ohtsuki series itself, which is exactly the involution the keystone uses to move from q0 ~ 1.10998 to 1/q0 ~ 0.901. Gives the keystone's bar step a literature statement at the right level of generality (manifold invariant, not just the false theta), and supplies the orientation-reversal bookkeeping any lambda_n cross-check needs.

Source: `library/04procbryden/04procbryden.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/04procbryden/  ->  [jacoby-lawrence2004]
  Some computations of Ohtsuki series

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [jacoby-lawrence2004] as the citation key when you do it.


## Implementation Progress (PR #8431)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/AnisotropicContentHelicityOhtsukiQBorelRound72.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round72_anisotropic_content_helicity_ohtsuki_qborel_probe.py` with 2-commit witness `computations/probes/round72-anisotropic-content-helicity-ohtsuki-qborel.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8431 (`ready: 9f16804370f4cb20ca3c9ba012e7448a071f0f7c`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8431, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
