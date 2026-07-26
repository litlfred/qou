# The `H(q₀)` coloring map: the flat shape is a Rogers-dilog inflection ⇒ `g₂` is the octahedral `e₂` term, not the single modulus

**Date:** 2026-07-26 · **Branch:** `claude/coloring-hq0-map-g2-derivation-2026-07-26` ·
**Axis:** Δ_λ binding — the μ₀ −9% closure, the bar-even coefficient `g₂` · **Owner steer:** *"go"*
(derive the `H(q₀)` coloring map) · **Tier:** derivation attempt → **scope-(a) prune** + a solid
formalized structural fact (no fit to `g₂`; nothing wired).

## 0. The task

PR #4301 narrowed the μ₀ −9% residual to a **bar-even function of the single shape modulus `z₀`**
of the deuteron crossing (deuteron `σ₁³` = trefoil `T(2,3)`, torus knot, flat shape `z₀ = ½`, exact
reciprocal partner `z₁ = 1/z₀`), deformed by the coloring's meridian holonomy through
`z₀ = H/(H−1)`. The open step was to **derive the `H(q₀)` map** and read off `g₂ ≈ 1.0087`. This
note reports the attempt: the map *is* derivable and parameter-free, but it **prunes** the
single-modulus route and **redirects** `g₂` to the octahedral `e₂` coupling.

## 1. The single-tetrahedron amplitude is the Rogers dilogarithm

For the flat (degenerate, real-shape) trefoil the octahedral state integral's **volume/imaginary
side vanishes** (`Vol = 0`, PR #4301); the surviving binding channel is the **real phase**, whose
single-tetrahedron value is the **Rogers dilogarithm**

  `L(z) = Li₂(z) + ½·log z·log(1−z)`.

Its second derivative has the elementary closed form (only `Li₂'(z) = −log(1−z)/z` is used; no `Li₂`
value enters)

  `L''(z) = −½·( log z/(1−z)² − log(1−z)/z² )`.

## 2. Solid fact (Lean, sorry-free): `z = ½` is an inflection point

The bracket `B(z) = log z/(1−z)² − log(1−z)/z²` is **antisymmetric under the Abel reflection
`z ↦ 1−z`** (`B(1−z) = −B(z)`), whose fixed point is `z = ½`; hence `B(½) = 0` and **`L''(½) = 0`**.
Formalized in
[`QOU/MassTheory/RogersDilogInflection.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/RogersDilogInflection.lean):

- `rogersL2Bracket_reflect` — `B(1−z) = −B(z)` (the Abel-reflection antisymmetry)
- `rogersL2_half_eq_zero` — `L''(½) = 0` (the inflection)
- `rogersL2Bracket_half_eq_zero` — the inflection *forced by* the reflection at its fixed point

**Stronger empirical statement (probe, from the Euler reflection).** The full Euler reflection
`L(z) + L(1−z) = π²/6` gives `L(½+δ) + L(½−δ) = π²/6` (constant), so **the single-tetrahedron
amplitude is *purely bar-odd* about `z = ½`: every even-order (bar-even) term vanishes** — verified
numerically to 50 dps (`L''(½) = L''''(½) = 0`; only the bar-odd `L'''(½) = 3.09…` survives). So the
single modulus supplies **zero** bar-even at *every* order, not merely the second.

## 3. The parameter-free consistency pin (`κ = ½`)

The octahedral first-order (bar-odd) amplitude must reproduce the **already-derived** μ₀ weight
`3(q−q⁻¹)/2` (μ₀ = m_e/(3(q−q⁻¹)/2), in the paper). Writing the shape deviation `δ = z₀ − ½ =
κ·(q−q⁻¹)`, the symmetric-combination slope `s'(½) = 1 − 1/z₀² = −3` gives `−3δ = −3κ(q−q⁻¹)`, so
matching `3(q−q⁻¹)/2` **pins `κ = ½` — parameter-free, not fitted.** (Suggestive, *not* claimed:
`1/z₀² − 1 = 3` at `z₀ = ½` equals the trefoil crossing number.)

## 4. The `g₂` bracket table (parameter-free consequences; no fit)

With `κ = ½` fixed by μ₀, the bar-even coefficient `g₂ = A₂·κ²` (units `h² = (q−q⁻¹)²`) is a
*consequence* — nothing is tuned to `g₂`:

| single-coordinate amplitude | `A₁` | `A₂` | `g₂ = A₂·κ²` | why |
|---|---|---|---|---|
| **Rogers `L(z)`** (physical, single tet) | `2ln2` | **0** | **0** | `z=½` inflection / purely bar-odd |
| naive symmetric `s = z₀+1/z₀` | `−3` | `8` | **2** | not the physical dilog (double-counts) |
| #4158 W2b cosh/crossing | — | — | `9/8` | algebraic overshoot |
| #4158 W2b BCH/Bernoulli (Magnus) | — | — | `0` | Lie elements, class-(b) |
| **target** | — | — | **1.0087** | the true bar-even coefficient |

**The target `1.0087` is reproduced by no single-coordinate amplitude.** The physical Rogers dilog
gives exactly `0` (it is bar-odd about the flat shape); the naive symmetric combination gives `2`
(a factor-2 overshoot — it is not the state-integral amplitude). So `g₂` is a genuine
**four-tetrahedron** quantity: the **pairwise `e₂` coupling** `Σᵢ<ⱼ aᵢaⱼ` of the octahedron's four
dilogarithms (`FourDilogFirstOrder.e2`, PR #4127), *not* a single-modulus self-term. This also
**explains the whole factor-2 / 9-8 family**: every single-coordinate route is either critical
(Rogers → 0) or double-counting (symmetric → 2; cosh → 9/8) at the flat shape.

## 5. Scope (honest)

**scope-(a).** Proved: the single-modulus bar-even contribution is **identically zero** (the flat
shape is a Rogers-dilog inflection / the amplitude is purely bar-odd by Euler reflection). This
**prunes** the single-modulus route and **localizes** `g₂` to the octahedral `e₂` pairwise coupling.
It does **not** derive `g₂`, and it does **not** exclude the octahedral route — the `e₂` coupling of
the four tetrahedra is the next target (it requires the *relative* shapes/amplitudes of the four
tetrahedra, i.e. the full octahedral decomposition of the crossing, not the single collapsed
modulus). Anti-laundering stands: the Lean proves the *inflection*, not `g₂`; no axiom/class carries
`g₂`.

## 6. Next

Compute the four octahedral tetrahedron amplitudes `a_b, a_t, a_r, a_l` of the deuteron crossing
(the `Z_b, Z_t, Z_r, Z_l` operators, 2509.02354) at the substrate coloring, and evaluate their
bar-even pairwise sum `e₂ = Σᵢ<ⱼ aᵢaⱼ` — the object `FourDilogFirstOrder.e2_bar_even` already
formalizes as bar-even. That is where `g₂` lives; the single collapsed modulus provably does not
carry it.

Refs: [`RogersDilogInflection.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/RogersDilogInflection.lean);
probe [`coloring_hq0_g2_derivation_probe.py`](../../computations/deltalambda/coloring_hq0_g2_derivation_probe.py);
PR #4301 (`2026-07-25-octahedral-chi-coloring-frame-r-narrowing.md`); #4127 (`FourDilogFirstOrder.lean`);
#4158 W2b (`2026-07-25-eunit-g2-derivation-attempt.md`); `hakimoglu-brown2025` (Rogers L-function).
