# z2bn Lever-1 τ — Gauss–Manin prolongation probe SPEC (for a Sage runner)

**Date:** 2026-06-25
**Bean:** `z2bn` (Lever-1 FOCUS)
**Spec script:** [`computations/substrate/z2bn_tau_gauss_manin_sage_probe.py`](../../computations/substrate/z2bn_tau_gauss_manin_sage_probe.py)
**Builds on:** [`2026-06-25-z2bn-tau-derivation-first-probe.md`](2026-06-25-z2bn-tau-derivation-first-probe.md)
(first probe, mpmath) · [`sl2-prolongation-recurrence.md`](../../content/quantum-observable-universe/mass-theory/sl2-prolongation-recurrence.md)
· [`mi-sw-abelianisation-cartan.md`](../../content/quantum-observable-universe/brings-surface/mi-sw-abelianisation-cartan.md)

> **Status: SPEC, not a result.** Authored where SageMath is unavailable. The
> script's Section A (anchors/target) runs in plain Python and reproduces the
> corpus values (τ(q₀)=2.642386, θ=0.781454); Sections B–E **require Sage and
> are untested here** (`NotImplementedError` markers flag the runner's TODO).
> Nothing is wired to production; no fit anywhere.

## Why a second probe

The first probe nailed two clean pieces and one clean negative:

| | result |
|---|---|
| (A+) | τ closed form `3(3q⁴+8q²+3)/(4q(q+1)²)` — **Lean-proved** (`tau_kernel_closed_form`) |
| (B+) | coral curve `E_q` **confirmed** (`j(q₀)=129.86`) |
| (E−) | **bare-period (a)-negative** — no single-curve period reproduces τ (≈6 % near-miss) |

(E−) is *expected*, not a dead end. Per `sl2-prolongation-recurrence.md`, the
kernel `R = x² − τx + 1` comes from the **2×2 Gauss–Manin prolongation operator
`B`** on the rank-2 Hodge plane `W` (`H¹(Bring)=2W`); `det B = 1` because GM
preserves the principal polarisation, so `τ = tr B` is the whole content. A
**single curve has no monodromy** — so a fixed-curve period *cannot* supply
`τ`; the object is the **q-family** GM monodromy. The integrality finding
(`2026-06-24-lever1-coral-eq-monodromy-integrality.md`) sharpens it: a
*topological* elliptic monodromy is `SL₂(ℤ)` (integer trace) but `τ=2.6424∉ℤ`,
so `B` is the **abelianised λ_SW Cartan-connection holonomy**
(`mi-sw-abelianisation-cartan.md`: `A⁰ = X dz = λ_SW`), a real/hyperbolic
`SL₂(ℝ)` element, `τ = 2cosh θ`.

The non-trivial unknown is the **prolongation operator** `λ_SW^(n) ↦ a_D^(n)`:
the anchors are **not** the bare power sums (`a_D³=(z²+4)/3 ≠ p₂(z)`). Computing
it is a Gauss–Manin / Picard–Fuchs job — what Sage does and mpmath cannot.

## Geometry (q₀ and 2.6424 never feed the construction)

- **Curve** `E_q : y² = x³ + p(q)x + r(q)`, `p = 2(q²−q+1)/(3q)+(q−1)/(3√q)`,
  `r = 20(q−1)³/(27q^{3/2})+5(q−1)²/(9q)+5(√q−1/√q)/9+20/27`.
- **Spectral cubic** `X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0`, `z=√q−1/√q`;
  `λ_SW = X dz`.
- **Anchors** `a_D²=1`, `a_D³=(q+1)²/(3q)`, `a_D⁴=(3q²+4+3q⁻²)/4`;
  `τ=(a_D²+a_D⁴)/a_D³`, `θ=acosh(τ/2)`. Targets at q₀: `τ=2.642386`,
  `θ=0.781454`, `λ=e^θ=2.184646`.

## The three principled candidates (each falsifiable; no fit)

| | construction | decisive test |
|---|---|---|
| **C1** GM-covariant prolongation | `a_D^(n)=∮(∇_GM)^{n-2}λ_SW`, `∇_GM`=Picard–Fuchs covariant `∂_q` | do the geometric `a_D^(2,3,4)(q)` equal `1, (q+1)²/(3q), (3q²+4+3q⁻²)/4` symbolically (normalise only by `a_D²=1`)? |
| **C2** monodromy iterate | `B`=GM monodromy of `H¹_dR(E_q)` on `W` around the binding loop `γ⊂q`-plane | `tr B = 2.642386` (∉ℤ ⇒ abelianised, not topological) **and** `det B = 1` |
| **C3** abelianised holonomy | `θ=∮_γ A⁰` (Cartan/U(1) part, `A⁰=λ_SW`), `τ=2cosh θ` | `∮_γ A⁰ = 0.781454` at q₀ |

**Decisive logic.** If one candidate reproduces the anchors/target to `<1e-12`
with the geometry blind to `2.6424`, that is an **(a)-positive derivation** of
the keystone `τ` — Lever-1's owner-gated residual closes. A near-but-not-exact
hit is **not** a derivation (numerology guard): re-scope to `(a)-negative` and
move to the next candidate. The first probe already showed bare periods are a
6 % near-miss — so C1/C2/C3 must beat that *exactly*, not approximately.

## What the Sage runner must supply (the `# VERIFY` TODOs)

1. **Section B** — assemble the 2nd-order Picard–Fuchs ODE for `∮ dx/y` of
   `E_q(s)` (Griffiths–Dwork) and expose `∇_GM` on the period vector `(ω,∇ω)`.
2. **Section C** — implement C1/C2/C3 against that connection; each returns its
   geometric value + the boolean `|value − target| < TOL`.
3. Confirm the anti-fit invariant: the target constants appear **only** in the
   C-tests, never in B's or C's construction.

## (a)/(b) scope

- **(a)+ standing:** τ closed form (Lean); curve `j(q₀)=129.86` (probe 1).
- **OPEN (owner-gated keystone):** the prolongation operator `B` / its trace
  `τ` from the q-family Gauss–Manin connection. This spec is the executable
  next step, ready for any Sage-enabled environment. It does **not** itself
  close the gate — Sage was unavailable at authoring time.
