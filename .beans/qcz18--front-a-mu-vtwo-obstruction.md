---
# qcz18
title: 'Front A (mu descent): v_[2] obstruction witness + conditional descent'
status: in-progress
type: task
priority: medium
created_at: 2026-07-31T20:00:00Z
updated_at: 2026-07-31T20:00:00Z
---

The q-Collatz convergence wall = construct a descent measure mu strictly
decreasing off the attractor (reaches_cycle_of_descent reduces convergence to
this). Attack options:
- A1 (START, tractable negative): PROVE the natural candidate v_[2] fails —
  concrete witness P=-X-2 (q-odd, v_[2]=0) whose odd branch ([3]_q P+1)/[2]_q =
  -(X+1)^2 has v_[2]=2, so v_[2] INCREASES on an odd step. Honest scope-(a): rules
  out the OBVIOUS mu, not the existence of ANY mu. Machine-checks the audit's
  prose wall with a witness.
- A2 (conditional): sharpen reaches_cycle_of_descent with a §3b-cond 'if
  <v_[2]> >= 2 average then descent'.
- A3 (hard): combined mu = a*deg + b*v_[2] — but degree ALSO fails at -q^-2 (odd
  fixed pt, +1 top-cancellation); needs a genuinely new invariant.
Anti-laundering: A1 is scope-(a) negative, NOT structural exclusion; no fabricated mu.
