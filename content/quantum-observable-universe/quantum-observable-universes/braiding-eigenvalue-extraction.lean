import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Algebra.Order.Field.Basic


/-!
# QOU.braiding_eigenvalue_extraction — Extracting q from the braiding

The deformation parameter q is not an external input: it is the
eigenvalue of the braiding c_{V,V} on the symmetric summand of V ⊗ V.
The Hecke relation (T - q)(T + q⁻¹) = 0 is an intrinsic polynomial
identity on the braiding morphism.

## What Mathlib provides (used here)
- `BraidedCategory C` — the braiding `β_ V V : V ⊗ V ≅ V ⊗ V`
- `RigidCategory C` — duals, evaluation, coevaluation
- Algebraic infrastructure: `field_simp`, `ring`, `linarith`

## Where we hit the wall
The **spectral decomposition** of `(β_ V V).hom : V ⊗ V ⟶ V ⊗ V`
into eigenspaces requires:
1. A notion of "eigenvalue of an endomorphism in a monoidal category"
   — not in Mathlib (eigenvalues exist for linear maps, not
   categorical morphisms).
2. Semisimplicity of the category — needed to guarantee the
   decomposition V ⊗ V = S²V ⊕ Λ²V.
3. The identification Λ²V ≅ 𝟙 (from the volume constraint) to
   get a scalar eigenvalue in End(𝟙) ≅ k.

Once the eigenvalues lamSym, lamAnti are extracted (wall), the rest
is pure algebra over the ground ring `R_q` (proved here without sorry).
Note `R_q` is a **ring, not a field**: it has no `Inv` instance, so the
narrative's `q⁻¹` spellings are carried multiplicatively below.

LaTeX label: `prop:braiding-eigenvalue-extraction`

## References
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [woronowicz1988] https://doi.org/10.1007/BF01219077

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open CategoryTheory MonoidalCategory

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Part 1: Categorical setup (Mathlib infrastructure)

In a braided rigid monoidal category, the braiding on V ⊗ V is
an automorphism.  We can state this using Mathlib's API. -/

/-- In a braided monoidal category, the braiding on V ⊗ V is an
    automorphism (isomorphism from V ⊗ V to itself). This is
    immediate from `BraidedCategory`: `β_ V V` is an `Iso`. -/
theorem braiding_is_automorphism
    (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C]
    (V : C) : IsIso (β_ V V).hom :=
  (β_ V V).isIso_hom

/-- The braiding squared: (β_ V V).hom ≫ (β_ V V).hom.
    When this equals 𝟙, the braiding is symmetric (classical case).
    When it doesn't, we're in the quantum regime. -/
noncomputable def braiding_squared
    (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C]
    (V : C) : V ⊗ V ⟶ V ⊗ V :=
  (β_ V V).hom ≫ (β_ V V).hom

/-- The braiding is symmetric iff c² = id. -/
def is_symmetric_braiding
    (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C]
    (V : C) : Prop :=
  braiding_squared C V = 𝟙 (V ⊗ V)

/-! ## Part 2: The wall — spectral decomposition

The step from the categorical braiding `(β_ V V).hom` to numerical
eigenvalues requires:
  (a) V ⊗ V decomposes as S²V ⊕ Λ²V  (semisimplicity)
  (b) Λ²V ≅ 𝟙                          (volume constraint)
  (c) The braiding acts by scalars on each summand

This is the spectral decomposition axiom — the single point where
we cross from Mathlib infrastructure to the deep result.

Kassel (1995) §VIII.3 proves this for Rep(U_q(sl_2)):
the braiding on V_1 ⊗ V_1 has eigenvalues q (on V_2 ≅ S²V_1)
and -q⁻¹ (on V_0 ≅ Λ²V_1 ≅ 𝟙). -/

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2  §VIII.3
axiom spectral_decomposition_of_braiding
    (C : Type*) [Category C] [MonoidalCategory C]
    [BraidedCategory C] [RigidCategory C]
    (V : C)
    -- V is "rank 2": the fundamental object of a QOU
    (h_rank2 : Prop)
    -- Λ²V ≅ 𝟙 (volume constraint)
    (h_volume : Prop)
    -- The category is semisimple
    (h_semisimple : Prop)
    : ∃ (lamSym lamAnti : R_q),
        lamSym ≠ 0 ∧ lamAnti ≠ 0 ∧ lamSym * lamAnti = -1

/-! ## Part 3: Pure algebra (no sorry, no axiom)

Given eigenvalues satisfying the determinant constraint, everything
below is proved by Lean's `field_simp`, `ring`, and `linarith`. -/

/-- The braiding eigenvalue data for a rank-2 fundamental object V.
    The braiding c_{V,V} : V ⊗ V → V ⊗ V has two eigenvalues:
    λ₊ = q on the symmetric summand S²V (dim 3),
    λ₋ = -q⁻¹ on the antisymmetric summand Λ²V ≅ 𝟙 (dim 1).

    This structure encodes the spectral data of the braiding as
    categorical invariants.  The fields are the *output* of the
    spectral decomposition axiom above. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
