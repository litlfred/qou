---
# qou-wkai
title: Cite 0604094v1.pdf at prop:phi-q-aj-machinery-identification
status: todo
pr: 8425
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:44Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-ysb7
---

prop:phi-q-aj-machinery-identification asserts the Phi_q to A-polynomial/AJ correspondence; this document derives the A-polynomial from the potential obtained as the classical limit of the quantum-dilogarithm state sum, which is the published form of that correspondence.

**From the source**
- abstract + §1 — For a cusped hyperbolic 3-manifold, the quantum invariant built by assigning the quantum dilogarithm to each ideal tetrahedron has the Neumann-Zagier potential function as its classical limit, and the A-polynomial is derived from that potential.
  Use here: Supplies a published derivation of the potential-from-quantum-dilogarithm link that the Phi_q / AJ identification asserts, and a literature anchor for the deformed-cusp (u-parameter) setting the shared-denominator conjecture works in.

Source: `library/arxiv-math-0604094v1/0604094v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0604094v1/  ->  [hikami2006]
  Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [hikami2006] as the citation key when you do it.


## Implementation Progress (PR #8425)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/PadicPolylogSelfReciprocalVortexPotentialRound71.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round71_padic_polylog_self_reciprocal_vortex_potential_probe.py` with 2-commit witness `computations/probes/round71-padic-polylog-self-reciprocal-vortex-potential.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8425 (`ready: e9a0477369d852fec1b713ba0fbbc441b552fa75`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8425, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
