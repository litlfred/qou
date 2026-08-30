---
# qou-0o6j
title: 'Bridge: instantiate HeckeGeneratorsBelow from the real H_n(q) — promotes the whole JM/twist arc from ''any ring'' to ''the Hecke algebra'''
status: completed
type: task
priority: normal
created_at: 2026-08-29T16:37:12Z
updated_at: 2026-08-30T02:55:56Z
---

## Why this exists

The JM / full-twist / seminormal arc (`qou-u9o1`, `sv8b`, `qou-t1kv` — all completed) proves
~40 theorems, every one of the form:

> *in any ring `A` carrying elements satisfying the Hecke/braid/far relations, …*

`HeckeGenerators` and `HeckeGeneratorsBelow` **axiomatise** the relations on an ambient ring.
They do **not construct** H_n(q). So `jmRaw_comm`, `jmProd_eq_delta_pow`, `IsJMWeight`,
`fullTwist_smul_eq_theta_sq` are all conditional on being handed such a ring — the
"conditional-proved ≠ premise-established" distinction, applied to the arc's own output.

Non-vacuity is real and now includes a `dim > 1` witness (`stdTwoBelow3_isJMWeight`), but a
witness is not a construction.

## What this task is

Once `qou-phir` (B2: H_n(q) as field-algebra via quadratic+braid relations) lands, exhibit it
as a `HeckeGeneratorsBelow R A q n` instance at `W = S_n`. That single instance promotes every
theorem in the arc to a statement about **the** Hecke algebra.

## The two obstacles — named, not hand-waved

