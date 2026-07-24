---
# qcz13
title: 'qcz13 (HARD, likely WALL): attempt a well-founded descent mu for reaches_cycle'
status: completed
type: task
priority: low
parent: qcz10
created_at: 2026-07-24T21:52:00Z
updated_at: 2026-07-24T21:05:32Z
---

Feed a candidate mu (built from v_[2] + a degree/height term) into the PROVED
reaches_cycle_of_descent. Expected outcome: WALL — no mu strictly descends off
the attractor without assuming the <v_[2]> >= 2 contact average, which is the
conjecture. The classical analog (a monotone Collatz stopping measure) is OPEN.
Honest dispositions: (a) prove a CONDITIONAL descent 'if <v_[2]> >= 2 pointwise
then mu descends' (a section-3b-cond theorem — real, wires nothing), OR (b)
document the wall in the 2026-07-18 audit with the (a) scope classification. Do
NOT fabricate a global mu. Expected to close as 'honest wall', not 'proved'.

CLOSED as HONEST WALL (disposition b). qcz12's qTwoValuation_mul_qplus_one makes it precise: even step v-1, odd step uncontrolled => no unconditional monotone mu. reaches_cycle_of_descent (already proved) IS the honest conditional (descent => convergence); a global mu = proving the open conjecture. NOT fabricated. Documented in the 2026-07-18 audit.
