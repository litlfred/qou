---
# qou-7q3s
title: Cross-check 0401068v1 (1).pdf at computations/aj_masbaum_crosscheck.py
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:44Z
updated_at: 2026-11-20T16:06:50Z
pr: 8325
parent: qou-8hur
---

Cross-check the QOU 4_1 / trefoil colored-Jones towers against Takata's rearranged Masbaum normalisation (eqs. 1-5) as an independent second transcription; the script's docstring documents a prior mis-attribution in exactly this area.

**From the source**
- eqs. (1)-(2) and (3)-(5) — Masbaum's colored Jones formula for the twist knot K_p, J_{K_p}(n) = sum_k C_{K_p}(k) {n-k}...{n+k}/{n} with C_{K_p}(k) explicit, rearranged so that the summand F(n,k,l) has closed-form ratios f_0 = F(n+1,k,l)/F(n,k,l), f_1 = F(n,k+1,l)/F(n,k,l), f_2 = F(n,k,l+1)/F(n,k,l).
  Use here: An independently published transcription of the same twist-knot coefficients that computations/aj_masbaum_crosscheck.py checks the QOU 4_1 and trefoil towers against, in a different normalisation — so agreement is a genuine second witness against transcription error, which that script's docstring shows is a real failure mode here.
- eq. (16), §4 — Explicit evaluation hat-J_{K_p}(n) of the twist-knot colored Jones at q = exp(2 pi i / n), stated for the volume conjecture 2 pi lim (log|hat-J_K(n)|/n) = Vol(M_K).
  Use here: A directly runnable formula for the Kashaev/volume-conjecture asymptotic on 4_1 = K_{-1}, whose Vol(4_1) = 2 Lambda(pi/3) is the CAL-2 numerical anchor. A finite-n numeric cross-check of Vol(4_1) from this formula is a falsifiable compute-check; it must NOT be used to adopt or re-derive the anchor value.

Source: `library/arxiv-math-0401068v1/0401068v1 (1).pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0401068v1/  ->  [takata2004]
  THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [takata2004] as the citation key when you do it.

### Progress (Round 61)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8325 (`5b31e8e9599f35d940975c6c2937ae31bf0eaa65`). Status kept `in-progress` pending PR merge.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8325, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
