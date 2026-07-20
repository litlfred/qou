# PI-2: Elliptic divisor-degree scaffold — Mathlib gap survey + tractable bricks

**Date:** 2026-07-20 **Bean:** `qou-toqt` (PI-2, epic `qou-lbth` pentagon-infra)
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**File:** `content/quantum-observable-universe/lean/QOU/Mathlib/EllipticDivisorDegree.lean`
**Status:** BEGUN — bricks proved sorry-free; deep theorem stated open (cited `sorry`).

## The theorem

For a nonconstant **elliptic** function `f` (doubly-periodic meromorphic on `ℂ`,
`ℝ`-independent periods `ω₁, ω₂`), the sum of local orders over a fundamental
parallelogram is zero: `Σ_p ord_p f = 0`, i.e. `#zeros = #poles` with
multiplicity (Liouville's third theorem). This is the degree-zero + sign input the
PentagonRigidity Φ₁/Φ₂-entire leg needs to force the doubly-periodic ratio-divisor
(already proved periodic in `MeromorphicSameOrder`) to vanish identically.

## Mathlib v4.24.0 gap survey

Cache is olean-only (root workspace `.lake/packages/mathlib`, 6990 oleans); probed
by `lean`-direct `#check`.

| Piece | In Mathlib? | Name |
|---|---|---|
| Liouville (bounded entire ⇒ const) | ✅ | `Differentiable.exists_const_forall_eq_of_bounded` |
| Meromorphic order (WithTop ℤ) | ✅ | `meromorphicOrderAt`, `…_eq_int_iff`, `…_congr` |
| Divisor (locallyFinsuppWithin U ℤ) | ✅ | `MeromorphicOn.divisor`, `divisor_apply` |
| `logDeriv f = f'/f` | ✅ | `logDeriv`, `logDeriv_apply` |
| deriv of `f(·+a)` | ✅ | `deriv_comp_add_const` |
| `Function.Periodic` | ✅ | `Mathlib.Algebra.Ring.Periodic` |
| Cauchy integral / circle integral | ✅ | `Complex.CauchyIntegral`, `circleIntegral` |
| **Elliptic / doubly-periodic function theory** | ❌ | — |
| **Weierstrass ℘** | ❌ | — |
| **Argument principle** `Σ ord = (1/2πi)∮ f'/f` | ❌ | — |
| **Residue theorem** (general) | ❌ | — (only `CauchyIntegral`, not residue calculus) |
| **Winding number** | ❌ | — |
| **Hadamard factorization / order-genus** | ❌ | — |

`Function.Periodic.deriv` does **not** exist by that name — proved locally from
`deriv_comp_add_const`.

## Bricks landed (sorry-free, Mathlib-only cone → `lean`-direct exit 0)

* `periodic_deriv`, `periodic_logDeriv` — derivative and **`f'/f` of a periodic
  function are periodic**.
* `isElliptic_logDeriv` — logarithmic derivative of an elliptic function is
  elliptic (periodic under both periods). **This is the boundary-cancellation
  half of the argument-principle route, done.**
* `IsElliptic` structure + `fundamentalParallelogram` (half-open cell) definitions.
* `meromorphicOrderAt_translate`, `divisor_translate` — **the order/divisor is
  lattice-periodic** (`meromorphicOrderAt_comp_add` reproved locally, namespaced,
  to keep the cone Mathlib-only; un-namespaced original in `QOU.QBeta.MeromorphicSameOrder`).
* `elliptic_divisor_degree_zero` — **stated open**, cited `sorry`. `Σ` over a
  Finset `S` enumerating the in-cell divisor points (finiteness passed as a
  hypothesis to isolate the analytic core). Not vacuous-`True`, not axiomatized.

## Is the f'/f boundary-cancellation route tractable now?

**Half of it, yes; the closing half, no.** The route is
`Σ_p ord_p f = (1/2πi)∮_{∂P} logDeriv f = 0`.

* **Boundary cancellation (`∮ = 0`): formalizable now.** The integrand
  `logDeriv f` is elliptic (`isElliptic_logDeriv`, proved). Opposite edges of `∂P`
  differ by a period and carry equal integrand with opposite orientation, so they
  cancel. Turning this into a literal `∮_{∂P} logDeriv f = 0` needs only
  `intervalIntegral` over the four parametrized edges + the pointwise periodicity
  already proved — no missing Mathlib theorem, just assembly (moderate effort:
  parametrize edges, orientation bookkeeping, pole-avoidance so `logDeriv` is
  integrable on `∂P`).
* **Argument principle (`Σ ord = (1/2πi)∮`): NOT tractable now.** This is the
  genuine gap. Mathlib has no residue theorem / argument principle linking the
  contour integral of `logDeriv f` to the sum of orders. Building it is a real
  Mathlib contribution (residue calculus for meromorphic functions), out of scope
  for this scaffold.

## Tractable-brick roadmap (ordered)

1. **`∮_{∂P} logDeriv f = 0`** from `isElliptic_logDeriv` + `intervalIntegral` edge
   assembly (moderate; no missing theorem).
2. **In-cell divisor finiteness** — `MeromorphicOn.divisor` is
   `locallyFinsuppWithin`; intersect with the compact closed cell ⇒ finite `S`.
   Discharges the `hS`/`S` hypothesis of `elliptic_divisor_degree_zero` (moderate).
3. **Argument principle for `logDeriv`** — `Σ_{p∈P} ord_p f = (1/2πi)∮_{∂P} f'/f`.
   The deep gap; a standalone Mathlib-grade contribution. Closes the theorem when
   composed with brick 1.
4. **(Alt) Hadamard factorization** — an independent route flagged in the
   pentagon-entire-leg audit; equally absent from Mathlib.

Nothing here is wired to production, fitted, or axiomatized-as-proved.
