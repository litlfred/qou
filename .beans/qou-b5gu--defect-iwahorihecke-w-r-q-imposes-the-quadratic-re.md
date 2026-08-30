---
# qou-b5gu
title: 'DEFECT: IwahoriHecke W R q imposes the quadratic relation on ALL of W, not on simple reflections'
status: completed
type: task
priority: normal
created_at: 2026-08-30T02:57:30Z
updated_at: 2026-08-30T03:21:21Z
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


---

## FIXED 2026-08-30 — repaired, not retired

The bean framed this as "repair or retire" and left the choice open. **Repaired**, on
the owner's instruction to *"fix up the correct algebra"*.

`IwahoriHecke W R q S` is now
`QOU.MathlibExt.IwahoriHecke.HeckeAlgebra R q (coxeterMatrixOn S)` — the real algebra,
both relation families, with the simple-reflection set as a parameter instead of
`Set.univ`.

**The Coxeter matrix comes from the group itself:** `coxeterMatrixOn S s t =
orderOf ((s : W) * t)`. The blocker `Defn.lean` recorded for a year — the order
accessor being *"in flux in Mathlib's `CoxeterSystem` API"* — **never applied**.
`orderOf` is plain Mathlib group theory and needs no accessor. That claim gated the
braid relations out of this file for its whole life.

### What changed, all of it a deletion of something wrong

| before | after |
|---|---|
| `T` indexed by `W`, asserting a quadratic relation for every group element | `T` indexed by `S` |
| `IsHeckeAlgebraMap`: quadratic only, `∀ s : W` | both families, `∀ s : S` |
| `IsHeckeBraidedAlgebraMap` (the "full" predicate, unused) | gone — `IsHeckeAlgebraMap` *is* full |
| `altProduct` (duplicate of MathlibExt's `altProd`) | gone |
| `universal_property_existence` hand proof + the `axiom` for uniqueness | both from `exists_unique_lift` |
| — | `T_braid`, `hom_ext`, `isUnit_T` are new |

The old predicate's docstring defended its over-quantification by saying the
restriction to simple reflections *"happens upstream … the caller passes an `f` that
is only nontrivial on `S`"*. That is a constraint on callers, not on the predicate,
and the **type** `IwahoriHecke W R q` had no upstream to be restricted by.

### Why this was safe

The surface was contained, measured before touching anything: `IwahoriHecke`,
`IsHeckeAlgebraMap`, `IsHeckeBraidedAlgebraMap` and `altProduct` had **no consumers
outside `Defn.lean`**, and **no content-block `lean.ref` points at any of them** — the
four refs into this namespace target `TypeA.ReverseLimitQToInfinity`,
`MarkovTrace.GradedMarkovTraceExistence`, `Hoefsmit.HoefsmitSeminormalBasis` and
`Tw.HeckeAnyonicSubstrate`, none of which were touched.

Verified: all six cluster files (`Defn`, `Quotient`, `Tw`, `TypeA`, `AvgCrossing`,
`Hoefsmit`, `MarkovTrace`) `lean`-direct exit 0, zero errors. `#print axioms` clean on
the five new declarations. No `axiom`, `sorryAx` or `native_decide` anywhere in the
cluster.
