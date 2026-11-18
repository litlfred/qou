set_option autoImplicit false

/-!
# Filtered Differential Square, Idempotent Block Decomposition, Isometry Transport, Overlap Commutation Defect, and Diamond Confluence

Formalizes five foundational algebraic identities over `Int` (`qou-pan0`, `qou-tgci`, `qou-ykt7`, `qou-bq5e`, `qou-ch3j`):

1. **`qou-pan0` (Filtered Differential Square and Two-Square Norm Multiplicativity):**
   On 3-component integer vectors `Vec3`, the stage-1 filtered differential `filteredDiff1 a (x0, x1, x2) = (a * x1, a * x2, 0)` satisfies `filteredDiff1 a (filteredDiff1 a v) = filteredDiff2 (a * a) v` and `filteredDiff1 a (filteredDiff1 a (filteredDiff1 a v)) = (0, 0, 0)`, and the quadratic norm `pairNormSq x y = x^2 + y^2` satisfies `pairNormSq (x1 * x2 - y1 * y2) (x1 * y2 + y1 * x2) = pairNormSq x1 y1 * pairNormSq x2 y2`.

2. **`qou-tgci` (Complementary Idempotent Decomposition and Mutual Orthogonality):**
   For the complementary operators `projPlus a b (x0, x1) = (a * x0 + b * x1, 0)` and `projMinus a b (x0, x1) = (-(b * x1), a * x1)`, their sum equals `vecScale a v`, each satisfies scaled idempotence `projPlus a b (projPlus a b v) = vecScale a (projPlus a b v)` and `projMinus a b (projMinus a b v) = vecScale a (projMinus a b v)`, and their cross-compositions vanish identically.

3. **`qou-ykt7` (Affine Isometry Inversion, Uniqueness Transport, and Displacement Additivity):**
   Under an involutive reflection sign `s * s = 1`, the affine isometry `isoMap s t x = s * x + t` and its inverse `isoInv s t y = s * (y - t)` satisfy `isoInv s t (isoMap s t x) = x` and `isoMap s t (isoInv s t y) = y`, transport equality (`isoMap s t x = isoMap s t y → x = y`), and satisfy `axisDisp x m + axisDisp m y = axisDisp x y` and `axisDisp (isoMap s t x) (isoMap s t y) = s * axisDisp x y`.

4. **`qou-bq5e` (Quadratic Overlap Commutation Defect vs Commuting Vanishing):**
   Comparing the two reduction branches `overlapBranchLeft p q xy y x c = p * xy + q * y + (2 * c) * x` and `overlapBranchRight p q xy y c = p * xy + q * y + p * c` yields `overlapDefect p q xy y x c = c * (2 * x - p)`, which vanishes at the commuting specialization `c = 0` (`overlapDefect p q xy y x 0 = 0`) and evaluates to `3` at `c = 1, p = 1, x = 2`.

5. **`qou-ch3j` (Diamond Confluence Join and Normal-Form Uniqueness on Weighted Words):**
   For the single-step weight drop `weightStep w d = w - d` and two reduction branches `branchA w d1 = weightStep w d1` and `branchB w d2 = weightStep w d2`, both 2-step continuations join at `diamondJoin w d1 d2 = w - d1 - d2`, and any two terminal evaluations agreeing with `diamondJoin w d1 d2` and `diamondJoin w d2 d1` are equal.
-/

namespace QOU.Foundations.FilteredDifferentialSquareIdempotentBlockDecompositionIsometryTransportFinitePresentationDiamondConfluence

/-! ## Section 1: Filtered Differential Square and Norm Multiplicativity (`qou-pan0`) -/

/-- Three-component integer vector representing a 3-stage filtered module. -/
@[ext]
structure Vec3 where
  x0 : Int
  x1 : Int
  x2 : Int
  deriving DecidableEq, Repr

/-- Stage-1 upper-triangular differential `(x0, x1, x2) ↦ (a * x1, a * x2, 0)`. -/
def filteredDiff1 (a : Int) (v : Vec3) : Vec3 :=
  ⟨a * v.x1, a * v.x2, 0⟩

/-- Stage-2 differential `(x0, x1, x2) ↦ (b * x2, 0, 0)`. -/
def filteredDiff2 (b : Int) (v : Vec3) : Vec3 :=
  ⟨b * v.x2, 0, 0⟩

/-- Two-component quadratic norm `x^2 + y^2`. -/
def pairNormSq (x y : Int) : Int :=
  x * x + y * y

