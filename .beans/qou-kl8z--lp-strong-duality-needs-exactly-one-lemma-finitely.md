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
- [x] **Farkas' lemma itself — PROVED.** `farkas_separation`: if `b` is not a
      non-negative combination of `v`, some continuous linear functional is
      `≥ 0` on every generator and `< 0` at `b`. This is what closedness was
      *for* — `ProperCone.hyperplane_separation` consumes a closed cone, and
      closedness of a finitely generated cone was the missing input. Packaging:
      `coneSpanPointed` (a `PointedCone`, i.e. a `Submodule` over the
      non-negative reals) then `coneSpanProper` via `isClosed_coneSpan`.
      `nonneg_on_coneSpan_of_nonneg_on_generators` gives the converse half, so
      the two alternatives are mutually exclusive.

      **So the link the bean asserted — closedness ⟹ Farkas — is now verified,
      not assumed.**

- [ ] **The remaining gap is narrower and now precisely known.** Getting from
      `farkas_separation` to `MatrixFarkas.farkas_alternative` still needs
      three things, none of them supplied here:

      1. **Riesz / coordinates.** `farkas_separation` yields a *functional*.
         `farkas_alternative` wants a vector `l : Fin m → R`. Over an inner
         product space that is `InnerProductSpace.toDual`, but note the LP
         file uses plain `Fin m → R` (sup norm, **not** an inner product
         space), so a bridge through `EuclideanSpace ℝ (Fin m)` is needed.
      2. **The augmented cone.** The duality-shaped statement is Farkas applied
         to `{(Ax, cᵀx) : x ≥ 0} ⊆ ℝ^{m+1}`, not to `A` alone.
      3. **The `s > 0` case split.** Separating `(a, γ−ε)` gives multipliers
         `(l', s)` with `s ≥ 0`; dividing by `s` needs `s > 0`, and *that*
         is where the class's primal-feasibility guard earns its place — the
         guard its own docstring calls "essential for truth".

      Note (3) also surfaces a genuine mathematical wrinkle: the separation
      argument naturally gives `aᵀl > γ − ε` for every `ε > 0`, whereas
      `farkas_alternative` demands an `l` with `γ ≤ aᵀl` **attained**. Closing
      that gap needs attainment of the dual optimum, which is a further
      polyhedral fact rather than a corollary of separation. So the bean's
      "exactly one lemma" is still not established, and this is the concrete
      reason why. This bean asserts it follows
      "the standard route" via the bidual; nobody has checked that the
      strong-duality-shaped `farkas_alternative` field really does follow from
      `ProperCone.innerDual_innerDual` plus closedness. Until it is checked,
      "LP strong duality needs exactly one lemma" is a claim about work not yet
      inspected — the lemma named is now proved, and the sentence may still be
      wrong.
- [ ] Instantiate for `operator_selection_lp` — though per `qou/k4f8` that
      block needed no Farkas at all, so this unblocks only the general theorem.

---

## 2026-08-21, later — the attainment worry was mine, and it was wrong

The previous entry said closing the gap "needs attainment of the dual optimum —
a further polyhedral fact, not a corollary of separation". **That is true of the
route I had sketched and false of the standard one.** Correcting it, because it
would have sent the next person down a much harder path than necessary.

### Why the naive route stalls

Separate `(a, γ−ε)` from the cone `{(Ax, cᵀx + t) : x ≥ 0, t ≥ 0}` — finitely
generated, hence closed by `isClosed_coneSpan`. That yields `(l', s)` with
`s ≥ 0`, and `s = 0` is excluded by primal feasibility (if `s = 0` then
`l'ᵀA_j ≥ 0` for all `j`, so `l'ᵀa = Σⱼ x₀ⱼ(l'ᵀAⱼ) ≥ 0`, contradicting
`l'ᵀa < 0`). Dividing by `s` gives a dual-feasible `l` with `aᵀl > γ − ε`.

For **every** `ε`, but never `≥ γ`. That is the wall, and it is real.

### The route that avoids it

Argue by contradiction on the conclusion instead. Suppose
`∃ l, Aᵀl ≤ c ∧ aᵀl ≥ γ` is **infeasible**. That is an infeasible system of
linear inequalities in `l`, so Farkas in *inequality form* gives multipliers
`(x, μ) ≥ 0` with

    A x − μ a = 0    and    cᵀx − μγ < 0

and then a two-case split, each contradicting the hypothesis directly:

- **`μ > 0`:** `x/μ ≥ 0` satisfies `A(x/μ) = a` and `cᵀ(x/μ) < γ` — a feasible
  point beating `γ`.
- **`μ = 0`:** `Ax = 0`, `x ≥ 0`, `cᵀx < 0`, so `x₀ + tx` is feasible for every
  `t ≥ 0` and `cᵀ(x₀ + tx) → −∞`; for large `t` it beats `γ`.

**No attainment anywhere.** The inequality form itself follows from what is now
proved: `{l : Bl ≤ d}` is infeasible exactly when `d` misses the finitely
generated cone spanned by `±` the columns of `B` together with the standard
basis vectors — and `farkas_vector` applies to that cone directly.

### What is proved now

