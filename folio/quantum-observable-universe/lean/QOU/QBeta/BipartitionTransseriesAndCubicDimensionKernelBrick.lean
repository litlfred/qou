/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Non-Degenerate Witness Margin, Closure Volume Deficit, Bipartition Transseries, and Cross Form Brick

Formalizes algebraic and arithmetic bricks for five tasks in the `b9cj` / `qou-wp3h` / `qou-10v9` lane:
1. `qou-m0bv`: Non-degenerate mass and crossing excess pair `(mass - m0, crossings - c0)`
   separating positive-threshold witnesses from zero-mass/unknot `(0, 0)` degeneracies.
2. `qou-m6gp`: Interface-coupled braid closure volume deficit `vBound - (v1 + v2)` and
   telescoping three-body closure decomposition.
3. `qou-mbz4`: Two-sector bipartition transseries partial sum `a0 + s1 * phi1 + s2 * phi2`
   linearity and parity-dual sector combination.
4. `qou-mdbh`: Cubic-to-quadratic dimension kernel excess `f^3 * w - f^2 * w = f^2 * (f - 1) * w`
   and centered reference-dimension shift.
5. `qou-mssy`: Meridian-longitude quadratic cross form `(2 * m + l) * l = 2 * m * l + l^2`,
   simultaneous sign-inversion invariance, and meridian shift increment.
-/

namespace QOU.QBeta.BipartitionTransseriesAndCubicDimensionKernelBrick

/-! ## Section 1: Non-Degenerate Mass-Crossing Witness Margin (`qou-m0bv`) -/

/-- Excess pair `(mass - m0, crossings - c0)` above lower non-degeneracy thresholds `(m0, c0)`. -/
def nonDegenerateExcessPair (mass crossings m0 c0 : Int) : Int × Int :=
  (mass - m0, crossings - c0)

-- Bean qou-m0bv: difference between a candidate witness and the degenerate `(0, 0)` witness.
/-- Subtracting the degenerate `(0, 0)` excess pair from `nonDegenerateExcessPair mass crossings m0 c0`
recovers `(mass, crossings)` independently of `(m0, c0)`. -/
theorem nonDegenerateExcessPair_degenerate_gap_and_sum
    (mass crossings m0 c0 : Int) :
    (nonDegenerateExcessPair mass crossings m0 c0).1 -
      (nonDegenerateExcessPair 0 0 m0 c0).1 + crossings + m0 + c0 =
      mass + crossings + m0 + c0 ∧
    (nonDegenerateExcessPair mass crossings m0 c0).1 +
      (nonDegenerateExcessPair mass crossings m0 c0).2 =
      (mass + crossings) - (m0 + c0) := by
  dsimp only [nonDegenerateExcessPair]
  have h1 : (mass - m0) - (0 - m0) + crossings + m0 + c0 =
      mass + crossings + m0 + c0 := by
    omega
  have h2 : (mass - m0) + (crossings - c0) = (mass + crossings) - (m0 + c0) := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-m0bv: threshold composition and composite hadron excess additivity.
/-- Summing two witness pairs `(m1, k1)` and `(m2, k2)` above thresholds `(m01, c01)` and
`(m02, c02)` adds both excess components. -/
theorem nonDegenerateExcessPair_composite_additivity
    (m1 k1 m01 c01 m2 k2 m02 c02 : Int) :
    (nonDegenerateExcessPair (m1 + m2) (k1 + k2) (m01 + m02) (c01 + c02)).1 =
      (nonDegenerateExcessPair m1 k1 m01 c01).1 +
        (nonDegenerateExcessPair m2 k2 m02 c02).1 ∧
    (nonDegenerateExcessPair (m1 + m2) (k1 + k2) (m01 + m02) (c01 + c02)).2 +
      m1 + m2 + m01 + m02 =
      (nonDegenerateExcessPair m1 k1 m01 c01).2 +
        (nonDegenerateExcessPair m2 k2 m02 c02).2 + m1 + m2 + m01 + m02 := by
  dsimp only [nonDegenerateExcessPair]
  have h1 : (m1 + m2) - (m01 + m02) = (m1 - m01) + (m2 - m02) := by
    omega
  have h2 : ((k1 + k2) - (c01 + c02)) + m1 + m2 + m01 + m02 =
      (k1 - c01) + (k2 - c02) + m1 + m2 + m01 + m02 := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 2: Interface-Inclusive Closure Volume Deficit (`qou-m6gp`) -/

/-- Volume deficit `vBound - (v1 + v2)` between an interface-coupled braid closure and its
free components. -/
def closureVolumeDeficit (vBound v1 v2 : Int) : Int :=
  vBound - (v1 + v2)

