---
# qou-m90h
title: Witness timing key "ms" is not in _EPHEMERAL_META_FIELDS — 28 witnesses report a false real-change on every re-run
status: todo
type: bug
priority: normal
created_at: 2026-09-07T11:01:32Z
updated_at: 2026-09-14T19:47:46Z
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


--------

## 2026-09-13 — re-measured after 412 commits: the finding HOLDS, my own count did not

Five days and 412 commits of `main` later. Re-measured before re-asserting anything,
which is what this bean exists to make routine.

### The finding stands

`ms` is **still absent** from `_EPHEMERAL_META_FIELDS`. Live set, measured:

    commitSha, computedAt, durationMs, durationSeconds, duration_sec,
    elapsed_s, elapsed_sec, elapsed_seconds, environment, scriptCommitSha

Ten entries, four of them timing spellings, and the bare `ms` is not one of them.
So every masked-comparison consumer still reads an `ms` jitter as a real value
change.

### CORRECTION to my own figure: 28 -> 24

This bean's headline said **28 witnesses under `computations/`**. Measured today:
**24**. I cannot re-measure the past, so I do not know whether 28 was wrong when
written or whether four have since been deleted or regenerated without the key —
but the number in the bean is not the number in the tree, which is precisely the
staleness class the bean is about. Quoting it without re-running was the risk;
re-running was cheap.

### And the scope was LOOSER than it needed to be

"under `computations/`" is true and unhelpful. All **24 of 24** live in a single
directory:

    24  computations/deltalambda
     0  everywhere else

All values are `int`. That is a sharper fact than the bean recorded and it changes
what the fix looks like: this is **one producer family**, not a scatter across the
corpus. Emitting `durationMs` at that family's witness builder would drain the
whole population, without touching the ambiguous-key question anywhere else.

### What is still NOT established

Whether all 24 are durations. The earlier note verified 12 of the then-28; today's
re-measure counts and locates the key, it does not re-verify semantics. So the
caveat against blind-masking `ms` stands unchanged — a field genuinely meaning
milliseconds-of-something-measured would be wrongly hidden, and the producer-side
fix avoids that question entirely.

## 2026-09-14 — the remaining 16 are verified, and there IS a counter-example. Do NOT type the one-liner.

This bean records *'twelve independent confirmations, zero counter-examples; 16
of the 28 remain unverified'*, and asks for the rest to be checked before
masking. Done — by **reading the producers** rather than re-running them, which
is cheaper and does not dirty the tree.

### The population splits three ways, not one

| shape | count | files |
|---|--:|---|
| top-level `/ms`, scalar int | **24** | the `m1-*` family, `a3-mirror-selection`, `wn-tower-domain`, `qbeta-d-ladder-attack-options`, `c-frame-conditionality-audit` |
| nested per-row `ms`, scalar int | **2** | `b1-kappa-window-extension` (`/data/rows[i]/ms`), `atom-nf-q-degree` (`/data/cross_check/stock_cases[i]/ms`) |
| **`ms` is a LIST of consecutive ints** | **2** | `qbeta-habiro-all-10-pairs-phi8-universality`, `qbeta-habiro-delta-am-partial-sum-scan` |

### 🛑 The two lists are NOT wall-clock — they are the plural of `m`

Both producers, at `qbeta_habiro_all_10_pairs_phi8_universality.py:206` and
`qbeta_habiro_delta_am_partial_sum_scan.py:221`:

    ms = sorted(delta_a.keys())
    M_max = max(ms)

`ms` is the sorted list of **Habiro `a_m` differencing indices** — the plural
of the index `m`, nothing to do with milliseconds. In the witness:

    /data/n_minus_p/ms   = [0,1,2,3,4,5,6,7,8]        M_max = 8
    /data/D_minus_n/ms   = [0,...,12]                 M_max = 12
    /data/He3_minus_D/ms = [0,...,15]                 M_max = 15

This bean anticipated exactly this shape — *'a field genuinely meaning
milliseconds-of-something-measured would be wrongly hidden'* — and the real
counter-example turns out to be sharper than the one imagined: not a different
duration, a different **part of speech**.

### Why that kills the one-liner

`_strip_ephemeral_fields` (`witness.py:2631`) is **RECURSIVE** — it removes the
key from dicts *and* walks lists, at any depth. So adding `ms` to
`_EPHEMERAL_META_FIELDS` strips `/data/<pair>/ms` in both Habiro witnesses.

The set's own comment already carries the precedent for refusing this:

> `wall_sec` — also in the corpus, also a duration — would need BOTH halves and
> is **deliberately NOT added blind**; see `qou-ywee`.

and the docstring at :2658 names *'the recursive-mask collision-risk note'*.
This is that risk, realised.

### Honest mitigation, stated because it weakens my own claim

**`M_max` sits beside `ms` in all four blocks**, so masking would not lose the
*range* — the endpoint survives. What it loses is the index **set**: `ms` is
`sorted(delta_a.keys())`, so a GAP (an absent `m`) moves `ms` and leaves
`M_max` unchanged. So the loss is real but narrower than 'the range disappears'.

### What I did NOT do

No fix. The mask is shared infra in `qou-substrate`, and a type-aware or
path-scoped mask is neither a precision increase nor corpus-fixed — the corpus
fixes that `ms` is ambiguous, not which disambiguation to adopt. Under the
2026-09-07 ASK-THE-OWNER directive that waits, and the `wall_sec` precedent
says the same.

**Options, for whoever takes it:**

1. **Type-aware mask** — strip `ms` only when its value is a scalar int/float.
   Smallest change; leaves both lists intact. Risk: a mask that branches on type
   is a new kind of rule in that set.
2. **Path-scoped mask** — strip only top-level `/ms`. Covers 24 of 26 durations,
   leaves the 2 nested per-row ones flagged and both lists intact.
3. **Rename at the producers** (this bean's own 'best') — emit `durationMs`, and
   the ambiguity disappears because the Habiro `ms` means something else and
   keeps its name. Up to 26 files.

**The 28-file false-positive stands** and is unaffected by any of this: 26
genuine durations still read as REAL VALUE CHANGE on every re-run.
