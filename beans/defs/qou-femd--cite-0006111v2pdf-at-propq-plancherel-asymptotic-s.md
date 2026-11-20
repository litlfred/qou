---
# qou-femd
title: Cite 0006111v2.pdf at prop:q-plancherel-asymptotic-skeleton
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:32Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-19m0
---

Clauses (1)/(2) of the block cite kerov1981 + biane1998 + feray2010; the concentration result they actually lean on is this paper's Thm 1/Thm 2.

**From the source**
- Def. 1.3 + Thm 1 — Defining F^n_{c,delta} as normalized positive-definite psi on S_q with |psi(rho)| <= c_l q^{-l/2} for |rho| = l and |psi(rho sigma) - psi(rho)psi(sigma)| <= delta q^{-l/2} on disjoint supports, every psi in F^n_{c,delta} is (delta + q^{-1})^{1/2}-supported on Young diagrams with |m_l(lambda) - m_l(psi)| <= K(delta + q^{-1})^{1/4} q^{l/2} for l <= n/2.
  Use here: Gives the explicit hypothesis list a q-analogue would need, turning clause (3) of prop:q-plancherel-asymptotic-skeleton from a bare 'converges weakly' conjecture into a checkable programme: exhibit the q-Plancherel weight tilde-w_lambda as arising from a psi satisfying a q-deformed (1)+(2), then the concentration is automatic.
- Thm 2 — Under the same hypotheses, |chi^lambda(rho) - psi(rho)| <= K(delta + q^{-1})^{1/4} q^{-l/2} for all rho with |rho| = l <= n/2 — concentration stated directly on normalized character values.
  Use here: Character-level concentration is the form clause (2) of prop:q-plancherel-asymptotic-skeleton uses ('character fluctuations have variance O(1/sqrt(n-3))'); Thm 2 is the q=1 statement of that shape from a source that actually proves a fluctuation bound, unlike the currently-cited feray2010 (see the 0304010v1 row).

Source: `library/arxiv-math-0006111v2/0006111v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0006111v2/  ->  [biane2000]
  Approximate factorization and concentration for characters of symmetric groups

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [biane2000] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8499, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