/-- **`qou-pan0` (Theorem 1a — Filtered Differential Square, 3-Step Nilpotency, and Norm Multiplicativity):**
    `filteredDiff1 a (filteredDiff1 a v) = filteredDiff2 (a * a) v`,
    `filteredDiff1 a (filteredDiff1 a (filteredDiff1 a v)) = ⟨0, 0, 0⟩`, and
    `pairNormSq (x1 * x2 - y1 * y2) (x1 * y2 + y1 * x2) = pairNormSq x1 y1 * pairNormSq x2 y2`. -/
theorem filteredDiff_nilpotency_and_norm_multiplicativity
    (a x1 y1 x2 y2 : Int) (v : Vec3) :
    filteredDiff1 a (filteredDiff1 a v) = filteredDiff2 (a * a) v ∧
    filteredDiff1 a (filteredDiff1 a (filteredDiff1 a v)) = ⟨0, 0, 0⟩ ∧
    pairNormSq (x1 * x2 - y1 * y2) (x1 * y2 + y1 * x2) =
      pairNormSq x1 y1 * pairNormSq x2 y2 := by
  refine ⟨?_, ?_, ?_⟩
  · ext
    · dsimp only [filteredDiff1, filteredDiff2]
      rw [← Int.mul_assoc a a v.x2]
    · dsimp only [filteredDiff1, filteredDiff2]
      omega
    · rfl
  · ext <;> dsimp only [filteredDiff1] <;> omega
  · dsimp only [pairNormSq]
    rw [Int.sub_mul (x1 * x2) (y1 * y2) (x1 * x2 - y1 * y2),
        Int.mul_sub (x1 * x2) (x1 * x2) (y1 * y2),
        Int.mul_sub (y1 * y2) (x1 * x2) (y1 * y2),
        Int.add_mul (x1 * y2) (y1 * x2) (x1 * y2 + y1 * x2),
        Int.mul_add (x1 * y2) (x1 * y2) (y1 * x2),
        Int.mul_add (y1 * x2) (x1 * y2) (y1 * x2),
        Int.add_mul (x1 * x1) (y1 * y1) (x2 * x2 + y2 * y2),
        Int.mul_add (x1 * x1) (x2 * x2) (y2 * y2),
        Int.mul_add (y1 * y1) (x2 * x2) (y2 * y2)]
    have hxx : (x1 * x2) * (x1 * x2) = (x1 * x1) * (x2 * x2) := by
      rw [Int.mul_assoc x1 x2 (x1 * x2), ← Int.mul_assoc x2 x1 x2,
          Int.mul_comm x2 x1, Int.mul_assoc x1 x2 x2, ← Int.mul_assoc x1 x1 (x2 * x2)]
    have hyy : (y1 * y2) * (y1 * y2) = (y1 * y1) * (y2 * y2) := by
      rw [Int.mul_assoc y1 y2 (y1 * y2), ← Int.mul_assoc y2 y1 y2,
          Int.mul_comm y2 y1, Int.mul_assoc y1 y2 y2, ← Int.mul_assoc y1 y1 (y2 * y2)]
    have hxy : (x1 * y2) * (x1 * y2) = (x1 * x1) * (y2 * y2) := by
      rw [Int.mul_assoc x1 y2 (x1 * y2), ← Int.mul_assoc y2 x1 y2,
          Int.mul_comm y2 x1, Int.mul_assoc x1 y2 y2, ← Int.mul_assoc x1 x1 (y2 * y2)]
    have hyx : (y1 * x2) * (y1 * x2) = (y1 * y1) * (x2 * x2) := by
      rw [Int.mul_assoc y1 x2 (y1 * x2), ← Int.mul_assoc x2 y1 x2,
          Int.mul_comm x2 y1, Int.mul_assoc y1 x2 x2, ← Int.mul_assoc y1 y1 (x2 * x2)]
    have hc1 : (x1 * x2) * (y1 * y2) = (x1 * y2) * (y1 * x2) := by
      rw [Int.mul_assoc x1 x2 (y1 * y2), ← Int.mul_assoc x2 y1 y2,
          Int.mul_comm x2 y1, Int.mul_assoc y1 x2 y2,
          Int.mul_comm y1 (x2 * y2), Int.mul_comm x2 y2,
          Int.mul_assoc y2 x2 y1, Int.mul_comm x2 y1,
          ← Int.mul_assoc x1 y2 (y1 * x2)]
    have hc2 : (y1 * y2) * (x1 * x2) = (y1 * x2) * (x1 * y2) := by
      rw [Int.mul_comm (y1 * y2) (x1 * x2), hc1, Int.mul_comm (x1 * y2) (y1 * x2)]
    rw [hxx, hyy, hxy, hyx, hc1, hc2]
    omega

