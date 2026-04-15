/-!
# QOU.Braiding.TypedCrossingOperator — Typed crossing operator

The typed crossing operator C(f_i, f_j; σ_k) ∈ H_3(q) assigns a
Hecke algebra element to each pairwise crossing in a Borromean baryon,
depending on the flavors (up or down) of the quarks at positions i, j.

LaTeX label: `def:typed-crossing-operator`

## References

- [manuscript] Ch 3 §16

**Ground ring**: `R_q = ℤ[q, q⁻¹]`
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Braiding

/-- Quark flavor: up (𝔲) or down (𝔡). -/
inductive QuarkFlavor where
  | up : QuarkFlavor
  | down : QuarkFlavor
  deriving DecidableEq, Repr

/-- The typed crossing operator C(f_i, f_j; σ_k) ∈ H_3(q).

    Given two quark flavors and a generator index, produces a
    Hecke algebra element according to:
    - Both up:   σ_k
    - Both down: σ_k − (q − q⁻¹)·𝟏
    - Mixed:     σ_k − ½(q − q⁻¹)·𝟏 -/
-- Ref: [manuscript] Ch 3 §16
structure TypedCrossingOperator where
  /-- Flavor of the first quark. -/
  flavor_i : QuarkFlavor
  /-- Flavor of the second quark. -/
  flavor_j : QuarkFlavor
  /-- Generator index k in the braid group B_3. -/
  generatorIndex : Fin 2
  /-- The resulting Hecke algebra element (abstractly). -/
  -- Ref: [manuscript] Ch 3 §16
  element : LaurentPolynomial ℤ := sorry

end QOU.Braiding
