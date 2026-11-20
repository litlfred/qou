---
# qou-r0fd
title: Cross-check 1811.05376v4.pdf at computations/qbeta/qbeta_c3_borel_pade_resummation_probe.py
status: todo
pr: 8386
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:24Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-mukd
---

The corpus's Borel-Pade probe locates a singularity at A = Vol(4_1)/pi ~ 0.646; Thm 2 says (in its own class) such singularities are exactly complex-CS actions. Cross-checking the probe's numerically located singularity against the 4_1 complex-CS spectrum is a cross-check to run, not a number to adopt.

**From the source**
- Thm. 3 — Z-hat_0(X;q) is a Borel-Laplace resummation of the Ohtsuki series Z_0(X), with a full asymptotic expansion as q -> exp(2 pi i / k) recovering the WRT invariant tau_k(X).
  Use here: The resummation-side template for the corpus's open multi-instanton / median-resummation residual on the one-instanton normalization (the quantitatively open leg of the u(q_0) map).

Source: `library/arxiv-1811.05376v4/1811.05376v4.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1811.05376v4/  ->  [andersen-mistegard2020]
  Resurgence analysis of quantum invariants of Seifert fibered homology spheres

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [andersen-mistegard2020] as the citation key when you do it.

## Progress (2026-11-18, PR #8386)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`dc2e35b36f4ebb7e9b1575a73bdbe33cb67ee130`, `scriptHash: 2ebaf0631eb0504b9d6d5bd79a3a8425d49d4ffed0fadf6b52c241edb18846dc`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8386`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8386, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
