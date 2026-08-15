/-
  High-degree edge gluing equations: shape fields of degree 7–9.

  Bean `qou-glhi`.  Same generator, same certificates, same formulation as
  `QOU/Knot/GeneratedGluing.lean` (degrees 2–6) — read that module's header for the
  formulation and its scope limits, which apply verbatim here.  This is a **separate
  module** for one reason only: the cofactors are an order of magnitude larger, so
  isolating them keeps the degree 2–6 module's compile time unchanged.

  ═══ WHAT "HIGHER DEGREE" COSTS, MEASURED ═══

  Nothing about the *method* changes with degree — that is the point worth recording.
  The cofactor `q = (LHS − RHS)/P` is still an exact polynomial division, still asserted
  to have zero residual before emission, and each proof is still one
  `linear_combination`.  What grows is size:

      knot   deg  tets  eqs   cofactor deg   max coef digits   emitted chars
      6_1     4     4    4         11               2            4,853
      9_2     7     5    5         35              15            8,287
      10_1    8     6    6         40               2           13,475
      7_5     8     7    7         34               4           13,869
      8_2     8     6    6         35              10           17,917
      8_3     8     6    6         31               4           11,428
      7_6     9     8    8         39               4           23,266

  So a degree-9 manifold costs ~5× the characters of a degree-4 one, and the cofactor
  degree roughly quadruples.  Both are linear-ish in `deg × tets`, not explosive.

  ═══ ⚠ SCOPE ═══

  Edge equations only, at an **arbitrary root** of the minimal polynomial — flat shapes
  are therefore permitted and nothing here establishes hyperbolicity, which needs
  `Im z > 0`.  Nothing here says any of this is a triangulation *of* a knot complement.

  -- Ref: [thurston1978] Ch. 4
  -- Ref: [neumann-zagier1985]
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Tactic.LinearCombination

namespace QOU.Knot.GeneratedGluingHigh

/-! ### `9_2` — 5 tetrahedra, shape field of degree 7

Minimal polynomial `8*x^7 - 33*x^6 + 60*x^5 - 65*x^4 + 45*x^3 - 21*x^2 + 6*x - 1`. -/

namespace K92

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 8 * t ^ 7 + (-33) * t ^ 6 + 60 * t ^ 5 + (-65) * t ^ 4 + 45 * t ^ 3 + (-21) * t ^ 2 + 6 * t + (-1)

/-- Shape `z0` of `9_2`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `9_2`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-8) * t ^ 6 + 25 * t ^ 5 + (-35) * t ^ 4 + 30 * t ^ 3 + (-15) * t ^ 2 + 6 * t

/-- Shape `z2` of `9_2`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (-8) * t ^ 6 + 33 * t ^ 5 + (-60) * t ^ 4 + 65 * t ^ 3 + (-45) * t ^ 2 + 21 * t + (-5)

/-- Shape `z3` of `9_2`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-8) * t ^ 6 + 33 * t ^ 5 + (-60) * t ^ 4 + 65 * t ^ 3 + (-44) * t ^ 2 + 18 * t + (-3)

