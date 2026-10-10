---
# qou-q425
title: 'M6: redo rj-canonical-inner-product in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:07Z
updated_at: 2026-10-10T09:01:50Z
parent: qou-d8c7
---

predicted-spectra/rj-canonical-inner-product.md:8 defines tr_M with z = z_C into Q(q^1/2) (4 users). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: restated in D on PR #7562: tr_M into Q(q), z = q^2/[2]_q, d_lambda = sl2 hook-content dim prod[2+c]/[h], w_lambda = d_lambda/[2]^r (sympy-checked n=3, normalisation 1). Form degenerate: radical = classes with >2 rows. OPEN: part (iii) Rosso-Jones not re-verified (antisymmetric eigenvalue sign -q^-1 missing from omega_lambda = q^c). Uniqueness claim in (ii) restricted to the two-row part.
