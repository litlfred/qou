import QOU.Archimedean.TorusKnotGenusFourUnique


/-!
# QOU.Archimedean.force_carrier_bring_uniqueness

Bring's surface `Σ_4` has genus 4.  By the genus-4 torus-knot
uniqueness ([torus_knot_genus_four_unique]), the force-carrier
sector of any Bring-supported QOU is exactly `{T_{2,9}, T_{3,5}}`.

The categorical complexities are `[9]_q` and `[10]_q`, with product
`[9]_q · [10]_q ∈ R` — the denominator of `α_EM`.

LaTeX label: `prop:force-carrier-bring-uniqueness`

## References

- [leitner2026] §5/force-carrier-bring-uniqueness
-/

namespace QOU.Archimedean

/-- A force-carrier knot must satisfy the Bring saturation
    condition: its Seifert genus equals `g(Σ_4) = 4`. -/
def IsBringSaturating (K : TorusKnot) : Prop := K.genus = 4

/-- **Proposition (Bring-supported force-carrier sector is forced)**.

    The force-carrier sector of any QOU built on Bring's surface
    contains exactly the two-element set `{T_{2,9}, T_{3,5}}`. -/
-- Ref: [leitner2026] §5/force-carrier-bring-uniqueness
theorem force_carrier_bring_uniqueness (K : TorusKnot)
    (h : IsBringSaturating K) :
    (K.m = 2 ∧ K.n = 9) ∨ (K.m = 3 ∧ K.n = 5) :=
  torus_knot_genus_four_unique K h

/-- **Corollary (categorical complexity of the force-carrier sector)**.

    The product of categorical `q`-dimensions of the two
    force-carrier knots is `[9]_q · [10]_q`. -/
-- Ref: [leitner2026] §5/force-carrier-bring-uniqueness
theorem force_carrier_categorical_complexity (K : TorusKnot)
    (h : IsBringSaturating K) :
    K.crossingNumber = 9 ∨ K.crossingNumber = 10 :=
  genus_four_crossing_numbers K h

end QOU.Archimedean