/-- Shape `z4` of `9_2`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := 24 * t ^ 6 + (-107) * t ^ 5 + 197 * t ^ 4 + (-197) * t ^ 3 + 113 * t ^ 2 + (-38) * t + 6

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (8 * t ^ 6 + (-33) * t ^ 5 + 60 * t ^ 4 + (-65) * t ^ 3 + 45 * t ^ 2 + (-21) * t + 6) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-8) * t ^ 6 + 25 * t ^ 5 + (-35) * t ^ 4 + 30 * t ^ 3 + (-15) * t ^ 2 + 6 * t) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-8) * t ^ 6 + 33 * t ^ 5 + (-60) * t ^ 4 + 65 * t ^ 3 + (-45) * t ^ 2 + 21 * t + (-5)) * h + (8 * t ^ 5 + (-25) * t ^ 4 + 35 * t ^ 3 + (-30) * t ^ 2 + 15 * t + (-6)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (8 * t ^ 6 + (-25) * t ^ 5 + 35 * t ^ 4 + (-30) * t ^ 3 + 15 * t ^ 2 + (-6) * t + 1) * h + (8 * t ^ 5 + (-25) * t ^ 4 + 35 * t ^ 3 + (-30) * t ^ 2 + 15 * t + (-6)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (24 * t ^ 6 + (-91) * t ^ 5 + 147 * t ^ 4 + (-135) * t ^ 3 + 78 * t ^ 2 + (-27) * t + 6) * h + (24 * t ^ 5 + (-91) * t ^ 4 + 147 * t ^ 3 + (-135) * t ^ 2 + 75 * t + (-19)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-32) * t ^ 6 + 76 * t ^ 5 + (-33) * t ^ 4 + (-53) * t ^ 3 + 78 * t ^ 2 + (-34) * t + 10) * h + (32 * t ^ 5 + (-76) * t ^ 4 + 33 * t ^ 3 + 53 * t ^ 2 + (-82) * t + 39) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (32 * t ^ 6 + (-140) * t ^ 5 + 257 * t ^ 4 + (-262) * t ^ 3 + 158 * t ^ 2 + (-56) * t + 10) * h + ((-96) * t ^ 5 + 452 * t ^ 4 + (-847) * t ^ 3 + 795 * t ^ 2 + (-362) * t + 59) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (112 * t ^ 6 + (-318) * t ^ 5 + 302 * t ^ 4 + (-77) * t ^ 3 + (-86) * t ^ 2 + 57 * t + (-22)) * h + (336 * t ^ 5 + (-1066) * t ^ 4 + 1000 * t ^ 3 + (-9) * t ^ 2 + (-467) * t + 109) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `9_2`, exponents `[2, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 2 * z1 t ^ 1 * z2 t ^ 1 * (z2 t - 1) ^ 1 = (1 - z1 t) ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-64) * t ^ 13 + 464 * t ^ 12 + (-1585) * t ^ 11 + 3415 * t ^ 10 + (-5195) * t ^ 9 + 5911 * t ^ 8 + (-5188) * t ^ 7 + 3537 * t ^ 6 + (-1837) * t ^ 5 + 675 * t ^ 4 + (-136) * t ^ 3 + (-15) * t ^ 2 + 21 * t + (-5)) * ht

/-- **Edge 1** of `9_2`, exponents `[0, 2, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z1 t ^ 1 * (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 = (1 - z0 t) ^ 2 * z0 t ^ 1 * z1 t ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination (512 * t ^ 18 + (-5824) * t ^ 17 + 31832 * t ^ 16 + (-111625) * t ^ 15 + 282267 * t ^ 14 + (-547624) * t ^ 13 + 846077 * t ^ 12 + (-1065960) * t ^ 11 + 1111805 * t ^ 10 + (-968463) * t ^ 9 + 706912 * t ^ 8 + (-431520) * t ^ 7 + 218496 * t ^ 6 + (-90285) * t ^ 5 + 29583 * t ^ 4 + (-7299) * t ^ 3 + 1224 * t ^ 2 + (-108) * t) * ht

/-- **Edge 2** of `9_2`, exponents `[0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * z2 t ^ 1 * (z3 t - 1) ^ 2 = z0 t ^ 1 * (1 - z1 t) ^ 1 * z3 t ^ 2 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination (1536 * t ^ 18 + (-17984) * t ^ 17 + 100296 * t ^ 16 + (-355571) * t ^ 15 + 900586 * t ^ 14 + (-1733529) * t ^ 13 + 2630466 * t ^ 12 + (-3217629) * t ^ 11 + 3214127 * t ^ 10 + (-2636743) * t ^ 9 + 1774213 * t ^ 8 + (-969836) * t ^ 7 + 420815 * t ^ 6 + (-137479) * t ^ 5 + 29068 * t ^ 4 + (-1191) * t ^ 3 + (-1682) * t ^ 2 + 611 * t + (-80)) * ht

/-- **Edge 3** of `9_2`, exponents `[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0, 0, 1, 2]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z4 t - 1) ^ 2 = z1 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 2 * (1 - z4 t) ^ 1 * z4 t ^ 2 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4]
  linear_combination ((-7077888) * t ^ 35 + 175177728 * t ^ 34 + (-2113228800) * t ^ 33 + 16567810048 * t ^ 32 + (-94961587520) * t ^ 31 + 424353147664 * t ^ 30 + (-1539504362331) * t ^ 29 + 4661638319768 * t ^ 28 + (-12019847684309) * t ^ 27 + 26791262738873 * t ^ 26 + (-52222090177706) * t ^ 25 + 89831373111885 * t ^ 24 + (-137352894688743) * t ^ 23 + 187741528142654 * t ^ 22 + (-230433450632412) * t ^ 21 + 254857892380290 * t ^ 20 + (-254643519324367) * t ^ 19 + 230254755038360 * t ^ 18 + (-188603394095904) * t ^ 17 + 139974268492329 * t ^ 16 + (-94071774988616) * t ^ 15 + 57171264361325 * t ^ 14 + (-31347383708614) * t ^ 13 + 15455134810027 * t ^ 12 + (-6820179162205) * t ^ 11 + 2677386591344 * t ^ 10 + (-927504689961) * t ^ 9 + 280539410709 * t ^ 8 + (-73045355658) * t ^ 7 + 16059870693 * t ^ 6 + (-2901800068) * t ^ 5 + 413943161 * t ^ 4 + (-43714531) * t ^ 3 + 3036792 * t ^ 2 + (-104060) * t + 25) * ht

/-- **Edge 4** of `9_2`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z3 t ^ 1 * z4 t ^ 2 = 1 := by
  simp only [minpoly] at ht
  simp only [z3, z4]
  linear_combination ((-576) * t ^ 11 + 5136 * t ^ 10 + (-20905) * t ^ 9 + 51614 * t ^ 8 + (-86319) * t ^ 7 + 103063 * t ^ 6 + (-89850) * t ^ 5 + 57123 * t ^ 4 + (-25767) * t ^ 3 + 7731 * t ^ 2 + (-1362) * t + 109) * ht

end K92

/-! ### `10_1` — 6 tetrahedra, shape field of degree 8

Minimal polynomial `x^8 + 7*x^7 + 14*x^6 - x^5 - 25*x^4 - 17*x^3 + 4*x^2 + 11*x + 7`. -/

namespace K101

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 8 + 7 * t ^ 7 + 14 * t ^ 6 + (-1) * t ^ 5 + (-25) * t ^ 4 + (-17) * t ^ 3 + 4 * t ^ 2 + 11 * t + 7

/-- Shape `z0` of `10_1`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `10_1`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (11 / 49) * t ^ 7 + (10 / 7) * t ^ 6 + (15 / 7) * t ^ 5 + (-109 / 49) * t ^ 4 + (-268 / 49) * t ^ 3 + (-12 / 49) * t ^ 2 + (163 / 49) * t + (93 / 49)

/-- Shape `z2` of `10_1`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := 1 * t ^ 3 + 1 * t ^ 2 + (-1) * t

/-- Shape `z3` of `10_1`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (416 / 2915) * t ^ 7 + (2543 / 2915) * t ^ 6 + (70 / 53) * t ^ 5 + (-334 / 583) * t ^ 4 + (-3596 / 2915) * t ^ 3 + (-502 / 2915) * t ^ 2 + (-887 / 2915) * t + (2267 / 2915)

/-- Shape `z4` of `10_1`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (416 / 2915) * t ^ 7 + (2543 / 2915) * t ^ 6 + (70 / 53) * t ^ 5 + (-334 / 583) * t ^ 4 + (-3596 / 2915) * t ^ 3 + (-502 / 2915) * t ^ 2 + (-887 / 2915) * t + (2267 / 2915)

/-- Shape `z5` of `10_1`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := (416 / 2915) * t ^ 7 + (2543 / 2915) * t ^ 6 + (70 / 53) * t ^ 5 + (-334 / 583) * t ^ 4 + (-3596 / 2915) * t ^ 3 + (-502 / 2915) * t ^ 2 + (-887 / 2915) * t + (2267 / 2915)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 7) * t ^ 7 + (-1) * t ^ 6 + (-2) * t ^ 5 + (1 / 7) * t ^ 4 + (25 / 7) * t ^ 3 + (17 / 7) * t ^ 2 + (-4 / 7) * t + (-11 / 7)) * h + ((1 / 7)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 7 + 8 * t ^ 6 + 22 * t ^ 5 + 21 * t ^ 4 + (-4) * t ^ 3 + (-21) * t ^ 2 + (-17) * t + (-6)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 2) * h + ((-11 / 49) * t + (1 / 7)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 6 + (-7) * t ^ 5 + (-15) * t ^ 4 + (-6) * t ^ 3 + 10 * t ^ 2 + 11 * t + 7) * h + ((-11 / 49) * t ^ 5 + (-10 / 7) * t ^ 4 + (-116 / 49) * t ^ 3 + (39 / 49) * t ^ 2 + (152 / 49) * t + (51 / 49)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((6 / 385) * t ^ 7 + (7 / 55) * t ^ 6 + (1 / 5) * t ^ 5 + (-237 / 385) * t ^ 4 + (-619 / 385) * t ^ 3 + (2 / 77) * t ^ 2 + (549 / 385) * t + (514 / 385)) * h + ((-6 / 385) * t ^ 2 + (-13 / 385) * t + (1 / 7)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (2 * t ^ 7 + 12 * t ^ 6 + 17 * t ^ 5 + (-12) * t ^ 4 + (-23) * t ^ 3 + (-5) * t ^ 2 + 3 * t + 8) * h + (2 * t ^ 2 + (-1)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-38 / 265) * t ^ 7 + (-46 / 53) * t ^ 6 + (-342 / 265) * t ^ 5 + (97 / 265) * t ^ 4 + (91 / 265) * t ^ 3 + (-26 / 265) * t ^ 2 + (61 / 53) * t + (367 / 265)) * h + ((15808 / 772475) * t ^ 6 + (81658 / 772475) * t ^ 5 + (80544 / 772475) * t ^ 4 + (-39818 / 772475) * t ^ 3 + (139393 / 772475) * t ^ 2 + (-38912 / 772475) * t + (-8502 / 772475)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((152 / 265) * t ^ 7 + (184 / 53) * t ^ 6 + (1368 / 265) * t ^ 5 + (-653 / 265) * t ^ 4 + (-1424 / 265) * t ^ 3 + (-426 / 265) * t ^ 2 + (-32 / 53) * t + (652 / 265)) * h + ((63232 / 772475) * t ^ 6 + (326632 / 772475) * t ^ 5 + (322176 / 772475) * t ^ 4 + (-269512 / 772475) * t ^ 3 + (214397 / 772475) * t ^ 2 + (-146373 / 772475) * t + (49997 / 772475)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-38 / 265) * t ^ 7 + (-46 / 53) * t ^ 6 + (-342 / 265) * t ^ 5 + (97 / 265) * t ^ 4 + (91 / 265) * t ^ 3 + (-26 / 265) * t ^ 2 + (61 / 53) * t + (367 / 265)) * h + ((15808 / 772475) * t ^ 6 + (81658 / 772475) * t ^ 5 + (80544 / 772475) * t ^ 4 + (-39818 / 772475) * t ^ 3 + (139393 / 772475) * t ^ 2 + (-38912 / 772475) * t + (-8502 / 772475)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((152 / 265) * t ^ 7 + (184 / 53) * t ^ 6 + (1368 / 265) * t ^ 5 + (-653 / 265) * t ^ 4 + (-1424 / 265) * t ^ 3 + (-426 / 265) * t ^ 2 + (-32 / 53) * t + (652 / 265)) * h + ((63232 / 772475) * t ^ 6 + (326632 / 772475) * t ^ 5 + (322176 / 772475) * t ^ 4 + (-269512 / 772475) * t ^ 3 + (214397 / 772475) * t ^ 2 + (-146373 / 772475) * t + (49997 / 772475)) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-38 / 265) * t ^ 7 + (-46 / 53) * t ^ 6 + (-342 / 265) * t ^ 5 + (97 / 265) * t ^ 4 + (91 / 265) * t ^ 3 + (-26 / 265) * t ^ 2 + (61 / 53) * t + (367 / 265)) * h + ((15808 / 772475) * t ^ 6 + (81658 / 772475) * t ^ 5 + (80544 / 772475) * t ^ 4 + (-39818 / 772475) * t ^ 3 + (139393 / 772475) * t ^ 2 + (-38912 / 772475) * t + (-8502 / 772475)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((152 / 265) * t ^ 7 + (184 / 53) * t ^ 6 + (1368 / 265) * t ^ 5 + (-653 / 265) * t ^ 4 + (-1424 / 265) * t ^ 3 + (-426 / 265) * t ^ 2 + (-32 / 53) * t + (652 / 265)) * h + ((63232 / 772475) * t ^ 6 + (326632 / 772475) * t ^ 5 + (322176 / 772475) * t ^ 4 + (-269512 / 772475) * t ^ 3 + (214397 / 772475) * t ^ 2 + (-146373 / 772475) * t + (49997 / 772475)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `10_1`, exponents `[2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 2 * z1 t ^ 1 = 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1]
  linear_combination ((11 / 49) * t + (-1 / 7)) * ht

/-- **Edge 1** of `10_1`, exponents `[0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z1 t ^ 2 * (1 - z2 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-121 / 2401) * t ^ 10 + (-99 / 343) * t ^ 9 + (-423 / 2401) * t ^ 8 + (3320 / 2401) * t ^ 7 + (3515 / 2401) * t ^ 6 + (-5612 / 2401) * t ^ 5 + (-6247 / 2401) * t ^ 4 + (3606 / 2401) * t ^ 3 + (4405 / 2401) * t ^ 2 + (-775 / 2401) * t + (-137 / 343)) * ht

/-- **Edge 2** of `10_1`, exponents `[0, 1, 2, 0, 2, 0, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 2 * (z2 t - 1) ^ 2 = (1 - z0 t) ^ 1 * z0 t ^ 2 * (1 - z1 t) ^ 2 * z2 t ^ 2 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((173056 / 168610225) * t ^ 29 + (147264 / 7570255) * t ^ 28 + (3064508313 / 20401837225) * t ^ 27 + (11577476602 / 20401837225) * t ^ 26 + (3275737631 / 4080367445) * t ^ 25 + (-29030396009 / 20401837225) * t ^ 24 + (-134806765816 / 20401837225) * t ^ 23 + (-91591909804 / 20401837225) * t ^ 22 + (292785993372 / 20401837225) * t ^ 21 + (92548725449 / 4080367445) * t ^ 20 + (-5184367479 / 416364025) * t ^ 19 + (-160476390506 / 4080367445) * t ^ 18 + (67528098531 / 20401837225) * t ^ 17 + (1410502806 / 37851275) * t ^ 16 + (-8921267792 / 2914548175) * t ^ 15 + (-451024064454 / 20401837225) * t ^ 14 + (31087143051 / 2914548175) * t ^ 13 + (159500442247 / 20401837225) * t ^ 12 + (-248651021233 / 20401837225) * t ^ 11 + (20262909866 / 20401837225) * t ^ 10 + (129809408397 / 20401837225) * t ^ 9 + (-11578933606 / 2914548175) * t ^ 8 + (-3069102213 / 4080367445) * t ^ 7 + (53755279007 / 20401837225) * t ^ 6 + (-2422997977 / 1854712475) * t ^ 5 + (-84346952 / 168610225) * t ^ 4 + (2274 / 2401) * t ^ 3 + (-103 / 343) * t ^ 2 + (-11 / 49) * t + (1 / 7)) * ht

/-- **Edge 3** of `10_1`, exponents `[0, 0, 0, 1, 0, 0, 2, 0, 0, 1, 1, 0, 1, 1, 0, 2, 0, 1]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * z2 t ^ 2 * z3 t ^ 1 * z4 t ^ 1 * z5 t ^ 2 * (z5 t - 1) ^ 1 = (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4, z5]
  linear_combination ((12458525720576 / 937553782617615625) * t ^ 40 + (875121586733056 / 2062618321758754375) * t ^ 39 + (1798664663138304 / 294659760251250625) * t ^ 38 + (106828121751709696 / 2062618321758754375) * t ^ 37 + (116851161761144928 / 412523664351750875) * t ^ 36 + (10429959189440178021 / 10313091608793771875) * t ^ 35 + (4482707332123100763 / 2062618321758754375) * t ^ 34 + (3324092196823039473 / 2062618321758754375) * t ^ 33 + (-10630658975470087357 / 2062618321758754375) * t ^ 32 + (-24697052497288063633 / 1473298801256253125) * t ^ 31 + (-150211841272326465836 / 10313091608793771875) * t ^ 30 + (41767400691184074041 / 2062618321758754375) * t ^ 29 + (593715024299884006071 / 10313091608793771875) * t ^ 28 + (300676828449961223527 / 10313091608793771875) * t ^ 27 + (-601331959714384255598 / 10313091608793771875) * t ^ 26 + (-954093357293607054558 / 10313091608793771875) * t ^ 25 + (-171604588035474106946 / 10313091608793771875) * t ^ 24 + (812693617908608357521 / 10313091608793771875) * t ^ 23 + (881421874362776928306 / 10313091608793771875) * t ^ 22 + (27491592442821470233 / 10313091608793771875) * t ^ 21 + (-103960034342184598789 / 1473298801256253125) * t ^ 20 + (-540833231371503301578 / 10313091608793771875) * t ^ 19 + (108683127910282525272 / 10313091608793771875) * t ^ 18 + (53370278778324153728 / 1473298801256253125) * t ^ 17 + (6266505924373734551 / 294659760251250625) * t ^ 16 + (-57634438730759989216 / 10313091608793771875) * t ^ 15 + (-31532496068816640647 / 2062618321758754375) * t ^ 14 + (-43206611652025495354 / 10313091608793771875) * t ^ 13 + (23698070776138701023 / 10313091608793771875) * t ^ 12 + (20827915917419450706 / 10313091608793771875) * t ^ 11 + (11561051076815841784 / 10313091608793771875) * t ^ 10 + (-3854498351320251279 / 10313091608793771875) * t ^ 9 + (-2063859331384339348 / 10313091608793771875) * t ^ 8 + (1295398328368441944 / 10313091608793771875) * t ^ 7 + (-182372972016990647 / 1473298801256253125) * t ^ 6 + (-794235699898664486 / 10313091608793771875) * t ^ 5 + (886788910540975114 / 10313091608793771875) * t ^ 4 + (-15674824837497877 / 937553782617615625) * t ^ 3 + (-35244225307321931 / 1473298801256253125) * t ^ 2 + (-5163910704 / 1213701132875) * t + (-951922368 / 173385876125)) * ht

/-- **Edge 4** of `10_1`, exponents `[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t - 1) ^ 1 * (z4 t - 1) ^ 1 * (z5 t - 1) ^ 1 = (1 - z2 t) ^ 1 * z3 t ^ 1 * z4 t ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z2, z3, z4, z5]
  linear_combination ((71991296 / 24769410875) * t ^ 16 + (888296448 / 24769410875) * t ^ 15 + (32733792 / 198155287) * t ^ 14 + (7758352399 / 24769410875) * t ^ 13 + (1765071012 / 24769410875) * t ^ 12 + (-11192929437 / 24769410875) * t ^ 11 + (-562979658 / 2251764625) * t ^ 10 + (5666708599 / 24769410875) * t ^ 9 + (763965674 / 4953882175) * t ^ 8 + (194225799 / 467347375) * t ^ 7 + (-2475711596 / 24769410875) * t ^ 6 + (-3283414661 / 4953882175) * t ^ 5 + (348711021 / 24769410875) * t ^ 4 + (136302266 / 24769410875) * t ^ 3 + (19458528 / 2251764625) * t ^ 2 + (2806206791 / 24769410875) * t + (-584311 / 8497225)) * ht

/-- **Edge 5** of `10_1`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    z3 t ^ 1 * (z3 t - 1) ^ 1 * z4 t ^ 1 * (z4 t - 1) ^ 1 = z3 t ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 2 := by
  simp only [minpoly] at ht
  simp only [z3, z4, z5]
  linear_combination (0) * ht

end K101

/-! ### `7_5` — 7 tetrahedra, shape field of degree 8

Minimal polynomial `x^8 + x^7 - 4*x^6 - 6*x^5 - x^4 + 2*x^3 + 4*x^2 + 3*x + 1`. -/

namespace K75

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 8 + 1 * t ^ 7 + (-4) * t ^ 6 + (-6) * t ^ 5 + (-1) * t ^ 4 + 2 * t ^ 3 + 4 * t ^ 2 + 3 * t + 1

/-- Shape `z0` of `7_5`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `7_5`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := 1 * t ^ 7 + 2 * t ^ 6 + (-2) * t ^ 5 + (-8) * t ^ 4 + (-9) * t ^ 3 + (-7) * t ^ 2 + (-3) * t

/-- Shape `z2` of `7_5`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (1 / 4) * t ^ 7 + (1 / 2) * t ^ 6 + (-3 / 4) * t ^ 5 + (-11 / 4) * t ^ 4 + (-5 / 4) * t ^ 3 + 1 * t ^ 2 + (5 / 4) * t + 2

/-- Shape `z3` of `7_5`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-1 / 4) * t ^ 7 + (3 / 4) * t ^ 6 + (5 / 4) * t ^ 5 + (-3) * t ^ 4 + (-5 / 2) * t ^ 3 + (7 / 4) * t ^ 2 + (3 / 4) * t + (9 / 4)

/-- Shape `z4` of `7_5`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (3 / 4) * t ^ 7 + (1 / 2) * t ^ 6 + (-13 / 4) * t ^ 5 + (-13 / 4) * t ^ 4 + (1 / 4) * t ^ 3 + 1 * t ^ 2 + (15 / 4) * t + 2

/-- Shape `z5` of `7_5`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := (3 / 4) * t ^ 7 + (1 / 2) * t ^ 6 + (-13 / 4) * t ^ 5 + (-13 / 4) * t ^ 4 + (1 / 4) * t ^ 3 + 1 * t ^ 2 + (11 / 4) * t + 2

/-- Shape `z6` of `7_5`, as an element of `ℚ(θ)`. -/
noncomputable def z6 (t : ℂ) : ℂ := (-1 / 4) * t ^ 7 + (-1 / 2) * t ^ 6 + (3 / 4) * t ^ 5 + (7 / 4) * t ^ 4 + (5 / 4) * t ^ 3 + 2 * t ^ 2 + (7 / 4) * t + 1

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 7 + (-1) * t ^ 6 + 4 * t ^ 5 + 6 * t ^ 4 + 1 * t ^ 3 + (-2) * t ^ 2 + (-4) * t + (-3)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 7 + 2 * t ^ 6 + (-2) * t ^ 5 + (-8) * t ^ 4 + (-9) * t ^ 3 + (-7) * t ^ 2 + (-3) * t) * h + (1) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 7 + 1 * t ^ 6 + (-4) * t ^ 5 + (-6) * t ^ 4 + (-1) * t ^ 3 + 2 * t ^ 2 + 4 * t + 4) * h + (1 * t ^ 6 + 2 * t ^ 5 + (-2) * t ^ 4 + (-8) * t ^ 3 + (-9) * t ^ 2 + (-7) * t + (-3)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 7 + (1 / 2) * t ^ 6 + (-3 / 4) * t ^ 5 + (-7 / 4) * t ^ 4 + (-5 / 4) * t ^ 3 + (-2) * t ^ 2 + (-7 / 4) * t) * h + ((-1 / 16) * t ^ 6 + (-3 / 16) * t ^ 5 + (1 / 16) * t ^ 4 + (11 / 16) * t ^ 3 + (11 / 16) * t ^ 2 + (1 / 2) * t + 1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 4) * t ^ 7 + (-3 / 4) * t ^ 6 + (5 / 4) * t ^ 5 + (7 / 2) * t ^ 4 + (-7 / 4) * t ^ 2 + (-1 / 4) * t + (-5 / 4)) * h + ((-1 / 16) * t ^ 6 + (-1 / 4) * t ^ 5 + (1 / 8) * t ^ 4 + (5 / 4) * t ^ 3 + (7 / 8) * t ^ 2 + (-17 / 16) * t + (-1 / 4)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 6 + (-1 / 2) * t ^ 5 + (-3 / 4) * t ^ 4 + (5 / 4) * t ^ 3 + (3 / 4) * t ^ 2 + (1 / 4)) * h + ((1 / 16) * t ^ 5 + (-3 / 8) * t ^ 4 + (1 / 2) * t ^ 3 + (5 / 8) * t ^ 2 + (-3 / 2) * t + (7 / 16)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 2) * t ^ 7 + (-3 / 4) * t ^ 6 + 2 * t ^ 5 + (15 / 4) * t ^ 4 + (3 / 4) * t ^ 3 + (-1 / 4) * t ^ 2 + (-1 / 2) * t + (-3 / 4)) * h + ((1 / 8) * t ^ 6 + (-5 / 16) * t ^ 5 + (-7 / 8) * t ^ 4 + (3 / 2) * t ^ 3 + (15 / 8) * t ^ 2 + (-11 / 8) * t + (1 / 16)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-3 / 4) * t ^ 7 + (-1 / 2) * t ^ 6 + (13 / 4) * t ^ 5 + (13 / 4) * t ^ 4 + (-1 / 4) * t ^ 3 + (-1) * t ^ 2 + (-11 / 4) * t + (-1)) * h + ((9 / 16) * t ^ 6 + (3 / 16) * t ^ 5 + (-41 / 16) * t ^ 4 + (-23 / 16) * t ^ 3 + (9 / 16) * t ^ 2 + (1 / 4) * t + 3) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((3 / 4) * t ^ 7 + (3 / 4) * t ^ 6 + (-11 / 4) * t ^ 5 + (-4) * t ^ 4 + (-3 / 2) * t ^ 3 + (-1 / 4) * t ^ 2 + (7 / 4) * t + (5 / 4)) * h + ((9 / 16) * t ^ 6 + (3 / 8) * t ^ 5 + (-9 / 4) * t ^ 4 + (-17 / 8) * t ^ 3 + (-1 / 2) * t ^ 2 + (-5 / 16) * t + (9 / 4)) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-3 / 4) * t ^ 7 + (-3 / 4) * t ^ 6 + (11 / 4) * t ^ 5 + 4 * t ^ 4 + (3 / 2) * t ^ 3 + (1 / 4) * t ^ 2 + (-7 / 4) * t + (-1 / 4)) * h + ((9 / 16) * t ^ 6 + (3 / 8) * t ^ 5 + (-9 / 4) * t ^ 4 + (-17 / 8) * t ^ 3 + (-1 / 2) * t ^ 2 + (-5 / 16) * t + (3 / 2)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((3 / 4) * t ^ 7 + (1 / 2) * t ^ 6 + (-13 / 4) * t ^ 5 + (-13 / 4) * t ^ 4 + (1 / 4) * t ^ 3 + 1 * t ^ 2 + (15 / 4) * t + 2) * h + ((9 / 16) * t ^ 6 + (3 / 16) * t ^ 5 + (-41 / 16) * t ^ 4 + (-23 / 16) * t ^ 3 + (9 / 16) * t ^ 2 + (1 / 4) * t + 3) * ht
  exact absurd this one_ne_zero

theorem z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 7 + (3 / 4) * t ^ 6 + (-5 / 4) * t ^ 5 + (-7 / 2) * t ^ 4 + (7 / 4) * t ^ 2 + (1 / 4) * t + (9 / 4)) * h + ((1 / 16) * t ^ 6 + (1 / 4) * t ^ 5 + (-1 / 8) * t ^ 4 + (-1) * t ^ 3 + (-3 / 8) * t ^ 2 + (-7 / 16) * t + (-5 / 4)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 4) * t ^ 7 + (1 / 2) * t ^ 6 + (-3 / 4) * t ^ 5 + (-11 / 4) * t ^ 4 + (-5 / 4) * t ^ 3 + 1 * t ^ 2 + (5 / 4) * t + 2) * h + ((-1 / 16) * t ^ 6 + (-3 / 16) * t ^ 5 + (1 / 16) * t ^ 4 + (11 / 16) * t ^ 3 + (11 / 16) * t ^ 2 + (1 / 2) * t + 1) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `7_5`, exponents `[1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z6 t ^ 1 = z0 t ^ 1 * (1 - z2 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z6]
  linear_combination ((-1 / 16) * t ^ 15 + (-1 / 4) * t ^ 14 + (1 / 8) * t ^ 13 + (15 / 8) * t ^ 12 + (37 / 16) * t ^ 11 + (-15 / 8) * t ^ 10 + (-97 / 16) * t ^ 9 + (-51 / 8) * t ^ 8 + (-49 / 8) * t ^ 7 + (-47 / 16) * t ^ 6 + (33 / 16) * t ^ 5 + (77 / 16) * t ^ 4 + (13 / 2) * t ^ 3 + (17 / 4) * t ^ 2 + 1 * t) * ht

/-- **Edge 1** of `7_5`, exponents `[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z4 t - 1) ^ 1 = (1 - z0 t) ^ 1 * (1 - z1 t) ^ 1 * z1 t ^ 1 * (1 - z4 t) ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z4, z5]
  linear_combination ((-27 / 64) * t ^ 28 + (-27 / 16) * t ^ 27 + (261 / 64) * t ^ 26 + (1765 / 64) * t ^ 25 + (743 / 64) * t ^ 24 + (-9359 / 64) * t ^ 23 + (-16747 / 64) * t ^ 22 + (4549 / 32) * t ^ 21 + (15121 / 16) * t ^ 20 + (2137 / 2) * t ^ 19 + (-21445 / 64) * t ^ 18 + (-82029 / 32) * t ^ 17 + (-215339 / 64) * t ^ 16 + (-69749 / 64) * t ^ 15 + (91795 / 32) * t ^ 14 + (334033 / 64) * t ^ 13 + (255159 / 64) * t ^ 12 + (5695 / 32) * t ^ 11 + (-49895 / 16) * t ^ 10 + (-121707 / 32) * t ^ 9 + (-73131 / 32) * t ^ 8 + (-8231 / 32) * t ^ 7 + (28397 / 32) * t ^ 6 + (3933 / 4) * t ^ 5 + (38385 / 64) * t ^ 4 + (459 / 2) * t ^ 3 + (217 / 4) * t ^ 2 + (9 / 4) * t + (-1)) * ht

/-- **Edge 2** of `7_5`, exponents `[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z5 t - 1) ^ 1 * z6 t ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z4, z5, z6]
  linear_combination ((-9 / 64) * t ^ 21 + (3 / 32) * t ^ 20 + (161 / 64) * t ^ 19 + (21 / 64) * t ^ 18 + (-137 / 8) * t ^ 17 + (-57 / 4) * t ^ 16 + (2975 / 64) * t ^ 15 + (2477 / 32) * t ^ 14 + (-9 / 2) * t ^ 13 + (-7761 / 64) * t ^ 12 + (-5291 / 32) * t ^ 11 + (-4265 / 64) * t ^ 10 + (1779 / 16) * t ^ 9 + (2949 / 16) * t ^ 8 + (8141 / 64) * t ^ 7 + (1171 / 64) * t ^ 6 + (-957 / 16) * t ^ 5 + (-4083 / 64) * t ^ 4 + (-2485 / 64) * t ^ 3 + (-97 / 8) * t ^ 2 + (-3) * t + (-1)) * ht

/-- **Edge 3** of `7_5`, exponents `[0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    z2 t ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z2 t ^ 1 * z3 t ^ 1 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z6]
  linear_combination ((1 / 256) * t ^ 20 + (-3 / 256) * t ^ 19 + (-5 / 64) * t ^ 18 + (21 / 128) * t ^ 17 + (211 / 256) * t ^ 16 + (-55 / 64) * t ^ 15 + (-643 / 128) * t ^ 14 + (275 / 256) * t ^ 13 + (4429 / 256) * t ^ 12 + (863 / 128) * t ^ 11 + (-7663 / 256) * t ^ 10 + (-7087 / 256) * t ^ 9 + (1731 / 128) * t ^ 8 + (2247 / 64) * t ^ 7 + (6771 / 256) * t ^ 6 + (-1011 / 128) * t ^ 5 + (-983 / 32) * t ^ 4 + (-3389 / 256) * t ^ 3 + (469 / 256) * t ^ 2 + (435 / 64) * t + (45 / 8)) * ht

/-- **Edge 4** of `7_5`, exponents `[1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z1 t - 1) ^ 1 * z3 t ^ 1 = z1 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z5]
  linear_combination ((-1 / 4) * t ^ 7 + (5 / 4) * t ^ 6 + 3 * t ^ 5 + (-13 / 4) * t ^ 4 + (-9) * t ^ 3 + (-7) * t ^ 2 + (-21 / 4) * t) * ht

/-- **Edge 5** of `7_5`, exponents `[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z2 t - 1) ^ 1 * z4 t ^ 1 * (z4 t - 1) ^ 1 * z5 t ^ 1 * (z6 t - 1) ^ 1 = z2 t ^ 1 * z4 t ^ 1 * (1 - z6 t) ^ 1 * z6 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z4, z5, z6]
  linear_combination ((-27 / 1024) * t ^ 34 + (-189 / 1024) * t ^ 33 + (-9 / 256) * t ^ 32 + (2953 / 1024) * t ^ 31 + (3631 / 512) * t ^ 30 + (-5181 / 512) * t ^ 29 + (-66557 / 1024) * t ^ 28 + (-59687 / 1024) * t ^ 27 + (181155 / 1024) * t ^ 26 + (246537 / 512) * t ^ 25 + (267519 / 1024) * t ^ 24 + (-776497 / 1024) * t ^ 23 + (-59039 / 32) * t ^ 22 + (-842821 / 512) * t ^ 21 + (665543 / 1024) * t ^ 20 + (4122127 / 1024) * t ^ 19 + (1464879 / 256) * t ^ 18 + (458175 / 128) * t ^ 17 + (-1901073 / 1024) * t ^ 16 + (-7574863 / 1024) * t ^ 15 + (-9368653 / 1024) * t ^ 14 + (-5821099 / 1024) * t ^ 13 + (646887 / 1024) * t ^ 12 + (371647 / 64) * t ^ 11 + (3631891 / 512) * t ^ 10 + (2398673 / 512) * t ^ 9 + (279401 / 256) * t ^ 8 + (-705677 / 512) * t ^ 7 + (-2056167 / 1024) * t ^ 6 + (-362561 / 256) * t ^ 5 + (-161237 / 256) * t ^ 4 + (-10411 / 64) * t ^ 3 + (-17 / 4) * t ^ 2 + 7 * t) * ht

/-- **Edge 6** of `7_5`, exponents `[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1]`, denominators cleared. -/
theorem edge_6 {t : ℂ} (ht : minpoly t = 0) :
    (z3 t - 1) ^ 1 * z4 t ^ 1 * z5 t ^ 1 * (z5 t - 1) ^ 1 * (z6 t - 1) ^ 1 = (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * z5 t ^ 1 * z6 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z2, z3, z4, z5, z6]
  linear_combination ((15 / 512) * t ^ 27 + (-7 / 1024) * t ^ 26 + (-359 / 512) * t ^ 25 + (-219 / 1024) * t ^ 24 + (6895 / 1024) * t ^ 23 + (83 / 16) * t ^ 22 + (-32301 / 1024) * t ^ 21 + (-39207 / 1024) * t ^ 20 + (33391 / 512) * t ^ 19 + (61029 / 512) * t ^ 18 + (-5671 / 1024) * t ^ 17 + (-112115 / 1024) * t ^ 16 + (-37781 / 256) * t ^ 15 + (-86411 / 512) * t ^ 14 + (12753 / 1024) * t ^ 13 + (249737 / 1024) * t ^ 12 + (73281 / 256) * t ^ 11 + (13119 / 64) * t ^ 10 + (-57319 / 1024) * t ^ 9 + (-296417 / 1024) * t ^ 8 + (-30381 / 128) * t ^ 7 + (-89293 / 1024) * t ^ 6 + (56137 / 1024) * t ^ 5 + (58653 / 512) * t ^ 4 + (58631 / 1024) * t ^ 3 + (1461 / 128) * t ^ 2 + (-271 / 64) * t + (-45 / 8)) * ht

end K75

/-! ### `8_2` — 6 tetrahedra, shape field of degree 8

Minimal polynomial `x^8 - 15*x^7 + 91*x^6 - 294*x^5 + 575*x^4 - 718*x^3 + 562*x^2 - 252*x + 49`. -/

namespace K82

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 8 + (-15) * t ^ 7 + 91 * t ^ 6 + (-294) * t ^ 5 + 575 * t ^ 4 + (-718) * t ^ 3 + 562 * t ^ 2 + (-252) * t + 49

/-- Shape `z0` of `8_2`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `8_2`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (-2584 / 26509) * t ^ 7 + (34287 / 26509) * t ^ 6 + (-24672 / 3787) * t ^ 5 + (8557 / 541) * t ^ 4 + (-547352 / 26509) * t ^ 3 + (376086 / 26509) * t ^ 2 + (-85836 / 26509) * t + (718 / 3787)

/-- Shape `z2` of `8_2`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (-83035 / 1086869) * t ^ 7 + (1154714 / 1086869) * t ^ 6 + (-894562 / 155267) * t ^ 5 + (350684 / 22181) * t ^ 4 + (-27256755 / 1086869) * t ^ 3 + (26349047 / 1086869) * t ^ 2 + (-14338403 / 1086869) * t + (599778 / 155267)

/-- Shape `z3` of `8_2`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (-1304 / 3787) * t ^ 7 + (18440 / 3787) * t ^ 6 + (-14633 / 541) * t ^ 5 + (41453 / 541) * t ^ 4 + (-474924 / 3787) * t ^ 3 + (469582 / 3787) * t ^ 2 + (-257968 / 3787) * t + (9221 / 541)

/-- Shape `z4` of `8_2`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (104 / 3787) * t ^ 7 + (-2400 / 3787) * t ^ 6 + (2956 / 541) * t ^ 5 + (-12596 / 541) * t ^ 4 + (205365 / 3787) * t ^ 3 + (-278890 / 3787) * t ^ 2 + (213897 / 3787) * t + (-10261 / 541)

/-- Shape `z5` of `8_2`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := (-29217 / 155267) * t ^ 7 + (406818 / 155267) * t ^ 6 + (-315842 / 22181) * t ^ 5 + (867732 / 22181) * t ^ 4 + (-9562174 / 155267) * t ^ 3 + (8953199 / 155267) * t ^ 2 + (-4480495 / 155267) * t + (136113 / 22181)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 49) * t ^ 7 + (15 / 49) * t ^ 6 + (-13 / 7) * t ^ 5 + 6 * t ^ 4 + (-575 / 49) * t ^ 3 + (718 / 49) * t ^ 2 + (-562 / 49) * t + (36 / 7)) * h + ((1 / 49)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 7 + 14 * t ^ 6 + (-77) * t ^ 5 + 217 * t ^ 4 + (-358) * t ^ 3 + 360 * t ^ 2 + (-202) * t + 50) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((201 / 3787) * t ^ 7 + (-2308 / 3787) * t ^ 6 + (1281 / 541) * t ^ 5 + (-1643 / 541) * t ^ 4 + (-7100 / 3787) * t ^ 3 + (39747 / 3787) * t ^ 2 + (-46687 / 3787) * t + (3312 / 541)) * h + ((519384 / 100389583) * t ^ 6 + (-5064799 / 100389583) * t ^ 5 + (1968957 / 14341369) * t ^ 4 + (41036 / 14341369) * t ^ 3 + (-35242384 / 100389583) * t ^ 2 + (43708162 / 100389583) * t + (-329249 / 100389583)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-3736 / 3787) * t ^ 7 + (52715 / 3787) * t ^ 6 + (-41768 / 541) * t ^ 5 + (118482 / 541) * t ^ 4 + (-1367665 / 3787) * t ^ 3 + (1368205 / 3787) * t ^ 2 + (-761785 / 3787) * t + (26445 / 541)) * h + ((9653824 / 100389583) * t ^ 6 + (-119504432 / 100389583) * t ^ 5 + (76728067 / 14341369) * t ^ 4 + (-21812117 / 2048767) * t ^ 3 + (1020298487 / 100389583) * t ^ 2 + (-397144089 / 100389583) * t + (-79110938 / 100389583)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((639 / 3787) * t ^ 7 + (-8920 / 3787) * t ^ 6 + (6947 / 541) * t ^ 5 + (-19152 / 541) * t ^ 4 + (211318 / 3787) * t ^ 3 + (-198983 / 3787) * t ^ 2 + (103667 / 3787) * t + (-2584 / 541)) * h + ((53059365 / 4115972903) * t ^ 6 + (-682643971 / 4115972903) * t ^ 5 + (467324563 / 587996129) * t ^ 4 + (-149636236 / 83999447) * t ^ 3 + (8683143037 / 4115972903) * t ^ 2 + (-5772841502 / 4115972903) * t + (1633825799 / 4115972903)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-4251 / 3787) * t ^ 7 + (60230 / 3787) * t ^ 6 + (-48062 / 541) * t ^ 5 + (138055 / 541) * t ^ 4 + (-1626452 / 3787) * t ^ 3 + (1677453 / 3787) * t ^ 2 + (-981110 / 3787) * t + (38081 / 541)) * h + ((352981785 / 4115972903) * t ^ 6 + (-4615160489 / 4115972903) * t ^ 5 + (3250707582 / 587996129) * t ^ 4 + (-7693099184 / 587996129) * t ^ 3 + (70212014056 / 4115972903) * t ^ 2 + (-52817669955 / 4115972903) * t + (17011422838 / 4115972903)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((29217 / 155267) * t ^ 7 + (-406818 / 155267) * t ^ 6 + (315842 / 22181) * t ^ 5 + (-867732 / 22181) * t ^ 4 + (9562174 / 155267) * t ^ 3 + (-8953199 / 155267) * t ^ 2 + (4480495 / 155267) * t + (-113932 / 22181)) * h + ((38098968 / 587996129) * t ^ 6 + (-497767632 / 587996129) * t ^ 5 + (349133665 / 83999447) * t ^ 4 + (-811608256 / 83999447) * t ^ 3 + (6995043263 / 587996129) * t ^ 2 + (-4636149489 / 587996129) * t + (1062566893 / 587996129)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((104 / 3787) * t ^ 7 + (-2400 / 3787) * t ^ 6 + (2956 / 541) * t ^ 5 + (-12596 / 541) * t ^ 4 + (205365 / 3787) * t ^ 3 + (-278890 / 3787) * t ^ 2 + (213897 / 3787) * t + (-10261 / 541)) * h + ((-135616 / 14341369) * t ^ 6 + (3013120 / 14341369) * t ^ 5 + (-3479048 / 2048767) * t ^ 4 + (1901712 / 292681) * t ^ 3 + (-181244012 / 14341369) * t ^ 2 + (186830692 / 14341369) * t + (-88772799 / 14341369)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1304 / 3787) * t ^ 7 + (-18440 / 3787) * t ^ 6 + (14633 / 541) * t ^ 5 + (-41453 / 541) * t ^ 4 + (474924 / 3787) * t ^ 3 + (-469582 / 3787) * t ^ 2 + (257968 / 3787) * t + (-8680 / 541)) * h + ((-135616 / 14341369) * t ^ 6 + (3013120 / 14341369) * t ^ 5 + (-3479048 / 2048767) * t ^ 4 + (1901712 / 292681) * t ^ 3 + (-181244012 / 14341369) * t ^ 2 + (186830692 / 14341369) * t + (-88772799 / 14341369)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-29217 / 155267) * t ^ 7 + (406818 / 155267) * t ^ 6 + (-315842 / 22181) * t ^ 5 + (867732 / 22181) * t ^ 4 + (-9562174 / 155267) * t ^ 3 + (8953199 / 155267) * t ^ 2 + (-4480495 / 155267) * t + (136113 / 22181)) * h + ((-3038568 / 587996129) * t ^ 6 + (66851352 / 587996129) * t ^ 5 + (-75939196 / 83999447) * t ^ 4 + (283060896 / 83999447) * t ^ 3 + (-3694152225 / 587996129) * t ^ 2 + (3573418853 / 587996129) * t + (-1458292705 / 587996129)) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-104 / 3787) * t ^ 7 + (2400 / 3787) * t ^ 6 + (-2956 / 541) * t ^ 5 + (12596 / 541) * t ^ 4 + (-205365 / 3787) * t ^ 3 + (278890 / 3787) * t ^ 2 + (-213897 / 3787) * t + (10802 / 541)) * h + ((-3038568 / 587996129) * t ^ 6 + (66851352 / 587996129) * t ^ 5 + (-75939196 / 83999447) * t ^ 4 + (283060896 / 83999447) * t ^ 3 + (-3694152225 / 587996129) * t ^ 2 + (3573418853 / 587996129) * t + (-1458292705 / 587996129)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1304 / 3787) * t ^ 7 + (18440 / 3787) * t ^ 6 + (-14633 / 541) * t ^ 5 + (41453 / 541) * t ^ 4 + (-474924 / 3787) * t ^ 3 + (469582 / 3787) * t ^ 2 + (-257968 / 3787) * t + (9221 / 541)) * h + ((38098968 / 587996129) * t ^ 6 + (-497767632 / 587996129) * t ^ 5 + (349133665 / 83999447) * t ^ 4 + (-811608256 / 83999447) * t ^ 3 + (6995043263 / 587996129) * t ^ 2 + (-4636149489 / 587996129) * t + (1062566893 / 587996129)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `8_2`, exponents `[1, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 2 * (z3 t - 1) ^ 1 = z0 t ^ 2 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * z3 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3]
  linear_combination ((279789421760 / 109110325685627) * t ^ 15 + (-7363055902584 / 109110325685627) * t ^ 14 + (85018501530216 / 109110325685627) * t ^ 13 + (-81163752088397 / 15587189383661) * t ^ 12 + (2449320971199148 / 109110325685627) * t ^ 11 + (-7214502936370176 / 109110325685627) * t ^ 10 + (15027188623429909 / 109110325685627) * t ^ 9 + (-22523554894199829 / 109110325685627) * t ^ 8 + (24258938265778463 / 109110325685627) * t ^ 7 + (-18276980745134078 / 109110325685627) * t ^ 6 + (8958327529451130 / 109110325685627) * t ^ 5 + (-2322464444139571 / 109110325685627) * t ^ 4 + (49810202404467 / 109110325685627) * t ^ 3 + (6950692527663 / 15587189383661) * t ^ 2 + (1240 / 3787) * t) * ht

/-- **Edge 1** of `8_2`, exponents `[0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z2 t - 1) ^ 1 = (1 - z0 t) ^ 2 * z1 t ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2]
  linear_combination ((-214562440 / 28811810321) * t ^ 8 + (3041490301 / 28811810321) * t ^ 7 + (-405538061 / 702727081) * t ^ 6 + (6329708725 / 4115972903) * t ^ 5 + (-62112829486 / 28811810321) * t ^ 4 + (45516388133 / 28811810321) * t ^ 3 + (-13449590031 / 28811810321) * t ^ 2 + (1291654823 / 28811810321) * t + (-67707 / 1086869)) * ht

/-- **Edge 2** of `8_2`, exponents `[1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * (z3 t - 1) ^ 1 * z4 t ^ 1 * (z4 t - 1) ^ 1 * (z5 t - 1) ^ 1 = z3 t ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination ((88416555104637726720 / 242960472882114185053762921) * t ^ 35 + (-7638684872892557372928 / 242960472882114185053762921) * t ^ 34 + (312436358872247333922304 / 242960472882114185053762921) * t ^ 33 + (-8064572293727159520281280 / 242960472882114185053762921) * t ^ 32 + (147730252032998795378555520 / 242960472882114185053762921) * t ^ 31 + (-2047662527901168008346848320 / 242960472882114185053762921) * t ^ 30 + (22359051435651084632748127744 / 242960472882114185053762921) * t ^ 29 + (-197717577961964807685883978464 / 242960472882114185053762921) * t ^ 28 + (1444543161510558603097660560768 / 242960472882114185053762921) * t ^ 27 + (-8852729026992210881078008711984 / 242960472882114185053762921) * t ^ 26 + (46046195749383667434342177153560 / 242960472882114185053762921) * t ^ 25 + (-205180724234622894377387964389035 / 242960472882114185053762921) * t ^ 24 + (789164459837019436850611335128370 / 242960472882114185053762921) * t ^ 23 + (-2635852331247383275285798325057800 / 242960472882114185053762921) * t ^ 22 + (7682678953439507408342437173772856 / 242960472882114185053762921) * t ^ 21 + (-19615909616218083840663863665393528 / 242960472882114185053762921) * t ^ 20 + (44001541571079607781777327483227538 / 242960472882114185053762921) * t ^ 19 + (-86889477055335027011230278411156322 / 242960472882114185053762921) * t ^ 18 + (151219279095832197301712630485792142 / 242960472882114185053762921) * t ^ 17 + (-232010714093403280655102402370351010 / 242960472882114185053762921) * t ^ 16 + (313610758473216564306797537901138214 / 242960472882114185053762921) * t ^ 15 + (-7609370778987712641665228225084415 / 4958376997594167041913529) * t ^ 14 + (388843840311963464733821074364951953 / 242960472882114185053762921) * t ^ 13 + (-354266147096190988961078426373664775 / 242960472882114185053762921) * t ^ 12 + (280408309316634688775892679705381083 / 242960472882114185053762921) * t ^ 11 + (-3905976432746911363831105062707314 / 4958376997594167041913529) * t ^ 10 + (111550531158464891637186411182216516 / 242960472882114185053762921) * t ^ 9 + (-54807480485622723805763436770129355 / 242960472882114185053762921) * t ^ 8 + (22321267862366532480423597279754884 / 242960472882114185053762921) * t ^ 7 + (-7372619456011257391691716484035139 / 242960472882114185053762921) * t ^ 6 + (1921701351654976411977111430988491 / 242960472882114185053762921) * t ^ 5 + (-7832529353085396456041200491218 / 4958376997594167041913529) * t ^ 4 + (1182353786205893211411573531356 / 4958376997594167041913529) * t ^ 3 + (-2897650185872266405005892433 / 101191367297840143712521) * t ^ 2 + (43274219610093968288935439 / 14455909613977163387503) * t + (-209611447458311028 / 1007986728043687)) * ht

/-- **Edge 3** of `8_2`, exponents `[0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z1 t - 1) ^ 1 * z3 t ^ 1 * z5 t ^ 1 = z1 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4, z5]
  linear_combination ((4597772306432 / 8432669456560601) * t ^ 20 + (-1233903541699392 / 59028686195924207) * t ^ 19 + (21573056652527528 / 59028686195924207) * t ^ 18 + (-227720404888272920 / 59028686195924207) * t ^ 17 + (1619554895124590385 / 59028686195924207) * t ^ 16 + (-8196704903368364884 / 59028686195924207) * t ^ 15 + (30340160412206213883 / 59028686195924207) * t ^ 14 + (-82683068863272089014 / 59028686195924207) * t ^ 13 + (162340326717736876972 / 59028686195924207) * t ^ 12 + (-208519631552883031701 / 59028686195924207) * t ^ 11 + (94310142102811234927 / 59028686195924207) * t ^ 10 + (280112163250750877031 / 59028686195924207) * t ^ 9 + (-832664976652467847720 / 59028686195924207) * t ^ 8 + (1274280857883607293169 / 59028686195924207) * t ^ 7 + (-1328481396080782899600 / 59028686195924207) * t ^ 6 + (993341659916147775431 / 59028686195924207) * t ^ 5 + (-529609646423261527933 / 59028686195924207) * t ^ 4 + (192904044346300093402 / 59028686195924207) * t ^ 3 + (-1071518821293171432 / 1439724053559127) * t ^ 2 + (5269491932866609998 / 59028686195924207) * t + (-32690433430201646 / 8432669456560601)) * ht

/-- **Edge 4** of `8_2`, exponents `[0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z2 t ^ 1 * z3 t ^ 1 * (z4 t - 1) ^ 1 * z5 t ^ 1 = (1 - z1 t) ^ 1 * (1 - z4 t) ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4, z5]
  linear_combination ((-295529495007552 / 2420176134032892487) * t ^ 20 + (14512950418485312 / 2420176134032892487) * t ^ 19 + (-324156014600138920 / 2420176134032892487) * t ^ 18 + (4388506460942714160 / 2420176134032892487) * t ^ 17 + (-40461398387837734212 / 2420176134032892487) * t ^ 16 + (270580357260989335788 / 2420176134032892487) * t ^ 15 + (-1365224670664171345005 / 2420176134032892487) * t ^ 14 + (5339773706888842133384 / 2420176134032892487) * t ^ 13 + (-16514136039223075212024 / 2420176134032892487) * t ^ 12 + (40994572602524372831096 / 2420176134032892487) * t ^ 11 + (-11803701331471487076908 / 345739447718984641) * t ^ 10 + (136383033307637304061247 / 2420176134032892487) * t ^ 9 + (-185488786906389308205799 / 2420176134032892487) * t ^ 8 + (208642118421869873210060 / 2420176134032892487) * t ^ 7 + (-194237435185777528255870 / 2420176134032892487) * t ^ 6 + (21293366813113019926587 / 345739447718984641) * t ^ 5 + (-93074181875416684723644 / 2420176134032892487) * t ^ 4 + (45929600106672216957518 / 2420176134032892487) * t ^ 3 + (-16874725096843940201828 / 2420176134032892487) * t ^ 2 + (83323640386064450250 / 49391349674140663) * t + (-9720518139437707404 / 49391349674140663)) * ht

/-- **Edge 5** of `8_2`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t - 1) ^ 1 * z4 t ^ 1 * (z5 t - 1) ^ 1 = z2 t ^ 1 * (1 - z3 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z2, z3, z4, z5]
  linear_combination ((-2911240314000 / 639074764730101) * t ^ 13 + (76265868035400 / 639074764730101) * t ^ 12 + (-875923891291425 / 639074764730101) * t ^ 11 + (830896586579026 / 91296394961443) * t ^ 10 + (-24881706404469412 / 639074764730101) * t ^ 9 + (72598208022894300 / 639074764730101) * t ^ 8 + (-149422073214733521 / 639074764730101) * t ^ 7 + (220500317319175357 / 639074764730101) * t ^ 6 + (-232792925994253419 / 639074764730101) * t ^ 5 + (172106712616930879 / 639074764730101) * t ^ 4 + (-85597453289079350 / 639074764730101) * t ^ 3 + (668896099923925 / 15587189383661) * t ^ 2 + (-6492405500869899 / 639074764730101) * t + (26993693722964 / 13042342137349)) * ht

end K82

/-! ### `8_3` — 6 tetrahedra, shape field of degree 8

Minimal polynomial `x^8 - 7*x^7 + 17*x^6 - 14*x^5 - x^4 - 2*x^3 + 6*x^2 + 4*x + 1`. -/

namespace K83

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 8 + (-7) * t ^ 7 + 17 * t ^ 6 + (-14) * t ^ 5 + (-1) * t ^ 4 + (-2) * t ^ 3 + 6 * t ^ 2 + 4 * t + 1

/-- Shape `z0` of `8_3`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `8_3`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (2 / 5) * t ^ 7 + (-13 / 5) * t ^ 6 + 6 * t ^ 5 + (-28 / 5) * t ^ 4 + (14 / 5) * t ^ 3 + (-17 / 5) * t ^ 2 + (11 / 5) * t + (1 / 5)

/-- Shape `z2` of `8_3`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (-1) * t ^ 2 + 1 * t + 1

/-- Shape `z3` of `8_3`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (1 / 5) * t ^ 7 + (-6 / 5) * t ^ 6 + (11 / 5) * t ^ 5 + (-3 / 5) * t ^ 4 + (-4 / 5) * t ^ 3 + (-6 / 5) * t ^ 2 + 1 * t + (4 / 5)

/-- Shape `z4` of `8_3`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (-1) * t ^ 7 + 7 * t ^ 6 + (-18) * t ^ 5 + 20 * t ^ 4 + (-10) * t ^ 3 + 6 * t ^ 2 + (-4) * t + 1

/-- Shape `z5` of `8_3`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := (2 / 5) * t ^ 7 + (-13 / 5) * t ^ 6 + 6 * t ^ 5 + (-23 / 5) * t ^ 4 + (-6 / 5) * t ^ 3 + (3 / 5) * t ^ 2 + (11 / 5) * t + (11 / 5)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 7 + 7 * t ^ 6 + (-17) * t ^ 5 + 14 * t ^ 4 + 1 * t ^ 3 + 2 * t ^ 2 + (-6) * t + (-4)) * h + (1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 5) * t ^ 7 + (-6 / 5) * t ^ 6 + (11 / 5) * t ^ 5 + (-3 / 5) * t ^ 4 + (-4 / 5) * t ^ 3 + (-6 / 5) * t ^ 2 + (4 / 5)) * h + ((1 / 5)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 7 + 6 * t ^ 6 + (-12) * t ^ 5 + 7 * t ^ 4 + 1 * t ^ 3 + 3 * t ^ 2 + (-2) * t + (-1)) * h + ((2 / 5) * t ^ 6 + (-11 / 5) * t ^ 5 + (21 / 5) * t ^ 4 + (-16 / 5) * t ^ 3 + 2 * t ^ 2 + (-11 / 5) * t + (6 / 5)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 5) * t ^ 7 + (-6 / 5) * t ^ 6 + (11 / 5) * t ^ 5 + (-3 / 5) * t ^ 4 + (-4 / 5) * t ^ 3 + (-6 / 5) * t ^ 2 + 1 * t + (4 / 5)) * h + ((2 / 25) * t ^ 6 + (-11 / 25) * t ^ 5 + (19 / 25) * t ^ 4 + (-9 / 25) * t ^ 3 + (1 / 5) * t ^ 2 + (-12 / 25) * t + (9 / 25)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1 / 5) * t ^ 7 + (-4 / 5) * t ^ 6 + (16 / 5) * t ^ 4 + (-13 / 5) * t ^ 3 + (-1 / 5) * t ^ 2 + (-12 / 5) * t + (3 / 5)) * h + ((1 / 5) * t + (2 / 5)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((4 / 5) * t ^ 7 + (-29 / 5) * t ^ 6 + (74 / 5) * t ^ 5 + (-67 / 5) * t ^ 4 + (-1 / 5) * t ^ 3 + (-4 / 5) * t ^ 2 + 6 * t + (16 / 5)) * h + ((-4 / 5) * t + 1) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-2 / 5) * t ^ 7 + (13 / 5) * t ^ 6 + (-6) * t ^ 5 + (28 / 5) * t ^ 4 + (-14 / 5) * t ^ 3 + (17 / 5) * t ^ 2 + (-11 / 5) * t + (4 / 5)) * h + ((2 / 25) * t ^ 6 + (-11 / 25) * t ^ 5 + (19 / 25) * t ^ 4 + (-9 / 25) * t ^ 3 + (1 / 5) * t ^ 2 + (-12 / 25) * t + (9 / 25)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 7 + (-6) * t ^ 6 + 12 * t ^ 5 + (-7) * t ^ 4 + (-1) * t ^ 3 + (-3) * t ^ 2 + 2 * t + 2) * h + ((1 / 5) * t ^ 6 + (-1) * t ^ 5 + (7 / 5) * t ^ 4 + (-1 / 5) * t ^ 2 + (-4 / 5) * t + (3 / 5)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((2 / 5) * t ^ 7 + (-13 / 5) * t ^ 6 + 6 * t ^ 5 + (-28 / 5) * t ^ 4 + (9 / 5) * t ^ 3 + (-2 / 5) * t ^ 2 + (1 / 5) * t + (1 / 5)) * h + ((2 / 5) * t ^ 6 + (-13 / 5) * t ^ 5 + (32 / 5) * t ^ 4 + (-39 / 5) * t ^ 3 + (28 / 5) * t ^ 2 + (-13 / 5) * t + (4 / 5)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-3 / 5) * t ^ 7 + (18 / 5) * t ^ 6 + (-38 / 5) * t ^ 5 + (29 / 5) * t ^ 4 + (-3 / 5) * t ^ 3 + (3 / 5) * t ^ 2 + (-1) * t + (-2 / 5)) * h + ((3 / 5) * t ^ 6 + (-18 / 5) * t ^ 5 + (41 / 5) * t ^ 4 + (-44 / 5) * t ^ 3 + (26 / 5) * t ^ 2 + (-12 / 5) * t + 1) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 4 + 3 * t ^ 3 + (-1) * t ^ 2 + (-2) * t) * h + ((2 / 5) * t ^ 3 + (-1) * t ^ 2 + (2 / 5) * t + 1) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 4 + 4 * t ^ 3 + (-4) * t ^ 2 + (-1)) * h + ((-2 / 5) * t ^ 3 + (7 / 5) * t ^ 2 + (-7 / 5) * t + (-1 / 5)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `8_3`, exponents `[1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * z1 t ^ 1 * z2 t ^ 1 * (z3 t - 1) ^ 1 * z4 t ^ 1 = z3 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4]
  linear_combination ((2 / 25) * t ^ 16 + (-27 / 25) * t ^ 15 + (31 / 5) * t ^ 14 + (-487 / 25) * t ^ 13 + (898 / 25) * t ^ 12 + (-981 / 25) * t ^ 11 + (688 / 25) * t ^ 10 + (-22) * t ^ 9 + (127 / 5) * t ^ 8 + (-479 / 25) * t ^ 7 + (203 / 25) * t ^ 6 + (-123 / 25) * t ^ 5 + (84 / 25) * t ^ 4 + (3 / 5) * t ^ 3 + (-69 / 25) * t ^ 2 + (54 / 25) * t + (-4 / 5)) * ht

/-- **Edge 1** of `8_3`, exponents `[0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z1 t - 1) ^ 1 * z2 t ^ 1 * z3 t ^ 1 * (z4 t - 1) ^ 1 * z5 t ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z4 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination ((8 / 625) * t ^ 29 + (-212 / 625) * t ^ 28 + (2602 / 625) * t ^ 27 + (-783 / 25) * t ^ 26 + (100683 / 625) * t ^ 25 + (-74806 / 125) * t ^ 24 + (1034659 / 625) * t ^ 23 + (-2171718 / 625) * t ^ 22 + (140722 / 25) * t ^ 21 + (-4526659 / 625) * t ^ 20 + (4898002 / 625) * t ^ 19 + (-4799446 / 625) * t ^ 18 + (4309167 / 625) * t ^ 17 + (-3215963 / 625) * t ^ 16 + (1772764 / 625) * t ^ 15 + (-695729 / 625) * t ^ 14 + (84841 / 625) * t ^ 13 + (430393 / 625) * t ^ 12 + (-713157 / 625) * t ^ 11 + (585219 / 625) * t ^ 10 + (-3104 / 5) * t ^ 9 + (293081 / 625) * t ^ 8 + (-164668 / 625) * t ^ 7 + (45602 / 625) * t ^ 6 + (-1688 / 125) * t ^ 5 + (-2498 / 625) * t ^ 4 + (10146 / 625) * t ^ 3 + (-6551 / 625) * t ^ 2 + (1279 / 625) * t + (6 / 25)) * ht

/-- **Edge 2** of `8_3`, exponents `[0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z2 t - 1) ^ 1 * (z3 t - 1) ^ 1 = (1 - z0 t) ^ 1 * z0 t ^ 1 * (1 - z1 t) ^ 1 * z2 t ^ 1 * (1 - z3 t) ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination ((4 / 625) * t ^ 31 + (-108 / 625) * t ^ 30 + (1349 / 625) * t ^ 29 + (-10308 / 625) * t ^ 28 + (53674 / 625) * t ^ 27 + (-200732 / 625) * t ^ 26 + (553657 / 625) * t ^ 25 + (-227963 / 125) * t ^ 24 + (1762702 / 625) * t ^ 23 + (-2087977 / 625) * t ^ 22 + (2052372 / 625) * t ^ 21 + (-1998401 / 625) * t ^ 20 + (83111 / 25) * t ^ 19 + (-1886642 / 625) * t ^ 18 + (1241824 / 625) * t ^ 17 + (-687808 / 625) * t ^ 16 + (540359 / 625) * t ^ 15 + (-75261 / 125) * t ^ 14 + (24697 / 625) * t ^ 13 + (29268 / 125) * t ^ 12 + (-84521 / 625) * t ^ 11 + (56823 / 625) * t ^ 10 + (-80093 / 625) * t ^ 9 + (54463 / 625) * t ^ 8 + (-13343 / 625) * t ^ 7 + (-824 / 625) * t ^ 6 + (526 / 125) * t ^ 5 + (-3897 / 625) * t ^ 4 + (2971 / 625) * t ^ 3 + (-991 / 625) * t ^ 2 + (1 / 5) * t) * ht

/-- **Edge 3** of `8_3`, exponents `[1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 = z0 t ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3]
  linear_combination ((-1 / 5) * t ^ 3 + (1 / 5) * t ^ 2) * ht

/-- **Edge 4** of `8_3`, exponents `[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * (z5 t - 1) ^ 1 = z1 t ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z3, z4, z5]
  linear_combination ((4 / 125) * t ^ 22 + (-16 / 25) * t ^ 21 + (29 / 5) * t ^ 20 + (-3921 / 125) * t ^ 19 + (2807 / 25) * t ^ 18 + (-6983 / 25) * t ^ 17 + (62044 / 125) * t ^ 16 + (-81164 / 125) * t ^ 15 + (84022 / 125) * t ^ 14 + (-79596 / 125) * t ^ 13 + (75699 / 125) * t ^ 12 + (-64917 / 125) * t ^ 11 + (46023 / 125) * t ^ 10 + (-30996 / 125) * t ^ 9 + (20983 / 125) * t ^ 8 + (-77) * t ^ 7 + (668 / 125) * t ^ 6 + (2339 / 125) * t ^ 5 + (-2719 / 125) * t ^ 4 + (2432 / 125) * t ^ 3 + (-1561 / 125) * t ^ 2 + (118 / 25) * t + (-24 / 25)) * ht

/-- **Edge 5** of `8_3`, exponents `[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    z4 t ^ 1 * (z4 t - 1) ^ 1 * z5 t ^ 1 * (z5 t - 1) ^ 1 = (1 - z1 t) ^ 1 * z4 t ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z4, z5]
  linear_combination ((4 / 25) * t ^ 20 + (-16 / 5) * t ^ 19 + (729 / 25) * t ^ 18 + (-3987 / 25) * t ^ 17 + (14509 / 25) * t ^ 16 + (-36816 / 25) * t ^ 15 + (66467 / 25) * t ^ 14 + (-86048 / 25) * t ^ 13 + (81066 / 25) * t ^ 12 + (-59232 / 25) * t ^ 11 + (38261 / 25) * t ^ 10 + (-21199 / 25) * t ^ 9 + (5184 / 25) * t ^ 8 + (3507 / 25) * t ^ 7 + (-3714 / 25) * t ^ 6 + (586 / 5) * t ^ 5 + (-2501 / 25) * t ^ 4 + (1126 / 25) * t ^ 3 + (-342 / 25) * t ^ 2 + (33 / 5) * t + (-44 / 25)) * ht

end K83

/-! ### `7_6` — 8 tetrahedra, shape field of degree 9

Minimal polynomial `x^9 - 4*x^8 + 3*x^7 + 7*x^6 + 3*x^5 - 7*x^4 - 9*x^3 - 8*x^2 - 4*x - 1`. -/

namespace K76

/-- The shape field's minimal polynomial, as a polynomial function. -/
noncomputable def minpoly (t : ℂ) : ℂ := 1 * t ^ 9 + (-4) * t ^ 8 + 3 * t ^ 7 + 7 * t ^ 6 + 3 * t ^ 5 + (-7) * t ^ 4 + (-9) * t ^ 3 + (-8) * t ^ 2 + (-4) * t + (-1)

/-- Shape `z0` of `7_6`, as an element of `ℚ(θ)`. -/
noncomputable def z0 (t : ℂ) : ℂ := 1 * t

/-- Shape `z1` of `7_6`, as an element of `ℚ(θ)`. -/
noncomputable def z1 (t : ℂ) : ℂ := (31 / 479) * t ^ 8 + (-534 / 479) * t ^ 7 + (2072 / 479) * t ^ 6 + (-2557 / 479) * t ^ 5 + (-932 / 479) * t ^ 4 + (119 / 479) * t ^ 3 + (2180 / 479) * t ^ 2 + (1653 / 479) * t + (1562 / 479)

/-- Shape `z2` of `7_6`, as an element of `ℚ(θ)`. -/
noncomputable def z2 (t : ℂ) : ℂ := (-1 / 19) * t ^ 8 + (3 / 19) * t ^ 7 + (-7 / 19) * t ^ 5 + (-10 / 19) * t ^ 4 + (-3 / 19) * t ^ 3 + (6 / 19) * t ^ 2 + (14 / 19) * t + (18 / 19)

/-- Shape `z3` of `7_6`, as an element of `ℚ(θ)`. -/
noncomputable def z3 (t : ℂ) : ℂ := (228 / 479) * t ^ 8 + (-729 / 479) * t ^ 7 + (-336 / 479) * t ^ 6 + (3444 / 479) * t ^ 5 + (423 / 479) * t ^ 4 + (-2246 / 479) * t ^ 3 + (-3590 / 479) * t ^ 2 + (-1239 / 479) * t + (-1043 / 479)

/-- Shape `z4` of `7_6`, as an element of `ℚ(θ)`. -/
noncomputable def z4 (t : ℂ) : ℂ := (188 / 479) * t ^ 8 + (-828 / 479) * t ^ 7 + (807 / 479) * t ^ 6 + (1428 / 479) * t ^ 5 + (-584 / 479) * t ^ 4 + (-1457 / 479) * t ^ 3 + (-1103 / 479) * t ^ 2 + (-467 / 479) * t + (140 / 479)

/-- Shape `z5` of `7_6`, as an element of `ℚ(θ)`. -/
noncomputable def z5 (t : ℂ) : ℂ := (288 / 479) * t ^ 8 + (-1299 / 479) * t ^ 7 + (1542 / 479) * t ^ 6 + (1199 / 479) * t ^ 5 + (257 / 479) * t ^ 4 + (-2232 / 479) * t ^ 3 + (-1333 / 479) * t ^ 2 + (-960 / 479) * t + (296 / 479)

/-- Shape `z6` of `7_6`, as an element of `ℚ(θ)`. -/
noncomputable def z6 (t : ℂ) : ℂ := (-339 / 479) * t ^ 8 + (1544 / 479) * t ^ 7 + (-1845 / 479) * t ^ 6 + (-1566 / 479) * t ^ 5 + (411 / 479) * t ^ 4 + (1789 / 479) * t ^ 3 + (1594 / 479) * t ^ 2 + (2088 / 479) * t + (889 / 479)

/-- Shape `z7` of `7_6`, as an element of `ℚ(θ)`. -/
noncomputable def z7 (t : ℂ) : ℂ := (-374 / 479) * t ^ 8 + (1637 / 479) * t ^ 7 + (-1743 / 479) * t ^ 6 + (-1893 / 479) * t ^ 5 + (-530 / 479) * t ^ 4 + (2659 / 479) * t ^ 3 + (2872 / 479) * t ^ 2 + (2524 / 479) * t + (1026 / 479)

theorem z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination (1 * t ^ 8 + (-4) * t ^ 7 + 3 * t ^ 6 + 7 * t ^ 5 + 3 * t ^ 4 + (-7) * t ^ 3 + (-9) * t ^ 2 + (-8) * t + (-4)) * h + ((-1)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z0_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z0 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z0] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1 / 19) * t ^ 8 + (3 / 19) * t ^ 7 + (-7 / 19) * t ^ 5 + (-10 / 19) * t ^ 4 + (-3 / 19) * t ^ 3 + (6 / 19) * t ^ 2 + (14 / 19) * t + (18 / 19)) * h + ((-1 / 19)) * ht
  exact absurd this one_ne_zero

