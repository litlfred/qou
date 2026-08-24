---
# qou-41qf
title: Remark interpreting 2111.04763v2.pdf at QOU.QBeta.StokesQZeroDTCount
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:34:49Z
updated_at: 2026-08-21T17:04:42Z
---

Fourteen QBeta Lean sites cite equations and theorems of arXiv:2012.00062 under the key garoufalidis-gu-marino2021, while references.ts registers that arXiv item under garoufalidis-gu-marino2023peacock. Re-key those sites so the Stokes-constant locators point at the paper that actually contains them.

**From the source**
- abstract — Complete description of the resurgent structure of the Chern-Simons series at the TRIVIAL flat connection for a hyperbolic knot complement, via an extended matrix of (x,q)-series indexed by the boundary-parabolic flat connections including the trivial one; gives an analytic extension of the Kashaev invariant and an exact form of the refined quantum modularity conjecture.
  Use here: The trivial-flat-connection sector is the one the QBeta Stokes modules are missing: the existing citations cover the non-trivial connections, while the framework's q = 0 / centring arguments live precisely at the trivial connection.

Source: `library/arxiv-2111.04763v2/2111.04763v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2111.04763v2/  ->  [garoufalidis2021a]
  RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis2021a] as the citation key when you do it.