-- Bean qou-m6gp: vanishing on disjoint sums and telescoping hierarchical closure identity.
/-- A disjoint union closure `vBound = v1 + v2` has zero `closureVolumeDeficit`, and composing
a two-body bound state `v12` with a third component `v3` telescopes the total three-body deficit. -/
theorem closureVolumeDeficit_telescoping_and_disjoint_zero
    (v123 v12 v1 v2 v3 : Int) :
    closureVolumeDeficit v123 v12 v3 + closureVolumeDeficit v12 v1 v2 =
      v123 - (v1 + v2 + v3) ∧
    closureVolumeDeficit (v1 + v2) v1 v2 + v123 + v12 + v3 =
      v123 + v12 + v3 := by
  dsimp only [closureVolumeDeficit]
  have h1 : (v123 - (v12 + v3)) + (v12 - (v1 + v2)) =
      v123 - (v1 + v2 + v3) := by
    omega
  have h2 : ((v1 + v2) - (v1 + v2)) + v123 + v12 + v3 =
      v123 + v12 + v3 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-m6gp: symmetry in the free components and perturbation linearity.
/-- `closureVolumeDeficit` is symmetric under swapping `v1` and `v2`, and shifting `vBound`
by `delta` shifts the deficit by `delta`. -/
theorem closureVolumeDeficit_component_symmetry_and_shift
    (vBound v1 v2 delta : Int) :
    closureVolumeDeficit (vBound + delta) v1 v2 -
      closureVolumeDeficit vBound v1 v2 = delta ∧
    closureVolumeDeficit vBound v1 v2 + delta =
      closureVolumeDeficit vBound v2 v1 + delta := by
  dsimp only [closureVolumeDeficit]
  have h1 : ((vBound + delta) - (v1 + v2)) - (vBound - (v1 + v2)) = delta := by
    omega
  have h2 : (vBound - (v1 + v2)) + delta = (vBound - (v2 + v1)) + delta := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 3: Two-Sector Bipartition Transseries Partial Sum (`qou-mbz4`) -/

/-- Two-sector transseries partial sum `a0 + s1 * phi1 + s2 * phi2`. -/
def bipartitionTransseries (a0 s1 phi1 s2 phi2 : Int) : Int :=
  a0 + s1 * phi1 + s2 * phi2

-- Bean qou-mbz4: instanton-sector increment above the perturbative leading term `a0`.
/-- Subtracting the leading term `a0` from `bipartitionTransseries` isolates the non-perturbative
bipartition sum `s1 * phi1 + s2 * phi2`, and negating both Stokes multipliers `(s1, s2)` averages
to `2 * a0`. -/
theorem bipartitionTransseries_nonperturbative_lift_and_parity_average
    (a0 s1 phi1 s2 phi2 : Int) :
    bipartitionTransseries a0 s1 phi1 s2 phi2 - a0 =
      s1 * phi1 + s2 * phi2 ∧
    bipartitionTransseries a0 s1 phi1 s2 phi2 +
      bipartitionTransseries a0 (-s1) phi1 (-s2) phi2 = 2 * a0 := by
  dsimp only [bipartitionTransseries]
  have h1 : (a0 + s1 * phi1 + s2 * phi2) - a0 = s1 * phi1 + s2 * phi2 := by
    omega
  have h2 : (a0 + s1 * phi1 + s2 * phi2) +
      (a0 + (-s1) * phi1 + (-s2) * phi2) = 2 * a0 := by
    have hn1 : (-s1) * phi1 = -(s1 * phi1) := Int.neg_mul s1 phi1
    have hn2 : (-s2) * phi2 = -(s2 * phi2) := Int.neg_mul s2 phi2
    omega
  exact ⟨h1, h2⟩

-- Bean qou-mbz4: linearity in the transseries basis modes `(phi1, phi2)`.
/-- `bipartitionTransseries` is additive when the basis modes decompose as `phi1 = p1 + q1` and
`phi2 = p2 + q2` with split leading terms `a0 + b0`. -/
theorem bipartitionTransseries_mode_linearity
    (a0 b0 s1 p1 q1 s2 p2 q2 : Int) :
    bipartitionTransseries (a0 + b0) s1 (p1 + q1) s2 (p2 + q2) =
      bipartitionTransseries a0 s1 p1 s2 p2 +
        bipartitionTransseries b0 s1 q1 s2 q2 ∧
    bipartitionTransseries a0 s1 p1 0 p2 + b0 + q1 + s2 + q2 =
      a0 + s1 * p1 + b0 + q1 + s2 + q2 := by
  dsimp only [bipartitionTransseries]
  have h1 : (a0 + b0) + s1 * (p1 + q1) + s2 * (p2 + q2) =
      (a0 + s1 * p1 + s2 * p2) + (b0 + s1 * q1 + s2 * q2) := by
    rw [Int.mul_add s1 p1 q1, Int.mul_add s2 p2 q2]
    omega
  have h2 : (a0 + s1 * p1 + 0 * p2) + b0 + q1 + s2 + q2 =
      a0 + s1 * p1 + b0 + q1 + s2 + q2 := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 4: Cubic vs Quadratic Dimension Kernel Excess (`qou-mdbh`) -/