theorem z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-188 / 479) * t ^ 8 + (828 / 479) * t ^ 7 + (-807 / 479) * t ^ 6 + (-1428 / 479) * t ^ 5 + (584 / 479) * t ^ 4 + (1457 / 479) * t ^ 3 + (1103 / 479) * t ^ 2 + (467 / 479) * t + (339 / 479)) * h + ((5828 / 229441) * t ^ 7 + (-102748 / 229441) * t ^ 6 + (428229 / 229441) * t ^ 5 + (-602638 / 229441) * t ^ 4 + (-160059 / 229441) * t ^ 3 + (475189 / 229441) * t ^ 2 + (89513 / 229441) * t + (300077 / 229441)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z1_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z1 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z1] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((293 / 479) * t ^ 8 + (-1107 / 479) * t ^ 7 + (501 / 479) * t ^ 6 + (2888 / 479) * t ^ 5 + (323 / 479) * t ^ 4 + (-2151 / 479) * t ^ 3 + (-2542 / 479) * t ^ 2 + (-1296 / 479) * t + (-750 / 479)) * h + ((9083 / 229441) * t ^ 7 + (-154447 / 229441) * t ^ 6 + (568728 / 229441) * t ^ 5 + (-546239 / 229441) * t ^ 4 + (-773844 / 229441) * t ^ 3 + (619474 / 229441) * t ^ 2 + (312082 / 229441) * t + (582809 / 229441)) * ht
  exact absurd this one_ne_zero

