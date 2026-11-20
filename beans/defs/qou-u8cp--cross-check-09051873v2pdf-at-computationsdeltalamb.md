---
# qou-u8cp
title: Cross-check 0905.1873v2.pdf at computations/deltalambda/mu4_vs_nuclear_4n_force_bound_probe.py
status: todo
pr: 8404
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8hur
---

The Lean bound uses 0.300 MeV as 'the N3LO four-nucleon estimate'; the paper says 'of order a few hundred keV' (a range, sourced to its own Ref. [20]) and separately measures 50 keV for the SRG-INDUCED four-body force. Confirm the probe is using the intended one of the two numbers and record which, since the 34x factor depends on it.

**From the source**
- p.3, col.2 (discussion of Fig. 3/4, lambda-dependence) — SRG-induced short-range four-body forces contribute about 50 keV net to the 4He ground-state energy at lambda = 2 fm^-1; the long-ranged N3LO four-nucleon contribution to 4He binding is estimated at a few hundred keV.
  Use here: The external numeric ceiling on genuine four-body physics in A = 4 that mu4_target_exceeds_n3lo_bound certifies the corpus target exceeds. It is what turns 'mu_4 = -4.591 is large' into a falsifiable scope-(a) statement about the C(A,k) basis rather than about the operator.

Source: `library/arxiv-0905.1873v2/0905.1873v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0905.1873v2/  ->  [jurgenson2009srg]
  Evolution of nuclear many-body forces with the similarity renormalization group

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [jurgenson2009srg] as the citation key when you do it.

In-progress in PR #8404 (`feat/qou-t8mi-tcgv-tiwv-u33z-u8cp-round68`, `QOU.QBeta.PoincareFalseThetaDilogPentagonRound68`, 80-dps probe `round68_poincare_false_theta_dilog_pentagon_probe.py`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8404, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
