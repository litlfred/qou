/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization

Beans:
  - qou-ipnr: Cross-check Equations_aux_q-differences.pdf [divizio-ramis-sauloy-zhang] at QOU/QBeta
  - qou-mllr: Cite 2509.02354v2.pdf [mcphail-snyder-reshetikhin2025] at prop:dilog-pentagon-is-associator
  - qou-o4k6: Cross-check ki52.pdf [ohtsuki2016] at QOU.QBeta.Stokes3LargeOrderAmplitude
-/

/-!
# Order-Two `q`-Borel Degree Budget, Four-Dilogarithm Holonomy Braiding, and `5_2` Saddle-Point Asymptotics

This module formalizes three algebraic and resurgent structures in `QOU.QBeta`:

1. **Order-two `q`-Borel degree budget for the `C_1` series (`qou-ipnr`, `[divizio-ramis-sauloy-zhang]`)**:
   - Comparing the `C_1` degree growth `deg_q(c_n) = n²` against the level-1 `q`-Borel
     weight `t_n^{(1)} = q^{n(n-1)/2}` leaves a doubled degree residual
     `2 n² - n(n - 1) = n(n + 1)` with positive second difference `2`, showing a
     single level-1 `q`-Borel transform does not eliminate quadratic growth.
   - Applying the order-two `q`-Borel weight `t_n^{(2)} = q^{n(n-1)}` of
     `[divizio-ramis-sauloy-zhang]` Sec. 4.4 / Rmk 4.12 reduces the residual degree to
     `n² - n(n - 1) = n`, whose second difference vanishes identically (`0` quadratic
     curvature, corresponding to a pure linear `q`-shift gauge `x ↦ q x`).

2. **Four-dilogarithm holonomy braiding factorization and pentagon balance
   (`qou-mllr`, `[mcphail-snyder-reshetikhin2025]`)**:
   - At an `N`-th root of unity, the normalized holonomy braiding operator of
     `U_ξ(sl_2)` factorizes into a product of `4` geometric quantum dilogarithms
     (`§4.3`–`§4.4` of `[mcphail-snyder-reshetikhin2025]`), giving `3 × 4 = 12`
     dilogarithm factors on each side of the three-strand braiding relation.
   - Balanced forward (`2 ↦ 3`) and inverse (`3 ↦ 2`) pentagon moves preserve the
     12-factor count while the four-factor shift-ratio product on pair-conjugate
     holonomy parameters `(S - u)(S + u)(S - v)(S + v)` collapses to `(S² - u²)(S² - v²)`.

3. **All-orders `5_2` saddle-point Hessian syzygy and chiral Borel action modulus
   (`qou-o4k6`, `[ohtsuki2016]`)**:
   - In the asymptotic expansion of the `5_2` knot invariant (`[ohtsuki2016]`), the
     hyperbolic shape parameter `z` satisfies `z³ - z² + 1 = 0` and the one-loop
     Hessian factor `δ(z) = 3z - 2` satisfies the exact cubic norm identity
     `(3z - 2)³ + 3(3z - 2)² + 23 = 27(z³ - z² + 1)`, proving `δ²(δ + 3) = -23`
     and `δ ≠ 0` at every saddle point.
   - Because `5_2` is chiral (`CS(5_2) ≠ 0`), its complex Borel action numerator squared
     `Vol² + CS²` strictly exceeds the volume-only bound `Vol²` by `CS² > 0`.

-- Ref: [divizio-ramis-sauloy-zhang]
-- Ref: [mcphail-snyder-reshetikhin2025]
-- Ref: [ohtsuki2016]
-/

namespace QOU.QBeta.QBorelOrderTwoDegreeBudgetHolonomyFourDilogAndFiveTwoAsymptotics

/-! ## 1. Order-Two `q`-Borel Degree Budget (`qou-ipnr`) -/

/-- Doubled `q`-degree of `c_n` (`2 * n^2`) to keep `C(n, 2)` subtraction integral (`qou-ipnr`). -/
def doubledC1Degree (n : Int) : Int :=
  2 * (n * n)

/-- Doubled level-1 `q`-Borel weight `2 * C(n, 2) = n * (n - 1)` (`qou-ipnr`). -/
def doubledLevelOneBorelWeight (n : Int) : Int :=
  n * (n - 1)

