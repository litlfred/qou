---
# qou-2cvs
title: 'Infra: FaddeevPhi holomorphicity endowment — ratio Ψ/Φ entire (hratio; closes uniqueUpToScalar via the landed reduction)'
status: todo
type: task
priority: normal
tags:
    - alien-habiro
created_at: 2026-07-18T18:06:37Z
updated_at: 2026-07-18T19:16:14Z
parent: qou-89f9
---

RE-SCOPED (2026-07-18, PR post-#3966): divisor-cancellation is OFF the critical path of the nowhere-zero scaffold — uniqueUpToScalar_of_entire takes NO separate hratio; ratio-entire is derived from the two entireness fields via hΨ.div hΦ hΦ0 (DoublyPeriodicLiouville:125). The endowment splits into: (A) idealization route — add an entireness FIELD, uniqueUpToScalar closes trivially, BUT the field is FALSE for true Φ_b (meromorphic, has zeros+poles) so it proves nothing physical; (B) meromorphic route — restate rigidity over MeromorphicOn/divisors, prove same-divisor from the shared q-difference eq (ord(Φ)=ord(Ψ) pointwise ⇒ ratio entire+nonvanishing). (B) is the real multi-week target. BLOCKED in sandbox: Mathlib meromorphic API oleans not cached + no mathlib source tree + network-blocked ⇒ cannot compile/verify meromorphic Lean here. Do (B) in a full-build session from MeromorphicOn.divisor. Doc: docs/audits/2026-07-18-endowment-scope-meromorphic-wall.md. Anti-laundering: not axiomatized.
