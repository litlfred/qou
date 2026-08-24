---
# qou-w7sc
title: Migrate the 20 ArchimedeanSubstrateField call sites onto ArchimedeanRealisation
status: todo
type: task
priority: normal
created_at: 2026-08-24T08:50:28Z
updated_at: 2026-08-24T08:50:28Z
---

Follow-up from `qou-d8m1`, which made the tie **available** but did not force anything through it.

## State after qou-d8m1

`QOU/Archimedean/GroundRingEval.lean` gives a **constructed** `ι : R_q →+* ℝ`
(`evalAt`, with `evalAt_T : T n ↦ q0 ^ n` pinning it as substitution) and
`ArchimedeanRealisation`, whose `toArchimedeanSubstrateField` produces the
archimedean layer from the categorical one.

But the bare `ArchimedeanSubstrateField` is **still directly constructible**,
and the 20 library modules that carry it were left untouched. So the tie is
opt-in: an instance can still posit a real field unrelated to any
`SubstrateParameter`. The defect qou-d8m1 describes is fixed *in principle* and
still reachable *in practice*.

## The design question qou-d8m1 answered only implicitly

That bean asked whether the tie belongs **on** `ArchimedeanSubstrateField` or
beside it. I took the second option — a separate `ArchimedeanRealisation` — to
keep blast radius at 2 files while the construction was being established.
The alternative was never costed:

1. **Give `ArchimedeanSubstrateField` the realisation as fields** (`sp`, `q0`,
   with `field := evalAt q0 ∘ sp.field` derived). Closes the loophole outright.
   Touches all 20 modules and every construction site.
2. **Leave both, migrate call sites case by case**, deleting the bare structure
   once empty.
3. **Leave as is** — the tie is available and documented; anyone positing an
   untied field is now doing so visibly.

Costing (1) needs the parent-first read `qou-mtcx` taught and `qou-mt7r`
repeated: check what the 20 modules actually need before assuming they can all
supply a `SubstrateParameter`. Some may legitimately be archimedean-only.

## Do not conflate with the τ wall

`ι` is an evaluation of the ground ring. The archimedean τ-functor
(`QOU/Archimedean/TauFunctorTargetSpec.lean`) is a different and still-open
thing. Migration here is hygiene, not progress on that.
