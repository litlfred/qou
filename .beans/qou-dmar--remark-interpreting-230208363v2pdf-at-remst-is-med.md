---
# qou-dmar
title: Remark interpreting 2302.08363v2.pdf at rem:st-is-median-resummation
status: todo
type: task
priority: normal
created_at: 2026-08-09T00:10:48Z
updated_at: 2026-08-21T17:04:53Z
---

rem:st-is-median-resummation asserts st = L^med as an identity of two selection rules for a transseries, justified by one-series uniqueness (Watson/Nevanlinna-Sokal) on the analytic side. A remark should record that for a transseries the identification additionally needs the sum over sectors to converge, cite the partial-series criterion, and note the 4_1 case where that convergence is argued (radius 1) rather than proved. What would need checking before any stronger claim: whether the QOU substrate transseries actually satisfies the eq (2.8) growth with a common radius.

**From the source**
- Sec 2, eqs (2.5)-(2.8) — The Borel-resummed trans-series s_pm(Phi) = sum_l y^l s_pm(phi_l)(g) is itself an infinite sum over non-perturbative sectors and is a potential new source of divergence; reorganising by fixed power n of the coupling gives the partial series G_n(y) = sum_l a_{n,l} y^l, and convergence of the G_n with a common radius R (eq 2.8) is the property that makes the resummed trans-series a well-defined function.
  Use here: Supplies the second-stage premise that def:ecalle-borel-resummation does not define and rem:st-is-median-resummation silently uses. That remark identifies st(f~|_eps) with L^med(f~) for a transseries f~, citing Watson/Nevanlinna-Sokal uniqueness -- which is a one-series statement. The sum over sectors is a separate convergence question, and this gives the vocabulary (partial series, common radius R) to state it.
- Sec 4, eqs (4.1)-(4.3), (4.8)-(4.10) — For the figure-eight complement the Andersen-Kashaev invariant I(tau) is written as a lateral Borel resummation of an explicit trans-series with two complex-instanton towers q~^l exp(-+ V/(2 pi tau)), q~ = exp(-2 pi i / tau), V = 2.029883... the hyperbolic volume, with perturbative series phi_g(tau) = 3^{-1/4}(1 + ...) and phi_c(tau) = phi_g(-tau); the partial series factorise as G^i_n(y) = a_n M_i(y), so the radius-1 convergence of M_{1,2} gives convergence of every partial series, with the same radius for all n.
  Use here: The 4_1 instance of the previous item, at the corpus's own muon anchor and with V = Vol(4_1) as the instanton action. The corpus has a 5_2 analogue (computations/probes/qbeta_5two_median_borel_resummation_probe.py, which records that the substrate ray misses every Stokes ray) but no 4_1 counterpart; this is the published trans-series a 4_1 probe would be written against.

Source: `library/arxiv-2302.08363v2/2302.08363v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2302.08363v2/  ->  [arxiv-2302.08363v2]
  On the structure of trans-series in quantum field theory

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-2302.08363v2] as the citation key when you do it.