/-! ## Section 2: Complementary Idempotent Decomposition and Orthogonality (`qou-tgci`) -/

/-- Two-component integer vector. -/
@[ext]
structure Vec2 where
  x0 : Int
  x1 : Int
  deriving DecidableEq, Repr

/-- Componentwise vector addition on `Vec2`. -/
def vecAdd (u w : Vec2) : Vec2 :=
  ⟨u.x0 + w.x0, u.x1 + w.x1⟩

/-- Scalar multiplication on `Vec2`. -/
def vecScale (c : Int) (v : Vec2) : Vec2 :=
  ⟨c * v.x0, c * v.x1⟩

/-- First complementary block projection `(a * x0 + b * x1, 0)`. -/
def projPlus (a b : Int) (v : Vec2) : Vec2 :=
  ⟨a * v.x0 + b * v.x1, 0⟩

/-- Second complementary block projection `(-(b * x1), a * x1)`. -/
def projMinus (a b : Int) (v : Vec2) : Vec2 :=
  ⟨-(b * v.x1), a * v.x1⟩

/-- **`qou-tgci` (Theorem 2a — Completeness, Scaled Idempotence, and Orthogonality of Block Projections):**
    `vecAdd (projPlus a b v) (projMinus a b v) = vecScale a v`,
    `projPlus a b (projPlus a b v) = vecScale a (projPlus a b v)`,
    `projMinus a b (projMinus a b v) = vecScale a (projMinus a b v)`,
    `projMinus a b (projPlus a b v) = ⟨0, 0⟩`, and
    `projPlus a b (projMinus a b v) = ⟨0, 0⟩`. -/
theorem complementary_projection_decomposition_and_orthogonality (a b : Int) (v : Vec2) :
    vecAdd (projPlus a b v) (projMinus a b v) = vecScale a v ∧
    projPlus a b (projPlus a b v) = vecScale a (projPlus a b v) ∧
    projMinus a b (projMinus a b v) = vecScale a (projMinus a b v) ∧
    projMinus a b (projPlus a b v) = ⟨0, 0⟩ ∧
    projPlus a b (projMinus a b v) = ⟨0, 0⟩ := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · ext
    · dsimp only [vecAdd, projPlus, projMinus, vecScale]
      omega
    · dsimp only [vecAdd, projPlus, projMinus, vecScale]
      omega
  · ext
    · dsimp only [projPlus, vecScale]
      omega
    · dsimp only [projPlus, vecScale]
      omega
  · ext
    · dsimp only [projMinus, vecScale]
      rw [Int.mul_neg a (b * v.x1), ← Int.mul_assoc b a v.x1, Int.mul_comm b a, Int.mul_assoc a b v.x1]
    · dsimp only [projMinus, vecScale]
  · ext <;> dsimp only [projMinus, projPlus] <;> omega
  · ext
    · dsimp only [projPlus, projMinus]
      rw [Int.mul_neg a (b * v.x1), ← Int.mul_assoc a b v.x1,
          ← Int.mul_assoc b a v.x1, Int.mul_comm b a]
      omega
    · rfl

/-! ## Section 3: Bijective Isometry Transport and Displacement Additivity (`qou-ykt7`) -/

/-- Affine reflection-shift isometry `s * x + t`. -/
def isoMap (s t x : Int) : Int :=
  s * x + t

/-- Inverse affine reflection-shift isometry `s * (y - t)`. -/
def isoInv (s t y : Int) : Int :=
  s * (y - t)

/-- Signed displacement `y - x` along the 1D axis. -/
def axisDisp (x y : Int) : Int :=
  y - x

/-- **`qou-ykt7` (Theorem 3a — Isometry Inversion, Uniqueness Transport, and Displacement Equivariance):**
    When `s * s = 1`, `isoInv s t (isoMap s t x) = x`, `isoMap s t (isoInv s t y) = y`,
    `isoMap s t x = isoMap s t y → x = y`, and unconditionally
    `axisDisp x m + axisDisp m y = axisDisp x y` and
    `axisDisp (isoMap s t x) (isoMap s t y) = s * axisDisp x y`. -/
