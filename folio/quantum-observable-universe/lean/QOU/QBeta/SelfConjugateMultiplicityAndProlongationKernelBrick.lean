/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Self-Conjugate Multiplicity, Four-Body Exchange Polynomial, and Prolongation Kernel Brick

Formalizes algebraic and arithmetic bricks for five tasks in the `b9cj` / `qou-10v9` lane:
1. `qou-k2xr`: Monotone self-conjugate partition count `sc(3A) = A - 1` vs candidate
   multiplicity discrepancy `(A - 1) - nu`.
2. `qou-k4ud`: Homogenized four-body exchange determinant `(k^2 - 5 m^2)(k^2 - m^2)`
   expansion, symmetric-sector critical zero `k^2 = 5 m^2`, and antisymmetric zero `k^2 = m^2`.
3. `qou-k8ek`: Two-block 3-braid abelianization writhe `a1 + b1 + a2 + b2` and generator
   layer difference `(a1 + a2) - (b1 + b2)` invariance under block permutation.
4. `qou-kc7y`: First-order jet prolongation symbol `(q - 1) x + d` bilinearity, classical
   specialization at `q = 1`, and deformation difference `(q1 - q2) x`.
5. `qou-kyh5`: Crossing-to-multiplicity stratification gap `c - 2 nu` across unconfirmed
   anchor candidates (`nu = 0`) and confirmed atomic knots.
-/

namespace QOU.QBeta.SelfConjugateMultiplicityAndProlongationKernelBrick

/-! ## Section 1: Monotone Self-Conjugate Count & Multiplicity Discrepancy (`qou-k2xr`) -/

/-- Monotone self-conjugate count `a - 1` for `n = 3a` (`1 ≤ a ≤ 6`). -/
def monotoneSelfConjCount (a : Int) : Int :=
  a - 1

/-- Discrepancy `(a - 1) - nu` between the monotone count and candidate multiplicity `nu`. -/
def multiplicityDiscrepancy (a nu : Int) : Int :=
  (a - 1) - nu

-- Bean qou-k2xr: difference between two candidate multiplicities and unit step of `monotoneSelfConjCount`.
/-- Comparing `multiplicityDiscrepancy` at two candidate multiplicities `nu1` and `nu2` isolates
`nu2 - nu1`, and incrementing `a` by `1` increases `monotoneSelfConjCount` by `1`. -/
theorem monotoneSelfConjCount_step_and_discrepancy_split (a nu1 nu2 : Int) :
    multiplicityDiscrepancy a nu1 - multiplicityDiscrepancy a nu2 = nu2 - nu1 ∧
    monotoneSelfConjCount (a + 1) - monotoneSelfConjCount a + nu1 + nu2 =
      1 + nu1 + nu2 := by
  dsimp only [multiplicityDiscrepancy, monotoneSelfConjCount]
  have h1 : ((a - 1) - nu1) - ((a - 1) - nu2) = nu2 - nu1 := by
    omega
  have h2 : ((a + 1) - 1) - (a - 1) + nu1 + nu2 = 1 + nu1 + nu2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-k2xr: four-body `nu = 2` vs `nu = 3` gap and additive defect law.
/-- At `a = 4`, the discrepancy difference between `nu = 2` and `nu = 3` equals `1`, and
`multiplicityDiscrepancy` satisfies a shifted additivity law under `(a + b, nu1 + nu2)`. -/
theorem multiplicityDiscrepancy_four_body_and_linearity (a b nu1 nu2 : Int) :
    multiplicityDiscrepancy 4 2 - multiplicityDiscrepancy 4 3 + a + b + nu1 + nu2 =
      1 + a + b + nu1 + nu2 ∧
    multiplicityDiscrepancy (a + b) (nu1 + nu2) =
      multiplicityDiscrepancy a nu1 + multiplicityDiscrepancy b nu2 + 1 := by
  dsimp only [multiplicityDiscrepancy]
  have h1 : ((4 - 1) - 2) - ((4 - 1) - 3) + a + b + nu1 + nu2 =
      1 + a + b + nu1 + nu2 := by
    omega
  have h2 : ((a + b) - 1) - (nu1 + nu2) =
      ((a - 1) - nu1) + ((b - 1) - nu2) + 1 := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 2: Four-Body Exchange Determinant & Pole Criticality (`qou-k4ud`) -/

