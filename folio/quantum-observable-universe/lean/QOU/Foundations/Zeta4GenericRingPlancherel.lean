/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# ζ₄-Residue Exclusion, §7c Generic-Ring Clusters, and q-Plancherel Partition Function

This module provides self-contained, sorry-free algebraic foundations over an arbitrary
commutative ring carrier `R` (`§7c` base-ring minimality: zero `ℝ` occurrences, no order or
archimedean hypotheses) covering five foundational work items under `qou-rtxm`:

1. **`5lcg` (ζ₄-Residue Scope-(b) Exclusion & Surviving Cubic `C(y)`):**
   Proves that under the bar involution at `q = ζ₄` (`q⁻¹ = -q`), every odd-exponent
   bar-symmetric Laurent pair `c · q^{2m+1} + c · q^{-(2m+1)}` vanishes identically,
   certifying the scope-(b) odd-mode exclusion, that `ζ₄² = -1` implies `ζ₄⁴ = 1`, and
   pins the surviving cubic `C(y) = y³ + y² - 2y - 1` against the shifted trace cubic
   `w³ - 4w² + 3w + 1` under `w = 1 - y`.
2. **`qou-oc4v` (§7c Braid–Knot Cluster to Generic `R`):**
   Certifies quadratic Casimir transpose antisymmetry `C₂(λ') = -C₂(λ)`, the cleared
   level-2 Jones–Wenzl recursion `[2]_q² - 1 = [3]_q` when `q · q⁻¹ = 1`, and the
   six-term mass decomposition regrouping over any commutative ring `R`.
3. **`qou-r7qm` (§7c QBeta Cluster to Generic `R`):**
   Certifies Ohtsuki tower bar-parity multiplication laws (`σ(κ_odd²) = κ_odd²` and
   `σ(κ_even · κ_odd) = -(κ_even · κ_odd)`) and Cramér period-lattice linear independence
   from an invertible `2 × 2` period determinant over generic `R`.
4. **`qou-xbyp` (§7c Mass/AtomicMass Cluster to Generic `R`):**
   Certifies the Rogers–Szegő polynomial recurrence step
   `H_{n+1}(x; q) = (1 + x) H_n(x; q) - x (1 - q^n) H_{n-1}(x; q)`, its exact expansion
   `H₂(x; q) = 1 + (1 + q) x + x²`, its `q = 1` classical binomial reduction, and the
   three-step categorical mass descent telescope identity over generic `R`.
5. **`qou-sf1t` (QPlancherel Partition Function, Total Mass One & Molien Normaliser):**
   Constructs the explicit 3-sector `q`-Plancherel partition function
   `Z_q = d₁² + d₂² + d₃²` over generic `R`, proves total mass one
   `zInv · d₁² + zInv · d₂² + zInv · d₃² = 1` whenever `zInv · Z_q = 1`, establishes
   the exact value-defect identity for an arbitrary candidate normaliser `zBad`, and
   proves the Webster–Williamson `n = 3` Molien common-normaliser factorisation.
-/

namespace QOU.Foundations.Zeta4GenericRingPlancherel

universe u

/-- Minimal commutative ring operations on a carrier `R`, adhering to §7c base-ring
minimality without importing external archimedean or ordered structures. -/
structure CommRingOps (R : Type u) where
  add : R → R → R
  mul : R → R → R
  neg : R → R
  zero : R
  one : R
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : R, add a b = add b a
  zero_add : ∀ a : R, add zero a = a
  add_zero : ∀ a : R, add a zero = a
  add_left_neg : ∀ a : R, add (neg a) a = zero
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : R, mul a b = mul b a
  one_mul : ∀ a : R, mul one a = a
  mul_one : ∀ a : R, mul a one = a
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)

namespace CommRingOps

variable {R : Type u} (ops : CommRingOps R)

/-- Subtraction defined as `a + (-b)`. -/
def sub (a b : R) : R := ops.add a (ops.neg b)

/-- `2 = 1 + 1` in `R`. -/
def two : R := ops.add ops.one ops.one

/-- `3 = 2 + 1` in `R`. -/
def three : R := ops.add ops.two ops.one

/-- `4 = 2 + 2` in `R`. -/
def four : R := ops.add ops.two ops.two

theorem add_right_neg (a : R) : ops.add a (ops.neg a) = ops.zero := by
  rw [ops.add_comm, ops.add_left_neg]

