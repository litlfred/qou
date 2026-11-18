set_option autoImplicit false

/-!
# Triangular Bar Involution, Length-2 Quadratic Defect, Right-Multiplication Dichotomy, Root Parameter Rescaling, and Writhe Homomorphism

Formalizes five foundational algebraic identities over `Int` (`qou-gmfz`, `qou-img9`, `qou-phir`, `qou-siin`, `qou-l25z`):

1. **`qou-gmfz` (Triangular Bar Involution and Classical-Limit Observation):**
   The upper-triangular bar operator `triBar d (x0, x1) = (x0 + d * x1, x1)` is involutive under sign reversal `d ↦ -d` (`triBar (-d) (triBar d v) = v`), reduces to the identity at `d = 0`, and induces the observation difference `obsLinear s0 s1 (triBar d v) - obsLinear s0 s1 v = (s0 * d) * v.x1`.

2. **`qou-img9` (Length-2 Word Quadratic Residual vs Simple-Reflection Vanishing):**
   For the simple-reflection diagonal operators `reflGen1 q = (q, -1)` and `reflGen2 q = (-1, q)`, each generator satisfies the monic quadratic relation `monicQuadDiag q (reflGen1 q) = (0, 0)` and `monicQuadDiag q (reflGen2 q) = (0, 0)`, whereas their length-2 product `wordLen2 q = (-q, -q)` has residual `(2 * q * (q - 1), 2 * q * (q - 1))`.

3. **`qou-phir` (Length-Dichotomy Right-Multiplication Operator on Rank-1 Free Module):**
   The length-dichotomy right-multiplication operator `rightDichotomyOp q (x0, x1) = (q * x1, x0 + (q - 1) * x1)` sends `(1, 0) ↦ (0, 1)` and `(0, 1) ↦ (q, q - 1)`, and satisfies the monic quadratic identity `rightDichotomyOp q (rightDichotomyOp q v) = vecAdd (vecScale (q - 1) (rightDichotomyOp q v)) (vecScale q v)` for all `v`.

4. **`qou-siin` (Root-Parameter Quadratic Rescaling and Chain Euler Invariance):**
   Rescaling the root-balanced quadratic polynomial `rootQuadPoly u v n = n^2 - (u - v) * n - u * v` by `t = u * n` yields `rescaledQuadPoly u v (u * n) = (u * u) * rootQuadPoly u v n`, and the 3-term alternating chain Euler characteristic `altChainEuler3 b0 b1 b2 = b0 - b1 + b2` is invariant under boundary rank shifts `(b0 + d1, b1 + d1 + d2, b2 + d2)`.

5. **`qou-l25z` (Word Writhe Homomorphism and Relator Exponent-Sum Vanishing):**
   The far-commutator relator exponent sum `farCommRelatorWrithe e_i e_j = e_i + e_j - e_i - e_j` vanishes for arbitrary generator weights `e_i, e_j`, while the length-3 braid relator exponent sum `braidRelatorWrithe e_i e_j = (e_i + e_j + e_i) - (e_j + e_i + e_j)` equals `e_i - e_j` and vanishes whenever adjacent generators carry equal weight `e_i = e_j`.
-/

namespace QOU.Foundations.TriangularBarInvolutionLengthTwoQuadraticDefectRightMultiplicationDichotomyRootParameterRescalingWritheHomomorphism

/-! ## Section 1: Triangular Bar Involution and Classical-Limit Observation (`qou-gmfz`) -/

/-- Two-component integer vector representing coordinates in a rank-2 module. -/
@[ext]
structure Vec2 where
  x0 : Int
  x1 : Int
  deriving DecidableEq, Repr

/-- Upper-triangular bar operator with off-diagonal bar defect `d`. -/
def triBar (d : Int) (v : Vec2) : Vec2 :=
  ⟨v.x0 + d * v.x1, v.x1⟩

/-- Linear observation functional with basis weights `s0, s1`. -/
def obsLinear (s0 s1 : Int) (v : Vec2) : Int :=
  s0 * v.x0 + s1 * v.x1

