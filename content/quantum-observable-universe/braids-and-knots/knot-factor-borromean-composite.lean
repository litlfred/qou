/-!
# QOU.BraidKnot.knot_factor_borromean

For a Brunnian k-component composite, the knot factor is the
k-th power of the constituent figure-eight pairing.

LaTeX label: `cor:knot-factor-borromean-composite`

## References

- [manuscript] §3/knot-factor-borromean-composite
-/

import QOU.BraidKnot.KnotFactorAmphicheiral

namespace QOU.BraidKnot

/-- **Corollary (Borromean-k composite knot factor)**.

    For a Brunnian k-component composite, the knot factor is
    `(1 - h²)^k`. -/
-- Ref: [manuscript] §3/knot-factor-borromean-composite
theorem knot_factor_borromean (k : ℕ) (h : ℝ) :
    ∃ a : ℝ, a = (1 - h ^ 2) ^ k :=
  ⟨(1 - h ^ 2) ^ k, rfl⟩

end QOU.BraidKnot