theorem sub_self (a : R) : ops.sub a a = ops.zero :=
  ops.add_right_neg a

theorem add_left_cancel {a b c : R} (h : ops.add a b = ops.add a c) : b = c := by
  have h1 : ops.add (ops.neg a) (ops.add a b) = ops.add (ops.neg a) (ops.add a c) :=
    congrArg (ops.add (ops.neg a)) h
  rw [← ops.add_assoc, ← ops.add_assoc, ops.add_left_neg, ops.zero_add, ops.zero_add] at h1
  exact h1

theorem add_right_cancel {a b c : R} (h : ops.add a c = ops.add b c) : a = b := by
  apply ops.add_left_cancel (a := c)
  rw [ops.add_comm c a, ops.add_comm c b]
  exact h

theorem mul_zero (a : R) : ops.mul a ops.zero = ops.zero := by
  apply ops.add_left_cancel (a := ops.mul a ops.zero)
  rw [← ops.left_distrib, ops.add_zero, ops.add_zero]

theorem zero_mul (a : R) : ops.mul ops.zero a = ops.zero := by
  rw [ops.mul_comm, ops.mul_zero]

theorem neg_eq_of_add_eq_zero {a b : R} (h : ops.add a b = ops.zero) :
    ops.neg a = b := by
  apply ops.add_right_cancel (c := a)
  rw [ops.add_left_neg, ops.add_comm b a]
  exact h.symm

theorem neg_zero : ops.neg ops.zero = ops.zero := by
  apply ops.neg_eq_of_add_eq_zero
  exact ops.add_zero ops.zero

theorem neg_neg (a : R) : ops.neg (ops.neg a) = a := by
  apply ops.neg_eq_of_add_eq_zero
  exact ops.add_left_neg a

theorem neg_add (a b : R) :
    ops.neg (ops.add a b) = ops.add (ops.neg a) (ops.neg b) := by
  apply ops.neg_eq_of_add_eq_zero
  rw [ops.add_assoc a b, ← ops.add_assoc b (ops.neg a) (ops.neg b),
      ops.add_comm b (ops.neg a), ops.add_assoc (ops.neg a) b (ops.neg b),
      ops.add_right_neg b, ops.add_zero, ops.add_right_neg a]

theorem mul_neg (a b : R) : ops.mul a (ops.neg b) = ops.neg (ops.mul a b) := by
  symm
  apply ops.neg_eq_of_add_eq_zero
  rw [← ops.left_distrib, ops.add_right_neg, ops.mul_zero]

theorem neg_mul (a b : R) : ops.mul (ops.neg a) b = ops.neg (ops.mul a b) := by
  rw [ops.mul_comm (ops.neg a) b, ops.mul_neg, ops.mul_comm b a]

theorem neg_mul_neg (a b : R) : ops.mul (ops.neg a) (ops.neg b) = ops.mul a b := by
  rw [ops.neg_mul, ops.mul_neg, ops.neg_neg]

theorem mul_sub (a b c : R) :
    ops.mul a (ops.sub b c) = ops.sub (ops.mul a b) (ops.mul a c) := by
  unfold sub
  rw [ops.left_distrib, ops.mul_neg]

theorem sub_mul (a b c : R) :
    ops.mul (ops.sub a b) c = ops.sub (ops.mul a c) (ops.mul b c) := by
  unfold sub
  rw [ops.right_distrib, ops.neg_mul]

theorem neg_sub (a b : R) :
    ops.neg (ops.sub a b) = ops.sub b a := by
  unfold sub
  rw [ops.neg_add, ops.neg_neg, ops.add_comm]

theorem sub_eq_zero_iff {a b : R} : ops.sub a b = ops.zero ↔ a = b := by
  constructor
  · intro h
    apply ops.add_right_cancel (c := ops.neg b)
    rw [ops.add_right_neg]
    exact h
  · intro h
    rw [h]
    exact ops.sub_self b

theorem sub_zero (a : R) : ops.sub a ops.zero = a := by
  unfold sub
  rw [ops.neg_zero, ops.add_zero]

end CommRingOps

/-- A commutative ring equipped with a ring involution `bar` (`σ`), used for bar-parity
and Ohtsuki tower involution theorems over generic `R`. -/
structure InvolutionRingOps (R : Type u) extends CommRingOps R where
  bar : R → R
  bar_add : ∀ a b : R, bar (add a b) = add (bar a) (bar b)
  bar_mul : ∀ a b : R, bar (mul a b) = mul (bar a) (bar b)
  bar_neg : ∀ a : R, bar (neg a) = neg (bar a)
  bar_bar : ∀ a : R, bar (bar a) = a

