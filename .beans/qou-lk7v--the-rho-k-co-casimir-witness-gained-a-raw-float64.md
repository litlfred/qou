---
# qou-lk7v
title: The rho-k co-casimir witness gained a raw float64 (3 -> 4) in the convention-D cascade
status: todo
type: task
priority: normal
created_at: 2026-08-16T11:27:45Z
updated_at: 2026-08-16T11:28:23Z
---

Found while wiring sigma_all_evaluator (PR #5199). NOT mine: git status shows the file untouched on my branch; it landed 2026-08-10 in 506ac91350 'witness: convention-D cascade, producers 41-44'.

witness_raw_float64_audit --strict:
  REGRESSED - these witnesses gained raw float64:
         3 -> 4       computations/rho-k-co-casimir-extended.witness.json

It is the only REGRESSED entry in the corpus. Fix at the producer (carry the
value as mpmath.mpf from its source and serialize with _precision.fmt); do NOT
widen raw-float64-baseline.json. Left for the convention-D cascade owner rather
than fixed inline -- different domain, and that cascade has an active sibling.
