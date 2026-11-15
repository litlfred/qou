---
# qou-w7sc
title: Migrate the 20 ArchimedeanSubstrateField call sites onto ArchimedeanRealisation
status: completed
type: task
priority: normal
created_at: 2026-08-24T08:50:28Z
updated_at: 2026-08-24T10:57:09Z
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

## Summary of Changes — 2026-08-24

**The migration this bean proposed was the wrong shape, and measuring first is
what showed it.** Commit `a770e71954c`.

### The 20 was a count of the wrong thing

20 modules *mention* `ArchimedeanSubstrateField`. Only a site that
**constructs** one can posit an untied field. There is exactly **one** in the
library:

| site | kind |
|---|---|
| `Elaboration.lean:219` | **construction** — the `PUnit` witness for `dq_squared_nonvanishing` |
| `collatz_substrate_link.lean:37` | parameter |
| `VolumeForm.lean:95` | parameter |
| `SubstrateParameter.lean:88` | the definition itself |
| `SubstrateParameter.lean:123` | `QuantumGaugeGroup extends` — **zero** construction sites anywhere |
| `GroundRingEval.lean:131` | the `qou-d8m1` tie |

So options **1** (fields on the structure) and **2** (case-by-case migration)
have almost nothing to act on, and the single site they would touch is a
counterexample witness whose whole value is being concrete. **Option 3 stands.**

Checked along the way and *not* a defect: `QOU.Glossary.QuantumGaugeGroup` and
`QOU.QuantumGaugeGroup` are distinct FQNs, so `check-duplicate-decls` is right
not to flag them. I suspected a collision and was wrong.

### What the measurement turned up instead

`dq_squared_nonvanishing` is quantified over **arbitrary**
`ArchimedeanSubstrateField`s. Because that structure's field is independent of
any categorical parameter, the refuted statement could have been about a
real-valued function with no substrate behind it — a weaker claim than it
reads as.

`QOU.Archimedean.dq_witness_realisable` closes that gap: the same witness
arises from a genuine `ArchimedeanRealisation`, categorical parameter `q`
specialised at `q₀ = 2`. `d_q²` therefore fails to vanish on a substrate the
framework can actually produce. Supporting `constRealisation` and
`constRealisation_field` show realisations are inhabited and can hit a
prescribed unit value.

This is the first thing the `qou-d8m1` tie buys beyond hygiene, and it would
not have been found by executing the migration as written.

`Elaboration.lean` gets a pointer comment and **no import** — the witness stays
concrete; realisability is proved next to the tie.

### Residue

- **The loophole is still open in principle.** A bare
  `ArchimedeanSubstrateField` remains directly constructible. The finding is
  that nothing in the library currently walks through it, not that it was
  sealed. If a future construction site appears, it should use
  `ArchimedeanRealisation` — worth a checker if it recurs, not worth one for a
  population of one.
- **The order axioms stay assumed**, correctly: `1 ≤ q₀^n` and "not a root of
  unity" are facts about the chosen `q₀`, not consequences of the categorical
  layer.
- **Not the τ-functor.** Unchanged and unaffected.

### Verification

```
lean-direct-cone     exit 0 — GroundRingEval, Elaboration
#print axioms        propext / Classical.choice / Quot.sound — no sorry
run-validate         30 issues, unchanged
mirror drift  @35    exit 0
duplicate decls @57  exit 0
```