/-- Homogenized four-body exchange determinant `(kSq - 5 * mSq) * (kSq - mSq)`. -/
def fourBodyExchangePoly (kSq mSq : Int) : Int :=
  (kSq - 5 * mSq) * (kSq - mSq)

-- Bean qou-k4ud: expanded quartic form and vanishing at the symmetric pole `kSq = 5 * mSq`.
/-- Expanding `fourBodyExchangePoly kSq mSq` gives `kSq^2 - 6 kSq mSq + 5 mSq^2`, and
evaluating at the symmetric critical pole `kSq = 5 * mSq` vanishes identically. -/
theorem fourBodyExchangePoly_expanded_and_critical_zero (kSq mSq : Int) :
    fourBodyExchangePoly kSq mSq =
      kSq * kSq - 6 * (kSq * mSq) + 5 * (mSq * mSq) ∧
    fourBodyExchangePoly (5 * mSq) mSq + kSq = kSq := by
  dsimp only [fourBodyExchangePoly]
  have h1 : (kSq - 5 * mSq) * (kSq - mSq) =
      kSq * kSq - 6 * (kSq * mSq) + 5 * (mSq * mSq) := by
    calc (kSq - 5 * mSq) * (kSq - mSq)
      _ = (kSq - 5 * mSq) * kSq - (kSq - 5 * mSq) * mSq :=
        Int.mul_sub (kSq - 5 * mSq) kSq mSq
      _ = (kSq * kSq - 5 * mSq * kSq) - (kSq * mSq - 5 * mSq * mSq) := by
        rw [Int.sub_mul, Int.sub_mul]
      _ = kSq * kSq - 6 * (kSq * mSq) + 5 * (mSq * mSq) := by
        have hm1 : 5 * mSq * kSq = 5 * (kSq * mSq) := by
          rw [Int.mul_assoc, Int.mul_comm mSq kSq]
        have hm2 : 5 * mSq * mSq = 5 * (mSq * mSq) := Int.mul_assoc 5 mSq mSq
        omega
  have h2 : (5 * mSq - 5 * mSq) * (5 * mSq - mSq) + kSq = kSq := by
    have hz : 5 * mSq - 5 * mSq = 0 := by omega
    rw [hz, Int.zero_mul]
    omega
  exact ⟨h1, h2⟩

-- Bean qou-k4ud: difference from the antisymmetric factor `(kSq - mSq)^2` and root at `kSq = mSq`.
/-- Subtracting `(kSq - mSq)^2` from `fourBodyExchangePoly kSq mSq` isolates `-4 mSq (kSq - mSq)`,
and evaluating at `kSq = mSq` vanishes identically. -/
theorem fourBodyExchangePoly_antisym_pole_and_gap (kSq mSq : Int) :
    fourBodyExchangePoly kSq mSq - (kSq - mSq) * (kSq - mSq) =
      -4 * mSq * (kSq - mSq) ∧
    fourBodyExchangePoly mSq mSq + kSq = kSq := by
  dsimp only [fourBodyExchangePoly]
  have h1 : (kSq - 5 * mSq) * (kSq - mSq) - (kSq - mSq) * (kSq - mSq) =
      -4 * mSq * (kSq - mSq) := by
    rw [← Int.sub_mul]
    have hsub : (kSq - 5 * mSq) - (kSq - mSq) = -4 * mSq := by omega
    rw [hsub]
  have h2 : (mSq - 5 * mSq) * (mSq - mSq) + kSq = kSq := by
    have hz : mSq - mSq = 0 := by omega
    rw [hz, Int.mul_zero]
    omega
  exact ⟨h1, h2⟩

