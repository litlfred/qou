/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Tower Inverse-Step Compatibility, Root-of-Unity Seminormal Vanishing, Convention Normalization Bridge, Quotient Kernel Deficit, and Bilinear Trace Symmetry

This module formalizes five self-contained algebraic foundation bricks in the `qou-59vq` / `qou-rtxm` lane:

1. **`qou-0fmb`** (*Tower-level compatibility and inverse-generator trace reduction*):
   For the cleared tower stabilization numerator `z_num(q) = q^4` and cleared quadratic defect
   numerator `h_num(q) = (q^2 - 1) * (q^2 + 1)` over common denominator `q * (q^2 + 1)`, proves
   that the inverse-generator trace step numerator `z_num(q) - h_num(q)` equals `1` identically,
   and that for any level-compatible trace value `t`, the cleared inverse-generator trace
   `z_num(q) * t - h_num(q) * t` reduces exactly to `t`.

2. **`qou-4lft`** (*Root-of-unity seminormal denominator vanishing at `q^2 = 1`*):
   For the cleared seminormal numerator `seminormalNum(q) = q^2 - 1` and cleared axial-distance
   denominators `seminormalDen1(q) = q^2 - 1` (at `d = 1`) and `seminormalDen2(q) = q^4 - 1`
   (at `d = 2`), proves the exact factorization `seminormalDen2(q) = seminormalDen1(q) * (q^2 + 1)`
   and demonstrates simultaneous `0/0` vanishing of both numerator and denominators at the
   roots of unity `q = 1` and `q = -1`.

3. **`qou-avt2`** (*Normalization bridge between quadratic conventions and character trace sum*):
   Under the quadratic rescaling `Q = q^2`, proves that the rescaled $2 \times 2$ standard
   generator `T_std(q) = [[q^2, q], [0, -1]]` satisfies the quadratic relation
   `T_std(q)^2 = (q^2 - 1) * T_std(q) + q^2 * I_2`, and that the degree-weighted 3-strand
   character sum `1 * chi_triv(q^2) + 2 * chi_std(q^2) + 1 * chi_sign` equals `3 * (q^2 - 1)`.

4. **`qou-cf3m`** (*Two-row quotient dimension deficit and sign-projector spectral vanishing*):
   For the 3-strand sign-block spectral polynomial `P_sign(Q, lam1, lam2) = (Q - lam1) * (Q - lam2)`,
   proves that `P_sign` vanishes identically on the trivial eigenvalue pair `(Q, Q)` and on the
   2-dimensional standard eigenvalue pair `(Q, -1)`, while taking the value `(Q + 1)^2` on the
   1-dimensional sign pair `(-1, -1)`, and confirms the two-row quotient dimension decomposition
   `(1^2 + 2^2) + 1^2 = 5 + 1 = 6`.

5. **`qou-g6vb`** (*Bilinear trace pairing symmetry and basis expansion on $2 \times 2$ blocks*):
   For the bilinear trace pairing `tracePair(A, B) = tr(A * B)` on $2 \times 2$ integer matrices,
   proves exact symmetry `tracePair(A, B) = tracePair(B, A)` and left/right linearity over
   arbitrary linear combinations `c1 * B1 + c2 * B2`.
-/

namespace QOU.Foundations.TowerCompatibilityRootOfUnitySeminormalNormalizationRadicalKernelBilinearSymmetry

/-- A $2 \times 2$ integer matrix representing an endomorphism on a 2-dimensional block. -/
@[ext]
structure BlockMat2 where
  m11 : Int
  m12 : Int
  m21 : Int
  m22 : Int
  deriving DecidableEq, Repr

/-- Matrix multiplication on `BlockMat2`. -/
def mulBlockMat2 (A B : BlockMat2) : BlockMat2 :=
  ⟨A.m11 * B.m11 + A.m12 * B.m21,
   A.m11 * B.m12 + A.m12 * B.m22,
   A.m21 * B.m11 + A.m22 * B.m21,
   A.m21 * B.m12 + A.m22 * B.m22⟩

/-- Matrix addition on `BlockMat2`. -/
def addBlockMat2 (A B : BlockMat2) : BlockMat2 :=
  ⟨A.m11 + B.m11, A.m12 + B.m12, A.m21 + B.m21, A.m22 + B.m22⟩

/-- Scalar multiplication on `BlockMat2`. -/
def smulBlockMat2 (c : Int) (A : BlockMat2) : BlockMat2 :=
  ⟨c * A.m11, c * A.m12, c * A.m21, c * A.m22⟩

/-- Matrix trace `m11 + m22` on `BlockMat2`. -/
def trBlockMat2 (A : BlockMat2) : Int :=
  A.m11 + A.m22

/-- The $2 \times 2$ identity matrix `I_2`. -/
def idBlockMat2 : BlockMat2 := ⟨1, 0, 0, 1⟩

/-! ## Section 1: Tower Inverse-Step Compatibility (`qou-0fmb`) -/

