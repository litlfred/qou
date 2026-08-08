---
# qou-gdc1
title: 'GAP: SkeinObservationBridge is red on main — blocks lean-direct on the Skein cone'
status: completed
type: task
priority: normal
created_at: 2026-08-08T01:30:01Z
updated_at: 2026-08-08T07:22:26Z
---


## Finding

`content/quantum-observable-universe/lean/QOU/Information/SkeinObservationBridge.lean`
does not compile against current `main` + the v4-24-0 olean cache. Found while
running the lean-direct verification gate for PR #4687 (the file is untouched by
that PR — this is pre-existing red on `main`).

Errors (lean-direct, exit 1):

- `:120:2` unknown identifier `reaches_of_descent_of_forward`
- `:281:54`, `:291:68`, `:301:5` — `QCollatz` applied to `Skein`, but `QCollatz`
  has type `Type` (arity drift: it lost a parameter, or the call sites gained one)
- `:312:65` `ComputationalHorizon.c` does not exist
- `:318:4`, `:318:50` — `ComputationalHorizon.numLeaves`, `.numLeaves_eq` do not exist

So both `QCollatz` and `ComputationalHorizon` changed shape upstream and this
consumer was never updated.

## Impact

Blocks lean-direct verification of anything importing it — notably
`SkeinNPEncoding.lean`. PR #4687 made a doc-comment-only edit there and had to
ship it un-machine-checked for exactly this reason.

## Next honest step

Find the commits that changed `QCollatz`'s arity and `ComputationalHorizon`'s
fields, then update this consumer to match. Not attempted in #4687: it is a
multi-error breakage in an unrelated module, out of that PR's scope.

## CORRECTION (2026-08-08) — the original diagnosis above was wrong

Two of the three claims in the Finding section do not survive contact with a
from-source rebuild. Recording the correction rather than editing it away:

- **"`ComputationalHorizon` field renames" — WRONG.** `ComputationalHorizon`
  has `c`, `numLeaves`, and `numLeaves_eq` in source and builds clean from
  source, `sorry=0`. The `Invalid field` errors were **stale-olean artifacts**:
  the restored `lake-cache/qou-v4-24-0` payload (seeded 2026-07-02) carries an
  older `ComputationalHorizon.olean` predating those fields.
- **"`QCollatz` arity drift" — WRONG, and a knock-on of the same staleness.**
  `QCollatz` is still `class QCollatz (Skein : Type u) [CommRing Skein]`. It
  read as `Type` only because `QCollatz.lean` itself failed to build, so the
  consumer loaded the stale cached olean.
- **`reaches_of_descent_of_forward` "unknown" — also a knock-on.** It is
  declared at `QCollatz.lean:439` and resolves fine via the `open`.

**Actual root cause: namespace drift, twice — the same bug class as
`SuperPolynomial.of_le` (PR #4687).** Declarations sat in an ambient namespace
while every caller used the qualified name:

1. `QCollatz.lean` — `inDomain`, `domainStable`, `domainStable_forward` were in
   ambient `QOU.AppendixSurreals`, but referenced as `QCollatz.inDomain` /
   `QCollatz.domainStable` (and so named in a sibling's docstring). Wrapped in
   `namespace QCollatz`.
2. `collatz_substrate_link.lean` — `def toSkeinCollatzArith` was ambient while
   used as `sp.toSkeinCollatzArith`; the very next declaration already called
   itself `SubstrateParameter.toSkeinCollatzArith_q`. Qualified the def.

## Method note — do not trust the olean cache for a red-file diagnosis

A "red on main" call made against the restored cache is unsound: the cache is
a month-old snapshot, so a stale dep produces `Invalid field` / `Function
expected` errors that look exactly like real upstream drift. **Rebuild the
whole cone from source before declaring any file red.** Three of the four
symptoms here were cache artifacts.

## Resolution

Fixed; all 15 modules in the consumer union cone build lean-direct, `sorry=0`.
`SkeinNPEncoding` — un-machine-checkable during PR #4687 — now verifies.
