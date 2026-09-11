---
# qou-sknx
title: 'raw-float64 ratchet: 5 NEW un-baselined on main (2026-09-04), and the committed audit witness again said 0'
status: completed
type: bug
priority: normal
created_at: 2026-09-04T04:51:29Z
updated_at: 2026-09-11T15:53:55Z
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


---

## RESOLVED — verified 2026-09-11 from `qou-n5kp` (PR #7161), on `main` +31

All five are clean, and **none was laundered into the baseline**. Checked
against the real 1004-entry file map inside
`computations/raw-float64-baseline.json` (the top level is a wrapper —
`note`/`enforced_rule`/`drain_owner`/`files_count`/`fields_count`/`files`/… —
so a naive `len(json.load(...))` reads 15 and tells you nothing):

| witness | in baseline | raw float64 today |
|---|---|---:|
| `probe-toroidal-legendre-weinberg-gate` | no | **0** |
| `probes/arc-count-diagnostic-degeneracy` | no | **0** |
| `probes/c2-diagonal-insertion-expansion-probe` | no | **0** |
| `probes/bpp-higher-a-sparse` | no | **0** |
| `qbeta/qbeta-meridian-holonomy-anchor-swing` | no | **0** |

Drained at the producer, which is the only admissible route. The baseline's
own history names the work: `a4fcd0bbf6` and `656e37bb8b` (`qou-r47m`),
`b7f9bee43d` (`qou-1u56`).

Live gate on the same head: `witness_raw_float64_audit.py --strict` → exit 0,
**NEW 0, REGRESSED 0**.

### Your `bpp-higher-a-sparse` sub-question — answered, and the hypothesis is wrong

This bean asks *"worth checking whether the producer's duration field was
renamed"* to explain that file leaving `ephemeral_duration_carved_out` for
the new-dirty bucket. **It was not renamed.** `git log -S` on
`computations/probes/bpp_higher_a_sparse_probe.py` finds **zero** commits
ever touching `wall_sec`; `elapsed_sec` — already a declared name — was
introduced by `6c5bb855a9` (*"chore(qou-6sts): drain raw-float64 at two NEW
probes (4+2 -> 0)"*), i.e. the file was **drained**, and it happens to spell
its duration field correctly.

**What I did NOT reconstruct:** what the category transition looked like on
2026-09-04 itself. I established the current state and ruled out the rename
in that producer; I did not replay the 2026-09-04 tree. If the bucket
movement still matters to someone, that replay is the missing step.

### The name question is real, just not here — see `qou-n5kp`

The rename hypothesis is a live class even though it is not this file's
story. `chi-free-via-lr` was REGRESSED 3 → 4 purely because its four
`time.time() - t0` fields were spelled **`wall_sec`**, which is in neither
`_EPHEMERAL_META_FIELDS` nor the `/dur|elapsed/` filter the ratchet applies
to it — so a wall-clock duration was counted as a precision finding. Fixed in
PR #7161 by renaming to the declared `elapsed_sec`, deliberately **not** by
widening the mask (`witness_raw_float64_audit.py:216` names `wall_sec` as the
case that fails *silently* under a one-sided edit; `qou-ywee` / `qou-hhm3`
own that widening, and ~411 timing-shaped fields under ~65 undeclared names
remain).

### One more thing worth carrying forward

This bean's title — *"and the committed audit witness again said 0"* — held
again on 2026-09-11, in the other direction: `main`'s committed
`witness-raw-float64-audit.witness.json` recorded `regressed: 0` while `main`
was REGRESSED **3**. **A clean-looking committed audit witness is not
evidence of a clean tree**, in either direction. PR #7161 regenerates it
(`dirty 1009 → 992`, `drained_files 0 → 16`).