- `isClosed_coneSpan` — a finitely generated cone is closed
- `farkas_separation` — Farkas, separating-functional form
- `farkas_vector` — Farkas, vector form, via `InnerProductSpace.toDual`

All sorry-free. `farkas_vector` is the form a linear program consumes, since
dual feasibility `Aᵀl ≤ c` is a statement about a vector of multipliers.

### One scope limit worth stating

`MatrixFarkas` is declared over **any** `[CommRing R] [LinearOrder R]
[IsStrictOrderedRing R]`. This route is analytic — it uses closedness and
separation — so it can only produce the instance at `R = ℝ`. Farkas is true
over any ordered field, but a general-`R` instance would need a
Fourier–Motzkin style argument instead. In practice the `ℝ` instance is what
the substrate needs (§7c fixes `R := ℝ` for evaluation), so this is a
statement about generality, not a blocker.

## Next

- [ ] The inequality-form Farkas (`{l : Bl ≤ d}` infeasible ⇒ `∃ z ≥ 0`,
      `Bᵀz = 0`, `dᵀz < 0`) — a direct application of `farkas_vector` to the
      cone spanned by `±`columns and basis vectors. Index the generators by a
      sum type.
- [ ] Then `MatrixFarkas` at `R = ℝ` by the two-case split above.

## Attempted and backed out: the inequality form (2026-08-21)

Tried to land `mem_coneSpan_ineqGens_of_feasible` — the bridge from
`farkas_vector` to the inequality form. **Backed out rather than committed with
a `sorry`**, because the file is otherwise pristine and a lone `sorry` in it
would misrepresent how close this is. The maths is not the obstacle; three
`EuclideanSpace`/`WithLp` API details are. Recording them so the next attempt
starts past them:

1. **Coordinatewise evaluation of a sum.**
   `(∑ i, x i • v i) q = ∑ i, x i * v i q` for `v : ι → EuclideanSpace ℝ (Fin p)`.
   `simp [Finset.sum_apply]` does **not** fire — the linter reports the lemma
   unused, because the head is `EuclideanSpace`, not a raw Pi type, so
   `Finset.sum_apply` fails to match syntactically even though `WithLp` is a
   type synonym. Needs either the PiLp-specific lemma or routing through
   `EuclideanSpace.proj q` as a linear map and `map_sum`.
2. **`WithLp.toLp_apply` does not exist** under that name. Something else
   provides `WithLp.toLp 2 f q = f q`; find it, or build generators with
   `EuclideanSpace.single` throughout instead of raw lambdas.
3. **`if` orientation.** After `simp`, the basis term comes out as
   `∑ x, if q = x then … else 0`, so it wants `Finset.sum_ite_eq`, not the
   primed `Finset.sum_ite_eq'` (which matches `if x = q`). Easy, but it cost a
   cycle.

The design that was working: index generators by `(Fin k ⊕ Fin k) ⊕ Fin p` —
columns, negated columns, basis — with coefficients
`Sum.elim (Sum.elim (max (l j) 0) (max (-l j) 0)) (fun q => d q − (Bl) q)`.
Non-negativity of those three families discharges by `le_max_right`,
`le_max_right`, `sub_nonneg.mpr (hl q)`, and that part **did** compile. The
scalar identity `max a 0 − max (-a) 0 = a` is proved by `rcases le_total 0 a`
and is also fine. Only the coordinate bookkeeping is unfinished.

Estimated remaining: one or two compile cycles once (1) is resolved, then the
two-case `μ` split for `MatrixFarkas` at `R = ℝ`.

## 2026-08-21 — the three API details resolved, inequality-form Farkas proved

All three obstacles from the handoff note turned out to be small, and two
dissolved on contact:

1. **`WithLp.toLp` application is `rfl`.** No lemma needed at all.
2. **The `ite` orientation yields to plain `simp`.** No named lemma needed.
3. **The coordinatewise sum needed a `show`.** `Finset.sum_apply` will not
   fire on an `EuclideanSpace` head — application reduces definitionally, but
   `simp` does not see through the `WithLp` synonym. Re-elaborating the goal
   with `show (∑ i, x i • v i) q = _` first makes it match. Recorded in
   `coneSpan_sum_apply`'s docstring, since the `show` looks removable and is
   not.

`EuclideanSpace.proj` + `map_sum` and brute `simp` both failed; only the
`show` route works.

### Also: the draft had the implication backwards

The handoff sketched `mem_coneSpan_ineqGens_of_feasible` — *feasible ⇒ in the
cone*. Farkas needs the **converse**: *in the cone ⇒ feasible*, whose
contrapositive turns "no solution" into "misses a closed cone". Proved as
`exists_solution_of_mem_coneSpan_ineqGens`.

### Proved

`farkas_inequality`: if `Bl ≤ d` has no solution then there are `z ≥ 0` with
`Bᵀz = 0` and `dᵀz < 0`. Sorry-free, compiled first try.

The chain is now `isClosed_coneSpan` → `farkas_separation` → `farkas_vector` →
`farkas_inequality`, all proved, with exactly one step left to `MatrixFarkas`:
the two-case `μ` split, over `B : Fin (n+1) → Fin m → ℝ` encoding dual
feasibility plus `−aᵀl ≤ −γ`.
