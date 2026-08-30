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
  -- Ref: [manuscript] bean qou-52ch
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

end QOU.Knot.FiveTwoNinthPower
