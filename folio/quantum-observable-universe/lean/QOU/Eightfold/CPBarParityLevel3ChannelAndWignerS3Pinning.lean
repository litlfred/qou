/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# CP Bar-Parity Asymmetry, Level-3 Quotient Channel, Coulomb Shape Hierarchy, Partition (2,2) Weight Ratio, and S3 Character Pinning

This module formalizes five structural results under `qou-8lxd`:

1. **`qou-hjs8` (Mirror Bar-Parity Mass Asymmetry and Crossing Phase Interference):**
   Proves the exact cross-multiplied factorization of the mirror mass asymmetry
   `(m_+ - m_-) * (rho_+ + rho_-) = (rho_+ - rho_-) * (m_+ + m_-)` for `m_± = m_0 * rho_±`,
   showing `m_+ - m_- = 0 ↔ rho_+ = rho_-` whenever `m_0 > 0`. For a mixed-sign crossing
   amplitude `n_+ q - n_- q⁻¹` with squared modulus proportional to
   `n_+² r² + n_-² r⁻² - 2 n_+ n_- cos(2θ)`, proves that pure-sign braids (`n_- = 0`) are
   independent of `cos(2θ)`, whereas mixed-sign braids (`n_+ n_- > 0`) depend strictly
   monotonically on `cos(2θ)`.

2. **`qou-lxh5` (Level-3 SU(3) vs Level-2 SU(2) Row-Cap Quotient Dimensions and Trace Shift):**
   Formalizes the exact dimensions of the 2-row quotient `H_n / ⟨e^(3)⟩`
   (`1, 2, 5, 14, 42, 132` for `n = 1..6`) versus the 3-row quotient `H_n / ⟨e^(4)⟩`
   (`1, 2, 6, 23, 103, 513` for `n = 1..6`), showing that the 3-row radical first opens at
   `n = 4` (`rowCapCorank3 3 = 0`, `rowCapCorank3 4 = 1` from `(1^4)`), and proves the
   numerator identity for the trace parameter shift `z_2 - z_3 > 0`.

3. **`qou-usft` (Light-Nucleus Coulomb Shape-Factor Hierarchy and Binding-Length Sensitivity):**
   Formalizes the rational hierarchy of squared Coulomb shape factors
   `f_exp² = 75/256 < f_unif² = 3/5 < f_req² = (10913/10000)²`, and proves that under the
   inverse-square binding-length relation `R_qou² * S_qou = R_ame² * S_ame`, a smaller predicted
   separation energy `0 < S_qou < S_ame` forces a strictly larger squared radius
   `R_ame² < R_qou²`.

4. **`qou-wg3c` (Partition λ = (2,2) Hook Product vs Shadow-Price Weight and k = 5 Cap):**
   Formalizes the polynomial relationship between the quantum hook product
   `H_q(2,2) = [3]_q [2]_q²` and the shadow-price weight `w_{(2,2)} = dim_q(2,2)² / [4]_q!`,
   including their classical `72 : 1` divergence at `q = 1`, and proves over the 7 partitions
   of `k = 5` that no partition of `5` is simultaneously two-row (`numRows ≤ 2`) and
   self-conjugate.

5. **`qou-x0th` (S3 Branching Dimension Under-Determination vs Unique Character Pinning):**
   Proves that the `S_3` dimension conservation equation `a + b + 2 c = 2 ℓ + 1` alone admits
   distinct solutions for distinct `c_1 ≠ c_2`, whereas the full `S_3` character trace system
   `(χ(e), χ((12)), χ((123))) = (a + b + 2c, a - b, a + b - c)` satisfies integer
   inversion identities (`6a`, `6b`, `3c`) that uniquely pin `(a, b, c)`.
-/

namespace QOU.Eightfold.CPBarParityLevel3ChannelAndWignerS3Pinning

/-! ## 1. Mirror Bar-Parity Mass Asymmetry & Mixed-Sign Crossing Phase (`qou-hjs8`) -/

