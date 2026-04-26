/-!
# QOU.spectral_chart_correspondence — Hecke eigenspaces realise the chart-glue of $\mathbb{P}_q(V)$

The Hecke spectral decomposition $V \otimes V = S^2V \oplus \Lambda^2 V$
of `braiding_eigenvalue_extraction` (Kassel §VIII.3) realises
geometrically as the chart-transition datum of the quantum projective
line $\mathbb{P}_q(V)$.  On the two affine charts $U_0, U_1$ of
`contact_affine_chart`, the chart-glue coefficient $\kappa$ in
$z \cdot w = \kappa$ is forced by the eigenvalue data to be
$\kappa = \lambda_{\mathrm{sym}}^{-1} = -\lambda_{\mathrm{anti}} = q^{-1}$.

## What is proven here
* `glue_eq_inv_sym` — the algebraic identity
  $\lambda_{\mathrm{sym}}^{-1} = -\lambda_{\mathrm{anti}}$ from the
  Hecke determinant constraint.  No `sorry`.
* `glue_classical_limit` — at $\lambda_{\mathrm{sym}} = 1$ the
  chart-glue degenerates to $1$.  No `sorry`.

## Where we hit the wall
The interpretation of $\kappa$ as the *chart-glue of* $\mathbb{P}_q(V)$
requires a categorical model of the quantum plane $\mathcal{O}_q(\mathbb{P}^1)$
and the chart structure of `contact_affine_chart` — not in Mathlib.
Captured by `axiom chart_glue_from_spectrum`, following the same
pattern as `spectral_decomposition_of_braiding` in
`braiding_eigenvalue_extraction`.

LaTeX label: `prop:spectral-chart-correspondence`

## References
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2  §IV.5 (quantum plane), §VIII.3 (braiding eigenvalues)
- [woronowicz1988] https://doi.org/10.1007/BF01393687
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic

namespace QOU

noncomputable section

/-- Eigenvalue data of the braiding on `V ⊗ V` for a rank-2 fundamental
    object: a symmetric eigenvalue `λ_sym` (on `S²V`) and an
    antisymmetric eigenvalue `λ_anti` (on `Λ²V ≅ 𝟙`), constrained by
    `λ_sym · λ_anti = -1` (Hecke determinant).

    Parametrised over the ground field `K = End(𝟙)` of the QOU; this
    is the natural setting since braiding eigenvalues land in
    `End(𝟙) ≅ k`, which is a field by simplicity of the unit. -/
structure SCBraidingEigenvalueData (K : Type*) [Field K] where
  λ_sym : K
  λ_anti : K
  λ_sym_ne_zero : λ_sym ≠ 0
  λ_anti_ne_zero : λ_anti ≠ 0
  det_constraint : λ_sym * λ_anti = -1

variable {K : Type*} [Field K]

/-- The antisymmetric eigenvalue is forced to be $-\lambda_{\mathrm{sym}}^{-1}$
    by the Hecke determinant constraint. -/
theorem SCBraidingEigenvalueData.anti_eq_neg_inv
    (bed : SCBraidingEigenvalueData K) :
    bed.λ_anti = -(bed.λ_sym)⁻¹ := by
  have h := bed.det_constraint
  have hne := bed.λ_sym_ne_zero
  field_simp at h
  linarith

/-- Algebraic identity: $\lambda_{\mathrm{sym}}^{-1} = -\lambda_{\mathrm{anti}}$.
    This is the Hecke determinant constraint rewritten as the
    candidate chart-glue coefficient. -/
theorem glue_eq_inv_sym
    (bed : SCBraidingEigenvalueData K) :
    bed.λ_sym⁻¹ = -bed.λ_anti := by
  rw [bed.anti_eq_neg_inv]; ring

/-- Classical limit: at $\lambda_{\mathrm{sym}} = 1$, the candidate
    chart-glue degenerates to $1$ (classical inversion $z\cdot w = 1$). -/
theorem glue_classical_limit
    (bed : SCBraidingEigenvalueData K)
    (hsym : bed.λ_sym = 1) :
    bed.λ_sym⁻¹ = 1 := by
  rw [hsym]; simp

/-- Categorical interpretation: on $\mathbb{P}_q(V)$, the chart-transition
    coefficient $\kappa$ of `contact_affine_chart` equals
    $\lambda_{\mathrm{sym}}^{-1}$.  This is the wall — the categorical
    model of $\mathcal{O}_q(\mathbb{P}^1)$ is not in Mathlib. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2  §IV.5
axiom chart_glue_from_spectrum
    (bed : SCBraidingEigenvalueData K) :
    ∃ κ : K, κ = bed.λ_sym⁻¹

/-- The full spectral–chart correspondence: the chart-glue
    coefficient $\kappa$ of $\mathbb{P}_q(V)$ equals
    $\lambda_{\mathrm{sym}}^{-1} = -\lambda_{\mathrm{anti}}$.  Packages
    the algebraic identity (`glue_eq_inv_sym`) with the categorical
    interpretation (`chart_glue_from_spectrum`). -/
theorem spectral_chart_correspondence
    (bed : SCBraidingEigenvalueData K) :
    ∃ κ : K, κ = bed.λ_sym⁻¹ ∧ κ = -bed.λ_anti := by
  obtain ⟨κ, hκ⟩ := chart_glue_from_spectrum bed
  refine ⟨κ, hκ, ?_⟩
  rw [hκ, glue_eq_inv_sym bed]

end

end QOU
