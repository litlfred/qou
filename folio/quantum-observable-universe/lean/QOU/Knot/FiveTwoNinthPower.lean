/-
  The 5₂ smallest dihedral angle exceeds `2π/9` — as a POLYNOMIAL condition.

  Bean `qou-52ch`.  This is the step that lets the Rivin-concavity chord bound
  close `VOL_4_1 < VOL_5_2`.

  ═══ WHY `z⁹` ═══

  `2π/9` is exactly one ninth of a full turn, so for `z` whose argument is pinned
  to a window narrow enough to fix the branch,

      arg z > 2π/9   ↔   9·arg z > 2π   ↔   0 < Im (z ^ 9)

  because `arg (z ^ 9) = 9 · arg z` in `Real.Angle` and a positive imaginary part
  is exactly `arg ∈ (0, π)`.  The alternative — comparing `arg z` to `2π/9`
  through `tan` — needs `tan_three_mul`, which Mathlib does not have, plus a
  rational bracket on the algebraic number `tan (2π/9)`.  This route needs
  neither.

  ═══ WHY IT REDUCES TO A QUADRATIC ═══

  Write `t := realRoot`.  Then `‖y₁‖² = t² − 2t + 3`, and the cubic
  `t³ − 2t² + 3t − 1 = 0` says exactly `t · (t² − 2t + 3) = 1`, i.e. `‖y₁‖² = 1/t`
  and `y₁⁻¹ = t · conj y₁`.  Hence for `z = 1 − y₁⁻¹`,

      z.re = (t² − 2t + 2)/2         z.im = t · √(3t² − 4t + 8) / 2

  `Im (z ^ 9) = z.im · Q (z.re², z.im²)` with
  `Q A B = 9A⁴ − 84A³B + 126A²B² − 36AB³ + B⁴`, and both `z.re²` and `z.im²` are
  polynomial in `t`.  So the condition is a degree-15 polynomial in `t` — which,
  **reduced modulo the cubic**, collapses to

      Q ≡ −3t² + 6t − 2.

  ⚠ That reduction is valid *because* `t` is the root.  Evaluating the same
  expression along a free parameter is not the same object: `‖y₁‖² = 1/t` is the
  cubic in disguise and fails off the root.  A first pass did exactly that and
  concluded the existing `2/5` bracket sufficed; it does not
  (`−3(2/5)² + 6(2/5) − 2 = −2/25 < 0`).

  Archimedean (ℝ): ordering — §7c.

  -- Ref: [neumann2004] Prop 2.5 (the 5₂ root data)
  -- Ref: [leitner2026] bean qou-52ch
-/

import QOU.Knot.FiveTwoShapeBounds

namespace QOU.Knot.FiveTwoNinthPower

open QOU.Knot.FiveTwoVolume QOU.Knot.FiveTwoShapeBounds

/-! ## §1 — A tighter lower bracket on the real root

`realRoot_gt : 2/5 < realRoot` is not enough: the quadratic below is negative
there.  `3/7` is, with room on both sides — `g(3/7) = −0.0029` makes it provable
and `−3(3/7)² + 6(3/7) − 2 = +0.0204` makes it work. -/

/-- **`3/7 < realRoot`.**  Same argument as `realRoot_gt`, tighter constant:
the cubic is strictly increasing and `g(3/7) < 0`. -/
theorem realRoot_gt_three_sevenths : (3 / 7 : ℝ) < realRoot := by
  by_contra h
  push_neg at h
  have h0 := realRoot_pos
  nlinarith [realRoot_cubic, sq_nonneg realRoot, sq_nonneg (realRoot - 3 / 7),
    sq_nonneg (realRoot + 3 / 7)]

/-! ## §2 — The three reduced conditions

Two of them are free; only the third needs §1. -/

/-- `Im z < Re z`, i.e. `arg z < π/4` — reduced, this is `−2t(t − 1) > 0`, which
needs only `0 < t < 1`.  Both are already proved. -/
theorem branch_upper : 0 < -2 * realRoot ^ 2 + 2 * realRoot := by
  have h0 := realRoot_pos
  have h1 := realRoot_lt_one
  nlinarith

/-- `√3 · Im z > Re z`, i.e. `arg z > π/6` — reduced, this is
`8(t − 1/2)² + 2 > 0`, which is unconditional. -/
theorem branch_lower : 0 < 8 * realRoot ^ 2 - 8 * realRoot + 4 := by
  nlinarith [sq_nonneg (realRoot - 1 / 2)]

/-- **`0 < Im (z ^ 9)`, reduced modulo the cubic.**