/-- Mirror mass difference `m_+ - m_- = m_0 * rho_+ - m_0 * rho_-`. -/
def mirrorMassDiff (m0 rho_plus rho_minus : Int) : Int :=
  m0 * rho_plus - m0 * rho_minus

/-- Mirror mass sum `m_+ + m_- = m_0 * rho_+ + m_0 * rho_-`. -/
def mirrorMassSum (m0 rho_plus rho_minus : Int) : Int :=
  m0 * rho_plus + m0 * rho_minus

/-- Bar-conjugation spectral difference `rho(q) - rho(q⁻¹)`. -/
def rhoDiff (rho_plus rho_minus : Int) : Int :=
  rho_plus - rho_minus

/-- Bar-conjugation spectral sum `rho(q) + rho(q⁻¹)`. -/
def rhoSum (rho_plus rho_minus : Int) : Int :=
  rho_plus + rho_minus

/-- Factorized form of the mirror mass difference `m_+ - m_- = m_0 * (rho_+ - rho_-)`. -/
theorem mirror_mass_diff_factorization (m0 rho_plus rho_minus : Int) :
    mirrorMassDiff m0 rho_plus rho_minus = m0 * rhoDiff rho_plus rho_minus := by
  dsimp [mirrorMassDiff, rhoDiff]
  rw [Int.mul_sub]

/-- Factorized form of the mirror mass sum `m_+ + m_- = m_0 * (rho_+ + rho_-)`. -/
theorem mirror_mass_sum_factorization (m0 rho_plus rho_minus : Int) :
    mirrorMassSum m0 rho_plus rho_minus = m0 * rhoSum rho_plus rho_minus := by
  dsimp [mirrorMassSum, rhoSum]
  rw [Int.mul_add]

/-- Cross-multiplied scale-invariance identity:
    `(m_+ - m_-) * (rho_+ + rho_-) = (rho_+ - rho_-) * (m_+ + m_-)`,
    showing that the common scale `m_0` cancels identically from the fractional mass asymmetry. -/
theorem mirror_mass_asymmetry_scale_invariance (m0 rho_plus rho_minus : Int) :
    mirrorMassDiff m0 rho_plus rho_minus * rhoSum rho_plus rho_minus =
      rhoDiff rho_plus rho_minus * mirrorMassSum m0 rho_plus rho_minus := by
  rw [mirror_mass_diff_factorization, mirror_mass_sum_factorization]
  rw [Int.mul_comm m0 (rhoDiff rho_plus rho_minus), Int.mul_assoc]

/-- For any positive overall mass scale `m0 > 0`, the mirror mass split vanishes if and only if
    the observable `rho` is bar-even (`rho_plus = rho_minus`). -/
theorem mirror_mass_diff_zero_iff_bar_even (m0 rho_plus rho_minus : Int) (hm0 : 0 < m0) :
    mirrorMassDiff m0 rho_plus rho_minus = 0 ↔ rho_plus = rho_minus := by
  rw [mirror_mass_diff_factorization]
  dsimp [rhoDiff]
  constructor
  · intro h
    cases Int.mul_eq_zero.mp h with
    | inl hm => omega
    | inr hr => omega
  · intro h
    have hsub : rho_plus - rho_minus = 0 := by omega
    rw [hsub, Int.mul_zero]

/-- Scaled squared modulus of a mixed-sign crossing amplitude `n_+ q - n_- q⁻¹`:
    `n_+² r² + n_-² r⁻² - 2 n_+ n_- cos(2θ)`. -/
def mixedCrossingNormSqScaled (n_plus n_minus r_sq r_inv_sq cos2theta : Int) : Int :=
  n_plus * n_plus * r_sq + n_minus * n_minus * r_inv_sq - 2 * ((n_plus * n_minus) * cos2theta)

/-- A pure-sign braid (`n_minus = 0`) has squared modulus strictly independent of the phase
    parameter `cos2theta`. -/
