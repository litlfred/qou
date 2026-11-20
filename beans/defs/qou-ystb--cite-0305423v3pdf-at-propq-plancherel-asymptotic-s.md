---
# qou-ystb
title: Cite 0305423v3.pdf at prop:q-plancherel-asymptotic-skeleton
status: todo
pr: 8440
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:42Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-19m0
---

Clause (2) of prop:q-plancherel-asymptotic-skeleton asserts a fluctuation rate with no rate-bearing source; Thm 1.2 is the q = 1 explicit rate.

**From the source**
- Thm 1.2 — For n >= 2 and all real x_0, |P(((n-1)/sqrt(2)) chi^lambda(12)/dim(lambda) <= x_0) - Phi(x_0)| <= 40.1 n^{-1/4}, with a conjectured C n^{-1/2}.
  Use here: The only explicit Berry-Esseen rate for the Plancherel character-ratio CLT. Gives a concrete q = 1 number against which the corpus's asserted O(1/sqrt(k)) / O(1/sqrt(n-3)) rates can be sanity-checked, and shows the best proved distributional rate is n^{-1/4}, not n^{-1/2} — which is weaker than what the corpus's prose implies.

Source: `library/arxiv-math-0305423v3/0305423v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0305423v3/  ->  [fulman2003]
  Stein's method and Plancherel measure of the symmetric group

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [fulman2003] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8440, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
