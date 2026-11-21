---
# qou-otpa
title: Cite 0811.1338v1.pdf at computations/deltalambda/mu4_vs_nuclear_4n_force_bound_probe.py
status: in-progress
pr: 8386
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:58Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

Once registered, the bare-string citations in the probe and the witness's sources list should become the bib key, so validate-bib can see them and the Lean -- Ref: convention (§1) is satisfiable for the Tjon/4N-force claims.

**From the source**
- §II.B, eq. (2.8) and the discussion on p.13 — Weinberg power counting: two-, three-, and four-nucleon forces begin to contribute at orders nu = 0, 2 and 4 respectively — a derived hierarchy of many-body force strengths from the Q/Lambda expansion, not a fit.
  Use here: A parameter-free external benchmark for the size ordering of the k-body terms in the residual-simplex expansion (mu_3, mu_4). The corpus target mu_4 = -4.591 in B(D) units is compared against it in the GAP-9 probe; the hierarchy is what makes that comparison meaningful rather than an arbitrary scale check.
- §II.A, Fig. 10 and surrounding text, p.12 — The Tjon line — the correlation between triton and alpha binding energies B_t and B_alpha — is predicted by pionless EFT because no four-body parameter is required for renormalization at leading order; higher orders broaden it into a band.
  Use here: Supplies the convention-free observable the GAP-9 probe reformulates the test around: instead of matching mu_4 in a C(A,k) basis, test the QOU block-trace operator against the B(3H)-B(4He) correlation. The Fig.-10 band gives the tolerance that test must meet.

Source: `library/arxiv-0811.1338v1/0811.1338v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0811.1338v1/  ->  [epelbaum2008]
  Modern theory of nuclear forces

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [epelbaum2008] as the citation key when you do it.

## Progress (2026-11-18, PR #8386)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`dc2e35b36f4ebb7e9b1575a73bdbe33cb67ee130`, `scriptHash: 2ebaf0631eb0504b9d6d5bd79a3a8425d49d4ffed0fadf6b52c241edb18846dc`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8386`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8386, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — expo-cite-xcheck drain

Bare strings in mu4_vs_nuclear_4n_force_bound_probe.py and its witness references now carry `[jurgenson2009srg]` / `[epelbaum2008]`; probe re-run, numbers byte-identical. Completes on merge. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): see qou-u8cp (empirical number inside a Lean theorem).

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.