theorem pure_sign_crossing_phase_independent (n_plus r_sq r_inv_sq c1 c2 : Int) :
    mixedCrossingNormSqScaled n_plus 0 r_sq r_inv_sq c1 =
      mixedCrossingNormSqScaled n_plus 0 r_sq r_inv_sq c2 := by
  dsimp [mixedCrossingNormSqScaled]
  omega

/-- A mixed-sign braid (`n_plus * n_minus > 0`) has strictly different squared modulus at
    distinct phase parameters `c1 < c2`, showing that bar-odd phase sensitivity arises when
    both positive and negative crossings are present (`n_+ n_- ≠ 0`). -/
theorem mixed_sign_crossing_phase_strictly_dependent
    (n_plus n_minus r_sq r_inv_sq c1 c2 : Int)
    (hprod : 0 < n_plus * n_minus) (hc : c1 < c2) :
    mixedCrossingNormSqScaled n_plus n_minus r_sq r_inv_sq c2 <
      mixedCrossingNormSqScaled n_plus n_minus r_sq r_inv_sq c1 := by
  dsimp [mixedCrossingNormSqScaled]
  have hdiff : 0 < (n_plus * n_minus) * (c2 - c1) :=
    Int.mul_pos hprod (by omega)
  have hsub :
      (n_plus * n_minus) * c2 - (n_plus * n_minus) * c1 =
        (n_plus * n_minus) * (c2 - c1) := by
    rw [Int.mul_sub]
  omega

/-! ## 2. Level-3 (SU(3)) vs Level-2 (SU(2)) Row-Cap Quotients & Trace Shift (`qou-lxh5`) -/

/-- Full symmetric/braid quotient algebra dimension `n!` for `n = 0..6`. -/
def fullBraidAlgebraDim : Nat → Nat
  | 0 => 1
  | 1 => 1
  | 2 => 2
  | 3 => 6
  | 4 => 24
  | 5 => 120
  | 6 => 720
  | n + 7 => n + 7

/-- Level-2 two-row quotient dimension `C_n` for `n = 0..6`. -/
def rowCapLevel2Dim : Nat → Nat
  | 0 => 1
  | 1 => 1
  | 2 => 2
  | 3 => 5
  | 4 => 14
  | 5 => 42
  | 6 => 132
  | _ => 0

/-- Level-3 three-row quotient dimension `∑_{ℓ(λ) ≤ 3} d_λ²` for `n = 0..6`. -/
def rowCapLevel3Dim : Nat → Nat
  | 0 => 1
  | 1 => 1
  | 2 => 2
  | 3 => 6
  | 4 => 23
  | 5 => 103
  | 6 => 513
  | _ => 0

/-- Radical corank at level 2 (`n! - rowCapLevel2Dim n`). -/
def rowCapCorank2 (n : Nat) : Nat :=
  fullBraidAlgebraDim n - rowCapLevel2Dim n

/-- Radical corank at level 3 (`n! - rowCapLevel3Dim n`). -/
def rowCapCorank3 (n : Nat) : Nat :=
  fullBraidAlgebraDim n - rowCapLevel3Dim n

/-- Comparison of the level-2 and level-3 quotient dimensions and radical coranks for `n = 1..6`:
    - At `n = 3`, level 2 kills `(1,1,1)` (`rowCapCorank2 3 = 1`), while level 3 is
      faithful (`rowCapCorank3 3 = 0`).
    - At `n = 4`, the level-3 radical first opens with dimension `rowCapCorank3 4 = 1`
      (killing only the 4-row antisymmetric diagram `(1,1,1,1)`).
    - At `n = 5, 6`, the level-3 quotient retains `103` and `513` dimensions (`corank 17` and `207`)
      compared to `42` and `132` at level 2 (`corank 78` and `588`). -/
