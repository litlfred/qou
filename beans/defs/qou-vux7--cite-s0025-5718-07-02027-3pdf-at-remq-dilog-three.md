---
# qou-vux7
title: Cite S0025-5718-07-02027-3.pdf at rem:q-dilog-three-contexts
status: in-progress
pr: 8425
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:15Z
updated_at: 2026-11-18T10:20:50Z
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
