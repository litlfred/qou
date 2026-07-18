---
# qcz1
title: 'Session: q-Collatz cycle-value probe + no-cycles honest re-scope'
status: in-progress
type: milestone
priority: medium
created_at: 2026-07-18T19:50:24Z
updated_at: 2026-07-18T19:50:24Z
---

Chip away at q-Collatz on branch claude/q-collatz-status-1v0pxv (PR #3996).
Done: (1) content-bearing QCollatz class; (2) re-scope no-cycles proof to
A=1 sub-case + audit doc 2026-07-18. Now: enumerate parity words w, form
the affine cycle candidate P0 = B_w/(1-A_w) over Z[q^±1], test
Skein-integrality + cone-positivity + self-consistency. Outcome open:
either find a q-cycle (major) or accumulate negative evidence with an
explicit obstruction.
