---
# qou-2cvs
title: 'Infra: FaddeevPhi holomorphicity endowment — ratio Ψ/Φ entire (hratio; closes uniqueUpToScalar via the landed reduction)'
status: in-progress
type: task
priority: normal
tags:
    - alien-habiro
created_at: 2026-07-18T18:06:37Z
updated_at: 2026-07-18T22:11:37Z
parent: qou-89f9
---

ROUTE-B IN PROGRESS (github egress authorized 2026-07-18): unblock = clone mathlib source at pinned rev f897ebcf → build Mathlib.Analysis.Meromorphic.Divisor cone (background clone underway). Then reformulate uniqueUpToScalar over MeromorphicOn/divisors: (1) FaddeevPhi.merom field; (2) same-order lemma — Φ,Ψ solve same first-order q-diff eq f(z+c)=P(z)f(z) ⇒ meromorphicOrderAt Ψ − meromorphicOrderAt Φ is c-periodic ⇒ constant over the ⟨ib,i/b⟩ lattice ⇒ 0 at a regular point ⇒ ord Φ=ord Ψ everywhere; (3) empty divisor ⇒ ratio entire+nonvanishing; (4) feed ratio_const_of_doublyPeriodic. Full lemma chain: docs/workplans/2026-07-18-alien-habiro-hard-infra-execution-plan.md §1. Anti-laundering: same-order (step 2) must be DERIVED from the diff eqs, FaddeevPhi.merom proved for PhiBProd or carried as honest conjecture.
