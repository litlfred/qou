/-!
# N=5 Level-Six Interpolation Threshold and Three-Link Cyclotomic Triad (`bwsc`, `qou-zkkv`)

Formalizes two linked algebraic structures in the braid/knot sector:

1. **Level-6 Fibre Interpolation Threshold for `n = 5` Block Polynomials (`bwsc`):**
   - The `n = 5` mark-6 block polynomial for `(3,1,1)` is `d((3,1,1)) = [5]_q + 1 = t^4 - 3 t^2 + 2`
     of degree `4` in `t`, whereas the six-strand quantum integer `[6]_q = t^5 - 4 t^3 + 3 t` has
     degree `5` in `t`.
   - Both polynomials evaluate to `6` at the classical specialization `t = 2`, which is why the
     mark is named `6`, while their constant terms (`2` vs `0`) and higher evaluations (`20` vs `120`
     at `t = 3`) separate them.
   - Because the maximum degree across the `n = 5` block polynomials `(0, 3, 4, 4)` is `4` rather
     than `5`, polynomial interpolation requires `4 + 1 = 5` distinct interior fibre points, which
     are supplied at level `N = 6` (`k = 1..5`), strictly below `N = 7`.

2. **Three-Component Link Symmetric Cyclotomic Cutoff and Degree Step (`qou-zkkv`, Ref: [habiro2000] Prop. 7.1):**
   - In the explicit closed formula for the colored invariant of the three-component link (Prop. 7.1,
     Sec. 7), the summation cutoff `min(j_1, j_2, j_3)` is totally symmetric in the three colour
     indices and bounded above by each individual colour, while the cyclotomic product degree advances
     by `6` per summation step `k`.
-/

namespace QOU.BraidKnot.N5LevelSixRootThresholdAndThreeLinkTriad

/-- The `n = 5` mark-6 block polynomial `d((3,1,1))(t) = t^4 - 3 t^2 + 2` of degree `4`. -/
def n5MarkSixBlockPoly (t : Int) : Int :=
  t ^ 4 - 3 * t ^ 2 + 2

/-- The degree-5 polynomial `[6]_q(t) = t^5 - 4 t^3 + 3 t`. -/
def qIntSixPoly (t : Int) : Int :=
  t ^ 5 - 4 * t ^ 3 + 3 * t

/-- Maximum polynomial degree in `t` across the four `n = 5` blocks `(0, 3, 4, 4)`. -/
def n5BlockMaxDegree : Int := 4

/-- Number of interior fold points `2 cos(k pi / N)` (`k = 1 .. N - 1`) at level `N`. -/
def levelInteriorFoldPoints (levelN : Int) : Int :=
  levelN - 1

/-- Interpolation point surplus `nPts - (deg + 1)` for a polynomial of degree `deg`. -/
def interpolationSurplus (nPts deg : Int) : Int :=
  nPts - (deg + 1)

/-- At `t = 2`, `n5MarkSixBlockPoly` and `qIntSixPoly` both equal `6`, while at `t = 0`, `t = -2`,
    and `t = 3` they separate cleanly (`2` vs `0` at `t = 0`, `6` vs `-6` at `t = -2`, and
    `56` vs `144` at `t = 3`). -/
theorem n5MarkSixBlockPoly_classical_coincidence_and_separation :
    n5MarkSixBlockPoly 2 = 6 ∧
    qIntSixPoly 2 = 6 ∧
    n5MarkSixBlockPoly 0 - qIntSixPoly 0 = 2 ∧
    n5MarkSixBlockPoly (-2) + qIntSixPoly (-2) = 0 ∧
    qIntSixPoly 3 - n5MarkSixBlockPoly 3 = 88 := by
  have h1 : n5MarkSixBlockPoly 2 = 6 := rfl
  have h2 : qIntSixPoly 2 = 6 := rfl
  have h3 : n5MarkSixBlockPoly 0 - qIntSixPoly 0 = 2 := rfl
  have h4 : n5MarkSixBlockPoly (-2) + qIntSixPoly (-2) = 0 := rfl
  have h5 : qIntSixPoly 3 - n5MarkSixBlockPoly 3 = 88 := rfl
  exact ⟨h1, h2, h3, h4, h5⟩