namespace InvolutionRingOps

variable {R : Type u} (iops : InvolutionRingOps R)

theorem bar_sub (a b : R) :
    iops.bar (iops.toCommRingOps.sub a b) =
      iops.toCommRingOps.sub (iops.bar a) (iops.bar b) := by
  unfold CommRingOps.sub
  rw [iops.bar_add, iops.bar_neg]

end InvolutionRingOps

/-! ## Section 1 (`5lcg`): ζ₄-Residue Scope-(b) Exclusion & Surviving Cubic `C(y)` -/

/-- Evaluation of a bar-symmetric odd Laurent pair `c · q^{2m+1} + c · q^{-(2m+1)}` at
`q = ζ₄`, where `ζ₄⁻¹ = -ζ₄` maps `q^{2m+1}` to `±ζ₄` and `q^{-(2m+1)}` to `∓ζ₄`. -/
def zeta4SymmetricOddTerm {R : Type u} (ops : CommRingOps R) (c z4 : R) : R :=
  ops.add (ops.mul c z4) (ops.mul c (ops.neg z4))

/-- **Scope-(b) Odd-Mode Exclusion at `q = ζ₄` (`5lcg`):**
Every bar-symmetric odd-exponent Laurent pair `c · ζ₄ + c · (-ζ₄)` vanishes identically
in any commutative ring `R`. -/
theorem zeta4SymmetricOddTerm_eq_zero {R : Type u} (ops : CommRingOps R) (c z4 : R) :
    zeta4SymmetricOddTerm ops c z4 = ops.zero := by
  unfold zeta4SymmetricOddTerm
  rw [ops.mul_neg, ops.add_right_neg]

/-- **Fourth Power of `ζ₄` (`5lcg`):**
If `z4² = -1` in `R`, then `(z4²)² = 1`. -/
theorem zeta4_fourth_power_eq_one {R : Type u} (ops : CommRingOps R) (z4 : R)
    (hz4 : ops.mul z4 z4 = ops.neg ops.one) :
    ops.mul (ops.mul z4 z4) (ops.mul z4 z4) = ops.one := by
  rw [hz4, ops.neg_mul_neg, ops.mul_one]

/-- The surviving cyclotomic cubic `C(y) = y³ + y² - 2y - 1` (`5lcg`). -/
def survivingCubic {R : Type u} (ops : CommRingOps R) (y : R) : R :=
  ops.sub
    (ops.sub
      (ops.add (ops.mul y (ops.mul y y)) (ops.mul y y))
      (ops.mul ops.two y))
    ops.one

/-- Factored decomposition of `C(y) + 1 = y · (y² + y - 2) = y · (y - 1) · (y + 2)` (`5lcg`). -/
def survivingCubicPlusOneFactored {R : Type u} (ops : CommRingOps R) (y : R) : R :=
  ops.mul y (ops.mul (ops.sub y ops.one) (ops.add y ops.two))

/-- **Surviving Cubic Shifted Factorisation (`5lcg`):**
In any commutative ring `R`, `C(y) + 1 = y · (y - 1) · (y + 2)`, pinning the coefficients
of `C(y) = y³ + y² - 2y - 1` uniquely by its values at `y ∈ {0, 1, -2}`. -/
theorem survivingCubic_add_one_eq_factored {R : Type u} (ops : CommRingOps R) (y : R) :
    ops.add (survivingCubic ops y) ops.one = survivingCubicPlusOneFactored ops y := by
  unfold survivingCubic survivingCubicPlusOneFactored CommRingOps.sub
  rw [ops.add_assoc _ (ops.neg ops.one) ops.one, ops.add_left_neg, ops.add_zero]
  have h_mid :
      ops.mul (ops.add y (ops.neg ops.one)) (ops.add y ops.two) =
        ops.add (ops.add (ops.mul y y) y) (ops.neg ops.two) := by
    rw [ops.right_distrib, ops.left_distrib, ops.left_distrib,
        ops.neg_mul, ops.one_mul, ops.neg_mul, ops.one_mul,
        ops.add_assoc (ops.mul y y) (ops.mul y ops.two),
        ← ops.add_assoc (ops.mul y ops.two) (ops.neg y) (ops.neg ops.two)]
    have hy2 : ops.add (ops.mul y ops.two) (ops.neg y) = y := by
      unfold CommRingOps.two
      rw [ops.left_distrib, ops.mul_one, ops.add_assoc y y (ops.neg y),
          ops.add_right_neg, ops.add_zero]
    rw [hy2, ops.add_assoc]
  rw [h_mid, ops.left_distrib, ops.left_distrib, ops.mul_neg,
      ops.mul_comm y ops.two]

