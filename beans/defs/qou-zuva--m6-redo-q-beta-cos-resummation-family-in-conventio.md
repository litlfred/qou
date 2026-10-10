---
# qou-zuva
title: 'M6: redo q-beta-cos-resummation family in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:08Z
updated_at: 2026-10-10T09:01:50Z
parent: qou-d8c7
---

nuclear-interactions/q-beta-cos-resummation.md:8,12 and table data use z_C; residual +305.7 ppm is C-measured (6 users). Overlaps qou-cds1. Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: redone in D on PR #7562 (subagent, reviewed). Ruled base 0.4447004085 MeV (-431571.8 ppm); cos factor 0.99918 makes it worse (-432037.5 ppm), forced since cos<=1 and F_required>1. Form A historical: +1677.6 -> +856.8 ppm with D phase (was 5.49x under C, now 1.96x). Bar-evenness argument for the cosine fails under D (z_D(1/q) != z_D(q)), so cosine is now a tested definition, not derived. OPEN: Lean sibling still markovZC (eigenphase_bar_involution false under D); downstream eps_DeltaS 1015->185 ppm still C; no D producer/witness (computation field points at old producer). Stays open.
