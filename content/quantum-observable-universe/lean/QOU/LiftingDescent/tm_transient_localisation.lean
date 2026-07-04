import Mathlib.Tactic

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

## Structure (hypotheses vs. derivation)

The `.md` lemma's two clauses map to two genuine sub-claims, each
stated as its own named proposition (honest `sorry` + citation per
AGENTS.md §1, §1a item 2); the main theorem *derives* the displayed
identity by chaining them (`trans` + `Finset.sum_congr`) — it does not
assume its conclusion:

1. `transient_disjoint_disc_additivity` — the support of
   `α − τ̂ₙ(α)` is contained in the disjoint discs `Dᵢ`, so the
   MI-norm over `Σ` is additive across the discs:
   `‖MI∫_Σ (α − τ̂ₙ(α))‖ = Σᵢ ‖MI∫_{Dᵢ} (α − τ̂ₙ(α))‖`.
2. `transient_disc_is_divisor_integral` — each disc contribution
   evaluates to the exceptional-divisor integral (the disc `Dᵢ`
   retracts onto `Eᵢ`):
   `‖MI∫_{Dᵢ} (α − τ̂ₙ(α))‖ = ‖MI∫_{Eᵢ} (∇_A q, L ∧ F⁺)‖`.

Both rest on the non-abelian-Stokes / multiplicative-integral
machinery that is **not in Mathlib**; each is a *visible* sorried gap.
The per-disc MI-norms `transientMIdisc` are genuine quantities of the
proof narrative, not a laundering device.  (An earlier revision
carried the decomposition as a class field `sum_of_disjoint` over
opaque Props and projected it, which was the self-assuming-projection
anti-pattern; a still earlier one universally quantified over
arbitrary reals, which made the statement false as stated.)

## Model

Quantities are named `opaque` reals (an `opaque` constant needs a
concrete inhabited carrier; the MI-norms are archimedean real values,
so `ℝ` is the honest carrier per §7c).

-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
-/

namespace QOU.LiftingDescent

/-- Number of blow-up points `N` (centres `p₁, …, p_N`). -/
opaque transientBlowupCount : ℕ

/-- The norm of the multiplicative integral of the transient component
    `α − τ̂ₙ(α)` over the whole surface `Σ`:
    `‖MI∫_Σ (α − τ̂ₙ(α))‖`. -/
opaque transientMItotal : ℝ

/-- The norm of the multiplicative integral of the transient component
    over the `i`-th disc `Dᵢ` (centred at the blow-up point `pᵢ`):
    `‖MI∫_{Dᵢ} (α − τ̂ₙ(α))‖`. -/
opaque transientMIdisc : ℕ → ℝ

/-- The norm of the multiplicative integral over the `i`-th exceptional
    divisor `Eᵢ`: `‖MI∫_{Eᵢ} (∇_A q, L ∧ F⁺)‖`. -/
opaque transientMIdiv : ℕ → ℝ

/-- **Open input 1 — disjoint-support additivity.**  The transient
    component is supported in the disjoint discs `Dᵢ`, so the MI-norm
    over `Σ` decomposes as the sum of the per-disc MI-norms.  Needs
    the multiplicative-integral / non-abelian-Stokes API (not in
    Mathlib); body is `sorry`. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
theorem transient_disjoint_disc_additivity :
    transientMItotal
      = ∑ i ∈ Finset.range transientBlowupCount, transientMIdisc i := by
  -- Needs: supp(α − τ̂ₙ(α)) ⊆ ⊔ᵢ Dᵢ with the Dᵢ disjoint, making the
  -- MI-norm additive across the discs.
  sorry

/-- **Open input 2 — per-disc evaluation at the exceptional divisor.**
    Each disc contribution equals the exceptional-divisor integral
    (the disc `Dᵢ` retracts onto `Eᵢ` and the transient integrand
    restricts to `(∇_A q, L ∧ F⁺)` there); body is `sorry`. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
theorem transient_disc_is_divisor_integral :
    ∀ i : ℕ, transientMIdisc i = transientMIdiv i := by
  -- Needs: the Briggs–Klein retraction of Dᵢ onto Eᵢ identifying the
  -- per-disc multiplicative integral with the divisor integral.
  sorry

/-- **Transient-term localisation (norm decomposition)**
    ([`lem:topological-mass-transient-localisation`]).

`‖MI∫_Σ (α − τ̂ₙ(α))‖ = Σ_{i<N} ‖MI∫_{Eᵢ} (∇_A q, L ∧ F⁺)‖`.
*Derived* (not assumed): split over the disjoint discs (open input 1),
then evaluate each disc at its exceptional divisor (open input 2)
under the finite sum. -/
theorem tm_transient_localisation :
    transientMItotal
      = ∑ i ∈ Finset.range transientBlowupCount, transientMIdiv i :=
  transient_disjoint_disc_additivity.trans
    (Finset.sum_congr rfl fun i _ => transient_disc_is_divisor_integral i)

end QOU.LiftingDescent
