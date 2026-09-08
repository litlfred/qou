---
# qou-m90h
title: Witness timing key "ms" is not in _EPHEMERAL_META_FIELDS — 28 witnesses report a false real-change on every re-run
status: todo
type: bug
priority: normal
created_at: 2026-09-07T11:01:32Z
updated_at: 2026-09-08T03:41:37Z
---

Found on PR #7061 while classifying witness churn from verification runs.

## The defect

`_EPHEMERAL_META_FIELDS` in `tools/qou-substrate/python/qou_substrate/witness.py`
masks ten keys:

    commitSha, computedAt, durationMs, durationSeconds, duration_sec,
    elapsed_s, elapsed_sec, elapsed_seconds, environment, scriptCommitSha

Four of those ten are wall-clock spellings. A fifth spelling, the bare key
**`ms`**, is NOT masked, and **28 witnesses under `computations/` carry it**.

Measured: re-running six `wlambda_covariance_epic_M1_*` producers produced
diffs whose ONLY changed line was

    - "ms": 32889
    + "ms": 34188

i.e. pure wall-clock. Under any comparison that strips the ten masked keys —
which is what the staleness paths and every ad-hoc agent classifier do — all
six read as **REAL VALUE CHANGE**.

## Why it matters more than it looks

This is a false positive that **cannot be drained and recurs on every run**.
Anyone comparing a witness before and after a re-run (staleness triage, a
producer-health sweep, an agent deciding whether its change moved a number)
gets a guaranteed hit on these 28 regardless of what the producer computed.
It is noise that looks exactly like signal, in the one place the corpus relies
on being able to tell them apart.

It is the same shape as the mask-gap rows in the detector-blindness taxonomy:
the mask is a LIST OF KNOWN SPELLINGS, and this is an unknown one. The set
already carries four spellings of "elapsed" and two of "duration", which is
itself the evidence that spellings proliferate faster than the list.

## The fix

Add `ms` to `_EPHEMERAL_META_FIELDS`. Cheap and safe — it is masked for
comparison only; the value stays in the file.

**Better, and the reason to look before typing the one-liner:** a key named
`ms` is ambiguous by construction. Verify each of the 28 is a duration before
masking — a field genuinely meaning milliseconds-of-something-measured would be
wrongly hidden. Spot-checked 6 of 28 (all `wlambda_covariance_epic_M1_*`); all
six are wall-clock. The other 22 are UNVERIFIED.

**Best, if someone owns this properly:** the producers should emit `durationMs`
and the ambiguous key should be retired, so the mask stops growing a spelling
at a time. That is a producer change across up to 28 files, not a one-liner.

## What is NOT claimed

Only `ms` was measured. Whether OTHER unmasked volatile keys exist in the
corpus was not checked, and the reasoning above says to expect some. A
systematic pass would diff a sample of witnesses across two no-op re-runs and
report every key that moved — that finds the class, not one member of it.


UPDATE, same session: the spot-check is now **10 of 28**, not 6. Four further
witnesses (`m1-kappa-structure`, `m1-kendall-route`, and re-runs of
`m1-kappa-large-n-sampler` / `m1-kappa-n-exact`) were dirtied by a still-running
background sweep after the first revert, and their diffs were **also `"ms"`
alone** — 4 changed lines, all of them `ms`. That is ten independent
confirmations and zero counter-examples. The other 18 remain UNVERIFIED.


UPDATE 2: the spot-check is **12 of 28**. Two further witnesses
(`m1-limit-closed-form`, `m1-monovary-route`) were dirtied by the same
background sweep and differed in **`"ms"` alone** — `157334 -> 144842` and
`439 -> 580`. Twelve independent confirmations, zero counter-examples; 16 of
the 28 remain unverified.

Note the second value went **down** (157334 -> 144842). A staleness reader
looking only at direction cannot use that either — it is wall-clock jitter in
both directions, not a monotone counter.

### Methodological trap, worth more than the extra two samples

The repeated re-dirtying was NOT the producers being nondeterministic. A
background sweep kept running after `TaskStop` reported it stopped:
`TaskStop` terminated the task wrapper, and the child `for f in ...; do
timeout 300 python3 "$f"; done` loop survived it and went on writing
witnesses. It took `pgrep -af` + `kill -9` on the child PIDs to actually
stop, and the task only reported `failed` afterwards.

Consequence for anyone measuring witness churn: **`git status` is not a
stable observation while a sweep may still be alive.** Check `pgrep` for the
producers before concluding that a revert held, or you will attribute your own
still-running loop to a nondeterministic producer. This cost three revert
rounds here.


--------

## 2026-09-08 — the stray-job hazard recurred the SAME session, and a second trap beside it

Two methodology findings from the session that filed this bean. Neither moves a
number; both are about measurements being wrong for reasons outside the thing
measured, which is this bean's subject.

### 1. A background job outliving its wrapper — SECOND instance, same session

This bean already records one: a sweep kept running after `TaskStop` reported it
stopped, and `git status` was therefore not a stable observation. It happened
again a few hours later with a different command.

`scripts/precision-gates.sh --changed` was started in the background. Its
harness task reported **completed, exit 0**. Fifteen minutes later a stop-hook
flagged four dirty witnesses, and `pgrep -af` found the script **still alive**
across four PIDs (wrapper, `timeout`, the script, and a `witness_provenance_audit.py`
child), still writing. It took `kill -9` on the PIDs to stop it.

So: **a completion notification is not evidence the process is gone.** Twice in
one session, two different commands. Treat "the task said it finished" as a
claim about the wrapper only, and confirm with `pgrep -af` before reading
`git status` as a measurement of your own work.

### 2. `GATE EXIT=$?` after a pipeline reports the PIPE, not the script

The same run was invoked as

    bash scripts/precision-gates.sh --changed 2>&1 | tail -25; echo "GATE EXIT=$?"

`$?` there is `tail`'s status, which is 0 essentially always. It printed
`GATE EXIT=0` while the gate was **RED** — and that 0 was quoted in a report
before the error was caught.

Run directly for the verdict: `python3 computations/witness_raw_float64_audit.py
--strict` exits **1**. Same class as everything else in this bean: a number that
looks like the measurement but is about the harness.

Use `PIPESTATUS[0]`, or `set -o pipefail`, or do not pipe the thing whose exit
code you intend to read.

### 3. A useful thing the gate says that is easy to miss

Its output ends with an instruction not to commit the witnesses it regenerates:

> DO NOT COMMIT THESE. Revert them: `git checkout -- computations/` … contended
> files that main regenerates on its own cadence, so committing one from a
> feature branch either walks a drain-only ratchet backwards (if this tree is
> behind main) or acquires a conflict that recurs until the branch merges (even
> at 0 behind). Both failure modes are measured; see bean `qou-v0t8`.

Worth knowing BEFORE running it, because the instruction arrives at the end of a
three-minute run whose output is easy to skim past — and the reflex on seeing
dirty witnesses is to inspect and decide, not to revert on sight. It also adds
the useful caveat that the diff is still worth READING: if the movement is your
own producer's, that is a real finding; it is the commit that is wrong, not the
measurement.