/-- Both `n5MarkSixBlockPoly` and `qIntSixPoly` vanish at `t = 1` and `t = -1`, while
    `n5MarkSixBlockPoly` has even parity at `t = ±2, ±3` and `qIntSixPoly` has odd parity. -/
theorem n5MarkSixBlockPoly_roots_and_parity_contrast :
    n5MarkSixBlockPoly 1 = 0 ∧
    n5MarkSixBlockPoly (-1) = 0 ∧
    qIntSixPoly 1 = 0 ∧
    qIntSixPoly (-1) = 0 ∧
    n5MarkSixBlockPoly 3 - n5MarkSixBlockPoly (-3) = 0 ∧
    qIntSixPoly 3 + qIntSixPoly (-3) = 0 := by
  have h1 : n5MarkSixBlockPoly 1 = 0 := rfl
  have h2 : n5MarkSixBlockPoly (-1) = 0 := rfl
  have h3 : qIntSixPoly 1 = 0 := rfl
  have h4 : qIntSixPoly (-1) = 0 := rfl
  have h5 : n5MarkSixBlockPoly 3 - n5MarkSixBlockPoly (-3) = 0 := rfl
  have h6 : qIntSixPoly 3 + qIntSixPoly (-3) = 0 := rfl
  exact ⟨h1, h2, h3, h4, h5, h6⟩

/-- For any level `levelN ≥ 6`, the interior fold-point count `levelN - 1` meets or exceeds the
    `5`-point interpolation threshold for degree `4`, with exact saturation at `levelN = 6`
    and a `1`-point deficit at `levelN = 5`. -/
theorem n5_level_six_threshold_sharpness (levelN : Int) (hLevel : 6 ≤ levelN) :
    0 ≤ interpolationSurplus (levelInteriorFoldPoints levelN) n5BlockMaxDegree ∧
    interpolationSurplus (levelInteriorFoldPoints 6) n5BlockMaxDegree = 0 ∧
    interpolationSurplus (levelInteriorFoldPoints 5) n5BlockMaxDegree = -1 ∧
    interpolationSurplus (levelInteriorFoldPoints 6) 5 = -1 := by
  dsimp [interpolationSurplus, levelInteriorFoldPoints, n5BlockMaxDegree]
  refine ⟨?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · omega
  · omega

/-- Three-colour summation cutoff `min(j1, min(j2, j3))` for the symmetric three-component link sum. -/
def threeLinkColorCutoff (j1 j2 j3 : Nat) : Nat :=
  min j1 (min j2 j3)

/-- Cyclotomic triple-factor degree `6 * k` at summation index `k`. -/
def threeLinkCyclotomicDegree (k : Int) : Int :=
  6 * k

/-- Total permutation symmetry and componentwise upper bounds for `threeLinkColorCutoff`. -/
theorem threeLinkColorCutoff_symmetric_and_bounded (j1 j2 j3 : Nat) :
    threeLinkColorCutoff j1 j2 j3 = threeLinkColorCutoff j2 j1 j3 ∧
    threeLinkColorCutoff j1 j2 j3 = threeLinkColorCutoff j1 j3 j2 ∧
    threeLinkColorCutoff j1 j2 j3 ≤ j1 ∧
    threeLinkColorCutoff j1 j2 j3 ≤ j2 ∧
    threeLinkColorCutoff j1 j2 j3 ≤ j3 := by
  dsimp [threeLinkColorCutoff]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · omega
  · omega
  · omega

/-- The cyclotomic triple-product degree advances by `6` on each summation step `k → k + 1`
    and is strictly positive for `k ≥ 1`. -/
theorem threeLinkCyclotomicDegree_step_and_positivity (k : Int) (hPos : 1 ≤ k) :
    threeLinkCyclotomicDegree (k + 1) - threeLinkCyclotomicDegree k = 6 ∧
    6 ≤ threeLinkCyclotomicDegree k ∧
    threeLinkCyclotomicDegree 0 = 0 := by
  dsimp [threeLinkCyclotomicDegree]
  refine ⟨?_, ?_, ?_⟩
  · omega
  · omega
  · omega

end QOU.BraidKnot.N5LevelSixRootThresholdAndThreeLinkTriad
