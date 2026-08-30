/-
  Certified numeric brackets on the 5₂ shape `y₁`.

  Bean `qou-f8lit`, steps (i)–(ii) of the route to `VOL_4_1 < VOL_5_2`.

  ═══ WHY THIS IS NEEDED AT ALL ═══

  `fiveTwoShape` is built from `realRoot := Classical.choose
  SaddleRoots.exists_real_root` — obtained from the intermediate value theorem, so it is
  **non-constructive by construction**.  Grepped before writing this: the only recorded
  fact about it anywhere in the corpus is `fiveTwoShape_im_pos`.  There is no bracket on
  its real part, imaginary part or modulus, so *no* numeric statement about `VOL_5_2` can
  even be started.  This file supplies the missing handle.

  It is deliberately scoped to the part that is cheap and certain.  The route to
  `VOL_4_1 < VOL_5_2` continues through certified `Λ` values at three angles that are
  **not rational multiples of π**, which needs interval arithmetic on `sin` at irrational
  arguments — machinery the corpus does not have, and its own project.  See `qou-f8lit`.
  Nothing here attempts that, and nothing here should be read as progress on it.

  ═══ WHAT MAKES IT EASY ═══

  `SaddleRoots.ofRealRoot` gives the root **explicitly**, not implicitly:

      a = ((2 − t)/2 : ℝ) + (√(3t² − 4t + 8)/2 : ℝ)·I

  so the real and imaginary parts are projections, and the whole problem reduces to
  bracketing the real root `t` of `X³ − 2X² + 3X − 1`.  That cubic is strictly monotone
  (`g'(x) = 3x² − 4x + 3 = 3(x − 2/3)² + 5/3 > 0`), so the sign change
  `g(2/5) < 0 < g(9/20)` pins it.

  Rationals are used throughout rather than decimal literals: this file exists because a
  truncated decimal caused the defect in `qou-f8lit`, and reintroducing one here would be
  a poor joke.

  -- Ref: [neumann2004] Prop 2.5 (the 5₂ root data)
-/
import QOU.Knot.FiveTwoVolumeConstant

namespace QOU.Knot.FiveTwoShapeBounds

open QOU.Knot.FiveTwoVolume

/-! ## §1 — Bracketing the real root -/

/-- The defining cubic, as a standalone fact. -/
theorem realRoot_cubic :
    realRoot ^ 3 - 2 * realRoot ^ 2 + 3 * realRoot - 1 = 0 :=
  realRoot_spec.2.2

theorem realRoot_pos : 0 < realRoot := realRoot_spec.1

theorem realRoot_lt_one : realRoot < 1 := realRoot_spec.2.1

/-- **Lower bracket** `2/5 < t`. The cubic is strictly increasing and `g(2/5) < 0`. -/
theorem realRoot_gt : (2 / 5 : ℝ) < realRoot := by
  by_contra h
  push_neg at h
  have h0 := realRoot_pos
  nlinarith [realRoot_cubic, sq_nonneg realRoot, sq_nonneg (realRoot - 2 / 5),
    sq_nonneg (realRoot + 2 / 5)]

/-- **Upper bracket** `t < 9/20`, from `g(9/20) > 0`. -/
theorem realRoot_lt : realRoot < (9 / 20 : ℝ) := by
  by_contra h
  push_neg at h
  have h1 := realRoot_lt_one
  nlinarith [realRoot_cubic, sq_nonneg realRoot, sq_nonneg (realRoot - 9 / 20),
    sq_nonneg (realRoot + 9 / 20)]

/-! ## §2 — The shape's real and imaginary parts

Both are projections of the explicit `ofRealRoot` witness, so they are definitional. -/

@[simp] theorem fiveTwoShape_re : fiveTwoShape.re = (2 - realRoot) / 2 := by
  simp [fiveTwoShape, saddle, QOU.QBeta.FiveTwoComplexPentagon.SaddleRoots.ofRealRoot]