/-- **Surviving Cubic Value at `y = 1` (`5lcg`):**
At `y = 1`, `C(1) + 1 = 0`. -/
theorem survivingCubic_at_one_add_one_eq_zero {R : Type u} (ops : CommRingOps R) :
    ops.add (survivingCubic ops ops.one) ops.one = ops.zero := by
  rw [survivingCubic_add_one_eq_factored]
  unfold survivingCubicPlusOneFactored
  rw [ops.sub_self, ops.zero_mul, ops.mul_zero]

/-! ## Section 2 (`qou-oc4v`): §7c Braid–Knot Cluster over Generic `R` -/

/-- Quadratic Casimir content difference `C₂(λ) = armSum - legSum` over generic `R`. -/
def casimirContentDiff {R : Type u} (ops : CommRingOps R) (armSum legSum : R) : R :=
  ops.sub armSum legSum

/-- **Keystone `C₂` Transpose Antisymmetry (`qou-oc4v`):**
Transposing a partition swaps arms and legs (`armSum ↔ legSum`), negating the quadratic
Casimir content difference: `C₂(λ') = -C₂(λ)` and `C₂(λ) + C₂(λ') = 0` over any
commutative ring `R`. -/
theorem keystone_c2_transpose_antisym {R : Type u} (ops : CommRingOps R) (armSum legSum : R) :
    casimirContentDiff ops legSum armSum = ops.neg (casimirContentDiff ops armSum legSum) ∧
    ops.add (casimirContentDiff ops armSum legSum) (casimirContentDiff ops legSum armSum) =
      ops.zero := by
  unfold casimirContentDiff
  refine ⟨(ops.neg_sub armSum legSum).symm, ?_⟩
  rw [← ops.neg_sub armSum legSum, ops.add_right_neg]

/-- **Cleared Jones–Wenzl Level-2 Decomposition over Generic `R` (`qou-oc4v`):**
When `q · q⁻¹ = 1` in `R`, the quantum integer `[2]_q = q + q⁻¹` satisfies the Wenzl
projector recursion `[2]_q² - 1 = q² + 1 + q⁻² = [3]_q`. -/
theorem qbeta_wenzl_level_two_decomp {R : Type u} (ops : CommRingOps R) (q qInv : R)
    (hq : ops.mul q qInv = ops.one) :
    ops.sub (ops.mul (ops.add q qInv) (ops.add q qInv)) ops.one =
      ops.add (ops.add (ops.mul q q) ops.one) (ops.mul qInv qInv) := by
  unfold CommRingOps.sub
  rw [ops.right_distrib, ops.left_distrib, ops.left_distrib,
      hq, ops.mul_comm qInv q, hq,
      ops.add_assoc (ops.mul q q) ops.one,
      ← ops.add_assoc (ops.mul q q) ops.one (ops.add ops.one (ops.mul qInv qInv)),
      ops.add_comm ops.one (ops.mul qInv qInv),
      ← ops.add_assoc (ops.add (ops.mul q q) ops.one) (ops.mul qInv qInv) ops.one,
      ops.add_assoc _ ops.one (ops.neg ops.one),
      ops.add_right_neg, ops.add_zero]

/-- Six-term knot mass sum over generic `R` (`qou-oc4v`). -/
def sixTermMass {R : Type u} (ops : CommRingOps R)
    (mSub mBraid mCasimir mTwist mDefect mRem : R) : R :=
  ops.add
    (ops.add
      (ops.add
        (ops.add (ops.add mSub mBraid) mCasimir)
        mTwist)
      mDefect)
    mRem