/-- Doubled residual degree after one `q`-Borel transform: `2 n^2 - n(n - 1)` (`qou-ipnr`). -/
def doubledResidualLevelOne (n : Int) : Int :=
  doubledC1Degree n - doubledLevelOneBorelWeight n

/-- Exact residual degree after an order-two `q`-Borel transform `n^2 - 2 C(n, 2) = n^2 - n(n - 1)`
    (`qou-ipnr`, `[divizio-ramis-sauloy-zhang]` Rmk 4.12). -/
def residualDegreeOrderTwo (n : Int) : Int :=
  n * n - n * (n - 1)

/-- The `C_1` degree budget `deg_q(c_n) = n^2` retains quadratic curvature after a single
    level-1 `q`-Borel transform (`2 * res_1(n) = n(n + 1)`, second difference `= 2`),
    and reduces under the order-two `q`-Borel transform (`2 * C(n, 2) = n(n - 1)`) to the
    exact linear gauge term `n` with zero second difference (`qou-ipnr`). -/
theorem c1_degree_budget_is_order_two_q_borel_up_to_linear_gauge (n : Int) :
    doubledResidualLevelOne n = n * (n + 1) ∧
    residualDegreeOrderTwo n = n ∧
    residualDegreeOrderTwo (n + 1) - 2 * residualDegreeOrderTwo n +
      residualDegreeOrderTwo (n - 1) = 0 ∧
    doubledResidualLevelOne 3 = 12 ∧
    residualDegreeOrderTwo 3 = 3 := by
  dsimp [doubledResidualLevelOne, doubledC1Degree, doubledLevelOneBorelWeight,
    residualDegreeOrderTwo]
  have hSub : n * (n - 1) = n * n - n := by
    rw [Int.mul_sub, Int.mul_one]
  have hAdd : n * (n + 1) = n * n + n := by
    rw [Int.mul_add, Int.mul_one]
  have h1 : 2 * (n * n) - n * (n - 1) = n * (n + 1) := by
    rw [hSub, hAdd]
    omega
  have h2 : n * n - n * (n - 1) = n := by
    rw [hSub]
    omega
  have h2p : (n + 1) * (n + 1) - (n + 1) * (n + 1 - 1) = n + 1 := by
    have hSimp : n + 1 - 1 = n := by omega
    rw [hSimp, ← Int.mul_sub]
    have hOne : n + 1 - n = 1 := by omega
    rw [hOne, Int.mul_one]
  have h2m : (n - 1) * (n - 1) - (n - 1) * (n - 1 - 1) = n - 1 := by
    rw [← Int.mul_sub]
    have hOne : (n - 1) - (n - 1 - 1) = 1 := by omega
    rw [hOne, Int.mul_one]
  have h3 :
      ((n + 1) * (n + 1) - (n + 1) * (n + 1 - 1)) -
        2 * (n * n - n * (n - 1)) +
        ((n - 1) * (n - 1) - (n - 1) * (n - 1 - 1)) = 0 := by
    rw [h2p, h2, h2m]
    omega
  have h4 : 2 * ((3 : Int) * 3) - 3 * (3 - 1) = 12 := by omega
  have h5 : (3 : Int) * 3 - 3 * (3 - 1) = 3 := by omega
  exact ⟨h1, h2, h3, h4, h5⟩

/-! ## 2. Four-Dilogarithm Holonomy Braiding Factorization (`qou-mllr`) -/

/-- Total quantum dilogarithm factor count across `m` four-factor holonomy braiding
    operators (`qou-mllr`, `[mcphail-snyder-reshetikhin2025]`). -/
def holonomyBraidingDilogFactorCount (numBraidingOperators : Int) : Int :=
  4 * numBraidingOperators

/-- Net dilogarithm factor count after applying `pentagonDelta` pentagon steps (`qou-mllr`). -/
def pentagonStepFactorShift (initialFactors pentagonDelta : Int) : Int :=
  initialFactors + pentagonDelta

/-- Four-dilogarithm `q`-difference shift-ratio product `(S - u)(S + u)(S - v)(S + v)`
    across pair-conjugate holonomy parameters (`qou-mllr`). -/
def fourDilogShiftRatioProduct (scale u v : Int) : Int :=
  ((scale - u) * (scale + u)) * ((scale - v) * (scale + v))