/-- **`qou-gmfz` (Theorem 1a — Semilinear Bar Involutivity and Classical-Limit Shift):**
    `triBar (-d) (triBar d v) = v`, `triBar 0 v = v`, and
    `obsLinear s0 s1 (triBar d v) - obsLinear s0 s1 v = (s0 * d) * v.x1`. -/
theorem triBar_involutive_and_classical_limit (d s0 s1 : Int) (v : Vec2) :
    triBar (-d) (triBar d v) = v ∧
    triBar 0 v = v ∧
    obsLinear s0 s1 (triBar d v) - obsLinear s0 s1 v = (s0 * d) * v.x1 := by
  refine ⟨?_, ?_, ?_⟩
  · ext
    · dsimp only [triBar]
      rw [Int.neg_mul d v.x1]
      omega
    · rfl
  · ext
    · dsimp only [triBar]
      omega
    · rfl
  · dsimp only [obsLinear, triBar]
    rw [Int.mul_add s0 v.x0 (d * v.x1), ← Int.mul_assoc s0 d v.x1]
    omega

/-! ## Section 2: Length-2 Word Quadratic Defect vs Simple-Reflection Vanishing (`qou-img9`) -/

/-- Two-by-two diagonal integer matrix. -/
@[ext]
structure DiagMat2 where
  d0 : Int
  d1 : Int
  deriving DecidableEq, Repr

/-- Entrywise multiplication of diagonal matrices. -/
def diagMul (A B : DiagMat2) : DiagMat2 :=
  ⟨A.d0 * B.d0, A.d1 * B.d1⟩

/-- Monic quadratic residual `A^2 - (q - 1) * A - q * I` on diagonal matrices. -/
def monicQuadDiag (q : Int) (A : DiagMat2) : DiagMat2 :=
  ⟨A.d0 * A.d0 - (q - 1) * A.d0 - q, A.d1 * A.d1 - (q - 1) * A.d1 - q⟩

/-- First simple-reflection diagonal generator `(q, -1)`. -/
def reflGen1 (q : Int) : DiagMat2 :=
  ⟨q, -1⟩

/-- Second simple-reflection diagonal generator `(-1, q)`. -/
def reflGen2 (q : Int) : DiagMat2 :=
  ⟨-1, q⟩

/-- Length-2 product `reflGen1 q * reflGen2 q = (-q, -q)`. -/
def wordLen2 (q : Int) : DiagMat2 :=
  diagMul (reflGen1 q) (reflGen2 q)

/-- **`qou-img9` (Theorem 2a — Simple-Reflection Vanishing vs Length-2 Quadratic Residual):**
    Both length-1 generators satisfy `monicQuadDiag q (reflGen1 q) = ⟨0, 0⟩` and
    `monicQuadDiag q (reflGen2 q) = ⟨0, 0⟩`, whereas the length-2 product satisfies
    `monicQuadDiag q (wordLen2 q) = ⟨2 * (q * q) - 2 * q, 2 * (q * q) - 2 * q⟩`. -/