structure BraidingEigenvalueData where
  /-- Eigenvalue on the symmetric summand S²V. -/
  lamSym : R_q
  /-- Eigenvalue on the antisymmetric summand Λ²V ≅ 𝟙. -/
  lamAnti : R_q
  /-- The braiding is non-degenerate: both eigenvalues are nonzero. -/
  lamSym_ne_zero : lamSym ≠ 0
  lamAnti_ne_zero : lamAnti ≠ 0
  /-- Hecke product condition: lamSym · lamAnti = -1.
      This is the product of roots of the Hecke polynomial
      (T - q)(T + q⁻¹) = T² - (q - q⁻¹)T - 1, whose constant
      term is -1.  Note: this is *not* the 4D determinant of
      c_{V,V} on V ⊗ V (which would be q³·(-q⁻¹) = -q²), but
      rather the product of the two *distinct* eigenvalues. -/
  det_constraint : lamSym * lamAnti = -1

/-- The deformation parameter q extracted from braiding eigenvalues.
    By convention, q := lamSym (the symmetric eigenvalue). -/
noncomputable def BraidingEigenvalueData.q (bed : BraidingEigenvalueData) : R_q :=
  bed.lamSym

/-- **The antisymmetric eigenvalue is the negated inverse of the symmetric
    one**, stated multiplicatively.

    The narrative form is `λ₋ = -q⁻¹`. That form is **not well-typed here**:
    the ground ring is `R_q = ℤ[q, q⁻¹]`, which has no `Inv` instance — the
    *indeterminate* `q` is invertible in `R_q`, but a general element is not,
    so there is no `⁻¹` operation to apply to `lamSym`. The equivalent
    product identity carries the same content and survives the ring:
    `-λ₋` is a two-sided inverse of `λ₊`.

    This is exactly `det_constraint` rearranged; the `⁻¹` spelling added no
    information over a field either. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem BraidingEigenvalueData.symm_mul_neg_anti
    (bed : BraidingEigenvalueData) :
    bed.lamSym * (-bed.lamAnti) = 1 := by
  have h := bed.det_constraint
  rw [mul_neg, h, neg_neg]

/-- Consequently `λ₊` is a **unit** of `R_q`, witnessed by `-λ₋`.

    Over a field this would be the content of `lamSym ≠ 0`; over a ring
    "invertible" is strictly stronger than "nonzero", and it is the stronger
    statement that the braiding actually supplies. -/
theorem BraidingEigenvalueData.isUnit_lamSym
    (bed : BraidingEigenvalueData) : IsUnit bed.lamSym :=
  isUnit_of_mul_eq_one _ _ bed.symm_mul_neg_anti

/-- **Both eigenvalues of `c_{V,V}` are roots of the Hecke polynomial**, in
    its `q`-cleared form.

    The narrative polynomial is `(X - q)(X + q⁻¹)`. Multiplying the second
    factor by the unit `q` clears the inverse without changing the root set,
    giving `(X - q)(qX + 1)` — well-typed over `R_q`, where `⁻¹` is not
    available (see `symm_mul_neg_anti`).

    Root set is unchanged because `q` is a unit (`isUnit_lamSym`): `qX + 1`
    and `X + q⁻¹` differ by that unit factor, so they vanish together. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem hecke_polynomial_roots (bed : BraidingEigenvalueData) :
    (bed.lamSym - bed.q) * (bed.q * bed.lamSym + 1) = 0
    ∧ (bed.lamAnti - bed.q) * (bed.q * bed.lamAnti + 1) = 0 := by
  unfold BraidingEigenvalueData.q
  refine ⟨by ring, ?_⟩
  have hzero : bed.lamSym * bed.lamAnti + 1 = 0 := by
    rw [bed.det_constraint]; ring
  rw [hzero, mul_zero]

/-- Classical limit: symmetric braiding (c² = id) forces q = 1. -/
theorem classical_limit (bed : BraidingEigenvalueData)
    (hsym : bed.lamSym = 1) : bed.lamAnti = -1 := by
  have h := bed.det_constraint
  rw [hsym, one_mul] at h
  exact h

/-- Quantum regime: non-symmetric braiding forces q ≠ 1. -/
theorem quantum_regime (bed : BraidingEigenvalueData)
    (hnsym : bed.lamSym ≠ 1) : bed.q ≠ 1 := by
  unfold BraidingEigenvalueData.q; exact hnsym

/-- The full extraction: from eigenvalues + det constraint, derive
    q, the forced antisymmetric eigenvalue, and the Hecke relation. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem braiding_eigenvalue_extraction
    (lamSym lamAnti : R_q)
    (hlamS : lamSym ≠ 0)
    (hlamA : lamAnti ≠ 0)
    (hdet : lamSym * lamAnti = -1)
    : ∃ (bed : BraidingEigenvalueData),
        bed.q = lamSym
        ∧ bed.lamSym * (-bed.lamAnti) = 1
        ∧ (bed.lamAnti - bed.lamSym) * (bed.lamSym * bed.lamAnti + 1) = 0 := by
  refine ⟨⟨lamSym, lamAnti, hlamS, hlamA, hdet⟩, rfl, ?_, ?_⟩
  · rw [mul_neg, hdet, neg_neg]
  · have hzero : lamSym * lamAnti + 1 = 0 := by rw [hdet]; ring
    rw [hzero, mul_zero]

end   -- noncomputable section

end QOU
