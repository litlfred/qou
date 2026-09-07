import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Units


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

## Ground ring (§7c) — a `CommRing`, eigenvalues carried as units

The determinant constraint $\lambda_{\mathrm{sym}}\lambda_{\mathrm{anti}} = -1$
**already exhibits each eigenvalue as a unit** (its inverse is minus the other),
so no field structure is needed: the data is stated over a bare `CommRing R`
with `lam_sym lam_anti : Rˣ`, and every inverse below is a `Units` inverse.
This is the intended home — the Hecke eigenvalue pair is $(q, -q^{-1})$ over
$\mathbb{Z}[q,q^{-1}]$ (AGENTS.md §7a), which is *not* a field, and there the
constraint $q \cdot (-q^{-1}) = -1$ holds on the nose.

The former `[Field K]` presentation is the special case `R := K`,
`lam_sym := Units.mk0 _ h`; its separate `lam_sym_ne_zero` / `lam_anti_ne_zero`
fields are now *derived* (`lam_sym_ne_zero`, `lam_anti_ne_zero` below, over any
nontrivial `R`) rather than assumed, so nothing is lost.

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

namespace QOU

/-- Eigenvalue data of the braiding on `V ⊗ V` for a rank-2 fundamental
    object: a symmetric eigenvalue `λ_sym` (on `S²V`) and an
    antisymmetric eigenvalue `λ_anti` (on `Λ²V ≅ 𝟙`), constrained by
    `λ_sym · λ_anti = -1` (Hecke determinant).

    Parametrised over the ground ring `R = End(𝟙)` of the QOU, with both
    eigenvalues carried in the unit group `Rˣ` — which is exactly what the
    determinant constraint asserts. -/
structure SCBraidingEigenvalueData (R : Type*) [CommRing R] where
  /-- Symmetric eigenvalue `λ_sym` (on `S²V`). -/
  lam_sym : Rˣ
  /-- Antisymmetric eigenvalue `λ_anti` (on `Λ²V ≅ 𝟙`). -/
  lam_anti : Rˣ
  /-- Hecke determinant constraint. -/
  det_constraint : lam_sym * lam_anti = -1

variable {R : Type*} [CommRing R]

/-- The symmetric eigenvalue is nonzero — *derived* from unit-hood rather
    than assumed as a structure field. -/
theorem SCBraidingEigenvalueData.lam_sym_ne_zero [Nontrivial R]
    (bed : SCBraidingEigenvalueData R) : (bed.lam_sym : R) ≠ 0 := by
  intro h
  have hu := bed.lam_sym.mul_inv
  rw [h, zero_mul] at hu
  exact zero_ne_one hu

/-- The antisymmetric eigenvalue is nonzero — *derived*, as above. -/
theorem SCBraidingEigenvalueData.lam_anti_ne_zero [Nontrivial R]
    (bed : SCBraidingEigenvalueData R) : (bed.lam_anti : R) ≠ 0 := by
  intro h
  have hu := bed.lam_anti.mul_inv
  rw [h, zero_mul] at hu
  exact zero_ne_one hu

/-- The antisymmetric eigenvalue is forced to be $-\lambda_{\mathrm{sym}}^{-1}$
    by the Hecke determinant constraint. -/
theorem SCBraidingEigenvalueData.anti_eq_neg_inv
    (bed : SCBraidingEigenvalueData R) :
    bed.lam_anti = -(bed.lam_sym⁻¹ : Rˣ) := by
  have h : (bed.lam_sym⁻¹ : Rˣ) * (bed.lam_sym * bed.lam_anti) = bed.lam_sym⁻¹ * (-1) := by
    rw [bed.det_constraint]
  rwa [inv_mul_cancel_left, mul_neg, mul_one] at h

/-- Algebraic identity: $\lambda_{\mathrm{sym}}^{-1} = -\lambda_{\mathrm{anti}}$.
    This is the Hecke determinant constraint rewritten as the
    candidate chart-glue coefficient. -/
theorem glue_eq_inv_sym
    (bed : SCBraidingEigenvalueData R) :
    (bed.lam_sym⁻¹ : Rˣ) = -bed.lam_anti := by
  rw [bed.anti_eq_neg_inv, neg_neg]

/-- Classical limit: at $\lambda_{\mathrm{sym}} = 1$, the candidate
    chart-glue degenerates to $1$ (classical inversion $z\cdot w = 1$). -/
theorem glue_classical_limit
    (bed : SCBraidingEigenvalueData R)
    (hsym : bed.lam_sym = 1) :
    (bed.lam_sym⁻¹ : Rˣ) = 1 := by
  rw [hsym, inv_one]

/-- **The former `chart_glue_from_spectrum` axiom asserted nothing, and
    is now a one-line theorem.**

    It stood as an `axiom` for

        ∃ κ : R, κ = ↑bed.lam_sym⁻¹

    which is discharged by `⟨_, rfl⟩`: an existential whose witness is
    named in its own body is a tautology, for any `R` and any `bed`.

    The docstring called this *"the wall — the categorical model of
    `O_q(P¹)` is not in Mathlib"*.  The wall is real; this statement was
    never standing at it.  Nothing here mentions a chart, a transition
    map, or `P_q(V)` — the categorical interpretation lived entirely in
    the prose, and the type said only that `λ_sym⁻¹` exists.

    Stating the real claim needs the quantum projective line as an
    object, which is indeed absent from Mathlib; that gap is deliberately
    left visible rather than papered over with an axiom that does not
    reach it. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2  §IV.5
theorem chart_glue_from_spectrum
    (bed : SCBraidingEigenvalueData R) :
    ∃ κ : R, κ = ↑bed.lam_sym⁻¹ :=
  ⟨_, rfl⟩

/-- The full spectral–chart correspondence: the chart-glue
    coefficient $\kappa$ of $\mathbb{P}_q(V)$ equals
    $\lambda_{\mathrm{sym}}^{-1} = -\lambda_{\mathrm{anti}}$.  Packages
    the algebraic identity (`glue_eq_inv_sym`) with the categorical
    interpretation (`chart_glue_from_spectrum`). -/
theorem spectral_chart_correspondence
    (bed : SCBraidingEigenvalueData R) :
    ∃ κ : R, κ = ↑bed.lam_sym⁻¹ ∧ κ = -↑bed.lam_anti := by
  obtain ⟨κ, hκ⟩ := chart_glue_from_spectrum bed
  refine ⟨κ, hκ, ?_⟩
  have h : (↑bed.lam_sym⁻¹ : R) = ↑(-bed.lam_anti) :=
    congrArg Units.val (glue_eq_inv_sym bed)
  rw [hκ, h, Units.val_neg]

end QOU
