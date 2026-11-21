import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle


/-!
# QOU.BriggsKleinChart

Briggs–Klein affine chart: coordinate system (w₁, w₂) on Bring's surface
restricted to 0 < |w₁|² < ∞, with inherited Fubini–Study metric and
C₅-action by phase rotation w_k ↦ ζᵏ w_k.

LaTeX label: `def:briggs-klein-chart`

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Brings

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Briggs–Klein affine chart**: coordinate system on Bring's surface
    using resolvent coordinates (w₁, w₂) ∈ ℂ², restricted to the open
    set where the radial coordinate r = |w₁|² satisfies 0 < r < ∞.

    The C₅ cyclic group acts by phase rotation w_k ↦ ζᵏ w_k, where
    ζ = exp(2πi/5) is a primitive 5th root of unity. The radial
    coordinate r is C₅-invariant.

    Ref: [leitner2026] Chapter 5, §Bundle structures -/
structure BriggsKleinChart where
  /-- First resolvent coordinate w₁ ∈ ℂ. -/
  w₁ : ℂ
  /-- Second resolvent coordinate w₂ ∈ ℂ. -/
  w₂ : ℂ
  /-- Radial coordinate r = |w₁|². -/
  r : ℝ
  /-- r is the squared modulus of w₁. -/
  r_eq : r = Complex.normSq w₁
  /-- The chart is restricted to 0 < r. -/
  r_pos : 0 < r

/-- The C₅ action order: the cyclic group acting by phase rotation. -/
-- Ref: [leitner2026] Chapter 5, §Bundle structures
def c5_order : ℕ := 5

/-- Primitive 5th root of unity phase angle. -/
-- Ref: [leitner2026] Chapter 5, §Bundle structures
noncomputable def zeta_angle : ℝ := 2 * Real.pi / 5

/-- The C₅ phase rotation on the k-th coordinate: ζᵏ · w.
    Since ζ⁵ = 1, the action is periodic with period 5. -/
-- Ref: [leitner2026] Chapter 5, §Bundle structures
noncomputable def c5_phase_rotation (k : ℕ) (w : ℂ) : ℂ :=
  Complex.exp (↑(k * zeta_angle) * Complex.I) * w

/-- The radial coordinate r = |w₁|² is C₅-invariant:
    |ζᵏ w₁|² = |ζᵏ|² · |w₁|² = 1 · |w₁|² = |w₁|².
    Here we express this for the normSq function. -/
-- Ref: [leitner2026] Chapter 5, §Bundle structures
theorem c5_preserves_normSq (k : ℕ) (w : ℂ) :
    Complex.normSq (c5_phase_rotation k w) =
    Complex.normSq w := by
  unfold c5_phase_rotation
  have h : Complex.normSq (Complex.exp (↑(↑k * zeta_angle) * Complex.I)) = 1 := by
    rw [Complex.normSq_eq_norm_sq, Complex.norm_exp_ofReal_mul_I, one_pow]
  rw [Complex.normSq_mul, h, one_mul]

end

end QOU.Brings
