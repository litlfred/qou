# W1 route 1 pruned: no rational base q-connection carries the colour sheets

**Date:** 2026-09-04 · **Bean:** `qou-1z28` · follows `qou-an6y` (#6652), `qou-col1` (#6628), `qou-w0tx` (#6610), `qou-33hb` (#6582)
**Lean:** [`QOU/Mass/ColorCubicIrreducible.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/ColorCubicIrreducible.lean) — sorry-free, generic `[Field K] [CharZero K]`, axioms `propext / Classical.choice / Quot.sound` only
**Probe:** [`w1_base_qshift_rationality_prune_probe.py`](../../computations/probes/w1_base_qshift_rationality_prune_probe.py) — exact sympy over `ℚ` / `ℚ(q)`, no float64, no witness by design
**Cited invariant (external, not held in `library/`):** a formal power series that satisfies both a linear differential equation and a linear q-difference equation with rational coefficients, `q` not a root of unity, is a rational function — J.-P. Bézivin, *Sur les équations fonctionnelles aux q-différences*, Aequationes Math. 43 (1992) 159–176; J.-P. Ramis, *About the growth of entire functions solutions of linear algebraic q-difference equations*, Ann. Fac. Sci. Toulouse 1 (1992) 53–94; unified with the Mahler case in R. Schäfke & M. F. Singer, *Consistent systems of linear differential and difference equations*, J. Eur. Math. Soc. 21 (2019) 2751–2792.

## What was asked

#6652 counted that, on the level axis, the content of "prolongation symbol = `L_K`"
is entirely in where the weights of `D_q` come from — wall W1 (`qou-d8de`, construct
`D_q` from the colour spectral curve Σ). The first route that bean names is a
**q-shift on the base**, `z ↦ q²z`, with a q-connection lift to the jet tower.
Formalize-first: before anyone builds it, can it exist?

## The argument

Let `P(X,z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)` be the colour cubic and
`X₁(z), X₂(z), X₃(z)` its three sheets.

1. **`P` is irreducible over `ℂ(z)`** — proved. `QOU.Mass.ColorCubicIrreducible.colorCubicAt_ne_zero`:
   no `r ∈ K[z]` is a root, for any field `K` of characteristic zero. Degree `≥ 2`
   is excluded by the leading term (`r³` has degree `3d`, the other terms `1+2d`,
   `2+d`, `3`). Degree `≤ 1`, `r = az + b`: the `z³`-coefficient `(a+1)(a²+1)`
   forces `a = −1` or `a² = −1`, and each branch turns the `z²`- and
   `z⁰`-coefficients into an inconsistent pair, with integer Bézout certificates
   `8·c₀ − (4b²+2b+3)·(2b+1) = 5` and `(8b²−4b+1)·(8b²+4b+1) + (64−64b)·c₀ = 65`.
   `colorCubic_no_ratFunc_root` lifts this to `K(z)` by Gauss (the cubic is monic over
   the integrally closed `K[z]`, Mathlib `IsIntegrallyClosed.isIntegral_iff`). A cubic
   with no root over a field is irreducible, so **no sheet is a rational function of
   `z`**.
2. **Each sheet is D-finite** — algebraic functions satisfy a linear ODE with
   polynomial coefficients. This is the *classical* prolongation, the one
   `prop:sw-classical-jet-exactness` proves exact and therefore dead for the
   binding period. The probe makes it explicit (§2 below).
3. **A rational base q-connection would make a sheet q-holonomic.** If a rank-3
   q-difference system `Y(λz) = A(z) Y(z)` with `A ∈ GL₃(ℂ(z))` had the three sheets
   as solutions, then `X₁(z), X₁(λz), X₁(λ²z), X₁(λ³z)` are four vectors in the
   3-dimensional `ℂ(z)`-span of `X₁, X₂, X₃`, hence `ℂ(z)`-linearly dependent: a
   scalar linear q-difference equation of order `≤ 3` with rational coefficients for
   `X₁`. (`λ = q²` in the bean; any `λ` that is not a root of unity.)
4. **D-finite ∧ q-holonomic ⇒ rational** (the cited theorem, applied to `X₁` as a
   power series at `z = 0`, where `P(X,0) = (X+1)(X²+1)` has simple roots so each
   sheet is a genuine power series). Contradiction with 1.

**Conclusion (scope (b), invariant cited).** No rational rank-3 q-difference system
on the `z`-line in a dilation `z ↦ λz`, `λ` not a root of unity, has the colour
sheets as flat sections. The classical connection on the base exists and is exact;
its rational q-analogue does not exist. Whatever `D_q` is, it is **not** a
q-holonomic system on the base.

## What the probe measured (exact)

§1 reproduces the irreducibility argument in sympy (one irreducible factor over
`ℚ[X,z]`; no constant root; no affine root over `ℚ̄`; both certificates evaluate to
`5` and `65`).

§2 exhibits the D-finite side without series: reducing `X, X', X'', X'''` in the
`ℚ(z)`-basis `{1, X, X²}` of `ℚ(z)[X]/(P)` (with `X' = −P_z/P_X` and `P_X` inverted
modulo `P`) gives four vectors in a 3-space, whose null vector is the ODE

| | |
|---|---|
| `p₀(z)` | `−30 · P(1,z) · P(z,z)` where `P(1,z) = z³+2z²+3z+4`, `P(z,z) = 4z³+3z²+2z+1` |
| `p₁(z)` | `30 (z+1) · P(1,z) · P(z,z)` |
| `p₂(z)` | `3 (z−1)(32z⁹ + 24z⁸ − 44z⁷ − 197z⁶ − 395z⁵ − 467z⁴ − 459z³ − 316z² − 138z − 40)` |
| `p₃(z)` | `(z−1)²(z+1)(2z²+z+2) · D(z)`, `D` the branch sextic `16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16` |

so the classical prolongation has order 3 and its leading coefficient vanishes
exactly on the branch locus (plus apparent singularities at `z = ±1` and the roots of
`2z²+z+2`) — the ramification points of Σ are where the classical connection is
singular, as the jet-pole picture of `qou-xufp` says.

§3 searches, on the sheet through `X(0) = −1` (`x₀..x₆ = −1, −1/2, 0, −5/16, 5/32,
5/128, 5/256`, exact, verified through `z⁴⁰`), for `Σ_{k≤3} c_k(z) X(qᵏz) = 0` with
`deg c_k ≤ D`:

| test | result |
|---|---|
| `q ∈ {11/10, 2, 3/2}`, `D ∈ {2, 4, 6}`, 41 equations | nullspace dimension **0** in all nine cases |
| symbolic `q`, `D ∈ {2, 4, 6}` | full column rank (`12 / 20 / 28`) at `q = 17/5` and `7/3`, so **no relation over `ℚ(q)`** either |

The symbolic verdict uses rank rather than symbolic elimination: the rank over
`ℚ(q)` is at least the rank at any rational specialisation, so full column rank at
one specialisation excludes a relation over `ℚ(q)`. (The first version of the probe
ran sympy's nullspace over `ℚ(q)` directly and did not finish `D = 1` in ten
minutes; the rank form is exact and takes seconds.)

§4 runs two controls through the same searcher: the differential search on the same
series **finds** an ODE proportional to §2's, and the q-search on `1/(1−z)` **finds**
`(1−z) f(z) − (1−qz) f(qz) = 0`. So the null result of §3 is a property of the sheet,
not of the searcher.

§3–§4 are **corroboration**: a finite search excludes only the orders and degrees it
tests. The exclusion of *all* orders and degrees is the theorem.

## Scope — what is and is not pruned

- **Pruned (b):** W1 route 1 as stated — a q-connection on the base `z`-line with
  coefficients in `ℂ(z)` whose flat sections are the sheets. Any `D_q` built that
  way must carry the sheets non-trivially, and then its action on the jets is not
  determined by Σ, which is the same "weights are free" defect #6652 counted.
- **Not pruned:** coefficients algebraic in `z` (i.e. in `ℂ(Σ)` — but a base
  dilation does not lift to Σ canonically; which sheet `X_i(λz)` continues to is a
  choice, and the theorem says no choice is rational); operators defined on Σ rather
  than on the base; the **local** q-dilation `t ↦ qt` at a ramification point, where
  every power series satisfies a first-order q-equation with a power-series
  coefficient and the theorem does not apply. The level-reading results of
  #6628/#6652 live in that local chart, and this prune is why they have to.
- **Not touched:** the conjecture itself. This closes its cheapest global
  realisation, not the identification.

## What it changes for the arc

The three named routes of `qou-d8de` are now: (1) **excluded** as a rational base
q-connection; (2) root-of-unity fibre monodromy — untouched; (3) import the
Ramis–Sauloy–Zhang / Sauloy local framework — untouched and, after this, the
natural next step, since the object that survives is local at the branch point. The
pattern across #6582 → #6652 → here is consistent: every global or untuned
realisation of "symbol = `L_K`" fails or is empty, and the content keeps
retreating to the ramified local chart.

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/w1_base_qshift_rationality_prune_probe.py
# Lean (lean-direct, restored olean cache):
lean content/quantum-observable-universe/lean/QOU/Mass/ColorCubicIrreducible.lean
```