theorem level2_vs_level3_row_cap_corank_hierarchy :
    (rowCapLevel3Dim 1 = 1 ∧ rowCapLevel3Dim 2 = 2 ∧ rowCapLevel3Dim 3 = 6 ∧
     rowCapLevel3Dim 4 = 23 ∧ rowCapLevel3Dim 5 = 103 ∧ rowCapLevel3Dim 6 = 513) ∧
    (rowCapCorank3 1 = 0 ∧ rowCapCorank3 2 = 0 ∧ rowCapCorank3 3 = 0 ∧
     rowCapCorank3 4 = 1 ∧ rowCapCorank3 5 = 17 ∧ rowCapCorank3 6 = 207) ∧
    (rowCapCorank2 3 = 1 ∧ rowCapCorank2 4 = 10 ∧ rowCapCorank2 5 = 78 ∧ rowCapCorank2 6 = 588) ∧
    (rowCapLevel2Dim 4 < rowCapLevel3Dim 4 ∧ rowCapLevel2Dim 6 < rowCapLevel3Dim 6) := by
  decide

/-- Cross-multiplied numerator of the trace parameter shift `z_2 - z_3`:
    Since `z_2 = q³ / (q² + 1)` and `z_3 = q⁵ / (q⁴ + q² + 1)`, factoring out `q` and letting
    `x = q²` gives `x * (x * x + x + 1) - x * (x * (x + 1))`. -/
def traceShiftNumerator (x : Int) : Int :=
  x * (x * x + x + 1) - x * (x * (x + 1))

/-- The trace parameter difference `z_2 - z_3` has cross-multiplied numerator identically equal
    to `x = q²`, which is strictly positive for all `x > 0`. -/
theorem trace_shift_level2_minus_level3_positive (x : Int) (hx : 0 < x) :
    traceShiftNumerator x = x ∧ 0 < traceShiftNumerator x := by
  dsimp [traceShiftNumerator]
  have hid : x * (x * x + x + 1) - x * (x * (x + 1)) = x := by
    rw [Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_one]
    omega
  exact ⟨hid, by omega⟩

/-! ## 3. Light-Nucleus Coulomb Shape Hierarchy & Binding-Length Sensitivity (`qou-usft`) -/

/-- Exact rational comparison of the squared Coulomb shape factors:
    - Exponential density: `f_exp = 5√3 / 16 ⟹ f_exp² = 75 / 256`
    - Uniform sphere: `f_unif = (3/5)√(5/3) ⟹ f_unif² = 3 / 5`
    - Required He-3/H-3 factor: `f_req ≈ 1.0913 ⟹ f_req² = (10913 / 10000)²`
    Cross-multiplication confirms `f_exp² < f_unif² < f_req²`. -/
theorem coulomb_shape_factor_squared_hierarchy :
    75 * 5 < 3 * 256 ∧ 3 * (10000 * 10000) < 5 * (10913 * 10913) := by
  decide

/-- Under the inverse-square binding-length scaling `R_qou² * S_qou = R_ame² * S_ame`,
    if the predicted separation energy is smaller than the experimental value (`0 < S_qou < S_ame`)
    and `0 < R_ame²`, then the resulting squared Coulomb radius satisfies `R_ame² < R_qou²`
    (forcing a larger radius and thus a smaller Coulomb energy `E_C ∝ 1/R`). -/
