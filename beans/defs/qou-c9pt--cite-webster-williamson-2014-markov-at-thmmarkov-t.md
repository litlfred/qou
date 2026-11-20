---
# qou-c9pt
title: Cite [webster-williamson-2014-markov] at thm:markov-trace-factorization
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:55Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-mub3
---

The reference currently sits in rem:hecke-markov-interpretation's cites array with no prose invocation. Move it to the block whose claim it actually bears on — the character expansion of the Markov trace — and cite Cor. 13 there with its locator.

**From the source**
- Cor. 13 — The geometric trace expands over irreducible characters as Tr(x) = sum_chi chi_q(x) * {chi, nu} * M_nu(q,t), where {chi,nu} are Lusztig Fourier-transform matrix coefficients and M_nu is the mixed Poincare polynomial of the corresponding character sheaf.
  Use here: An independent, geometric identification of the character weights in the Markov-trace expansion tr_M = sum_lambda y_lambda chi_lambda — a second route to the y_lambda that does not go through Wedderburn.
- Thm 6 — The trace Tr(C'_w) = dim_{q,t} H*_{B_Delta}(IC_w) depends only on the root system, and agrees with the trace defined independently by Gomi.
  Use here: Supplies the well-definedness context for treating the Markov trace as a root-system-level invariant rather than a type-A accident.

Source: `library/arxiv-0911.4494v2/0911.4494v2.pdf` (`webster-williamson-2014-markov`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8486, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
