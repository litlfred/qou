---
# qou-5k23
title: Cite 0304010v1.pdf at conj:jet-convergence-classical-limit
status: todo
type: task
priority: normal
created_at: 2026-08-08T16:12:39Z
updated_at: 2026-08-21T17:04:42Z
---

conj:jet-convergence-classical-limit's prose names a 'Feray-Meliot q-Plancherel Central Limit Theorem' but cites feray2010 + kerov1996; the named q-CLT paper is absent from references.ts and the q = 1 antecedent is uncited. Add this and verify the Feray-Meliot citation separately.

**From the source**
- Introduction, eqs. (0.1)-(0.4); proved in §7 — Kerov's CLT: for lambda drawn from Plancherel measure M_n, the rescaled boundary satisfies n^{-1/2} lambda(sqrt(n) x) ~ Omega(x) + (2/sqrt(n)) Delta(x), with Omega(x) = (2/pi)(x arcsin(x/2) + sqrt(4 - x^2)) on |x| <= 2 and Delta a generalized Gaussian process given by the random trigonometric series Delta(2 cos theta) = (1/pi) sum_{k>=2} (xi_k/sqrt(k)) sin(k theta), xi_k i.i.d. standard normal.
  Use here: Supplies the actual q = 1 fluctuation theorem — including the exact 1/sqrt(n) scale — that conj:jet-convergence-classical-limit's O(1/sqrt(k)) claim and prop:q-plancherel-asymptotic-skeleton clause (2) are asserting a q-analogue of. Replaces a citation (feray2010) that does not state a CLT.

Source: `library/arxiv-math-0304010v1/0304010v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0304010v1/  ->  [ivanov-olshanski2003]
  Kerov's central limit theorem for the Plancherel measure on Young diagrams

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [ivanov-olshanski2003] as the citation key when you do it.