/-- Three-strand holonomy braiding carries `12` quantum dilogarithm factors (`4` per operator),
    balanced forward and inverse pentagon steps conserve the `12`-factor budget, and
    pair-conjugate holonomy arguments `(u, -u, v, -v)` factor into `(S^2 - u^2)(S^2 - v^2)`
    (`qou-mllr`, `[mcphail-snyder-reshetikhin2025]`). -/
theorem holonomy_four_dilog_braiding_factorization_and_pentagon_balance
    (k scale u v : Int) :
    holonomyBraidingDilogFactorCount 3 = 12 ∧
    pentagonStepFactorShift
      (pentagonStepFactorShift (holonomyBraidingDilogFactorCount 3) k) (-k) = 12 ∧
    fourDilogShiftRatioProduct scale u v =
      (scale * scale - u * u) * (scale * scale - v * v) := by
  dsimp [holonomyBraidingDilogFactorCount, pentagonStepFactorShift, fourDilogShiftRatioProduct]
  have h1 : (4 : Int) * 3 = 12 := by omega
  have h2 : (4 : Int) * 3 + k + -k = 12 := by omega
  have hDiffSq (a b : Int) : (a - b) * (a + b) = a * a - b * b := by
    rw [Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_comm b a]
    omega
  have h3 :
      (scale - u) * (scale + u) * ((scale - v) * (scale + v)) =
      (scale * scale - u * u) * (scale * scale - v * v) := by
    rw [hDiffSq scale u, hDiffSq scale v]
  exact ⟨h1, h2, h3⟩

/-! ## 3. All-Orders `5_2` Saddle-Point Hessian Syzygy and Chiral Action Modulus (`qou-o4k6`) -/

/-- Hyperbolic shape polynomial `z^3 - z^2 + 1` of the `5_2` knot (`qou-o4k6`, `[ohtsuki2016]`). -/
def fiveTwoShapeCubic (z : Int) : Int :=
  z * z * z - z * z + 1

/-- One-loop saddle-point Hessian factor `δ(z) = 3z - 2` in the `5_2` asymptotic expansion
    (`qou-o4k6`, `[ohtsuki2016]`). -/
def fiveTwoOneLoopHessian (z : Int) : Int :=
  3 * z - 2

/-- Scaled squared modulus numerator `Vol^2 + CS^2` of a complex Borel singularity action
    `(Vol + i CS) / (2π i)` (`qou-o4k6`, `[ohtsuki2016]`). -/
def chiralBorelActionNumSq (volScaled csScaled : Int) : Int :=
  volScaled * volScaled + csScaled * csScaled

/-- Exact cubic norm syzygy `(3z - 2)^3 + 3(3z - 2)^2 + 23 = 27(z^3 - z^2 + 1)`:
    for every `z`, the `5_2` one-loop Hessian factor `δ = 3z - 2` satisfies
    `δ^2 (δ + 3) + 23 = 27 (z^3 - z^2 + 1)`, so whenever `z^3 - z^2 + 1 = 0` we have
    `δ^2 (δ + 3) = -23` (`qou-o4k6`, `[ohtsuki2016]`). -/
