---
# qou-3ral
title: 'Every witness guard sits on ONE of WitnessBuilder''s two write paths: save(extra) validates nothing, and 124 producers use only that route'
status: todo
type: task
created_at: 2026-09-04T21:23:12Z
updated_at: 2026-09-04T21:23:12Z
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
