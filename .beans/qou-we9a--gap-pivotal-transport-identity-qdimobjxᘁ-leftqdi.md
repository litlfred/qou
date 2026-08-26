---
# qou-we9a
title: 'GAP: pivotal transport identity qDimObj(Xᘁ) = leftQDim X — rtqd''s last residual'
status: todo
type: task
priority: normal
created_at: 2026-08-26T17:01:29Z
updated_at: 2026-08-26T17:17:36Z
---


## Status 2026-08-26: the GOAL is closed, this identity is NOT

I opened this to prove the pivotal transport identity qDimObj (Xdual) = leftQDim X, as
rtqd's last residual. That is NOT what happened, and the distinction matters.

rtqd's actual goal -- qDimObj (Xdual) = qDimObj X -- is now proved outright by a route
that does not pass through transport at all (see rtqd, and
QOU/MathlibExt/BraidedQuantumDimension.lean). So this bean is no longer BLOCKING anything.

The transport identity itself remains unproved. It stays a hypothesis of
qDim_conj_of_pivotalTransport and friends, which remain valid conditional theorems. Worth
having on its own account -- it relates the two traces, which the unconditional route says
nothing about -- but it is no longer on anyone's critical path.

Left OPEN rather than scrapped: it is a real statement, still unproved, and the file that
carries it still carries it as a hypothesis.