This is the one condition that needs the tighter bracket: it is false at
`t = 2/5`. -/
theorem ninth_power_im_pos_reduced :
    0 < -3 * realRoot ^ 2 + 6 * realRoot - 2 := by
  have hlo := realRoot_gt_three_sevenths
  have hhi := realRoot_lt
  nlinarith [sq_nonneg (realRoot - 3 / 7), sq_nonneg (realRoot - 9 / 20)]

/-! ## §3 — `z := 1 − y₁⁻¹` and its cubic

`z` is the quantity whose argument is the SMALLEST dihedral angle of the 5₂
tetrahedron (`tetAngle₃ y₁ = arg (1 − 1/y₁)`). -/

open Complex in
/-- The third tetrahedral parameter. -/
noncomputable def zz : ℂ := 1 - fiveTwoShape⁻¹

theorem fiveTwoShape_ne_zero : fiveTwoShape ≠ 0 :=
  fun h => by simpa [h] using fiveTwoShape_im_pos

/-- **`z³ = z − 1`.**  The Landen image of `y₁`'s cubic: clearing denominators,
`z³ − z + 1` is exactly `(y³ − 2y² + 3y − 1) / y³`. -/
theorem zz_cubic : zz ^ 3 - zz + 1 = 0 := by
  have h0 := fiveTwoShape_ne_zero
  have hc := fiveTwoShape_cubic
  unfold zz
  field_simp
  linear_combination hc

/-- **`z⁹ = −3z² + 4z − 2`.**  From `z³ = z − 1`: `z⁹ = (z³)³ = (z − 1)³`, and
one more reduction. -/
theorem zz_pow_nine : zz ^ 9 = -3 * zz ^ 2 + 4 * zz - 2 := by
  have h := zz_cubic
  linear_combination (zz ^ 6 + zz ^ 4 - zz ^ 3 + zz ^ 2 - 2 * zz + 2) * h

/-! ## §4 — `z`'s real and imaginary parts

`saddle.hprod` says `y₁ · conj y₁ · t = 1`, i.e. `‖y₁‖² = 1/t` — the cubic in
disguise.  That is what makes `y₁⁻¹ = t · conj y₁`, and hence both parts of `z`
polynomial in `t`. -/

/-- **`‖y₁‖² · t = 1`** — read straight off the root data. -/
theorem normSq_mul_realRoot : Complex.normSq fiveTwoShape * realRoot = 1 := by
  have h := saddle.hprod
  rw [Complex.mul_conj] at h
  exact_mod_cast h

theorem normSq_pos : 0 < Complex.normSq fiveTwoShape :=
  Complex.normSq_pos.mpr fiveTwoShape_ne_zero

/-- `Im z > 0`: `z.im = y₁.im / ‖y₁‖²`. -/
theorem zz_im_pos : 0 < zz.im := by
  have hn := normSq_pos
  have : zz.im = fiveTwoShape.im / Complex.normSq fiveTwoShape := by
    simp [zz, Complex.inv_im]
    ring
  rw [this]
  exact div_pos fiveTwoShape_im_pos hn

/-- **`Re z = (t² − 2t + 2)/2`.**  Uses `‖y₁‖² = 1/t` to turn `y₁⁻¹` into
`t · conj y₁`, then `fiveTwoShape_re`. -/
theorem zz_re_eq : zz.re = (realRoot ^ 2 - 2 * realRoot + 2) / 2 := by
  have hn := normSq_pos
  have hnt := normSq_mul_realRoot
  have hre : zz.re = 1 - fiveTwoShape.re / Complex.normSq fiveTwoShape := by
    simp [zz, Complex.inv_re]
  rw [hre, fiveTwoShape_re]
  field_simp
  nlinarith [hnt, hn]

/-- **`Re z < 2/3`** — equivalent to the reduced quadratic of §2. -/
theorem zz_re_lt_two_thirds : zz.re < 2 / 3 := by
  rw [zz_re_eq]
  nlinarith [ninth_power_im_pos_reduced]

/-! ## §5 — The polynomial condition -/

/-- **`0 < Im (z⁹)`.**

`z⁹ = −3z² + 4z − 2`, so `Im (z⁹) = Im z · (4 − 6 Re z)`, and both factors are
positive.  No degree-9 expansion, and no value of any transcendental. -/
theorem zz_pow_nine_im_pos : 0 < (zz ^ 9).im := by
  have hfac : (zz ^ 9).im = zz.im * (4 - 6 * zz.re) := by
    rw [zz_pow_nine, sq]
    simp [Complex.add_im, Complex.mul_im, Complex.sub_im]
    ring
  rw [hfac]
  have h1 := zz_im_pos
  have h2 := zz_re_lt_two_thirds
  nlinarith

