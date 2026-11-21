---
# qou-fjcd
title: 'METHOD DEFECT: lean-direct consumer verification reads STALE oleans'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T15:43:36Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
---


## The defect

`lean`-direct verification (`LEAN_PATH=<olean dirs> lean <file>`) reads
the *edited file* from source but every one of its **imports from
compiled `.olean`s**. So:

> After editing file `A`, running `lean B.lean` where `B` imports `A`
> verifies `B` **against the old `A`**. It cannot see your change.

The run prints `OK` and means nothing.

## How it was caught

While fixing `MarkovTrace.lean` (bean `qou-t7zg`) I wrote a probe proving
`markovTrace n x = 0` from the buggy axiom, fixed the axiom, and re-ran
the probe expecting it to fail. **It still passed** — because the probe
imports `QOU.HeckeAlgebra.MarkovTrace` and got the stale olean. Only
after

```bash
lean -o .lake/build/lib/lean/QOU/HeckeAlgebra/MarkovTrace.olean \
     QOU/HeckeAlgebra/MarkovTrace.lean
```

did the probe correctly fail.

## What this invalidates

**PR #4750 (merged).** Its "Verification" section claims `lean`-direct
exit 0 on every de-laundered class *and every consumer*. The class checks
were valid (the edited file is read from source). **The consumer checks
were not** — `CasimirEpsilonVacuum`, `CasimirModeCountFunctor`,
`Conjectures`, `TwoFiltrationBridgeGeneral`,
`TwoFiltrationBridgeSmallCases`, `WardFiltrationCounting`,
`QGeometricLanglands` were all compiled against oleans that still
contained the global instances I had just removed.

**Re-done correctly afterwards** (rebuild all 8 class oleans, then
re-check the 7 consumers): all still exit 0. So the *conclusion* in
#4750 holds and nothing needs reverting — but it held by luck, not by
the check I said I ran. Recorded rather than quietly re-run, because the
claim in a merged PR body was stronger than the evidence behind it.

## Correct recipe

```bash
# 1. rebuild the olean of every file you EDITED, in dependency order
lean -o .lake/build/lib/lean/QOU/<Path>.olean QOU/<Path>.lean
# 2. only then check consumers
lean QOU/<Consumer>.lean
```

Rule of thumb: **`lean`-direct verifies exactly one file — the one on the
command line.** To verify a *cone*, you must rebuild the cone's oleans
bottom-up first. `lake build -R <Module>` does this correctly but is the
40-minute path the lake-cache workflow exists to avoid.

## Follow-up

- Fold the recipe into
  [`lean-environment-setup.md` §"VERIFY a single file with lean-direct"](.claude/skills/local/lean-environment-setup.md),
  which currently documents the single-file case and does **not** warn
  that consumer checks are stale. That omission is what produced this.
- Wrap it in a script (`scripts/lean-verify-cone.sh <edited...> --
  <consumers...>`) so the rebuild step cannot be skipped by hand.
- This compounds the earlier lesson from bean `qou-gdc1` (stale oleans
  make healthy files *look red*). Same root cause, opposite symptom:
  there, stale deps invented failures; here, stale deps hide them. Both
  say the same thing — **an olean-backed check is only as fresh as its
  oleans.**

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

**Completed.** The correct recipe exists on main: `scripts/lean-verify-cone.sh` (edited files rebuilt first, consumers checked after) and `scripts/lean-direct-cone.sh` with freshness from `scripts/lean_freshness.py`. This session's whole-library sweep used the latter, so consumers were checked against freshly rebuilt oleans.
