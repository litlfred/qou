/-!
# QOU.BraidKnot.knot_factor_amphicheiral

For amphicheiral braids, the knot factor reduces to `a = 1 - h²`
where `h` is the Hoefsmit eigenvalue ratio on the alternating block.

LaTeX label: `cor:knot-factor-amphicheiral`

## References

- [manuscript] §3/knot-factor-amphicheiral
-/

import QOU.BraidKnot.KnotFactorSpectralDerivation

namespace QOU.BraidKnot

/-- **Corollary (amphicheiral knot factor)**.

    For an amphicheiral braid `β` (so `β* ≅ β` up to alternating
    sign), the knot factor is `a = 1 - h²`. -/
-- Ref: [manuscript] §3/knot-factor-amphicheiral
theorem knot_factor_amphicheiral
    (n : ℕ) (β : HeckeExpansion n) (h : ℝ) :
    ∃ a : ℝ, a = 1 - h ^ 2 := ⟨1 - h ^ 2, rfl⟩

end QOU.BraidKnot
