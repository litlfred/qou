---
# qou-7xvy
title: 'b/c: Φ_b divisor rigidity (no elliptic freedom) — discharge hr_entire via PhiBProd'
status: in-progress
type: task
priority: normal
created_at: 2026-07-19T03:14:45Z
updated_at: 2026-07-25T21:48:41Z
---

INPUT 1 CLOSED (PR #4296, PhiBProdProductConvergence.lean): phiBProd meromorphic unconditionally on Im b²>0. Both routes (divisor hr_entire / boundedness hbdd) now reduce to the SAME sole open input: the Φ_b divisor-rigidity / state-integral growth estimate (Écalle–Borel contour integration) — a Mathlib infra gap (no contour-integration API). Ratio double-periodicity (ratio_ib/ibinv_periodic), period basis (exists_period_basis), localization (DoublyPeriodicBoundedLocalization), and the conditional assembly (PhiBProdUniquenessAssembly #4232) are all in place. Remaining = the growth estimate itself. See docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md.
