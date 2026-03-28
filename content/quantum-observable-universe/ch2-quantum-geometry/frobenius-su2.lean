/-!
# QOU.Examples.frobenius_su2 — Frobenius relation for SU(2)

The Frobenius relation on O(SU(2)):
- Multiplication: μ(f ⊗ g) = fg (pointwise product)
- Frobenius form: ∫_A = ∫_G (Haar integral)
- Dual comultiplication: Δ_μ(f)(g,h) = ∫_G f(xg) h̄(x) dx
- Frobenius relation: μ ≫ Δ = (Δ ▷ A) ≫ α ≫ (A ◁ μ)

The relation encodes that comultiplication is a bimodule map,
which follows from the convolution structure of the Haar integral.

LaTeX label: `ex:frobenius-su2`

## References

- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [manuscript] §1 Example: Frobenius relation for SU(2)
-/

import Mathlib.Data.Real.Basic

namespace QOU.Examples

/-- **SU(2) Frobenius data**: witnesses that O(SU(2)) satisfies the
    Frobenius relation with the Haar integral as Frobenius form.

    LaTeX: `\label{ex:frobenius-su2}` -/
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
structure SU2FrobeniusData where
  /-- The Haar integral is normalised: ∫_G 1 dμ = 1. -/
  haar_normalised : Prop
  /-- The Haar integral is bi-invariant: ∫ f(gx) dμ = ∫ f(x) dμ. -/
  haar_invariant : Prop
  /-- The Frobenius relation holds: comultiplication is a bimodule map. -/
  frobenius_holds : Prop

/-- The Frobenius data for SU(2). -/
-- Ref: [manuscript] §1
def su2Frobenius : SU2FrobeniusData where
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  haar_normalised := sorry
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  haar_invariant := sorry
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  frobenius_holds := sorry

end QOU.Examples