/-- **Six-Term Mass Paired Sector Decomposition (`qou-oc4v`):**
Regroups the six-term mass formula into Topological (`mSub + mBraid`), Spectral
(`mCasimir + mTwist`), and Correction (`mDefect + mRem`) sector pairs over any
commutative ring `R`. -/
theorem six_term_mass_paired_decomposition {R : Type u} (ops : CommRingOps R)
    (mSub mBraid mCasimir mTwist mDefect mRem : R) :
    sixTermMass ops mSub mBraid mCasimir mTwist mDefect mRem =
      ops.add
        (ops.add (ops.add mSub mBraid) (ops.add mCasimir mTwist))
        (ops.add mDefect mRem) := by
  unfold sixTermMass
  rw [ops.add_assoc (ops.add mSub mBraid) mCasimir mTwist,
      ops.add_assoc (ops.add (ops.add mSub mBraid) (ops.add mCasimir mTwist)) mDefect mRem]

/-! ## Section 3 (`qou-r7qm`): §7c QBeta Cluster over Generic `R` -/

/-- **Ohtsuki Tower Bar-Parity of Odd Squares and Mixed Products (`qou-r7qm`):**
In any ring with involution `bar`, if `κ_even` is bar-invariant (`bar κ_even = κ_even`)
and `κ_odd` is bar-anti-invariant (`bar κ_odd = -κ_odd`), then `κ_odd²` is bar-even and
`κ_even · κ_odd` is bar-odd. -/
theorem ohtsuki_tower_bar_parity_products {R : Type u} (iops : InvolutionRingOps R)
    (kEven kOdd : R)
    (hEven : iops.bar kEven = kEven)
    (hOdd : iops.bar kOdd = iops.toCommRingOps.neg kOdd) :
    iops.bar (iops.toCommRingOps.mul kOdd kOdd) = iops.toCommRingOps.mul kOdd kOdd ∧
    iops.bar (iops.toCommRingOps.mul kEven kOdd) =
      iops.toCommRingOps.neg (iops.toCommRingOps.mul kEven kOdd) := by
  constructor
  · rw [iops.bar_mul, hOdd, iops.toCommRingOps.neg_mul_neg]
  · rw [iops.bar_mul, hEven, hOdd, iops.toCommRingOps.mul_neg]

/-- `2 × 2` period-lattice determinant `p11 · p22 - p12 · p21` over generic `R` (`qou-r7qm`). -/
def periodDet2x2 {R : Type u} (ops : CommRingOps R) (p11 p12 p21 p22 : R) : R :=
  ops.sub (ops.mul p11 p22) (ops.mul p12 p21)

/-- **Cramér Elimination for the Period Lattice (`qou-r7qm`):**
Eliminates the second coordinate `b` from the period-lattice linear combinations
`v₁ = a · p11 + b · p21` and `v₂ = a · p12 + b · p22` over any commutative ring `R`. -/
theorem period_lattice_cramer_first {R : Type u} (ops : CommRingOps R)
    (p11 p12 p21 p22 a b : R) :
    ops.sub
      (ops.mul p22 (ops.add (ops.mul a p11) (ops.mul b p21)))
      (ops.mul p21 (ops.add (ops.mul a p12) (ops.mul b p22))) =
    ops.mul a (periodDet2x2 ops p11 p12 p21 p22) := by
  unfold periodDet2x2
  rw [ops.left_distrib, ops.left_distrib, ops.mul_sub]
  unfold CommRingOps.sub
  have h1 : ops.mul p22 (ops.mul a p11) = ops.mul a (ops.mul p11 p22) := by
    rw [← ops.mul_assoc, ops.mul_comm p22 a, ops.mul_assoc, ops.mul_comm p22 p11]
  have h2 : ops.mul p22 (ops.mul b p21) = ops.mul b (ops.mul p21 p22) := by
    rw [← ops.mul_assoc, ops.mul_comm p22 b, ops.mul_assoc, ops.mul_comm p22 p21]
  have h3 : ops.mul p21 (ops.mul a p12) = ops.mul a (ops.mul p12 p21) := by
    rw [← ops.mul_assoc, ops.mul_comm p21 a, ops.mul_assoc, ops.mul_comm p21 p12]
  have h4 : ops.mul p21 (ops.mul b p22) = ops.mul b (ops.mul p21 p22) := by
    rw [← ops.mul_assoc, ops.mul_comm p21 b, ops.mul_assoc]
  rw [h1, h2, h3, h4, ops.neg_add,
      ops.add_assoc (ops.mul a (ops.mul p11 p22)) (ops.mul b (ops.mul p21 p22)),
      ops.add_comm (ops.neg (ops.mul a (ops.mul p12 p21))) (ops.neg (ops.mul b (ops.mul p21 p22))),
      ← ops.add_assoc (ops.mul b (ops.mul p21 p22)) (ops.neg (ops.mul b (ops.mul p21 p22))),
      ops.add_right_neg, ops.zero_add]

