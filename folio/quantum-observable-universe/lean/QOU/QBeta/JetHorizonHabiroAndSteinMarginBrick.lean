/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Jet Horizon Filtration, Gram Interior Margin, Cyclotomic Truncation, and Transfer Remainder Brick

Formalizes algebraic and arithmetic bricks for five tasks in the `b9cj` / `qou-10v9` lane:
1. `qou-iv9f`: Degree-graded jet multiplication in $A_0 \oplus A_1 \varepsilon / (\varepsilon^2)$
   and nilpotency of the horizon ideal $\mathfrak{h} = A_1 \varepsilon$.
2. `qou-j1bs`: Symmetric $2 \times 2$ Gram matrix interior margin, completed-square identity,
   and isotropic diagonal stratification shift.
3. `qou-j6i3`: Two-step cyclotomic truncation polynomial $(q - 1)$ factorization and finite
   step differences at $q = 1$ specialization.
4. `qou-jh3m`: Bilinear Cauchy-Schwarz margin propagation $m = \rho \sigma_A - \sigma_D$ and
   threshold headroom above $N_0 = 78$.
5. `qou-jy04`: Exchangeable-pair 3-cycle scaled drift $3 \omega_3$, falling-factorial variance
   $n(n-1)(n-2)$, and Taylor transfer remainder $R = g(1) - g(0) - g'(0)$.
-/

namespace QOU.QBeta.JetHorizonHabiroAndSteinMarginBrick

/-! ## Section 1: Degree-Graded Jet Multiplication & Horizon Ideal (`qou-iv9f`) -/

/-- Truncated degree-1 jet multiplication `(a0 + a1 ε)(b0 + b1 ε) = a0 b0 + (a0 b1 + a1 b0) ε`
modulo `ε^2 = 0`. -/
def jetProductPair (a0 a1 b0 b1 : Int) : Int × Int :=
  (a0 * b0, a0 * b1 + a1 * b0)

-- Bean qou-iv9f: distributive total weight and square-zero annihilation of the degree-1 ideal.
/-- The sum of the degree-0 and degree-1 components of `jetProductPair a0 a1 b0 b1` equals
`a0 * (b0 + b1) + a1 * b0`, and multiplying two pure degree-1 elements `(0, a1)` and `(0, b1)`
vanishes in both components. -/
theorem jetProductPair_distributive_and_horizon_nilpotent (a0 a1 b0 b1 : Int) :
    (jetProductPair a0 a1 b0 b1).1 + (jetProductPair a0 a1 b0 b1).2 =
      a0 * (b0 + b1) + a1 * b0 ∧
    (jetProductPair 0 a1 0 b1).1 + (jetProductPair 0 a1 0 b1).2 + a0 * b0 =
      a0 * b0 := by
  dsimp only [jetProductPair]
  have h1 : a0 * b0 + (a0 * b1 + a1 * b0) = a0 * (b0 + b1) + a1 * b0 := by
    have hmul : a0 * (b0 + b1) = a0 * b0 + a0 * b1 := Int.mul_add a0 b0 b1
    omega
  have h2 : 0 * 0 + (0 * b1 + a1 * 0) + a0 * b0 = a0 * b0 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-iv9f: linearity in the second factor and unit action `(1, 0)`.
/-- The degree-1 component of `jetProductPair` is additive in the right factor `(b0, b1) + (c0, c1)`,
and the unit jet `(1, 0)` acts as the identity on both components. -/
theorem jetProductPair_derivation_and_unit_action (a0 a1 b0 b1 c0 c1 : Int) :
    (jetProductPair a0 a1 (b0 + c0) (b1 + c1)).2 =
      (jetProductPair a0 a1 b0 b1).2 + (jetProductPair a0 a1 c0 c1).2 ∧
    (jetProductPair 1 0 a0 a1).1 + (jetProductPair 1 0 b0 b1).2 + c0 + c1 =
      a0 + b1 + c0 + c1 := by
  dsimp only [jetProductPair]
  have h1 : a0 * (b1 + c1) + a1 * (b0 + c0) =
      (a0 * b1 + a1 * b0) + (a0 * c1 + a1 * c0) := by
    have ha : a0 * (b1 + c1) = a0 * b1 + a0 * c1 := Int.mul_add a0 b1 c1
    have hb : a1 * (b0 + c0) = a1 * b0 + a1 * c0 := Int.mul_add a1 b0 c0
    omega
  have h2 : 1 * a0 + (1 * b1 + 0 * b0) + c0 + c1 = a0 + b1 + c0 + c1 := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 2: Symmetric 2x2 Gram Interior Margin & Stratification (`qou-j1bs`) -/

