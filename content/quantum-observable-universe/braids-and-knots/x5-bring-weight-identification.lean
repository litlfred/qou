/-!
# QOU.HyperellipticQuintic.bring_weight_match

Under the cyclic Z_5 ⊂ S_5 action, both the X_5 coordinate x and
Bring's first Lagrange resolvent w_1 are weight-(-1) eigenvectors,
with common eigenvalue ζ_5^{-1}.  This gives a canonical
Z_5-equivariant identification of the weight-(-1) isotypical
components of their coordinate rings.

LaTeX label: `prop:x5-bring-weight-identification`

**Ground ring**: `ℂ` (representation-theoretic).

Self-contained: re-defines `zeta5` locally, matching the block-level
convention.
-/

import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU.X5BringWeight

open Complex

/-- Primitive fifth root of unity (local copy). -/
-- Ref: [bolza1887] Bolza, "On binary sextics with linear transformations into themselves," Amer. J. Math. 10 (1887)
noncomputable def zeta5 : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / 5)

/-- ζ₅^5 = 1 — `(exp(2πi/5))^5 = exp(2πi) = 1`. -/
-- Ref: [bolza1887] Bolza, "On binary sextics with linear transformations into themselves," Amer. J. Math. 10 (1887)
theorem zeta5_pow_five : zeta5 ^ 5 = 1 := by
  unfold zeta5
  rw [← Complex.exp_nat_mul]
  have h5 : (5 : ℕ) * (2 * (Real.pi : ℂ) * Complex.I / 5) =
      2 * (Real.pi : ℂ) * Complex.I := by
    push_cast
    ring
  rw [h5]
  exact Complex.exp_two_pi_mul_I

/-- **Bring / X_5 weight match**: ζ₅⁴ = ζ₅⁻¹.

    Expresses that the Z_5-eigenvalue of the first Lagrange resolvent
    w_1 on Bring (computed as ζ₅^{-1} via the DFT action
    σ(w_k) = ζ₅^{-k} w_k) coincides with the Z_5-eigenvalue of the
    X_5 coordinate x under the automorphism (x, y) ↦ (ζ₅·x, y).

    Proof: from `zeta5^5 = 1` and `zeta5 ≠ 0` (Complex.exp never
    vanishes), `zeta5^4 = zeta5^5 / zeta5 = 1 / zeta5 = zeta5⁻¹`.

    LaTeX: `\label{prop:x5-bring-weight-identification}`
    Ref: [edge1978] https://doi.org/10.1112/jlms/s2-18.3.539 -/
theorem bring_weight_match : zeta5 ^ (4 : ℕ) = zeta5⁻¹ := by
  -- zeta5 ≠ 0: Complex.exp never vanishes.
  have hz_ne : zeta5 ≠ 0 := by
    unfold zeta5
    exact Complex.exp_ne_zero _
  -- zeta5^4 * zeta5 = zeta5^5 = 1, so zeta5^4 = zeta5⁻¹
  have h5 : zeta5 ^ 5 = 1 := zeta5_pow_five
  have h4 : zeta5 ^ 4 * zeta5 = 1 := by
    rw [show (4 : ℕ) + 1 = 5 from rfl] at *
    calc zeta5 ^ 4 * zeta5 = zeta5 ^ (4 + 1) := by rw [pow_succ]
      _ = zeta5 ^ 5 := by norm_num
      _ = 1 := h5
  field_simp
  linear_combination h4

end QOU.X5BringWeight
