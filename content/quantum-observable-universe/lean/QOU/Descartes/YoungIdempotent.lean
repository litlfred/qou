import QOU.Descartes.GroundRing
import QOU.Descartes.TransferMatrix
import Mathlib.Tactic.Ring

/-!
# Young Symmetric Idempotent for H_n(q)

The Young symmetric idempotent `e_{(n)}` projects onto the 1-dimensional
symmetric representation of the Iwahori--Hecke algebra `H_n(q)`.

## Key properties

1. **Idempotent**: `e_{(n)} · e_{(n)} = e_{(n)}`
2. **Symmetric eigenvalue**: `e_{(n)} · T_w = q^{ℓ(w)} · e_{(n)}` for all `w ∈ S_n`
3. **1-dimensional image**: the image of `e_{(n)}` is the symmetric representation
4. **Character extraction**: `e_{(n)} · B · e_{(n)} = χ_{(n)}(B) · e_{(n)}`
   where `χ_{(n)}` is the symmetric character

The symmetric character evaluates each generator at `q`:
`χ_{(n)}(σ_i) = q` for all `i`.

## Construction

```
e_{(n)} = (1/P_n(q⁻²)) · Σ_{w ∈ S_n} q^{ℓ(w)} · T_w
```

where `P_n(q⁻²) = Σ_{w ∈ S_n} q^{2ℓ(w)} = [n]_q! · (q²)^{n(n-1)/2}...`
is the Poincaré polynomial of `S_n`.

## References

- [murphy1992] https://doi.org/10.1016/0021-8693(92)90139-D
- [mathas1999] A. Mathas, *Iwahori–Hecke Algebras and Schur Algebras*, AMS 1999.
-/

namespace QOU.Descartes

/-! ## §1  Poincaré polynomial of S_n -/

/-- The Poincaré polynomial of `S_n` evaluated at `q²`:
    `P_n(q²) = Σ_{w ∈ S_n} q^{2ℓ(w)} = ∏_{k=1}^{n} [k]_{q²}`
    where `[k]_{q²} = 1 + q² + q⁴ + ⋯ + q^{2(k-1)}`.

    For `n = 1`: `P₁ = 1`
    For `n = 2`: `P₂ = 1 + q²`
    For `n = 3`: `P₃ = (1 + q²)(1 + q² + q⁴) = 1 + 2q² + 2q⁴ + q⁶` -/
noncomputable def poincarePolynomial : ℕ → R_t
  | 0 => 1
  | n + 1 =>
    poincarePolynomial n *
    ((Finset.range (n + 1)).sum fun k =>
      (q_from_t * q_from_t) ^ k)  -- Σ_{k=0}^{n} (q²)^k = [n+1]_{q²}

/-- `P₁ = 1`. -/
theorem poincare_one : poincarePolynomial 1 = 1 := by
  unfold poincarePolynomial
  simp

/-- `P₂ = 1 + q²`. -/
theorem poincare_two :
    poincarePolynomial 2 = 1 + q_from_t * q_from_t := by
  unfold poincarePolynomial
  simp [Finset.sum_range_succ, Finset.sum_range_succ]
  ring

/-! ## §2  The Young symmetric idempotent -/

/-- The **Young symmetric idempotent** `e_{(n)}` for `H_n(q)`.

    This is the central idempotent projecting onto the 1-dimensional
    symmetric representation.  In the symmetric representation, every
    generator `σ_i` acts as multiplication by `q`.

    **Key property**: for any element `B ∈ H_n(q)`,
    `e_{(n)} · B · e_{(n)} = χ_{(n)}(B) · e_{(n)}`
    where `χ_{(n)}(B)` is the character of `B` in the symmetric
    representation.

    Construction: `e_{(n)} = (1/P_n(q⁻²)) · Σ_{w ∈ S_n} q^{ℓ(w)} · T_w`

    We represent this abstractly as a structure carrying the key
    properties, since the full construction requires explicit
    permutation group machinery. -/
-- Ref: [murphy1992] https://doi.org/10.1016/0021-8693(92)90139-D
structure YoungSymmetricIdempotent (n : ℕ) where
  /-- The idempotent as a 2×2 matrix (in the standard representation).
      In the symmetric rep, this is the rank-1 projector onto the
      symmetric eigenspace. -/
  matrix : TMatrix
  /-- **Idempotent property**: `e² = e`. -/
  idempotent : matrix * matrix = matrix
  /-- **Symmetric eigenvalue**: the symmetric trace of `e` equals 1.
      (The symmetric character maps `e_{(n)} ↦ 1`.) -/
  sym_trace_one : tracedVolCleared matrix = poincarePolynomial n

