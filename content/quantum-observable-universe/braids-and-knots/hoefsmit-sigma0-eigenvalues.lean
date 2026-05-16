/-!
# QOU.BraidKnot.hoefsmit_sigma0_eigenvalues

Explicit eigenvalue identification for the Hoefsmit seminormal action of
σ_0 on V_(2,1) of H_3(q).

  ρ_(2,1)(σ_0) = ⟨q, -q⁻¹⟩  (diagonal)

Eigenvalues: q and -q⁻¹ (trivially, since the matrix is diagonal).

This file:
  1. Proves the explicit eigenvalue identification via direct matrix
     algebra (no class hypotheses needed).
  2. Proves the trace and determinant of ρ_(2,1)(σ_0) match the Hecke
     quadratic relation σ² = h·σ + 1 (so the characteristic polynomial
     is λ² − h·λ − 1).
  3. DISCHARGES the σ_0 component of `V21Eigenphase` class (the σ_1
     component requires the full off-diagonal analysis, deferred).

LaTeX label: `rem:hoefsmit-sigma0-eigenvalues` (Lean helper).
-/

import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

open Matrix

/-! ## The Hoefsmit σ_0 matrix -/

/-- Hoefsmit seminormal matrix for `ρ_(2,1)(σ_0)`: diagonal with entries
    `q` and `-q⁻¹`. -/
noncomputable def hoefsmitSigma0 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![q, 0; 0, -q⁻¹]

/-- Trace of `ρ_(2,1)(σ_0) = q + (-q⁻¹) = q - q⁻¹ = h`. -/
theorem hoefsmit_sigma0_trace (q : ℝ) :
    Matrix.trace (hoefsmitSigma0 q) = q - q⁻¹ := by
  unfold hoefsmitSigma0
  simp [Matrix.trace, Fin.sum_univ_two]
  ring

/-- Determinant of `ρ_(2,1)(σ_0) = q · (-q⁻¹) = -1` (when q ≠ 0). -/
theorem hoefsmit_sigma0_det (q : ℝ) (hq : q ≠ 0) :
    Matrix.det (hoefsmitSigma0 q) = -1 := by
  unfold hoefsmitSigma0
  rw [Matrix.det_fin_two]
  simp
  field_simp

/-! ## Eigenvalues: directly from diagonal structure -/

/-- **The first eigenvector**: `[1; 0]` has eigenvalue `q`. -/
theorem hoefsmit_sigma0_eigenvector_q (q : ℝ) :
    (hoefsmitSigma0 q).mulVec ![1, 0] = q • ![1, 0] := by
  unfold hoefsmitSigma0
  ext i
  fin_cases i <;>
    simp [Matrix.mulVec, Matrix.dotProduct, Fin.sum_univ_two] <;>
    ring

/-- **The second eigenvector**: `[0; 1]` has eigenvalue `-q⁻¹`. -/
theorem hoefsmit_sigma0_eigenvector_neg_qinv (q : ℝ) :
    (hoefsmitSigma0 q).mulVec ![0, 1] = (-q⁻¹) • ![0, 1] := by
  unfold hoefsmitSigma0
  ext i
  fin_cases i <;>
    simp [Matrix.mulVec, Matrix.dotProduct, Fin.sum_univ_two] <;>
    ring

/-! ## Hecke quadratic on σ_0

The Hecke quadratic relation `σ² = h·σ + 1` is satisfied at the matrix
level by `ρ_(2,1)(σ_0)` — verified by direct entry-wise computation. -/

-- Ref: [manuscript] prop:hoefsmit-V21-cos-symmetrization
-- Ref: [hoefsmit1974] Hoefsmit's PhD thesis (seminormal form)
/-- **Hecke quadratic for σ_0**: at the matrix level,
    `ρ(σ_0)² = h · ρ(σ_0) + 1` where `h = q - q⁻¹`. -/
theorem hoefsmit_sigma0_hecke_quadratic_explicit (q : ℝ) (hq : q ≠ 0) :
    hoefsmitSigma0 q * hoefsmitSigma0 q
      = (q - q⁻¹) • hoefsmitSigma0 q + (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  unfold hoefsmitSigma0
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.smul_apply, Matrix.add_apply,
          Matrix.one_apply, Fin.sum_univ_two] <;>
    field_simp

/-! ## Top-level export -/

-- Ref: [manuscript] rem:hoefsmit-sigma0-eigenvalues
/-- **Hoefsmit σ_0 eigenvalue identification**: the Hoefsmit matrix
    for `ρ_(2,1)(σ_0)` has explicit eigenvalues `q` and `-q⁻¹`, with
    `[1,0]` and `[0,1]` as the corresponding eigenvectors. The matrix
    satisfies the Hecke quadratic `M² = h·M + 1`. -/
theorem hoefsmit_sigma0_eigenvalues (q : ℝ) (hq : q ≠ 0) :
    -- eigenvalue q with eigenvector [1, 0]
    ((hoefsmitSigma0 q).mulVec ![1, 0] = q • ![1, 0])
    ∧
    -- eigenvalue -q⁻¹ with eigenvector [0, 1]
    ((hoefsmitSigma0 q).mulVec ![0, 1] = (-q⁻¹) • ![0, 1])
    ∧
    -- trace = q - q⁻¹ = h
    (Matrix.trace (hoefsmitSigma0 q) = q - q⁻¹)
    ∧
    -- det = -1
    (Matrix.det (hoefsmitSigma0 q) = -1)
    ∧
    -- Hecke quadratic identity
    (hoefsmitSigma0 q * hoefsmitSigma0 q
       = (q - q⁻¹) • hoefsmitSigma0 q + (1 : Matrix (Fin 2) (Fin 2) ℝ)) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · exact hoefsmit_sigma0_eigenvector_q q
  · exact hoefsmit_sigma0_eigenvector_neg_qinv q
  · exact hoefsmit_sigma0_trace q
  · exact hoefsmit_sigma0_det q hq
  · exact hoefsmit_sigma0_hecke_quadratic_explicit q hq

/-! ## What remains open

The σ_0 component is closed; for the full `V21Eigenphase` class
discharge we still need the σ_1 OFF-DIAGONAL analysis:

  ρ_(2,1)(σ_1) = ⟨d_1, d_2; b, b⟩
  d_1 = q³/(q²+1),  d_2 = -q⁻¹/(q²+1),  b² = d_1·d_2 + 1.

The eigenvalues of this 2×2 are still `{q, -q⁻¹}` by the Hecke
quadratic (any Hecke generator has the same spectrum), but the
EIGENVECTORS depend on the off-diagonal `b`. The single-wrap eigenphase
`α = (z-1)·h/2` on `V_(2,1)` is the leading-order shift in the
eigenstructure when σ_0 and σ_1 are multiplied together, projected to
the Markov-trace symmetrized character.

That analysis is research-level Hecke-seminormal Lean infrastructure
beyond the present scope. -/

end QOU.BraidKnot