theorem z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t + 1) * h + ((-1 / 19)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z2_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z2 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z2] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1) * t ^ 8 + 4 * t ^ 7 + (-3) * t ^ 6 + (-7) * t ^ 5 + (-3) * t ^ 4 + 7 * t ^ 3 + 9 * t ^ 2 + 8 * t + 5) * h + ((1 / 19) * t ^ 7 + (-3 / 19) * t ^ 6 + (7 / 19) * t ^ 4 + (10 / 19) * t ^ 3 + (3 / 19) * t ^ 2 + (-6 / 19) * t + (-14 / 19)) * ht
  exact absurd this one_ne_zero

theorem z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-36 / 479) * t ^ 8 + (342 / 479) * t ^ 7 + (-1031 / 479) * t ^ 6 + (868 / 479) * t ^ 5 + (866 / 479) * t ^ 4 + (-200 / 479) * t ^ 3 + (-971 / 479) * t ^ 2 + (-838 / 479) * t + (-516 / 479)) * h + ((8208 / 229441) * t ^ 7 + (-71388 / 229441) * t ^ 6 + (162114 / 229441) * t ^ 5 + (94557 / 229441) * t ^ 4 + (-706734 / 229441) * t ^ 3 + (320019 / 229441) * t ^ 2 + (278370 / 229441) * t + (308747 / 229441)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z3_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z3 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z3] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1876 / 9101) * t ^ 8 + (-9200 / 9101) * t ^ 7 + (640 / 479) * t ^ 6 + (9959 / 9101) * t ^ 5 + (-11545 / 9101) * t ^ 4 + (-13581 / 9101) * t ^ 3 + (-2782 / 9101) * t ^ 2 + (3167 / 9101) * t + (4536 / 9101)) * h + ((22512 / 229441) * t ^ 7 + (-1754292 / 4359379) * t ^ 6 + (548592 / 4359379) * t ^ 5 + (7421304 / 4359379) * t ^ 4 + (-5833083 / 4359379) * t ^ 3 + (-5431859 / 4359379) * t ^ 2 + (262626 / 4359379) * t + (2544413 / 4359379)) * ht
  exact absurd this one_ne_zero

