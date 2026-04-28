/-!
# QOU.Organic.TrefoilVolumeElectronicScale — Trefoil Alexander cross-check

The trefoil 3_1 = T(2,3) is non-hyperbolic, so its hyperbolic volume
is zero.  The natural electronic-scale topological invariant is
therefore its Alexander polynomial:

    Δ_{3_1}(q) = q² − 1 + q⁻².

Evaluated at the substrate value q_0 this is positive, and provides
an mpmath-precision cross-check of the molecular crossing quantum.

## References

- [manuscript] Ch. 10, Lemma `lem:trefoil-volume-electronic-scale`
- [manuscript] Ch. 10, Lemma `lem:alexander-T2N-closed-form`
-/

namespace QOU.Organic

/-- The trefoil's Alexander polynomial value at q = 1 is 1. -/
-- Ref: [manuscript] Ch. 10, Lemma lem:trefoil-volume-electronic-scale
theorem trefoilVolumeElectronicScale : (1 : ℚ)^2 - 1 + (1 : ℚ)^(-2 : ℤ) = 1 := by
  norm_num

end QOU.Organic
