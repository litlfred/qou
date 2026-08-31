---
# qou-6sts
title: 'raw-float64 ratchet is RED on main again: 1 new + 1 regressed (2026-08-31)'
status: todo
type: bug
priority: normal
created_at: 2026-08-31T03:49:09Z
updated_at: 2026-08-31T03:49:09Z
---

MEASURED on `main` `83f5e6482e`, 2026-08-31T03:5xZ, by running
`computations/witness_raw_float64_audit.py` directly (the committed audit
witness on main said `new_not_baselined: 0`, so do not trust it -- same
staleness family as `qou-82ur`).

    dirty_witnesses      1045
    new_not_baselined       1
    regressed               1
    drained_files         168

NEW (4 raw float64 fields):
    computations/probes/arc-count-diagnostic-degeneracy.witness.json
    last touched a4f54a3127 "research(qou-0c19): the R^2=0.83 arc-count
    diagnostic is not in the witness it cites"  -> owning arc is qou-0c19

REGRESSED (89 -> 91):
    computations/audits/braid-encoding-audit.witness.json
    last touched 89f1137463 "fix(qou-soj6): all three routes tried -- route 1
    lands, and it catches a 43% disagreement"  -> owning arc is qou-soj6

NOT MINE, and I am not fixing them from the Toffoli branch (#6341) -- different
domain, different producers, and the "ride on the active PR" rule is for
ADJACENT code. Handing them to the owning arcs instead.

FIX AT THE PRODUCER, per the standing rule: carry the value as `mpmath.mpf`
from its source and serialize with `_precision.fmt`, then re-run. Do NOT add
either file to `raw-float64-baseline.json`, do NOT `--rebaseline`, and do NOT
hand-edit a number. Baselines drain, never grow.

WHY THIS KEEPS HAPPENING, and why this bean is about two names rather than the
mechanism: `qou-mnrd` (completed) already established the durable finding --
nothing runs the ratchet on a push, because CI is `workflow_dispatch`-only under
the 2026-06-30 Actions-billing directive, and the owner reaffirmed that
dispatch-only choice on 2026-08-09 with this exact failure cost on the table.
So the enforcement gap is settled policy, not an open item, and re-proposing a
push trigger is out of scope. `qou-mnrd`'s own conclusion is that WHICH files
are dirty is transient and cheap to drain; this bean exists only to name the
current two so the arcs that produced them can drain them, and should be closed
when they are -- not held open as a tracker for the class.

A TRAP I walked into while measuring this. I first ran the ratchet on a tree
**146 commits behind main** and got a different `dirty_witnesses` (1049) and
`drained_files` (165) with the SAME two offenders. The offenders happened to be
stable; the counts were not. Re-measure on the tip before quoting any figure
from this family.

A SECOND TRAP, in the harness rather than the corpus. `precision-gates.sh`
prints `NEW dirty witnesses : 0` for the padding-family ratchets, and a grep
that matches that phrase reads as an all-clear while the raw-float64 ratchet is
red one line further down under a DIFFERENT phrase (`NEW witnesses carrying raw
float64`). I misread it that way for one turn. The gate to read is the `RED:`
summary line, or the per-audit witness's `new_not_baselined` / `regressed`
fields -- never a phrase match on one ratchet's wording.
