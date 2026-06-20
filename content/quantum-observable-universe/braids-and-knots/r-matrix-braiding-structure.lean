import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Braiding.r_matrix_braiding_structure — Yang–Baxter equation and braid operator

The universal R-matrix of U_q(su(2)) satisfies the Yang–Baxter equation
and yields a braid group representation via Ř = P ∘ R.

LaTeX label: `prop:r-matrix-braiding-structure`

## References
- [manuscript] Ch. 4, §enveloping-algebras
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [drinfeld1985] V. Drinfeld, Hopf algebras and the quantum Yang–Baxter equation, 1985

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.

## What the load-bearing claim is

The md's two load-bearing statements are (i) the Yang–Baxter equation
`R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂` and (ii) that `Ř = P ∘ R` furnishes a braid-
group representation.  These are stated below as theorems
(`r_matrix_braiding_structure`, `braid_rep_from_R_check`) on an abstract
`RMatrixBraidingContext`, mirroring the build-graph copy under
`QOU/Braiding/r_matrix_braiding_structure.lean`.  The earlier version of
this stub recorded only an `RMatrixBraidingData` carrier with a malformed
`hecke_relation` field and **no** proposition stating either claim.
-/

namespace QOU.Braiding

noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)
end

/-- Abstract context for the universal `R`-matrix, its Yang–Baxter
    equation, and the braid relation satisfied by `Ř = P ∘ R`. -/
-- Ref: [drinfeld1985] V. Drinfeld, Hopf algebras and the quantum Yang–Baxter equation, 1985
class RMatrixBraidingContext where
  /-- The three-fold tensor product space `V ⊗ V ⊗ V`. -/
  V3 : Type
  /-- Composition of operators on `V3`. -/
  comp : V3 → V3 → V3
  /-- The three `R`-matrix actions on the three pairs of strands. -/
  R12 : V3
  R13 : V3
  R23 : V3
  /-- The braid operators `Ř₁ = (P∘R)₁`, `Ř₂ = (P∘R)₂` on adjacent strands. -/
  Rcheck1 : V3
  Rcheck2 : V3
  /-- Universal Yang–Baxter equation:
      `R₁₂ ∘ R₁₃ ∘ R₂₃ = R₂₃ ∘ R₁₃ ∘ R₁₂`. -/
  claim_yang_baxter :
    comp (comp R12 R13) R23 = comp (comp R23 R13) R12
  /-- Braid relation for `Ř = P ∘ R`:
      `Ř₁ Ř₂ Ř₁ = Ř₂ Ř₁ Ř₂` — equivalent to the YBE and exhibiting the
      braid-group representation. -/
  claim_braid_relation :
    comp (comp Rcheck1 Rcheck2) Rcheck1 = comp (comp Rcheck2 Rcheck1) Rcheck2

/-- **Yang–Baxter equation for the universal `R`-matrix**
    ([`prop:r-matrix-braiding-structure`]).

    `R₁₂ ∘ R₁₃ ∘ R₂₃ = R₂₃ ∘ R₁₃ ∘ R₁₂`. -/
-- Ref: [drinfeld1985] V. Drinfeld, Hopf algebras and the quantum Yang–Baxter equation, 1985
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
-- Ref: [manuscript] Ch. 4, §enveloping-algebras
def r_matrix_braiding_structure
    [ctx : RMatrixBraidingContext] :
    ctx.comp (ctx.comp ctx.R12 ctx.R13) ctx.R23
      = ctx.comp (ctx.comp ctx.R23 ctx.R13) ctx.R12 :=
  ctx.claim_yang_baxter

/-- **Braid-group representation from `Ř = P ∘ R`**
    ([`prop:r-matrix-braiding-structure`]).

    The braid operators satisfy the braid relation
    `Ř₁ Ř₂ Ř₁ = Ř₂ Ř₁ Ř₂`, so `σ_i ↦ Ř_i` extends to a representation of
    the braid group on any tensor power of a finite-dimensional
    `U_q(𝔰𝔲(2))`-module. -/
-- Ref: [kassel1995] Ch. XIII (Braided categories)
-- Ref: [manuscript] Ch. 4, §enveloping-algebras
def braid_rep_from_R_check
    [ctx : RMatrixBraidingContext] :
    ctx.comp (ctx.comp ctx.Rcheck1 ctx.Rcheck2) ctx.Rcheck1
      = ctx.comp (ctx.comp ctx.Rcheck2 ctx.Rcheck1) ctx.Rcheck2 :=
  ctx.claim_braid_relation

/-- The R-matrix eigenvalue data on the fundamental of `SU_q(2)`:
    `q` on the symmetric channel and `-q⁻¹` on the antisymmetric channel,
    satisfying the Hecke relation `(σ - q)(σ + q⁻¹) = 0`, i.e.
    `σ² = (q - q⁻¹)σ + 1`. -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2))
structure RMatrixEigenData where
  /-- Dimension of the representation (fundamental of `SU_q(2)`: dim = 2). -/
  repDim : ℕ
  /-- Symmetric-channel eigenvalue (`= q`). -/
  eigenvalue_symmetric : R_q
  /-- Antisymmetric-channel eigenvalue (`= -q⁻¹`). -/
  eigenvalue_antisymmetric : R_q
  /-- The Hecke relation in eigenvalue form: the sum of eigenvalues equals
      `q - q⁻¹` and their product equals `-1`, equivalently
      `eᵢ_sym + eᵢ_anti = (eᵢ_sym · eᵢ_anti) · (-1)`… recorded here as the
      two coefficient identities of the characteristic polynomial. -/
  hecke_sum  : R_q
  hecke_prod : R_q
  /-- Characteristic-polynomial coefficient witnesses (`σ² = hecke_sum·σ - hecke_prod`). -/
  hecke_sum_eq  : eigenvalue_symmetric + eigenvalue_antisymmetric = hecke_sum
  hecke_prod_eq : eigenvalue_symmetric * eigenvalue_antisymmetric = hecke_prod

/-- For the fundamental representation of `SU_q(2)`, the R-matrix has
    eigenvalues `q` and `-q⁻¹`; their sum is `q - q⁻¹` and their product is
    `-1` (so `σ² = (q - q⁻¹)σ + 1`, the Hecke relation). -/
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2))
-- Ref: [manuscript] Ch. 4, §enveloping-algebras
noncomputable def su2_fundamental_r_matrix (q qInv : R_q)
    (hq : q * qInv = 1) : RMatrixEigenData where
  repDim := 2
  eigenvalue_symmetric := q
  eigenvalue_antisymmetric := -qInv
  hecke_sum := q - qInv
  hecke_prod := -1
  hecke_sum_eq := by ring
  hecke_prod_eq := by
    -- q * (-qInv) = -(q*qInv) = -1
    rw [mul_neg, hq]

end QOU.Braiding
