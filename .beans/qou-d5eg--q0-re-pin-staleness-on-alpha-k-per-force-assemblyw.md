---
# qou-d5eg
title: 'q0 re-pin staleness on alpha-k-per-force-assembly.witness.json: committed witness is MUON-pinned, q_at() now returns PROTON - every delta_q_value_at_q0 digit moves'
status: todo
type: task
priority: normal
created_at: 2026-08-11T00:51:30Z
updated_at: 2026-08-15T22:32:50Z
blocked_by:
    - qou-7vm4
---

2026-08-15 (reorientation pass): this is the SAME underlying question as
qou-7vm4 defect 1, seen from the witness side rather than the code side. The
committed witness is muon-pinned; q_at() returns proton. Whether that is
staleness or correctness depends entirely on which way the manifest call goes.
Do not regenerate this witness independently of that decision -- doing so would
silently pick the proton side of an undecided owner call. Blocked on qou-7vm4.