theorem z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-293 / 479) * t ^ 8 + (1107 / 479) * t ^ 7 + (-501 / 479) * t ^ 6 + (-2888 / 479) * t ^ 5 + (-323 / 479) * t ^ 4 + (2151 / 479) * t ^ 3 + (2542 / 479) * t ^ 2 + (1296 / 479) * t + (1229 / 479)) * h + ((55084 / 229441) * t ^ 7 + (-230384 / 229441) * t ^ 6 + (160447 / 229441) * t ^ 5 + (600523 / 229441) * t ^ 4 + (-309954 / 229441) * t ^ 3 + (-493975 / 229441) * t ^ 2 + (-162979 / 229441) * t + (-57381 / 229441)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z4_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z4 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z4] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((31 / 479) * t ^ 8 + (-534 / 479) * t ^ 7 + (2072 / 479) * t ^ 6 + (-2557 / 479) * t ^ 5 + (-932 / 479) * t ^ 4 + (119 / 479) * t ^ 3 + (2180 / 479) * t ^ 2 + (1653 / 479) * t + (1562 / 479)) * h + ((5828 / 229441) * t ^ 7 + (-102748 / 229441) * t ^ 6 + (428229 / 229441) * t ^ 5 + (-602638 / 229441) * t ^ 4 + (-160059 / 229441) * t ^ 3 + (475189 / 229441) * t ^ 2 + (89513 / 229441) * t + (300077 / 229441)) * ht
  exact absurd this one_ne_zero

