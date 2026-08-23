/-
# The seminormal rep on `V_(2,1)`, and why its characters cannot be the ladder phase

Bean `qou-pdix` (child of `qou-cds1`).

`QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum` states the obligation a
derivation of the Q_β ladder phase must discharge: a transfer matrix `M` on the
2-dimensional irrep `V_(2,1)` of `H₃(q)` with

  `M.trace = 2·cos(eigenphase q)`  and  `M.det = 1`.

This file supplies the representation and the two invariants that obstruct it.

`σ₁ = diag(q, −q⁻¹)` on the standard tableaux `[[1,2],[3]]`, `[[1,3],[2]]`.  `σ₂`
is then **forced** by the Hecke relation together with the braid relation; the
solve is in
`computations/qbeta/qbeta_eigenphase_seminormal_exclusion_probe.py` (6/6, exact
ℚ(q)), and its off-diagonal product is exactly `hoefsmitB q ^ 2`, so the corpus
constant is recovered rather than imported.

The obstruction: `det (σ_i^{±1}) = −1`, so a word of length `L` has determinant
`(−1)^L`, and `trace (σ₁σ₂) = −1` **identically in q**.  Every character of this
representation is an integral Laurent polynomial (the square root enters only
through `b·c`, which is rational), whereas `2 cos((z−1)h/2)` is the cosine of a
non-constant algebraic function and so is not algebraic.  The two cannot agree
as functions of `q`.

**Scope.**  This does not derive the phase, and does not exclude an `M` built by
a non-scalar normalisation or lying outside the braid image.  It also says
nothing about numerical coincidence at a single anchor — at `q₀` the nearest
character sits only ≈2.7e-3 away.  Scope-(b) for the *functional identity*,
with the invariant named.  See the probe's docstring for the full scoping.
-/
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

namespace QOU.QBeta.Seminormal

open Matrix

variable {q : ℝ}

/-- `σ₁ = diag(q, −q⁻¹)`: on the two standard tableaux of shape `(2,1)`, the
entries `1` and `2` share a row in the first and a column in the second, giving
the Hecke eigenvalues `q` and `−q⁻¹`. -/
noncomputable def sigma1 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![q, 0; 0, -q⁻¹]

/-- Lower-right seminormal entry, `d₁ = q³/(q²+1)`. -/
noncomputable def d1 (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- Upper-left seminormal entry, `d₂ = −1/(q(q²+1))`. -/
noncomputable def d2 (q : ℝ) : ℝ := -1 / (q * (q ^ 2 + 1))

/-- Hoefsmit off-diagonal coupling, `b = √(q⁴+q²+1)/(q²+1)` — the same constant
as `QOU.BraidKnot.hoefsmitB`, here in its role as the seminormal off-diagonal. -/
noncomputable def bCoupling (q : ℝ) : ℝ :=
  Real.sqrt (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1)

/-- `σ₂` in the symmetric gauge. -/
noncomputable def sigma2 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![d2 q, bCoupling q; bCoupling q, d1 q]

/-- `d₁ + d₂ = h = q − q⁻¹`: the Hecke trace condition. -/
theorem d1_add_d2 (hq : 0 < q) : d1 q + d2 q = q - q⁻¹ := by
  have h1 : q ≠ 0 := ne_of_gt hq
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  unfold d1 d2
  field_simp
  ring

/-- **The off-diagonal square is `d₁d₂ + 1`** — i.e. the determinant condition
`det σ₂ = −1` is what fixes the Hoefsmit coupling. -/
theorem bCoupling_sq (hq : 0 < q) :
    bCoupling q ^ 2 = d1 q * d2 q + 1 := by
  have h1 : q ≠ 0 := ne_of_gt hq
  have h2 : (q ^ 2 + 1) ≠ 0 := by positivity
  have hnn : (0 : ℝ) ≤ q ^ 4 + q ^ 2 + 1 := by positivity
  unfold bCoupling d1 d2
  rw [div_pow, Real.sq_sqrt hnn]
  field_simp
  ring

/-- `det σ₁ = −1`. -/
theorem det_sigma1 (hq : 0 < q) : (sigma1 q).det = -1 := by
  have h1 : q ≠ 0 := ne_of_gt hq
  simp [sigma1, Matrix.det_fin_two_of]
  field_simp

/-- `det σ₂ = −1`.  Both generators are unimodular-up-to-sign, which is the
source of the parity obstruction: a word of length `L` has determinant `(−1)^L`. -/
theorem det_sigma2 (hq : 0 < q) : (sigma2 q).det = -1 := by
  have hb2 : bCoupling q * bCoupling q = d1 q * d2 q + 1 := by
    rw [← sq]; exact bCoupling_sq hq
  simp only [sigma2, Matrix.det_fin_two_of]
  rw [hb2]; ring

/-- The scalar content of the trace identity: `q·d₂ − q⁻¹·d₁ = −1`.  The
`q`-dependence cancels exactly. -/
theorem trace_entries_eq (hq : 0 < q) : q * d2 q + -(q⁻¹ * d1 q) = -1 := by
  have h1 : q ≠ 0 := ne_of_gt hq
  have h2 : (q ^ 2 + 1) ≠ 0 := by positivity
  unfold d1 d2
  field_simp
  ring

/-- The explicit product `σ₁σ₂`. -/
theorem sigma1_mul_sigma2_eq (q : ℝ) :
    sigma1 q * sigma2 q
      = !![q * d2 q, q * bCoupling q; -q⁻¹ * bCoupling q, -q⁻¹ * d1 q] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [sigma1, sigma2, Matrix.mul_apply, Fin.sum_univ_two]

/-- **`trace (σ₁σ₂) = −1`, identically in `q`.**  The `q`-dependence cancels
exactly — this is the sharpest instance of the integrality obstruction, and it
pins the eigenphase of `σ₁σ₂` to the constant `2π/3`, not to `(z−1)h/2`. -/
theorem trace_sigma1_mul_sigma2 (hq : 0 < q) :
    (sigma1 q * sigma2 q).trace = -1 := by
  rw [sigma1_mul_sigma2_eq, Matrix.trace_fin_two_of, neg_mul]
  exact trace_entries_eq hq

/-- `det (σ₁σ₂) = 1`, so `σ₁σ₂` *does* meet the determinant half of
`TransferMatrixSpectrum` — it is the trace half that fails. -/
theorem det_sigma1_mul_sigma2 (hq : 0 < q) :
    (sigma1 q * sigma2 q).det = 1 := by
  rw [Matrix.det_mul, det_sigma1 hq, det_sigma2 hq]
  norm_num

/-- **The obstruction, stated.**  `σ₁σ₂` satisfies `det = 1` and has constant
trace `−1`; so if it were the transfer matrix, `2 cos α = −1` would force
`α = 2π/3` — a constant, with no dependence on `q` and in particular not
`(z−1)h/2`, which is non-constant. -/
theorem sigma1_mul_sigma2_forces_constant_phase (hq : 0 < q) (α : ℝ)
    (hspec : (sigma1 q * sigma2 q).trace = 2 * Real.cos α) :
    Real.cos α = -(1 / 2) := by
  rw [trace_sigma1_mul_sigma2 hq] at hspec
  linarith

end QOU.QBeta.Seminormal
