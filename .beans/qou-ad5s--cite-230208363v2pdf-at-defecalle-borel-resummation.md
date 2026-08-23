---
# qou-ad5s
title: Cite 2302.08363v2.pdf at def:ecalle-borel-resummation
status: todo
type: task
priority: normal
created_at: 2026-08-09T00:10:48Z
updated_at: 2026-08-21T17:04:48Z
---

def:ecalle-borel-resummation defines the Borel transform, lateral sums, Stokes rays and the median average for a single Gevrey-1 series, and never mentions the sum over non-perturbative sectors. Its eqs (2.5)-(2.8) are the natural citation for that second layer.

**From the source**
- Sec 2, eqs (2.5)-(2.8) — The Borel-resummed trans-series s_pm(Phi) = sum_l y^l s_pm(phi_l)(g) is itself an infinite sum over non-perturbative sectors and is a potential new source of divergence; reorganising by fixed power n of the coupling gives the partial series G_n(y) = sum_l a_{n,l} y^l, and convergence of the G_n with a common radius R (eq 2.8) is the property that makes the resummed trans-series a well-defined function.
  Use here: Supplies the second-stage premise that def:ecalle-borel-resummation does not define and rem:st-is-median-resummation silently uses. That remark identifies st(f~|_eps) with L^med(f~) for a transseries f~, citing Watson/Nevanlinna-Sokal uniqueness -- which is a one-series statement. The sum over sectors is a separate convergence question, and this gives the vocabulary (partial series, common radius R) to state it.

Source: `library/arxiv-2302.08363v2/2302.08363v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2302.08363v2/  ->  [arxiv-2302.08363v2]
  On the structure of trans-series in quantum field theory

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [arxiv-2302.08363v2] as the citation key when you do it.
