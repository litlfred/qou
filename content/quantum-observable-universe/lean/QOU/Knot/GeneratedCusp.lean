/-
  Machine-generated CUSP equations.  Bean `qou-glhi`.

  `QOU/Knot/GeneratedGluing.lean` covers EDGE equations only, because those have
  non-negative exponents and clear straight to a polynomial identity.  Cusp rows carry
  NEGATIVE exponents — 5₂'s are `[-1,0,0, 0,0,1, 0,0,0]` and `[2,0,-3, 1,0,-2, 0,0,1]` —
  so they are not directly a product of natural powers.

  ═══ HOW THE NEGATIVE EXPONENTS ARE REMOVED ═══

  Not by `zpow`, which would drag `Int` exponents and invertibility through every
  statement.  Instead, **split by sign**.  Every edge parameter is a unit, so

      ∏ paramᵉ = 1     ⟺     ∏_{e>0} paramᵉ  =  ∏_{e<0} param^{−e}

  and both sides now have **natural** exponents.  Clearing denominators on each side
  turns the whole equation into one polynomial identity — exactly the edge case — so the
  same exact-division cofactor works and `zpow` never appears.

  Each cofactor is asserted exact in the generator before emission, so a wrong split
  fails there rather than producing Lean that does not compile.

  ⚠ Cusp equations are the **completeness** condition on the cusp, not the edge
  condition.  Satisfying them says nothing further about whether this is a triangulation
  *of* a knot complement.
-/
import QOU.Knot.GeneratedGluing

namespace QOU.Knot.GeneratedCusp

/-! ### `4_1` cusp equations -/

namespace Cusp41
open QOU.Knot.GeneratedGluing.K41

/-- **Cusp 0** of `4_1`, exponents `[1, 0, 0, 0, 0, -1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t ^ 1) * (z1 t ^ 1) = ((z1 t - 1) ^ 1) * (1) := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  all_goals linear_combination (1) * ht

/-- **Cusp 1** of `4_1`, exponents `[1, 1, 1, 1, -1, -3]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t ^ 1 * (z0 t - 1) ^ 1 * z1 t ^ 1) * ((1 - z1 t) ^ 1 * z1 t ^ 3) = ((z1 t - 1) ^ 3) * ((1 - z0 t) ^ 1 * z0 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  all_goals linear_combination ((-1) * t ^ 5 + 1 * t ^ 4 + 2 * t ^ 3 + (-3) * t ^ 2 + 1 * t) * ht

end Cusp41

/-! ### `5_2` cusp equations -/

namespace Cusp52
open QOU.Knot.GeneratedGluing.K52

/-- **Cusp 0** of `5_2`, exponents `[-1, 0, 0, 0, 0, 1, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 1) * (1) = (z0 t ^ 1) * (z1 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  all_goals linear_combination ((-1)) * ht

/-- **Cusp 1** of `5_2`, exponents `[2, 0, -3, 1, 0, -2, 0, 0, 1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t ^ 2 * z1 t ^ 1 * (z2 t - 1) ^ 1) * (z0 t ^ 3 * z1 t ^ 2) = ((z0 t - 1) ^ 3 * (z1 t - 1) ^ 2) * (z2 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  all_goals linear_combination (1 * t ^ 9 + (-2) * t ^ 8 + 5 * t ^ 7 + (-5) * t ^ 6 + 3 * t ^ 5 + 1 * t ^ 4 + (-4) * t ^ 3 + 2 * t ^ 2 + (-1) * t) * ht

end Cusp52

/-! ### `6_1` cusp equations -/

namespace Cusp61
open QOU.Knot.GeneratedGluing.K61

/-- **Cusp 0** of `6_1`, exponents `[-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 1) * (1) = (z0 t ^ 1) * (z1 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  all_goals linear_combination ((-1)) * ht

/-- **Cusp 1** of `6_1`, exponents `[-1, 1, 0, 0, 1, 1, 0, -1, 0, 0, 0, -2]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 1) * ((1 - z2 t) ^ 1 * z3 t ^ 2) = (z0 t ^ 1 * (z3 t - 1) ^ 2) * ((1 - z0 t) ^ 1 * (1 - z1 t) ^ 1 * z1 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  all_goals linear_combination ((-1 / 4) * t ^ 10 + 2 * t ^ 9 + (-33 / 4) * t ^ 8 + (85 / 4) * t ^ 7 + (-147 / 4) * t ^ 6 + 42 * t ^ 5 + (-57 / 2) * t ^ 4 + (13 / 2) * t ^ 3 + 4 * t ^ 2 + (-2) * t) * ht

end Cusp61

/-! ### `7_2` cusp equations -/

namespace Cusp72
open QOU.Knot.GeneratedGluing.K72

/-- **Cusp 0** of `7_2`, exponents `[0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    (1) * (1) = (z1 t ^ 1) * ((1 - z2 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z1, z2]
  all_goals linear_combination ((1 / 3) * t ^ 3 + (-1 / 3) * t ^ 2 + 1) * ht

/-- **Cusp 1** of `7_2`, exponents `[0, -2, -1, -2, 2, 2, 0, 3, -2, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 2) * ((1 - z0 t) ^ 2 * z0 t ^ 1 * z2 t ^ 2) = ((z0 t - 1) ^ 1 * z1 t ^ 2 * (z2 t - 1) ^ 2) * ((1 - z1 t) ^ 2 * z1 t ^ 2 * (1 - z2 t) ^ 3) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  all_goals linear_combination ((1 / 729) * t ^ 40 + (-16 / 729) * t ^ 39 + (40 / 243) * t ^ 38 + (-530 / 729) * t ^ 37 + (1357 / 729) * t ^ 36 + (-1024 / 729) * t ^ 35 + (-244 / 27) * t ^ 34 + (3257 / 81) * t ^ 33 + (-52801 / 729) * t ^ 32 + (55 / 243) * t ^ 31 + (241912 / 729) * t ^ 30 + (-597691 / 729) * t ^ 29 + (158869 / 243) * t ^ 28 + (1002577 / 729) * t ^ 27 + (-3556637 / 729) * t ^ 26 + (1358695 / 243) * t ^ 25 + (1813511 / 729) * t ^ 24 + (-4371736 / 243) * t ^ 23 + (18029197 / 729) * t ^ 22 + (-1813420 / 729) * t ^ 21 + (-31735418 / 729) * t ^ 20 + (49793935 / 729) * t ^ 19 + (-6010381 / 243) * t ^ 18 + (-16960979 / 243) * t ^ 17 + (90368633 / 729) * t ^ 16 + (-15284593 / 243) * t ^ 15 + (-52236413 / 729) * t ^ 14 + (11970127 / 81) * t ^ 13 + (-7118989 / 81) * t ^ 12 + (-10102630 / 243) * t ^ 11 + (332174 / 3) * t ^ 10 + (-1955504 / 27) * t ^ 9 + (-564749 / 81) * t ^ 8 + (1249663 / 27) * t ^ 7 + (-297700 / 9) * t ^ 6 + (150823 / 27) * t ^ 5 + (22142 / 3) * t ^ 4 + (-19355 / 3) * t ^ 3 + (22504 / 9) * t ^ 2 + (-4580 / 9) * t + (400 / 9)) * ht

end Cusp72

/-! ### `6_2` cusp equations -/

namespace Cusp62
open QOU.Knot.GeneratedGluing.K62

/-- **Cusp 0** of `6_2`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z3 t - 1) ^ 1) * (z4 t ^ 1) = ((z4 t - 1) ^ 1) * (z3 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z3, z4]
  all_goals linear_combination (0) * ht