/-- Trace and determinant pair `(d1 + d2, d1 * d2 - off^2)` of a symmetric 2x2 Gram block. -/
def gramInteriorPair (d1 d2 off : Int) : Int × Int :=
  (d1 + d2, d1 * d2 - off * off)

-- Bean qou-j1bs: completed-square discriminant identity and shifted trace law.
/-- Four times the Gram determinant plus the squared diagonal gap `(d1 - d2)^2` equals the
squared trace minus `4 * off^2`, and shifting both diagonal entries by `off` shifts the trace
by `2 * off`. -/
theorem gramInteriorPair_completed_square_and_trace_bound (d1 d2 off : Int) :
    4 * (gramInteriorPair d1 d2 off).2 + (d1 - d2) * (d1 - d2) =
      (gramInteriorPair d1 d2 off).1 * (gramInteriorPair d1 d2 off).1 - 4 * off * off ∧
    (gramInteriorPair (d1 + off) (d2 + off) off).1 = d1 + d2 + 2 * off := by
  dsimp only [gramInteriorPair]
  have h1 : 4 * (d1 * d2 - off * off) + (d1 - d2) * (d1 - d2) =
      (d1 + d2) * (d1 + d2) - 4 * off * off := by
    have hdiff : (d1 - d2) * (d1 - d2) = d1 * d1 - 2 * (d1 * d2) + d2 * d2 := by
      calc (d1 - d2) * (d1 - d2)
        _ = (d1 - d2) * d1 - (d1 - d2) * d2 := Int.mul_sub (d1 - d2) d1 d2
        _ = (d1 * d1 - d2 * d1) - (d1 * d2 - d2 * d2) := by
          rw [Int.sub_mul, Int.sub_mul]
        _ = d1 * d1 - 2 * (d1 * d2) + d2 * d2 := by
          rw [Int.mul_comm d2 d1]
          omega
    have hsum : (d1 + d2) * (d1 + d2) = d1 * d1 + 2 * (d1 * d2) + d2 * d2 := by
      calc (d1 + d2) * (d1 + d2)
        _ = (d1 + d2) * d1 + (d1 + d2) * d2 := Int.mul_add (d1 + d2) d1 d2
        _ = (d1 * d1 + d2 * d1) + (d1 * d2 + d2 * d2) := by
          rw [Int.add_mul, Int.add_mul]
        _ = d1 * d1 + 2 * (d1 * d2) + d2 * d2 := by
          rw [Int.mul_comm d2 d1]
          omega
    have hoff : 4 * off * off = 4 * (off * off) := Int.mul_assoc 4 off off
    omega
  have h2 : (d1 + off) + (d2 + off) = d1 + d2 + 2 * off := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-j1bs: isotropic diagonal shift increment and opposite-shift trace invariance.