theorem simple_refl_quad_zero_vs_wordLen2_residual (q : Int) :
    monicQuadDiag q (reflGen1 q) = ⟨0, 0⟩ ∧
    monicQuadDiag q (reflGen2 q) = ⟨0, 0⟩ ∧
    monicQuadDiag q (wordLen2 q) = ⟨2 * (q * q) - 2 * q, 2 * (q * q) - 2 * q⟩ := by
  have hq : q * q - (q - 1) * q - q = 0 := by
    rw [Int.sub_mul q 1 q]
    omega
  have hm1 : (-1) * (-1) - (q - 1) * (-1) - q = 0 := by
    omega
  refine ⟨?_, ?_, ?_⟩
  · ext
    · dsimp only [monicQuadDiag, reflGen1]
      exact hq
    · dsimp only [monicQuadDiag, reflGen1]
      exact hm1
  · ext
    · dsimp only [monicQuadDiag, reflGen2]
      exact hm1
    · dsimp only [monicQuadDiag, reflGen2]
      exact hq
  · ext
    · dsimp only [monicQuadDiag, wordLen2, diagMul, reflGen1, reflGen2]
      have h1 : (q * -1) * (q * -1) = q * q := by
        rw [Int.mul_neg q 1, Int.mul_one q, Int.neg_mul q (-q), Int.mul_neg q q, Int.neg_neg]
      have h2 : (q - 1) * (q * -1) = -(q * q) + q := by
        rw [Int.mul_neg q 1, Int.mul_one q, Int.mul_neg (q - 1) q, Int.sub_mul q 1 q]
        omega
      rw [h1, h2]
      omega
    · dsimp only [monicQuadDiag, wordLen2, diagMul, reflGen1, reflGen2]
      have h1 : (-1 * q) * (-1 * q) = q * q := by
        rw [Int.neg_mul 1 q, Int.one_mul q, Int.neg_mul q (-q), Int.mul_neg q q, Int.neg_neg]
      have h2 : (q - 1) * (-1 * q) = -(q * q) + q := by
        rw [Int.neg_mul 1 q, Int.one_mul q, Int.mul_neg (q - 1) q, Int.sub_mul q 1 q]
        omega
      rw [h1, h2]
      omega

/-! ## Section 3: Length-Dichotomy Right-Multiplication Operator (`qou-phir`) -/

/-- Componentwise addition on `Vec2`. -/
def vecAdd (u v : Vec2) : Vec2 :=
  ⟨u.x0 + v.x0, u.x1 + v.x1⟩

/-- Scalar multiplication on `Vec2`. -/
def vecScale (c : Int) (v : Vec2) : Vec2 :=
  ⟨c * v.x0, c * v.x1⟩

/-- Length-dichotomy right-multiplication operator on the rank-2 free module indexed by `{1, s}`. -/
def rightDichotomyOp (q : Int) (v : Vec2) : Vec2 :=
  ⟨q * v.x1, v.x0 + (q - 1) * v.x1⟩

/-- **`qou-phir` (Theorem 3a — Basis Action and Monic Quadratic Relation of `rightDichotomyOp`):**
    `rightDichotomyOp q ⟨1, 0⟩ = ⟨0, 1⟩`, `rightDichotomyOp q ⟨0, 1⟩ = ⟨q, q - 1⟩`, and
    `rightDichotomyOp q (rightDichotomyOp q v) = vecAdd (vecScale (q - 1) (rightDichotomyOp q v)) (vecScale q v)`. -/
theorem rightDichotomyOp_basis_and_quadratic_identity (q : Int) (v : Vec2) :
    rightDichotomyOp q ⟨1, 0⟩ = ⟨0, 1⟩ ∧
    rightDichotomyOp q ⟨0, 1⟩ = ⟨q, q - 1⟩ ∧
    rightDichotomyOp q (rightDichotomyOp q v) =
      vecAdd (vecScale (q - 1) (rightDichotomyOp q v)) (vecScale q v) := by
  refine ⟨?_, ?_, ?_⟩
  · ext <;> dsimp only [rightDichotomyOp] <;> omega
  · ext <;> dsimp only [rightDichotomyOp] <;> omega
  · ext
    · dsimp only [rightDichotomyOp, vecAdd, vecScale]
      rw [Int.mul_add q v.x0 ((q - 1) * v.x1),
          Int.mul_comm (q - 1) (q * v.x1),
          Int.mul_assoc q v.x1 (q - 1),
          Int.mul_comm v.x1 (q - 1)]
      omega
    · dsimp only [rightDichotomyOp, vecAdd, vecScale]
      rw [Int.mul_add (q - 1) v.x0 ((q - 1) * v.x1)]
      omega

/-! ## Section 4: Root-Parameter Quadratic Rescaling and Chain Euler Invariance (`qou-siin`) -/

/-- Root-balanced quadratic polynomial `n^2 - (u - v) * n - u * v`. -/
def rootQuadPoly (u v n : Int) : Int :=
  n * n - (u - v) * n - u * v

/-- Rescaled quadratic polynomial `t^2 - (u^2 - u * v) * t - u^2 * (u * v)`. -/
def rescaledQuadPoly (u v t : Int) : Int :=
  t * t - (u * u - u * v) * t - (u * u) * (u * v)

