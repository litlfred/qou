/-
  Classical q-Reeb angle of the figure-eight knot operator.

  RELOCATED (no mathematical change).  `figure_eight_classical_reeb` was declared in
  `folio/quantum-observable-universe/braids-and-knots/figure-eight-reeb-rotation.lean`, a
  chapter-directory `.lean` belonging to a different content block, so the content-block
  resolver found it via neither candidate 1 (the citing block's own sibling) nor candidate 2
  (`<lakeRoot>/<Decl/Path>.lean`).  Moving it to the path matching its namespace makes candidate
  2 resolve.

  The declaration below is verbatim as it stood in the source file — same statement, same proof,
  same `-- Ref:` citations.
-/

import QOU.BraidsAndKnots.unit_modulus_of_det_one_small_trace

namespace QOU.BraidsAndKnots

/-- **Classical q-Reeb angle `θ(1) = 2π/3` (proved).** At `q = 1` the trace is
    `t = −1` with `t² = 1 < 4`, so every eigenvalue `λ` (root of the characteristic
    polynomial `x² + x + 1`) has unit modulus (via
    `unit_modulus_of_det_one_small_trace`) *and* is a primitive cube root of unity
    (`λ³ = 1`, `λ ≠ 1`).  A primitive cube root has argument `±2π/3`, so the
    classical q-Reeb rotation angle is exactly `2π/3` — the amphichiral anchor from
    which the `q`-deformation `θ(q₀) ≈ 117.087°` departs (`Δθ ≈ −2.913°`, the
    derived symmetry-breaking seed of the `c₃` bar-odd `S`). -/
-- Ref: [jones1987] Jones, Hecke algebra representations of braid groups (1987)
-- Ref: [leitner2026] prop:figure-eight-reeb-rotation
theorem figure_eight_classical_reeb (lam : ℂ)
    (hroot : lam ^ 2 + lam + 1 = 0) :
    ‖lam‖ = 1 ∧ lam ^ 3 = 1 ∧ lam ≠ 1 := by
  refine ⟨?_, ?_, ?_⟩
  · -- unit modulus: the existing theorem with real trace `t = −1`, `t² = 1 < 4`
    have ht : ((-1 : ℝ)) ^ 2 < 4 := by norm_num
    have hcast : ((-1 : ℝ) : ℂ) = -1 := by norm_num
    have hr : lam ^ 2 - ((-1 : ℝ) : ℂ) * lam + 1 = 0 := by
      rw [hcast]; linear_combination hroot
    exact unit_modulus_of_det_one_small_trace (-1) ht lam hr
  · -- `λ³ = 1` from `x³ − 1 = (x − 1)(x² + x + 1)`; `sub_eq_zero.mp` closes it
    have key : lam ^ 3 - 1 = (lam - 1) * (lam ^ 2 + lam + 1) := by ring
    rw [hroot, mul_zero] at key
    exact sub_eq_zero.mp key
  · -- `λ ≠ 1`: else `1 + 1 + 1 = 3 = 0`, impossible in characteristic 0
    intro h
    rw [h] at hroot
    norm_num at hroot

end QOU.BraidsAndKnots
