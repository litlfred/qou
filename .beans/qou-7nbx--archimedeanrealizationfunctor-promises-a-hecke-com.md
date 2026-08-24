---
# qou-7nbx
title: ArchimedeanRealizationFunctor promises a Hecke-compatible functor and carries a real number
status: todo
type: bug
priority: high
created_at: 2026-08-24T19:38:25Z
updated_at: 2026-08-24T19:38:25Z
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
