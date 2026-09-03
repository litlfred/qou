---
# qou-q0rf
title: 'The q0-anchor refill ratchet is RED on main (NEW 147) — and the arrival rate, not the backlog, is the thing to fix'
status: in-progress
type: task
priority: high
created_at: 2026-09-03T04:40:00Z
updated_at: 2026-09-03T04:40:00Z
---

`scripts/precision-gates.sh` has a **blocking** gate red on `main`. Nothing
claimed it; `qou-1c4y` is the muon migration, which is a different thing.

## Measured 2026-09-03 on `d502ed06ce9`

    q0-anchor refill ratchet   NEW (not in baseline)   147   (was 0 on 2026-08-29)
    unstamped witnesses (live scope)                  1742   (was 1627)
    q0-anchor flip             Q0_FLIP                  18   (was 1)

Arrival dates of the 147: **4** on 08-29, **74** on 08-30, **48** on 08-31,
**16** on 09-01, **5** on 09-02 — about **29/day**, still arriving. A re-run
the same afternoon reported **150**, so the number moves while you look at it.

## The discipline held — this is not a baseline being widened

    q0-anchor-missing-baseline.json   1678 -> 1677

It **drained by one**. Nobody absorbed the refill into the baseline, and
agents are stamping correctly as they go — `1c2e251dabf` registers five probes
as proton-pinned and restamps three witnesses. The gate is telling the truth
and the practice is right; it is simply slower than the arrival rate.

## Why draining first is the wrong move

This has been drained to zero and refilled twice already, and the pattern is
recorded from both directions in `qou-mnrd` and `qou-82ur`: *"dirty witnesses
reach main, get drained, and are replaced by different dirty witnesses — a
revolving door — because each one lands the same way the last did,
unexamined."* I drained it to zero myself on 2026-08-29 (#6017). Five days
later it is at 147. **A third drain buys about five days.**

## Done: the arrival rate now has a check

`scripts/precommit-precision-warn.sh` grew a **q0Anchor ratchet** — warn-only,
exits 0, stdlib JSON over the witnesses in the commit. It speaks only on a
witness **absent from HEAD** committed with no anchor, or one that **had** an
anchor and lost it. It stays silent on the 1,663 legacy witnesses, because
firing on a pre-existing condition the committer did not cause is how a
warning gets learned as noise.

**Validated against the live refill: all 150 currently-flagged witnesses did
not exist at `a788e78ce2b`** — every one is a NEW-file case the ratchet
catches.

## Still open — the 147 themselves

Not drained here, deliberately: the arrival rate had to be closed first or the
drain is the third of three. Whoever takes it should know:

- **Not all 147 want `proton`.** Some are genuinely q0-independent and need
  `"independent"` **with a reason**. Stamping `proton` to silence the gate
  asserts a pin the computation may not have — the exact failure `q0Anchor`
  exists to prevent, and the mistake I nearly made on
  `fake_degree_via_telescope` in #6017 before reading the producer.
- **Some producers refuse a re-run by design.** AGENTS.md names three
  (`atomic_tr_m_mpfr_50dps`, `he4_stage2_ranking_seminormal_xcheck`,
  `cross_check_trM_1ppb`); a non-zero exit is not a defect there.
- **Re-measure before starting.** 147 → 150 within one afternoon.

## `Q0_FLIP: 18` is a separate question

Up from the 1 I left. Not characterised here — the two flips I understood in
#6017 were a mislabelled producer and a compute-bound re-run, and 18 will not
be one story. Do not assume it is the same defect eighteen times.
