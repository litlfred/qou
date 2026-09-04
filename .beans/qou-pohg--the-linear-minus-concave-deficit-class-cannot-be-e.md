---
# qou-pohg
title: 'The linear-minus-concave-deficit class cannot be excluded by three points: it is convexity restated'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T10:42:12Z
updated_at: 2026-09-04T10:54:14Z
---

## Result

**The proposed exclusion route in `qou-zy94` cannot succeed.** Two independent
reasons; the first is decisive and the second is a direct refutation of the
hypothesis as stated.

### 1. Definitional — the class is convexity restated

`QOU/MassTheory/ConcaveDeficitNonExclusion.lean` (9 declarations, sorry-free,
`lean`-direct exit 0, `#print axioms` = `[propext, Classical.choice, Quot.sound]`
on all nine, generic `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`).

Subtracting the data from a line negates every secant slope
(`deficit_secant₀/₁/₂`: the deficit's slopes are `c − s_j`). Hence

* `deficit_concave_iff_convex` — `ψ := c·x − Φ` is concave through the origin
  **iff** `Φ` is convex through the origin, **for every `c`**, no hypothesis;
* `deficit_increasing_of_gt_secant₂` — and strictly increasing once `c` clears
  the largest secant slope.

So `exists_concaveDeficit_of_convex`: every convex-through-the-origin dataset
**is** a linear term minus a strictly increasing concave deficit, for an open ray
of `c` — not a lucky witness. `concaveDeficit_class_not_excludable` states it in
the form the follow-up needs: class membership *follows from* the convexity the
same three points establish, so no three-point test can rule the class out.

Numerically (`computations/probes/concave_deficit_non_exclusion_probe.py`, 5/5,
exact `Fraction`): `det3(x, ψ, Φ)` — the very filter `AggregatorFamilyExclusions`
uses — is **exactly 0** for every data-derived `ψ`, at `c ∈ {6.731918, 7, 8, 10,
1000}`. The column is by construction a combination of the other two.

### 2. Analytic — the monotone-exponent hypothesis is false on the class

Explicit member `Φ(x) = 1.02·x − 100·(1 − e^{−x/100})`: convex through the
origin, concave increasing deficit, `Φ(x)/x → c` bounded (so compatible with
`CoordinationSaturation`), and secant exponents **1.302995541 → 1.503565786**,
i.e. **increasing** — the same direction the data goes.

The hypothesis is true for `ψ(x) = x^s`, where it was read off. It does not
survive the class.

## Why this does not contradict the five shape exclusions

`not_realizable_of_det3_ne_zero` excludes a **two-parameter** family with `ψ`
fixed **in advance** — three points, two parameters, one residual. Here `ψ` is a
free *shape*, chosen after the data, so there is no residual left to fail. **The
five shape exclusions are about parameter counting, not about the concave-deficit
structure**, and they all still stand. Do not read this as reopening them.

## What this does NOT establish

* Nothing about which `ψ` is right. A fixed shape is still testable by `det3`.
* The exponential member carries **three** parameters on three points — the same
  underdetermined regime the sibling probe's SEMF caveat describes. Exhibiting it
  refutes the monotonicity hypothesis; it is **not** evidence that it fits.
* Three points are three points. The standing recommendation in `qou-82mc` /
  `qou-zy94` — extend the grid past `A = 4` with a **derived** bond set — is
  what would change any of this, and this result raises its priority: it is now
  the only thing that can make the class testable at all.

## Related

`qou-zy94` (the two zero-fit filters and the proposed follow-up), `qou-82mc`
(the convexity dichotomy), `qou-brng` (linking-vs-self-energy amplitude).
