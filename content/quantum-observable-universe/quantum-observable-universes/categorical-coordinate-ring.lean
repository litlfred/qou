import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.RingTheory.AdjoinRoot
import Mathlib.RingTheory.Polynomial.Quotient


/-!
# QOU.QuantumObservableUniverse.CategoricalCoordinateRing

The categorical-coordinate ring `R[i, q^±¹]` of the chart-transition
data of the deformation family `(P_q(V))`.

## Statement

The ring is `R[q, q^{-1}][i] / (i^2 + 1)`, equivalently realised as
`AdjoinRoot (X^2 + 1)` over `LaurentPolynomial R`.

It is characterised by the universal property: it is the smallest
`R`-algebra extension `S` such that
  (1) `q ∈ S^×`, and
  (2) the involution-eigenvalue `-1 ∈ End_R(T_p)` admits a square
      root in `S`.

LaTeX label: `prop:categorical-coordinate-ring`

## References
- [manuscript] §sec:braiding-conventions, §rem:affine-chart-origin-of-i-and-q
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 §IV (quantum plane)
-/

open Polynomial LaurentPolynomial

namespace QOU.QuantumObservableUniverse

noncomputable section

variable (R : Type*) [CommRing R]

/-! ## Part 1: The categorical-coordinate ring -/

/-- The ring `R[q, q^{-1}]` of Laurent polynomials in `q` over `R`. -/
abbrev LaurentR : Type _ := LaurentPolynomial R

/-- The polynomial `i^2 + 1` over `R[q, q^{-1}]`. -/
noncomputable def iPoly : Polynomial (LaurentR R) :=
  Polynomial.X^2 + 1

/-- The categorical-coordinate ring `R[i, q^±¹] = R[q, q^{-1}][i]/(i^2+1)`.

    Declared as an `abbrev` so the `CommRing`, `Algebra (LaurentR R) ·`,
    and `Algebra R ·` instances of `AdjoinRoot` transfer transparently. -/
abbrev CategoricalCoordinateRing : Type _ :=
  AdjoinRoot (iPoly R)

/-- The categorical coordinate `i ∈ R[i, q^±¹]`, the categorical
square root of the antisymmetric braiding eigenvalue `λ_- = -1`. -/
noncomputable def i_coord : CategoricalCoordinateRing R :=
  AdjoinRoot.root (iPoly R)

/-- The categorical coordinate `q ∈ R[i, q^±¹]`, the chart-transition
coefficient of `P_q(V)`. -/
noncomputable def q_coord : CategoricalCoordinateRing R :=
  algebraMap (LaurentR R) (CategoricalCoordinateRing R) (T 1)

/-! ## Part 2: Defining properties of `i` and `q`

The key axiomatic facts. The first is `i^2 = -1`; the second is that
`q` is invertible. Both follow from the construction but require some
Mathlib unfolding. -/

/-- The defining identity `i^2 = -1` of the categorical coordinate `i`.
    Follows from `AdjoinRoot.eval_root`. -/
-- Ref: [manuscript] §sec:braiding-conventions
theorem i_coord_sq_eq_neg_one : (i_coord R)^2 = -1 := by
  -- `AdjoinRoot.root` is a root of the defining polynomial `X^2 + 1`,
  -- so `root^2 + 1 = 0`, hence `root^2 = -1`.
  have h : (i_coord R)^2 + 1 = 0 := by
    have hmap := AdjoinRoot.isRoot_root (iPoly R)
    simpa [i_coord, iPoly, Polynomial.IsRoot, AdjoinRoot.aeval_eq,
      map_add, map_pow] using hmap
  linear_combination h

/-- The categorical coordinate `q` is a unit in `R[i, q^±¹]`.
    Witnessed explicitly by `q^{-1}` = image of `T (-1)`. -/
-- Ref: [manuscript] §sec:braiding-conventions
theorem q_coord_isUnit : IsUnit (q_coord R) := by
  unfold q_coord
  -- The image of a unit under a ring homomorphism is a unit.
  -- T 1 in LaurentPolynomial R is a unit (with inverse T (-1)).
  exact (LaurentPolynomial.isUnit_T 1).map _

/-! ## Part 3: Universal property (sketch)

Any `R`-algebra `S` with a chosen `q ∈ S^×` and `i ∈ S` with `i^2 = -1`
admits a unique `R`-algebra map `R[i, q^±¹] → S`. -/

/-- Universal property of `R[i, q^±¹]`: for any commutative `R`-algebra
    `S` equipped with a unit `qS : S^×` and an element `iS : S` with
    `iS^2 = -1`, there is a unique `R`-algebra homomorphism
    `R[i, q^±¹] → S` sending `q ↦ qS` and `i ↦ iS`.

    The existence direction is the universal property of `AdjoinRoot`
    (factoring through `LaurentPolynomial`'s universal property for the
    unit `qS`); uniqueness is generation by `i_coord`, `q_coord`. The
    full Mathlib assembly is deferred. -/
theorem categorical_coordinate_ring_universal
    (S : Type*) [CommRing S] [Algebra R S]
    (qS : Sˣ) (iS : S) (hiS : iS^2 = -1) :
    ∃! (φ : CategoricalCoordinateRing R →ₐ[R] S),
        φ (q_coord R) = qS ∧ φ (i_coord R) = iS := by
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 §IV
  sorry

end

end QOU.QuantumObservableUniverse
