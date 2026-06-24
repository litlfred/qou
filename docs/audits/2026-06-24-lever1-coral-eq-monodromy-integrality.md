# Lever-1 option 2: coral `E_q` confirmed, but `tr B` is non-integer — `B` is the abelianised connection holonomy, not the topological monodromy

**Date:** 2026-06-24
**Probe:** [`computations/substrate/lever1_coral_eq_monodromy_integrality.py`](../../computations/substrate/lever1_coral_eq_monodromy_integrality.py)
**Witness:** [`computations/substrate/lever1-coral-eq-monodromy-integrality.witness.json`](../../computations/substrate/lever1-coral-eq-monodromy-integrality.witness.json) (7/7)
**Status:** the "compute the genus-1 coral `E_q` Picard–Fuchs monodromy to test `tr B = 2.6424`" step (option 2), executed analytically (Sage unavailable). One confirmation + one decisive reframing. No fit; not owner-gated (curve algebra + a trace-integrality argument). Follows [`2026-06-24-lever1-binding-monodromy-hyperbolicity.md`](2026-06-24-lever1-binding-monodromy-hyperbolicity.md).

## 1. The coral `E_q` IS the descartes elliptic curve (direction-B curve confirmed)

The [`2026-06-24` hyperbolicity audit](2026-06-24-lever1-binding-monodromy-hyperbolicity.md) proposed the rank-2 `W` is `H¹(coral E_z)`. The coral cubic
([`coral-elliptic.md`](../../content/quantum-observable-universe/brings-surface/coral-elliptic.md))
and the Weierstrass form
([`descartes-elliptic-curve.md`](../../content/quantum-observable-universe/brings-surface/descartes-elliptic-curve.md),
`y² = x³ + p(q)x + r(q)`) are now confirmed to be the same curve, by the invariant `j`:

| quantity | computed | `descartes-elliptic-curve.md` |
|---|---|---|
| `j(q₀)` | **129.860** | 129.9 |
| `j(1)` (classical) | **128** | 128 |
| `p(1)`, `r(1)` | **2/3, 20/27** | 2/3, 20/27 (`E₁`) |

(The `Δ` "mismatch" 303 vs 18.95 is the standard `×16` between the naive `−16(4p³+27r²)` and the
minimal-model discriminant; `j` — the actual invariant — matches.) So the rank-2 `W` candidate is a
**single, identified elliptic curve**, not an open genus-4 object — direction B's curve half is closed.

## 2. The decisive obstruction — `tr B = 2.6424 ∉ ℤ`

Option 2's literal goal was to compute the coral `E_q` **Picard–Fuchs monodromy** and test it equals
`τ_binding = 2.6424`. That computation would yield the **wrong object**, for a one-line reason:

> The **topological** Gauss–Manin monodromy of an elliptic-curve family acts on `H¹(E, ℤ) ≅ ℤ²`
> preserving the intersection form, so it lands in **`SL₂(ℤ)`** — every element has **integer trace**.

But `τ_binding = 3(3q⁴+8q²+3)/(4q(q+1)²) = 2.6423863… ∉ ℤ` (nearest integer 3). Therefore **`B` is not a
topological `SL₂(ℤ)` monodromy element of `E_q`** — *(b)-exclusion, invariant cited: integrality of
`SL₂(ℤ)` traces.* The substrate torus is the same: `τ_torus = 2cosh 2η₀ = 2.0437 ∉ ℤ`.

**What `B` is, then.** Per the M-workplan ([`2026-06-06`](../workplans/2026-06-06-deriving-bring-M-abelianisation-scalar.md),
`prop:mi-sw-abelianisation`), the prolonged periods `a_D⁽ⁿ⁾ = ∮ λ_SW⁽ⁿ⁾` are periods of the **abelianised
Cartan sub-connection** `A⁰ = λ_SW`, not of the full integral homology. So `B` is the **holonomy of the
abelianised `λ_SW` flat connection** — a real / hyperbolic `SL₂(ℝ)` element (`τ = 2cosh θ`,
`θ_binding = 0.78145`), **not** the integral topological monodromy. The non-integer trace is the signature
of a non-unitary, infinite-order connection holonomy — exactly what one expects at a substrate `q₀ > 1`
that is **not a root of unity** (the keystone's non-compact / growth-regime arena, reached here from the
binding side).

## 3. Net

- **Confirmed:** coral `E_q` = descartes `E_q` (`j(q₀) = 129.86`); the rank-2 `W` is this identified curve.
- **Reframed (decisive):** `tr B = 2.6424 ∉ ℤ` ⇒ `B` is **not** the topological `SL₂(ℤ)` monodromy; the
  genus-1 Picard–Fuchs **topological**-monodromy computation (option 2's literal target) would return an
  integer-trace object, not `2.6424`. The right object is the **abelianised `λ_SW` connection holonomy**
  (real, hyperbolic), consistent with the M-workplan's Cartan reduction and the keystone non-compact arena.
- **Still open (the keystone step):** the explicit abelianised-connection holonomy `= θ_binding = 0.78145`
  — its derivation from the `λ_SW` connection at `q₀` — is the owner-gated keystone `M` restricted to the
  coral elliptic factor. **Not closed here.** No fit; nothing wired; no tier change.

## Honest scope

This identifies the *type* of object `B` is (abelianised connection holonomy, real trace) and rules out
the *type* it is not (integral topological monodromy) — it does **not** derive `2.6424` from the
connection. The (b)-exclusion is on the **object class** (topological vs connection), not on the coral
`E_q` (which is confirmed). The curve algebra (`j(q₀)`) and the trace-integrality argument are both
parameter-free and tool-independent (no Sage); the residual is the keystone connection holonomy.