/-- **Cusp 1** of `6_2`, exponents `[0, -2, 1, 1, 0, -1, 0, 1, 1, 0, 1, -5, 0, -1, 5]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z0 t - 1) ^ 1 * z1 t ^ 1 * (z2 t - 1) ^ 1 * (z4 t - 1) ^ 5) * ((1 - z0 t) ^ 2 * z1 t ^ 1 * z3 t ^ 5 * (1 - z4 t) ^ 1) = ((z1 t - 1) ^ 1 * (z3 t - 1) ^ 5) * (z0 t ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 * (1 - z3 t) ^ 1 * z4 t ^ 5) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination ((-1) * t ^ 49 + 37 * t ^ 48 + (-690) * t ^ 47 + 8623 * t ^ 46 + (-81062) * t ^ 45 + 610322 * t ^ 44 + (-3827670) * t ^ 43 + 20539271 * t ^ 42 + (-96146687) * t ^ 41 + 398415620 * t ^ 40 + (-1478203630) * t ^ 39 + 4955245471 * t ^ 38 + (-15118974121) * t ^ 37 + 42240790366 * t ^ 36 + (-108611867556) * t ^ 35 + 258099040537 * t ^ 34 + (-568850549978) * t ^ 33 + 1166301084869 * t ^ 32 + (-2230067755770) * t ^ 31 + 3985097714438 * t ^ 30 + (-6667122011252) * t ^ 29 + 10457899826377 * t ^ 28 + (-15397896246678) * t ^ 27 + 21299974039609 * t ^ 26 + (-27700028662747) * t ^ 25 + 33880118614809 * t ^ 24 + (-38981024529262) * t ^ 23 + 42187692353584 * t ^ 22 + (-42936051566836) * t ^ 21 + 41071197959657 * t ^ 20 + (-36897450115476) * t ^ 19 + 31098901220947 * t ^ 18 + (-24558343375345) * t ^ 17 + 18139624394483 * t ^ 16 + (-12506523488212) * t ^ 15 + 8028518762376 * t ^ 14 + (-4784195095223) * t ^ 13 + 2636741696836 * t ^ 12 + (-1338093798184) * t ^ 11 + 621899548968 * t ^ 10 + (-262956365876) * t ^ 9 + 100318665152 * t ^ 8 + (-34170800000) * t ^ 7 + 10251491008 * t ^ 6 + (-2659868752) * t ^ 5 + 581879616 * t ^ 4 + (-103367808) * t ^ 3 + 14034816 * t ^ 2 + (-1301184) * t + 62208) * ht

end Cusp62

/-! ### `8_20` cusp equations -/

namespace Cusp820
open QOU.Knot.GeneratedGluing.K820

/-- **Cusp 0** of `8_20`, exponents `[0, 1, -1, 0, -1, 0, 0, -1, 1, -1, 0, 1, 0, -1, 1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 * (z4 t - 1) ^ 1) * (z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z4 t) ^ 1) = ((z0 t - 1) ^ 1 * z3 t ^ 1) * ((1 - z0 t) ^ 1 * z2 t ^ 1 * z3 t ^ 1 * z4 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination ((729 / 262144) * t ^ 20 + (729 / 65536) * t ^ 19 + (7047 / 262144) * t ^ 18 + (4077 / 262144) * t ^ 17 + (-8559 / 131072) * t ^ 16 + (-15273 / 65536) * t ^ 15 + (-10585 / 32768) * t ^ 14 + (-8229 / 131072) * t ^ 13 + (167287 / 262144) * t ^ 12 + (175469 / 131072) * t ^ 11 + (291001 / 262144) * t ^ 10 + (-86863 / 262144) * t ^ 9 + (-544589 / 262144) * t ^ 8 + (-329573 / 131072) * t ^ 7 + (-215737 / 262144) * t ^ 6 + (230969 / 262144) * t ^ 5 + (61877 / 32768) * t ^ 4 + (27909 / 32768) * t ^ 3 + (2123 / 16384) * t ^ 2 + (-163 / 16384) * t + (-5 / 1024)) * ht

/-- **Cusp 1** of `8_20`, exponents `[1, -1, 1, 0, 1, 0, 0, 1, 1, 0, -1, -3, 1, 0, -1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t ^ 1 * (z0 t - 1) ^ 1 * (z2 t - 1) ^ 1 * z4 t ^ 1) * ((1 - z0 t) ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 3 * z4 t ^ 1) = ((z3 t - 1) ^ 3 * (z4 t - 1) ^ 1) * (z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination ((2187 / 2097152) * t ^ 26 + (729 / 262144) * t ^ 25 + (3645 / 1048576) * t ^ 24 + (-11259 / 1048576) * t ^ 23 + (-94635 / 2097152) * t ^ 22 + (-74817 / 1048576) * t ^ 21 + (-13155 / 2097152) * t ^ 20 + (117575 / 524288) * t ^ 19 + (996693 / 2097152) * t ^ 18 + (51215 / 131072) * t ^ 17 + (-44595 / 131072) * t ^ 16 + (-1452777 / 1048576) * t ^ 15 + (-892279 / 524288) * t ^ 14 + (-505255 / 1048576) * t ^ 13 + (3640139 / 2097152) * t ^ 12 + (3287635 / 1048576) * t ^ 11 + (4598713 / 2097152) * t ^ 10 + (-427389 / 1048576) * t ^ 9 + (-5248625 / 2097152) * t ^ 8 + (-669783 / 262144) * t ^ 7 + (-453697 / 524288) * t ^ 6 + (37247 / 65536) * t ^ 5 + (130205 / 131072) * t ^ 4 + (8425 / 16384) * t ^ 3 + (2625 / 32768) * t ^ 2) * ht

end Cusp820

/-! ### `7_4` cusp equations -/

namespace Cusp74
open QOU.Knot.GeneratedGluing.K74

/-- **Cusp 0** of `7_4`, exponents `[2, 0, 0, 0, 0, -1, 1, 0, -1, 0, 0, 0, 0, -1, 1, 0, 0, -1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t ^ 2 * z2 t ^ 1 * (z4 t - 1) ^ 1) * (z1 t ^ 1 * z2 t ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1) = ((z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 * (z5 t - 1) ^ 1) * (z4 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4, z5]
  all_goals linear_combination ((-1 / 2) * t ^ 11 + (15 / 4) * t ^ 10 + (-59 / 4) * t ^ 9 + (301 / 8) * t ^ 8 + (-2173 / 32) * t ^ 7 + (5707 / 64) * t ^ 6 + (-2747 / 32) * t ^ 5 + (3799 / 64) * t ^ 4 + (-881 / 32) * t ^ 3 + (25 / 4) * t ^ 2) * ht

/-- **Cusp 1** of `7_4`, exponents `[-1, 1, 1, 0, 1, 0, 0, -1, 2, 0, -2, 0, 0, 0, -1, -1, -1, 1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z0 t - 1) ^ 1 * (z2 t - 1) ^ 2 * (z5 t - 1) ^ 1) * ((1 - z2 t) ^ 1 * (1 - z3 t) ^ 2 * z4 t ^ 1 * (1 - z5 t) ^ 1) = (z0 t ^ 1 * (z4 t - 1) ^ 1 * z5 t ^ 1) * ((1 - z0 t) ^ 1 * z0 t ^ 1 * (1 - z1 t) ^ 1 * z2 t ^ 2 * z5 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  all_goals linear_combination ((1 / 2) * t ^ 14 + (-25 / 4) * t ^ 13 + (281 / 8) * t ^ 12 + (-1879 / 16) * t ^ 11 + (8245 / 32) * t ^ 10 + (-24567 / 64) * t ^ 9 + (49391 / 128) * t ^ 8 + (-63313 / 256) * t ^ 7 + (21393 / 256) * t ^ 6 + (-125 / 128) * t ^ 5 + (-35 / 4) * t ^ 4 + (15 / 8) * t ^ 3) * ht

end Cusp74

/-! ### `12n242` cusp equations -/

namespace Cusp12n242
open QOU.Knot.GeneratedGluing.K12n242

/-- **Cusp 0** of `12n242`, exponents `[0, 0, 1, -1, 0, 0, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z0 t - 1) ^ 1) * (1) = (z1 t ^ 1) * (z0 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  all_goals linear_combination (1) * ht

/-- **Cusp 1** of `12n242`, exponents `[0, 1, -18, 18, 0, -1, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t ^ 18) * (z0 t ^ 18 * z1 t ^ 1) = ((z0 t - 1) ^ 18 * (z1 t - 1) ^ 1) * ((1 - z0 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  all_goals linear_combination ((-1) * t ^ 53 + 18 * t ^ 52 + (-170) * t ^ 51 + 1104 * t ^ 50 + (-5492) * t ^ 49 + 22169 * t ^ 48 + (-75240) * t ^ 47 + 219894 * t ^ 46 + (-562891) * t ^ 45 + 1278043 * t ^ 44 + (-2598545) * t ^ 43 + 4766412 * t ^ 42 + (-7933027) * t ^ 41 + 12034698 * t ^ 40 + (-16699510) * t ^ 39 + 21252115 * t ^ 38 + (-24852690) * t ^ 37 + 26741139 * t ^ 36 + (-26492624) * t ^ 35 + 24169261 * t ^ 34 + (-20295610) * t ^ 33 + 15670813 * t ^ 32 + (-11107229) * t ^ 31 + 7209583 * t ^ 30 + (-4271820) * t ^ 29 + 2300879 * t ^ 28 + (-1120470) * t ^ 27 + 489886 * t ^ 26 + (-190559) * t ^ 25 + 65161 * t ^ 24 + (-19269) * t ^ 23 + 4814 * t ^ 22 + (-984) * t ^ 21 + 158 * t ^ 20 + (-14) * t ^ 19 + (-4) * t ^ 18 + 12 * t ^ 17 + (-167) * t ^ 16 + 982 * t ^ 15 + (-3859) * t ^ 14 + 11452 * t ^ 13 + (-26360) * t ^ 12 + 47653 * t ^ 11 + (-68409) * t ^ 10 + 78661 * t ^ 9 + (-72788) * t ^ 8 + 54197 * t ^ 7 + (-32292) * t ^ 6 + 15210 * t ^ 5 + (-5545) * t ^ 4 + 1511 * t ^ 3 + (-290) * t ^ 2 + 35 * t + (-2)) * ht

end Cusp12n242

/-! ### `s776` cusp equations -/

namespace Cusps776
open QOU.Knot.GeneratedGluing.Ks776

/-- **Cusp 0** of `s776`, exponents `[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, -1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 1 * z3 t ^ 1) * ((1 - z4 t) ^ 1 * z5 t ^ 1) = ((z5 t - 1) ^ 1) * (z1 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z1, z3, z4, z5]
  all_goals linear_combination ((-4) * t ^ 2 + 1) * ht

/-- **Cusp 1** of `s776`, exponents `[0, 2, 0, 0, 0, 1, 0, -1, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 1 * (z4 t - 1) ^ 1) * ((1 - z2 t) ^ 1 * (1 - z3 t) ^ 1) = (1) * ((1 - z0 t) ^ 2 * z1 t ^ 1 * z4 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination (6 * t ^ 2 + (-1) * t + (-1)) * ht

/-- **Cusp 2** of `s776`, exponents `[0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_2 {t : ℂ} (ht : minpoly t = 0) :
    ((z3 t - 1) ^ 1) * ((1 - z1 t) ^ 1) = (1) * ((1 - z0 t) ^ 1 * z3 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3]
  all_goals linear_combination ((-1)) * ht

/-- **Cusp 3** of `s776`, exponents `[0, 1, 0, 0, 0, 1, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_3 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 1 * (z5 t - 1) ^ 1) * (z2 t ^ 1) = ((z2 t - 1) ^ 1 * z3 t ^ 1) * ((1 - z0 t) ^ 1 * z1 t ^ 1 * z5 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z5]
  all_goals linear_combination (4 * t ^ 3 + (-2) * t ^ 2 + (-2) * t) * ht

/-- **Cusp 4** of `s776`, exponents `[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_4 {t : ℂ} (ht : minpoly t = 0) :
    ((z2 t - 1) ^ 1) * ((1 - z4 t) ^ 1) = (1) * ((1 - z0 t) ^ 1 * z2 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z2, z4]
  all_goals linear_combination ((-1)) * ht

/-- **Cusp 5** of `s776`, exponents `[0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_5 {t : ℂ} (ht : minpoly t = 0) :
    ((z4 t - 1) ^ 1 * (z5 t - 1) ^ 1) * (z3 t ^ 1) = (z2 t ^ 1 * (z3 t - 1) ^ 1) * ((1 - z0 t) ^ 1 * z4 t ^ 1 * z5 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z4, z5]
  all_goals linear_combination (4 * t ^ 3 + (-2) * t ^ 2 + (-2) * t) * ht

end Cusps776

/-! ### `m371` cusp equations -/

namespace Cuspm371
open QOU.Knot.GeneratedGluing.Km371

/-- **Cusp 0** of `m371`, exponents `[-2, 0, 0, -1, 0, 0, -1, 1, 0, 1, 0, 1, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t ^ 1 * (z3 t - 1) ^ 1) * (1) = (z0 t ^ 2 * z1 t ^ 1 * z2 t ^ 1) * ((1 - z2 t) ^ 1 * z3 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  all_goals linear_combination ((1 / 1024) * t ^ 10 + (-1 / 256) * t ^ 9 + (25 / 1024) * t ^ 8 + (-13 / 256) * t ^ 7 + (151 / 1024) * t ^ 6 + (-31 / 256) * t ^ 5 + (179 / 1024) * t ^ 4 + (25 / 256) * t ^ 3 + (-17 / 256) * t ^ 2 + (-19 / 64) * t + (3 / 32)) * ht

/-- **Cusp 1** of `m371`, exponents `[1, 1, 0, 0, 0, -1, 0, 0, 1, -1, -1, 0, 0, 0, 1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t ^ 1 * (z2 t - 1) ^ 1 * (z4 t - 1) ^ 1) * (z1 t ^ 1 * (1 - z3 t) ^ 1) = ((z1 t - 1) ^ 1 * z3 t ^ 1) * ((1 - z0 t) ^ 1 * z2 t ^ 1 * z4 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination ((-1 / 32) * t ^ 4 + (3 / 32) * t ^ 3 + (-5 / 32) * t ^ 2 + (3 / 32) * t) * ht

end Cuspm371

/-! ### `7_7` cusp equations -/

namespace Cusp77
open QOU.Knot.GeneratedGluing.K77

/-- **Cusp 0** of `7_7`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    (1) * (1) = (z5 t ^ 1) * ((1 - z7 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z5, z7]
  all_goals linear_combination (1) * ht

/-- **Cusp 1** of `7_7`, exponents `[-1, 2, 0, 1, 1, 0, 0, -1, 0, 0, 0, 1, -1, 0, -2, -2, 1, 0, -1, 0, 0, 1, 1, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t ^ 1 * (z3 t - 1) ^ 1 * z7 t ^ 1) * ((1 - z2 t) ^ 1 * z4 t ^ 2) = (z0 t ^ 1 * z4 t ^ 1 * (z4 t - 1) ^ 2 * z5 t ^ 2 * z6 t ^ 1) * ((1 - z0 t) ^ 2 * (1 - z1 t) ^ 1 * z3 t ^ 1 * (1 - z5 t) ^ 1 * (1 - z7 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5, z6, z7]
  all_goals linear_combination ((1 / 4) * t ^ 26 + (-9 / 4) * t ^ 25 + (45 / 4) * t ^ 24 + (-165 / 4) * t ^ 23 + (241 / 2) * t ^ 22 + (-294) * t ^ 21 + (1235 / 2) * t ^ 20 + (-2271 / 2) * t ^ 19 + 1853 * t ^ 18 + (-2710) * t ^ 17 + (14305 / 4) * t ^ 16 + (-17165 / 4) * t ^ 15 + (18851 / 4) * t ^ 14 + (-19087 / 4) * t ^ 13 + (9001 / 2) * t ^ 12 + (-7971 / 2) * t ^ 11 + (13369 / 4) * t ^ 10 + (-10661 / 4) * t ^ 9 + 2002 * t ^ 8 + (-1402) * t ^ 7 + (3573 / 4) * t ^ 6 + (-2003 / 4) * t ^ 5 + (485 / 2) * t ^ 4 + (-189 / 2) * t ^ 3 + 28 * t ^ 2 + (-6) * t) * ht

end Cusp77

/-! ### `8_21` cusp equations -/

namespace Cusp821
open QOU.Knot.GeneratedGluing.K821

/-- **Cusp 0** of `8_21`, exponents `[0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, -1, 0, 0, 0, 1, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z3 t - 1) ^ 1) * (1) = (z1 t ^ 1 * z4 t ^ 1 * z5 t ^ 1) * ((1 - z0 t) ^ 1 * z3 t ^ 1 * (1 - z6 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4, z5, z6]
  all_goals linear_combination ((-64) * t ^ 10 + 352 * t ^ 9 + (-1008) * t ^ 8 + 1832 * t ^ 7 + (-2276) * t ^ 6 + 1954 * t ^ 5 + (-1118) * t ^ 4 + 388 * t ^ 3 + (-59) * t ^ 2 + 3 * t + (-1)) * ht

/-- **Cusp 1** of `8_21`, exponents `[1, 4, 0, -4, 0, -1, 0, 0, 0, -1, -2, 3, -6, 0, -1, -3, 1, 2, 1, 6, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t ^ 1 * (z3 t - 1) ^ 3 * (z5 t - 1) ^ 2 * z6 t ^ 1) * (z1 t ^ 1 * (1 - z3 t) ^ 2 * z4 t ^ 1) = (z1 t ^ 4 * (z1 t - 1) ^ 1 * z3 t ^ 1 * z4 t ^ 6 * (z4 t - 1) ^ 1 * z5 t ^ 3) * ((1 - z0 t) ^ 4 * z3 t ^ 3 * (1 - z5 t) ^ 1 * z5 t ^ 2 * (1 - z6 t) ^ 6) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4, z5, z6]
  all_goals linear_combination ((-4398046511104) * t ^ 72 + 184717953466368 * t ^ 71 + (-3892271162327040) * t ^ 70 + 54787015144636416 * t ^ 69 + (-578820304256630784) * t ^ 68 + 4890314909289545728 * t ^ 67 + (-34381961215984271360) * t ^ 66 + 206697644660315127808 * t ^ 65 + (-1083694972054880124928) * t ^ 64 + 5029276752654540734464 * t ^ 63 + (-20900808921708796837888) * t ^ 62 + 78504516299479450648576 * t ^ 61 + (-268512585233995705352192) * t ^ 60 + 841526492088763139751936 * t ^ 59 + (-2429156842514617177473024) * t ^ 58 + 6486754111411943863484416 * t ^ 57 + (-16084156705831735716216832) * t ^ 56 + 37149168376008234403627008 * t ^ 55 + (-80143030096387154450055168) * t ^ 54 + 161871126453757594442924032 * t ^ 53 + (-306718569364877503669207040) * t ^ 52 + 546179989738917110568976384 * t ^ 51 + (-915393028568673654125101056) * t ^ 50 + 1445812324298956471450206208 * t ^ 49 + (-2154370705004621998794473472) * t ^ 48 + 3031294836460713644373442560 * t ^ 47 + (-4030511052063417434808188928) * t ^ 46 + 5067297823202896551188430848 * t ^ 45 + (-6026661347999128951342219264) * t ^ 44 + 6782717062697104391682072576 * t ^ 43 + (-7225120731435205138493063168) * t ^ 42 + 7285112815067370709539526656 * t ^ 41 + (-6952821989293453457160370176) * t ^ 40 + 6279901462616267297337367552 * t ^ 39 + (-5366538032082046271099459328) * t ^ 38 + 4337277993841372317963470848 * t ^ 37 + (-3313617638200864783187777536) * t ^ 36 + 2391537261482235695727302496 * t ^ 35 + (-1629349940545829525260586528) * t ^ 34 + 1046959370116595556161209280 * t ^ 33 + (-633839560555034273363111392) * t ^ 32 + 361123057347451668059830720 * t ^ 31 + (-193366861402379020692484000) * t ^ 30 + 97165418646004622900354088 * t ^ 29 + (-45742259537237982703005816) * t ^ 28 + 20136671981636582572119280 * t ^ 27 + (-8272115071014064514865152) * t ^ 26 + 3163705288096655668586088 * t ^ 25 + (-1123579830113155763742920) * t ^ 24 + 369480112291083868334218 * t ^ 23 + (-112141201957414161062254) * t ^ 22 + 31301988877876357962108 * t ^ 21 + (-8003333813438651079534) * t ^ 20 + 1865977358594362375384 * t ^ 19 + (-394701851619013836510) * t ^ 18 + (150618371475082267499 / 2) * t ^ 17 + (-25750993934197792097 / 2) * t ^ 16 + 1957414082480903917 * t ^ 15 + (-262234681112938984) * t ^ 14 + (61255568233986801 / 2) * t ^ 13 + (-6155991610643339 / 2) * t ^ 12 + 261835279740206 * t ^ 11 + (-18458068432331) * t ^ 10 + (2095785222125 / 2) * t ^ 9 + (-92043980025 / 2) * t ^ 8 + (2973354555 / 2) * t ^ 7 + (-77524733 / 2) * t ^ 6 + 2585567 * t ^ 5 + (-436428) * t ^ 4 + 57452 * t ^ 3 + (-4612) * t ^ 2 + 168 * t) * ht

end Cusp821

/-! ### `6_3` cusp equations -/

namespace Cusp63
open QOU.Knot.GeneratedGluing.K63

/-- **Cusp 0** of `6_3`, exponents `[0, 0, 1, -1, 0, 0, 0, 1, 0, -1, 0, 0, 0, 1, 0, -1, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z0 t - 1) ^ 1) * (1) = (z1 t ^ 1 * z3 t ^ 1 * z5 t ^ 1) * (z0 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z4 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  all_goals linear_combination ((-400 / 81) * t ^ 16 + (-3440 / 81) * t ^ 15 + (-11356 / 81) * t ^ 14 + (-188) * t ^ 13 + (-287 / 27) * t ^ 12 + (3670 / 27) * t ^ 11 + (-6223 / 81) * t ^ 10 + (-2831 / 81) * t ^ 9 + (25118 / 81) * t ^ 8 + (-2665 / 81) * t ^ 7 + (-13112 / 81) * t ^ 6 + (22844 / 81) * t ^ 5 + (-19174 / 81) * t ^ 4 + (7759 / 81) * t ^ 3 + (-3298 / 81) * t ^ 2 + (-2) * t + (-1)) * ht

/-- **Cusp 1** of `6_3`, exponents `[-2, 0, 2, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 0, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z0 t - 1) ^ 2 * (z1 t - 1) ^ 1 * (z3 t - 1) ^ 1) * (z2 t ^ 1 * z4 t ^ 1) = (z0 t ^ 2 * z1 t ^ 1 * z2 t ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 * z4 t ^ 1 * (z4 t - 1) ^ 1) * (z0 t ^ 2 * (1 - z1 t) ^ 1 * z1 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination ((-64000000 / 531441) * t ^ 58 + (-1907200000 / 531441) * t ^ 57 + (-26384000000 / 531441) * t ^ 56 + (-223039360000 / 531441) * t ^ 55 + (-1273720256000 / 531441) * t ^ 54 + (-5107722341120 / 531441) * t ^ 53 + (-14353289182016 / 531441) * t ^ 52 + (-26660390136128 / 531441) * t ^ 51 + (-2842045485152 / 59049) * t ^ 50 + (10155503451952 / 531441) * t ^ 49 + (59823653559980 / 531441) * t ^ 48 + (44045573963548 / 531441) * t ^ 47 + (-46177255907509 / 531441) * t ^ 46 + (-34777692699734 / 531441) * t ^ 45 + (141147153245401 / 531441) * t ^ 44 + (99287524738171 / 531441) * t ^ 43 + (-288062263388300 / 531441) * t ^ 42 + (-65529901193911 / 177147) * t ^ 41 + (489115570959727 / 531441) * t ^ 40 + (147048788935244 / 531441) * t ^ 39 + (-888303853830044 / 531441) * t ^ 38 + (137068191180542 / 531441) * t ^ 37 + (1322732141123416 / 531441) * t ^ 36 + (-890942256796328 / 531441) * t ^ 35 + (-1349872656423260 / 531441) * t ^ 34 + (2127722595537184 / 531441) * t ^ 33 + (38726815591906 / 59049) * t ^ 32 + (-1008778214140072 / 177147) * t ^ 31 + (1917857994003064 / 531441) * t ^ 30 + (2092624022606414 / 531441) * t ^ 29 + (-4059974851211225 / 531441) * t ^ 28 + (1269279427679294 / 531441) * t ^ 27 + (3266035203006767 / 531441) * t ^ 26 + (-4509328571572795 / 531441) * t ^ 25 + (1182946903839755 / 531441) * t ^ 24 + (1076537221368809 / 177147) * t ^ 23 + (-4577452494365173 / 531441) * t ^ 22 + (2070947738363641 / 531441) * t ^ 21 + (1705926543562064 / 531441) * t ^ 20 + (-3748599266660726 / 531441) * t ^ 19 + (3080586114189560 / 531441) * t ^ 18 + (-821448269047888 / 531441) * t ^ 17 + (-1317325608859414 / 531441) * t ^ 16 + (2348767930788917 / 531441) * t ^ 15 + (-760564997835874 / 177147) * t ^ 14 + (548939646152431 / 177147) * t ^ 13 + (-954914933696269 / 531441) * t ^ 12 + (457825423198177 / 531441) * t ^ 11 + (-183122168456764 / 531441) * t ^ 10 + (60918972301549 / 531441) * t ^ 9 + (-16622977918889 / 531441) * t ^ 8 + (3618208452955 / 531441) * t ^ 7 + (-596622661718 / 531441) * t ^ 6 + (7436045791 / 59049) * t ^ 5 + (-3568888702 / 531441) * t ^ 4 + (-33455 / 81) * t ^ 3 + (12961 / 81) * t ^ 2 + (-40) * t + (400 / 81)) * ht

end Cusp63

/-! ### `7_3` cusp equations -/

namespace Cusp73
open QOU.Knot.GeneratedGluing.K73

/-- **Cusp 0** of `7_3`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t ^ 1) * ((1 - z4 t) ^ 1) = (1) * (1) := by
  simp only [minpoly] at ht
  simp only [z3, z4]
  all_goals linear_combination ((195 / 529) * t ^ 4 + (-2 / 529) * t ^ 3 + (-93 / 529) * t ^ 2 + (402 / 529) * t + (193 / 529)) * ht

/-- **Cusp 1** of `7_3`, exponents `[1, 1, 1, 0, -1, 1, -1, -1, -1, 7, -1, -1, 0, -7, 2]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t ^ 1 * (z0 t - 1) ^ 1 * (z1 t - 1) ^ 1 * z3 t ^ 7 * (z4 t - 1) ^ 2) * ((1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 7) = (z2 t ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1) * ((1 - z0 t) ^ 1 * z0 t ^ 1 * z1 t ^ 1 * z4 t ^ 2) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination ((-585832209939208595328468750000 / 907846434775996175406740561329) * t ^ 106 + (15668758415066371430439121875000 / 907846434775996175406740561329) * t ^ 105 + (-208306458986785710914754303046875 / 907846434775996175406740561329) * t ^ 104 + (1807737330760325597427907500984375 / 907846434775996175406740561329) * t ^ 103 + (-11330220205997275123276891282237500 / 907846434775996175406740561329) * t ^ 102 + (53492186157558401461444528922955000 / 907846434775996175406740561329) * t ^ 101 + (-191017914472421363047696492312692000 / 907846434775996175406740561329) * t ^ 100 + (491080065070350172966574147342169300 / 907846434775996175406740561329) * t ^ 99 + (-712674145225937235727123150222310670 / 907846434775996175406740561329) * t ^ 98 + (-650053455374766296347214587442507412 / 907846434775996175406740561329) * t ^ 97 + (7623375702969993076104832197206226549 / 907846434775996175406740561329) * t ^ 96 + (-24806711811798567089023141638795142206 / 907846434775996175406740561329) * t ^ 95 + (43597666646087211035722965603725215128 / 907846434775996175406740561329) * t ^ 94 + (-11254468452622445056242150632732301657 / 907846434775996175406740561329) * t ^ 93 + (-186588495053360182457703839948503765941 / 907846434775996175406740561329) * t ^ 92 + (27074858451013053959248772625141946044 / 39471584120695485887249589623) * t ^ 91 + (-975451042486088345173034719579115622501 / 907846434775996175406740561329) * t ^ 90 + (83776196256314559887104808919376249413 / 907846434775996175406740561329) * t ^ 89 + (3681941795491676079619848045728645680221 / 907846434775996175406740561329) * t ^ 88 + (-9809153089966615210598723179456604447298 / 907846434775996175406740561329) * t ^ 87 + (11104083320264068315699524218301936482598 / 907846434775996175406740561329) * t ^ 86 + (6994743366782376717672428781710686121966 / 907846434775996175406740561329) * t ^ 85 + (-52500786446469570868514499257033529477172 / 907846434775996175406740561329) * t ^ 84 + (96041021862049675406944046531281026834559 / 907846434775996175406740561329) * t ^ 83 + (-52470161501862244878800823215610473333078 / 907846434775996175406740561329) * t ^ 82 + (-163113697174135545121749241501442409849986 / 907846434775996175406740561329) * t ^ 81 + (477469372803885237852495385441229100430098 / 907846434775996175406740561329) * t ^ 80 + (-523451630592168590628294710475407686166889 / 907846434775996175406740561329) * t ^ 79 + (-186226475619205178799964513123748386889088 / 907846434775996175406740561329) * t ^ 78 + (1613464148340403905815176281194811145840284 / 907846434775996175406740561329) * t ^ 77 + (-2526833629410333841671360848356964289851031 / 907846434775996175406740561329) * t ^ 76 + (917287991449960112186839879258195244550343 / 907846434775996175406740561329) * t ^ 75 + (3820453443737314919376625155289797669598308 / 907846434775996175406740561329) * t ^ 74 + (-8374703164028177902630509865439506765240051 / 907846434775996175406740561329) * t ^ 73 + (6268675870225833194448847420232103912688762 / 907846434775996175406740561329) * t ^ 72 + (5901838898958683461593041109513577571077946 / 907846434775996175406740561329) * t ^ 71 + (-20846648403475755937721644642849431803666368 / 907846434775996175406740561329) * t ^ 70 + (937539501440510407146449734642488412026060 / 39471584120695485887249589623) * t ^ 69 + (3317579061243057855552057038285089031563739 / 907846434775996175406740561329) * t ^ 68 + (-40419083792975000787854547210977412531063187 / 907846434775996175406740561329) * t ^ 67 + (2283717847429346615206130016881749232146144 / 39471584120695485887249589623) * t ^ 66 + (-11414515069508773427989277186115073058822215 / 907846434775996175406740561329) * t ^ 65 + (-61993706447352468721658532249654902901043606 / 907846434775996175406740561329) * t ^ 64 + (98751932765900180405309156788388103578586608 / 907846434775996175406740561329) * t ^ 63 + (-43319206773644085640787434117598268733635989 / 907846434775996175406740561329) * t ^ 62 + (-75484738921125801348121405201978846774711151 / 907846434775996175406740561329) * t ^ 61 + (148549798282068147041915322205788862805740127 / 907846434775996175406740561329) * t ^ 60 + (-86998088678529780937641820103115200206791885 / 907846434775996175406740561329) * t ^ 59 + (-72573561242560662741057595385861929536262861 / 907846434775996175406740561329) * t ^ 58 + (182055157165867525740275047664410096192381935 / 907846434775996175406740561329) * t ^ 57 + (-124850453958877330063779974667156939814720886 / 907846434775996175406740561329) * t ^ 56 + (-54429426817706158867010451655753774229604327 / 907846434775996175406740561329) * t ^ 55 + (183493427464279380573587330885173842259188768 / 907846434775996175406740561329) * t ^ 54 + (-137374547045888374515725008464631667646880256 / 907846434775996175406740561329) * t ^ 53 + (-31552176327732605510248757181365974077224814 / 907846434775996175406740561329) * t ^ 52 + (152692546834110233857856297526926576973854162 / 907846434775996175406740561329) * t ^ 51 + (-118318754344743285496183306088678297201809952 / 907846434775996175406740561329) * t ^ 50 + (-14781575211721165422077990803946939800797843 / 907846434775996175406740561329) * t ^ 49 + (104797529912280894051120136263106106046530102 / 907846434775996175406740561329) * t ^ 48 + (-79615878250143386988527953009818765489185406 / 907846434775996175406740561329) * t ^ 47 + (-7180120222169509881735333029578719946969506 / 907846434775996175406740561329) * t ^ 46 + (58880527903636784653489985532819875480226968 / 907846434775996175406740561329) * t ^ 45 + (-40957027217734916013134937923882730102569536 / 907846434775996175406740561329) * t ^ 44 + (-4895344293558702016516816537082469834998818 / 907846434775996175406740561329) * t ^ 43 + (26586965488568447980030342265246760008767407 / 907846434775996175406740561329) * t ^ 42 + (-15265469191808300924111966810559201006324836 / 907846434775996175406740561329) * t ^ 41 + (-3577233242776114014156109557966430166687018 / 907846434775996175406740561329) * t ^ 40 + (9269934336714354939059280875277365269542306 / 907846434775996175406740561329) * t ^ 39 + (-155035022841894275499902088509514351127522 / 39471584120695485887249589623) * t ^ 38 + (-1980123753197841791621699040171177058869905 / 907846434775996175406740561329) * t ^ 37 + (2277409382312874315671022620306599863529399 / 907846434775996175406740561329) * t ^ 36 + (-212238520621291032788346683629517077222817 / 907846434775996175406740561329) * t ^ 35 + (-715212738376572770943142874118460881134334 / 907846434775996175406740561329) * t ^ 34 + (293447291213728360109666687109119756740775 / 907846434775996175406740561329) * t ^ 33 + (162377405429574717569861629109903573106067 / 907846434775996175406740561329) * t ^ 32 + (-140557716984513483903132313620036528206293 / 907846434775996175406740561329) * t ^ 31 + (-21220873804800042046773757630402732470600 / 907846434775996175406740561329) * t ^ 30 + (50702541531485651833630899000678805896151 / 907846434775996175406740561329) * t ^ 29 + (-166249633431520162247413149465916597612 / 39471584120695485887249589623) * t ^ 28 + (-14257871620025517892725363664160066479033 / 907846434775996175406740561329) * t ^ 27 + (2970146686715804842616874672766180682346 / 907846434775996175406740561329) * t ^ 26 + (3737733451144099194124740156050285281334 / 907846434775996175406740561329) * t ^ 25 + (-1147111100868043398951241244515794199473 / 907846434775996175406740561329) * t ^ 24 + (-946068954201232157435153483132731097867 / 907846434775996175406740561329) * t ^ 23 + (355808238460108157345591078482650907284 / 907846434775996175406740561329) * t ^ 22 + (222975707654567250538064231626382927862 / 907846434775996175406740561329) * t ^ 21 + (-82398629279692383670672699829594183880 / 907846434775996175406740561329) * t ^ 20 + (-57139112226266616193168535848231042097 / 907846434775996175406740561329) * t ^ 19 + (17349718743458863369036727281980785039 / 907846434775996175406740561329) * t ^ 18 + (13337985923069084787941834621396856095 / 907846434775996175406740561329) * t ^ 17 + (-2275205566016212081850269265221513811 / 907846434775996175406740561329) * t ^ 16 + (-133250824377060007038366233470147609 / 39471584120695485887249589623) * t ^ 15 + (58195833193108050733301401430931228 / 907846434775996175406740561329) * t ^ 14 + (24779428419575723037808303593620484 / 39471584120695485887249589623) * t ^ 13 + (97323392207334010214711827633799845 / 907846434775996175406740561329) * t ^ 12 + (-77316749589204494883350708788208202 / 907846434775996175406740561329) * t ^ 11 + (-32244125081382917272692726208909251 / 907846434775996175406740561329) * t ^ 10 + (3179666178026928639195243490776945 / 907846434775996175406740561329) * t ^ 9 + (5249009814899256332527003638031747 / 907846434775996175406740561329) * t ^ 8 + (1239072913583346748854169979267170 / 907846434775996175406740561329) * t ^ 7 + (-275670339031942590540905310350406 / 907846434775996175406740561329) * t ^ 6 + (-253803591328838602701044663870264 / 907846434775996175406740561329) * t ^ 5 + (-1991059398816396373196500896945 / 907846434775996175406740561329) * t ^ 4 + (-5727291047332795121475210830913 / 907846434775996175406740561329) * t ^ 3 + (-9131885557421390025028973007900 / 907846434775996175406740561329) * t ^ 2 + (7613546278375609597734166096800 / 907846434775996175406740561329) * t) * ht

end Cusp73

/-! ### `8_1` cusp equations -/

namespace Cusp81
open QOU.Knot.GeneratedGluing.K81

/-- **Cusp 0** of `8_1`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t ^ 1) * (z4 t ^ 1) = ((z4 t - 1) ^ 1) * (1) := by
  simp only [minpoly] at ht
  simp only [z3, z4]
  all_goals linear_combination ((209066936 / 14936564163) * t ^ 4 + (-157069936 / 4978854721) * t ^ 3 + (51315703261 / 104555949141) * t ^ 2 + (-6815782289 / 14936564163) * t + (97506369847 / 104555949141)) * ht

/-- **Cusp 1** of `8_1`, exponents `[-1, -1, 1, 0, 2, -1, 0, 1, 0, 4, 0, 1, 1, 0, -3]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z0 t - 1) ^ 1 * z3 t ^ 4 * (z3 t - 1) ^ 1 * z4 t ^ 1) * ((1 - z0 t) ^ 1 * z1 t ^ 1 * z4 t ^ 3) = (z0 t ^ 1 * (z1 t - 1) ^ 1 * (z4 t - 1) ^ 3) * (z0 t ^ 1 * (1 - z1 t) ^ 2 * (1 - z2 t) ^ 1 * z3 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination ((-7842923502997619394531670911508410374815744 / 109287597492626412893424198938184577990621639956645321) * t ^ 46 + (229514941887319962896373878922133115356315648 / 109287597492626412893424198938184577990621639956645321) * t ^ 45 + (-39401540601470501695053574696167764478821466112 / 765013182448384890253969392567292045934351479696517247) * t ^ 44 + (673410722550223415322073364411476244787242663936 / 765013182448384890253969392567292045934351479696517247) * t ^ 43 + (-23209323122416719613363647151714043337864054493184 / 1785030759046231410592595249323681440513486785958540243) * t ^ 42 + (858053771366214613492806148161044029957526704734208 / 5355092277138694231777785747971044321540460357875620729) * t ^ 41 + (-65753676993543675179166749443505281493479749058156544 / 37485645939970859622444500235797310250783222505129345103) * t ^ 40 + (90747568483075518536432417822235899164914672331184128 / 5355092277138694231777785747971044321540460357875620729) * t ^ 39 + (-38840074487947549930930807618666951278635213428557960128 / 262399521579796017357111501650581171755482557535905415721) * t ^ 38 + (306842731221915347343649611389983824115888870773260742272 / 262399521579796017357111501650581171755482557535905415721) * t ^ 37 + (-105532273390463043653433877377861273674534188408150376048 / 12495215313323619874148166745265770083594407501709781701) * t ^ 36 + (4886546824904546539823119197639854101116757856617050241648 / 87466507193265339119037167216860390585160852511968471907) * t ^ 35 + (-89263943263020685857318164981071091113562081960512506423337 / 262399521579796017357111501650581171755482557535905415721) * t ^ 34 + (167052990733866908026173613172458967414647082799321698619448 / 87466507193265339119037167216860390585160852511968471907) * t ^ 33 + (-866833673101316160334737632679967804036984545074816255752640 / 87466507193265339119037167216860390585160852511968471907) * t ^ 32 + (1387210763413706171230336333721295701433740828310970755620489 / 29155502397755113039679055738953463528386950837322823969) * t ^ 31 + (-55512516710483129110952271846024642165025565997285765056552453 / 262399521579796017357111501650581171755482557535905415721) * t ^ 30 + (25412126908314178402221281762575301299879734585131659670771494 / 29155502397755113039679055738953463528386950837322823969) * t ^ 29 + (-873322724633015891502956594498499202548371797646124537247924633 / 262399521579796017357111501650581171755482557535905415721) * t ^ 28 + (3090906659316858859617876359453969969997985965872274954030259799 / 262399521579796017357111501650581171755482557535905415721) * t ^ 27 + (-1448376978720297846620228448628331279760547706363480369214029641 / 37485645939970859622444500235797310250783222505129345103) * t ^ 26 + (30817031842552686544913391434880405680125519663668306772268509388 / 262399521579796017357111501650581171755482557535905415721) * t ^ 25 + (-86785121005035404581514606264501028021771005189487333884701274710 / 262399521579796017357111501650581171755482557535905415721) * t ^ 24 + (226398820637546933425448512237244172300330659096716948415491281848 / 262399521579796017357111501650581171755482557535905415721) * t ^ 23 + (-547032836139363211710113153486702868609160911183726841860357652307 / 262399521579796017357111501650581171755482557535905415721) * t ^ 22 + (1224033759282950829359350358946482534819153370014291549419360760867 / 262399521579796017357111501650581171755482557535905415721) * t ^ 21 + (-2535833993744807205534872672257005629943675158091294514063089645071 / 262399521579796017357111501650581171755482557535905415721) * t ^ 20 + (4862448318223478671674344897569681128496046570357412639844165095602 / 262399521579796017357111501650581171755482557535905415721) * t ^ 19 + (-8625452090180480038982592272563314190493256955964381739477386132389 / 262399521579796017357111501650581171755482557535905415721) * t ^ 18 + (1571605227940765989128498689136332584703292106485025354812996323412 / 29155502397755113039679055738953463528386950837322823969) * t ^ 17 + (-3060009315170331775016154203529984316251252322478426588806715458325 / 37485645939970859622444500235797310250783222505129345103) * t ^ 16 + (29914131121873291383387182474836687329176584065779089947356233550518 / 262399521579796017357111501650581171755482557535905415721) * t ^ 15 + (-12818033144302287702815432297182005211319213701508038833227773309817 / 87466507193265339119037167216860390585160852511968471907) * t ^ 14 + (45390538484376865471733274422554239993367529221703430110917087954136 / 262399521579796017357111501650581171755482557535905415721) * t ^ 13 + (-16348209542207810245969857730308396727264349919681735072466862468003 / 87466507193265339119037167216860390585160852511968471907) * t ^ 12 + (16105596945926566820496104205431739371405840879533797463512477691312 / 87466507193265339119037167216860390585160852511968471907) * t ^ 11 + (-43181423923482835910449892943763581875895137325626622726429240206845 / 262399521579796017357111501650581171755482557535905415721) * t ^ 10 + (34785785497339609688505812367970933722847276657865058637166732764909 / 262399521579796017357111501650581171755482557535905415721) * t ^ 9 + (-25051757479649566462117309531962197488228554207107136423120409383094 / 262399521579796017357111501650581171755482557535905415721) * t ^ 8 + (15957359496387734662733594035079590318536604407041855666441615119388 / 262399521579796017357111501650581171755482557535905415721) * t ^ 7 + (-2954578296256451448182169297190320824345379606990935909753339722367 / 87466507193265339119037167216860390585160852511968471907) * t ^ 6 + (4211441584104840632691731592923495372054515568768184085029929771582 / 262399521579796017357111501650581171755482557535905415721) * t ^ 5 + (-1665597177277233880440472509529928339951907684187689552362489016686 / 262399521579796017357111501650581171755482557535905415721) * t ^ 4 + (526497483665096630439559326864935371017219482842834231690995594208 / 262399521579796017357111501650581171755482557535905415721) * t ^ 3 + (-17797363593888509567217287346172258410776293310044318748225850128 / 37485645939970859622444500235797310250783222505129345103) * t ^ 2 + (1163913569596461028685766714221955713974859202359912894300000 / 15612513927518058984774885562597796855803091422377903) * t + (-1436959783569872388916875337893370558589356638112055740000 / 247817681389175539440871199406314235806398276545681)) * ht

end Cusp81

/-! ### `9_42` cusp equations -/

namespace Cusp942
open QOU.Knot.GeneratedGluing.K942

/-- **Cusp 0** of `9_42`, exponents `[0, 0, -1, 0, -1, 1, 0, 1, 0, 1, -1, 0, 0, 2, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 1 * z3 t ^ 1) * (z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z3 t) ^ 1) = ((z0 t - 1) ^ 1) * (z1 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z4 t) ^ 2) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination (64 * t ^ 12 + (-384) * t ^ 11 + 1040 * t ^ 10 + (-1792) * t ^ 9 + 2300 * t ^ 8 + (-2296) * t ^ 7 + 1783 * t ^ 6 + (-1100) * t ^ 5 + 532 * t ^ 4 + (-187) * t ^ 3 + 51 * t ^ 2 + (-12) * t + 1) * ht

/-- **Cusp 1** of `9_42`, exponents `[0, 1, 3, -1, 3, -4, 1, -4, 0, -3, 2, 1, 0, -7, 1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z0 t - 1) ^ 3 * z2 t ^ 1 * (z3 t - 1) ^ 1 * (z4 t - 1) ^ 1) * (z1 t ^ 4 * (1 - z2 t) ^ 4 * (1 - z4 t) ^ 7) = (z1 t ^ 1 * (z1 t - 1) ^ 4 * z3 t ^ 3) * ((1 - z0 t) ^ 1 * z0 t ^ 3 * (1 - z1 t) ^ 3 * (1 - z3 t) ^ 2 * z3 t ^ 1 * z4 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  all_goals linear_combination ((-67108864) * t ^ 56 + 1811939328 * t ^ 55 + (-24008196096) * t ^ 54 + 208624680960 * t ^ 53 + (-1340575055872) * t ^ 52 + 6808789843968 * t ^ 51 + (-28525027393536) * t ^ 50 + 101544131297280 * t ^ 49 + (-313927270137856) * t ^ 48 + 856975088025600 * t ^ 47 + (-2092776345894912) * t ^ 46 + 4619613888118784 * t ^ 45 + (-9295623660306432) * t ^ 44 + 17169220717838336 * t ^ 43 + (-29276565710225408) * t ^ 42 + 46310358043344896 * t ^ 41 + (-68231584078814208) * t ^ 40 + 93957461849543680 * t ^ 39 + (-121276877170718976) * t ^ 38 + 147094343244078336 * t ^ 37 + (-167992738450319488) * t ^ 36 + 180976897539941248 * t ^ 35 + (-184173911665158688) * t ^ 34 + 177265924431858656 * t ^ 33 + (-161521301067605940) * t ^ 32 + 139431094118901068 * t ^ 31 + (-114088113622181183) * t ^ 30 + 88513322307505699 * t ^ 29 + (-65119814390311226) * t ^ 28 + 45427055355330164 * t ^ 27 + (-30038851410341835) * t ^ 26 + 18818955497126168 * t ^ 25 + (-11161616322578958) * t ^ 24 + 6261024694970523 * t ^ 23 + (-3317402694481754) * t ^ 22 + 1657673035654791 * t ^ 21 + (-779664417211497) * t ^ 20 + 344355554458202 * t ^ 19 + (-142419403010003) * t ^ 18 + 54968391064962 * t ^ 17 + (-19717291743151) * t ^ 16 + 6540206274888 * t ^ 15 + (-1993732555261) * t ^ 14 + 554295331649 * t ^ 13 + (-139187897898) * t ^ 12 + 31175597916 * t ^ 11 + (-6126437308) * t ^ 10 + 1032897637 * t ^ 9 + (-144829848) * t ^ 8 + 16174820 * t ^ 7 + (-1364921) * t ^ 6 + 86876 * t ^ 5 + (-5898) * t ^ 4 + 635 * t ^ 3 + (-55) * t ^ 2 + 2 * t) * ht

end Cusp942

/-! ### `v3227` cusp equations -/

namespace Cuspv3227
open QOU.Knot.GeneratedGluing.Kv3227

/-- **Cusp 0** of `v3227`, exponents `[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_0 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t ^ 1 * z6 t ^ 1) * ((1 - z3 t) ^ 1 * z4 t ^ 1) = ((z4 t - 1) ^ 1) * (1) := by
  simp only [minpoly] at ht
  simp only [z2, z3, z4, z6]
  all_goals linear_combination ((-1 / 8) * t ^ 5 + (3 / 4) * t ^ 4 + (-11 / 8) * t ^ 3 + (3 / 8) * t ^ 2 + 1 * t + (-5 / 8)) * ht

/-- **Cusp 1** of `v3227`, exponents `[0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_1 {t : ℂ} (ht : minpoly t = 0) :
    ((z2 t - 1) ^ 2) * (z5 t ^ 1) = ((z5 t - 1) ^ 1 * z6 t ^ 1) * ((1 - z0 t) ^ 1 * z2 t ^ 2 * (1 - z3 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z5, z6]
  all_goals linear_combination ((1 / 8) * t ^ 8 + (-5 / 4) * t ^ 7 + (39 / 8) * t ^ 6 + (-37 / 4) * t ^ 5 + 8 * t ^ 4 + (-3 / 4) * t ^ 3 + (-19 / 8) * t ^ 2 + (-1 / 4) * t + (-1 / 8)) * ht

/-- **Cusp 2** of `v3227`, exponents `[0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_2 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t ^ 1 * z3 t ^ 1) * (z5 t ^ 1 * (1 - z6 t) ^ 1) = ((z5 t - 1) ^ 1) * (1) := by
  simp only [minpoly] at ht
  simp only [z1, z3, z5, z6]
  all_goals linear_combination ((-1 / 8) * t ^ 5 + (3 / 4) * t ^ 4 + (-11 / 8) * t ^ 3 + (3 / 8) * t ^ 2 + 1 * t + (-5 / 8)) * ht

/-- **Cusp 3** of `v3227`, exponents `[0, 1, 0, 0, 0, 2, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_3 {t : ℂ} (ht : minpoly t = 0) :
    ((z1 t - 1) ^ 2) * (z4 t ^ 1) = (z3 t ^ 1 * (z4 t - 1) ^ 1) * ((1 - z0 t) ^ 1 * z1 t ^ 2 * (1 - z6 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4, z6]
  all_goals linear_combination ((1 / 8) * t ^ 8 + (-5 / 4) * t ^ 7 + (39 / 8) * t ^ 6 + (-37 / 4) * t ^ 5 + 8 * t ^ 4 + (-3 / 4) * t ^ 3 + (-19 / 8) * t ^ 2 + (-1 / 4) * t + (-1 / 8)) * ht

/-- **Cusp 4** of `v3227`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_4 {t : ℂ} (ht : minpoly t = 0) :
    ((z6 t - 1) ^ 1) * (z3 t ^ 1) = ((z3 t - 1) ^ 1) * (z6 t ^ 1) := by
  simp only [minpoly] at ht
  simp only [z3, z6]
  all_goals linear_combination (0) * ht

/-- **Cusp 5** of `v3227`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 1, 0, -1, 0, 0]`.

Negative exponents are removed by moving those factors to the other side —
legitimate because every edge parameter is a unit — and then denominators are
cleared, leaving a polynomial identity. -/
theorem cusp_5 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t ^ 1) * ((1 - z4 t) ^ 1) = (z6 t ^ 1) * ((1 - z5 t) ^ 1) := by
  simp only [minpoly] at ht
  simp only [z3, z4, z5, z6]
  all_goals linear_combination (0) * ht

end Cuspv3227

end QOU.Knot.GeneratedCusp
