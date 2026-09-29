---
# qou-f64j
title: DONE — the diagnosis was WRONG. Complex literals were already covered; CALL ARGUMENTS were not, and the guard reported CLEAN on seven of them
status: completed
type: bug
priority: medium
tags:
    - infra
    - ci
    - qou-f64g
    - precision
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-09-26T11:03:24Z
---

## ✅ DONE 2026-08-10 — and this bean's own diagnosis was wrong

Fix on **#4777**, which owns the guard (`2f8631197f`); this bean and the probe
repair are on #4701. Measured in place on the gates branch at `c9078fbcb7`,
against `origin/main` **`1b8b30758b`**.

**D1 was already implemented.** `visit_Constant` has a `complex` branch: `0.1j`
is flagged, `1j` / `2j` / `0.25j` are allowed because they are *exactly
representable* — a documented decision, not an oversight. This bean's headline
was **false** by the time it was read. Checking before fixing is what caught it.

**What was actually missing is bigger**, and it is the failure the guard exists
to prevent, committed by the guard itself: a lossy float literal handed to a
**call** was in neither the `arithmetic` nor the `constructor` context, so it was
dropped. A file with seven such entry points reported **clean**:

```
sqrt(0.1)   findroot(f, 0.1)   quad(f, [0, 0.1])   complex(0.1, 0)
```

Two rules added — `float-call-arg` (any call argument, walking container
literals; tolerance comparisons stay exempt) and `complex-call` (`complex(...)`,
the exact analogue of `float(...)` one type up).

### D2 — the backlog jump, attributed

| version | hits | files |
|---|---|---|
| baseline `c9078fbcb7` | 17,607 | 2,192 |
| `+ float-call-arg` | 18,779 | 2,239 |
| `+ complex-call` | **19,114** | **2,244** |

**+1,507 hits in +52 files**; +1,172/+47 from the call-argument rule, +335/+5 from
`complex(...)`. The gate is `--diff`-scoped, so the backlog blocks nothing.

### ⚠⚠ The new rule earned its keep on its FIRST run, in this lane's own probe

`qbeta_5two_route29_root_structure_probe.py` used
`complex(t), complex(y2), complex(y3)` and then compared against a stated
tolerance of `1e-20`. **Binary64 resolves ~1e-16**, so the check read as 1e-20
and was in fact "do these agree to float64". Removing the rounding made G6 fail
at 147 of 699 points, with a worst discrepancy of **2.65** — not noise.

And the failure was *also* not a mathematical error. Sorting on `(re, im)` is
unstable exactly there: the conjugate pair has equal real parts in exact
arithmetic, `polyroots` returns them differing at ~1e-40, and the sort then
orders by that noise and can invert the pair, mis-pairing `a+bi` with `a−bi` for
a difference of `2|Im y| ≈ 2.6`. **The float64 rounding had been hiding the
fragility** by making the two real parts bit-identical, so the tie-break fell to
`im` consistently in both lists.

Repaired by matching **nearest-neighbour in both directions** instead of by
sorting. G6 passes at working precision. Two lessons, both worth keeping:

* a tolerance below the precision of the values being compared is not a
  tolerance, it is decoration;
* removing a float64 downgrade can expose a *fragile comparison* rather than a
  wrong answer — and the fragile comparison was the real defect.

### D3 — sibling classes, checked rather than guessed

| class | status |
|---|---|
| `complex(...)` calls | ✅ now flagged |
| `math` / `numpy` / `cmath` / `statistics` / `scipy` imports | already flagged |
| `**0.1` on an `mpf` | already flagged (`float-in-arithmetic`); `**0.5` correctly allowed, dyadic |
| lossy float inside a list/dict passed to a call | ✅ now flagged (walked) |
| `round()` on an `mpf` | left alone — mpmath's `__round__` returns an `mpf`, so it is not an entry point |

No false positives: clean on both branches' diffs and on Routes 36–39, and the
four control paths (clean / dirty / missing / empty) all still behave.

## What

`scripts/probe-float64-guard.py` (PR #4777) flags `float(...)` calls, float
literals feeding `mpf` arithmetic, and `round()` on an `mpf`. It does **not**
flag Python **complex literals** — `1j`, `2j`, `0.5j` — which are float64
entry points exactly as much as `1.0` is.

Found 2026-08-08 during `/prepare-merge` on
`computations/probes/qbeta_5two_route19_transport_repaired_probe.py`, which
contained **seven** float64 entry points. The gate reported **one**:

```
line 89   round(float(im(prev - s) / (2*pi)))      <- FLAGGED
line 85   exp(1j * ph)                             <- missed
line 89   2j * pi * ...                            <- missed
lines 103, 120, 135, 145, 147, 174   exp(1j * ...) <- missed
```

## Why it matters, and why it is only priority medium

`1j` is **exactly representable** in binary64, so `1j * ph` promotes to `mpc`
with no precision loss for that factor — which is why the Route 19 witness was
**bit-identical** after the fix (36 fields, 0 changed). The class is mostly
benign in practice.

It is not benign in principle, and the gate's value is precisely that a reader
should not have to reason about which literals happen to be exact:

* `0.1j` is **not** exact. Nothing in the current ruleset would catch it.
* `2j * pi` mixes a float64 literal with an `mpf` — the product is `mpc`, but
  the written form invites `2j * 3.14159...` in the next edit.
* A gate that catches 1 of 7 entry points in a file, and reports **clean** on
  the other 6, is a smaller version of the failure this whole gate exists to
  prevent: **reporting a pass for something it did not check.**

That last point is why this is worth a bean rather than a shrug.

## Attack vectors

### D1 — Add `ast.Constant` complex detection to the existing Finder
The guard already walks the AST. A complex literal is `ast.Constant` with
`isinstance(node.value, complex)`. Flag it with the same message shape as the
float-literal rule, suggesting `mpc(0, 1)` / `mpc(re, im)`. **~5 lines**, same
place as the existing float-literal rule. This is the whole fix.

### D2 — Decide the annotation story before turning it on
There are ~3200 Python files under `computations/`. Turning D1 on will add hits
to the measured backlog (currently 17596 in 2186 files at `origin/main`
`ee66f30102`). Since the gate is `--diff`-scoped, that does **not** block work —
but the survey number will jump and should be re-quoted with its base sha, per
`qou-mfst`'s format rule. Measure before and after and say which part of the
jump is the new rule.

### D3 — Check for sibling classes while in there
Worth one pass for other unflagged entry points: `complex(...)` calls,
`math.*` functions (`math.log` vs `mpmath.log`), `numpy` scalars, and `**0.5`
(float exponent) on an `mpf`. Do **not** guess which exist — grep for them and
report the counts, then decide.

## Do this first

D1 plus the D2 measurement, in one change. It is small, and the honest framing
in the PR should be that the gate previously reported clean on files containing
this class — including one of this lane's own probes.

## Refs

* `qou-f64g` (parent — the gate itself), `qou-brkp`
* Gate: `scripts/probe-float64-guard.py`, PR #4777
* Found in: `computations/probes/qbeta_5two_route19_transport_repaired_probe.py`,
  fixed on PR #4701 (witness bit-identical, so a hardening not a correction)

**The 5₂ sum rule remains verified to 80 dps, unproved.**
