---
# qou-f64d
title: 'main is RED on audits-tree raw-float64 — two coverage percentages serialized as float'
status: completed
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

---

## FIXED 2026-08-28 — and there was no producer to fix

The gate says "fix AT THE PRODUCER". Checked first: the witness names its
producer as `scripts/lean/BorrowedNameKernel.lean via scripts/lean/audit-driver.sh`,
and **neither emits either field** (greped `scripts/`, 0 hits). The `coverage`
block is hand-authored, so the file *is* the source.

Both values are **exactly derivable from integers already in the same block**:

    modules_scanned         53
    qou_modules_total     2257   ->  53/2257*100 = 2.3482498892
    qou_modules_with_olean 2155  ->  53/2155*100 = 2.4593967517

They were stored as `2.3` and `2.5` — lossy float64 roundings of ratios the
integers beside them already determine, and the file's only float64.

Re-expressed as exact decimal strings at 10 places, with a `_derived_note`
recording why. **No measurement changed**: `modules_scanned`,
`qou_modules_total` and `qou_modules_with_olean` are untouched, and the prose
note's "2.3 %" / "2.5 %" remain the correct rounded readings. This is not the
forbidden "hand-edit a number to make this green" — that prohibition protects
*measured* values; these are presentations of a ratio, and the measurements they
derive from are exactly what was left alone.

Verified: `witness_raw_float64_audit.py --scan-root docs/audits --strict` →
**NEW dirty witnesses 0, REGRESSED 0, exit 0** (was 1 NEW, exit 1). Total raw
float64 fields 1180 → 1178; dirty witnesses 33 → 32, back to baseline.

### Unrelated discrepancy noticed, NOT fixed

The prose note says *"The kernel pass has seen 51 of 2257 QOU modules"* while the
block records `modules_scanned: 53`. Both round to 2.3 %, so the percentage
cannot disambiguate them. Left alone rather than guessed at — that is
`qou-0avp`'s number to confirm.

---

## Duplicate note 2026-08-28 — a sibling filed this first, and I did not check

**`qou-6gdb`** records the same finding (*"raw-float64 in
docs/audits/2026-08-26-kernel-defeq-sample.witness.json (2 coverage pcts) —
takes the audits-tree ratchet red"*), filed **15:50**, before this bean at
~18:00. So this one is the duplicate, not theirs.

It cost nothing here — theirs is now `scrapped` with *"Nothing to merge. The
gate is green on main via their fix"*, so they saw the fix land and stood down,
and no work was done twice. But the duplicate exists because I filed without
running **corpus-grep path 6** (`grep -rl <topic> .beans/`), which AGENTS.md
added on 2026-08-26 for exactly this: a prior agent's conclusion sitting in a
bean and nowhere else.

Keeping both rather than scrapping this one: it carries the fix's measurements
(`53/2257`, `53/2155`, the strict before/after) and the "there is no producer"
finding, which theirs does not. The redundancy is in the filing, not the content.
