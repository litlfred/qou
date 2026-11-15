/-
# The `M_β` spectrum on `V_(2,1)`, and why no named transfer matrix has one

Bean `qou-pdix` (child of `qou-cds1`), continuing entry (10).

`prop:q-beta-cos-resummation` asserts that "the transfer-matrix `M_β` has
spectrum `{e^{+iα}, e^{−iα}}` on the 2-dimensional irreducible representation
`V_(2,1)` of `H₃(q)`", with `α = (z−1)h/2`.

`QOU.QBeta.Seminormal` already excludes `M = λ·ρ(w)` for a braid word `w`, by a
rationality invariant.  **That exclusion does not reach the matrices the block is
actually conditional on.**  `prop:beta-decay-transfer-matrix` defines four
explicit `2×2` matrices over `ℤ[q^{±1}]`, and two of them are not braid-image
elements at all: `T_mix` is an algebraic average (the block says so) and
`Δ_β` is a scalar multiple of the identity.  This file excludes all four, by a
different and much cheaper invariant — the **determinant**.

`M_β` itself is never defined in the corpus: a six-path corpus-grep finds exactly
two occurrences, both inside the claim.  The only "universal beta decay matrix"
the conditional-on block defines is `Δ_β = (h/2)·I`, whose spectrum is the
**repeated real eigenvalue** `h/2`.  A scalar matrix has no eigenphase.

## What is proved here

* the four matrices, their Hecke relations, and `Δ_β = (h/2)·I`;
* their determinants, all four ≠ 1, **with no hypothesis on `q`** and over a
  generic field;
* that `det = 1` is genuinely necessary for a unit-circle pair, via the
  characteristic discriminant `−4sin²α ≤ 0`;
* `z_D = q³/(q²+1)` **is** the seminormal `σ₂` diagonal entry `d₁`, identically —
  so `z_D + d₂ = h` splits the Hecke differential across the `V_(2,1)` diagonal.
  Convention C does not do this;
* the braid image *does* supply a `q`-dependent eigenphase (`σ₁σ₂⁻¹`), but its
  classical limit is `2π/3` while the ladder phase's is `0`.

**Scope.**  Scope-(b) for the four named matrices, invariant = determinant.  It
does not derive the ladder phase, and does not exclude an `M_β` that no corpus
block defines.

Companion probe: `computations/qbeta/qbeta_mbeta_v21_spectrum_under_d.py` (23/23,
exact ℚ(q) plus mpmath at the proton pin).
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic
import QOU.QBeta.SeminormalV21Trace

namespace QOU.QBeta.MBetaV21

open Matrix

/-! ## §1  The four transfer matrices, over a generic field -/

variable {K : Type*} [Field K]

/-- Hecke differential `h(q) = q − q⁻¹`. -/
def hq (q : K) : K := q - q⁻¹

/-- The crossing transfer matrix `T(c,d) = !![c·h + d, c; c, d]` of
`prop:beta-decay-transfer-matrix`. -/
def betaT (q c d : K) : Matrix (Fin 2) (Fin 2) K := !![c * hq q + d, c; c, d]

/-- `T_pp = T(1, 0)`; represents `σ`. -/
def T_pp (q : K) : Matrix (Fin 2) (Fin 2) K := betaT q 1 0

/-- `T_nn = T(1, −h)`; represents `σ⁻¹`, per the block's uniqueness remark. -/
def T_nn (q : K) : Matrix (Fin 2) (Fin 2) K := betaT q 1 (-hq q)

/-- `T_mix = T(1, −h/2) = ½(σ + σ⁻¹)`: an algebraic average, **not** a group
element. -/
def T_mix (q : K) : Matrix (Fin 2) (Fin 2) K := betaT q 1 (-hq q / 2)

/-- The universal beta decay matrix `Δ_β := T_mix − T_nn`. -/
def Delta_beta (q : K) : Matrix (Fin 2) (Fin 2) K := T_mix q - T_nn q

/-- **`T_pp` satisfies the Hecke relation** `σ² = h·σ + 1`.  So its eigenvalues
are the Hecke eigenvalues `q` and `−q⁻¹`, and it really is the `V_(2,1)` action
of a generator rather than an unrelated `2×2` matrix. -/
theorem T_pp_hecke (q : K) :
    T_pp q * T_pp q = hq q • T_pp q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [T_pp, betaT, Matrix.mul_apply, Fin.sum_univ_two]

