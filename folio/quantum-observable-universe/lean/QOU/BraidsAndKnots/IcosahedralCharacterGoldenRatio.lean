/-
  The golden-ratio fingerprint of the A₅ ↔ icosahedral geometric-angle map.

  Formalises the exact, parameter-free identity that validates the
  SO(3)-restriction assignment of the keystone fibre map `irrepToRotation`
  (`S5SO3FiberAction.lean`): the ℓ=1 (T₁) irrep, evaluated on the 5-fold
  icosahedral rotation (angle 2π/5), has character the golden ratio.

  For the SO(3) spin-ℓ irrep, χ_ℓ(θ) = sin((2ℓ+1)θ/2)/sin(θ/2); at ℓ=1 this is
  χ_1(θ) = 1 + 2cos θ.  On the 5-fold class (θ = 2π/5):

      χ_1(2π/5) = 1 + 2cos(2π/5) = (1 + √5)/2 = φ,

  the exact golden ratio.  This is the closed-form fingerprint behind the
  numerical validation in
  `docs/audits/scripts/keystone_geometric_angles_preflight.py`
  (`|χ − φ| = 0` to machine precision) and pins T₁ as the ℓ=1 restriction with
  no free parameter.

  Built on Mathlib's `Real.cos_pi_div_five`; unconditional, sorry-free.

  -- Ref: [klein1888] Klein, Lectures on the Icosahedron
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.BraidsAndKnots

open Real

/-- **The ℓ=1 icosahedral character on the 5-fold rotation is the golden ratio.**

`χ_{ℓ=1}(2π/5) = 1 + 2cos(2π/5) = (1 + √5)/2`.  The exact, parameter-free
fingerprint validating the `irrepToRotation` angle assignment (T₁ ← ℓ=1). -/
theorem icosahedral_ell1_fivefold_char_eq_golden :
    1 + 2 * Real.cos (2 * π / 5) = (1 + Real.sqrt 5) / 2 := by
  have h2 : (2 : ℝ) * π / 5 = 2 * (π / 5) := by ring
  rw [h2, Real.cos_two_mul, Real.cos_pi_div_five]
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  linear_combination (1 / 4 : ℝ) * h5

end QOU.BraidsAndKnots
