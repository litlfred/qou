---
# qou-t8mi
title: Cross-check 04procbryden.pdf at computations/probes/keystone_colored_sigma235_wrt.py
status: in-progress
pr: 8404
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:10:44Z
updated_at: 2026-11-18T15:18:15Z
parent: qou-8hur
---

Cross-check the probe's Psi(q) = sum chi(n) q^{n^2/120} against this paper's q(q-1) Z_inf = 1 - (1/2) sum chi(n) q^{(n^2-1)/120}. The support set agrees (independent confirmation); the exponent offset q^{-1/120} and the q(q-1) prefactor do not obviously agree, and they move the operational Psi(1/q0) = 2.32958 in the fourth digit. A disagreement is a normalisation bug in the transcription; an agreement is an independent confirmation. Either way the external number is never adopted — only compared.

**From the source**
- Section 1, p. 55 — q(q-1) Z_inf(Sigma(2,3,5))(q) = 1 - (1/2) sum_{n>=1} chi(n) q^{(n^2-1)/120}, where chi : Z/60Z -> {-1,0,1} is odd and takes the value +1 precisely at 1, 11, 19, 29 and nowhere else.
  Use here: Independently confirms the support set {1,11,19,29} that computations/probes/keystone_colored_sigma235_wrt.py hardcodes, and simultaneously pins the exponent normalisation as (n^2-1)/120 — which makes every exponent an integer (n=1,11,19,29 give 0,1,3,7) — whereas that probe uses Psi(q) = sum chi(n) q^{n^2/120}. The two differ by an overall q^{-1/120}; at the probe's evaluation point that is a factor ~1.00088, i.e. it moves the operational number Psi(1/q0) = 2.32958 in its fourth significant digit. This is a normalisation cross-check to run, not a number to adopt.
- Section 4.3, p. 65 — Defines the slope sigma(M) = lim_{n->inf} lambda_n(M) / (n lambda_{n-1}(M)); cites Lawrence-Rozansky that the slope exists for Seifert fibred manifolds and equals sigma(Sigma(Q_1/P_1,...,Q_N/P_N)) = ±P/pi^2 = ±(1/pi^2)(sum_i Q_i/P_i)^{-1}, so pi^2 sigma(M) is in Q for such manifolds and in Z when they are additionally integer homology spheres.
  Use here: For Sigma(2,3,5) both readings of P give |pi^2 sigma| = 30 = p1 p2 p3, the same 30 the keystone's McKay 2I <-> affine E8 derivation uses as h(E8) = sum of Coxeter marks (docs/coordination/s5-so3-keystone.md, 2026-07-12 row). So the growth rate of the perturbative coefficients is that same P: lambda_n grows like (30/pi^2)^n n!, i.e. Z_inf(Sigma(2,3,5)) is Gevrey-1 with zero radius of convergence. That is a quantitative reason why the keystone's h = q-1 expansion cannot simply be evaluated at the substrate (h_0 ~ 0.11) and why the bar-involution route into the disk (q -> 1/q, where the false theta converges) is the correct one — it corroborates a route the ledger already chose, and supplies the divergence rate the ledger currently does not record.

Source: `library/04procbryden/04procbryden.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/04procbryden/  ->  [jacoby-lawrence2004]
  Some computations of Ohtsuki series

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [jacoby-lawrence2004] as the citation key when you do it.

In-progress in PR #8404 (`feat/qou-t8mi-tcgv-tiwv-u33z-u8cp-round68`, `QOU.QBeta.PoincareFalseThetaDilogPentagonRound68`, 80-dps probe `round68_poincare_false_theta_dilog_pentagon_probe.py`).