/-! ## §6 — The argument window

`arg z ∈ (π/6, π/4)` is what fixes the branch: it puts `9·arg z` in
`(3π/2, 9π/4)`, strictly inside `(π, 3π)`, so the winding number below is
forced. Both bounds come from §2's reduced conditions. -/

open Real Complex in
theorem zz_re_pos : 0 < zz.re := by
  rw [zz_re_eq]; nlinarith [sq_nonneg (realRoot - 1)]

/-- The discriminant is positive, so its square root behaves. -/
theorem disc_pos' : 0 < 3 * realRoot ^ 2 - 4 * realRoot + 8 := by
  nlinarith [sq_nonneg (3 * realRoot - 2)]

/-- **`Im z = t·√(3t² − 4t + 8) / 2`** — via `‖y₁‖² = 1/t` again. -/
theorem zz_im_eq :
    zz.im = realRoot * Real.sqrt (3 * realRoot ^ 2 - 4 * realRoot + 8) / 2 := by
  have hn := normSq_pos
  have hnt := normSq_mul_realRoot
  have him : zz.im = fiveTwoShape.im / Complex.normSq fiveTwoShape := by
    simp [zz, Complex.inv_im]; ring
  have hinv : (Complex.normSq fiveTwoShape)⁻¹ = realRoot :=
    inv_eq_of_mul_eq_one_right hnt
  rw [him, fiveTwoShape_im, div_eq_mul_inv, hinv]
  ring

/-! The two branch inequalities, lifted from the reduced polynomials of §2 by
squaring.  Each cofactor is exact — `(2Re)² − (2Im)²` is `(−2t² + 2t)` plus
`(−2t − 4)` times the cubic, and `3(2Im)² − (2Re)²` is `(8t² − 8t + 4)` plus
`(8t + 8)` times it. -/

theorem zz_im_lt_re : zz.im < zz.re := by
  have hd := disc_pos'
  have hsq : Real.sqrt (3 * realRoot ^ 2 - 4 * realRoot + 8) ^ 2
      = 3 * realRoot ^ 2 - 4 * realRoot + 8 := Real.sq_sqrt hd.le
  have him := zz_im_eq
  have hre := zz_re_eq
  have hb := branch_upper
  have hc := realRoot_cubic
  have hpos := zz_im_pos
  nlinarith [hsq, him, hre, hb, hc, hpos, zz_re_pos]

