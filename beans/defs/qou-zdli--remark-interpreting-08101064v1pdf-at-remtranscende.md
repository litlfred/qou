---
# qou-zdli
title: Remark interpreting 0810.1064v1.pdf at rem:transcendental-accounting
status: todo
pr: 8440
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:57Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-aqfj
---

The transcendental-accounting ledger indexes periods by Goncharov depth but records no dimension bound on the span at a given weight/level. A remark recording D(w,N) as the available upper bound — and Zhao's warning that the standard relations do not exhaust the relations at level 4 — makes the ledger's independence claims auditable rather than asserted.

**From the source**
- Proposition 1 (= [Deligne-Goncharov, 5.25]), §1 — d(w,N) <= D(w,N), where the D(w,N) are the coefficients of an explicit generating function depending only on Euler's totient phi(N) and the number of prime factors nu(N).
  Use here: A closed-form upper bound on the number of Q-independent polylog constants of weight w at level N. This is a formalize-first prune of exactly the kind AGENTS.md mandates before a wide search: any PSLQ or closed-form hunt over polylog values at roots of unity (the Lambda(pi/3), Lambda(pi/4), Li_2 at cyclotomic points that populate the transcendental-accounting table) has its basis size bounded a priori by D(w,N), so an over-large candidate basis is refutable on entropy grounds before it is run.
- eq. (2) + §1 'Fact (*)', level 4 weight 3 — There is an explicit Q-linear relation among weight-3, level-4 MPVs (5*Li_{1,2}(-1,-i) = ... , nine terms) that does NOT follow from the standard relations; it is derived instead from the octahedral symmetry of P^1 - ({0, infinity} U mu_4).
  Use here: A concrete counterexample to 'the standard relation set is complete' at exactly the level (4) where the corpus's Catalan/Lambda(pi/4) values live. It supports the ledger's own distinction between relations forced by structure and relations that appear only after archimedean realization — here a genuine extra relation arises from a SYMMETRY (octahedral), not an accident, which is the ledger's Fact-2 mechanism in a different guise.

Source: `library/arxiv-0810.1064v1/0810.1064v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0810.1064v1/  ->  [zhao2008-mpl-roots-of-unity]
  Multiple polylogarithm values at roots of unity

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [zhao2008-mpl-roots-of-unity] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8440, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
