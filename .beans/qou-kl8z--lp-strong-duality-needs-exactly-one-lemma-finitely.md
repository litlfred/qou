---
# qou-kl8z
title: 'LP strong duality needs exactly one lemma: finitely generated cones are closed'
status: todo
type: task
created_at: 2026-08-16T10:54:54Z
updated_at: 2026-08-16T10:54:54Z
---

Scoping done with a **working Lean toolchain** (see `lean-environment-setup.md`
§middle case) against the pinned mathlib `f897ebcf72`.

## The chain is in better shape than the sorry count suggests

`QOU/Optimization/` already has:

- **`lp_weak_duality`** — proved unconditionally, over any ordered commutative
  ring.
- **`lp_strong_duality`**, **`lp_dual_feasible_of_lower_bound`**,
  **`lp_zero_duality_gap`** — **fully derived and sorry-free** from a
  conditional class `MatrixFarkas A a c` whose one field is the Farkas/Gale
  alternative.

So "LP duality is missing" is wrong. Everything above the analytic input is
done. **The whole LP layer rests on a single missing instance:
`MatrixFarkas`.**

## What mathlib gives, and the one thing it does not

Present in the pinned build (verified by reading
`Mathlib/Analysis/Convex/Cone/InnerDual.lean` at that rev):

- `ConvexCone.hyperplane_separation_of_nonempty_of_isClosed_of_notMem`
- **`ConvexCone.innerDualCone_of_innerDualCone_eq_self`** — for a **nonempty
  closed** convex cone `K`, `(K*)* = K`. This is the separation engine Farkas
  needs.
- `Set.innerDualCone` with a full lattice/union API, and
  `isClosed_innerDualCone`.

Absent: any statement that a **finitely generated cone is closed**. Nothing in
`Mathlib/Analysis/Convex/Cone/*` mentions closedness of a span/FG/generated
cone. `ProperCone` exists but is **not in the restored olean cache** (the cache
is a partial mathlib build — only what QOU imports), which is a separate,
purely practical obstacle.

## So the gap is exactly one lemma

```
IsClosed { y | ∃ x : Fin n → ℝ, (∀ j, 0 ≤ x j) ∧ y = A.mulVec x }
```

Minkowski–Weyl / the closedness half of finitely-generated-cone theory. With it,
`MatrixFarkas` follows the standard route: the image cone is convex, nonempty
and closed → apply `innerDualCone_of_innerDualCone_eq_self` → unfold membership
in the bidual to get the alternative.

That is a genuine but **bounded and standard** target, and it is the right
Mathlib-shaped contribution: the usual proof is induction on the number of
generators via a Carathéodory argument for cones (`Mathlib/Analysis/Convex/
Caratheodory.lean` is present and is the natural starting point).

## Why this bean is not "prove Farkas"

Reframing the ask matters. `operator_selection_lp`'s comment says "Missing
infra: the LP strong-duality theorem ... and the simplex/vertex optimality
argument", which reads as two large projects. It is neither: strong duality is
**already proved** here, and vertex optimality is not needed — `lp_strong_duality`
gives dual optimality directly. One closedness lemma unblocks the layer.

## Next

- [ ] Prove `IsClosed` for the finitely generated cone (induction on generators
      + Carathéodory), or locate it under a name not searched here
- [ ] Derive `MatrixFarkas` from it + `innerDualCone_of_innerDualCone_eq_self`
- [ ] Instantiate for `operator_selection_lp`, closing that sorry

Practical note: `Mathlib.Analysis.Convex.Cone.Proper` is **not** in the olean
cache, so any file importing it needs that module built first. `Cone/Basic`,
`Cone/Closure`, `Cone/Dual`, `Cone/InnerDual` and `Convex/Caratheodory` **are**
cached.
