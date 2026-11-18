---
# qou-q0rf
title: The q0-anchor refill ratchet is RED on main (NEW 147) — and the arrival rate, not the backlog, is the thing to fix
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T04:40:00Z
updated_at: 2026-10-10T07:56:22Z
parent: qou-cdx1
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


---

## 🛑 CORRECTIONS to my section above, and a verified all-clear on the hook (2026-09-04)

**The arrival-rate check WORKS — verified by reproduction, not by reading.**
Stripped `q0Anchor` from a stamped witness, staged it, fed
`scripts/precommit-precision-warn.sh` the JSON payload the harness sends:
**14 s, exit 0**, and it printed
`REGRESSED computations/full-twist-delta-n2-verification.witness.json`.
No gap. (My first attempt ran the hook **without stdin**, where it blocks
forever on `cat`; it reached 643 s and I was one step from filing "the hook
exceeds its own 130 s timeout so the q0 block never runs" — a measurement of my
own invocation, not of the hook.)

**"A drain of one q0 gate refilled another" is the wrong story.** Retracted in
full on `qou-3f7a`. `9c2058f0bd` re-ran a **bare producer** that emits no
provenance; the `q0Anchor: proton` it erased was hand-added downstream by
`a4d9906659` and was **wrong** — the cache is symbolic in q. So this is not a
new refill mechanism; it is the bare-producer class AGENTS.md already names.

**And my "12 strip events in 130 commits" was 4x too high.** That scan matched
diff LINES (`-"q0Anchor"` with no `+`), so it counted **JSON key reordering** as
stripping: `c29e0752bb` "stripped" nine anchors that are present before AND
after. Measured at the VALUE level (parse both revisions, compare the field):

    VALUE-LEVEL strips, 0465ce1ec5..HEAD (130 commits):  3
      6c5bb855a9  probes/arc-count-diagnostic-degeneracy   (repaired)
      6c5bb855a9  probes/bpp-higher-a-sparse               (repaired)
      9c2058f0bd  chi-neutron-h3                           (bare producer)

An earlier awk version of the same scan said **2**, because it reset the
filename before evaluating its print condition and could emit at most one hit
per commit. Three passes, three numbers; only the value-level one is quotable.

**Consequence for this bean:** the arrival-rate half is genuinely closed and
verified. The live regression rate is ~1 per 130 commits, and that one is a
producer defect rather than a committer error — so **do not upgrade the hook to
blocking on the strength of it.** The remaining work is the backlog, which this
bean already says not to drain.

## 2026-09-08: canonical ledger for the q₀-gate family is qou-1c4y (the AGENTS.md-named migration tracker); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3. Sixteen q₀-gate beans, ~10 % cross-reference density, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

Same as `qou-3f7a`: the q0-anchor refill ratchet is the pin axis, not the
convention axis. Keep open, re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.


## RETRACTION, same session — this bean was CORRECTLY parented and my verdict above was wrong (bean `qou-am5t`)

The 2026-10-10 verdict above says **REPARENT**, on the reasoning that this is the
q0/colour axis rather than the convention axis and therefore the wrong milestone.
**That reasoning is wrong, and `qou-cdx1`'s own title says so**:

> `MILESTONE: excise convention C, adopt proton pin + colour weighting (owner ruling 2026-08-15)`

Its body states the three rulings explicitly — **R1** convention D canonical / C
excised, **R2** proton pin canonical, **R3** `bring_color_weighted` canonical.
So the milestone is a THREE-RULING milestone, not a C-excision milestone, and a
q0-pin bean (R2) or a colour-weight bean (R3) sits under it by design.

My §9 paragraph calling the shared milestone an artefact of the two rulings
"landing in the same message" had it backwards: they share a milestone because
the milestone was scoped to cover all three, deliberately.

**This bean stays under `qou-cdx1`. It is not re-parented, and the REPARENT
verdict above is withdrawn.** Everything else in that verdict — that it is live
and worth doing — stands.

Third correction of this session, and the same class each time: a claim about a
bean made without reading that bean's own primary text closely enough. The first
was `qou-m7py` (called satisfied off one grepped line), the second was the
66-unscoped paper classifier.