**1. The corpus does not yet have H_n(q).** `QOU/IwahoriHecke/Defn.lean` constructs
`IwahoriHecke W R q := Quotient.IwahoriHeckeQuot R q Set.univ`, and that quotient is
`RingQuot (heckeRel …)` where `heckeIdeal := Ideal.span (heckeQuadraticGenerators R q S)` —
**quadratic relations only**. The braid relations are NOT imposed (the `heckeIdeal` docstring
says so explicitly: "Sprint 2 scope… braid relations… added in the Sprint 2 follow-up once the
Coxeter order accessor stabilises"). So `IwahoriHecke` as built cannot satisfy the class's
`braid` field. This is `qou-phir`'s job; do not duplicate it here.

**2. Convention mismatch — the part specific to this bridge.** `IwahoriHecke` uses
`(T_s − q)(T_s + 1) = 0`, i.e. eigenvalues `q, −1`. The corpus convention (AGENTS.md §7a) is
`σᵢ² = (q − q⁻¹)σᵢ + 1`, i.e. eigenvalues `q, −q⁻¹`. These differ by the rescaling
`σ = q^{-1/2} T`, so the bridge needs `√q` in the base ring — either a `[∃ r, r*r = q]`
hypothesis, a base change to `R[√q]`, or restating one side. **Check which before starting:**
picking the wrong one forces `ℝ` and would breach §7c.

## Verified state of the arc (2026-08-29, source-rebuilt cone, 29 modules, 0 failures)

All `[propext, Classical.choice, Quot.sound]`, no `sorryAx`:
`jmRawB_comm`, `stdTwoBelow3_isJMWeight`, `sigma_eq_of_succ_scalar`, `sigma_scalar_of_schur`,
`stdTwo_no_stable_extension`, `existsNonscalar_heckeGenerators`.

Blocked on: `qou-phir`. Related: `qou-ml0e`, `qou-mbm9`, `qou-hnhg` Track 2 (B2f).


---

## Obstacle 2 is RESOLVED, and this bean was WRONG about it (2026-08-29, PR #6055)

The "Convention mismatch" section above says the bridge *"needs √q in the base
ring — either a `[∃ r, r*r = q]` hypothesis, a base change to `R[√q]`, or
restating one side"*, and warns that picking wrong forces `ℝ` and breaches §7c.
**That is false. No √q is needed and no base change is needed.**

Writing `σ = c·T` against the Iwahori relation `(T − Q)(T + 1) = 0` gives
`σ² = c(Q−1)·σ + c²Q`, so matching the corpus relation
`σ² = (q − q⁻¹)σ + 1` requires BOTH:

    c²Q = 1        and        c(Q − 1) = q − q⁻¹

Take `Q = q²`, `c = q⁻¹`. First: `q⁻²·q² = 1`. Second: `q⁻¹(q² − 1) = q − q⁻¹`.
Both hold identically.

**The parameter moves, not the generator.** The corpus's `q` is already the
square root of the Iwahori parameter. You instantiate the Iwahori algebra at
`Q = q²` and rescale by `q⁻¹`, which lives in the field whenever `q ≠ 0`.
Nothing leaves a generic `[Field R]`.

The error came from reading the mismatch as "eigenvalues `q, −1` vs `q, −q⁻¹`,
therefore rescale by `q^{-1/2}`" — true if you hold `Q = q` fixed, which is
exactly the assumption that does not survive. A two-equation match has two
unknowns; only one was solved for.

## What landed

`content/quantum-observable-universe/lean/QOU/BraidKnot/HeckeIwahoriConventionBridge.lean`
— nine declarations, `lean`-direct exit 0, no warnings, no sorries, all on
`[propext, Classical.choice, Quot.sound]` (`braid_of_scaled` / `far_of_scaled`
choice-free):

- `hecke_of_iwahori` (+ an `algebraMap` form) — the quadratic bridge.
- `braid_of_scaled` / `far_of_scaled` — braid and far are scale-invariant
  (`c³` and `c²` cancel).
- `heckeGeneratorsBelow_of_iwahori` — the three together: **any Iwahori family
  at `Q = q²` is a `HeckeGeneratorsBelow` at `q`.**
- `iwahori_jm_comm` — the payoff, demonstrated: such a family inherits
  `jmRawB_comm` with no new hypotheses.
- `iwahori_of_hecke` — the inverse rescaling, `T = q·σ`. Stated **without**
  `q ≠ 0`: the identity survives `q = 0`, where Lean's `q⁻¹ = 0` collapses both
  sides. (Written in out of symmetry, flagged unused by the linter, checked
  rather than silenced, then dropped — a strictly stronger lemma.)
- `stdTwoIw` / `stdTwoIw_isHeckeGeneratorsBelow` / `stdTwoIw_roundTrip` — the
  explicit 2×2 Young seminormal matrices pushed into Iwahori normalisation,
  shown to satisfy the three Iwahori relations at `n = 3`, and shown to come
  back out as `stdTwo` on the nose. The round trip is the falsifiability check:
  a bridge with the scaling inverted, or with `Q = q`, fails it.

Authoring trap worth carrying forward: state everything with the scalar action
`•`, not `algebraMap _ * _`. The two agree by `Algebra.smul_def`, but
`algebraMap`'s centrality makes `rw` fail to find its own pattern — it broke two
attempts here and had already broken one earlier on `HeckeSeminormalWeight`.
`smul_smul` / `smul_mul_assoc` / `mul_smul_comm` move scalars cleanly, and the
`module` tactic closes scalar-coefficient goals that `abel` cannot.

## What is left

Obstacle 1 only — the corpus still has no H_n(q) with braid relations imposed.
That is `qou-phir`. When it lands, `heckeGeneratorsBelow_of_iwahori` is the
instance and nothing further is needed from this bean.

One note for `qou-phir` recorded in `Quotient.lean`'s header: the cited blocker
is the Coxeter order accessor being "in flux in Mathlib's `CoxeterSystem` API",
but `m_{st}` is just `orderOf (s * t : W)` — plain Mathlib group theory, no
accessor — and `altProduct` already exists in `Defn.lean`. Worth checking that
route before waiting.


## Corollary worth keeping: the bridge rules out one explanation of the OTHER √q

Raised by a sibling on #6033, which found `√q` in the Toffoli information-theory
closed forms (`P₇₇`, `Φ`) and traced it to the excised convention-C Markov
parameter `z_C = √q/(q+1)`. Their four reconstructions verify symbolically to
exact zeros (checked here, sympy, not taken on trust).

**This bridge does NOT give an independent derivation of that** — theirs is
about the Markov parameter `z`, mine about generator normalisation, and
`σ ↦ cσ` does not act on `z`. Recorded so the headline agreement ("the √q was
the convention") is not mistaken for two witnesses to one result.

What it DOES give is a negative: **`z_C`'s `√q` is not the Iwahori↔corpus
normalisation root.** The bridge fixes corpus-`q = √Q`, so `√q = Q^{1/4}` — a
*fourth* root of the Iwahori parameter, one level deeper than any generator
rescaling reaches. That kills a plausible-sounding explanation before someone
writes it down.

Side observation, independent of their route: the two Markov parameters are the
same rational shape `x^k/(x²+1)` — C is `u/(u²+1)` at `u = √q` (`u²+1 = q+1`,
which is why the denominators look unlike), D is `q³/(q²+1)` at `x = q`. The
`√q` is carried by the choice of variable, not by the shape.


---

## CLOSED 2026-08-30 — and closed STRONGER than this bean asked

The bean asks for a `HeckeGeneratorsBelow R A q n` instance. What landed is the
**unbounded** `HeckeGenerators R (TypeAHecke R q) q`
(`QOU/BraidKnot/HeckeTypeAInstance.lean::typeAHeckeGenerators`), from which every
`HeckeGeneratorsBelow n` follows by restriction via the existing
`HeckeGenerators.toBelow`.

The move that bought the stronger form: **index the type-A Coxeter matrix by `ℕ`,
not by `Fin (n-1)`.** `typeAMatrix i j` is 3 for adjacent, 2 for distant, 1 on the
diagonal, over all of `ℕ`. The relations then hold at every index, so one object
serves every `n` at once and all the `Fin` bookkeeping disappears.

Obstacle 1 (the corpus had no H_n(q) with braid relations) is gone: see the
`qou-phir` note. Obstacle 2 was already resolved and is recorded above.

`typeA_jmRaw_comm` is the payoff in one line — Jucys–Murphy elements commute **in
the type-A Hecke algebra**, not merely in a ring that happens to carry the
relations. The rest of the arc composes the same way.

Verified: `lean`-direct exit 0, no warnings; `#print axioms` on all ten new
declarations shows no `sorryAx`.