theorem binding_length_radius_sq_strictly_larger
    (R_qou_sq R_ame_sq S_qou S_ame : Int)
    (hS_pos : 0 < S_qou)
    (hS_lt : S_qou < S_ame)
    (hR_pos : 0 < R_ame_sq)
    (hrel : R_qou_sq * S_qou = R_ame_sq * S_ame) :
    R_ame_sq < R_qou_sq := by
  have hdiff_pos : 0 < R_ame_sq * (S_ame - S_qou) :=
    Int.mul_pos hR_pos (by omega)
  have h1 : R_ame_sq * (S_ame - S_qou) = (R_qou_sq - R_ame_sq) * S_qou := by
    rw [Int.mul_sub, Int.sub_mul, hrel]
  have hprod_pos : 0 < (R_qou_sq - R_ame_sq) * S_qou := by omega
  cases Int.lt_trichotomy R_ame_sq R_qou_sq with
  | inl hlt => exact hlt
  | inr hrest =>
    cases hrest with
    | inl heq =>
      have hzero : R_qou_sq - R_ame_sq = 0 := by omega
      rw [hzero, Int.zero_mul] at hprod_pos
      omega
    | inr hgt =>
      have hnonpos : (R_qou_sq - R_ame_sq) * S_qou ≤ 0 :=
        Int.mul_nonpos_of_nonpos_of_nonneg (by omega) (by omega)
      omega

/-! ## 4. Partition λ = (2,2) Hook vs Shadow Weight & k = 5 Cap (`qou-wg3c`) -/

/-- Quantum hook product at `λ = (2,2)`: `H_q(2,2) = [3]_q [2]_q²`. -/
def hookProduct22 (q2 q3 : Int) : Int :=
  q3 * (q2 * q2)

/-- Quantum factorial `[4]_q! = [4]_q [3]_q [2]_q`. -/
def qFactorial4 (q2 q3 q4 : Int) : Int :=
  q4 * (q3 * q2)

/-- Cross-multiplied identity verifying `dim_q(2,2) = [4]_q! / H_q(2,2) = [4]_q / [2]_q`:
    `[4]_q! * [2]_q = H_q(2,2) * [4]_q`. -/
theorem dimq22_hook_quotient_identity (q2 q3 q4 : Int) :
    qFactorial4 q2 q3 q4 * q2 = hookProduct22 q2 q3 * q4 := by
  dsimp [qFactorial4, hookProduct22]
  rw [Int.mul_assoc q4 (q3 * q2) q2, Int.mul_assoc q3 q2 q2, Int.mul_comm q4 (q3 * (q2 * q2))]

/-- Classical `q → 1` specialization (`[2]_1 = 2, [3]_1 = 3, [4]_1 = 4`):
    - Hook product: `H_1(2,2) = 3 * 2² = 12`
    - Quantum dimension: `dim_1(2,2) = 4 / 2 = 2`
    - Shadow-price weight: `w_{(2,2)}(1) = dim_1(2,2)² / 4! = 4 / 24 = 1 / 6`
    - Ratio `H_1(2,2) / w_{(2,2)}(1) = 12 * 6 = 72 ≠ 1`. -/
theorem classical_partition22_hook_vs_shadow_weight_divergence :
    hookProduct22 2 3 = 12 ∧ qFactorial4 2 3 4 = 24 ∧ 12 * 24 = 72 * (2 * 2) := by
  decide

/-- Enumeration of all 7 integer partitions of `k = 5`. -/
inductive PartitionOf5 where
  | p5       -- (5)
  | p41      -- (4,1)
  | p32      -- (3,2)
  | p311     -- (3,1,1)
  | p221     -- (2,2,1)
  | p2111    -- (2,1,1,1)
  | p11111   -- (1,1,1,1,1)
  deriving DecidableEq

/-- Number of parts (rows `ℓ(λ)`) of each partition of `5`. -/
def PartitionOf5.numRows : PartitionOf5 → Nat
  | .p5     => 1
  | .p41    => 2
  | .p32    => 2
  | .p311   => 3
  | .p221   => 3
  | .p2111  => 4
  | .p11111 => 5

/-- Transpose (conjugate partition `λ'`) on the 7 partitions of `5`. -/
def PartitionOf5.conjugate : PartitionOf5 → PartitionOf5
  | .p5     => .p11111
  | .p41    => .p2111
  | .p32    => .p221
  | .p311   => .p311
  | .p221   => .p32
  | .p2111  => .p41
  | .p11111 => .p5

/-- Conjugation on partitions of `5` is an involution (`(λ')' = λ`). -/
theorem partitionOf5_conjugate_involution (p : PartitionOf5) :
    p.conjugate.conjugate = p := by
  cases p <;> rfl

