---
# qou-4dq1
title: Resolve the 6 conflicting open PRs and land them
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T10:08:52Z
updated_at: 2026-08-25T10:09:32Z
---

## Map (measured 2026-08-25 by git merge-tree against origin/main)

| PR | conflicts | shape | state |
|---|---|---|---|
| #4673 | (was) 0, but rebase-red | convention C→D shift, see below | **MERGED** |
| #4766 | 1 | docs/coordination/trace-convention-registry.json | resolved, verifying |
| #4619 | 1 | .beans/qou-3q7t bean, append-only | trivial |
| #5249 | 2 | rho_k_h3a_refinement.py + its witness | producer re-run needed |
| #4868 | 2 | delta_lambda_k_star_variance_phase5d_5b.py + witness | producer re-run needed |
| #4718 | 4 | 2 lepton producers + 2 witnesses | producer re-run needed |
| #4925 | 8 | 4 add/add content blocks + references.ts + mass-theory.ts | main has later edited copies |
| #5500 | 2 | SKIP — its own body says "DO NOT MERGE YET, knowingly red" |
| #5352, #5402 | — | SKIP — author said do not merge |

## The finding that came out of #4673

Rebasing moved two probes' numbers 22 % / 26 % and turned the convention audit's
own gate red. Attributed by running the UNMODIFIED producer in a worktree at the
pre-rebase merge-base: it reproduces the old numbers there and the new ones on
main. Not a regression — `_wenzl_constants` moved C -> D, and under D the Wenzl
level collapses to r = 2, so y_lambda = 0 exactly for every partition with three
or more rows (25 of 30 at n = 9). Already Lean-proved on main
(`wenzlLevel_conventionD`, `schurPrincipal_eq_zero_iff`) and measured by
`two_row_support_recount.py`; nothing re-derived.

Two consequences that were live in #4673 and are now fixed there:

1. Its headline "7.7 % undeclared systematic from the |chi|-vs-signed choice" was
   ALL of the measured spread and is a convention-C artifact — the ten negative-
   weight partitions under C all have ell >= 3, so under D |chi| is a no-op.
   Measured under D: 0.0146 %, all of it the p-n crossing.
2. `mu3_door_budget_probe` printed "the negative blocks supply ~1/7.6e39 of what
   the door needs". There are no negative blocks; sum|y_neg| = 1.04e-42 is
   round-off at 40 dps. Round-off reported as a measurement.

GENERALISATION NOT YET SWEPT: 32 producers import `y_lambda_at_q0_mpmath`, and
several reason explicitly about three-row or negative-weight structure
(`threerow_sign_crossing_decomp`, `threerow_sign_crossing_probe`,
`threerow_4he_completion_probe`, `threerow_qcross_trend_probe`,
`ylambda_sign_content_threshold_probe`, `mirror_split_milnor_one_third_probe`).
Any of them written pre-2026-08-09 may be measuring an object D sets to zero, or
dividing by round-off. Not swept here — separate bean when someone picks it up.
