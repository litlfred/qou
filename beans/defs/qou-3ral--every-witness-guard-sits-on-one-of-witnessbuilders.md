---
# qou-3ral
title: 'Every witness guard sits on ONE of WitnessBuilder''s two write paths: save(extra) validates nothing, and 124 producers use only that route'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T21:23:12Z
updated_at: 2026-10-04T15:12:30Z
parent: qou-5vkl
---


## The class

`WitnessBuilder` has **two write entry points**, and every guard added to it so
far sits on exactly one of them:

| route | what runs on it |
|---|---|
| `stamp_staleness_metadata(..., q0_anchor=…)` / `add_assertion(...)` | the guards — `_tolerance_literal` normalises a float tolerance to a string at `Assertion.to_dict`; `stamp_staleness_metadata` raises on `q0_anchor=True` |
| `WitnessBuilder.save(extra)` and hand-built `json.dump` | **nothing** |

`save(extra)` is three statements — `witness = self.build()`, `if extra:
witness.update(extra)`, then write the file. There is no validation of any kind
in it, and it is not a back door: the `witness.py` module header **documents**
`save({"q0Anchor": "comparison", ...})` and `save({"q0Anchor": "independent",
...})` as the intended route for the two tokens that cannot be resolved from
`computations/q0_anchor_manifest.json`.

So a producer can be scrupulous on the guarded path and still emit whatever it
likes on the unguarded one, and no detector keyed on the guarded path can see it.

## Measured twice, in two unrelated fields, by two sessions that did not know

