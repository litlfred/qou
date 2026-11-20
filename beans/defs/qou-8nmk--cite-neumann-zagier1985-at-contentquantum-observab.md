---
# qou-8nmk
title: Cite [neumann-zagier1985] at folio/quantum-observable-universe/lean/QOU/Knot/NeumannZagierParit…
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:58Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-mub3
---

Add the 'Lemma 4.1(b)' locator to the bare '-- Ref: [neumann-zagier1985]' lines carrying the parity claim, so the hypothesis class's antecedent is checkable at the citation rather than only in the source.

**From the source**
- Lemma 4.1(b) — In a neighbourhood of the origin v_i = u_i * tau_i(u_1,...,u_h) with tau_i analytic and even in each argument; hence the longitude log-holonomy v is odd in the meridian log-holonomy u and the deformation potential is even.
  Use here: This is the proved invariant behind the scope-(b) exclusion of a geometric-NZ u^3 rung for the Q_beta bar-odd target; it should be the cited locator wherever NeumannZagierEvenPotential is instantiated or discussed.

Source: `library/1-s20-0040938385900047-main/1-s2.0-0040938385900047-main.pdf` (`neumann-zagier1985`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8486, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
