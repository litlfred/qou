---
# qou-6cm9
title: Long computes launched with setsid/nohup DIE at session boundaries; the harness's own run_in_background survives — 3 losses traced to this
status: in-progress
type: bug
priority: high
created_at: 2026-09-08T06:02:23Z
updated_at: 2026-09-13T13:01:24Z
parent: qou-9c80
---

## UPDATE 2026-09-08: harness tasks survived a 31-min boundary

Relaunched via run_in_background; re-checked 31 min later across a scheduled
check-in. He4 52 -> 58 banked, triton 13 -> 19 rows, both process groups alive at
~1870s elapsed. Under setsid the comparable gap banked ZERO. Mechanism confirmed
as the difference.

STILL NOT the discriminating test: this boundary fired no SessionStart:resume
hook, and the boundaries that killed the setsid jobs did. "Survives a 31-min idle
gap" is measured; "survives a resume" is not.


---

## 2026-09-13 — the nohup half is now MEASURED three times; the resume test is running

Claimed and in progress. This bean's open question is *"survives a 31-min idle
gap is measured; survives a RESUME is not"*. Both halves now have evidence.

### The nohup half — confirmed, three times in one session

`scripts/hkt-resume.sh:94` launches the `qou-uiut` table with
`nohup env … python3 … &` + `disown`. Across three `SessionStart:resume`
boundaries today it was killed every time:

| boundary | table | notes |
|---|---|---|
| 11:38:02 | killed mid-⁴He | ~6 min of that atom lost; 6 atoms banked |
| 12:25 | killed | and the `nohup`'d supervisor died WITH it |
| 12:54 | killed | had banked deuterium first |

The 12:25 datum is the sharpest: I had written `.work/hkt-supervise.sh` to
poll-restart the table, launched it the same way, and **the boundary killed the
supervisor too**. A supervisor inside the thing it supervises cannot outlive it,
so that approach cannot close this bean.

### The resume half — now running, and it is the discriminating test

`.work/hkt-foreground.sh` runs the table **in the foreground** of whatever
launches it, and it was started as a harness `run_in_background` task
(`b5pomrilh`) at 4/19. The harness owns the process group. If it is still alive
after the next `SessionStart:resume`, the mechanism is confirmed as the
difference and `hkt-resume.sh` should stop using `nohup`; if it dies, the
boundary kills everything and the only viable pattern is restart-on-turn-start.

It keeps both of `hkt-resume.sh`'s safety properties rather than trading them
for lifecycle: the LP-kernel gate (without
`lp_accumulator_step_traces_mpfr` the run violates the braid relation, and the
failure is silent — A=1 reproduces byte-identically and it diverges only at
compounds) and the single-producer guard.

### Related, for whoever closes this

The **memo is what makes the loss survivable**, and it is worth not deleting by
reflex. Measured across the 12:25 boundary: `.work/kernel-memo/` went 1329 →
1520 entries and persisted, so the restart resumed partway through the atom in
flight rather than from its start. A recycle costs the un-memoised remainder of
one atom, not the atom.