**Instance A — the assertion-tolerance guard (not mine; PR #6453, `qou-9tqx`).**
That session's own words: *"every tolerance guard here keys on the construction
path. A producer that writes its payload by hand is invisible to it however
careful it is elsewhere."* Their measurement: the float64 drain holds for 489 of
499 witnesses and is **structurally undoable**, because **26 of the 33** producers
carrying a float-literal `"tolerance":` hand-build their witness with `json.dump`
and never construct an `Assertion`. Ten have already reverted. Cited as theirs,
not re-measured here.

**Instance B — the `q0Anchor` token vocabulary (mine).** Measured on
`origin/main` at `6b5df361ea5`:

```sh
# unguarded route: "q0Anchor": written as a dict-literal key
git grep -l '"q0Anchor":' origin/main -- 'computations/**/*.py' | grep -v /audits/ | wc -l
#   161
# guarded route
git grep -l 'q0_anchor *='  origin/main -- 'computations/**/*.py' | wc -l
#   425
# overlap
#    37   -> 124 producers use the UNGUARDED route exclusively
```

The `q0Anchor` vocabulary is five tokens (`muon`, `proton`, `ambiguous`,
`independent`, `comparison`) and is **enforced on neither route** — the guarded
one at least rejects the boolean `q0_anchor=True`; `save(extra)` rejects nothing.

## Why this is not merely tidiness: the refill is total

`qou-eggf` was filed against 17 witnesses that put prose in the token field. Set
difference over `*.witness.json` between `8ddfeaf1b7` (the commit it was filed
against) and `origin/main` today, on the dominant string
`'proton (experimental pin)'`:

```
15 out, 12 in, ZERO persisted
```

Not one original survives and not one current offender was there before. The
population was **replaced**, not partially drained. Over that same window net
stamped witnesses went 1494 -> 1785, so roughly **4 % of newly-stamped witnesses
arrive off-vocabulary** — and the growth is concentrated in exactly the two
tokens that must be typed by hand at the stamp site: `comparison` 5 -> 32
(+540 %), `independent` 90 -> 136 (+51 %), against `proton` at +16 %. So the
refill rate should be expected to **rise** as stamping adoption completes.

## Proposed detector-blindness taxonomy row

`docs/audits/2026-08-15-detector-blindness-taxonomy.md` had 26 rows at
`6b5df361ea5`; PR #6693 adds six more (27–32), all of which key on the *shape of
the data around a field*. None of the 32 is this class — the closest is row 21
(*the GUARD's TYPE*), which is explicitly scoped to one measured mpmath-vs-sympy
site and is about a helper a caller cannot invoke, not about a second write path
that bypasses the helper entirely. Checked before writing this.

| keys on | therefore misses | worked example |
|---|---|---|
| **the WRITE PATH** — the guard is installed at one of `WitnessBuilder`'s two entry points | a producer using the **other** entry point, however careful it is elsewhere — and for two of the five `q0Anchor` tokens the unguarded route is the *documented* one | tolerance: 26 of 33 producers hand-build, drain structurally undoable (#6453); `q0Anchor`: `save(extra)` is a bare `dict.update`, 124 producers use it exclusively |

## Scope — what this bean deliberately does NOT do

- **It does not add the guard.** PR #6654 owns the `q0Anchor` producer drain and
  states explicitly that *"whether to add a write-time guard is a real design
  question"* and is not smuggling it in. That call is theirs. The blast radius
  datum is posted on that PR: after their drain, a hard raise breaks one test
  that asserts verbatim pass-through of `""` plus three runtime-computed sites.
- **It does not edit the taxonomy.** PR #6693 is renumbering that file right now
  and is clean; a second PR touching the row count is a guaranteed conflict. The
  row above is written to be landed by whoever holds the file next — them in
  #6693, or me once it merges.
- **It does not touch `witness.py`.** Two live PRs are working its neighbourhood.

**Default if nothing is done:** nothing breaks today. The `q0Anchor` gate stays
red-on-arrival (which is `qou-z23u`'s thesis for why it gets skipped), the
tolerance drain stays structurally undoable, and both classes keep refilling at
a rate that rises with adoption.


## UPDATE 2026-09-04 22:40 — the drain merged, a guard landed, and it is TWO paths short

Three things changed within the hour, and one of them corrects this bean.

### 1. #6654 merged, and it ANSWERED the design question rather than deferring it

This bean recorded that #6654 *"states outright that whether to add a write-time
guard is a real design question"* and left it. It merged, and it **added the
guard**: `_warn_unmappable_anchor` + `Q0_ANCHOR_VOCABULARY` in `witness.py`. The
decision it reached is **warn, never raise**, for a reason worth preserving —
stamping happens *after* the compute, several producers run tens of minutes and
one past fifty, so discarding a run to correct a label is the worse trade. It
cites the owner's 2026-08-25 decision against a blocking pre-commit hook as the
same question already settled once.

**So the design question is closed and it is not mine to re-open.** What follows
applies their decision; it does not revisit it.

### 2. Their drain worked: off-vocabulary witnesses 14 → 3

Re-measured on `main` at `6a9c2c44fb9` with the same command:

| token | before | now |
|---|---:|---:|
| `proton (experimental pin)` | 12 | **2** |
| `not-applicable` | 1 | **1** |
| `none (exact symbolic identities in q)` | 1 | **0** |

The `+540 %` / `+51 %` growth figures above are the state *before* this drain and
should be read as historical, not current.

### 3. 🛑 CORRECTION TO THIS BEAN: there are THREE write paths, not two

The title and the whole argument above say **two**. Measured while checking
whether the new guard reaches the remaining offenders — it does not, and finding
out why turned up a route this bean did not know about:

| # | route | guarded? |
|---|---|---|
| 1 | `stamp_staleness_metadata(payload, q0_anchor=…)` | **yes** — `_warn_unmappable_anchor`, added by #6654 |
| 2 | `save(extra)` with `q0Anchor` in `extra` | no |
| 3 | **`wrap_legacy(name, payload)`** with `q0Anchor` in `payload` | no |

Route 3 carries the payload's keys into `_extra_top_level` and out through
`build()`, touching neither of the other two. Measured on `main`: **152
producers call `wrap_legacy`, and 22 of them set `q0Anchor` in the payload.**

**The one live off-vocabulary producer travels route 3.**
`codata_corpus_literal_scan.py` sets `"q0Anchor": "not-applicable"` at line 816
and calls `.save()` with **no** `extra` at line 898 — so neither the guard that
exists nor the `save(extra)` fix alone would ever have warned about it. I found
this by checking a claim I was about to make, having assumed it used route 2.

### What this branch does now

Both remaining routes get the same warn-only call, deliberately reusing
`_warn_unmappable_anchor` rather than writing a second policy:

- `save(extra)` — checks `extra` only, so a producer that stamps *and* passes
  `extra` warns exactly once (`stamp_staleness_metadata` warns only when
  `"q0Anchor" not in payload`, so its own guard is already skipped in that case).
- `wrap_legacy` — checks `payload` at entry, where `script_path` is in scope.

**Verified, 9 cases across both routes**, in a scratchpad harness driving the real
`WitnessBuilder` end to end (`build()`, the ephemeral-diff preserve logic, the
file write):

    save(extra)   bad-prose / bad-other -> WARN     good-comp / good-indep -> silent
                  no-extra / unrelated-key -> silent
    wrap_legacy   bad -> WARN            good / absent -> silent

In every case the token is written to disk **unchanged** — the guards warn, they
do not mutate, matching #6654's decision exactly.

### Still true, and still the point

The taxonomy row stands and is strengthened: the count in it should read **three
entry points**, not two. `#6693` still holds
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`, so the row is still
offered rather than added.


## ENUMERATED, not inspected — and there is a FOURTH route the library cannot reach

The correction above was found by inspection, which is how the two-vs-three
error happened in the first place. Enumerating instead:

### The library surface is exactly three, and all three are now guarded

Every `WitnessBuilder` entry point that accepts a caller-supplied dict, by
scanning the class for methods taking `payload` / `extra` / `witness`:

    1555  wrap_legacy(name, payload, ...)        -> guarded (this branch)
    1735  stamp_staleness_metadata(payload, ...) -> guarded (#6654)
    2126  save(self, extra=None)                 -> guarded (this branch)

There is no fourth method. **3 of 3.** That figure is now enumerated rather
than believed, which is the whole point of redoing it this way.

### Route 4: 23 producers bypass the library entirely

Producers that write `"q0Anchor"` and never import or mention `WitnessBuilder`
— they build a dict and `json.dump` it themselves. **No library guard can ever
reach these**, because the library is not in the call path at all.

Measured on `main` at `6a9c2c44fb9`, and the narrowing matters:

| | count |
|---|---:|
| files naming `"q0Anchor"` with no `WitnessBuilder` | 35 |
| — of those, READERS (audits comparing the field) | 12 |
| — **genuine hand-writers** (construct the key AND serialise) | **23** |

**Quote 23, never 35.** The first number counts audit scripts like
`q0_independence_checker.py` and `q0_pin_flip_test.py`, which *read* the field
to check it. Counting a reader as a writer is the same defect this bean is
about, one level down, and I made it once before narrowing.

**And 23 overstates the independence too:** 19 of them are the single
`wlambda_covariance_epic_M1_*` family, so this is roughly five distinct
authoring decisions, not twenty-three. (Same inflation as the per-witness
sampling AGENTS.md records, where 119 of 268 witnesses shared one producer.)

### Route 4 is LATENT, not live

Every one of the 23 currently emits an in-vocabulary token — `proton` ×5,
`independent` ×18. **Zero off-vocabulary.** So this is a gap in coverage, not a
defect to drain, and it is stated as such: nothing is broken there today.

What it bounds is the claim this branch can make. The fix closes the arrival
rate **for producers that use the library** — which is where all three
historical off-vocabulary populations came from, including the one live
offender. It does not and cannot close it for the 23, and a future refill could
arrive through them with nothing to say a word.

The honest options for route 4, none taken here: a static check in
`q0_anchor_consistency_audit.py` keyed on the producer source rather than the
witness; migrating the 23 onto `wrap_legacy` (which exists for exactly this and
is what `codata_corpus_literal_scan.py` already does); or leaving it, since it
is clean and the audit already catches the *output* CI-failingly. Left for now
because none of the three is this branch's scope and the last is defensible.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- **Round 93 (`litlfred/qou#8421`)**: Advanced in `feat/round93-strip-kindratio-kohnokz-resolvent-affinenorm-43c1` (Commit 1 `53341df5af4d7e77e4fbee34d9b0bead3b0b6187`, Commit 2 `2f40c0d2d071ec6bb42d20002fb53171245df01c`, probe sha256 `3d8255f15bbdfc2d9c41114f8ac21a1bec3996e0b1546ef080914210757c628c`).
