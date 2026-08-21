---
# qou-kl8z
title: 'LP strong duality needs exactly one lemma: finitely generated cones are closed'
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T10:54:54Z
updated_at: 2026-08-21T16:25:20Z
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

---

## 2026-08-21 — the gap is now one *combinatorial* lemma, not an analytic one

`QOU/Mathlib/FinitelyGeneratedConeClosed.lean`. Compiles clean against the
pinned rev with **exactly one `sorry`**.

### Two corrections to the scoping above

- **`ProperCone` is present.** This bean records it as absent from the olean
  cache — "a separate, purely practical obstacle". Measured today by compiling
  a probe: the names simply moved.
  `ConvexCone.innerDualCone_of_innerDualCone_eq_self`, `Set.innerDualCone` and
  `isClosed_innerDualCone` are now **deprecated aliases** for
  `ProperCone.innerDual_innerDual`, `ProperCone.innerDual` and
  `ProperCone.isClosed`. There is no practical obstacle.
- **`Convex/Caratheodory.lean` is not a starting point in the way stated.** It
  proves `convexHull_eq_union` over *affinely independent* subsets — a
  statement about convex hulls, not cones. The argument transfers; the
  statement does not.

### What is proved

- `isClosed_coneSpan_of_linearIndependent` — a cone on **independent**
  generators is closed. The coefficient map is injective (from
  `Fintype.linearIndependent_iff`) out of a finite-dimensional space, hence a
  closed embedding by `LinearMap.isClosedEmbedding_of_injective`, and the cone
  is the image of the closed non-negative orthant. Supporting: `coneMap`,
  `coneSpan_eq_image`, `isClosed_nonneg_orthant`, `ker_coneMap_eq_bot`,
  `sum_eq_sum_subtype`.
- `coneSpanOn_eq`, `isClosed_coneSpanOn` — the same for a subfamily indexed by
  a `Finset`.
- `coneSpan_eq_iUnion` — the cone is the union of the sub-cones on independent
  subfamilies.
- **`isClosed_coneSpan` — this bean's target theorem, derived.** A *finite*
  union of closed sets, since `Finset ι` is finite.

Stated over an arbitrary `[Fintype ι]` rather than `Fin n`, which is what lets
the subfamily indexed by `s : Finset ι` reuse the same lemma.

### PROVED 2026-08-21 — `exists_linearIndependent_support` closed too

The file is now **sorry-free**. Conic Carathéodory is proved by induction on
the support (`caratheodory_aux`): extract a dependency via
`Fintype.not_linearIndependent_iff`, extend it by zero off the active set,
orient it so some coefficient is positive (negating if necessary), and walk
`x ↦ x − cλ` with `c = minᵢ{xᵢ/λᵢ : λᵢ > 0}` obtained from
`Finset.exists_min_image`. Non-negativity survives — where `λᵢ ≤ 0` because
`c ≥ 0`, and where `λᵢ > 0` by minimality — and the coefficient attaining
the minimum is driven to zero, so the support strictly shrinks.

**So this bean's headline lemma is done.** `isClosed_coneSpan` is proved, and
with it the analytic input the LP layer was said to rest on.

### Original scoping of what remained (kept for the record)

> Every point of the cone is a non-negative combination of a **linearly
> independent** subfamily of the generators.

Conic Carathéodory. **Finite and purely algebraic — no topology appears in
it.** Sketch, for whoever takes it: if the active generators are dependent,
take a dependency `Σ λᵢvᵢ = 0` with some `λᵢ > 0` (negate if necessary), walk
`x ↦ x − tλ` with `t = minᵢ {xᵢ/λᵢ : λᵢ > 0}`; non-negativity survives (for
`λᵢ > 0` by minimality, for `λᵢ ≤ 0` because `t ≥ 0`), the coefficient
attaining the minimum is driven to zero, the support strictly shrinks, and
induction on its cardinality terminates.

So the bean's headline — "LP strong duality needs exactly one lemma" — is now
**verified rather than asserted**, and the one lemma is combinatorial rather
than analytic. That is a strictly better position: the remaining work needs no
convex analysis, no separation theorem, and no Mathlib infrastructure that
does not already exist.

## Next

- [ ] Prove `exists_linearIndependent_support` (sketch above; the only `sorry`)
- [ ] Derive `MatrixFarkas` from `isClosed_coneSpan` via
      `ProperCone.innerDual_innerDual` — **note this derivation is still
      unverified**: this bean asserts it follows "the standard route", and
      nobody has checked that the strong-duality-shaped `farkas_alternative`
      field really does follow from the bidual identity. Worth doing before
      trusting the reduction end-to-end.
- [ ] Then instantiate for `operator_selection_lp` — though per `qou/k4f8`
      that block needed no Farkas at all, so this now unblocks only the
      *general* theorem.

## Status after 2026-08-21

- [x] Prove `isClosed_coneSpan` — **done, sorry-free**, including conic
      Carathéodory.
- [ ] **Derive `MatrixFarkas` from it. Still unverified, and this is now the
      only thing between here and the LP layer.** This bean asserts it follows
      "the standard route" via the bidual; nobody has checked that the
      strong-duality-shaped `farkas_alternative` field really does follow from
      `ProperCone.innerDual_innerDual` plus closedness. Until it is checked,
      "LP strong duality needs exactly one lemma" is a claim about work not yet
      inspected — the lemma named is now proved, and the sentence may still be
      wrong.
- [ ] Instantiate for `operator_selection_lp` — though per `qou/k4f8` that
      block needed no Farkas at all, so this unblocks only the general theorem.