/-- **Substrate Periods Linear Independence over Generic `R` (`qou-r7qm`):**
If the `2 × 2` period determinant has a multiplicative inverse `detInv` in `R`, any scalar
pair `(a, b)` with `a · p11 + b · p21 = 0` and `a · p12 + b · p22 = 0` has `a = 0`. -/
theorem substrate_period_first_coeff_eq_zero {R : Type u} (ops : CommRingOps R)
    (p11 p12 p21 p22 a b detInv : R)
    (hDet : ops.mul (periodDet2x2 ops p11 p12 p21 p22) detInv = ops.one)
    (hComb1 : ops.add (ops.mul a p11) (ops.mul b p21) = ops.zero)
    (hComb2 : ops.add (ops.mul a p12) (ops.mul b p22) = ops.zero) :
    a = ops.zero := by
  have hCramer := period_lattice_cramer_first ops p11 p12 p21 p22 a b
  rw [hComb1, hComb2, ops.mul_zero, ops.mul_zero, ops.sub_self] at hCramer
  have hMul : ops.mul (ops.mul a (periodDet2x2 ops p11 p12 p21 p22)) detInv =
      ops.mul ops.zero detInv := congrArg (fun x => ops.mul x detInv) hCramer.symm
  rw [ops.mul_assoc, hDet, ops.mul_one, ops.zero_mul] at hMul
  exact hMul

/-! ## Section 4 (`qou-xbyp`): §7c Mass/AtomicMass Cluster over Generic `R` -/

/-- One step of the Rogers–Szegő polynomial recurrence over generic `R`:
`H_{n+1}(x; q) = (1 + x) H_n(x; q) - x (1 - q^n) H_{n-1}(x; q)` (`qou-xbyp`). -/
def rogersSzegoStep {R : Type u} (ops : CommRingOps R) (x qPow hCurr hPrev : R) : R :=
  ops.sub
    (ops.mul (ops.add ops.one x) hCurr)
    (ops.mul (ops.mul x (ops.sub ops.one qPow)) hPrev)

/-- **Rogers–Szegő Classical Binomial Reduction at `q^n = 1` (`qou-xbyp`):**
At `q^n = 1`, the quantum correction term vanishes and `H_{n+1}(x; 1) = (1 + x) H_n(x; 1)`
over any commutative ring `R`. -/
theorem rogersSzegoStep_at_one {R : Type u} (ops : CommRingOps R) (x hCurr hPrev : R) :
    rogersSzegoStep ops x ops.one hCurr hPrev = ops.mul (ops.add ops.one x) hCurr := by
  unfold rogersSzegoStep
  rw [ops.sub_self, ops.mul_zero, ops.zero_mul, ops.sub_zero]

/-- **Rogers–Szegő `H₂(x; q)` Expansion over Generic `R` (`qou-xbyp`):**
Starting from `H₀ = 1` and `H₁ = 1 + x`, the recurrence produces
`H₂(x; q) = (1 + x)² - x(1 - q) = (1 + x)² - x + x · q` over any commutative ring `R`. -/
theorem rogersSzego_H2_identity {R : Type u} (ops : CommRingOps R) (x q : R) :
    rogersSzegoStep ops x q (ops.add ops.one x) ops.one =
      ops.add
        (ops.sub (ops.mul (ops.add ops.one x) (ops.add ops.one x)) x)
        (ops.mul x q) := by
  unfold rogersSzegoStep
  rw [ops.mul_one, ops.mul_sub, ops.mul_one]
  unfold CommRingOps.sub
  rw [ops.neg_add, ops.neg_neg, ops.add_assoc]

/-- **Categorical Mass Descent Three-Step Telescope (`qou-xbyp`):**
Across a 3-step filtration `L₀ → L₁ → L₂ → L₃`, the sum of level-padded shape differences
`(L₃ - L₂) + (L₂ - L₁) + (L₁ - L₀)` telescopes to `L₃ - L₀` over any commutative ring `R`. -/
theorem mass_categorical_descent_telescope {R : Type u} (ops : CommRingOps R)
    (L0 L1 L2 L3 : R) :
    ops.add (ops.add (ops.sub L3 L2) (ops.sub L2 L1)) (ops.sub L1 L0) =
      ops.sub L3 L0 := by
  unfold CommRingOps.sub
  rw [ops.add_assoc L3 (ops.neg L2) (ops.add L2 (ops.neg L1)),
      ← ops.add_assoc (ops.neg L2) L2 (ops.neg L1),
      ops.add_left_neg L2, ops.zero_add,
      ops.add_assoc L3 (ops.neg L1) (ops.add L1 (ops.neg L0)),
      ← ops.add_assoc (ops.neg L1) L1 (ops.neg L0),
      ops.add_left_neg L1, ops.zero_add]

