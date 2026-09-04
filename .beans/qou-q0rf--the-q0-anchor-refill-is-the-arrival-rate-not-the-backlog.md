---
# qou-q0rf
title: The q0-anchor refill ratchet is RED on main (NEW 147) — and the arrival rate, not the backlog, is the thing to fix
status: in-progress
type: task
priority: high
created_at: 2026-09-03T04:40:00Z
updated_at: 2026-09-04T04:34:01Z
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


---

## Within-session replacement measured 1:1, and one arrival has a mechanism this bean does not record (2026-09-04)

Measured on `claude/resumable-compute-chunking-2026-09-04` while draining four
witnesses that were blocked on a compute rather than on anyone's attention:

    NEW (not in baseline)     14  ->  14
    drained since baseline    86  ->  90
    unstamped (live scope)  1605  -> 1601

**Four out, four in — net zero on NEW**, inside one session. That is this
bean's thesis at a shorter timescale than the ~29/day arrival rate it records.

The four that arrived did so **via a rebase across 55 commits of main**, not
spontaneously in my tree — stating the mechanism because \"four arrived while I
worked\" would otherwise read as a stronger claim than was measured:

    probe-plancherel-convention-gap          ABSENT pre-rebase
    probes/c1-mirror-asymmetry-sign-probe    ABSENT pre-rebase
    probes/conjugation-orbit-isospin-room    ABSENT pre-rebase
    chi-neutron-h3                           PRESENT pre-rebase  <-- different

**The fourth is the one worth reading, and it is a new mechanism.**
`chi-neutron-h3` was already in my tree **stamped**; the rebase brought a
version with the stamp **removed**. `9c2058f0bd` — a commit whose own message
is *\"drain(qou-3f7a): q0 drift NEW 10 -> 5\"* — stripped `q0Anchor` and
`q0Value` from it. **A drain of one q0 gate refilled another.**

Net on the anchor gate from that commit is **+2** (3 stamps added, 1 stripped),
so this is not a systematic defect in that drain — but it is a refill source
this bean's model does not have. Its arrival-rate data is *new witnesses
landing unstamped*; this is *an existing stamp being removed*. Full evidence
and the reason it is a genuine regression (the producer reads `Q_MP`, so
`proton` was correct and nothing replaced it) is recorded on `qou-3f7a`.

Consequence for this bean's conclusion: unchanged, and if anything sharpened.
A backlog that can be refilled by its own drains is even less amenable to
being drained than one refilled only by new arrivals.
