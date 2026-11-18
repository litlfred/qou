import QOU.Infra.Polylogarithm

/-!
# Im Li_3(ζ_5) = 4π³/125 — Tate-rational, K=5 case

Compiled formalisation of
`prop:bring-trilog-imaginary-tate-rational`.
Sibling docstub at
`braids-and-knots/bring-trilog-imaginary-tate-rational.lean`.

K = 5 specialisation of the cyclotomic Theorem A closed form.
-/

namespace QOU.BraidKnot.BringTrilogImaginaryTateRational

open QOU.Infra.Polylogarithm

/-- Tate-rational value at K = 5: `4 π³ / 125`. -/
noncomputable def imLi3Zeta5Value : ℝ := 4 * Real.pi ^ 3 / 125

/-- **Proposition (`prop:bring-trilog-imaginary-tate-rational`,
    arithmetic core).**
    Theorem A specialised at K = 5: `(K-1)(K-2)π³/(3K³)` at K=5
    reduces to `4·3·π³/(3·125) = 12 π³/375 = 4 π³/125`.  Per
    Copilot review: `field_simp` to clear denominators before
    `ring`. -/
theorem im_li3_zeta5_closed_form :
    imLi3ZetaPredicted 5 = imLi3Zeta5Value := by
  unfold imLi3ZetaPredicted imLi3Zeta5Value
  field_simp
  ring

/-- Subtracting the closed-form value from the predicted value at five cancels to zero (`qou-eggf`). -/
theorem im_li3_zeta5_sub_eq_zero :
    imLi3ZetaPredicted 5 - imLi3Zeta5Value = 0 := by
  rw [im_li3_zeta5_closed_form, sub_self]

end QOU.BraidKnot.BringTrilogImaginaryTateRational