/-! ## Section 3: Three-Braid Abelianization Writhe & Block Balance (`qou-k8ek`) -/

/-- Total writhe `a1 + b1 + a2 + b2` and strand-layer balance `(a1 + a2) - (b1 + b2)` of a
two-block 3-braid word. -/
def threeBraidWrithePair (a1 b1 a2 b2 : Int) : Int × Int :=
  (a1 + b1 + a2 + b2, (a1 + a2) - (b1 + b2))

-- Bean qou-k8ek: recovery of first-generator exponent sum and permutation invariance.
/-- Adding the two components of `threeBraidWrithePair` yields `2 * (a1 + a2)`, and swapping
`a1` with `a2` preserves the total abelianized writhe. -/
theorem threeBraidWrithePair_reordering_invariance_and_sum (a1 b1 a2 b2 : Int) :
    (threeBraidWrithePair a1 b1 a2 b2).1 + (threeBraidWrithePair a1 b1 a2 b2).2 =
      2 * (a1 + a2) ∧
    (threeBraidWrithePair a2 b1 a1 b2).1 = (threeBraidWrithePair a1 b1 a2 b2).1 := by
  dsimp only [threeBraidWrithePair]
  have h1 : (a1 + b1 + a2 + b2) + ((a1 + a2) - (b1 + b2)) = 2 * (a1 + a2) := by
    omega
  have h2 : a2 + b1 + a1 + b2 = a1 + b1 + a2 + b2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-k8ek: recovery of second-generator exponent sum and formal commutator neutrality.
/-- Subtracting the second component from the first in `threeBraidWrithePair` yields `2 * (b1 + b2)`,
and a formal commutator block `(a1, b1, -a1, -b1)` has zero net writhe. -/
theorem threeBraidWrithePair_commutator_neutral_and_difference (a1 b1 a2 b2 : Int) :
    (threeBraidWrithePair a1 b1 a2 b2).1 - (threeBraidWrithePair a1 b1 a2 b2).2 =
      2 * (b1 + b2) ∧
    (threeBraidWrithePair a1 b1 (-a1) (-b1)).1 + a2 + b2 = a2 + b2 := by
  dsimp only [threeBraidWrithePair]
  have h1 : (a1 + b1 + a2 + b2) - ((a1 + a2) - (b1 + b2)) = 2 * (b1 + b2) := by
    omega
  have h2 : (a1 + b1 + (-a1) + (-b1)) + a2 + b2 = a2 + b2 := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 4: First-Order Prolongation Symbol & Binding Kernel (`qou-kc7y`) -/

/-- First-order jet prolongation symbol `(q - 1) * x + d`. -/
def prolongationSymbol (q x d : Int) : Int :=
  (q - 1) * x + d

-- Bean qou-kc7y: joint additivity in `(x, d)` and classical specialization at `q = 1`.
/-- For fixed `q`, `prolongationSymbol q` is additive in `(x, d)`, and at `q = 1` it reduces
to the fibre derivative `d1`. -/
theorem prolongationSymbol_linearity_and_classical_limit (q x1 x2 d1 d2 : Int) :
    prolongationSymbol q (x1 + x2) (d1 + d2) =
      prolongationSymbol q x1 d1 + prolongationSymbol q x2 d2 ∧
    prolongationSymbol 1 x1 d1 + q + x2 + d2 = d1 + q + x2 + d2 := by
  dsimp only [prolongationSymbol]
  have h1 : (q - 1) * (x1 + x2) + (d1 + d2) =
      ((q - 1) * x1 + d1) + ((q - 1) * x2 + d2) := by
    rw [Int.mul_add]
    omega
  have h2 : ((1 - 1) * x1 + d1) + q + x2 + d2 = d1 + q + x2 + d2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-kc7y: deformation parameter difference and unit `q`-shift increment.
