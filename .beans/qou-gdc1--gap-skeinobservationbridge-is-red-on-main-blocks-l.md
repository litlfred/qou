---
# qou-gdc1
title: 'GAP: SkeinObservationBridge is red on main — blocks lean-direct on the Skein cone'
status: todo
type: task
created_at: 2026-08-08T01:30:01Z
updated_at: 2026-08-08T01:30:01Z
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