/-- No partition of `k = 5` is simultaneously within the two-row cap (`numRows ≤ 2`)
    and self-conjugate (`p.conjugate = p`): the unique self-conjugate partition of `5` is
    `(3,1,1)` which has `3` rows. -/
theorem no_two_row_self_conjugate_partition_of_5 (p : PartitionOf5) :
    ¬ (p.numRows ≤ 2 ∧ p.conjugate = p) := by
  cases p <;> decide

/-! ## 5. S3 Branching Dimension Under-Determination vs Character Pinning (`qou-x0th`) -/

/-- Dimension conservation for `S_3` branching `V_ℓ → a · 1 ⊕ b · 1_sign ⊕ c · 2_std`. -/
def s3DimConservation (a b c ell : Int) : Prop :=
  a + b + 2 * c = 2 * ell + 1

/-- Dimension conservation alone cannot uniquely pin the 2D multiplicity `c`:
    for any `ℓ` and any two distinct multiplicities `c1 ≠ c2`, choosing `a_i = 2ℓ + 1 - 2c_i`
    and `b_i = 0` gives two distinct solutions satisfying `s3DimConservation`. -/
theorem s3_dim_conservation_underdetermines_c (ell c1 c2 : Int) (hne : c1 ≠ c2) :
    s3DimConservation (2 * ell + 1 - 2 * c1) 0 c1 ell ∧
    s3DimConservation (2 * ell + 1 - 2 * c2) 0 c2 ell ∧
    (2 * ell + 1 - 2 * c1) ≠ (2 * ell + 1 - 2 * c2) := by
  dsimp [s3DimConservation]
  refine ⟨by omega, by omega, by omega⟩

/-- Character trace on the identity class `e ∈ S_3`: `χ(e) = a + b + 2c`. -/
def s3CharE (a b c : Int) : Int := a + b + 2 * c

/-- Character trace on the transposition class `(12) ∈ S_3`: `χ((12)) = a - b`. -/
def s3CharTrans (a b : Int) : Int := a - b

/-- Character trace on the 3-cycle class `(123) ∈ S_3`: `χ((123)) = a + b - c`. -/
def s3Char3Cycle (a b c : Int) : Int := a + b - c

/-- Exact orthogonality inversion identities recovering `(6a, 6b, 3c)` from the three
    conjugacy class traces `(χ(e), χ((12)), χ((123)))` of `S_3`. -/
theorem s3_character_orthogonality_inversion (a b c : Int) :
    6 * a = s3CharE a b c + 3 * s3CharTrans a b + 2 * s3Char3Cycle a b c ∧
    6 * b = s3CharE a b c - 3 * s3CharTrans a b + 2 * s3Char3Cycle a b c ∧
    3 * c = s3CharE a b c - s3Char3Cycle a b c := by
  dsimp [s3CharE, s3CharTrans, s3Char3Cycle]
  refine ⟨by omega, by omega, by omega⟩

/-- In contrast to dimension conservation alone, matching the three `S_3` conjugacy class traces
    uniquely pins all three multiplicities `(a, b, c)`. -/
theorem s3_character_traces_uniquely_pin_multiplicities
    (a1 b1 c1 a2 b2 c2 : Int)
    (hE : s3CharE a1 b1 c1 = s3CharE a2 b2 c2)
    (hT : s3CharTrans a1 b1 = s3CharTrans a2 b2)
    (hC : s3Char3Cycle a1 b1 c1 = s3Char3Cycle a2 b2 c2) :
    a1 = a2 ∧ b1 = b2 ∧ c1 = c2 := by
  dsimp [s3CharE, s3CharTrans, s3Char3Cycle] at hE hT hC
  refine ⟨by omega, by omega, by omega⟩

end QOU.Eightfold.CPBarParityLevel3ChannelAndWignerS3Pinning
