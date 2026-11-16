---
# qou-atsd-t0
title: 'T0: dim V=2 arithmetic crux — n.choose 2 = 1 -> n = 2 (Lambda^2 V cong 1 nondeg => dim 2), Lean sorry-free'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-atomicity
created_at: 2026-07-25T20:32:48Z
updated_at: 2026-10-10T07:16:12Z
parent: qou-8lxd
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Note (2026-11-16)
- Formalized T0 `dim V = 2` arithmetic crux (`chooseTwo n = n*(n-1)/2 = 1 <-> n = 2`) sorry-free in `QOU/Eightfold/T29FluxTubeLatticeAndColourDisc.lean` (`chooseTwo_eq_one_iff_eq_two`) + 50-dps probe `t29_flux_tube_lattice_and_colour_disc_probe.py` (PR `litlfred/qou#8168`, head `bca84d0884fa3fb226f06011fff4d42b6b78d003`).