/-- Subtracting `prolongationSymbol q2 x d` from `prolongationSymbol q1 x d` cancels `d` and
factors as `(q1 - q2) * x`, with unit `q`-step equal to `x`. -/
theorem prolongationSymbol_shift_and_commutator (q1 q2 x d : Int) :
    prolongationSymbol q1 x d - prolongationSymbol q2 x d = (q1 - q2) * x ∧
    prolongationSymbol (q1 + 1) x d - prolongationSymbol q1 x d + q2 = x + q2 := by
  dsimp only [prolongationSymbol]
  have h1 : ((q1 - 1) * x + d) - ((q2 - 1) * x + d) = (q1 - q2) * x := by
    have hsub : (q1 - 1) * x - (q2 - 1) * x = (q1 - q2) * x := by
      rw [← Int.sub_mul]
      have hq : (q1 - 1) - (q2 - 1) = q1 - q2 := by omega
      rw [hq]
    omega
  have h2 : (((q1 + 1) - 1) * x + d) - ((q1 - 1) * x + d) + q2 = x + q2 := by
    have hstep : ((q1 + 1) - 1) * x - (q1 - 1) * x = x := by
      rw [← Int.sub_mul]
      have hq : ((q1 + 1) - 1) - (q1 - 1) = 1 := by omega
      rw [hq, Int.one_mul]
    omega
  exact ⟨h1, h2⟩

/-! ## Section 5: Crossing-Multiplicity Stratification Gap (`qou-kyh5`) -/

/-- Crossing-to-multiplicity stratification gap `crossings - 2 * nu`. -/
def crossingMultiplicityGap (crossings nu : Int) : Int :=
  crossings - 2 * nu

-- Bean qou-kyh5: additivity under connected-sum composition and invariance under `(c + 2k, nu + k)`.
/-- `crossingMultiplicityGap` is additive across `(c1 + c2, nu1 + nu2)` and invariant when
`crossings` increases by `2 * nu2` while `nu` increases by `nu2`. -/
theorem crossingMultiplicityGap_additivity_and_double_shift (c1 c2 nu1 nu2 : Int) :
    crossingMultiplicityGap (c1 + c2) (nu1 + nu2) =
      crossingMultiplicityGap c1 nu1 + crossingMultiplicityGap c2 nu2 ∧
    crossingMultiplicityGap (c1 + 2 * nu2) (nu1 + nu2) + c2 =
      crossingMultiplicityGap c1 nu1 + c2 := by
  dsimp only [crossingMultiplicityGap]
  have h1 : (c1 + c2) - 2 * (nu1 + nu2) =
      (c1 - 2 * nu1) + (c2 - 2 * nu2) := by
    omega
  have h2 : ((c1 + 2 * nu2) - 2 * (nu1 + nu2)) + c2 =
      (c1 - 2 * nu1) + c2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-kyh5: unconfirmed anchor (`nu = 0`) vs confirmed atom (`nu > 0`) gap difference.
/-- Comparing an unconfirmed anchor (`nu = 0`) with a confirmed atom of multiplicity `nu` at
crossing number `c` yields `2 * nu`, and simultaneous `(2 * delta, delta)` shifts preserve the gap. -/
theorem crossingMultiplicityGap_anchor_vs_confirmed_balance (c nu delta : Int) :
    crossingMultiplicityGap c 0 - crossingMultiplicityGap c nu = 2 * nu ∧
    crossingMultiplicityGap (c + 2 * delta) (nu + delta) =
      crossingMultiplicityGap c nu := by
  dsimp only [crossingMultiplicityGap]
  have h1 : (c - 2 * 0) - (c - 2 * nu) = 2 * nu := by
    omega
  have h2 : (c + 2 * delta) - 2 * (nu + delta) = c - 2 * nu := by
    omega
  exact ⟨h1, h2⟩

end QOU.QBeta.SelfConjugateMultiplicityAndProlongationKernelBrick
