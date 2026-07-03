import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

/-!
# QOU.LiftingDescent.tm_transient_localisation

Canonical Lean for content block
[`lem:topological-mass-transient-localisation`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md):
*Transient terms localise to exceptional divisors.*

**Lemma.** The transient component `α − τ̂ₙ(α)` has support contained in
disjoint discs `Dᵢ` centred at the blow-up points `p₁, …, p_N`, and the
norm of the multiplicative integral decomposes as a sum over the
exceptional divisors `Eᵢ`:

  `‖MI∫_Σ (α − τ̂ₙ(α))‖ = Σᵢ ‖MI∫_{Eᵢ} (∇_A q, L ∧ F⁺)‖`.

The genuine mathematical content is the **additivity of the
multiplicative-integral norm over a disjoint support decomposition**.
The non-circular input is the per-disc factorisation of the
multiplicative integral (each `Eᵢ` contributes the integral over its
disc `Dᵢ`, and disjointness of the discs makes the contributions add),
which rests on the non-abelian-Stokes / multiplicative-integral
machinery that is **not in Mathlib**.

Following the sibling pattern of
`QOU.TopologicalMass.cat_transient_localises_blowup`, the quantities
are modelled as named `opaque` constants — `transientMItotal` (the
total transient MI-norm over `Σ`), `transientMIdiv i` (the per-divisor
MI-norm at `Eᵢ`), with `transientBlowupCount` blow-up points — so the
theorem `transientMItotal = Σ_{i<N} transientMIdiv i` is the genuine
unproven localisation identity between *these specific* objects (a
prior revision universally quantified over arbitrary reals, which made
the statement false as stated).  Discharged with `sorry` per
AGENTS.md §1.

-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
-/

namespace QOU.LiftingDescent

/-- Number of blow-up points `N` (centres `p₁, …, p_N`). -/
opaque transientBlowupCount : ℕ

/-- The norm of the multiplicative integral of the transient component
    `α − τ̂ₙ(α)` over the whole surface `Σ`:
    `‖MI∫_Σ (α − τ̂ₙ(α))‖`. -/
opaque transientMItotal : ℝ

/-- The norm of the multiplicative integral over the `i`-th exceptional
    divisor `Eᵢ`: `‖MI∫_{Eᵢ} (∇_A q, L ∧ F⁺)‖`. -/
opaque transientMIdiv : ℕ → ℝ

/-- **Transient-term localisation (norm decomposition).**

The total transient MI-norm equals the sum of the per-divisor MI-norms
over the `transientBlowupCount` blow-up points.  The analytic input is
the per-disc factorisation of the transient multiplicative integral
over the disjoint support `⊔ᵢ Dᵢ` (making the norm additive across the
divisors); discharging it requires the multiplicative-integral /
non-abelian-Stokes API, which is not in Mathlib, so the body is
`sorry`. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
theorem tm_transient_localisation :
    transientMItotal
      = (Finset.range transientBlowupCount).sum (fun i => transientMIdiv i) := by
  -- Ref: [manuscript] §non-abelian-Stokes multiplicative-integral localisation
  -- on the disjoint discs Dᵢ ⊃ supp(α − τ̂ₙ(α)); Mathlib has no
  -- multiplicative-integral / Stokes API to discharge the per-disc
  -- factorisation, so the disjoint-support additivity is left as `sorry`.
  sorry

end QOU.LiftingDescent