/-- **`T_nn` is the inverse of `T_pp`**, so the block's `(1, −h)` convention is
forced exactly as it claims. -/
theorem T_pp_mul_T_nn (q : K) : T_pp q * T_nn q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [T_pp, T_nn, betaT, Matrix.mul_apply, Fin.sum_univ_two]

/-- `T_mix` is the midpoint of the two group elements. -/
theorem T_mix_midpoint (h2 : (2 : K) ≠ 0) (q : K) :
    (2 : K) • T_mix q = T_pp q + T_nn q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [T_pp, T_nn, T_mix, betaT] <;> field_simp <;> ring

/-- **`Δ_β = (h/2)·I`** — the boxed proposition of `prop:beta-decay-transfer-matrix`,
derived from the entries. -/
theorem Delta_beta_eq_scalar (h2 : (2 : K) ≠ 0) (q : K) :
    Delta_beta q = !![hq q / 2, 0; 0, hq q / 2] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Delta_beta, T_mix, T_nn, betaT] <;> field_simp <;> ring

/-- **The universality claim**: the `nn → mix` and `mix → pp` steps give the same
matrix. -/
theorem Delta_beta_universal (h2 : (2 : K) ≠ 0) (q : K) : T_mix q - T_nn q = T_pp q - T_mix q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [T_pp, T_nn, T_mix, betaT] <;> field_simp <;> ring

/-! ## §2  The determinants — no hypothesis on `q`, over any field -/

/-- `det T_pp = −1` (Hecke unimodularity). -/
theorem det_T_pp (q : K) : (T_pp q).det = -1 := by
  simp [T_pp, betaT, Matrix.det_fin_two_of]

/-- `det T_nn = −1`. -/
theorem det_T_nn (q : K) : (T_nn q).det = -1 := by
  simp [T_nn, betaT, Matrix.det_fin_two_of]

/-- `det T_mix = −(1 + h²/4)`.  Strictly below `−1` over an ordered field, so it
is never `1` — `T_mix` is excluded for **every** `q`, not merely at the substrate. -/
theorem det_T_mix (h2 : (2 : K) ≠ 0) (q : K) : (T_mix q).det = -(1 + hq q ^ 2 / 4) := by
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by norm_num
    rw [e]; exact mul_ne_zero h2 h2
  simp only [T_mix, betaT, Matrix.det_fin_two_of]
  field_simp
  ring

/-- `det Δ_β = h²/4`. -/
theorem det_Delta_beta (h2 : (2 : K) ≠ 0) (q : K) : (Delta_beta q).det = hq q ^ 2 / 4 := by
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by norm_num
    rw [e]; exact mul_ne_zero h2 h2
  rw [Delta_beta_eq_scalar h2]
  simp only [Matrix.det_fin_two_of]
  field_simp
  ring

/-! ## §3  `det = 1` is genuinely necessary

A `2×2` matrix has spectrum `{e^{+iα}, e^{−iα}}` exactly when its characteristic
polynomial is `X² − 2cos α · X + 1`.  The predicate below is the one
`QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum` already states; it is
restated here so the exclusions can be phrased against it directly. -/

/-- `M` carries the unit-circle pair `{e^{±iα}}`. -/
def UnitCirclePair (M : Matrix (Fin 2) (Fin 2) ℝ) (α : ℝ) : Prop :=
  M.trace = 2 * Real.cos α ∧ M.det = 1

/-- **Why the pair is genuinely non-real**: the characteristic discriminant of
`X² − 2cos α·X + 1` is `−(2 sin α)² ≤ 0`, so the roots are a conjugate pair on
the unit circle rather than two reals (they coincide exactly when `sin α = 0`). -/
theorem unitCirclePair_discriminant (α : ℝ) :
    (2 * Real.cos α) ^ 2 - 4 * 1 = -(2 * Real.sin α) ^ 2 := by
  have h := Real.sin_sq_add_cos_sq α
  nlinarith [h]