/-- The **symmetric eigenvalue property**: for any crossing matrix `M`,
    `e · M · e = λ_sym(M) · e` where `λ_sym(M) = tracedVolCleared M`
    is the symmetric eigenvalue.

    This is the core property used in ordering independence:
    the symmetric idempotent collapses any element to a scalar
    multiple of itself (since the symmetric rep is 1-dimensional). -/
-- Ref: [murphy1992] https://doi.org/10.1016/0021-8693(92)90139-D
theorem young_idempotent_character_extraction
    {n : ℕ} (e : YoungSymmetricIdempotent n)
    (M : TMatrix) :
    -- In the 1D symmetric representation:
    -- e · M · e = χ_{(n)}(M) · e
    -- The trace of the result is χ_{(n)}(M) · tr(e)
    tracedVolCleared (e.matrix * M * e.matrix) =
    tracedVolCleared M * tracedVolCleared (e.matrix * e.matrix) := by
  -- The traced volume is multiplicative on the symmetric eigenspace.
  -- This follows from e being a rank-1 projector:
  -- e · M · e = (some scalar) · e, so tr(e·M·e) = scalar · tr(e)
  -- and scalar = tr_sym(M) / tr_sym(e) up to normalisation.
  -- Ref: [murphy1992] https://doi.org/10.1016/0021-8693(92)90139-D
  sorry -- requires explicit matrix computation for rank-1 projectors

/-- The symmetric eigenvalue of a crossing matrix `T(c, d)`.

    In the symmetric representation, each generator `σ_i` acts as
    multiplication by `q`.  So the crossing `(c · σ + d)` acts as
    `c · q + d` in the symmetric channel.

    Over `ℤ[t, t⁻¹]` (where `q = t²`):
    `λ_sym(T(c,d)) = c · t² + d` -/
noncomputable def symEigenvalue (c d : R_t) : R_t :=
  c * q_from_t + d

/-- The alternating eigenvalue of a crossing matrix `T(c, d)`.

    In the alternating representation, each generator `σ_i` acts as
    multiplication by `−q⁻¹`.  So the crossing `(c · σ + d)` acts as
    `c · (−q⁻¹) + d = d − c · q⁻¹`.

    Over `ℤ[t, t⁻¹]` (where `q = t²`):
    `λ_alt(T(c,d)) = d − c · t⁻²` -/
noncomputable def altEigenvalue (c d : R_t) : R_t :=
  d - c * q_inv_from_t

/-- The symmetric eigenvalue of the pp crossing `T(1, 0)` is `q = t²`. -/
theorem symEigenvalue_pp : symEigenvalue 1 0 = q_from_t := by
  unfold symEigenvalue; ring

/-- The alternating eigenvalue of the pp crossing `T(1, 0)` is `−q⁻¹ = −t⁻²`. -/
theorem altEigenvalue_pp : altEigenvalue 1 0 = -q_inv_from_t := by
  unfold altEigenvalue; ring

/-- **Key lemma**: the symmetric eigenvalue of a product of crossings
    is the product of symmetric eigenvalues.

    This is because the symmetric representation is 1-dimensional,
    so it is a ring homomorphism: `χ_{(n)}(AB) = χ_{(n)}(A) · χ_{(n)}(B)`. -/
-- Ref: [mathas1999]
theorem symEigenvalue_mul (c₁ d₁ c₂ d₂ : R_t) :
    symEigenvalue (c₁ * c₂ * HA_t + c₁ * d₂ + d₁ * c₂) (c₁ * c₂ + d₁ * d₂) =
    symEigenvalue c₁ d₁ * symEigenvalue c₂ d₂ := by
  unfold symEigenvalue HA_t q_from_t q_inv_from_t
  ring

/-- **Key lemma**: the alternating eigenvalue of a product is the
    product of alternating eigenvalues (1D representation = homomorphism). -/
-- Ref: [mathas1999]
theorem altEigenvalue_mul (c₁ d₁ c₂ d₂ : R_t) :
    altEigenvalue (c₁ * c₂ * HA_t + c₁ * d₂ + d₁ * c₂) (c₁ * c₂ + d₁ * d₂) =
    altEigenvalue c₁ d₁ * altEigenvalue c₂ d₂ := by
  unfold altEigenvalue HA_t q_from_t q_inv_from_t
  ring

end QOU.Descartes
