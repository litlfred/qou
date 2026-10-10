---
# qou-z2ma
title: 'G5: growth => hbdd wiring => faddeevPhi_proportional_of_bounded_ratio'
status: completed
type: task
priority: normal
created_at: 2026-07-26T01:17:32Z
updated_at: 2026-07-26T12:15:54Z
blocked_by:
    - qou-zt8v
---

G5 nearly closed for concrete phiBProd. faddeevPhi_proportional_of_stripGrowth (hbdd derived) + phiBProd_uniqueUpToScalar_of_stripGrowth (PhiBProdUniquenessFinal.lean) now discharge hΦ₂_iso via PhiBProdZeroIsolation.phiBProd_eventually_ne_zero (zeros isolated: products entire + z=0 non-vanishing witness + order != top + meromorphicOrderAt_ne_top_iff_eventually_ne_zero). REMAINING carried inputs: hr_ratio (normal-form identity off zeros) + density of the two periodicity loci -- both gated on the same phiBProd zero-discreteness now available, dischargeable by the normal-form API + a Baire/codiscrete density argument. Both hbdd and hΦ₂_iso are now theorems.
