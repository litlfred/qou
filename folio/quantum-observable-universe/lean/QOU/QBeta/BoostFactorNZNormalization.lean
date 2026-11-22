/-
  The c₃ boost-rapidity enhancement factor `c = √A` and the Neumann–Zagier ½
  potential normalization — the STRUCTURAL identity underlying the clean value
  `A = 2` (`c = √2`).

  CONTEXT (bean qou-iyj5 / PR #4515; audit
  docs/audits/2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md).
  PR #4515 measured, via the EXACT figure-8 complex volume, that the muon bar-odd
  leak needs an effective boost `Re u = c·ln q₀` with `c = √A ≈ 1.4305`, `A ≈ 2.054`,
  because `Im 𝔙₄₁(u) = κ_pot·(Re²u − Im²u)` with the Lean-exact POTENTIAL coefficient
  `κ_pot = √3/4` (`QOU.Knot.FigureEightComplexVolume.cuspModulus`) and `Re u = ln q₀`
  gives only `A = 1`.

  THE STRUCTURAL IDENTITY (this file). The figure-8 cusp SHAPE and the NZ complex-
  volume POTENTIAL coefficient differ by EXACTLY the Neumann–Zagier ½:
        κ_shape = √3/2 = sin(π/3) = Im(e^{iπ/3}),
        κ_pot   = √3/4 = ½·κ_shape        (the ½ = NZ potential normalization),
        κ_shape / κ_pot = 2               (EXACTLY).
  Since `Im 𝔙` is QUADRATIC in `Re u`, an observable carrying the cusp-SHAPE quadratic
  form `κ_shape·(Re u)²` rather than the NZ-POTENTIAL form `κ_pot·(Re u)²` has
        A = κ_shape / κ_pot = 2  (exact),   c = √A = √2,
  with NO free parameter. This REDUCES the opaque `O(1)` factor `c ≈ 1.4305` to a single
  named, binary, falsifiable normalization question: does the bar-odd leak carry the NZ ½?

  ANTI-FIT / ANTI-LAUNDERING (STRICT). This file states the EXACT factor and the
  conditional boost identity ONLY. It does NOT assert that the physical bar-odd leak `S`
  carries `κ_shape` (that is the OPEN sub-obstruction, bean qou-yh67) — asserting it to
  force `A = 2` would be a fit. Nothing here inverts `Q_β`/CODATA; no
  `SDeformedVolumeChannel` instance is produced; the `A = 2` value is the clean CANDIDATE,
  consistent with the amplified readout `2.054` within the (large) precision ceiling
  measured by the companion probe. The theorems below are unconditionally true arithmetic
  facts about the two cusp constants — falsifiable (e.g. `κ_shape/κ_pot` could have been
  any value; it is exactly 2) and content-bearing, not tautologies.

  Base ring: genuinely archimedean (`Real.sqrt`, `Real.sin`) — §7c-correct `ℝ`.

  -- Ref: [leitner2026] docs/audits/2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md
  -- Ref: [leitner2026] conj:binding-qbeta-complex-volume; PR #4515 (qou-iyj5)
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.QBeta.BoostFactorNZNormalization

open scoped Real

/-- The figure-eight cusp **shape** imaginary part `κ_shape = √3/2 = sin(π/3) = Im(e^{iπ/3})`.
    The raw quadratic-form coefficient of the cusp, BEFORE the Neumann–Zagier ½ potential
    normalization. -/
noncomputable def cuspShape : ℝ := Real.sqrt 3 / 2

/-- The Neumann–Zagier complex-volume **potential** coefficient `κ_pot = √3/4 = ½·κ_shape`
    (the same constant as `QOU.Knot.FigureEightComplexVolume.cuspModulus`). The `½` is the
    NZ potential normalization. -/
noncomputable def cuspPotential : ℝ := Real.sqrt 3 / 4

theorem cuspShape_pos : 0 < cuspShape := by unfold cuspShape; positivity
theorem cuspPotential_pos : 0 < cuspPotential := by unfold cuspPotential; positivity

/-- **`κ_shape = sin(π/3)`** — the cusp shape is the standard trig value, tying `√3/2` to the
    hexagonal `ζ₃` geometry `e^{iπ/3}`. -/
theorem cuspShape_eq_sin_pi_div_three : cuspShape = Real.sin (π / 3) := by
  rw [Real.sin_pi_div_three]; rfl

/-- **The Neumann–Zagier ½.** `κ_shape = 2·κ_pot` — the cusp shape is exactly twice the NZ
    potential coefficient. -/
theorem cuspShape_eq_two_mul_pot : cuspShape = 2 * cuspPotential := by
  unfold cuspShape cuspPotential; ring

/-- **The exact amplification factor `A_shape = κ_shape / κ_pot = 2`.** This is the clean
    structural value of the boost enhancement `A`: an observable carrying the cusp-shape
    quadratic form rather than the NZ-potential one is amplified by exactly 2. Falsifiable:
    the ratio could have been any real; it is exactly 2 (the NZ ½). -/
theorem shape_over_pot_eq_two : cuspShape / cuspPotential = 2 := by
  rw [cuspShape_eq_two_mul_pot, mul_div_assoc, div_self (ne_of_gt cuspPotential_pos), mul_one]

/-- **The boost factor is `√2` (the conditional structural identity).** For every real
    deformation magnitude `x`, enhancing the rapidity by `√2` in the NZ-POTENTIAL–normalized
    quadratic form reproduces the cusp-SHAPE–normalized form:
        `κ_pot·(√2·x)² = κ_shape·x²`.
    Equivalently: IF the bar-odd leak carries `κ_shape` (the open sub-obstruction, NOT
    asserted here), THEN the effective boost is `Re u = √2·ln q₀`, i.e. `c = √2`, `A = 2` —
    with no free parameter. Derived from `(√2)² = 2 = κ_shape/κ_pot`, not fitted. -/
theorem boost_factor_sqrt_two (x : ℝ) :
    cuspPotential * (Real.sqrt 2 * x) ^ 2 = cuspShape * x ^ 2 := by
  have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have : (Real.sqrt 2 * x) ^ 2 = 2 * x ^ 2 := by rw [mul_pow, h2]
  rw [this, cuspShape_eq_two_mul_pot]; ring

end QOU.QBeta.BoostFactorNZNormalization
