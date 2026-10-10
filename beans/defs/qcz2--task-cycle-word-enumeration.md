---
# qcz2
title: 'Cycle-word enumeration compute + witness'
status: completed
type: task
priority: medium
parent: qcz1
created_at: 2026-07-18T19:50:24Z
updated_at: 2026-07-18T20:28:29Z
---

sympy probe: for E/O words up to length k, compute A_w,B_w, candidate
P0=B/(1-A), test is_laurent_Z + parity self-consistency + return. Promote
to computations/ with a witness JSON if it yields a clean result. Started
in scratchpad/qcollatz_cycle_probe.py.

**Result (period<=18):** only 2 cycles — positive {q^-1,1+q^-1} (q-lift of {1,2}), negative fixed point -q^-2 (q-lift of -1). No nontrivial positive cycle. Also: unknot 1 is outside C_q domain. computations/qcollatz_cycle_census.py + witness.