theorem z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-1421 / 9101) * t ^ 8 + (7512 / 9101) * t ^ 7 + (-735 / 479) * t ^ 6 + (7704 / 9101) * t ^ 5 + (-11189 / 9101) * t ^ 4 + (16162 / 9101) * t ^ 3 + (1496 / 9101) * t ^ 2 + (2661 / 9101) * t + (6616 / 9101)) * h + ((409248 / 4359379) * t ^ 7 + (-2372343 / 4359379) * t ^ 6 + (5254074 / 4359379) * t ^ 5 + (-4970423 / 4359379) * t ^ 4 + (5857010 / 4359379) * t ^ 3 + (-7884400 / 4359379) * t ^ 2 + (4040468 / 4359379) * t + (-2401043 / 4359379)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z5_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z5 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z5] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((1226 / 479) * t ^ 8 + (-5420 / 479) * t ^ 7 + (5706 / 479) * t ^ 6 + (7376 / 479) * t ^ 5 + (-965 / 479) * t ^ 4 + (-9262 / 479) * t ^ 3 + (-6556 / 479) * t ^ 2 + (-5364 / 479) * t + (-1747 / 479)) * h + ((353088 / 229441) * t ^ 7 + (-1741182 / 229441) * t ^ 6 + (2550408 / 229441) * t ^ 5 + (778090 / 229441) * t ^ 4 + (-654044 / 229441) * t ^ 3 + (-2436147 / 229441) * t ^ 2 + (-462164 / 229441) * t + (-549142 / 229441)) * ht
  exact absurd this one_ne_zero

