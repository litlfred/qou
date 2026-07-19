---
# qou-2cvs
title: 'Infra: FaddeevPhi holomorphicity endowment — ratio Ψ/Φ entire (hratio; closes uniqueUpToScalar via the landed reduction)'
status: in-progress
type: task
priority: normal
tags:
    - alien-habiro
created_at: 2026-07-18T18:06:37Z
updated_at: 2026-07-19T00:05:58Z
parent: qou-89f9
---

ROUTE-B STEP 2 FULLY PROVEN (2026-07-18, lean exit 0), QOU/QBeta/MeromorphicSameOrder.lean, against in-sandbox Meromorphic cone:
- BRICK (a) CLOSED: meromorphicOrderAt_comp_add — ord(g∘(·+c)) x = ord g (x+c), translation invariance (was a Mathlib gap). Proved from eq_top_iff/eq_int_iff + AnalyticAt.comp + punctured-nhds Tendsto (tendsto_add_right_nhdsWithin_ne, meromorphicAt_comp_add[_iff] helpers). Sorry-free.
- meromorphicOrderAt_sharedPrefactor_balance (prefactor cancels).
- meromorphicOrderAt_orderDiff_periodic — UNCONDITIONAL order-difference periodicity (brick a discharges the translation input). Route-B step 2 complete.
REMAINING BRICKS (honest): (b) lattice ⟨ib,i/b⟩ ⇒ order-diff constant ⇒ 0 at regular point ⇒ ord Φ=ord Ψ (same divisor) — uses orderDiff_periodic + exists_period_basis; (c) empty divisor ⇒ ratio AnalyticOnNhd+nonvanishing (MeromorphicOn.divisor); (d) assemble → uniqueUpToScalar via ratio_const_of_doublyPeriodic.
