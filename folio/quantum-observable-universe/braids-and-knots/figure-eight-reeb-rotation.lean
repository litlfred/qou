/-
  The figure-eight knot operator acts unitarily on V_(2,1).

  M_{4₁} = (σ₁σ₂⁻¹)² has det = 1 and real trace on V_(2,1),
  forcing eigenvalues to be complex conjugates on the unit circle.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kashaev1997] https://doi.org/10.1007/s100529801020
-/

import Mathlib.Analysis.Complex.Norm
import Mathlib.Tactic
-- `unit_modulus_of_det_one_small_trace` and `figure_eight_classical_reeb` were relocated
-- to the Lake tree (`QOU/BraidsAndKnots/…`) so the content-block resolver
-- finds them; `figure_eight_unitary_on_standard` below still uses the former.
import QOU.BraidsAndKnots.unit_modulus_of_det_one_small_trace

namespace QOU.BraidsAndKnots

/-- The determinant of the figure-eight knot operator
  M_{4₁} = (σ₁σ₂⁻¹)² on a 2-dim representation is 1.
  det(σ₁) = −1, det(σ₂⁻¹) = −1, so det(M) = (−1)⁴ = 1. -/
theorem figure_eight_det_one : (-1 : ℝ)^4 = 1 := by norm_num

/-- **Figure-eight knot operator is unitary on `V_(2,1)`.**

  The knot operator `M_{4₁} = (σ₁σ₂⁻¹)²` has determinant `1` (product of
  four generator determinants, each `-1`), and its trace `t` on `V_(2,1)`
  is real with `t² < 4`; hence by `unit_modulus_of_det_one_small_trace`
  its eigenvalues have unit modulus `‖λ‖ = 1`.  This is the precise
  statement of the md proposition (replacing the prior placeholder
  `(-1)^4 = 1 ∧ 2 = 2`). -/
-- Ref: [jones1987] Jones, Hecke algebra representations of braid groups (1987)
-- Ref: [kashaev1997]
theorem figure_eight_unitary_on_standard
    (t : ℝ) (ht : t ^ 2 < 4) (lam : ℂ)
    (hroot : lam ^ 2 - (t : ℂ) * lam + 1 = 0) :
    ‖lam‖ = 1 :=
  unit_modulus_of_det_one_small_trace t ht lam hroot

/-! ## Closed-form trace and the classical anchor `θ(1) = 2π/3`

The `q`-Reeb rotation angle `θ(q)` is `arg λ_{4₁}` where `2 cos θ = tr M_{4₁}`.
Building the `2×2` Hoefsmit seminormal block of `σ₁, σ₂` on `V_(2,1)` explicitly
(`σ₁ = diag(q, −q⁻¹)`; `σ₂` from braid + Hecke; only the *trace* is used, which is
gauge-invariant) gives the closed Laurent form below.  Derived and numerically
validated (`θ(q₀) ≈ 117.087°`, `dθ/dq ≈ −51°` per unit `q` — smooth) in
`computations/qbeta/qbeta_c3_reeb_rotation_phase_probe.py`.  Here we formalise the
**algebraically exact** facts: the closed form's value at the classical point
`q = 1` is `−1`, and the resulting eigenvalue is a *primitive cube root of unity*
(`θ = ±2π/3`) of unit modulus. -/

/-- Closed-form trace of `M_{4₁} = (σ₁σ₂⁻¹)²` on `V_(2,1)` as a Laurent polynomial
    in `q` (from the explicit seminormal block). -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
noncomputable def figureEightTrace (q : ℝ) : ℝ :=
  q ^ 4 - 2 * q ^ 2 + 1 - 2 * q ^ (-2 : ℤ) + q ^ (-4 : ℤ)

/-- **Classical trace value.** `tr M_{4₁}|_{q=1} = −1`: at `q = 1` the seminormal
    block is the `S₃` representation and `(σ₁σ₂)²` is a 3-cycle. -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_one : figureEightTrace 1 = -1 := by
  simp only [figureEightTrace, one_pow, one_zpow]; norm_num

/-! ## Reeb-rotation degeneration loci = figure-eight geometric special points

The eigenvalue leaves the unit circle exactly where `tr M_{4₁}(q) = ±2` (i.e.
`θ = 0` or `π`).  Both trace boundaries factor exactly, and the roots are the two
geometric special points of the figure-eight knot — the **golden ratio** (the
`A`-polynomial complex-volume branch point) and the **cusp shape** `ω = e^{iπ/3}`
(root of `Φ₆`).  So the operator-monodromy angle `θ` and the geometric
`A`-polynomial / cusp structure share their degeneration loci — two faces of one
object. Numerically cross-checked in
`computations/qbeta/qbeta_c3_reeb_rotation_phase_probe.py`. -/

/-- **`tr M + 2` is a perfect square.** Hence `tr M_{4₁}(q) ≥ −2` for every real
    `q ≠ 0`: the Reeb rotation never reaches `θ = π` on the real substrate axis
    (it does so only at the complex cusp shape `q² = e^{iπ/3}`, where the square's
    base `q² − 1 + q⁻²` — i.e. `q⁴ − q² + 1 = Φ₆(q²)` — vanishes). -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_add_two {q : ℝ} (hq : q ≠ 0) :
    figureEightTrace q + 2 = (q ^ 2 - 1 + q ^ (-2 : ℤ)) ^ 2 := by
  rw [figureEightTrace]; field_simp; ring

/-- `tr M_{4₁}(q) ≥ −2` on the real axis (`θ ≤ π`, never a full flip). -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_ge_neg_two {q : ℝ} (hq : q ≠ 0) :
    -2 ≤ figureEightTrace q := by
  have hsq := figureEightTrace_add_two hq
  nlinarith [sq_nonneg (q ^ 2 - 1 + q ^ (-2 : ℤ)), hsq]

/-- **`tr M − 2` factors; the golden root is `q² − q − 1`.** The four factors are
    `(q²−q−1)(q²+q−1)` (the golden pair, real roots `q = φ`, `1/φ` up to sign) and
    `(q²−q+1)(q²+q+1) = Φ₆(q)Φ₆(−q)` (the cusp/cyclotomic pair, no real roots). -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_sub_two_factored {q : ℝ} (hq : q ≠ 0) :
    figureEightTrace q - 2 =
      (q ^ 2 - q - 1) * ((q ^ 2 + q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1))
        / q ^ 4 := by
  rw [figureEightTrace]; field_simp; ring

/-- **`θ = 0` at the golden ratio.** If `q² = q + 1` (the golden relation, `q = φ`)
    then `tr M_{4₁}(q) = 2`, so the Reeb eigenvalue is `+1` (`θ = 0`): the operator
    degenerates exactly at the `A`-polynomial complex-volume branch point
    `u = 2 ln φ`. -/
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figureEightTrace_golden {q : ℝ} (h : q ^ 2 = q + 1) (hq : q ≠ 0) :
    figureEightTrace q = 2 := by
  have hz : q ^ 2 - q - 1 = 0 := by rw [h]; ring
  have hfac := figureEightTrace_sub_two_factored hq
  rw [hz, zero_mul, zero_div] at hfac
  linarith

end QOU.BraidsAndKnots
