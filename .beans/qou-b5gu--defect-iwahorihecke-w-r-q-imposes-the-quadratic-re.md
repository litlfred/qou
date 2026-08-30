---
# qou-b5gu
title: 'DEFECT: IwahoriHecke W R q imposes the quadratic relation on ALL of W, not on simple reflections'
status: todo
type: task
priority: normal
created_at: 2026-08-30T02:57:30Z
updated_at: 2026-08-30T02:58:08Z
---

`content/quantum-observable-universe/lean/QOU/IwahoriHecke/Defn.lean:109`

```lean
def IwahoriHecke (W : Type u) [Group W] [DecidableEq W]
    (R : Type v) [CommRing R] (q : R) : Type (max u v) :=
  QOU.IwahoriHecke.Quotient.IwahoriHeckeQuot R q (Set.univ : Set W)
```

`IwahoriHeckeQuot R q S` builds `FreeAlgebra R ↥S` modulo `(T_s − q)(T_s + 1) = 0`
**for every `s : ↥S`**. Passing `Set.univ : Set W` therefore imposes the quadratic
relation on **every element of the Coxeter group**, not on the simple reflections.

## Why that is wrong, not merely loose

In the actual Iwahori–Hecke algebra `T_w` satisfies the quadratic relation exactly
when `ℓ(w) = 1`. For `w = st` of order 3, `T_{st}` does not. So the object is not the
"quadratic-only intermediate" its docstring claims — it is the free product over all
of `W` of copies of `R[x]/((x − q)(x + 1))`, an algebra that has no natural map to or
from the Hecke algebra.

The same over-quantification is in the predicate: `IsHeckeAlgebraMap q f` is
`∀ s : W, (f s − q)(f s + 1) = 0`. Its docstring defends this by saying *"the
restriction to `S : Set W` of simple reflections happens upstream ... the caller
passes an `f` that is only nontrivial on `S`"* — but that is a constraint on callers,
not on the predicate, and the **type** `IwahoriHecke W R q` has no upstream to be
restricted by.

`IwahoriHeckeOfSn` does NOT have this defect: it passes
`adjacentTranspositionIndex n : Set (Fin (n-1))`, the simple reflections, correctly.

## The fix, and why it was not done in passing

The construction already takes an arbitrary `S : Set W`. The fix is to make the
simple-reflection set a parameter of `IwahoriHecke` rather than hard-coding
`Set.univ`. That is a signature change, so it touches the consumers — five `.lean`
files, all inside `QOU/IwahoriHecke/` (`Defn`, `Quotient`, `Tw`, `TypeA`,
`AvgCrossing`); nothing outside that directory imports the cluster.

Left alone deliberately while building the real algebra
(`QOU/MathlibExt/IwahoriHeckeAlgebra.lean`, bean `qou-phir`): rewiring a
mis-parameterised legacy type and constructing its correct replacement are different
jobs, and doing both in one diff would have made neither reviewable.

## Decide before fixing

Given that `HeckeAlgebra R q M` now exists and is correct, the honest question is
whether `IwahoriHecke W R q` should be **repaired or retired**. Retiring it is
plausible — its five consumers are all in-directory, and `Tw`/`AvgCrossing` may be
re-pointable at the new algebra. That is a judgement about what the cluster is for,
which is why this bean stops at naming it rather than picking.
