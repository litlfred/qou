import Mathlib.Analysis.SpecialFunctions.Pow.Real

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

open Real

/-- The Markov normaliser `q^{1/2} + q^{-1/2}` of the pair Skein mass.

**Convention C.**  Its reciprocal is `√q/(q+1) = z_C`, not the canonical
`z_D = q³/(q²+1)` — see the module docstring.  Named so the convention is
visible at the use site rather than buried in a division. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/pair-skein-mass-formula.md
noncomputable def skeinNormaliserC (q : ℝ) : ℝ := Real.sqrt q + 1 / Real.sqrt q

/-- **The normaliser never vanishes**: for `q > 0` it is at least `2`, with
equality exactly at `q = 1` (AM–GM on `√q`).

Derived, and load-bearing: Lean's `x / 0 = 0` would otherwise let the pair
Skein mass formula hold vacuously wherever the normaliser vanished. -/
theorem two_le_normaliser {q : ℝ} (hq : 0 < q) : 2 ≤ skeinNormaliserC q := by
  have hs : 0 < Real.sqrt q := Real.sqrt_pos.mpr hq
  have key : skeinNormaliserC q - 2 = (Real.sqrt q - 1) ^ 2 / Real.sqrt q := by
    unfold skeinNormaliserC
    field_simp
    ring
  have : 0 ≤ skeinNormaliserC q - 2 := by
    rw [key]
    exact div_nonneg (sq_nonneg _) (Real.sqrt_nonneg _)
  linarith

/-- **The pair Skein mass formula** ([`lem:pair-skein-mass-formula`]), as a
proposition over caller-supplied data:

    𝒮_{ab}(q) = (q μ_a + q⁻¹ μ_b) / (q^{1/2} + q^{-1/2}).

**Named, not asserted.**  See the module docstring for the convention-C
scoping and for what the identity would need in order to be about the
categorical pair Skein mass rather than about reals. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/pair-skein-mass-formula.md
def pair_skein_mass_formula (q : ℝ) (μ : ℕ → ℝ) (S_ab : ℕ → ℕ → ℝ) : Prop :=
  ∀ a b : ℕ, S_ab a b = (q * μ a + q⁻¹ * μ b) / skeinNormaliserC q

/-- **Species exchange is antisymmetric with the Skein coefficient** —
derived, not assumed.

    𝒮_ab − 𝒮_ba = (q − q⁻¹)(μ_a − μ_b) / (q^{1/2} + q^{-1/2}).

The factor `q − q⁻¹` is the Skein-relation coefficient
(`σ − σ⁻¹ = q − q⁻¹`, AGENTS.md §7a), which is precisely what the
manuscript's description of the crossing weights asserts. Obtaining it as a
theorem is the reason the formula is worth naming. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/pair-skein-mass-formula.md
theorem pair_skein_difference {q : ℝ} {μ : ℕ → ℝ} {S_ab : ℕ → ℕ → ℝ}
    (h : pair_skein_mass_formula q μ S_ab) (a b : ℕ) :
    S_ab a b - S_ab b a
      = (q - q⁻¹) * (μ a - μ b) / skeinNormaliserC q := by
  simp only [pair_skein_mass_formula] at h
  rw [h a b, h b a]
  ring

/-- **The formula is refutable at freely-chosen data**, which is why it is
named rather than carried as a `sorry`.

At `q = 1` with all dressed masses zero the right-hand side is `0`, so a pair
Skein mass of `1` fails. -/
theorem not_pair_skein_mass_formula_of_free_data :
    ¬ pair_skein_mass_formula 1 (fun _ => 0) (fun _ _ => 1) := by
  intro h
  have := h 0 0
  simp [skeinNormaliserC] at this

end QOU.HadronicMass
