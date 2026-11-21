/-
Copyright (c) 2026. All rights reserved.

# The electron word σ₀σ₁σ₀ on the Hecke blocks of H₃

Owner ruling 2026-11-21: the electron is `Δ = σ₀σ₁σ₀ ∈ B₃` (closure: the Hopf link). This file
computes what `Δ` contributes as a lepton strand next to the γγ base, from the Hecke relation
and the defining character values only (`docs/coordination/owner-rulings.md`).

Results (generic `[Field R]` or `[CommRing R]`, `h = q − q⁻¹`):

* `trace_halfTwist`  : on the two-dimensional block `V_(2,1)`, tr Δ = 0.
* `det_halfTwist`    : on that block, det Δ = −1.
* `halfTwist_sq`     : on that block, Δ² = 1. So its eigenvalues are ±1: unit modulus,
  real phase, no cosh lever from `V_(2,1)`.
* `halfTwist_trivial`: on the one-dimensional block `V_(3)` (σ acts as `q`), Δ = q³.
  For `q > 1` this is a real positive eigenvalue ≠ 1 (an imaginary phase `a = 3 ln q`), and
  `cosh_halfTwist_trivial_ge_one` gives `(q³ + q⁻³)/2 ≥ 1`.
* `markov_halfTwist` : for any cyclic functional `t` with the Markov property
  `t(x σ₁) = z t(x)`, `t(σ₀) = z`, `t(1) = 1`, one has `t(Δ) = z (h z + 1)`.
* `markov_halfTwist_zD` : at convention D, `z = q³/(q²+1)`, this is
  `q³ (q⁴+1)/(q²+1)²`.

Which of these numbers (if any) multiplies the scored Q_β cell is NOT decided here: that
needs the rule for how a disjoint lepton strand enters the flavour-split functional. No
empirical input appears in this file.
-/
import QOU.QBeta.PhotonVertexEigenphase

namespace QOU.QBeta.ElectronHalfTwistBlock

open Matrix QOU.QBeta.PhotonVertexEigenphase

variable {R : Type*} [Field R]

/-- The `V_(2,1)` block data, with both Hecke relations and both generator traces. -/
structure HeckeBlock2 (h : R) extends HeckeBlock h where
  hecke0 : S0 * S0 = h • S0 + 1
  tr1 : S1.trace = h

/-- The electron word `Δ = σ₀σ₁σ₀` on the block. -/
def halfTwist {h : R} (B : HeckeBlock2 h) : Matrix (Fin 2) (Fin 2) R :=
  B.S0 * B.S1 * B.S0

theorem trace_halfTwist {h : R} (B : HeckeBlock2 h) : (halfTwist B).trace = 0 := by
  have e : (halfTwist B).trace = (B.S0 * B.S0 * B.S1).trace := by
    rw [halfTwist, Matrix.trace_mul_comm, ← Matrix.mul_assoc]
  rw [e, B.hecke0, Matrix.add_mul, Matrix.smul_mul, Matrix.one_mul, Matrix.trace_add,
    Matrix.trace_smul, B.tr01, B.tr1, smul_eq_mul]
  ring

theorem det_halfTwist {h : R} (B : HeckeBlock2 h) : (halfTwist B).det = -1 := by
  rw [halfTwist, Matrix.det_mul, Matrix.det_mul, B.det0, B.det1]
  ring

/-- Cayley–Hamilton for a 2×2 matrix of trace 0 and determinant −1. -/
theorem sq_of_trace_zero_det_neg_one (M : Matrix (Fin 2) (Fin 2) R) (ht : M.trace = 0)
    (hd : M.det = -1) : M * M = 1 := by
  rw [Matrix.det_fin_two] at hd
  rw [Matrix.trace_fin_two] at ht
  have h11 : M 1 1 = -M 0 0 := by linear_combination ht
  rw [h11] at hd
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, h11] <;>
    first | linear_combination (-1 : R) * hd | ring

theorem halfTwist_sq {h : R} (B : HeckeBlock2 h) : halfTwist B * halfTwist B = 1 :=
  sq_of_trace_zero_det_neg_one _ (trace_halfTwist B) (det_halfTwist B)

/-- On the trivial block σ₀ = σ₁ = q, so Δ = q³. -/
theorem halfTwist_trivial (q : R) : q * q * q = q ^ 3 := by ring

theorem cosh_halfTwist_trivial_ge_one {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {q : K} (hq : 0 < q) : 1 ≤ (q ^ 3 + (q ^ 3)⁻¹) / 2 := by
  have h3 : 0 < q ^ 3 := by positivity
  rw [le_div_iff₀ (by norm_num : (0 : K) < 2)]
  have key : q ^ 3 + (q ^ 3)⁻¹ - 2 = (q ^ 3 - 1) ^ 2 / q ^ 3 := by
    field_simp
    ring
  have : 0 ≤ (q ^ 3 - 1) ^ 2 / q ^ 3 := by positivity
  linarith

/-- The Markov value of the electron word, from cyclicity, the Markov property and the
Hecke relation alone. -/
theorem markov_halfTwist {A : Type*} [Ring A] [Algebra R A] (t : A →ₗ[R] R)
    (cyc : ∀ a b : A, t (a * b) = t (b * a)) (s0 s1 : A) (h z : R)
    (hecke : s0 * s0 = h • s0 + 1) (mark : t (s0 * s0 * s1) = z * t (s0 * s0))
    (t0 : t s0 = z) (t1 : t 1 = 1) :
    t (s0 * s1 * s0) = z * (h * z + 1) := by
  rw [cyc, ← mul_assoc, mark, hecke, map_add, map_smul, t0, t1, smul_eq_mul]

/-- At convention D, `z = q³/(q²+1)`. -/
theorem markov_halfTwist_zD (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    q ^ 3 / (q ^ 2 + 1) * ((q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) + 1)
      = q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  field_simp
  ring

end QOU.QBeta.ElectronHalfTwistBlock