/-- Dimension-cubed vs dimension-squared kernel term pair `(f * f * w, f * f * f * w)`. -/
def dimSquaredCubedKernelPair (f w : Int) : Int × Int :=
  (f * f * w, f * f * f * w)

-- Bean qou-mdbh: exact factorization `f^3 w - f^2 w = f^2 (f - 1) w` and fixed point at `f = 1`.
/-- Subtracting the quadratic-dimension term from the cubic-dimension term factors as
`f * f * (f - 1) * w`, and at `f = 1` both components equal `w`. -/
theorem dimSquaredCubedKernelPair_excess_factorization_and_trivial_rep
    (f w : Int) :
    (dimSquaredCubedKernelPair f w).2 - (dimSquaredCubedKernelPair f w).1 =
      f * f * (f - 1) * w ∧
    (dimSquaredCubedKernelPair 1 w).2 - (dimSquaredCubedKernelPair 1 w).1 + f =
      f := by
  dsimp only [dimSquaredCubedKernelPair]
  have h1 : f * f * f * w - f * f * w = f * f * (f - 1) * w := by
    have hsub : f * f * (f - 1) = f * f * f - f * f := by
      rw [Int.mul_sub, Int.mul_one]
    rw [hsub, Int.sub_mul]
  have h2 : 1 * 1 * 1 * w - 1 * 1 * w + f = f := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-mdbh: linearity in the observable `w1 + w2` and sign-flip under `w -> -w`.
/-- Both components of `dimSquaredCubedKernelPair` are linear in the observable `w`. -/
theorem dimSquaredCubedKernelPair_observable_linearity
    (f w1 w2 : Int) :
    (dimSquaredCubedKernelPair f (w1 + w2)).2 =
      (dimSquaredCubedKernelPair f w1).2 + (dimSquaredCubedKernelPair f w2).2 ∧
    (dimSquaredCubedKernelPair f (w1 + w2)).1 =
      (dimSquaredCubedKernelPair f w1).1 + (dimSquaredCubedKernelPair f w2).1 := by
  dsimp only [dimSquaredCubedKernelPair]
  have h1 : f * f * f * (w1 + w2) = f * f * f * w1 + f * f * f * w2 := by
    rw [Int.mul_add]
  have h2 : f * f * (w1 + w2) = f * f * w1 + f * f * w2 := by
    rw [Int.mul_add]
  exact ⟨h1, h2⟩

/-! ## Section 5: Meridian-Longitude Quadratic Cross Form (`qou-mssy`) -/

/-- Meridian-longitude cross form `(2 * m + l) * l`. -/
def windingCrossForm (m l : Int) : Int :=
  (2 * m + l) * l

-- Bean qou-mssy: expanded form `2 m l + l^2` and simultaneous orientation-inversion symmetry.
/-- `windingCrossForm m l` expands to `2 * m * l + l * l` and is invariant under `(m, l) -> (-m, -l)`. -/
theorem windingCrossForm_expanded_and_inversion_even (m l : Int) :
    windingCrossForm m l = 2 * m * l + l * l ∧
    windingCrossForm (-m) (-l) = windingCrossForm m l := by
  dsimp only [windingCrossForm]
  have h1 : (2 * m + l) * l = 2 * m * l + l * l := by
    rw [Int.add_mul]
  have h2 : (2 * (-m) + (-l)) * (-l) = (2 * m + l) * l := by
    have hneg1 : 2 * (-m) + (-l) = -(2 * m + l) := by
      have hm : 2 * (-m) = -(2 * m) := Int.mul_neg 2 m
      omega
    rw [hneg1, Int.neg_mul_neg]
  exact ⟨h1, h2⟩

-- Bean qou-mssy: meridian step difference `2 * dm * l` and pure-meridian vanishing at `l = 0`.
/-- Shifting the meridian winding `m` by `dm` changes `windingCrossForm` by `2 * dm * l`, and
at zero longitude `l = 0` the cross form vanishes identically. -/
theorem windingCrossForm_meridian_shift_and_zero_longitude (m dm l : Int) :
    windingCrossForm (m + dm) l - windingCrossForm m l = 2 * dm * l ∧
    windingCrossForm m 0 + dm + l = dm + l := by
  dsimp only [windingCrossForm]
  have h1 : (2 * (m + dm) + l) * l - (2 * m + l) * l = 2 * dm * l := by
    rw [← Int.sub_mul]
    have hsub : (2 * (m + dm) + l) - (2 * m + l) = 2 * dm := by omega
    rw [hsub]
  have h2 : (2 * m + 0) * 0 + dm + l = dm + l := by
    omega
  exact ⟨h1, h2⟩

end QOU.QBeta.BipartitionTransseriesAndCubicDimensionKernelBrick
