---
# qou-xzlt
title: 'L4-1: refined s_n expansion — second-order Euler-Maclaurin for log-sine sums (the crux)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:36:11Z
updated_at: 2026-10-04T15:13:11Z
parent: qou-r9ih
---


Feasibility pass DONE (docs/audits/2026-08-11-l41-euler-maclaurin-feasibility.md): FEASIBLE multi-session, decomposed into qou-me9q (exact cell-defect representation, first), qou-itg0 (Stirling half-log — Mathlib Stirling.lean exists, 19 thms), qou-q8lc (uniform O(1/N) cot-bound remainder, the genuinely new estimate). vdV's own route avoids the Euler-Maclaurin endpoint singularity; Mathlib has no E-M formula anyway.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-11 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
