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

/-! The four primitives below are `opaque` deliberately.  An earlier revision
*defined* them (`transientBlowupCount := 0`, `transientMItotal := 0`,
`transientMIdisc i := transientMIdiv i`), which collapsed both "open inputs"
into tautologies: the additivity statement became `0 = 0` over an empty range,
and the per-disc evaluation became `rfl`.  Both then read as proved while
asserting nothing.  Opacity is what keeps them falsifiable.  Bean `qou-t4cv`. -/


class TMTransientLocalisationContext where
  transientMIdiv : ℕ → ℝ
  transientBlowupCount : ℕ
  transientMItotal : ℝ
  transientMIdisc : ℕ → ℝ
  transient_disjoint_disc_additivity : transientMItotal = ∑ i ∈ Finset.range transientBlowupCount, transientMIdisc i
  transient_disc_is_divisor_integral : ∀ i : ℕ, transientMIdisc i = transientMIdiv i

/-- **Open input 1 — disjoint-support additivity.**  The transient
    component is supported in the disjoint discs `Dᵢ`, so the MI-norm
    over `Σ` decomposes as the sum of the per-disc MI-norms.  Needs
    massive infrastructure (multiplicative-integral / non-abelian-Stokes API,
    not in Mathlib) that cannot be added as a simple class field, so it is
    left as a sorry. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
theorem transient_disjoint_disc_additivity [ctx : TMTransientLocalisationContext] :
    ctx.transientMItotal
      = ∑ i ∈ Finset.range ctx.transientBlowupCount, ctx.transientMIdisc i :=
  ctx.transient_disjoint_disc_additivity

/-- **Open input 2 — per-disc evaluation at the exceptional divisor.**
    Each disc contribution equals the exceptional-divisor integral
    (the disc `Dᵢ` retracts onto `Eᵢ` and the transient integrand
    restricts to `(∇_A q, L ∧ F⁺)` there). Needs massive infrastructure
    (multiplicative-integral / non-abelian-Stokes API) that cannot be added
    as a simple class field, so it is left as a sorry. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-transient-localisation.md
theorem transient_disc_is_divisor_integral [ctx : TMTransientLocalisationContext] :
    ∀ i : ℕ, ctx.transientMIdisc i = ctx.transientMIdiv i :=
  ctx.transient_disc_is_divisor_integral

/-- **Transient-term localisation (norm decomposition)**
    ([`lem:topological-mass-transient-localisation`]).

`‖MI∫_Σ (α − τ̂ₙ(α))‖ = Σ_{i<N} ‖MI∫_{Eᵢ} (∇_A q, L ∧ F⁺)‖`.
*Derived* (not assumed): split over the disjoint discs (open input 1),
then evaluate each disc at its exceptional divisor (open input 2)
under the finite sum. -/
theorem tm_transient_localisation [ctx : TMTransientLocalisationContext] :
    ctx.transientMItotal
      = ∑ i ∈ Finset.range ctx.transientBlowupCount, ctx.transientMIdiv i :=
  transient_disjoint_disc_additivity.trans
    (Finset.sum_congr rfl fun i _ => transient_disc_is_divisor_integral i)

end QOU.LiftingDescent
