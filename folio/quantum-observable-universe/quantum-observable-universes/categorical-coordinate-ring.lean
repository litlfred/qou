import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.RingTheory.AdjoinRoot
import Mathlib.RingTheory.Polynomial.Quotient
import Mathlib.Algebra.MonoidAlgebra.Basic


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
- [leitner2026] §sec:braiding-conventions, §rem:affine-chart-origin-of-i-and-q
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
-- Ref: [leitner2026] §sec:braiding-conventions
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
-- Ref: [leitner2026] §sec:braiding-conventions
theorem q_coord_isUnit : IsUnit (q_coord R) := by
  unfold q_coord
  -- The image of a unit under a ring homomorphism is a unit.
  -- T 1 in LaurentPolynomial R is a unit (with inverse T (-1)).
  exact (LaurentPolynomial.isUnit_T 1).map _

/-! ## Part 3: Universal property

Any `R`-algebra `S` with a chosen `q ∈ S^×` and `i ∈ S` with `i^2 = -1`
admits a unique `R`-algebra map `R[i, q^±¹] → S`.  Proved sorry-free in
`categorical_coordinate_ring_universal` below. -/

/-- Universal property of `R[i, q^±¹]`: for any commutative `R`-algebra
    `S` equipped with a unit `qS : S^×` and an element `iS : S` with
    `iS^2 = -1`, there is a unique `R`-algebra homomorphism
    `R[i, q^±¹] → S` sending `q ↦ qS` and `i ↦ iS`.

    The existence direction is the universal property of `AdjoinRoot`
    over `LaurentPolynomial`: build `LaurentR R →ₐ[R] S` sending `T 1 ↦ qS`
    (the monoid-algebra universal property, `AddMonoidAlgebra.lift`), make
    `S` a `LaurentR R`-algebra via it, then `AdjoinRoot.liftHom` with root
    `iS` (using `iS² = -1 ⟹ aeval iS (X²+1) = 0`) and `restrictScalars R`.
    Uniqueness: any such `ψ` agrees with the constructed `φ` because it is
    forced to be `LaurentR R`-linear (two monoid homs from `Multiplicative ℤ`
    agreeing at `T 1 = qS`, `MonoidHom.ext_mint`), and then agrees on the
    root `i_coord = iS` (`AdjoinRoot.algHom_ext`). -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 §IV
theorem categorical_coordinate_ring_universal
    (S : Type*) [CommRing S] [Algebra R S]
    (qS : Sˣ) (iS : S) (hiS : iS^2 = -1) :
    ∃! (φ : CategoricalCoordinateRing R →ₐ[R] S),
        φ (q_coord R) = qS ∧ φ (i_coord R) = iS := by
  -- `LaurentR R →ₐ[R] S` sending `T 1 ↦ qS`.
  let F : Multiplicative ℤ →* S := (Units.coeHom S).comp (zpowersHom Sˣ qS)
  let f₁ : LaurentR R →ₐ[R] S := AddMonoidAlgebra.lift R ℤ S F
  have hf1 : f₁ (T 1) = (qS : S) := by
    show AddMonoidAlgebra.lift R ℤ S F (Finsupp.single 1 1) = (qS : S)
    rw [AddMonoidAlgebra.lift_single, one_smul]
    simp [F, zpowersHom_apply]
  -- Make `S` a `LaurentR R`-algebra via `f₁`, then `AdjoinRoot.liftHom`.
  letI : Algebra (LaurentR R) S := f₁.toRingHom.toAlgebra
  have haeval : (Polynomial.aeval iS) (iPoly R) = 0 := by
    show (Polynomial.aeval iS) (Polynomial.X ^ 2 + 1) = 0
    rw [map_add, map_pow, Polynomial.aeval_X, map_one, hiS]; ring
  have halg : (algebraMap (LaurentR R) S) = f₁.toRingHom := rfl
  let ψlift : AdjoinRoot (iPoly R) →ₐ[LaurentR R] S := AdjoinRoot.liftHom (iPoly R) iS haeval
  let φ : CategoricalCoordinateRing R →ₐ[R] S := ψlift.restrictScalars R
  have hφq : φ (q_coord R) = (qS : S) := by
    show ψlift (algebraMap (LaurentR R) (CategoricalCoordinateRing R) (T 1)) = qS
    rw [AlgHom.commutes]; rw [halg]; exact hf1
  have hφi : φ (i_coord R) = iS := by
    show AdjoinRoot.liftHom (iPoly R) iS haeval (AdjoinRoot.root (iPoly R)) = iS
    exact AdjoinRoot.liftHom_root (f := iPoly R) (hfx := haeval)
  refine ⟨φ, ⟨hφq, hφi⟩, ?_⟩
  rintro ψ ⟨hψq, hψi⟩
  -- `ψ ∘ (algebraMap LaurentR CCR) = f₁`, as `R`-alg homs `LaurentR R → S`.
  have hcomm : ψ.comp (IsScalarTower.toAlgHom R (LaurentR R) (CategoricalCoordinateRing R)) = f₁ := by
    apply AddMonoidAlgebra.algHom_ext'
    apply MonoidHom.ext_mint
    show ψ (algebraMap (LaurentR R) (CategoricalCoordinateRing R) (T 1)) = f₁ (T 1)
    rw [hf1]; exact hψq
  have hcommx : ∀ x : LaurentR R, ψ (algebraMap (LaurentR R) (CategoricalCoordinateRing R) x) = f₁ x :=
    fun x => DFunLike.congr_fun hcomm x
  -- View `ψ` as a `LaurentR R`-algebra hom, then apply `AdjoinRoot.algHom_ext`.
  let ψ' : CategoricalCoordinateRing R →ₐ[LaurentR R] S :=
    { ψ.toRingHom with
      commutes' := fun r => by
        show ψ (algebraMap (LaurentR R) (CategoricalCoordinateRing R) r) = algebraMap (LaurentR R) S r
        rw [halg]; exact hcommx r }
  have hψ'lift : ψ' = ψlift := by
    apply AdjoinRoot.algHom_ext
    have h2 : ψlift (AdjoinRoot.root (iPoly R)) = iS :=
      AdjoinRoot.liftHom_root (f := iPoly R) (hfx := haeval)
    rw [h2]; exact hψi
  apply AlgHom.ext
  intro x
  exact DFunLike.congr_fun hψ'lift x

end

end QOU.QuantumObservableUniverse
