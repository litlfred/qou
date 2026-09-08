# A long compute launched with `setsid nohup` does not survive a session boundary

Bean `qou-6cm9`. Measured 2026-09-08 in a Claude Code remote container, while running
the ⁴He Ω₂ sparse probe (`qou-za3q`) and the triton far-commutativity
verification (`qou-5mxd`).

## The claim

Both compute jobs were launched detached:

    setsid nohup timeout 10800 python3 -u <probe>.py >> log 2>&1 < /dev/null &
    disown

**Both were killed at the next session boundary. Twice each.** The processes were
simply gone (`ps` empty), with no traceback and no completion line — the logs
just stop.

By contrast, a job launched through the **Bash tool's own `run_in_background`**
(harness-tracked, given a task id and an output file) ran for roughly 30 minutes
across turn boundaries and delivered a completion notification.

## What it cost

The second ⁴He cycle banked **zero** partitions. It resumed 52/77, printed its
resume line, and was killed within seconds; the log's last write was 2455 s before
it was noticed. About 41 minutes of wall clock produced nothing.

This is the same failure the ORIGINAL stalled session hit — it reached 63/77 and
lost the run — and the same one that lost the triton dense baseline at its
timeout. Three losses, one cause.

## The rule

Launch any compute expected to outlive the current turn through the harness's
background mechanism, **not** `setsid`/`nohup`/`disown`. `nohup` defends
against SIGHUP; it does not defend against the container suspending or the
session's process group being reaped, which is what actually happens here.

AGENTS.md §"Long-compute logging discipline" prescribes
`python3 -u script.py 2>&1 | tee /tmp/<script>.log` and is right about the
logging. It says nothing about **which backgrounding mechanism** to use, and the
obvious shell idiom is the one that loses the work. Both can be had at once —
the harness task runs the `| tee` pipeline as its foreground command.

## Follow-up measurement, same day: the harness tasks SURVIVED — partially decisive

Relaunched through `run_in_background` and re-checked 31 minutes later, across a
scheduled check-in boundary:

| | before | after 31 min |
|---|---|---|
| ⁴He banked partitions | 52/77 | **58/77** |
| triton banked rows | 13/30 | **19/30** |

Both process groups were alive with ~1870 s elapsed, i.e. they ran continuously
through the gap. Under `setsid`, the comparable gap produced **zero** banked
units. So the mechanism is the difference, and the rule stands.

## What is STILL not established — and it is the discriminating case

**This boundary did not fire a `SessionStart:resume` hook; the ones that killed
the `setsid` jobs did.** So what has been shown is that a harness-tracked task
survives a ~31-minute idle gap. It has *not* been shown to survive the heavier
resume that reaped the detached jobs, because that event did not occur here.

Do not read "survived a boundary" as "survives a resume" — they are different
claims and only the weaker one is measured. If a harness task is later observed
dying at a resume, the rule narrows to: only per-unit checkpointing preserves
anything, and the interval between boundaries bounds how long a single work unit
may take.
- **Why** the detached jobs die. Container suspension, process-group reaping and
  cgroup cleanup are all consistent with the observation; nothing here separates
  them.

## The corollary that matters more than the mechanism

Whatever kills them, **a partition that takes longer than the interval between
boundaries can never be banked**, because the checkpoint is written per
completed unit. The ⁴He tail runs to dim 7700 against the dim ~2100 where it
currently sits, so this is a live risk for that run and not a hypothetical.
Per-unit checkpointing is the only thing that has actually preserved progress
here: it survived both kills, and it is why the run stands at 52/77 rather than 0.