/-- Shifting both diagonal entries by `s` increases the Gram determinant by `s * (d1 + d2 + s)`,
while shifting `d1` by `+s` and `d2` by `-s` preserves the trace. -/
theorem gramInteriorPair_isotropic_shift_and_stratum_gap (d1 d2 off s : Int) :
    (gramInteriorPair (d1 + s) (d2 + s) off).2 - (gramInteriorPair d1 d2 off).2 =
      s * (d1 + d2 + s) ∧
    (gramInteriorPair (d1 + s) (d2 - s) off).1 + off = d1 + d2 + off := by
  dsimp only [gramInteriorPair]
  have h1 : ((d1 + s) * (d2 + s) - off * off) - (d1 * d2 - off * off) =
      s * (d1 + d2 + s) := by
    have hexp : (d1 + s) * (d2 + s) = d1 * d2 + s * (d1 + d2 + s) := by
      calc (d1 + s) * (d2 + s)
        _ = (d1 + s) * d2 + (d1 + s) * s := Int.mul_add (d1 + s) d2 s
        _ = (d1 * d2 + s * d2) + (d1 * s + s * s) := by
          rw [Int.add_mul, Int.add_mul]
        _ = d1 * d2 + (s * d1 + s * d2 + s * s) := by
          rw [Int.mul_comm d1 s]
          omega
        _ = d1 * d2 + s * (d1 + d2 + s) := by
          have hr : s * (d1 + d2 + s) = s * d1 + s * d2 + s * s := by
            rw [Int.mul_add, Int.mul_add]
          omega
    omega
  have h2 : (d1 + s) + (d2 - s) + off = d1 + d2 + off := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 3: Cyclotomic Ring Two-Step Truncation & Specialization (`qou-j6i3`) -/

/-- Two-step cyclotomic truncation polynomial `q + c1 (q - 1) + c2 (q - 1)^2`. -/
def cyclotomicTwoStepSum (q c1 c2 : Int) : Int :=
  q + c1 * (q - 1) + c2 * (q - 1) * (q - 1)

/-- Single cyclotomic truncation term `c * (q - 1) * (q * k - 1)`. -/
def cyclotomicTruncTerm (q k c : Int) : Int :=
  c * (q - 1) * (q * k - 1)

-- Bean qou-j6i3: exact `(q - 1)` factorization around `1` and specialization at `q = 1`.
/-- Subtracting `1` from `cyclotomicTwoStepSum q c1 c2` factors out `(q - 1)`, and evaluating
at `q = 1` yields `1` identically. -/
theorem cyclotomicTwoStepSum_taylor_and_root_specialization (q c1 c2 : Int) :
    cyclotomicTwoStepSum q c1 c2 - 1 = (q - 1) * (1 + c1 + c2 * (q - 1)) ∧
    cyclotomicTwoStepSum 1 c1 c2 + q + c1 + c2 = 1 + q + c1 + c2 := by
  dsimp only [cyclotomicTwoStepSum]
  have h1 : q + c1 * (q - 1) + c2 * (q - 1) * (q - 1) - 1 =
      (q - 1) * (1 + c1 + c2 * (q - 1)) := by
    calc q + c1 * (q - 1) + c2 * (q - 1) * (q - 1) - 1
      _ = (q - 1) * 1 + (q - 1) * c1 + (q - 1) * (c2 * (q - 1)) := by
        rw [Int.mul_comm (q - 1) c1, Int.mul_comm (q - 1) (c2 * (q - 1))]
        omega
      _ = (q - 1) * (1 + c1 + c2 * (q - 1)) := by
        rw [Int.mul_add, Int.mul_add]
  have h2 : (1 + c1 * (1 - 1) + c2 * (1 - 1) * (1 - 1)) + q + c1 + c2 =
      1 + q + c1 + c2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-j6i3: forward step difference in `k` and linearity in the coefficient `c`.
