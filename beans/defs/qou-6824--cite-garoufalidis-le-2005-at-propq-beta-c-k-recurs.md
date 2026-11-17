---
# qou-6824
title: Cite [garoufalidis-le-2005] at prop:q-beta-c-k-recursion-from-habiro-q-difference
status: in-progress
pr: 8283
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:56Z
updated_at: 2026-10-04T15:17:33Z
parent: qou-1qhv
---

The recurrence-minimality assumption used by computations/probes/qlift_routeC_homogenized_factor_probe.py has no counterpart in the paper layer. Cite it at the block stating the Habiro q-difference recursion so the assumption is visible at the proposition, not only in a probe docstring.

**From the source**
- Abstract / Thm 1 — The colored Jones function of a knot is q-holonomic: it satisfies a finite set of linear q-difference recursions with polynomial coefficients.
  Use here: Supplies the existence-and-minimality frame the q-lift Route C probe already assumes when it certifies an order-2 inhomogeneous recurrence; a content block stating that recursion should carry it.

Source: `library/0309214v3/0309214v3.pdf` (`garoufalidis-le-2005`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## Round 56 Implementation Progress (PR #8283)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8283 (head `f53a095b5ee34373c44ef4b0b400e85b12af4c1c`, Commit 1 `0e2f86d58bac8f2f07854f3515aabf15d9779cd3`)
- **Lean 4 Module & Theorems:** `QOU/QBeta/StokesDTBpsHolomorphicBlockAndQHolonomicRecurrence.lean` (`garoufalidis_le_q_holonomic_inhomogeneous_homogenisation` citing `[garoufalidis-le-2005]`)
- **80-dps Witness:** `computations/probes/round56-mellor-melvin-bws0-stokes-dt-qholonomic.witness.json` (`scriptHash: d98411981e4d`, `allPassed: true`, `0` raw `float64`)
