---
# qou-ad5s
title: Cite 2302.08363v2.pdf at def:ecalle-borel-resummation
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:10:48Z
updated_at: 2026-11-20T16:06:50Z
pr: 8325
parent: qou-ysb7
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

### Progress (Round 61)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8325 (`5b31e8e9599f35d940975c6c2937ae31bf0eaa65`). Status kept `in-progress` pending PR merge.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8325, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
