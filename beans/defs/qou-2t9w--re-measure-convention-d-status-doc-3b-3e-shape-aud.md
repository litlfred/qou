---
# qou-2t9w
title: 'Re-measure convention-D status doc §3b-§3e: shape audit, Lean audit, and the three disagreeing witness detectors'
status: todo
type: task
priority: normal
created_at: 2026-11-14T07:02:23Z
updated_at: 2026-11-14T07:02:51Z
parent: qou-cxh0
---

§3b (convention-c-producer-audit.py), §3c (tools/Rust), §3d (lean-markov-convention-audit.py) and §3e (three witness detectors that DISAGREE) all still carry 2026-10-10 figures and must not be quoted as current. §3a is re-measured in §12; these are not.

§3e caveat to confirm or refute: the fingerprint detector's single hit is a float64 zero (y_(1^3) = 1.45e-17 on a 3-row block, exactly 0 under D), NOT a convention-C weight.

Measurement hazard from §3e: a live git worktree double-counts every repo-wide audit -- it once reported 2 files where 1 existed, the second being a dispatched agent's own copy. De-dupe on path suffix or quiesce.