/-- The discriminant is nonpositive. -/
theorem unitCirclePair_discriminant_nonpos (α : ℝ) :
    (2 * Real.cos α) ^ 2 - 4 * 1 ≤ 0 := by
  rw [unitCirclePair_discriminant]; nlinarith [sq_nonneg (2 * Real.sin α)]

/-- A matrix whose determinant is not `1` carries no unit-circle pair, for any
`α` whatsoever. -/
theorem not_unitCirclePair_of_det_ne_one
    {M : Matrix (Fin 2) (Fin 2) ℝ} (hM : M.det ≠ 1) :
    ¬ ∃ α, UnitCirclePair M α := by
  rintro ⟨α, -, hdet⟩; exact hM hdet

/-! ## §4  The four exclusions -/

/-- `T_pp` carries no unit-circle pair. -/
theorem not_unitCirclePair_T_pp (q : ℝ) : ¬ ∃ α, UnitCirclePair (T_pp q) α := by
  refine not_unitCirclePair_of_det_ne_one ?_
  rw [det_T_pp]; norm_num

/-- `T_nn` carries no unit-circle pair. -/
theorem not_unitCirclePair_T_nn (q : ℝ) : ¬ ∃ α, UnitCirclePair (T_nn q) α := by
  refine not_unitCirclePair_of_det_ne_one ?_
  rw [det_T_nn]; norm_num

/-- **`T_mix` carries no unit-circle pair, for any real `q`.**  Its determinant
is `−(1 + h²/4) ≤ −1 < 1`, so the exclusion is uniform in `q` rather than an
accident of the substrate value. -/
theorem not_unitCirclePair_T_mix (q : ℝ) : ¬ ∃ α, UnitCirclePair (T_mix q) α := by
  refine not_unitCirclePair_of_det_ne_one ?_
  rw [det_T_mix two_ne_zero]
  nlinarith [sq_nonneg (hq q)]

/-- **`Δ_β` carries a unit-circle pair only if `h = ±2`.**  Contrapositively: at
any `q` with `h(q)² ≠ 4` — the substrate included, where `h ≈ 0.209` — the only
`M_β` the corpus defines has no eigenphase. -/
theorem not_unitCirclePair_Delta_beta (q : ℝ) (h4 : hq q ^ 2 ≠ 4) :
    ¬ ∃ α, UnitCirclePair (Delta_beta q) α := by
  refine not_unitCirclePair_of_det_ne_one ?_
  rw [det_Delta_beta two_ne_zero]
  intro hcon; exact h4 (by linarith)

/-- **`Δ_β` is scalar, so its spectrum is a repeated real eigenvalue.**  Stated
as: it commutes with every `2×2` matrix — the defining property of a scalar, and
the reason it cannot carry a nontrivial pair of eigenphases. -/
theorem Delta_beta_central (h2 : (2 : K) ≠ 0) (q : K) (M : Matrix (Fin 2) (Fin 2) K) :
    Delta_beta q * M = M * Delta_beta q := by
  rw [Delta_beta_eq_scalar h2]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-! ## §5  `z_D` is the seminormal diagonal entry — convention C is not -/