theorem isoMap_bijection_and_displacement_transport (s t x y m : Int) (hs : s * s = 1) :
    isoInv s t (isoMap s t x) = x ∧
    isoMap s t (isoInv s t y) = y ∧
    (isoMap s t x = isoMap s t y → x = y) ∧
    axisDisp x m + axisDisp m y = axisDisp x y ∧
    axisDisp (isoMap s t x) (isoMap s t y) = s * axisDisp x y := by
  have hleft : ∀ z : Int, isoInv s t (isoMap s t z) = z := by
    intro z
    dsimp only [isoInv, isoMap]
    have hsub : s * z + t - t = s * z := by omega
    rw [hsub, ← Int.mul_assoc s s z, hs, Int.one_mul z]
  refine ⟨hleft x, ?_, ?_, ?_, ?_⟩
  · dsimp only [isoMap, isoInv]
    rw [← Int.mul_assoc s s (y - t), hs, Int.one_mul (y - t)]
    omega
  · intro heq
    have hcongr := congrArg (isoInv s t) heq
    rw [hleft x, hleft y] at hcongr
    exact hcongr
  · dsimp only [axisDisp]
    omega
  · dsimp only [axisDisp, isoMap]
    rw [Int.mul_sub s y x]
    omega

/-! ## Section 4: Quadratic Overlap Commutation Defect vs Commuting Vanishing (`qou-bq5e`) -/

/-- Left-first reduction of overlap `y * x^2` with commutation defect `c`. -/
def overlapBranchLeft (p q xy y x c : Int) : Int :=
  p * xy + q * y + (2 * c) * x

/-- Right-first reduction of overlap `y * x^2` with commutation defect `c`. -/
def overlapBranchRight (p q xy y c : Int) : Int :=
  p * xy + q * y + p * c

/-- Difference between the left-first and right-first overlap reductions. -/
def overlapDefect (p q xy y x c : Int) : Int :=
  overlapBranchLeft p q xy y x c - overlapBranchRight p q xy y c

/-- **`qou-bq5e` (Theorem 4a — Overlap Commutation Defect Formula and Commuting Vanishing):**
    `overlapDefect p q xy y x c = c * (2 * x - p)`,
    `overlapDefect p q xy y x 0 = 0`, and
    `overlapDefect 1 q xy y 2 1 = 3`. -/
theorem overlapDefect_formula_and_commuting_vanishing (p q xy y x c : Int) :
    overlapDefect p q xy y x c = c * (2 * x - p) ∧
    overlapDefect p q xy y x 0 = 0 ∧
    overlapDefect 1 q xy y 2 1 = 3 := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp only [overlapDefect, overlapBranchLeft, overlapBranchRight]
    rw [Int.mul_sub c (2 * x) p, Int.mul_comm c (2 * x),
        Int.mul_assoc 2 x c, Int.mul_comm x c, ← Int.mul_assoc 2 c x,
        Int.mul_comm c p]
    omega
  · dsimp only [overlapDefect, overlapBranchLeft, overlapBranchRight]
    omega
  · dsimp only [overlapDefect, overlapBranchLeft, overlapBranchRight]
    omega

/-! ## Section 5: Diamond Confluence Join and Normal-Form Uniqueness (`qou-ch3j`) -/

/-- Single-step reduction weight drop `w - d`. -/
def weightStep (w d : Int) : Int :=
  w - d

/-- First reduction branch `w - d1`. -/
def branchA (w d1 : Int) : Int :=
  weightStep w d1

/-- Second reduction branch `w - d2`. -/
def branchB (w d2 : Int) : Int :=
  weightStep w d2

/-- Common confluence join `w - d1 - d2`. -/
def diamondJoin (w d1 d2 : Int) : Int :=
  w - d1 - d2

/-- **`qou-ch3j` (Theorem 5a — Diamond Confluence Join and Normal-Form Uniqueness):**
    `weightStep (branchA w d1) d2 = diamondJoin w d1 d2`,
    `weightStep (branchB w d2) d1 = diamondJoin w d1 d2`, and
    `diamondJoin w d1 d2 = diamondJoin w d2 d1`. -/
theorem diamondJoin_confluence_and_normal_form_uniqueness (w d1 d2 : Int) :
    weightStep (branchA w d1) d2 = diamondJoin w d1 d2 ∧
    weightStep (branchB w d2) d1 = diamondJoin w d1 d2 ∧
    diamondJoin w d1 d2 = diamondJoin w d2 d1 := by
  dsimp only [weightStep, branchA, branchB, diamondJoin]
  refine ⟨?_, ?_, ?_⟩ <;> omega

end QOU.Foundations.FilteredDifferentialSquareIdempotentBlockDecompositionIsometryTransportFinitePresentationDiamondConfluence
