---
# qou-2cvs
title: 'Infra: FaddeevPhi holomorphicity endowment — ratio Ψ/Φ entire (hratio; closes uniqueUpToScalar via the landed reduction)'
status: in-progress
type: task
priority: normal
tags:
    - alien-habiro
created_at: 2026-07-18T18:06:37Z
updated_at: 2026-07-18T23:31:28Z
parent: qou-89f9
---

ROUTE-B STEP 2 LANDED (2026-07-18, both lean exit 0) in QOU/QBeta/MeromorphicSameOrder.lean, against the in-sandbox-built Meromorphic cone:
1. meromorphicOrderAt_sharedPrefactor_balance — ord(P·Ψ)+ord Φ = ord(P·Φ)+ord Ψ (prefactor cancels; mul + WithTop ℤ abel). PROVED.
2. meromorphicOrderAt_orderDiff_shift — ord Ψ(x+c)+ord Φ x = ord Φ(x+c)+ord Ψ x (order-diff c-periodic), composing (1) with the order-translation invariance htr carried as explicit §3b-cond hypothesis. PROVED modulo htr.

REMAINING BRICKS (honest, not axiomatized):
(a) htr = meromorphicOrderAt (g∘(·+c)) x = meromorphicOrderAt g (x+c) — translation invariance. Filter-level Mathlib-gap: punctured-nhds pushforward Tendsto (·+c) (𝓝[≠]x)(𝓝[≠](x+c)) + witness transport across eq_top_iff/eq_int_iff. Best done with LSP. This is now the SINGLE isolated analytic input for step 2.
(b) lattice ⟨ib,i/b⟩ ⇒ order-diff constant ⇒ 0 at a regular point ⇒ ord Φ=ord Ψ everywhere (uses orderDiff_shift + exists_period_basis).
(c) empty divisor ⇒ ratio AnalyticOnNhd + nonvanishing (MeromorphicOn.divisor).
(d) assemble → uniqueUpToScalar via ratio_const_of_doublyPeriodic.
Cone build recipe recorded in prior bean note + workplan.
