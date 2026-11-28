import QOU.MassTheory.PairSkeinMassConventionD

/-!
# QOU.HadronicMass.pair_skein_mass_formula

**Lemma** ([`lem:pair-skein-mass-formula`](../../../mass-theory/pair-skein-mass-formula.md)).
*The Borromean braid of a nucleon with quarks `(q₁, q₂, q₃)` contributes a
pair Skein mass at each of its three strand pairs:*

    𝒮_{ab}(q) = (q³ μ_a + q⁻¹ μ_b) / (q² + 1),

*where `μ_a` is the dressed quark Skein mass of species `a`. The total
nucleon mass is the sum over the three strand pairs.*

## Convention D, derived (owner ruling 2026-11-27)

The formula is the convention-D Markov trace of the pair's crossing element:
`𝒮_{ab} = trace₂ z_D (μ_a·σ + μ_b·σ⁻¹)` in `H₂(q)`, with
`z_D = q³/(q² + 1)`. It is derived in `QOU.MassTheory.PairSkeinD`
(`pairMassD_closed`); `pair_skein_mass_formula_of_pairMassD` below records
that the derived pair mass satisfies the named formula.

The convention-C form `(q μ_a + q⁻¹ μ_b)/(q^{1/2} + q^{-1/2})`, which stood
here until 2026-11-27, is retired. Its denominator was never derived (the
proof block said so), and `1/(q^{1/2} + q^{-1/2}) = z_C` is the excised
convention-C Markov parameter. Its square-root variable and its archimedean
companion `QOU.Transcendental.MassTheory.PairSkeinMassFormulaReal` are
removed with it.

## History (kept)

Until 2026-09-03 this file projected the identity out of a class hypothesis
while its docstring denied doing so (bean `qou-z9ws`). The formula has since
been a `Prop`-valued definition over caller-supplied data, refutable at free
data (`not_pair_skein_mass_formula_of_free_data`).

Base ring (§7c): a generic field.
-/

namespace QOU.HadronicMass

open QOU.MassTheory.PairSkeinD

/-- The pair Skein mass formula under convention D:
`𝒮_ab = (q³ μ_a + q⁻¹ μ_b) / (q² + 1)`. Named, not asserted. -/
def pair_skein_mass_formula {K : Type*} [Field K] (q : K) (μ : ℕ → K)
    (S_ab : ℕ → ℕ → K) : Prop :=
  ∀ a b : ℕ, S_ab a b = (q ^ 3 * μ a + q⁻¹ * μ b) / (q ^ 2 + 1)

/-- **The derived pair mass satisfies the formula.** The convention-D Markov
trace `pairMassD q (μ a) (μ b)` of the crossing element is the pair Skein
mass. -/
theorem pair_skein_mass_formula_of_pairMassD {K : Type*} [Field K] (q : K)
    (μ : ℕ → K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    pair_skein_mass_formula q μ (fun a b => pairMassD q (μ a) (μ b)) :=
  fun a b => pairMassD_closed q (μ a) (μ b) hq hq2

/-- **Species exchange is antisymmetric with the Skein coefficient**:
`𝒮_ab − 𝒮_ba = (q − q⁻¹)(μ_a − μ_b)`. The factor `q² + 1` cancels, because
`q³ − q⁻¹ = (q − q⁻¹)(q² + 1)`. -/
theorem pair_skein_difference {K : Type*} [Field K] {q : K} {μ : ℕ → K}
    {S_ab : ℕ → ℕ → K} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h : pair_skein_mass_formula q μ S_ab) (a b : ℕ) :
    S_ab a b - S_ab b a = (q - q⁻¹) * (μ a - μ b) := by
  rw [h a b, h b a]
  field_simp
  ring

/-- **Refutable at free data**: at `q = 1` with zero dressed masses the
right-hand side is `0`, so a pair Skein mass of `1` fails. -/
theorem not_pair_skein_mass_formula_of_free_data {K : Type*} [Field K] :
    ¬ pair_skein_mass_formula (1 : K) (fun _ => 0) (fun _ _ => 1) := by
  intro h
  have := h 0 0
  simp at this

end QOU.HadronicMass
