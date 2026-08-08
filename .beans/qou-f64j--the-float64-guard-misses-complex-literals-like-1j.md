---
# qou-f64j
title: 'The float64 guard misses complex literals (`1j`, `2j*pi`) — a whole entry-point class'
status: todo
type: bug
priority: medium
tags:
    - infra
    - ci
    - qou-f64g
    - precision
created_at: 2026-08-08T17:30:00Z
updated_at: 2026-08-08T17:30:00Z
---

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
