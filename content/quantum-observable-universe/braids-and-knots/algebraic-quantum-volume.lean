/-!
# QOU.Braiding.AlgebraicQuantumVolume — Algebraic quantum volume Vol_q(K)

The algebraic quantum volume of a braid element β ∈ H_n(q) is the
product of traced volumes Vol_q(β) = ∏ᵢ V̂ᵢ(q) ∈ ℤ[q^{1/2}, q^{-1/2}],
where each V̂ᵢ(q) is the traced volume of generator i built from the
transfer matrix chain.

LaTeX label: `def:algebraic-quantum-volume`

## References

- [manuscript] Ch 3 §18

**Ground ring**: `R_q = ℤ[q, q⁻¹]`
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Braiding

/-- The algebraic quantum volume of a braid element.

    Vol_q(β) = ∏_{i=0}^{n-2} V̂_i(q)

    where V̂_i(q) = z(q) · a_i(q) + b_i(q) is the traced volume
    of generator i, with a_i, b_i the Laurent polynomial entries
    of the transfer matrix chain.

    The volume lives in ℤ[q^{1/2}, q^{-1/2}] — an algebraic object,
    not a real number. -/
-- Ref: [manuscript] Ch 3 §18
structure AlgebraicQuantumVolume where
  /-- Number of generators n in the braid group B_n. -/
  numGenerators : ℕ
  /-- The traced volumes V̂_i(q) for each generator. -/
  tracedVolumes : Fin numGenerators → LaurentPolynomial ℤ
  /-- The product of all traced volumes. -/
  -- Ref: [manuscript] Ch 3 §18
  volume : LaurentPolynomial ℤ := sorry

end QOU.Braiding
