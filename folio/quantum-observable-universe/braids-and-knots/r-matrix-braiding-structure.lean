import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Braiding.r_matrix_braiding_structure — Yang–Baxter equation and braid operator

The universal R-matrix of U_q(su(2)) satisfies the Yang–Baxter equation
and yields a braid group representation via Ř = P ∘ R.

LaTeX label: `prop:r-matrix-braiding-structure`

## References
- [leitner2026] Ch. 4, §enveloping-algebras
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [drinfeld1985] V. Drinfeld, Hopf algebras and the quantum Yang–Baxter equation, 1985

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.

## What the load-bearing claim is

The md's two load-bearing statements are (i) the Yang–Baxter equation
`R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂` and (ii) that `Ř = P ∘ R` furnishes a braid-
group representation.  Both are **named** below — `YangBaxterHolds`,
`BraidRelationHolds`, and their conjunction `r_matrix_braiding_structure` —
as propositions over caller-supplied data.  Neither is asserted here: the
`.md` attributes both to standard `R`-matrix theory for the universal
`R`-matrix of `U_q(𝔰𝔲(2))`, an object this development never constructs.
See the section note below for what this replaced and why.
-/

namespace QOU.Braiding

noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)
end

/-! ### The two load-bearing claims, NAMED rather than asserted

**Changed 2026-08-31.**  This section used to hold `RMatrixBraidingContext` — a
class carrying the Yang–Baxter equation and the braid relation as its own fields
— together with `r_matrix_braiding_structure` and `braid_rep_from_R_check`,
each of which handed the corresponding field straight back.

The old docstrings were candid about the shape (*"Assumed, not derived here.
The body projects `RMatrixBraidingContext.claim_yang_baxter`"*) and even
identified the risk: *"`comp`, `R12`, `R13`, `R23` are arbitrary context data,
and YBE is false for a general assignment"*.  What was missed is that the data
were **fields of the class**, not parameters, so the instance chose them — and a
commutative model discharges both claims outright.  Measured: `V3 := ℕ`,
`comp := (· * ·)`, `R12 := 2`, `R13 := 3`, `R23 := 5` satisfies
`claim_yang_baxter` by `ring`, and the braid relation forces `Ř₁ = Ř₂` in any
commutative model.  So a `[RMatrixBraidingContext]` binder assumed nothing and
both declarations stated nothing (bean `qou-z9ws`).

The replacement names each claim as a **proposition over caller-supplied data**
and asserts neither.  That is AGENTS.md §1a disposition 3 — the honest form for
a statement this development does not prove.  And it is not a loss: the `.md`
attributes both to standard `R`-matrix theory (*"The underlying `R`-matrix
theory is standard"*), for the universal `R`-matrix of `U_q(𝔰𝔲(2))` — an object
this development never constructs.  Drinfeld and Kassel are cited for where the
facts are established; naming them here as propositions records exactly that,
without a Lean declaration claiming to have proved them.

A caller who has a genuine `R`-matrix takes `YangBaxterHolds …` as an ordinary
hypothesis. -/

/-- **Yang–Baxter equation** `R₁₂ ∘ R₁₃ ∘ R₂₃ = R₂₃ ∘ R₁₃ ∘ R₁₂`, as a
proposition about a caller-supplied triple of `R`-matrix actions. -/
-- Ref: [drinfeld1985] V. Drinfeld, Hopf algebras and the quantum Yang–Baxter equation, 1985
def YangBaxterHolds {V3 : Type} (comp : V3 → V3 → V3) (R12 R13 R23 : V3) : Prop :=
  comp (comp R12 R13) R23 = comp (comp R23 R13) R12

/-- **Braid relation** `Ř₁ Ř₂ Ř₁ = Ř₂ Ř₁ Ř₂` for `Ř = P ∘ R`, as a proposition
about caller-supplied braid operators.  This is what makes `σ_i ↦ Ř_i` extend to
a braid-group representation. -/
-- Ref: [kassel1995] Ch. XIII (Braided categories)
def BraidRelationHolds {V3 : Type} (comp : V3 → V3 → V3) (Rcheck1 Rcheck2 : V3) :
    Prop :=
  comp (comp Rcheck1 Rcheck2) Rcheck1 = comp (comp Rcheck2 Rcheck1) Rcheck2

/-- **The claim of `prop:r-matrix-braiding-structure`**: for the universal
`R`-matrix of `U_q(𝔰𝔲(2))` and its braid operator `Ř = P ∘ R`, the Yang–Baxter
equation and the braid relation both hold.

Stated here as a named proposition over an arbitrary system, **not asserted**.
Establishing it for Drinfeld's `R`-matrix is standard and cited; constructing
that `R`-matrix is not done in this development, so no declaration here claims
it. -/
-- Ref: [drinfeld1985] V. Drinfeld, Hopf algebras and the quantum Yang–Baxter equation, 1985
-- Ref: [kassel1995] Ch. VIII (Quantum SL(2)) + Ch. XIII (Braided categories)
-- Ref: [leitner2026] Ch. 4, §enveloping-algebras
def r_matrix_braiding_structure {V3 : Type} (comp : V3 → V3 → V3)
    (R12 R13 R23 Rcheck1 Rcheck2 : V3) : Prop :=
  YangBaxterHolds comp R12 R13 R23 ∧ BraidRelationHolds comp Rcheck1 Rcheck2

/-- Alias for the braid-relation half, kept because the manuscript refers to the
braid-group representation separately from the Yang–Baxter equation. -/
-- Ref: [kassel1995] Ch. XIII (Braided categories)
def braid_rep_from_R_check {V3 : Type} (comp : V3 → V3 → V3)
    (Rcheck1 Rcheck2 : V3) : Prop :=
  BraidRelationHolds comp Rcheck1 Rcheck2

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
-- Ref: [leitner2026] Ch. 4, §enveloping-algebras
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
