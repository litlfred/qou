---
# qou-7xvy
title: 'b/c: Φ_b divisor rigidity (no elliptic freedom) — discharge hr_entire via PhiBProd'
status: in-progress
pr: 8230
updated_at: 2026-11-17T06:37:48Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T03:14:45Z
updated_at: 2026-10-04T15:11:56Z
parent: qou-r9ih
---

INPUT 1 CLOSED (PR #4296, PhiBProdProductConvergence.lean): phiBProd meromorphic unconditionally on Im b²>0. Both routes (divisor hr_entire / boundedness hbdd) now reduce to the SAME sole open input: the Φ_b divisor-rigidity / state-integral growth estimate (Écalle–Borel contour integration) — a Mathlib infra gap (no contour-integration API). Ratio double-periodicity (ratio_ib/ibinv_periodic), period basis (exists_period_basis), localization (DoublyPeriodicBoundedLocalization), and the conditional assembly (PhiBProdUniquenessAssembly #4232) are all in place. Remaining = the growth estimate itself. See docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR #8230)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8230` at `1bb9d799f645494190e9e4834f3982913ab5e918`).
- **Lean Formalization**: `QOU.QBeta.PentagonTwoRouteAndC1RamifiedStokesBrick.phi_b_prod_divisor_rigidity_exponential_elimination` (Divisor rigidity exponential elimination for doubly-periodic quadratic log ansatz across 0 -> w1 -> 2*w1.)
- **80-dps Witness**: `computations/probes/pentagon-two-route-and-c1-ramified-stokes-brick.witness.json` (`scriptHash: ad15e8ab2a08`, `scriptCommitSha: 4eaeef60b72e32fbaaef92149ff8588e4dde4090`).
