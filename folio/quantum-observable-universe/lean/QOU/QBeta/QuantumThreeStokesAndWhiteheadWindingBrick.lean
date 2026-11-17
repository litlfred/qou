/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  * qou-hmr9: Icosahedral 1/sqrt(5) per-partition quadratic slack identity (s^2 - 5*m^2).
  * qou-nkm1: Quantum-dimension [3]_q numerator q^2 + q + 1 classical evaluation = 3 and cyclotomic product.
  * qou-r75d: Whitehead link (5^2_1) four-Catalan volume decomposition and symmetric saddle sum.
  * qou-smyz: Wedderburn multiplicity obstruction excess gap (mSrc > mTgt -> mSrc - mTgt >= 1).
  * qou-thj7: Murakami deformed meridian winding threshold (u^2 - w0^2) parity and factorization.
-/

namespace QOU.QBeta.QuantumThreeStokesAndWhiteheadWindingBrick

/-! ### 1. Icosahedral `1/sqrt(5)` per-partition quadratic slack (`qou-hmr9`) -/

/-- Scaled icosahedral quadratic slack `s^2 - 5 * m^2` comparing a partition magnitude `m`
    against the `s / sqrt(5)` icosahedral envelope. -/
def icosahedralFifthQuadraticSlack (s m : Int) : Int :=
  s * s - 5 * (m * m)

/-- `icosahedralFifthQuadraticSlack` is even in both `s` and `m` (`m |-> -m`) and satisfies
    the complementary partition sum `icosahedralFifthQuadraticSlack s m + 5 * m^2 = s^2`. -/
theorem icosahedralFifthQuadraticSlack_parity_and_complement (s m : Int) :
    icosahedralFifthQuadraticSlack s (-m) = icosahedralFifthQuadraticSlack s m ∧
    icosahedralFifthQuadraticSlack s m + 5 * (m * m) = s * s := by
  unfold icosahedralFifthQuadraticSlack
  have hneg : (-m) * (-m) = m * m := by
    rw [Int.neg_mul_neg]
  exact ⟨by omega, by omega⟩

/-! ### 2. Quantum-dimension `[3]_q` numerator and Stokes constant `3` (`qou-nkm1`) -/

/-- Numerator `q^2 + q + 1` of the symmetric quantum dimension `[3]_q = (q^2 + q + 1) / q`. -/
def qDimThreeNumerator (q : Int) : Int :=
  q * q + q + 1

/-- At the classical limit `q = 1`, `qDimThreeNumerator 1 = 3` (the GGM Stokes constant for `4_1`),
    and for any `q`, `(q - 1) * qDimThreeNumerator q = q^3 - 1`. -/
theorem qDimThreeNumerator_classical_three_and_cyclotomic (q : Int) :
    qDimThreeNumerator 1 = 3 ∧
    (q - 1) * qDimThreeNumerator q = q * q * q - 1 := by
  unfold qDimThreeNumerator
  have hcyc : (q - 1) * (q * q + q + 1) = q * q * q - 1 := by
    rw [Int.sub_mul, Int.one_mul, Int.mul_add, Int.mul_add, Int.mul_one]
    have hq2 : q * (q * q) = q * q * q := by
      rw [← Int.mul_assoc]
    omega
  exact ⟨by omega, hcyc⟩

/-! ### 3. Whitehead link four-Catalan volume and saddle index balance (`qou-r75d`) -/

/-- Four-Catalan octahedral volume sum `4 * g` for the Whitehead link `5^2_1` (`Vol(5^2_1) = 4*G`). -/
def whiteheadFourCatalanSum (g : Int) : Int :=
  4 * g

/-- Two-variable Kashaev saddle index pair `(n - k, n + k)` around the central index `n`. -/
def whiteheadSaddlePairSum (n k : Int) : Int :=
  (n - k) + (n + k)

/-- The Whitehead four-Catalan sum decomposes into four equal Catalan Lobachevsky quarters `g`,
    and the shifted saddle indices `(n - k)` and `(n + k)` sum to `2 * n` with difference `2 * k`. -/
theorem whiteheadFourCatalan_and_saddle_balance (g n k : Int) :
    whiteheadFourCatalanSum g = g + g + g + g ∧
    whiteheadSaddlePairSum n k = 2 * n ∧
    (n + k) - (n - k) = 2 * k := by
  dsimp only [whiteheadFourCatalanSum, whiteheadSaddlePairSum]
  have h1 : 4 * g = g + g + g + g := by omega
  have h2 : (n - k) + (n + k) = 2 * n := by omega
  have h3 : (n + k) - (n - k) = 2 * k := by omega
  exact ⟨h1, h2, h3⟩

/-! ### 4. Semisimple block multiplicity obstruction excess (`qou-smyz`) -/

/-- Multiplicity excess `mSrc - mTgt` comparing source and target direct-summand block multiplicities. -/
def blockMultiplicityExcess (mSrc mTgt : Int) : Int :=
  mSrc - mTgt

/-- Whenever the source multiplicity strictly exceeds the target multiplicity (`mTgt < mSrc`),
    the block multiplicity excess is at least `1` (`1 <= blockMultiplicityExcess mSrc mTgt`),
    is antisymmetric under source-target swap, and reconstructs `mSrc`. -/
theorem blockMultiplicityExcess_pos_of_lt (mSrc mTgt : Int) (hLt : mTgt < mSrc) :
    1 ≤ blockMultiplicityExcess mSrc mTgt ∧
    blockMultiplicityExcess mSrc mTgt + mTgt = mSrc ∧
    blockMultiplicityExcess mSrc mTgt = - blockMultiplicityExcess mTgt mSrc := by
  dsimp only [blockMultiplicityExcess]
  have hPos : 1 ≤ mSrc - mTgt := by omega
  have hAdd : (mSrc - mTgt) + mTgt = mSrc := by omega
  have hSkew : mSrc - mTgt = - (mTgt - mSrc) := by omega
  exact ⟨hPos, hAdd, hSkew⟩

/-! ### 5. Murakami deformed meridian winding threshold (`qou-thj7`) -/

/-- Squared meridian winding slack `u^2 - w0^2` above the `2*pi` threshold `w0`. -/
def deformedMeridianWindingSlack (u w0 : Int) : Int :=
  u * u - w0 * w0

/-- The deformed meridian winding slack factors into `(u - w0) * (u + w0)`, is invariant under
    winding sign reversal `u |-> -u` (`| -u | = | u |`), and vanishes at the threshold `u = w0`. -/
theorem deformedMeridianWindingSlack_factorization_and_parity (u w0 : Int) :
    deformedMeridianWindingSlack u w0 = (u - w0) * (u + w0) ∧
    deformedMeridianWindingSlack (-u) w0 = deformedMeridianWindingSlack u w0 ∧
    deformedMeridianWindingSlack w0 w0 = 0 := by
  unfold deformedMeridianWindingSlack
  have hfac : u * u - w0 * w0 = (u - w0) * (u + w0) := by
    rw [Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_comm w0 u]
    omega
  have hneg : (-u) * (-u) = u * u := by
    rw [Int.neg_mul_neg]
  exact ⟨hfac, by omega, by omega⟩

end QOU.QBeta.QuantumThreeStokesAndWhiteheadWindingBrick
