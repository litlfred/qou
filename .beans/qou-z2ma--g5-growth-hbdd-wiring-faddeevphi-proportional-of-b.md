---
# qou-z2ma
title: 'G5: growth => hbdd wiring => faddeevPhi_proportional_of_bounded_ratio'
status: in-progress
type: task
priority: normal
created_at: 2026-07-26T01:17:32Z
updated_at: 2026-07-26T11:28:58Z
blocked_by:
    - qou-zt8v
---

G5 ASSEMBLY DONE (FaddeevStripGrowthUniqueness.lean): faddeevPhi_proportional_of_stripGrowth derives the capstone's hbdd from the strip-growth class (G4) + the removable-singularity extension (G5 crux). The analytic hbdd endowment is ELIMINATED. Remaining to specialize to concrete phiBProd (assembly, no Mathlib gap): (i) hΦ₂_iso via meromorphicOrderAt_ne_top_iff_eventually_ne_zero + #4296/#4225; (ii) hr_ratio via normal-form identity; (iii) honest MeromorphicOn Phi_1. Canonical arc map: docs/audits/2026-07-26-faddeev-keystone-7xvy-canonical-arc.md
