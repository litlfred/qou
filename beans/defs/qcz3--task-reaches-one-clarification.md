---
# qcz3
title: 'Content: clarify q-Collatz "reaches 1" -> reaches 2-cycle {q^-1,1+q^-1}'
status: completed
type: task
priority: medium
parent: qcz1
created_at: 2026-07-24T15:48:40Z
updated_at: 2026-07-24T16:16:58Z
---

The unknot 1 is not in C_q's domain (1|_{q=-1}=1 ∉ {0,-1}); the genuine positive
attractor is the 2-cycle {q^-1,1+q^-1} (q-lift of {1,2}). Add a precise
clarification to q-collatz-conjecture.md (and the QCollatz reaches_one docstring)
that "reaches 1" is a classical-limit shorthand. Scope (a) clarification, not a
refutation. Render-QA the math edit. Sidecar refresh after.

DONE: conjecture .md scoped 'within a QOU' + reaches-2-cycle clarification; QCollatz.lean reaches_cycle targets fundamental attractor (not literal 1).
