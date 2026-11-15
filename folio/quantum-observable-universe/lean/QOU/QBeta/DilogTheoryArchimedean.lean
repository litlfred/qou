import QOU.QBeta.DilogTheory
import QOU.QBeta.FiveTwoAbelFiveTerm

/-!
# The Rogers instance of `RogersDilogTheory` (archimedean half of `DilogTheory`, split per §7c)

The analysis is exactly Euler reflection (`rogersL_reflection`) and Abel's relation
(`rogersL_fiveTerm`). Everything downstream is `RogersDilogTheory.numerators`.
-/

namespace QOU.QBeta.DilogTheory

open FiveTwoRogersReflection FiveTwoAbelFiveTerm in
/-- **The real instance.** Rogers' `L` on `(0,1)`. The analysis is exactly
`rogersL_reflection` (Euler reflection) and `rogersL_fiveTerm` (Abel). -/
noncomputable def rogers : RogersDilogTheory ℝ where
  L := rogersL
  L1 := Real.pi ^ 2 / 6
  reflection _ h0 h1 := rogersL_reflection h0 h1
  abel _ _ hx0 hx1 hy0 hy1 := rogersL_fiveTerm hx0 hx1 hy0 hy1

/-- `FiveTwoAbelFiveTerm.numerators_of_root` is the `rogers` instance of
`RogersDilogTheory.numerators`. -/
example {x : ℝ} (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hlo : 1 / 2 < x) (hhi : x < 1) :=
  rogers.numerators hx hlo hhi

end QOU.QBeta.DilogTheory
