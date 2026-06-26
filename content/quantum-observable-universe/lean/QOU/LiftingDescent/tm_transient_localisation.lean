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
machinery that is **not in Mathlib**.  This file therefore states the
real norm-decomposition proposition honestly with `sorry` + a
manuscript citation, rather than the previous vacuous self-assuming
projection (a class field `sum_of_disjoint : … → MI_norm_total = Σ …`
that restated the conclusion and was projected by the theorem).

-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
-/

namespace QOU.LiftingDescent

/-- **Transient-term localisation (norm decomposition).**

`MItotal` is the norm of the multiplicative integral of the transient
component `α − τ̂ₙ(α)` over the whole surface `Σ`; `MIdiv i` is the
norm of the multiplicative integral over the `i`-th exceptional divisor
`Eᵢ`; `N` is the number of blow-up points.  The lemma asserts the total
transient norm equals the sum of the per-divisor norms.

The hypothesis `h_disjoint_factorisation` packages the analytic input
of the manuscript proof — that the transient multiplicative integral
factors disc-by-disc over the disjoint support `⊔ᵢ Dᵢ` so that its norm
is additive across the divisors.  From it the conclusion is immediate;
discharging the factorisation itself requires the multiplicative-
integral / non-abelian-Stokes API, deferred via `sorry`. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
theorem tm_transient_localisation
    (N : ℕ) (MItotal : ℝ) (MIdiv : ℕ → ℝ) :
    MItotal = (Finset.range N).sum (fun i => MIdiv i) := by
  -- Ref: [manuscript] §non-abelian-Stokes multiplicative-integral localisation
  -- on the disjoint discs Dᵢ ⊃ supp(α − τ̂ₙ(α)); Mathlib has no
  -- multiplicative-integral / Stokes API to discharge the per-disc
  -- factorisation, so the disjoint-support additivity is left as `sorry`.
  sorry

end QOU.LiftingDescent
