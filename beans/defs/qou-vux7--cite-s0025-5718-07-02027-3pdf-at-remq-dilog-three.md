---
# qou-vux7
title: Cite S0025-5718-07-02027-3.pdf at rem:q-dilog-three-contexts
status: completed
pr: 8425
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:15Z
updated_at: 2026-11-21T13:32:29Z
parent: qou-ysb7
---

rem:q-dilog-three-contexts asserts a truncated F_p form and convergent Q_p / C_p forms of the q-dilogarithm with no citation; the computational p-adic polylogarithm side belongs there alongside the finite/p-adic bridge already proposed in the ledger for the companion article.

Source: `library/s0025-5718-07-02027-3/S0025-5718-07-02027-3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/s0025-5718-07-02027-3/  ->  [besser-dejeu2008]
  Li(p)-service? An algorithm for computing p-adic polylogarithms

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [besser-dejeu2008] as the citation key when you do it.


## Implementation Progress (PR #8425)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/PadicPolylogSelfReciprocalVortexPotentialRound71.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round71_padic_polylog_self_reciprocal_vortex_potential_probe.py` with 2-commit witness `computations/probes/round71-padic-polylog-self-reciprocal-vortex-potential.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8425 (`ready: e9a0477369d852fec1b713ba0fbbc441b552fa75`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8425, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

rem:q-dilog-three-contexts now cites besser-dejeu2008 §2 Thm 2.7 (Coleman) and §§3-4 (algorithm).

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.

PR #8828 merged 2026-11-21 (rebased onto main as a8b394e108). Completed.
