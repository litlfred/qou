---
# qou-f64d
title: 'main is RED on audits-tree raw-float64 — two coverage percentages serialized as float'
status: todo
type: bug
priority: normal
created_at: 2026-08-28T00:00:00Z
updated_at: 2026-08-28T00:00:00Z
---

`scripts/precision-gates.sh` exits **1** on `main` today. One blocking gate is
red and it is not any branch's doing.

## Measured

    ▸ audits-tree raw-float64   (computations/witness_raw_float64_audit.py)
        scan root          : docs/audits
        NEW dirty witnesses: 1
        REGRESSED          : 0
           2  docs/audits/2026-08-26-kernel-defeq-sample.witness.json

The two fields, read out of **`origin/main`'s own copy** (not a working tree):

    /coverage/coverage_of_tree_pct            = 2.3
    /coverage/coverage_of_olean_reachable_pct = 2.5

Both are non-integral `float`, so they are raw float64 in a committed witness —
the class the ratchet exists to keep at zero.

## Provenance — established, not assumed

The gate's own output says *"check whether the movement is yours or main's
before claiming it (git log the newly-listed entries)."* Done:

- added by `cdbdc84af1` (2026-08-27), part of the `qou-0avp` olean-coverage work;
- present on `origin/main`;
- the branch that found it (`claude/bk-crossing-coordination-woiqj3`, the `1j39`
  + `qou-stlw` commits) touches **zero** `docs/` files — its whole diff is under
  `computations/` and `.beans/`.

So this is main's, and it was red before the branch and stays red after it.

## Not fixed here, deliberately

The fix is the one the gate names: carry the percentage as `mpmath.mpf` in the
producer and serialize with `_precision.fmt`, then re-run — **not** a baseline
entry, which the gate explicitly forbids ("Do NOT add the file to the baseline
to silence this").

It is left alone because the producer is a **sibling's live area**: `qou-0avp`
commits landed on 2026-08-27 and the audit doc is theirs. Editing another
agent's in-flight producer to clear a gate on my unrelated PR is how two agents
collide, and it happened once already today (`qou-1brv`, where a sibling landed
the same fix in parallel). Whoever owns `qou-0avp` should take it; it is a
two-line change at the producer.

## Why it matters beyond the number

A percentage is exactly the field where float64 looks harmless — `2.3` is not a
precision-critical quantity, and that is the argument for leaving it. But the
ratchet's value is that it stays at **zero**: once one "obviously harmless"
float is allowed through, the next reader has to adjudicate rather than read a
count. AGENTS.md is explicit that baselines drain and never grow, and the same
logic makes a permanently-red blocking gate corrosive — see `qou-p8lx`, which
records two *other* blocking staleness gates that policy says cannot be drained.
This one is different from those: it is cheaply fixable at the producer.
