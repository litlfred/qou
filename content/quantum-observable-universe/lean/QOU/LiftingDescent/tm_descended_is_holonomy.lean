import Mathlib.Tactic

/-!
# QOU.LiftingDescent.tm_descended_is_holonomy

**Lemma** ([`lem:topological-mass-holonomy`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-holonomy.md)).

*Under the topological blow-up decomposition
`Σ = Σ₀ ∪ ⋃_{i=1}^N D_i`, where `Σ₀` is a disc spanning the unknot core
`ϱ₀` and each `D_i` is the exceptional disc at the `i`-th blow-up, the
descended term equals the unknot-core holonomy:*

    MI∫_Σ τ̂ₙ(α) = Hol_{∇A}(ϱ₀; 𝔊).

## Structure (hypotheses vs. derivation)

The proof narrative has three genuine sub-claims, each stated as its
own named proposition (honest `sorry` + citation per AGENTS.md §1,
§1a item 2), and the main theorem *derives* the .md identity by
composing them — it does not assume the conclusion:

1. `descended_MI_factorises` — the multiplicative integral is
   multiplicative over the blow-up decomposition:
   `MI∫_Σ = MI∫_{Σ₀} · Π_i MI∫_{D_i}` (Yekutieli multiplicative
   integration on surfaces).
2. `descended_exceptional_disc_trivial` — the *descended* term
   `τ̂ₙ(α)` is base-level, so its contribution over each exceptional
   disc `D_i` is trivial: `MI∫_{D_i} τ̂ₙ(α) = 1`.
3. `descended_core_stokes` — non-abelian Stokes on the spanning disc:
   `MI∫_{Σ₀} τ̂ₙ(α) = Hol_{∇A}(ϱ₀; 𝔊)`.

The derivation collapses the product of trivial exceptional-disc
contributions (`Finset.prod_eq_one`, `mul_one`) and chains through
Stokes — a genuine algebraic composition, per the
lean-proof-vacuity-audit fix recipe and AGENTS.md §3b-cond item 5.

## Model

The multiplicative-integral values are modelled as named `opaque`
reals (an `opaque` constant needs a concrete inhabited carrier, so a
generic `R` per §7c is unavailable; group-valued holonomies enter this
chapter through their archimedean scalar values).
-/

namespace QOU.LiftingDescent

/-! The five primitives below are `opaque`.  That is load-bearing, not
stylistic: an earlier revision *defined* them (`descendedBlowupCount := 0`,
`descendedMIdisc := 1`, `descendedMI := descendedMIcore := unknotHolonomy`),
which silently collapsed all three "open inputs" into tautologies —
`descended_MI_factorises` became `x = x * (empty product)`, and the other two
became `rfl`.  The three theorems then *looked* proved while asserting nothing,
and `tm_descended_is_holonomy` "derived" its conclusion from them.  Keeping the
primitives opaque is what makes the open inputs falsifiable statements and the
final theorem a genuine composition.  Bean `qou-t4cv`. -/

/-- The unknot-core holonomy `Hol_{∇A}(ϱ₀; 𝔊)`. -/
opaque unknotHolonomy : ℝ

/-- Number of blow-up points `N` in the decomposition
    `Σ = Σ₀ ∪ ⋃_{i=1}^N D_i`. -/
opaque descendedBlowupCount : ℕ

/-- The descended-term multiplicative surface integral over the whole
    surface: `MI∫_Σ τ̂ₙ(α)`. -/
opaque descendedMI : ℝ

/-- The descended-term multiplicative integral over the spanning disc
    `Σ₀` of the unknot core: `MI∫_{Σ₀} τ̂ₙ(α)`. -/
opaque descendedMIcore : ℝ

/-- The descended-term multiplicative integral over the `i`-th
    exceptional disc: `MI∫_{D_i} τ̂ₙ(α)`. -/
opaque descendedMIdisc : ℕ → ℝ

class TmDescendedInputs : Prop where
  /-- Open input 1 -/
  factorises : descendedMI = descendedMIcore * ∏ i ∈ Finset.range descendedBlowupCount, descendedMIdisc i
  /-- Open input 2 -/
  trivial : ∀ i : ℕ, descendedMIdisc i = 1
  /-- Open input 3 -/
  stokes : descendedMIcore = unknotHolonomy

/-- **Open input 1 — multiplicativity over the blow-up decomposition.**
    Yekutieli's multiplicative surface integral is multiplicative over
    `Σ = Σ₀ ∪ ⋃ D_i`; not in Mathlib. -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
theorem descended_MI_factorises [ctx : TmDescendedInputs] :
    descendedMI
      = descendedMIcore
          * ∏ i ∈ Finset.range descendedBlowupCount, descendedMIdisc i :=
  ctx.factorises

/-- **Open input 2 — the descended term is trivial on exceptional
    discs.**  `τ̂ₙ(α)` is base-level (descended), so it carries no
    contribution over the blow-up discs `D_i`. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-holonomy.md
theorem descended_exceptional_disc_trivial [ctx : TmDescendedInputs] :
    ∀ i : ℕ, descendedMIdisc i = 1 :=
  ctx.trivial

/-- **Open input 3 — non-abelian Stokes on the spanning disc.**
    The multiplicative integral of the descended term over `Σ₀` is the
    boundary holonomy of the unknot core `ϱ₀`. -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
theorem descended_core_stokes [ctx : TmDescendedInputs] :
    descendedMIcore = unknotHolonomy :=
  ctx.stokes

/-- **Descended term = unknot-core holonomy**
    ([`lem:topological-mass-holonomy`]).

`MI∫_Σ τ̂ₙ(α) = Hol_{∇A}(ϱ₀; 𝔊)`.  *Derived* (not assumed): factorise
over the blow-up decomposition, collapse the product of trivial
exceptional-disc contributions, then apply Stokes on the spanning
disc. -/
theorem tm_descended_is_holonomy [TmDescendedInputs] : descendedMI = unknotHolonomy := by
  rw [descended_MI_factorises,
    Finset.prod_eq_one fun i _ => descended_exceptional_disc_trivial i,
    mul_one]
  exact descended_core_stokes

end QOU.LiftingDescent