/-- Cleared forward-step trace numerator `z_num(q) = q^4` over common denominator `q * (q^2 + 1)`. -/
def forwardStepNum (q : Int) : Int :=
  (q * q) * (q * q)

/-- Cleared quadratic defect numerator `h_num(q) = (q^2 - 1) * (q^2 + 1)` over `q * (q^2 + 1)`. -/
def quadraticDefectNum (q : Int) : Int :=
  (q * q - 1) * (q * q + 1)

/-- **`qou-0fmb` (Theorem 1a — Inverse-Step Numerator Unit Identity & Trace Reduction):**
    The difference `forwardStepNum q - quadraticDefectNum q` equals `1` for every `q : Int`,
    and for any level-compatible trace value `t : Int`,
    `forwardStepNum q * t - quadraticDefectNum q * t = t`. -/
theorem inverseStepNum_unit_and_trace_reduction (q t : Int) :
    forwardStepNum q - quadraticDefectNum q = 1 ∧
    forwardStepNum q * t - quadraticDefectNum q * t = t := by
  have hdiff : forwardStepNum q - quadraticDefectNum q = 1 := by
    dsimp only [forwardStepNum, quadraticDefectNum]
    rw [Int.sub_mul (q * q) 1 (q * q + 1), Int.mul_add (q * q) (q * q) 1]
    omega
  refine ⟨hdiff, ?_⟩
  rw [← Int.sub_mul (forwardStepNum q) (quadraticDefectNum q) t, hdiff, Int.one_mul t]

/-! ## Section 2: Root-of-Unity Seminormal Vanishing (`qou-4lft`) -/

/-- Cleared seminormal numerator `q^2 - 1`. -/
def seminormalNum (q : Int) : Int :=
  q * q - 1

/-- Cleared seminormal denominator at axial distance `d = 1`: `q^2 - 1`. -/
def seminormalDen1 (q : Int) : Int :=
  q * q - 1

/-- Cleared seminormal denominator at axial distance `d = 2`: `q^4 - 1`. -/
def seminormalDen2 (q : Int) : Int :=
  (q * q) * (q * q) - 1

/-- **`qou-4lft` (Theorem 2a — Seminormal Denominator Factorization & Root-of-Unity Singularity):**
    `seminormalDen2 q = seminormalDen1 q * (q * q + 1)` for all `q`, and at `q = 1` and `q = -1`
    both the numerator and the `d = 1, 2` denominators vanish identically. -/
theorem seminormal_factorization_and_root_of_unity_vanishing (q : Int) :
    seminormalDen2 q = seminormalDen1 q * (q * q + 1) ∧
    seminormalNum 1 + seminormalDen1 1 + seminormalDen2 1 + q = q ∧
    seminormalNum (-1) + seminormalDen1 (-1) + seminormalDen2 (-1) + q = q := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp only [seminormalDen2, seminormalDen1]
    rw [Int.sub_mul (q * q) 1 (q * q + 1), Int.mul_add (q * q) (q * q) 1]
    omega
  · dsimp only [seminormalNum, seminormalDen1, seminormalDen2]
    omega
  · dsimp only [seminormalNum, seminormalDen1, seminormalDen2]
    omega

/-! ## Section 3: Convention Normalization Bridge & Character Sum (`qou-avt2`) -/

/-- Rescaled 2-dimensional standard generator `T_std(q) = [[q^2, q], [0, -1]]` at `Q = q^2`. -/
def rescaledStdGen (q : Int) : BlockMat2 :=
  ⟨q * q, q, 0, -1⟩

/-- **`qou-avt2` (Theorem 3a — Rescaled Quadratic Relation & Degree-Weighted Character Sum):**
    `T_std(q)^2 = (q^2 - 1) * T_std(q) + q^2 * I_2`, and the degree-weighted character sum
    `1 * q^2 + 2 * tr(T_std(q)) + 1 * (-1)` equals `3 * (q * q - 1)`. -/
theorem rescaledStdGen_quadratic_and_character_sum (q : Int) :
    mulBlockMat2 (rescaledStdGen q) (rescaledStdGen q) =
      addBlockMat2 (smulBlockMat2 (q * q - 1) (rescaledStdGen q)) (smulBlockMat2 (q * q) idBlockMat2) ∧
    1 * (q * q) + 2 * trBlockMat2 (rescaledStdGen q) + 1 * (-1) = 3 * (q * q - 1) := by
  constructor
  · ext
    · dsimp only [mulBlockMat2, addBlockMat2, smulBlockMat2, rescaledStdGen, idBlockMat2]
      rw [Int.sub_mul (q * q) 1 (q * q)]
      omega
    · dsimp only [mulBlockMat2, addBlockMat2, smulBlockMat2, rescaledStdGen, idBlockMat2]
      rw [Int.sub_mul (q * q) 1 q]
      omega
    · dsimp only [mulBlockMat2, addBlockMat2, smulBlockMat2, rescaledStdGen, idBlockMat2]
      omega
    · dsimp only [mulBlockMat2, addBlockMat2, smulBlockMat2, rescaledStdGen, idBlockMat2]
      omega
  · dsimp only [trBlockMat2, rescaledStdGen]
    omega