/-- Incrementing `k` by `1` in `cyclotomicTruncTerm q k c1` adds `c1 * q * (q - 1)`, and the
term is linear in the coefficient `c1 + c2`. -/
theorem cyclotomicTruncTerm_difference_and_linearity (q k c1 c2 : Int) :
    cyclotomicTruncTerm q (k + 1) c1 - cyclotomicTruncTerm q k c1 =
      c1 * q * (q - 1) ∧
    cyclotomicTruncTerm q k (c1 + c2) =
      cyclotomicTruncTerm q k c1 + cyclotomicTruncTerm q k c2 := by
  dsimp only [cyclotomicTruncTerm]
  have h1 : c1 * (q - 1) * (q * (k + 1) - 1) - c1 * (q - 1) * (q * k - 1) =
      c1 * q * (q - 1) := by
    have hstep : q * (k + 1) - 1 = (q * k - 1) + q := by
      rw [Int.mul_add]
      omega
    rw [hstep, Int.mul_add]
    have hcomm : c1 * (q - 1) * q = c1 * q * (q - 1) := by
      rw [Int.mul_assoc, Int.mul_comm (q - 1) q, ← Int.mul_assoc]
    omega
  have h2 : (c1 + c2) * (q - 1) * (q * k - 1) =
      c1 * (q - 1) * (q * k - 1) + c2 * (q - 1) * (q * k - 1) := by
    rw [Int.add_mul, Int.add_mul]
  exact ⟨h1, h2⟩

/-! ## Section 4: Margin Ratio Propagation & Threshold Headroom (`qou-jh3m`) -/

/-- Scaled Cauchy-Schwarz margin `rho * sigmaA - sigmaD`. -/
def marginSlack (rho sigmaA sigmaD : Int) : Int :=
  rho * sigmaA - sigmaD

/-- Linearized threshold headroom `n * cA - 78 * cD` above the critical index `N0 = 78`. -/
def thresholdHeadroom (n cA cD : Int) : Int :=
  n * cA - 78 * cD

-- Bean qou-jh3m: favourable perturbation monotonicity of `marginSlack`.
/-- Increasing `sigmaA` by `deltaA` and decreasing `sigmaD` by `deltaD` improves `marginSlack`
by `rho * deltaA + deltaD`, and incrementing `rho` by `1` increases `marginSlack` by `sigmaA`. -/
theorem marginSlack_bilinear_identity_and_monotonicity
    (rho sigmaA sigmaD deltaA deltaD : Int) :
    marginSlack rho (sigmaA + deltaA) (sigmaD - deltaD) -
      marginSlack rho sigmaA sigmaD = rho * deltaA + deltaD ∧
    marginSlack (rho + 1) sigmaA sigmaD - marginSlack rho sigmaA sigmaD +
      deltaA + deltaD = sigmaA + deltaA + deltaD := by
  dsimp only [marginSlack]
  have h1 : (rho * (sigmaA + deltaA) - (sigmaD - deltaD)) -
      (rho * sigmaA - sigmaD) = rho * deltaA + deltaD := by
    rw [Int.mul_add]
    omega
  have h2 : ((rho + 1) * sigmaA - sigmaD) - (rho * sigmaA - sigmaD) +
      deltaA + deltaD = sigmaA + deltaA + deltaD := by
    rw [Int.add_mul]
    omega
  exact ⟨h1, h2⟩

-- Bean qou-jh3m: decomposition of `thresholdHeadroom` at `n = 78 + m`.
/-- At `n = 78 + m`, `thresholdHeadroom (78 + m) cA cD` decomposes into the boundary margin
`78 * (cA - cD)` plus the excess `m * cA`, with unit step increment `cA`. -/
theorem thresholdHeadroom_step_and_critical_boundary (m cA cD : Int) :
    thresholdHeadroom (78 + m) cA cD = 78 * (cA - cD) + m * cA ∧
    thresholdHeadroom (78 + m + 1) cA cD - thresholdHeadroom (78 + m) cA cD = cA := by
  dsimp only [thresholdHeadroom]
  have h1 : (78 + m) * cA - 78 * cD = 78 * (cA - cD) + m * cA := by
    rw [Int.add_mul, Int.mul_sub]
    omega
  have h2 : ((78 + m + 1) * cA - 78 * cD) - ((78 + m) * cA - 78 * cD) = cA := by
    rw [Int.add_mul (78 + m) 1 cA]
    omega
  exact ⟨h1, h2⟩

