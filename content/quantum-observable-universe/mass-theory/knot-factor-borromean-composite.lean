import Mathlib.Data.Real.Basic
import QOU.BraidKnot.KnotFactorAmphicheiral


/-!
# QOU.BraidKnot.knot_factor_borromean

For a Brunnian k-component composite, the knot factor is the k-th
power of the constituent figure-eight pairing: `a = (1 - h²)^k`.

LaTeX label: `cor:knot-factor-borromean-composite`

## References

- [manuscript] Ch. Braids and Knots, §Knot factor / Borromean
-/

namespace QOU.BraidKnot

/-- **Brunnian decoupling hypothesis.**

    A `k`-component Brunnian composite has knot factor equal to the
    `k`-fold product of single-component knot factors. -/
structure BrunnianDecoupling (k : ℕ) (component_factor : ℝ)
    (composite_factor : ℝ) : Prop where
  decouples : composite_factor = component_factor ^ k

/-- **Corollary (Borromean-k composite knot factor).**

    A `k`-fold Brunnian composite of amphicheiral components, each
    with knot factor `1 - h²`, has total knot factor `(1 - h²)^k`. -/
-- Ref: [manuscript] Ch. Braids and Knots, §Knot factor / Borromean
theorem knot_factor_borromean (k : ℕ) (h : ℝ)
    (composite : ℝ)
    (decouple : BrunnianDecoupling k (1 - h ^ 2) composite) :
    composite = (1 - h ^ 2) ^ k :=
  decouple.decouples

-- The former `knot_factor_borromean_value : ∃ a : ℝ, a = (1 - h ^ 2) ^ k`
-- was removed: `∃ a, a = e` is provable by `⟨e, rfl⟩` for any `e`, so it
-- asserted nothing about the Borromean composite. `knot_factor_borromean`
-- above already proves the real statement -- `composite = (1 - h²)^k`, and
-- it genuinely consumes the `BrunnianDecoupling` hypothesis.

end QOU.BraidKnot
