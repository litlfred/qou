---
# qou-2cvs
title: 'Infra: FaddeevPhi holomorphicity endowment — ratio Ψ/Φ entire (hratio; closes uniqueUpToScalar via the landed reduction)'
status: in-progress
type: task
priority: normal
tags:
    - alien-habiro
created_at: 2026-07-18T18:06:37Z
updated_at: 2026-07-18T23:21:58Z
parent: qou-89f9
---

ROUTE-B STEP-2 CORE LANDED (2026-07-18, lean exit 0): built the 7-module Meromorphic cone in-sandbox from pinned mathlib source (github egress works; release-server cache blocked, source build not). QOU/QBeta/MeromorphicSameOrder.lean — meromorphicOrderAt_sharedPrefactor_balance: ord(P·Ψ)+ord Φ = ord(P·Φ)+ord Ψ (prefactor cancels; via meromorphicOrderAt_mul + WithTop ℤ abel). This is the algebraic heart of 'order-difference preserved by the q-diff equation'. REMAINING route-B bricks (honest, not axiomatized): (a) meromorphicOrderAt of a c-shift = order at shifted point (translation lemma); (b) lattice ⟨ib,i/b⟩ ⇒ order-diff constant ⇒ 0 at regular point ⇒ ord Φ=ord Ψ (same divisor); (c) empty divisor ⇒ ratio AnalyticOnNhd + nonvanishing; (d) assemble → uniqueUpToScalar via ratio_const_of_doublyPeriodic. Cone build recipe: cd clone, LEAN_PATH=cache (absolute, no overlay), lean -o into cache dir, topo order.