theorem z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((510 / 479) * t ^ 8 + (-2450 / 479) * t ^ 7 + (3509 / 479) * t ^ 6 + (796 / 479) * t ^ 5 + (505 / 479) * t ^ 4 + (-3234 / 479) * t ^ 3 + (-2131 / 479) * t ^ 2 + (-2179 / 479) * t + (-354 / 479)) * h + ((172890 / 229441) * t ^ 7 + (-926430 / 229441) * t ^ 6 + (1688911 / 229441) * t ^ 5 + (-544938 / 229441) * t ^ 4 + (89821 / 229441) * t ^ 3 + (-656531 / 229441) * t ^ 2 + (-499695 / 229441) * t + (-544147 / 229441)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z6_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z6 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z6] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-374 / 479) * t ^ 8 + (1637 / 479) * t ^ 7 + (-1743 / 479) * t ^ 6 + (-1893 / 479) * t ^ 5 + (-530 / 479) * t ^ 4 + (2659 / 479) * t ^ 3 + (2872 / 479) * t ^ 2 + (2524 / 479) * t + (1026 / 479)) * h + ((126786 / 229441) * t ^ 7 + (-625255 / 229441) * t ^ 6 + (927057 / 229441) * t ^ 5 + (212445 / 229441) * t ^ 4 + (-179507 / 229441) * t ^ 3 + (-575372 / 229441) * t ^ 2 + (-576724 / 229441) * t + (-650101 / 229441)) * ht
  exact absurd this one_ne_zero

theorem z7_ne_zero {t : ℂ} (ht : minpoly t = 0) : z7 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z7] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((339 / 479) * t ^ 8 + (-1544 / 479) * t ^ 7 + (1845 / 479) * t ^ 6 + (1566 / 479) * t ^ 5 + (-411 / 479) * t ^ 4 + (-1789 / 479) * t ^ 3 + (-1594 / 479) * t ^ 2 + (-2088 / 479) * t + (-410 / 479)) * h + ((126786 / 229441) * t ^ 7 + (-625255 / 229441) * t ^ 6 + (927057 / 229441) * t ^ 5 + (212445 / 229441) * t ^ 4 + (-179507 / 229441) * t ^ 3 + (-575372 / 229441) * t ^ 2 + (-576724 / 229441) * t + (-650101 / 229441)) * ht
  exact absurd this one_ne_zero

theorem one_sub_z7_ne_zero {t : ℂ} (ht : minpoly t = 0) : 1 - z7 t ≠ 0 := by
  intro h
  simp only [minpoly] at ht
  simp only [z7] at h
  have : (1 : ℂ) = 0 := by
    linear_combination ((-510 / 479) * t ^ 8 + (2450 / 479) * t ^ 7 + (-3509 / 479) * t ^ 6 + (-796 / 479) * t ^ 5 + (-505 / 479) * t ^ 4 + (3234 / 479) * t ^ 3 + (2131 / 479) * t ^ 2 + (2179 / 479) * t + (833 / 479)) * h + ((190740 / 229441) * t ^ 7 + (-988210 / 229441) * t ^ 6 + (1686886 / 229441) * t ^ 5 + (-374455 / 229441) * t ^ 4 + (421227 / 229441) * t ^ 3 + (-1360945 / 229441) * t ^ 2 + (-554037 / 229441) * t + (-685092 / 229441)) * ht
  exact absurd this one_ne_zero

