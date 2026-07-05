---
# 1c24
title: 'Swarm: shell_filling_rule shell_filling_inner_shells (assess: closeable vs honest wall)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-05T23:07:22Z
updated_at: 2026-07-05T23:08:37Z
parent: uudc
---


## Swarm finding (assessed — 3× WALL, no honest close)
All 3 sorries (`shell_filling_inner_shells`, `shell_filling_hund_rule`, `shell_filling_lp_strong_duality`) need conclusions (occupancy `=` capacity; `ground` maximises `singly`; `primal_obj = Z·y_0`) not derivable from the deliberately input-only `ShellFillingRuleContext` class (only `occupancy_le_capacity` `≤`, free fields). Closing would reintroduce the self-assuming-projection anti-pattern removed in bean qsb2. Honest cited sorries stay.
