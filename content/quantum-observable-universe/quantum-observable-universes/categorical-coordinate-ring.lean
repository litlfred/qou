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

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.RingTheory.AdjoinRoot
import Mathlib.RingTheory.Polynomial.Quotient

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

/-- The categorical-coordinate ring `R[i, q^±¹] = R[q, q^{-1}][i]/(i^2+1)`. -/
def CategoricalCoordinateRing : Type _ :=
  AdjoinRoot (iPoly R)

instance : CommRing (CategoricalCoordinateRing R) :=
  AdjoinRoot.instCommRing _

instance : Algebra (LaurentR R) (CategoricalCoordinateRing R) :=
  AdjoinRoot.algebra (LaurentR R) (iPoly R)

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
  unfold i_coord iPoly
  -- AdjoinRoot.root is a root of the defining polynomial:
  --   eval₂ (algebraMap _ _) root (X^2 + 1) = 0
  -- so root^2 + 1 = 0, hence root^2 = -1.
  have h : (AdjoinRoot.root (Polynomial.X^2 + 1 : Polynomial (LaurentR R)))^2 + 1 = 0 := by
    have := AdjoinRoot.eval₂_root (Polynomial.X^2 + 1 : Polynomial (LaurentR R))
    simpa [Polynomial.eval₂_add, Polynomial.eval₂_pow, Polynomial.eval₂_X,
            Polynomial.eval₂_one] using this
  linarith_or_polyrith
  where
    -- Fall through if linarith doesn't apply over CommRing
    linarith_or_polyrith : (AdjoinRoot.root (Polynomial.X^2 + 1 : Polynomial (LaurentR R)))^2 = -1 := by
      have : (AdjoinRoot.root (Polynomial.X^2 + 1 : Polynomial (LaurentR R)))^2 + 1 = 0 := by
        have := AdjoinRoot.eval₂_root (Polynomial.X^2 + 1 : Polynomial (LaurentR R))
        simpa using this
      linear_combination this

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
    `R[i, q^±¹] → S` sending `q ↦ qS` and `i ↦ iS`. -/
-- Ref: [manuscript] §sec:braiding-conventions, [kassel1995] §IV
theorem categorical_coordinate_ring_universal
    (S : Type*) [CommRing S] [Algebra R S]
    (qS : Sˣ) (iS : S) (hiS : iS^2 = -1) :
    ∃! (φ : CategoricalCoordinateRing R →ₐ[R] S),
        φ (q_coord R) = qS ∧ φ (i_coord R) = iS := by
  -- Construct φ as the composition of two universal maps:
  --   (a) LaurentPolynomial.lift sending T 1 ↦ qS
  --       (universal property of LaurentPolynomial)
  --   (b) AdjoinRoot.lift extending to R[i, q^±¹] sending root ↦ iS
  --       (universal property of AdjoinRoot, applied since iS^2 + 1 = 0)
  -- Uniqueness from uniqueness of each universal map.
  -- Ref: [manuscript] §sec:braiding-conventions
  sorry

end

end QOU.QuantumObservableUniverse