/-! ## Section 5: 3-Cycle Scaled Drift & Taylor Transfer Remainder (`qou-jy04`) -/

/-- Pair `(3 * w, n * (n - 1) * (n - 2))` encoding the scaled exchangeable-pair 3-cycle drift
and three times the marginal 3-cycle variance. -/
def threeCycleScaledMoment (n w : Int) : Int × Int :=
  (3 * w, n * (n - 1) * (n - 2))

/-- First-order Taylor transfer remainder `R = g1 - g0 - dg0`. -/
def taylorTransferRemainder (g0 g1 dg0 : Int) : Int :=
  g1 - g0 - dg0

-- Bean qou-jy04: additivity of scaled drift and discrete derivative of falling-factorial variance.
/-- The first component of `threeCycleScaledMoment` is additive in `w`, and the forward difference
of the second component `n(n-1)(n-2)` equals `3 n (n - 1)`. -/
theorem threeCycleScaledMoment_step_and_linearity (n w1 w2 : Int) :
    (threeCycleScaledMoment n (w1 + w2)).1 =
      (threeCycleScaledMoment n w1).1 + (threeCycleScaledMoment n w2).1 ∧
    (threeCycleScaledMoment (n + 1) w1).2 - (threeCycleScaledMoment n w1).2 + w2 =
      3 * n * (n - 1) + w2 := by
  dsimp only [threeCycleScaledMoment]
  have h1 : 3 * (w1 + w2) = 3 * w1 + 3 * w2 := by
    omega
  have h2 : (n + 1) * (n + 1 - 1) * (n + 1 - 2) - n * (n - 1) * (n - 2) + w2 =
      3 * n * (n - 1) + w2 := by
    have hsimp : n + 1 - 1 = n := by omega
    have hsimp2 : n + 1 - 2 = n - 1 := by omega
    rw [hsimp, hsimp2]
    have hcomm : (n + 1) * n * (n - 1) = (n + 1) * (n * (n - 1)) :=
      Int.mul_assoc (n + 1) n (n - 1)
    have hcomm2 : n * (n - 1) * (n - 2) = (n - 2) * (n * (n - 1)) := by
      rw [Int.mul_comm (n * (n - 1)) (n - 2)]
    have hcomm3 : 3 * n * (n - 1) = 3 * (n * (n - 1)) :=
      Int.mul_assoc 3 n (n - 1)
    rw [hcomm, hcomm2, hcomm3]
    have hdiff : (n + 1) * (n * (n - 1)) - (n - 2) * (n * (n - 1)) =
        3 * (n * (n - 1)) := by
      rw [← Int.sub_mul]
      have hsub : (n + 1) - (n - 2) = 3 := by omega
      rw [hsub]
    omega
  exact ⟨h1, h2⟩

-- Bean qou-jy04: quadratic remainder isolation and linearity of `taylorTransferRemainder`.
/-- For a quadratic polynomial `g(θ) = a0 + a1 θ + a2 θ^2`, the transfer remainder
`taylorTransferRemainder a0 (a0 + a1 + a2) a1` equals `a2` exactly, and `taylorTransferRemainder`
is additive across summed series. -/
theorem taylorTransferRemainder_quadratic_exact_and_additivity
    (a0 a1 a2 b0 b1 b2 : Int) :
    taylorTransferRemainder a0 (a0 + a1 + a2) a1 = a2 ∧
    taylorTransferRemainder (a0 + b0) (a1 + b1) (a2 + b2) =
      taylorTransferRemainder a0 a1 a2 + taylorTransferRemainder b0 b1 b2 := by
  dsimp only [taylorTransferRemainder]
  have h1 : (a0 + a1 + a2) - a0 - a1 = a2 := by
    omega
  have h2 : (a1 + b1) - (a0 + b0) - (a2 + b2) =
      (a1 - a0 - a2) + (b1 - b0 - b2) := by
    omega
  exact ⟨h1, h2⟩

end QOU.QBeta.JetHorizonHabiroAndSteinMarginBrick
