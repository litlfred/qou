---
# qou-h4ab
title: 'wedderburn-lp-ew-wiring is stale on main: t_legacy_matrix_entries moves ~13% on re-run'
status: todo
type: task
priority: normal
created_at: 2026-08-17T01:44:20Z
updated_at: 2026-08-17T01:45:18Z
---

## Evidence (PR #5260)

Re-running `wedderburn_lp_ew_wiring.py` on current main moves:

    t_legacy_matrix_entries_min/max  0.6003377241833765 -> 0.6803696974650493
    (a second pair moves from 0.3727036271108378)

~13 %. **Verified pre-existing**, not caused by the y_λ layer fix on #5260: the
same move reproduces with this branch's changes stashed. A 13 % shift is ~7
orders too large to be the 1.85e-9 straddle, so it is a different cause.

Not diagnosed. Candidates worth checking first: the committed witness predates a
convention change (the field is named `t_legacy_*`, which suggests a legacy
trace convention that may have been re-defined), or an upstream input it reads
was regenerated without this consumer being re-run.

The witness asserts 3 assertions, all passing, in both the old and new state —
so this is a silent value drift, not a failing check.
