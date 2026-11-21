---
# qou-fs87
title: Cite 0304010v1.pdf at prop:q-plancherel-asymptotic-skeleton
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:38Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

prop:q-plancherel-asymptotic-skeleton clause (2) cites feray2010 ('Stanley's formula for characters') for a fluctuation/variance claim that paper does not make; the q = 1 CLT source belongs here.

**From the source**
- Introduction, eqs. (0.1)-(0.4); proved in §7 — Kerov's CLT: for lambda drawn from Plancherel measure M_n, the rescaled boundary satisfies n^{-1/2} lambda(sqrt(n) x) ~ Omega(x) + (2/sqrt(n)) Delta(x), with Omega(x) = (2/pi)(x arcsin(x/2) + sqrt(4 - x^2)) on |x| <= 2 and Delta a generalized Gaussian process given by the random trigonometric series Delta(2 cos theta) = (1/pi) sum_{k>=2} (xi_k/sqrt(k)) sin(k theta), xi_k i.i.d. standard normal.
  Use here: Supplies the actual q = 1 fluctuation theorem — including the exact 1/sqrt(n) scale — that conj:jet-convergence-classical-limit's O(1/sqrt(k)) claim and prop:q-plancherel-asymptotic-skeleton clause (2) are asserting a q-analogue of. Replaces a citation (feray2010) that does not state a CLT.
- §6 (CLT for characters) — Central limit theorem for normalized character values on cycles: character ratios evaluated on cycles of different lengths are asymptotically independent Gaussians with explicit variances.
  Use here: This is the precise q = 1 form of prop:q-plancherel-asymptotic-skeleton clause (2)'s 'character fluctuations have variance O(...)'; the asymptotic independence across cycle lengths is additional structure the corpus block does not currently record and which any q-deformed statement would have to reproduce or break.
- §10 (free cumulants and Biane's theorem); §3-§4 (the p#_k basis and filtrations in A) — The proof is organised through the algebra of polynomial functions on Young diagrams, the elements p#_k, and free cumulants, connecting to Biane's asymptotic character theory.
  Use here: rem:non-commutative-probability-dictionary already frames the Hecke GNS data in free-probability terms; §10 gives the bridge between the Plancherel CLT and the free-cumulant language the corpus uses, so a q-deformed statement can be posed in the corpus's own coordinates.

Source: `library/arxiv-math-0304010v1/0304010v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0304010v1/  ->  [ivanov-olshanski2003]
  Kerov's central limit theorem for the Plancherel measure on Young diagrams

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [ivanov-olshanski2003] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8499, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — expo-cite-xcheck drain

Premise stale: the feray2010 fluctuation claim is gone from prop:q-plancherel-asymptotic-skeleton, and conj:jet-convergence-classical-limit already cites [ivanov-olshanski2003] §7. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.
