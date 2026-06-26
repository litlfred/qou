import Mathlib.Tactic

/-!
# QOU.BraidKnot.chirality_frobenius_self_pairing

Canonical Lean for content block
[`prop:chirality-from-frobenius-self-pairing`](../../../quantum-observable-universe/braids-and-knots/chirality-from-frobenius-self-pairing.md).

The `.md` derives the **amphichiral** case of the chirality factor
from the Fricke trace relation in `H_3(R, q)`: the figure-eight
character evaluates to `χ_{4_1}((2,1)) = 2 − [3]_q = −1 − h²`, from
which the chirality factor is `a_{4_1} = 1 − h²` (`h = q − q⁻¹` the
Hecke deformation, `[3]_q = q² + 1 + q⁻²` the balanced quantum
integer).

This file derives those identities **directly** over `ℝ`
(archimedean specialisation per AGENTS.md §7c — the only archimedean
ingredient is `q ≠ 0` for the `q⁻¹` in `[3]_q`).  The previous
encoding axiomatised the conclusion `χ = 1 − h²` as a class field and
projected it (`:= ctx.claim_chirality_factor`); that was a vacuous
self-assuming projection and is removed in favour of the genuine
`field_simp; ring` derivations below.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/chirality-from-frobenius-self-pairing.md
-/

namespace QOU.BraidKnot

/-- The balanced quantum integer `[3]_q = q² + 1 + q⁻²`. -/
noncomputable def qInt3 (q : ℝ) : ℝ := q ^ 2 + 1 + q⁻¹ ^ 2

/-- The Hecke deformation parameter `h = q − q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- **Figure-eight Fricke identity** (manuscript, amphichiral case).

The figure-eight character in the standard `(2,1)` representation of
`H_3(R, q)` is `χ_{4_1}((2,1)) = 2 − [3]_q`, and this equals `−1 − h²`
with `h = q − q⁻¹`.  Derived by clearing the `q⁻¹` denominators and
`ring`. -/
-- Ref: [manuscript] prop:chirality-from-frobenius-self-pairing (Fricke trace relation in H_3)
theorem chirality_figure_eight_character (q : ℝ) (hq : q ≠ 0) :
    2 - qInt3 q = -1 - heckeH q ^ 2 := by
  unfold qInt3 heckeH
  field_simp
  ring

/-- **Amphichiral chirality factor of the figure-eight** as a quantum
integer.

The manuscript's amphichiral chirality factor is `a_{4_1} = 1 − h²`.
Writing it through the balanced quantum integer `[3]_q`, the closed
form is `1 − h² = 4 − [3]_q` (since `[3]_q = q² + 1 + q⁻²` and
`h² = q² − 2 + q⁻²`).  This is the normalisation-free algebraic face
of the chirality factor and is derived by `field_simp; ring`. -/
-- Ref: [manuscript] prop:chirality-from-frobenius-self-pairing (a_{4_1} = 1 − h²)
theorem chirality_amphichiral_via_qInt3 (q : ℝ) (hq : q ≠ 0) :
    1 - heckeH q ^ 2 = 4 - qInt3 q := by
  unfold qInt3 heckeH
  field_simp
  ring

end QOU.BraidKnot
