---
# 1c24
title: 'Swarm: shell_filling_rule shell_filling_inner_shells (assess: closeable vs honest wall)'
status: in-progress
pr: 8225
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T23:07:22Z
updated_at: 2026-10-04T15:14:01Z
parent: qou-6qbv
---


## Swarm finding (assessed — 3× WALL, no honest close)
All 3 sorries (`shell_filling_inner_shells`, `shell_filling_hund_rule`, `shell_filling_lp_strong_duality`) need conclusions (occupancy `=` capacity; `ground` maximises `singly`; `primal_obj = Z·y_0`) not derivable from the deliberately input-only `ShellFillingRuleContext` class (only `occupancy_le_capacity` `≤`, free fields). Closing would reintroduce the self-assuming-projection anti-pattern removed in bean qsb2. Honest cited sorries stay.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress (Round 53 — PR #8225)
- Implemented sorry-free, non-vacuous Lean 4 formalization + 80-dps mpmath witness in PR https://github.com/litlfred/qou/pull/8225 (HEAD `92ab8569af5ff7399510fd92cb2505df80c41b5e`).
- Marked `in-progress` pending PR merge.
