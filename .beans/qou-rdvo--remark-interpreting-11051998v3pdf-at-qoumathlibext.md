---
# qou-rdvo
title: Remark interpreting 1105.1998v3.pdf at QOU.MathlibExt.QBesselContiguityRecurrence
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:35:16Z
updated_at: 2026-08-21T17:05:02Z
---

Before citing it anywhere, its Hahn-Exton normalisation must be reconciled with the corpus's convention recorded in the gasper-rahman-2004 note (J_nu(x;q) = x^nu (q^{nu+1};q)_inf/(q;q)_inf . 1phi1(0; q^{nu+1}; q, q x^2)). A connection formula in a different normalisation is not transferable, and adopting one because its numbers look right would be a fit.

**From the source**
- main connection formula; p -> 1^- limit — A connection formula relating the Hahn-Exton q-Bessel function's behaviour at the origin and at infinity, obtained by q-Borel and q-Laplace transformation, together with its confluent limit as the base tends to 1 from below.
  Use here: The corpus's q-Bessel work and its q-Borel/confluence work are currently separate literature legs; this supplies the connection-formula bridge between them, and the explicit base -> 1 limit is the same confluence route BalancedKernelConfluence.lean cites divizio-zhang2009 for. Reading it may sharpen the q-Bessel contiguity/recurrence derivation, though I have NOT checked whether its normalisation matches the corpus's J_nu(x;q) convention — that check is a precondition for any use.

Source: `library/arxiv-1105.1998v3/1105.1998v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1105.1998v3/  ->  [morita2011]
  A Connection Formula of the Hahn-Exton q-Bessel Function

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [morita2011] as the citation key when you do it.
