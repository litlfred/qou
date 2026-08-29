---
# qou-29pv
title: 'Two knot-factor Lean files do not compile: HeckeExpansion genericisation dropped Mathlib.Data.Real.Basic'
status: todo
type: task
priority: normal
created_at: 2026-08-21T21:58:32Z
updated_at: 2026-08-21T21:58:55Z
---


Found 2026-08-21 while working `qou/q407` (PR #5371), which changed
`KnotFactorSpectralDerivation.lean` and `KnotFactorAmphicheiral.lean` and so had
to check their downstreams. **Both failures are pre-existing** — identical 12
errors with the q407 branch stashed and unstashed — and are **not fixed there**:
they have nothing to do with trivial existentials, and one needs an authoring
decision.

## Root cause

The 2026-08-09 genericisation (`HeckeExpansion (R : Type*) [Field R] (n : ℕ)`,
recorded in `knot-factor-amphicheiral.ts`'s `refined-framing` note) correctly
dropped `Mathlib.Data.Real.Basic` from `KnotFactorSpectralDerivation.lean` —
nothing there needs `ℝ` any more. Two downstream files were still ℝ-typed and
had been getting `ℝ` transitively.

## The two files

**1. `mass-theory/knot-factor-borromean-composite.lean` — one-line fix.**

```
25:33: failed to synthesize HPow ℝ ℕ ?m
34:38: failed to synthesize HSub ℕ ℝ ℝ
36:2:  Invalid field `decouples`: … does not contain
       QOU.BraidKnot.BrunnianDecoupling.decouples
```

`BrunnianDecoupling` is declared in this same file over `(component_factor
composite_factor : ℝ)`; with `ℝ`'s instances unavailable the structure itself
fails to elaborate, which is why its own projection goes missing. Adding
`import Mathlib.Data.Real.Basic` should be the whole fix — verify, don't assume.

**2. `mass-theory/knot-factor-shell-closed.lean` — needs a decision.**

```
24:65: Application type mismatch: n has type ℕ … expected Type
       in the application @HeckeExpansion n
41:10: Function expected at MarkovEquilibrium
```

Still written against the **pre-genericisation** arity `HeckeExpansion n`, so
`n : ℕ` is being passed as the base ring. Not a missing import: someone has to
say which `R` this file means. `KnotFactorSpectralDerivation`'s own §7c note
says `R := ℚ(q)` is intended and `R := ℝ` is the archimedean instance — this
file's shell-closure content decides which applies, and `MarkovEquilibrium`'s
arity has to be re-read at the same time.

## Why no gate caught it

`bun run scripts/run-validate.ts` passes (exit 0) — it validates the `.ts`
content objects, not whether the `.lean` a `lean.ref` points at compiles. Both
blocks are `validation: "not_checked"`, so nothing over-claims; the files are
simply unbuildable and no check says so. Compare the sibling finding in q407:
`spectral-decomposition-qvalue.lean` had `Real.log` as an unknown constant —
i.e. `sorry` in a `def` body — under a live `lean.ref`, and also passed
everything.

That is the same shape as the rest of the vacuity arc: **an absent check is
indistinguishable from a passing one.** A per-file `lean`-direct compile over
every `lean.ref` target is the check that would have caught all three.

## Next

- [ ] Fix (1) — add the import, recompile, confirm the 6 errors go.
- [ ] Decide the base ring for (2), then repair the signatures.
- [ ] Consider a gate: compile every file named by a `lean.ref`.
