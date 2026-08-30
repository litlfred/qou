---
# qou-si7d
title: Wire the orphaned hook-sum/twist Common modules into QOU.lean and cross-reference the register bridge
status: completed
type: task
priority: normal
created_at: 2026-08-30T09:07:17Z
updated_at: 2026-08-30T09:14:34Z
---

Two decisions taken together on the hook-sum cluster, both "option A" of the
options put to the owner.

## Q1 — do NOT retire either hook-sum proof

The premise that one is a dead duplicate is false. `QOU/Common/TwistUnconditional.lean`
uses `HookSumComplete.hookSum_eq` in a real proof --

    rw [<- Nat.cast_sum, sum_hookLenP, hookSum_eq l M hsort hM]

-- to discharge a previously HYPOTHESISED hook-sum exponent in a
balanced-quantum-twist result, and it works natively in the list register
(`cellsOf l`, `hookLenP l c`). So each register has a native consumer: lists for
TwistUnconditional, YoungDiagram for the Lambda-star argument. Converting either
consumer costs more than the duplicate does.

Retirement was wanted to stop the two drifting apart. `HookSumRegisterBridge`
(qou-8r18) already does that: it stops compiling if either side moves. The
duplication is checked, which was the actual goal.

Only change here: `HookSumComplete`'s docstring did not know the bridge exists.
Adding the pointer, so whoever reads that file first learns there is a second
register and a proved equivalence.

## Q2 — wire the orphaned modules into QOU.lean

Four modules de-orphaned by three import lines:

- `QOU.Common.TwistUnconditional` -- the one that matters. Carries a real
  unconditional result and a real dependency, and no import-walking tool could
  see it. Importing it also de-orphans `QOU.Common.BalancedQuantumTwist`, which
  nothing else imports.
- `QOU.Common.HookSumGeneral` -- the arm half, predecessor of HookSumComplete.
- `QOU.Common.HookSumIdentity` -- `decide`-checked small shapes.

All three verified to compile standalone BEFORE wiring (direct `lean`, EXIT=0
each), so this is not expected to turn anything red.

Into `QOU.lean` rather than a new `QOU/Common.lean` umbrella: QOU.lean imports
leaf modules directly for 717 of its 781 imports, and qou-6mnt is precedent for
exactly this operation ("Wire 4 orphaned QGeometricLanglands section-3b carriers
into QOU.lean").

NOT deleting HookSumGeneral or HookSumIdentity. HookSumIdentity's `decide` cases
are a cheap INDEPENDENT check of an identity now proved twice in general, which
is worth more wired up than removed.

## Stale rationale corrected

`scripts/lean-orphan-modules.sh`'s header says wiring orphans up is
"owner-scoped (bean qou-kljb) because turning on hundreds of unbuilt modules at
once could be very red". qou-kljb is CLOSED, and closed on the finding that the
"never built" premise had already been retired by qou-rc7b's
`globs = ["QOU", "QOU.+"]` -- orphans ARE compiled. The header is what led me to
report this work as owner-blocked several times over. Corrected in the same
change, since this change falsifies it.


## Summary of Changes

**Q1 (retire nothing) — one docstring edit.** `HookSumComplete`'s module
docstring now records that the same identity is proved over `YoungDiagram` in
`QOU.BraidKnot.HookSum`, that each register has a native consumer
(`TwistUnconditional` here in lists, the Lambda-star argument there in
diagrams), and that `HookSumRegisterBridge` proves them equal — so a drift in
either stops the bridge compiling, which is the protection retiring one would
have bought. It also warns that the registers agree only ON A CELL.

**Q2 (wire all three) — four modules de-orphaned by three import lines** in
`QOU.lean`: `TwistUnconditional`, `HookSumGeneral`, `HookSumIdentity`, and
`BalancedQuantumTwist` reached transitively. Verified: all four compiled
standalone BEFORE wiring (direct `lean`, EXIT=0 each), so nothing was turned
red; afterwards none appears in `lean-orphan-modules.sh --list`, checked with a
control (a still-orphaned module the same grep does find), because four zero
counts and a broken grep look identical. Orphaned `QOU.Common` modules: 8 -> 4.

Into `QOU.lean` rather than a new `QOU/Common.lean` umbrella: 717 of QOU.lean's
781 imports were already leaf modules, and qou-6mnt is precedent.

**Stale rationale corrected, and it was load-bearing.**
`scripts/lean-orphan-modules.sh`'s header opened "list library modules no build
ever elaborates", described the lakefile as having "no globs key", and said
wiring orphans up was "owner-scoped (bean qou-kljb)". All three were true when
written; none is true now (qou-rc7b added globs; qou-kljb closed on exactly that
finding). I read that header as a live gate and reported this work as
owner-blocked to the owner several times before checking the bean. Header
rewritten, --help range repointed so it prints the corrected text, and the
summary line changed from "N NOT BUILT" to "N UNREACHABLE" with a note that
they ARE compiled — "not built" was the same false claim in the one place
people actually read.

## Noted, not fixed

- `QOU.Common.CyclotomicValueTruncates` and `PeriodicDense` still report as
  orphans even though modules DO import them — because those importers are
  themselves orphans. Second-order orphaning; out of scope here.
- `BalancedQuantumTwist` imports the deprecated `Mathlib.Algebra.GeomSum`
  (warning, not error). Pre-existing and unaffected by wiring: globs already
  compiled it, so the warning was already being emitted.
