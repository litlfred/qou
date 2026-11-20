---
# qou-a7cr
title: 'OWNER-SCOPE: state what "critical Lyapunov alpha_crit = q_0" means before anyone works it'
status: todo
type: task
priority: normal
created_at: 2026-11-20T16:10:00Z
updated_at: 2026-11-20T16:10:00Z
parent: qou-uhx0
---

Split out of qou-2och (W12, 2026-11-20). DO NOT START until the owner writes the statement.

`alpha_crit` appears nowhere in `folio/` and no Lean, probe or content block defines it. Two readings with opposite status:
- a threshold derived from the substrate whose value is q_0: that derives q_0, FOREVER GATED (owner 2026-08-02);
- a threshold defined independently and evaluated at the CAL-2 pin: not gated, but its definition (which Lyapunov function, on what dynamics) has never been written.
