---
# qou-ovxx
title: 'Lean-prove MilnorExactOrderConjecture (#4471): exact order 2(A−1) ⇔ leading μ̄ coefficient ≠ 0'
status: completed
type: task
priority: normal
tags:
    - formalization
    - deltalambda
created_at: 2026-08-01T19:01:04Z
updated_at: 2026-08-01T19:01:38Z
parent: qou-pddf
blocked_by:
    - qou-q64u
---

#4471 (MilnorOrderLawGeneral.lean) proved the LOWER BOUND order(D_A) ≥ 2(A−1) for all A sorry-free, and left the EXACT law as the instance-less MilnorExactOrderConjecture (content-bearing class, no instance). Closing it = proving the length-A iterated-commutator Brunnian trace-deficit leading coefficient is nonzero for all A. Two routes: (B) inductive leading-coefficient tracking through the commutator recursion — the crux is tr([x,y])=0 (trace kills the bare top commutator; nonvanishing must come from the Markov closure); attempted on branch claude/deltalambda-milnor-exact-coefficient-2026-08-01, honest sub-wall if the trace-cyclicity obstruction blocks it. (A) the Vassiliev bridge (the sibling task under this epic). Blocked-by the Vassiliev bridge task for the general route.
