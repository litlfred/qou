---
# qou-sknx
title: 'raw-float64 ratchet: 5 NEW un-baselined on main (2026-09-04), and the committed audit witness again said 0'
status: todo
type: bug
priority: normal
created_at: 2026-09-04T04:51:29Z
updated_at: 2026-09-04T04:52:19Z
---

Successor to `qou-6sts` (completed, 2026-08-31). Same failure mode, larger.

## Measured

`python3 computations/witness_raw_float64_audit.py` on this branch's head
`a69d5e9d04` (= `origin/main` `c29e0752bb` merged in, 151 commits):

    dirty_witnesses      1042      (was 1040 in the committed witness)
    total_fields        34100      (was 34107)
    new_not_baselined       5      (was 0 in the committed witness)
    regressed               0
    drained_files         180      (was 177)

**`regressed = 0` — no previously-clean witness went dirty.** All five are new
arrivals that were never baselined.

## The 5, with field counts

    5  computations/probe-toroidal-legendre-weinberg-gate.witness.json     0679303635  2026-09-03
    4  computations/probes/arc-count-diagnostic-degeneracy.witness.json    f36eef162a  2026-09-03
    3  computations/probes/c2-diagonal-insertion-expansion-probe.witness.json  a2e07cef4c  2026-09-03
    2  computations/probes/bpp-higher-a-sparse.witness.json                f36eef162a  2026-09-03
    2  computations/qbeta/qbeta-meridian-holonomy-anchor-swing.witness.json 9c2058f0bd 2026-09-04

All five landed on `main`. **None is from this branch** — `git diff
origin/main...HEAD -- computations/` is empty; this session touched zero
`computations/` files. Flagging, not claiming.

`arc-count-diagnostic-degeneracy` is the SAME file `qou-6sts` flagged on
2026-08-31 (then 4 fields, still 4). It was never drained; its owning arc is
`qou-0c19`.

`bpp-higher-a-sparse` also **changed category**: it was carried under
`ephemeral_duration_carved_out` (43 → 42 fields) and is now counted as new
dirty. Worth checking whether the producer's duration field was renamed, or
whether the two raw floats are genuinely new.

## The recurring meta-defect: the committed audit witness lies

`qou-6sts` recorded it in these words — *"the committed audit witness on main
said `new_not_baselined: 0`, so do not trust it -- same staleness family as
`qou-82ur`"*. **It happened again, identically.** The witness committed on main
said `0`; running the producer says `5`.

So the ratchet is only as live as its last run, and nothing re-runs it on a
push (`witness-staleness.yml` is `workflow_dispatch`-only under the 2026-06-30
Actions-billing directive, reaffirmed 2026-08-09). The warn-only PreToolUse
commit hook (`scripts/precommit-precision-warn.sh`) is what re-ran it here — it
fired because this session committed, not because anything checked the tree.

**That is the third recorded instance** (`qou-mnrd`, `qou-82ur`, `qou-6sts`) of
"dirty witnesses land, get drained, and are replaced by different dirty
witnesses, each arriving the way the last did".

## What was done here

The regenerated witness is committed. This is **not** baseline widening:
`raw-float64-baseline.json` is untouched, and the audit's own record moving from
a stale `0` to a true `5` is the opposite of laundering. Do NOT drain these by
adding them to the baseline — fix at the producer (carry `mpmath.mpf` from the
source, serialize with `_precision.fmt`), then re-run it.

## Not done, and why

Four of the five belong to other agents' live arcs (`qou-0c19` among them).
Draining someone else's producer mid-arc is the "never touch a sibling's claim"
case, and re-running probes I have not read risks moving numbers I cannot
verify. Raised here for their owners.
