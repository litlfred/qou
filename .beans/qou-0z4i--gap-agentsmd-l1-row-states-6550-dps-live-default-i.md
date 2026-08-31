---
# qou-0z4i
title: 'GAP: AGENTS.md L1 row states 65/50 dps; live default is 70/60'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:21:27Z
updated_at: 2026-08-30T14:21:41Z
---

Measured 2026-08-30 on branch claude/srvu-drain-a-2026-08-30, no QOU_* env
vars set:

    python3 -c "import qou_substrate.precision as P; print(P.COMPUTE_DPS, P.OUTPUT_DPS, P.PRECISION_GUARD)"
    -> 70 60 10

AGENTS.md, table under "Precision goals (STRICT)", L1 row, still reads:

    met -- `_precision.py` default is 65 dps compute / 50 dps serialization
    (10^-50 absolute truncation)

Live is 70 dps compute / 60 dps serialization / 1e-60 truncation. All three
numbers in that parenthetical are stale.

NOT a regression: the change is strictly a tightening, and it is visible in
witness diffs as `precisionMetadata` 65/50/15/1e-50 -> 70/60/10/1e-60 when an
old producer is re-run. Recomputed values agree with the committed ones over
their entire shared prefix, so no recorded result is invalidated -- only the
documented figure is wrong.

Surfaced by re-running two producers under bean qou-srvu:
  computations/cyclotomic_depth3_dimension_pslq.py   (witness dated 2026-05-11)
  computations/bring_trilog_zeta5_depth_3.py         (witness dated 2026-05-29)

Not edited in that PR because AGENTS.md is contested across sibling branches
and a one-line doc fix there would conflict with four concurrent srvu agents.