/-- Convention-D Markov parameter `z_D = q³/(q²+1)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- **`z_D` IS the seminormal `σ₂` diagonal entry `d₁`** — the same rational
function, not a numerical coincidence at one anchor. -/
theorem zD_eq_seminormal_d1 (q : ℝ) : zD q = Seminormal.d1 q := rfl

/-- **Convention D splits the Hecke differential across the `V_(2,1)` diagonal**:
`z_D + d₂ = h`.  The two seminormal diagonal entries of `σ₂` are `z_D` and
`h − z_D`. -/
theorem zD_add_d2_eq_h {q : ℝ} (hq0 : 0 < q) : zD q + Seminormal.d2 q = hq q := by
  rw [zD_eq_seminormal_d1, hq]
  rw [add_comm] at *
  have := Seminormal.d1_add_d2 hq0
  linarith [this]

/-- **Convention C does not have that property.**  At `q = 4`,
`z_C = √4/(4+1) = 2/5` while `d₁ = 64/17`. -/
theorem zC_ne_seminormal_d1_at_four :
    Real.sqrt 4 / (4 + 1) ≠ Seminormal.d1 4 := by
  have h4 : Real.sqrt 4 = 2 := by
    rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  rw [h4, Seminormal.d1]
  norm_num

/-! ## §6  The braid image does supply a `q`-dependent eigenphase — a different one -/

/-- The explicit inverse of `σ₂` (built from `det σ₂ = −1`, so no `Matrix.inv`). -/
noncomputable def sigma2inv (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![-Seminormal.d1 q, Seminormal.bCoupling q;
     Seminormal.bCoupling q, -Seminormal.d2 q]

/-- It really is the inverse. -/
theorem sigma2_mul_sigma2inv {q : ℝ} (hq0 : 0 < q) :
    Seminormal.sigma2 q * sigma2inv q = 1 := by
  have hb : Seminormal.bCoupling q * Seminormal.bCoupling q
      = Seminormal.d1 q * Seminormal.d2 q + 1 := by
    rw [← sq]; exact Seminormal.bCoupling_sq hq0
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Seminormal.sigma2, sigma2inv, Matrix.mul_apply, Fin.sum_univ_two] <;>
    nlinarith [hb]

/-- `det (σ₁σ₂⁻¹) = 1`: an even-length word, so it meets the determinant half. -/
theorem det_sigma1_mul_sigma2inv {q : ℝ} (hq0 : 0 < q) :
    (Seminormal.sigma1 q * sigma2inv q).det = 1 := by
  have h1 : q ≠ 0 := ne_of_gt hq0
  have hb : Seminormal.bCoupling q * Seminormal.bCoupling q
      = Seminormal.d1 q * Seminormal.d2 q + 1 := by
    rw [← sq]; exact Seminormal.bCoupling_sq hq0
  rw [Matrix.det_mul, Seminormal.det_sigma1 hq0]
  simp only [sigma2inv, Matrix.det_fin_two_of]
  nlinarith [hb]

/-- The explicit product `σ₁σ₂⁻¹`, mirroring `Seminormal.sigma1_mul_sigma2_eq`. -/
theorem sigma1_mul_sigma2inv_eq (q : ℝ) :
    Seminormal.sigma1 q * sigma2inv q
      = !![q * -Seminormal.d1 q, q * Seminormal.bCoupling q;
           -q⁻¹ * Seminormal.bCoupling q, -q⁻¹ * -Seminormal.d2 q] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Seminormal.sigma1, sigma2inv, Matrix.mul_apply, Fin.sum_univ_two]

/-- **`trace (σ₁σ₂⁻¹) = −1 − h²`** — a genuinely `q`-dependent character, so the
representation is not short of oscillatory phases.  It is elliptic exactly when
`h² ≤ 1`. -/
theorem trace_sigma1_mul_sigma2inv {q : ℝ} (hq0 : 0 < q) :
    (Seminormal.sigma1 q * sigma2inv q).trace = -1 - hq q ^ 2 := by
  have h1 : q ≠ 0 := ne_of_gt hq0
  have h2 : (q ^ 2 + 1) ≠ 0 := by positivity
  rw [sigma1_mul_sigma2inv_eq, Matrix.trace_fin_two_of,
    Seminormal.d1, Seminormal.d2, hq]
  field_simp
  ring

/-- **The classical limits differ.**  At `q = 1` the elliptic character is `−1`,
so its eigenphase is `2π/3`; the ladder phase `α = (z−1)h/2` vanishes there,
because `h(1) = 0`.  They do not even share a `q → 1` limit. -/
theorem hq_one_eq_zero : hq (1 : ℝ) = 0 := by simp [hq]

/-- The elliptic character at `q = 1` is `−1`, i.e. `2cos α = −1`, `α = 2π/3`. -/
theorem trace_sigma1_mul_sigma2inv_at_one :
    (-1 : ℝ) - hq (1 : ℝ) ^ 2 = -1 := by rw [hq_one_eq_zero]; ring

/-- The ladder phase vanishes at `q = 1` for **any** Markov parameter, `z_C` and
`z_D` alike — it is `h` that vanishes, not `z − 1`. -/
theorem ladder_phase_vanishes_at_one (z : ℝ) :
    (z - 1) * hq (1 : ℝ) / 2 = 0 := by rw [hq_one_eq_zero]; ring

end QOU.QBeta.MBetaV21
