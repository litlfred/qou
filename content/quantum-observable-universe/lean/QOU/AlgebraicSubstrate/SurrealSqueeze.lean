import Mathlib.Algebra.Order.Field.Basic

/-!
# QOU.AlgebraicSubstrate.SurrealSqueeze — the squeeze lemma

The common punchline of every millennium-problem remark in the
paper: for every standard real `δ > 0`, the cost `δ² · ε⁻¹` of a
standard-scale deviation strictly exceeds the mass-gap budget `ε³`
in the ordered field `ℝ(ε) ⊂ 𝐍𝐨`.

Informal proof: multiply the claim by `ε > 0` to reduce to
`δ² > ε⁴`, which holds because `δ²` is a strictly positive
standard real and `ε⁴` is a positive infinitesimal.  The formal
version requires `LinearOrderedField` + an archimedean-infinitesimal
hypothesis, both available in `QOU.AppendixSurreals`.

LaTeX label: `lem:surreal-squeeze`.

## References

- [conway1976] Conway, *On Numbers and Games*, §0.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*. DOI:10.1017/CBO9780511629143.
-/

namespace QOU.AlgebraicSubstrate

universe u

/-- **surreal_squeeze**: in any `LinearOrderedField F` equipped with
    a strictly positive element `ε` that is *archimedean-infinitesimal*
    (dominated by every standard-real positive element), for every
    strictly positive standard-real `δ` that exceeds `ε`, the
    inequality `δ² · ε⁻¹ > ε³` holds.

    The archimedean hypothesis is packaged as `ε ≤ δ` together with
    positivity; this encodes "δ is standard-real and ε is infinitesimal"
    without committing to a specific surreal carrier.

    DIAGNOSTIC (false as stated): on the standard reals (e.g. F = ℝ),
    take ε = 2, δ = 3 (both > 0, ε ≤ δ). Then δ²·ε⁻¹ = 9/2 = 4.5 and
    ε³ = 8, so 4.5 > 8 fails. The intended hypothesis is "δ is a
    *standard real* and ε is *archimedean-infinitesimal*", which the
    current `LinearOrderedField` typeclass cannot express. Closing
    requires either:
    1. specialising F to a surreal/Hahn-completion model with explicit
       infinitesimal classification, or
    2. adding an `ε^4 < δ^2` hypothesis (which captures the substantive
       size separation directly).

    Sorry retained with this diagnosis rather than closed-as-stated
    (which would be a false claim).
    Ref: [conway1976] https://doi.org/10.1201/9781439864159
    Ref: [gonshor1986] https://doi.org/10.1017/CBO9780511629143 -/
theorem surreal_squeeze
    {F : Type u} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (ε δ : F) (hε : 0 < ε) (hδ : 0 < δ) (h_inf : ε ≤ δ) :
    δ^2 * ε⁻¹ > ε^3 := by
  -- See docstring: false as stated on standard reals.
  sorry

end QOU.AlgebraicSubstrate