theorem sqrt_three_mul_zz_im_gt_re : zz.re < Real.sqrt 3 * zz.im := by
  have hd := disc_pos'
  have hsq : Real.sqrt (3 * realRoot ^ 2 - 4 * realRoot + 8) ^ 2
      = 3 * realRoot ^ 2 - 4 * realRoot + 8 := Real.sq_sqrt hd.le
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have h3p : (0:ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hb := branch_lower
  have hc := realRoot_cubic
  refine lt_of_pow_lt_pow_left₀ 2
    (mul_nonneg (Real.sqrt_nonneg 3) zz_im_pos.le) ?_
  have e1 : (Real.sqrt 3 * zz.im) ^ 2 = 3 * zz.im ^ 2 := by rw [mul_pow, h3]
  have e2 : (realRoot * Real.sqrt (3 * realRoot ^ 2 - 4 * realRoot + 8) / 2) ^ 2
      = realRoot ^ 2 * (3 * realRoot ^ 2 - 4 * realRoot + 8) / 4 := by
    rw [div_pow, mul_pow, hsq]; ring
  rw [e1, zz_re_eq, zz_im_eq, e2]
  nlinarith [hb, hc]

open Real Complex in
/-- `arg z = arctan (Im z / Re z)`, valid because `Re z > 0` puts `arg z` in
`(−π/2, π/2)` where `arctan` inverts `tan`. -/
theorem zz_arg_eq_arctan : zz.arg = Real.arctan (zz.im / zz.re) := by
  have h : |zz.arg| < π / 2 :=
    Complex.abs_arg_lt_pi_div_two_iff.mpr (Or.inl zz_re_pos)
  rw [abs_lt] at h
  rw [← Complex.tan_arg, Real.arctan_tan h.1 h.2]

open Real Complex in
/-- `arg z < π/4`, from `Im z < Re z`. -/
theorem zz_arg_lt_pi_div_four : zz.arg < π / 4 := by
  have hre := zz_re_pos
  have hlt : zz.im / zz.re < 1 := (div_lt_one hre).mpr zz_im_lt_re
  rw [zz_arg_eq_arctan, ← Real.arctan_one]
  exact Real.arctan_lt_arctan hlt

open Real Complex in
/-- `π/6 < arg z`, from `√3·Im z > Re z` — i.e. `Im/Re > tan (π/6) = 1/√3`. -/
theorem pi_div_six_lt_zz_arg : π / 6 < zz.arg := by
  have hre := zz_re_pos
  have h3p : (0:ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hgt : Real.tan (π / 6) < zz.im / zz.re := by
    rw [Real.tan_pi_div_six, lt_div_iff₀ hre, div_mul_eq_mul_div,
      div_lt_iff₀ h3p]
    nlinarith [sqrt_three_mul_zz_im_gt_re, Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 3), h3p]
  have hpi := Real.pi_pos
  calc π / 6 = Real.arctan (Real.tan (π / 6)) := by
        rw [Real.arctan_tan (by nlinarith) (by nlinarith)]
    _ < Real.arctan (zz.im / zz.re) := Real.arctan_lt_arctan hgt
    _ = zz.arg := zz_arg_eq_arctan.symm

/-! ## §7 — The angle bound

`arg (z⁹) = 9 · arg z` in `Real.Angle`, i.e. modulo `2π`.  The window of §6 puts
`9 · arg z` in `(3π/2, 9π/4)`, strictly inside `(π, 3π)`, so the winding number
is forced to be exactly one and `arg (z⁹) = 9·arg z − 2π`.  Positivity of the
left side is then `arg z > 2π/9`. -/

open Real Complex in
/-- `0 < arg (z⁹)`: nonneg from `Im (z⁹) > 0`, and nonzero because a zero
argument forces a zero imaginary part. -/
theorem zz_pow_nine_arg_pos : 0 < (zz ^ 9).arg := by
  have him := zz_pow_nine_im_pos
  rcases (Complex.arg_nonneg_iff.mpr him.le).lt_or_eq with h | h
  · exact h
  · exact absurd (Complex.arg_eq_zero_iff.mp h.symm).2 (ne_of_gt him)

open Real Complex in
/-- **`2π/9 < arg z`** — the smallest dihedral angle of the 5₂ tetrahedron
exceeds `2π/9`.

This is the inequality the Rivin-concavity chord bound needs, and it is reached
without a single value of a transcendental function: `z³ = z − 1` gives
`z⁹ = −3z² + 4z − 2`, whose imaginary part is positive precisely when
`Re z < 2/3`, which is the quadratic `−3t² + 6t − 2 > 0`. -/
theorem two_pi_div_nine_lt_zz_arg : 2 * π / 9 < zz.arg := by
  have hpi := Real.pi_pos
  have hlo := pi_div_six_lt_zz_arg
  have hhi := zz_arg_lt_pi_div_four
  have h9 := zz_pow_nine_arg_pos
  have h9le : (zz ^ 9).arg ≤ π := Complex.arg_le_pi _
  have hangle : (((zz ^ 9).arg : ℝ) : Real.Angle) = ((9 * zz.arg : ℝ) : Real.Angle) := by
    rw [show (9 * zz.arg : ℝ) = (9 : ℕ) • zz.arg by simp [nsmul_eq_mul]]
    rw [Real.Angle.coe_nsmul, Complex.arg_pow_coe_angle]
  obtain ⟨k, hk⟩ := Real.Angle.angle_eq_iff_two_pi_dvd_sub.mp hangle
  -- `hk : arg (z^9) - 9 * arg z = 2 * π * k`, and the window forces `k = -1`.
  have hkr1 : (-2 : ℝ) < (k : ℝ) := by nlinarith
  have hkr2 : (k : ℝ) < 0 := by nlinarith
  have hkz : k = -1 := by
    have a : (-2 : ℤ) < k := by exact_mod_cast hkr1
    have b : k < 0 := by exact_mod_cast hkr2
    omega
  rw [hkz] at hk
  push_cast at hk
  linarith

/-! ## §8 — Back to the tetrahedron

`z` is not an auxiliary quantity: `arg z` **is** the 5₂ tetrahedron's third
dihedral angle, `tetAngle₃ y₁ = arg (1 − 1/y₁)`. -/

/-- `arg z` is the third dihedral angle. -/
theorem zz_arg_eq_angle₃ : zz.arg = fiveTwoTet.angle₃ := by
  simp [zz, fiveTwoTet, QOU.MathlibExt.IdealTetrahedron.angle₃,
    QOU.Archimedean.tetAngle₃, one_div]

/-- **The 5₂ tetrahedron's third dihedral angle exceeds `2π/9`.**

`qou-52ch`'s chord bound needs this of the *smallest* angle; `angle₃` is the
smallest numerically (`0.7039` against `1.0300` and `1.4077`), but that ordering
is not proved here — see the module header. -/
theorem two_pi_div_nine_lt_angle₃ : 2 * Real.pi / 9 < fiveTwoTet.angle₃ := by
  rw [← zz_arg_eq_angle₃]; exact two_pi_div_nine_lt_zz_arg

/-! ## §9 — The other two angles, and hence the minimum

The chord bound wants the SMALLEST angle to exceed `2π/9`.  §8 gives that for
`angle₃`; the other two clear it with room, and by a cheaper route — both exceed
`π/4`, and `π/4 > 2π/9` because `1/4 > 2/9`.  So no ordering of the three needs
proving. -/

open Real Complex in
theorem fiveTwoShape_re_pos : 0 < fiveTwoShape.re := by
  rw [fiveTwoShape_re]; have := realRoot_lt_one; linarith

open Real Complex in
/-- `Im y₁ > Re y₁` — reduced, this is `2t² + 4 > 0`, unconditional. -/
theorem fiveTwoShape_im_gt_re : fiveTwoShape.re < fiveTwoShape.im := by
  have hd := disc_pos'
  have hsq : Real.sqrt (3 * realRoot ^ 2 - 4 * realRoot + 8) ^ 2
      = 3 * realRoot ^ 2 - 4 * realRoot + 8 := Real.sq_sqrt hd.le
  have hre := fiveTwoShape_re_pos
  rw [fiveTwoShape_re, fiveTwoShape_im] at *
  refine lt_of_pow_lt_pow_left₀ 2 (by positivity) ?_
  rw [div_pow, div_pow, hsq]
  nlinarith [sq_nonneg realRoot]

open Real Complex in
/-- **`π/4 < angle₁`**, from `Im y₁ > Re y₁`. -/
theorem pi_div_four_lt_angle₁ : π / 4 < fiveTwoTet.angle₁ := by
  have hre := fiveTwoShape_re_pos
  have h : |fiveTwoShape.arg| < π / 2 :=
    Complex.abs_arg_lt_pi_div_two_iff.mpr (Or.inl hre)
  rw [abs_lt] at h
  have harg : fiveTwoShape.arg = Real.arctan (fiveTwoShape.im / fiveTwoShape.re) := by
    rw [← Complex.tan_arg, Real.arctan_tan h.1 h.2]
  have hgt : (1:ℝ) < fiveTwoShape.im / fiveTwoShape.re :=
    (one_lt_div hre).mpr fiveTwoShape_im_gt_re
  have : π / 4 < fiveTwoShape.arg := by
    rw [harg, ← Real.arctan_one]; exact Real.arctan_lt_arctan hgt
  simpa [fiveTwoTet, QOU.MathlibExt.IdealTetrahedron.angle₁,
    QOU.Archimedean.tetAngle₁] using this

open Real Complex in
theorem angle₁_lt_pi_div_two : fiveTwoTet.angle₁ < π / 2 := by
  have hre := fiveTwoShape_re_pos
  have h : |fiveTwoShape.arg| < π / 2 :=
    Complex.abs_arg_lt_pi_div_two_iff.mpr (Or.inl hre)
  rw [abs_lt] at h
  simpa [fiveTwoTet, QOU.MathlibExt.IdealTetrahedron.angle₁,
    QOU.Archimedean.tetAngle₁] using h.2

open Real Complex in
/-- **`π/4 < angle₂`** — from the angle sum, `angle₁ < π/2` and `angle₃ < π/4`. -/
theorem pi_div_four_lt_angle₂ : π / 4 < fiveTwoTet.angle₂ := by
  have hsum := fiveTwoTet.angle_sum
  have h1 := angle₁_lt_pi_div_two
  have h3 : fiveTwoTet.angle₃ < π / 4 := by
    rw [← zz_arg_eq_angle₃]; exact zz_arg_lt_pi_div_four
  linarith

/-- **All three dihedral angles exceed `2π/9`** — so the chord bound's
hypothesis holds for the minimum, whichever it is. -/
theorem all_angles_gt_two_pi_div_nine :
    2 * Real.pi / 9 < fiveTwoTet.angle₁ ∧
    2 * Real.pi / 9 < fiveTwoTet.angle₂ ∧
    2 * Real.pi / 9 < fiveTwoTet.angle₃ := by
  have hpi := Real.pi_pos
  refine ⟨?_, ?_, two_pi_div_nine_lt_angle₃⟩
  · have := pi_div_four_lt_angle₁; linarith
  · have := pi_div_four_lt_angle₂; linarith

end QOU.Knot.FiveTwoNinthPower