/-- **Edge 0** of `7_6`, exponents `[1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_0 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z0 t - 1) ^ 1 * z1 t ^ 1 * z2 t ^ 1 * z4 t ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z4]
  linear_combination ((-5828 / 4359379) * t ^ 17 + (126060 / 4359379) * t ^ 16 + (-856705 / 4359379) * t ^ 15 + (2583002 / 4359379) * t ^ 14 + (-2833428 / 4359379) * t ^ 13 + (-1956074 / 4359379) * t ^ 12 + (4558415 / 4359379) * t ^ 11 + (3680230 / 4359379) * t ^ 10 + (-3092303 / 4359379) * t ^ 9 + (-6330822 / 4359379) * t ^ 8 + (-2734498 / 4359379) * t ^ 7 + (-6171282 / 4359379) * t ^ 6 + (17361344 / 4359379) * t ^ 5 + (428506 / 229441) * t ^ 4 + (-6838954 / 4359379) * t ^ 3 + (-1202713 / 4359379) * t ^ 2 + (-5920143 / 4359379) * t) * ht

/-- **Edge 1** of `7_6`, exponents `[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0]`, denominators cleared. -/
theorem edge_1 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * z3 t ^ 1 * (z3 t - 1) ^ 1 * z6 t ^ 1 * z7 t ^ 1 = (1 - z0 t) ^ 1 * z1 t ^ 1 * z3 t ^ 1 * (1 - z7 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z3, z6, z7]
  linear_combination ((204316146144 / 25216079618399) * t ^ 31 + (-5833659309120 / 25216079618399) * t ^ 30 + (62943170538582 / 25216079618399) * t ^ 29 + (-342305391392109 / 25216079618399) * t ^ 28 + (909996911656209 / 25216079618399) * t ^ 27 + (-270240899659209 / 25216079618399) * t ^ 26 + (-5304399598991562 / 25216079618399) * t ^ 25 + (12981868213498833 / 25216079618399) * t ^ 24 + (-2124954838522266 / 25216079618399) * t ^ 23 + (-32146984996693908 / 25216079618399) * t ^ 22 + (26726805700691298 / 25216079618399) * t ^ 21 + (40310575688639786 / 25216079618399) * t ^ 20 + (-17540605882073777 / 25216079618399) * t ^ 19 + (-94706501755794924 / 25216079618399) * t ^ 18 + (11872115331626617 / 25216079618399) * t ^ 17 + (78929504734791929 / 25216079618399) * t ^ 16 + (110210747933938951 / 25216079618399) * t ^ 15 + (-21569264292375921 / 25216079618399) * t ^ 14 + (-129412931147180816 / 25216079618399) * t ^ 13 + (-165985300303585537 / 25216079618399) * t ^ 12 + (-21422002101387213 / 25216079618399) * t ^ 11 + (120211055944770670 / 25216079618399) * t ^ 10 + (188612609987302547 / 25216079618399) * t ^ 9 + (124185756699663494 / 25216079618399) * t ^ 8 + (11074865502058587 / 25216079618399) * t ^ 7 + (-85207571923613583 / 25216079618399) * t ^ 6 + (-110690444535565076 / 25216079618399) * t ^ 5 + (-89593354719022453 / 25216079618399) * t ^ 4 + (-51148725103481272 / 25216079618399) * t ^ 3 + (-21800300386606058 / 25216079618399) * t ^ 2 + (-6420559223730673 / 25216079618399) * t + (-1363642834189370 / 25216079618399)) * ht

/-- **Edge 2** of `7_6`, exponents `[0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_2 {t : ℂ} (ht : minpoly t = 0) :
    (z0 t - 1) ^ 1 * (z4 t - 1) ^ 1 * (z5 t - 1) ^ 1 = z0 t ^ 1 * (1 - z1 t) ^ 1 * (1 - z2 t) ^ 1 * (1 - z3 t) ^ 1 * z4 t ^ 1 * z5 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z1, z2, z3, z4, z5]
  linear_combination ((-20141568 / 52643172481) * t ^ 32 + (10844604720 / 1000220277139) * t ^ 31 + (-116216031852 / 1000220277139) * t ^ 30 + (635123239116 / 1000220277139) * t ^ 29 + (-1781874159387 / 1000220277139) * t ^ 28 + (1398832261137 / 1000220277139) * t ^ 27 + (5979790319712 / 1000220277139) * t ^ 26 + (-16367502483882 / 1000220277139) * t ^ 25 + (3591332708843 / 1000220277139) * t ^ 24 + (30070607405649 / 1000220277139) * t ^ 23 + (-4321525840035 / 1000220277139) * t ^ 22 + (-64147230008511 / 1000220277139) * t ^ 21 + (-14962168426344 / 1000220277139) * t ^ 20 + (92076018266552 / 1000220277139) * t ^ 19 + (7659181243777 / 52643172481) * t ^ 18 + (-119251557885238 / 1000220277139) * t ^ 17 + (-281255663255046 / 1000220277139) * t ^ 16 + (-82927949758402 / 1000220277139) * t ^ 15 + (307152840024002 / 1000220277139) * t ^ 14 + (328098567706142 / 1000220277139) * t ^ 13 + (32394496406275 / 1000220277139) * t ^ 12 + (-274061120394202 / 1000220277139) * t ^ 11 + (-263500350324966 / 1000220277139) * t ^ 10 + (-68334201301224 / 1000220277139) * t ^ 9 + (4584394647754 / 52643172481) * t ^ 8 + (95784255886377 / 1000220277139) * t ^ 7 + (3154329104719 / 52643172481) * t ^ 6 + (9479708202556 / 1000220277139) * t ^ 5 + (-1888417525529 / 1000220277139) * t ^ 4 + (-3731129290665 / 1000220277139) * t ^ 3 + (32224731723 / 52643172481) * t ^ 2 + (19513293996 / 52643172481) * t + (62037 / 229441)) * ht

/-- **Edge 3** of `7_6`, exponents `[0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1]`, denominators cleared. -/
theorem edge_3 {t : ℂ} (ht : minpoly t = 0) :
    (z2 t - 1) ^ 1 * (z6 t - 1) ^ 1 * (z7 t - 1) ^ 1 = (1 - z0 t) ^ 1 * (1 - z2 t) ^ 1 * z2 t ^ 1 * (1 - z6 t) ^ 1 * z6 t ^ 1 * z7 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z6, z7]
  linear_combination ((-42980454 / 39674708279) * t ^ 32 + (708582207 / 39674708279) * t ^ 31 + (-5012326226 / 39674708279) * t ^ 30 + (18810392408 / 39674708279) * t ^ 29 + (-35609035806 / 39674708279) * t ^ 28 + (13921701913 / 39674708279) * t ^ 27 + (57984313013 / 39674708279) * t ^ 26 + (-31161026307 / 39674708279) * t ^ 25 + (-162608521194 / 39674708279) * t ^ 24 + (97641571795 / 39674708279) * t ^ 23 + (241663989806 / 39674708279) * t ^ 22 + (133559287588 / 39674708279) * t ^ 21 + (-406179044695 / 39674708279) * t ^ 20 + (-785391035490 / 39674708279) * t ^ 19 + (35841224596 / 39674708279) * t ^ 18 + (1544249476525 / 39674708279) * t ^ 17 + (1511457901893 / 39674708279) * t ^ 16 + (-497744864614 / 39674708279) * t ^ 15 + (-2400442340873 / 39674708279) * t ^ 14 + (-166388298696 / 2088142541) * t ^ 13 + (16495729291 / 39674708279) * t ^ 12 + (3021868623132 / 39674708279) * t ^ 11 + (3482374345198 / 39674708279) * t ^ 10 + (1354555673385 / 39674708279) * t ^ 9 + (-960028908037 / 39674708279) * t ^ 8 + (-2620062986504 / 39674708279) * t ^ 7 + (-1644705579208 / 39674708279) * t ^ 6 + (-300020923626 / 39674708279) * t ^ 5 + (494319254789 / 39674708279) * t ^ 4 + (571676857109 / 39674708279) * t ^ 3 + (19353199806 / 2088142541) * t ^ 2 + (39083798740 / 39674708279) * t + (-246858950 / 2088142541)) * ht

/-- **Edge 4** of `7_6`, exponents `[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]`, denominators cleared. -/
theorem edge_4 {t : ℂ} (ht : minpoly t = 0) :
    z0 t ^ 1 * (z2 t - 1) ^ 1 * z3 t ^ 1 = z2 t ^ 1 * (1 - z5 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z0, z2, z3, z5]
  linear_combination ((-12 / 479) * t ^ 8 + (213 / 9101) * t ^ 7 + (1848 / 9101) * t ^ 6 + (-3138 / 9101) * t ^ 5 + (-4760 / 9101) * t ^ 4 + (-2771 / 9101) * t ^ 3 + (3051 / 9101) * t ^ 2 + (5623 / 9101) * t + (3294 / 9101)) * ht

/-- **Edge 5** of `7_6`, exponents `[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0]`, denominators cleared. -/
theorem edge_5 {t : ℂ} (ht : minpoly t = 0) :
    (z1 t - 1) ^ 1 * z2 t ^ 1 * (z4 t - 1) ^ 1 * z5 t ^ 1 * z6 t ^ 1 * (z6 t - 1) ^ 1 = z1 t ^ 1 * (1 - z4 t) ^ 1 * z4 t ^ 1 * z6 t ^ 1 * (1 - z7 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z2, z4, z5, z6, z7]
  linear_combination ((-192890761344 / 479105512749581) * t ^ 39 + (6606435852396 / 479105512749581) * t ^ 38 + (-93631052034288 / 479105512749581) * t ^ 37 + (747663024534063 / 479105512749581) * t ^ 36 + (-3731451499038909 / 479105512749581) * t ^ 35 + (11854508548511942 / 479105512749581) * t ^ 34 + (-1170635998620617 / 25216079618399) * t ^ 33 + (15859948995467261 / 479105512749581) * t ^ 32 + (22246607718449268 / 479105512749581) * t ^ 31 + (-39979473680537882 / 479105512749581) * t ^ 30 + (-42386762752497642 / 479105512749581) * t ^ 29 + (112981147577391228 / 479105512749581) * t ^ 28 + (30546743243132429 / 479105512749581) * t ^ 27 + (-6253880739923606 / 25216079618399) * t ^ 26 + (-7299516433675615 / 25216079618399) * t ^ 25 + (21067998517412599 / 479105512749581) * t ^ 24 + (465332307934207791 / 479105512749581) * t ^ 23 + (182412845917117656 / 479105512749581) * t ^ 22 + (-609231122249385693 / 479105512749581) * t ^ 21 + (-739419201011962755 / 479105512749581) * t ^ 20 + (184257385562975479 / 479105512749581) * t ^ 19 + (995528371860482855 / 479105512749581) * t ^ 18 + (893307315573927112 / 479105512749581) * t ^ 17 + (-128945418732797726 / 479105512749581) * t ^ 16 + (-1091168331490091580 / 479105512749581) * t ^ 15 + (-1069299327107852201 / 479105512749581) * t ^ 14 + (-276552059071222535 / 479105512749581) * t ^ 13 + (557499523562636495 / 479105512749581) * t ^ 12 + (829167479762381402 / 479105512749581) * t ^ 11 + (556477017236319678 / 479105512749581) * t ^ 10 + (84986955301352159 / 479105512749581) * t ^ 9 + (-182503226409961360 / 479105512749581) * t ^ 8 + (-221638937093556041 / 479105512749581) * t ^ 7 + (-137472807947452486 / 479105512749581) * t ^ 6 + (-53406342726280958 / 479105512749581) * t ^ 5 + (-7158702734818022 / 479105512749581) * t ^ 4 + (3776476839322284 / 479105512749581) * t ^ 3 + (3468425539997913 / 479105512749581) * t ^ 2 + (71218333129786 / 25216079618399) * t + (1475934335400 / 25216079618399)) * ht

/-- **Edge 6** of `7_6`, exponents `[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]`, denominators cleared. -/
theorem edge_6 {t : ℂ} (ht : minpoly t = 0) :
    z1 t ^ 1 * (z3 t - 1) ^ 1 * z5 t ^ 1 * (z5 t - 1) ^ 1 * (z7 t - 1) ^ 1 = (1 - z3 t) ^ 1 * z3 t ^ 1 * (1 - z4 t) ^ 1 * z5 t ^ 1 * z7 t ^ 1 := by
  simp only [minpoly] at ht
  simp only [z1, z3, z4, z5, z7]
  linear_combination ((833411690496 / 25216079618399) * t ^ 31 + (-9974133590400 / 25216079618399) * t ^ 30 + (28892636402904 / 25216079618399) * t ^ 29 + (172948231769166 / 25216079618399) * t ^ 28 + (-1604992212039303 / 25216079618399) * t ^ 27 + (4895252470069407 / 25216079618399) * t ^ 26 + (-4146749734130097 / 25216079618399) * t ^ 25 + (-12481809847527333 / 25216079618399) * t ^ 24 + (31521521483263089 / 25216079618399) * t ^ 23 + (-5451986653368663 / 25216079618399) * t ^ 22 + (-34974551922710613 / 25216079618399) * t ^ 21 + (-32543137743075812 / 25216079618399) * t ^ 20 + (103324191043472955 / 25216079618399) * t ^ 19 + (34987833109114006 / 25216079618399) * t ^ 18 + (-57369032495105043 / 25216079618399) * t ^ 17 + (-163965336766370967 / 25216079618399) * t ^ 16 + (-3559857533913647 / 25216079618399) * t ^ 15 + (131130478578839665 / 25216079618399) * t ^ 14 + (204344701873671240 / 25216079618399) * t ^ 13 + (27881897113904285 / 25216079618399) * t ^ 12 + (-126071872789721298 / 25216079618399) * t ^ 11 + (-202127037597364933 / 25216079618399) * t ^ 10 + (-105708997000536319 / 25216079618399) * t ^ 9 + (7849897807922560 / 25216079618399) * t ^ 8 + (92535673566306544 / 25216079618399) * t ^ 7 + (93370388579849906 / 25216079618399) * t ^ 6 + (64724965118204652 / 25216079618399) * t ^ 5 + (28512513730946631 / 25216079618399) * t ^ 4 + (9364347648663670 / 25216079618399) * t ^ 3 + (928745375062224 / 25216079618399) * t ^ 2 + (-86826009818928 / 25216079618399) * t + (-233873287215168 / 25216079618399)) * ht

/-- **Edge 7** of `7_6`, exponents `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]`, denominators cleared. -/
theorem edge_7 {t : ℂ} (ht : minpoly t = 0) :
    z4 t ^ 1 * z7 t ^ 1 = (1 - z5 t) ^ 1 * (1 - z6 t) ^ 1 := by
  simp only [minpoly] at ht
  simp only [z4, z5, z6, z7]
  linear_combination ((27320 / 229441) * t ^ 7 + (-158325 / 229441) * t ^ 6 + (359556 / 229441) * t ^ 5 + (-323768 / 229441) * t ^ 4 + (198045 / 229441) * t ^ 3 + (-84078 / 229441) * t ^ 2 + (224758 / 229441) * t + (-218670 / 229441)) * ht

end K76
end QOU.Knot.GeneratedGluingHigh