/-- Three-term alternating chain Euler characteristic `b0 - b1 + b2`. -/
def altChainEuler3 (b0 b1 b2 : Int) : Int :=
  b0 - b1 + b2

/-- **`qou-siin` (Theorem 4a — Root-Parameter Rescaling and Alternating Chain Euler Invariance):**
    `rescaledQuadPoly u v (u * n) = (u * u) * rootQuadPoly u v n` and
    `altChainEuler3 (b0 + d1) (b1 + d1 + d2) (b2 + d2) = altChainEuler3 b0 b1 b2`. -/
theorem rescaledQuadPoly_eq_mul_rootQuadPoly_and_euler_invariance
    (u v n b0 b1 b2 d1 d2 : Int) :
    rescaledQuadPoly u v (u * n) = (u * u) * rootQuadPoly u v n ∧
    altChainEuler3 (b0 + d1) (b1 + d1 + d2) (b2 + d2) = altChainEuler3 b0 b1 b2 := by
  constructor
  · dsimp only [rescaledQuadPoly, rootQuadPoly]
    have h1 : (u * n) * (u * n) = (u * u) * (n * n) := by
      rw [Int.mul_assoc u n (u * n), ← Int.mul_assoc n u n,
          Int.mul_comm n u, Int.mul_assoc u n n, ← Int.mul_assoc u u (n * n)]
    have h2 : (u * u - u * v) * (u * n) = (u * u) * ((u - v) * n) := by
      rw [← Int.mul_sub u u v, Int.mul_assoc u (u - v) (u * n),
          ← Int.mul_assoc (u - v) u n, Int.mul_comm (u - v) u,
          Int.mul_assoc u (u - v) n, ← Int.mul_assoc u u ((u - v) * n)]
    rw [h1, h2, Int.mul_sub (u * u) (n * n - (u - v) * n) (u * v),
        Int.mul_sub (u * u) (n * n) ((u - v) * n)]
  · dsimp only [altChainEuler3]
    omega

/-! ## Section 5: Word Writhe Homomorphism and Relator Exponent-Sum Vanishing (`qou-l25z`) -/

/-- Additive writhe of a concatenated two-factor word. -/
def wordWritheConcat (w1 w2 : Int) : Int :=
  w1 + w2

/-- Exponent sum of the far-commutator relator `g_i * g_j * g_i⁻¹ * g_j⁻¹`. -/
def farCommRelatorWrithe (e_i e_j : Int) : Int :=
  e_i + e_j - e_i - e_j

/-- Exponent sum of the length-3 cubic braid relator `(g_i * g_j * g_i) * (g_j * g_i * g_j)⁻¹`. -/
def braidRelatorWrithe (e_i e_j : Int) : Int :=
  (e_i + e_j + e_i) - (e_j + e_i + e_j)

/-- **`qou-l25z` (Theorem 5a — Relator Exponent-Sum Vanishing and Writhe Associativity):**
    `farCommRelatorWrithe e_i e_j = 0`, `braidRelatorWrithe e_i e_j = e_i - e_j`,
    `braidRelatorWrithe w w = 0`, and `wordWritheConcat (wordWritheConcat w1 w2) w3 = wordWritheConcat w1 (wordWritheConcat w2 w3)`. -/
theorem writhe_relators_and_uniform_generator_vanishing (e_i e_j w w1 w2 w3 : Int) :
    farCommRelatorWrithe e_i e_j = 0 ∧
    braidRelatorWrithe e_i e_j = e_i - e_j ∧
    braidRelatorWrithe w w = 0 ∧
    wordWritheConcat (wordWritheConcat w1 w2) w3 = wordWritheConcat w1 (wordWritheConcat w2 w3) := by
  dsimp only [farCommRelatorWrithe, braidRelatorWrithe, wordWritheConcat]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> omega

end QOU.Foundations.TriangularBarInvolutionLengthTwoQuadraticDefectRightMultiplicationDichotomyRootParameterRescalingWritheHomomorphism