@[simp] theorem fiveTwoShape_im :
    fiveTwoShape.im = Real.sqrt (3 * realRoot ^ 2 - 4 * realRoot + 8) / 2 := by
  simp [fiveTwoShape, saddle, QOU.QBeta.FiveTwoComplexPentagon.SaddleRoots.ofRealRoot]

/-! ## §3 — Numeric brackets

Everything below follows from §1 and §2 by monotonicity. The margins are deliberately
loose: the consumer (`VOL_4_1 < VOL_5_2`) has 34 % headroom, so there is no reason to
chase digits — and chasing them is what made item 2 of `qou-f8lit` infeasible. -/

/-- `31/40 < Re(y₁) < 4/5`. -/
theorem fiveTwoShape_re_bounds :
    (31 / 40 : ℝ) < fiveTwoShape.re ∧ fiveTwoShape.re < (4 / 5 : ℝ) := by
  rw [fiveTwoShape_re]
  constructor
  · linarith [realRoot_lt]
  · linarith [realRoot_gt]

/-- The radicand is bracketed, which is what the `Im` bound needs. -/
theorem radicand_bounds :
    (34 / 5 : ℝ) < 3 * realRoot ^ 2 - 4 * realRoot + 8 ∧
      3 * realRoot ^ 2 - 4 * realRoot + 8 < (69 / 10 : ℝ) := by
  have hlo := realRoot_gt
  have hhi := realRoot_lt
  constructor <;> nlinarith [sq_nonneg realRoot, sq_nonneg (realRoot - 2 / 5),
    sq_nonneg (realRoot - 9 / 20)]

/-- `13/10 < Im(y₁) < 132/100`. Strictly positive, and bounded away from `0` by an
explicit rational — which `fiveTwoShape_im_pos` alone does not give. -/
theorem fiveTwoShape_im_bounds :
    (13 / 10 : ℝ) < fiveTwoShape.im ∧ fiveTwoShape.im < (33 / 25 : ℝ) := by
  have hr := radicand_bounds
  have hpos : (0 : ℝ) < 3 * realRoot ^ 2 - 4 * realRoot + 8 := by linarith [hr.1]
  rw [fiveTwoShape_im]
  constructor
  · have : (13 / 5 : ℝ) < Real.sqrt (3 * realRoot ^ 2 - 4 * realRoot + 8) := by
      have h : ((13 : ℝ) / 5) ^ 2 < 3 * realRoot ^ 2 - 4 * realRoot + 8 := by
        norm_num; linarith [hr.1]
      nlinarith [Real.sq_sqrt hpos.le, Real.sqrt_nonneg
        (3 * realRoot ^ 2 - 4 * realRoot + 8), h]
    linarith
  · have : Real.sqrt (3 * realRoot ^ 2 - 4 * realRoot + 8) < (66 / 25 : ℝ) := by
      have h : 3 * realRoot ^ 2 - 4 * realRoot + 8 < ((66 : ℝ) / 25) ^ 2 := by
        norm_num; linarith [hr.2]
      nlinarith [Real.sq_sqrt hpos.le, Real.sqrt_nonneg
        (3 * realRoot ^ 2 - 4 * realRoot + 8), h]
    linarith

/-- **`normSq y₁ > 1`, i.e. `|y₁| > 1`** — recorded because it closes the obvious
shortcut: the `Li₂` power series does **not** converge at `y₁`, which is why the corpus
uses the extended `cLiTwoExt`, and why a naive dilogarithm partial sum cannot be used to
bound `VOL_5_2`. Anyone reaching for one will find it diverges. -/
theorem fiveTwoShape_normSq_gt_one : (1 : ℝ) < Complex.normSq fiveTwoShape := by
  have hre := fiveTwoShape_re_bounds.1
  have him := fiveTwoShape_im_bounds.1
  have hre0 : (0 : ℝ) < fiveTwoShape.re := lt_trans (by norm_num) hre
  have him0 : (0 : ℝ) < fiveTwoShape.im := lt_trans (by norm_num) him
  rw [Complex.normSq_apply]
  nlinarith [hre, him, hre0, him0]

end QOU.Knot.FiveTwoShapeBounds