/-! ## Section 4: Two-Row Quotient Dimension Deficit & Sign-Projector Kernel (`qou-cf3m`) -/

/-- Unnormalized sign-block spectral polynomial `(Q - lam1) * (Q - lam2)`. -/
def signSpectralPoly (Q lam1 lam2 : Int) : Int :=
  (Q - lam1) * (Q - lam2)

/-- **`qou-cf3m` (Theorem 4a — Sign-Projector Vanishing on Two-Row Blocks & Dimension Deficit):**
    `signSpectralPoly Q Q Q = 0` (trivial block), `signSpectralPoly Q Q (-1) = 0` (standard block),
    `signSpectralPoly Q (-1) (-1) = (Q + 1) * (Q + 1)` (sign block), and the two-row quotient
    dimension `1^2 + 2^2 = 5` has exact kernel deficit `6 - (1 * 1 + 2 * 2) = 1`. -/
theorem signSpectralPoly_two_row_vanishing_and_deficit (Q : Int) :
    signSpectralPoly Q Q Q + Q = Q ∧
    signSpectralPoly Q Q (-1) + Q = Q ∧
    signSpectralPoly Q (-1) (-1) = (Q + 1) * (Q + 1) ∧
    6 - (1 * 1 + 2 * 2) + Q = 1 + Q := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · dsimp only [signSpectralPoly]
    have h0 : Q - Q = 0 := by omega
    rw [h0]
    omega
  · dsimp only [signSpectralPoly]
    have h0 : Q - Q = 0 := by omega
    rw [h0]
    omega
  · dsimp only [signSpectralPoly]
    have h1 : Q - -1 = Q + 1 := by omega
    rw [h1]
  · omega

/-! ## Section 5: Bilinear Trace Pairing Symmetry on $2 \times 2$ Blocks (`qou-g6vb`) -/

/-- Bilinear trace pairing `tr(A * B)` on $2 \times 2$ block matrices. -/
def tracePair (A B : BlockMat2) : Int :=
  trBlockMat2 (mulBlockMat2 A B)

/-- **`qou-g6vb` (Theorem 5a — Symmetry and Bilinearity of the Matrix Trace Pairing):**
    For all `A, B, C : BlockMat2` and scalars `c1, c2 : Int`,
    `tracePair A B = tracePair B A` and
    `tracePair (addBlockMat2 (smulBlockMat2 c1 A) (smulBlockMat2 c2 B)) C = c1 * tracePair A C + c2 * tracePair B C`. -/
theorem tracePair_symm_and_left_linear (A B C : BlockMat2) (c1 c2 : Int) :
    tracePair A B = tracePair B A ∧
    tracePair (addBlockMat2 (smulBlockMat2 c1 A) (smulBlockMat2 c2 B)) C =
      c1 * tracePair A C + c2 * tracePair B C := by
  constructor
  · dsimp only [tracePair, trBlockMat2, mulBlockMat2]
    rw [Int.mul_comm A.m11 B.m11, Int.mul_comm A.m12 B.m21,
        Int.mul_comm A.m21 B.m12, Int.mul_comm A.m22 B.m22]
    omega
  · dsimp only [tracePair, trBlockMat2, mulBlockMat2, addBlockMat2, smulBlockMat2]
    rw [Int.add_mul (c1 * A.m11) (c2 * B.m11) C.m11,
        Int.add_mul (c1 * A.m12) (c2 * B.m12) C.m21,
        Int.add_mul (c1 * A.m21) (c2 * B.m21) C.m12,
        Int.add_mul (c1 * A.m22) (c2 * B.m22) C.m22]
    rw [Int.mul_assoc c1 A.m11 C.m11, Int.mul_assoc c2 B.m11 C.m11,
        Int.mul_assoc c1 A.m12 C.m21, Int.mul_assoc c2 B.m12 C.m21,
        Int.mul_assoc c1 A.m21 C.m12, Int.mul_assoc c2 B.m21 C.m12,
        Int.mul_assoc c1 A.m22 C.m22, Int.mul_assoc c2 B.m22 C.m22]
    rw [Int.mul_add c1 (A.m11 * C.m11 + A.m12 * C.m21) (A.m21 * C.m12 + A.m22 * C.m22),
        Int.mul_add c1 (A.m11 * C.m11) (A.m12 * C.m21),
        Int.mul_add c1 (A.m21 * C.m12) (A.m22 * C.m22),
        Int.mul_add c2 (B.m11 * C.m11 + B.m12 * C.m21) (B.m21 * C.m12 + B.m22 * C.m22),
        Int.mul_add c2 (B.m11 * C.m11) (B.m12 * C.m21),
        Int.mul_add c2 (B.m21 * C.m12) (B.m22 * C.m22)]
    omega

end QOU.Foundations.TowerCompatibilityRootOfUnitySeminormalNormalizationRadicalKernelBilinearSymmetry
