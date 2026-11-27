/-
  Archimedean form of `QOU.MassTheory.pair_skein_mass_formula`, in `q` with
  `Real.sqrt`.  The generic statements over `t = √q` are in the main module;
  this companion keeps the original `ℝ`-valued names.  Same namespace.
-/
import QOU.MassTheory.pair_skein_mass_formula
import Mathlib.Analysis.SpecialFunctions.Pow.Real

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
