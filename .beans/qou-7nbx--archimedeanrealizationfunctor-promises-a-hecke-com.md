---
# qou-7nbx
title: ArchimedeanRealizationFunctor promises a Hecke-compatible functor and carries a real number
status: completed
type: bug
priority: high
created_at: 2026-08-24T19:38:25Z
updated_at: 2026-08-24T21:04:07Z
---

`QOU/Mathlib/ArchimedeanRealization.lean:111-124`, verified present 2026-08-24.

## What the docstring promises

> **3b-cond class hypothesis**: the existence of a Hecke-compatible Archimedean
> realisation **functor**. Once Mathlib's Iwahori-Hecke library lands, the class
> is discharged concretely. For now, the class wraps the substrate-axiom that
> some such functor exists **with the listed compatibility properties**.

## What the class contains

```
class ArchimedeanRealizationFunctor where
  q0 : R
  q0_gt_one : q0 > 1
  q0_canonical : q0 = q_zero

noncomputable instance canonical : ArchimedeanRealizationFunctor where
  q0 := q_zero
  q0_gt_one := q_zero_gt_one
  q0_canonical := rfl
```

There is no functor. There is no source category, no target category, no
action on morphisms, and nothing Hecke-compatible: the three fields are a real
number, its positivity, and an equation pinning it to `q_zero`. "The listed
compatibility properties" refers to a list that is not there.

Because `q0_canonical` forces `q0 = q_zero`, the class has **exactly one model**,
`canonical` supplies it as a global `instance`, and `[ArchimedeanRealizationFunctor]`
is therefore equivalent to no hypothesis at all.

## Why it matters more than the usual case

`QOU/Mathlib/UpstreamSubstrateBridge.lean:23` maps a substrate axiom onto it:

```
S-Archimedean-realisation <- ArchimedeanRealization.ArchimedeanRealizationFunctor
```

So a named substrate axiom is discharged in the bridge table by a class whose
content is `q0 = q_zero`. That is the sentence to fix first: the bridge claims
coverage the class does not provide.

`QOU/MotivesArchimedean.lean:132` separately declares a **`structure`** of the
same name. Two different objects, one name — check which one you are reading.

## Disposition (design decision)

Not a demote-and-move-on. Either

1. give the class the functor data it advertises (a realisation map plus the
   Hecke compatibility square), which is real work and probably blocked on the
   Mathlib Iwahori-Hecke library the docstring already names; or
2. rename it to what it is — `ArchimedeanEvaluationPoint`, say — delete the
   functor prose, and mark `S-Archimedean-realisation` in
   `UpstreamSubstrateBridge.lean` as **not** covered.

Option 2 is honest and takes an hour. Option 1 is the paper's actual claim.
Doing neither is the current state.

**The automated vacuity detector will not catch a regression here**: `q0 := q_zero`
is a named constant, not one of the literal degenerate tokens it matches. See
folio-assistant bean `folio-assistant-ilbh`.


## Resolved 2026-08-24 — option 2, and here is why not option 1

**Consumers before the change: 6 mentions, and not one `[ArchimedeanRealizationFunctor]`
binder anywhere in the corpus.** The six were: the class declaration, the
`canonical` instance, the bridge-table line
`UpstreamSubstrateBridge.lean:23`, the Bridge-3 prose at
`UpstreamSubstrateBridge.lean:105`, the `Summary.lean:39` file-index row, and
`MotivesArchimedean.lean:132` — which is a **different** `structure` of the same
name in namespace `QOU.BraidsKnots`, untouched. So the class had *zero* code
consumers: renaming it broke nothing, and the only work was prose.

Worth recording: the content block
`mass-theory/archimedean-realization-functor.ts` has
`ref: "qou:QOU.BraidsKnots.ArchimedeanRealizationFunctor"` — it points at the
**MotivesArchimedean structure**, not this class. The bean's "two objects, one
name" warning is exactly right and the block belongs to the other one.

**Decision: option 2 (rename/restate), and the reason is not just cost.**
Option 1 is the paper's actual claim, but it cannot be written honestly today:
this checkout's Mathlib contains **no Iwahori–Hecke algebra at all** (`find
.lake/packages/mathlib -iname '*Hecke*' -o -iname '*Iwahori*'` → empty). A
"functor" declared now would have to invent both its source category and its
compatibility square, which reproduces the present defect one level up with more
prose covering it. Recorded in the file, together with what a genuine discharge
owes: the two categories, the action on morphisms, and the square
`Real_q₀ ∘ (Hecke action) = (real action) ∘ Real_q₀`.

**What was done.**

- `QOU/Mathlib/ArchimedeanRealization.lean`: class renamed to
  `ArchimedeanEvaluationPoint` and — going beyond a rename — **parameterised over
  the point**: `class ArchimedeanEvaluationPoint (q0 : ℝ) : Prop` with the single
  field `is_substrate : q0 = q_zero`. This is what kills the one-model defect:
  `[ArchimedeanEvaluationPoint q0]` is now falsifiable, satisfied at `q_zero`
  (`instCanonical`) and refuted everywhere else (`not_evaluationPoint_of_ne`,
  concretely `not_evaluationPoint_two`).
- `q0_gt_one` was a *second* field derivable from the first, so it is now the
  derived theorem `ArchimedeanEvaluationPoint.gt_one` rather than an assumption a
  model gets to restate.
- File-level docstring states plainly that nothing in the file is the functor.
- `UpstreamSubstrateBridge.lean`: the bridge-table row is now
  `S-Archimedean-realisation ← NOT COVERED (see Bridge 3)`, with the history and
  the reason spelled out, and Bridge 3 retitled "the scalar piece only". What
  Bridge 3 *does* prove is left standing and is genuine —
  `archimedean_eval_well_defined`: the evaluation is the **unique** ring map
  `ℝ[q] → ℝ` fixing constants and sending `q ↦ q₀`.
- `Summary.lean`: file-index row corrected.

**Verification.** Fresh `lean` on `ArchimedeanRealization`,
`UpstreamSubstrateBridge`, `Summary` (and the 80-module `Summary` cone) — all
exit 0. Only pre-existing warnings (`hden`, the `W*` unused binders); the
bridge/summary edits are comment-only so no warning could change.
`#print axioms` on the four new decls: `[propext, Classical.choice, Quot.sound]`
only — no `sorryAx`. No `sorry` in committed work.
