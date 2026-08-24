---
# qou-1ugy
title: 'lean-verify-changed --build-missing gives up one level deep: build_qou_module does not recurse on its own missing QOU upstreams'
status: completed
type: task
priority: normal
created_at: 2026-08-24T06:34:47Z
updated_at: 2026-08-24T06:54:55Z
---

Claimed by claude/q407-self-assuming-projections-2026-08-21

## What was wrong

`--build-missing` exists so a verification run can rebuild a stale QOU upstream
from current source instead of trusting the dated olean snapshot. It gave up
**one level deep**, and the caller could not tell that it had.

`build_qou_module` compiled one module and returned its status. If that module
was itself missing an upstream, `lean` failed, the function returned 1, and the
retry loop `break`ed. It also swallowed lean's output (`>/dev/null 2>&1`), so a
REAL compile error in an upstream and a missing sub-dependency were the same
non-zero to the caller.

Measured on the merged q407 branch: it built `QOU.Mathlib.NonAbelianStokes`,
then `QOU.Mathlib.HeckeAlgebra` failed on `QOU.MathlibExt.QPartitionCombinatorics`
and the run stopped. The file under test was reported

    UpstreamSubstrateBridge.lean   MISSING-OLEAN (module QOU.Mathlib.HeckeAlgebra)

which reads as "the cache is short one module". The truth was "the cache is
short a whole cone, and this script stopped after the first one". 5 of 16
changed files were unverified for that reason.

## The other half: stale-but-PRESENT oleans

`--build-missing` only ever fired on lean's `does not exist`. A stale olean is
*present*, so it was used as-is — and that does not fail safely, it produces a
confident wrong ERROR:

    QOU/Mathlib/UpstreamSubstrateBridge.lean:174:35: error: Application type
    mismatch: ... yekutieli_finite_slice_substrate Y

The file is fine. `origin/main`'s own copy fails identically (at line 158,
before this branch's 16-line insertion shifted it), and the error disappears
once `NonAbelianStokes` is rebuilt from current source — which succeeds, with
linter warnings only. Every `QOU/**.olean` is dated **2026-07-19** while every
source is current, and `scripts/lean-olean-cache-seed.sh` excludes paper oleans
*by design*, so nothing refreshes them. An agent reading that ERROR goes hunting
for a proof bug that was never there.

## Fix

1. `build_qou_module` recurses on its own missing QOU upstreams, with
   `_MOD_SEEN` / `_MOD_OK` sets so a diamond costs one build and an import
   cycle terminates. Its failure reason is surfaced in `$_BUILD_ERR` and
   printed, so "cannot build X — compile error in X" and "cannot build X —
   non-QOU olean missing" are no longer the same silence.
2. A freshness pass (`ensure_fresh` / `freshen_cone`) walks each file's QOU
   import cone **post-order** and rebuilds anything whose olean is older than
   its source. Rebuilding an upstream invalidates everything compiled against
   the old one, so a rebuilt module propagates "you must follow" to its
   dependents via exit status 10 — without that, the cone half-rebuilds and the
   type mismatch survives one level down.

`LEAN_NO_REBUILD_STALE=1` restores the old behaviour.

## Measured

```
before (snapshot only)          15 exit 0,  1 error,  0 unverified
after recursion, partial scratch 11 exit 0,  0 error,  5 unverified
after recursion, full run        16 exit 0,  0 error,  0 unverified
after freshness pass             16 exit 0,  0 error,  0 unverified   (14 stale rebuilt)
```

**Cost, stated plainly:** after a mathlib or toolchain bump every olean is older
than its source, so this approaches a full QOU rebuild. That is the accepted
trade — a slow true answer over a fast false one — and it is the owner's ruling
of 2026-08-24, taken over the cheaper "report stale as UNVERIFIED".