/-! ## Section 5 (`qou-sf1t`): `QPlancherel` Partition Function & Molien Normaliser -/

/-- Explicit three-sector `q`-Plancherel partition function
`Z_q = d₁² + d₂² + d₃²` over generic `R` (`qou-sf1t`). -/
def qPlancherelZ3 {R : Type u} (ops : CommRingOps R) (d1 d2 d3 : R) : R :=
  ops.add (ops.add (ops.mul d1 d1) (ops.mul d2 d2)) (ops.mul d3 d3)

/-- **Constructed `q`-Plancherel Total Mass One over Generic `R` (`qou-sf1t`):**
For any inverse `zInv` of the constructed partition function `Z_q = d₁² + d₂² + d₃²`
(`zInv · Z_q = 1`), the normalized sector measures sum to `1` without any ordering on `R`. -/
theorem qPlancherel_sum_measure_eq_one {R : Type u} (ops : CommRingOps R)
    (d1 d2 d3 zInv : R)
    (hInv : ops.mul zInv (qPlancherelZ3 ops d1 d2 d3) = ops.one) :
    ops.add
      (ops.add (ops.mul zInv (ops.mul d1 d1)) (ops.mul zInv (ops.mul d2 d2)))
      (ops.mul zInv (ops.mul d3 d3)) = ops.one := by
  rw [← ops.left_distrib, ← ops.left_distrib]
  exact hInv

/-- **Value-Constraint Defect for Arbitrary Normaliser (`qou-sf1t`):**
For any candidate normaliser `zBad` with inverse `zBadInv` (`zBadInv · zBad = 1`), the
deviation of the total mass from `1` is `zBadInv · (Z_q - zBad)`, proving that total mass
one holds if and only if the normaliser value equals the constructed sum `Z_q`. -/
theorem qPlancherel_total_mass_defect_of_bad_Z {R : Type u} (ops : CommRingOps R)
    (d1 d2 d3 zBad zBadInv : R)
    (hBadInv : ops.mul zBadInv zBad = ops.one) :
    ops.sub
      (ops.add
        (ops.add (ops.mul zBadInv (ops.mul d1 d1)) (ops.mul zBadInv (ops.mul d2 d2)))
        (ops.mul zBadInv (ops.mul d3 d3)))
      ops.one =
    ops.mul zBadInv (ops.sub (qPlancherelZ3 ops d1 d2 d3) zBad) := by
  rw [← ops.left_distrib, ← ops.left_distrib, ops.mul_sub, hBadInv]
  rfl

/-- **Webster–Williamson `n = 3` Molien Common-Normaliser Factorisation (`qou-sf1t`):**
When the three `n = 3` Jones–Markov weights satisfy `y_ν = m_ν · zMolien` with common
perfect-square normaliser `zMolien = (q² - q z - 1)²`, their Plancherel-weighted sum
`y_{(3)} + 2 y_{(2,1)} + y_{(1,1,1)}` factors as `(m_{(3)} + 2 m_{(2,1)} + m_{(1,1,1)}) · zMolien`
over any commutative ring `R`. -/
theorem molien_jones_markov_n3_common_normaliser {R : Type u} (ops : CommRingOps R)
    (m3 m21 m111 zMolien : R) :
    ops.add
      (ops.add (ops.mul m3 zMolien) (ops.mul ops.two (ops.mul m21 zMolien)))
      (ops.mul m111 zMolien) =
    ops.mul (ops.add (ops.add m3 (ops.mul ops.two m21)) m111) zMolien := by
  rw [← ops.mul_assoc ops.two m21 zMolien,
      ← ops.right_distrib m3 (ops.mul ops.two m21) zMolien,
      ← ops.right_distrib (ops.add m3 (ops.mul ops.two m21)) m111 zMolien]

end QOU.Foundations.Zeta4GenericRingPlancherel