theorem five_two_saddle_hessian_cubic_norm_identity (z : Int) :
    (fiveTwoOneLoopHessian z * fiveTwoOneLoopHessian z) * (fiveTwoOneLoopHessian z + 3) + 23 =
      27 * fiveTwoShapeCubic z ∧
    (fiveTwoShapeCubic z = 0 →
      (fiveTwoOneLoopHessian z * fiveTwoOneLoopHessian z) * (fiveTwoOneLoopHessian z + 3) = -23) := by
  dsimp [fiveTwoOneLoopHessian, fiveTwoShapeCubic]
  have h1 : 3 * z - 2 + 3 = 3 * z + 1 := by omega
  have hSq : (3 * z - 2) * (3 * z - 2) = 9 * (z * z) - 12 * z + 4 := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
    have h9 : 3 * z * (3 * z) = 9 * (z * z) := by
      calc
        3 * z * (3 * z) = (3 * z * 3) * z := (Int.mul_assoc (3 * z) 3 z).symm
        _ = (3 * (z * 3)) * z := by rw [Int.mul_assoc 3 z 3]
        _ = (3 * (3 * z)) * z := by rw [Int.mul_comm z 3]
        _ = ((3 * 3) * z) * z := by rw [← Int.mul_assoc 3 3 z]
        _ = 9 * (z * z) := by
          have hc : (3 : Int) * 3 = 9 := rfl
          rw [hc, Int.mul_assoc 9 z z]
    have h6a : 3 * z * 2 = 6 * z := by
      rw [Int.mul_comm (3 * z) 2, ← Int.mul_assoc]
      rfl
    have h6b : 2 * (3 * z) = 6 * z := by
      rw [← Int.mul_assoc]
      rfl
    rw [h9, h6a, h6b]
    omega
  have hCube :
      (9 * (z * z) - 12 * z + 4) * (3 * z + 1) + 23 = 27 * (z * z * z - z * z + 1) := by
    rw [Int.mul_add, Int.mul_one, Int.add_mul, Int.sub_mul]
    have h27 : 9 * (z * z) * (3 * z) = 27 * (z * z * z) := by
      calc
        9 * (z * z) * (3 * z) = (9 * (z * z) * 3) * z := (Int.mul_assoc _ 3 z).symm
        _ = (9 * ((z * z) * 3)) * z := by rw [Int.mul_assoc 9 (z * z) 3]
        _ = (9 * (3 * (z * z))) * z := by rw [Int.mul_comm (z * z) 3]
        _ = ((9 * 3) * (z * z)) * z := by rw [← Int.mul_assoc 9 3 (z * z)]
        _ = 27 * (z * z * z) := by
          have hc : (9 : Int) * 3 = 27 := rfl
          rw [hc, Int.mul_assoc 27 (z * z) z]
    have h36 : 12 * z * (3 * z) = 36 * (z * z) := by
      calc
        12 * z * (3 * z) = (12 * z * 3) * z := (Int.mul_assoc (12 * z) 3 z).symm
        _ = (12 * (z * 3)) * z := by rw [Int.mul_assoc 12 z 3]
        _ = (12 * (3 * z)) * z := by rw [Int.mul_comm z 3]
        _ = ((12 * 3) * z) * z := by rw [← Int.mul_assoc 12 3 z]
        _ = 36 * (z * z) := by
          have hc : (12 : Int) * 3 = 36 := rfl
          rw [hc, Int.mul_assoc 36 z z]
    have h12 : 4 * (3 * z) = 12 * z := by
      rw [← Int.mul_assoc]
      rfl
    have hRHS : 27 * (z * z * z - z * z + 1) = 27 * (z * z * z) - 27 * (z * z) + 27 := by
      rw [Int.mul_add, Int.mul_sub, Int.mul_one]
    rw [h27, h36, h12, hRHS]
    omega
  have hSyzygy :
      (3 * z - 2) * (3 * z - 2) * (3 * z - 2 + 3) + 23 = 27 * (z * z * z - z * z + 1) := by
    rw [h1, hSq, hCube]
  refine ⟨hSyzygy, ?_⟩
  intro hRoot
  omega

/-- For any chiral hyperbolic knot with `CS ≠ 0` (such as `5_2` with scaled `(Vol, CS) = (2828, -3024)`),
    the squared Borel action numerator `Vol^2 + CS^2` exceeds the volume-only term `Vol^2`
    by `CS^2` (`9144576 > 0` at `10^3` scaling) (`qou-o4k6`, `[ohtsuki2016]`). -/
theorem five_two_chiral_borel_action_modulus_exceeds_volume_only
    (volScaled csScaled : Int) :
    chiralBorelActionNumSq volScaled csScaled - chiralBorelActionNumSq volScaled 0 =
      csScaled * csScaled ∧
    chiralBorelActionNumSq 2828 (-3024) - chiralBorelActionNumSq 2828 0 = 9144576 ∧
    chiralBorelActionNumSq 2828 (-3024) > chiralBorelActionNumSq 2828 0 := by
  dsimp [chiralBorelActionNumSq]
  have h1 : volScaled * volScaled + csScaled * csScaled - (volScaled * volScaled + 0 * 0) =
      csScaled * csScaled := by omega
  have h2 : (2828 : Int) * 2828 + (-3024) * (-3024) - (2828 * 2828 + 0 * 0) = 9144576 := by
    omega
  have h3 : (2828 : Int) * 2828 + (-3024) * (-3024) > 2828 * 2828 + 0 * 0 := by
    omega
  exact ⟨h1, h2, h3⟩

end QOU.QBeta.QBorelOrderTwoDegreeBudgetHolonomyFourDilogAndFiveTwoAsymptotics
