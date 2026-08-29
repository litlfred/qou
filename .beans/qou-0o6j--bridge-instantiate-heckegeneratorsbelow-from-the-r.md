---
# qou-0o6j
title: 'Bridge: instantiate HeckeGeneratorsBelow from the real H_n(q) — promotes the whole JM/twist arc from ''any ring'' to ''the Hecke algebra'''
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:37:12Z
updated_at: 2026-08-29T16:37:12Z
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
