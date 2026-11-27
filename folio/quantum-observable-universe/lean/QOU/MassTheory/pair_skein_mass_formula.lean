import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# QOU.HadronicMass.pair_skein_mass_formula

**Lemma** ([`lem:pair-skein-mass-formula`](../../../mass-theory/pair-skein-mass-formula.md)).

*The Borromean braid of a nucleon with quarks `(q₁, q₂, q₃)` contributes
a pair Skein mass at each of its three color-exchange crossing pairs:*

    𝒮_{ab}(q) = (q μ_a + q⁻¹ μ_b) / (q^{1/2} + q^{-1/2}),

*where `μ_a` is the dressed quark Skein mass of species `a`.  The total
nucleon mass is the sum over the three crossing pairs.*

## 2026-09-03 — the docstring denied, by name, what the code did

The module docstring said:

> *"The categorical pair Skein mass `S_ab` and the dressed masses `μ` are
> modelled as named **`opaque` reals**, so the theorem … is the genuine
> unproven identity between *these specific* objects (**not a restatement of
> a definitional field, and not a projection of a class hypothesis**).
> **Discharged with `sorry`** and the citation per AGENTS.md §1."*

`S_ab` and `μ` were **fields** of `PairSkeinMassContext`, not `opaque`; the
body was `exact ctx.pair_skein_mass_ident`, which is exactly "a projection of
a class hypothesis"; and there was no `sorry` in the file.  Three denials,
three matching defects — the sharpest contradiction in this drain, since the
prose rules out the specific thing the code is.

The file also contradicted itself: the declaration docstring says, correctly,
*"body is proved via the class hypothesis"*.  Same shape as
`QOU.BraidsKnots.skein_mass_from_linking`, where the class docstring was
honest and the module docstring above it was not.

## 🛑 The normaliser is the convention-C Markov parameter, in the spelling the audits miss

`1 / (q^{1/2} + q^{-1/2}) = √q / (q + 1) = z_C`.  Verified numerically at the
proton pin: `0.4993203341836945` against AGENTS.md's quoted
`z_C(q₀) = 0.4993203342`, and against `z_D(q₀) = 0.6126880371`.

So this file computes with **convention C**, which the 2026-08-15 owner
ruling excises in favour of `z_D = q³/(q²+1)` — and it does so in the
**sqrt-variable spelling** that AGENTS.md records as invisible to the shape
audits, here inside a *class field type* rather than a `markovZ` definition.
`scripts/lean-markov-convention-audit.py` does not report this file.

**Not migrated here, deliberately.**  AGENTS.md is explicit that the C-frame
results need **re-derivation**, not a `z` substitution — `z_D` dropped into a
C-frame formula is not a valid move.  The formula is kept exactly as the
`.md` states it and is now *labelled* C-frame, which is the scoping AGENTS.md
prescribes for this situation.  Recorded as a finding under bean `qou-z9ws`;
migration is `qou-cds1`'s.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`pair_skein_mass_formula` is a **`Prop`-valued definition over
caller-supplied data**.  A `sorry` would not have been sound either: with
`S_ab` free the identity is refutable
(`not_pair_skein_mass_formula_of_free_data`).

Two consequences are **derived** rather than assumed:

* `two_le_normaliser` — for `q > 0` the normaliser is at least `2`, so it
  never vanishes and the formula is well-defined.  Without this the division
  is silently `x / 0 = 0` at `q = 0`.
* `pair_skein_difference` — the chirality content: exchanging the two species
  gives `𝒮_ab − 𝒮_ba = (q − q⁻¹)(μ_a − μ_b) / (√q + q^{-1/2})`.  The factor
  `q − q⁻¹` is the Skein-relation coefficient, which is what the manuscript's
  own description asserts (the positive crossing weights `a` by `q`, the
  negative weights `b` by `q⁻¹`).  So the antisymmetry is a theorem here, not
  a restatement.

## What is still unencoded

The pair-Skein-mass categorical construction and the Markov-trace
normalisation: nothing here builds the Borromean braid, the colour-exchange
crossings, `𝒮_{ab}` as a categorical object, or the dressed quark masses.
`q`, `μ` and `S_ab` are a real and two functions the caller supplies. The
total-mass claim `m_N = 𝒮_{q₁q₂} + 𝒮_{q₁q₃} + 𝒮_{q₂q₃}` from the `.md` is
also not encoded.

Bean `qou-z9ws`.
-/

namespace QOU.HadronicMass

/-! ### Over a generic ordered field, in the square-root variable

Following the convention-C rule of the transcendental-boundary strangler (bean
`qou-dk7p`): the half-integer powers are carried by a variable `t` with
`q = t²`, so `q^{1/2} + q^{-1/2} = t + t⁻¹` and no square root is taken.  The
`ℝ`-valued statements in `q` (with `Real.sqrt`) are re-proved from these in
`QOU.Transcendental.MassTheory.PairSkeinMassFormulaReal`. -/

/-- The Markov normaliser `t + t⁻¹ = q^{1/2} + q^{-1/2}` with `q = t²`.
Convention C (reciprocal `t/(t²+1) = z_C`). -/
def skeinNormaliserCt {K : Type*} [Field K] (t : K) : K := t + 1 / t

/-- **The normaliser never vanishes**: for `t > 0` it is at least `2`, with
equality exactly at `t = 1` (AM–GM). -/
theorem two_le_normaliserCt {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {t : K} (ht : 0 < t) : 2 ≤ skeinNormaliserCt t := by
  have key : skeinNormaliserCt t - 2 = (t - 1) ^ 2 / t := by
    unfold skeinNormaliserCt
    field_simp
    ring
  have : 0 ≤ skeinNormaliserCt t - 2 := by
    rw [key]
    exact div_nonneg (sq_nonneg _) ht.le
  linarith

/-- The pair Skein mass formula in the square-root variable `t` (`q = t²`):
`𝒮_ab = (t² μ_a + t⁻² μ_b) / (t + t⁻¹)`.  Named, not asserted. -/
def pair_skein_mass_formula_t {K : Type*} [Field K] (t : K) (μ : ℕ → K)
    (S_ab : ℕ → ℕ → K) : Prop :=
  ∀ a b : ℕ, S_ab a b = (t ^ 2 * μ a + (t ^ 2)⁻¹ * μ b) / skeinNormaliserCt t

/-- **Species exchange is antisymmetric with the Skein coefficient**, in `t`:
`𝒮_ab − 𝒮_ba = (q − q⁻¹)(μ_a − μ_b) / (t + t⁻¹)` with `q = t²`. -/
theorem pair_skein_difference_t {K : Type*} [Field K] {t : K} {μ : ℕ → K}
    {S_ab : ℕ → ℕ → K} (h : pair_skein_mass_formula_t t μ S_ab) (a b : ℕ) :
    S_ab a b - S_ab b a
      = (t ^ 2 - (t ^ 2)⁻¹) * (μ a - μ b) / skeinNormaliserCt t := by
  simp only [pair_skein_mass_formula_t] at h
  rw [h a b, h b a]
  ring

/-- **Refutable at free data**: at `t = 1` with zero dressed masses the
right-hand side is `0`, so a pair Skein mass of `1` fails. -/
theorem not_pair_skein_mass_formula_t_of_free_data {K : Type*} [Field K] :
    ¬ pair_skein_mass_formula_t (1 : K) (fun _ => 0) (fun _ _ => 1) := by
  intro h
  have := h 0 0
  simp [skeinNormaliserCt] at this

end QOU.HadronicMass
