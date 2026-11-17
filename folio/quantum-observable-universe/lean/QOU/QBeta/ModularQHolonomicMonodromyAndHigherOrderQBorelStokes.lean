/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  - qou-godb: Cross-check 2203.17029v1.pdf [garoufalidis-wheeler-modular] at qlift_routeB_connection_matrix_probe.py
  - qou-hnuw: Cite 1404.2541v1.pdf [morita2014] at QOU/MathlibExt/QBorelKernelLevel
-/

namespace QOU.QBeta

/-!
# Section 1: Modular `q`-Holonomic Monodromy and Jacobi-Theta Connection Growth (`qou-godb`)

Ref: [garoufalidis-wheeler-modular] S. Garoufalidis and C. Wheeler, "Modular q-holonomic modules",
arXiv:2203.17029v1 (2022), Theorem 1.6(a) and Theorem 1.7(a) (§1.5):
For the `q`-holonomic modules attached to knots and cusped 3-manifolds, the connection/monodromy
matrix `M(t, λ, μ, q) = V^{-1} U` is lower-triangular unipotent (Theorem 1.6(a)) or signed
diagonal `diag(-1, 1)` (Theorem 1.7(a)) with a single non-trivial off-diagonal entry `M_{2,1}`
given by an explicit ratio of Jacobi theta functions whose `q`-series coefficients grow with
quadratic exponent `m^2 / 4`.
-/

/-- Determinant `1 * 1 - 0 * m21` of the lower-triangular unipotent monodromy matrix
`M = [[1, 0], [m21, 1]]` from Theorem 1.6(a) (`qou-godb`).
Ref: [garoufalidis-wheeler-modular] Theorem 1.6(a). -/
def unipotentMonodromyDet (m21 : Int) : Int :=
  1 * 1 - 0 * m21

/-- Off-diagonal `(2, 1)` entry `(-1) * m21 + 1 * m21` of the square `M^2` of the signed
monodromy matrix `M = [[-1, 0], [m21, 1]]` from Theorem 1.7(a) (`qou-godb`).
Ref: [garoufalidis-wheeler-modular] Theorem 1.7(a). -/
def signedMonodromySquareOffDiag (m21 : Int) : Int :=
  (-1) * m21 + 1 * m21

/-- Scaled (`× 4`) quadratic theta-growth exponent `4 * (m^2 / 4) = m^2` of the Jacobi-theta
connection entry `M_{2,1}` (`qou-godb`).
Ref: [garoufalidis-wheeler-modular] §1.5, Theorems 1.6(a) & 1.7(a). -/
def thetaConnectionExponent4x (m : Int) : Int :=
  m * m

/-- For every Jacobi-theta ratio entry `m21`:
1. the unipotent monodromy matrix has unit determinant (`unipotentMonodromyDet m21 = 1`),
2. the signed monodromy matrix `M = [[-1, 0], [m21, 1]]` is strictly involutive (`M^2 = I_2`,
   with off-diagonal entry `signedMonodromySquareOffDiag m21 = 0`), and
3. the scaled quadratic theta exponent `m^2` has constant second difference
   `(m + 1)^2 - 2 m^2 + (m - 1)^2 = 2` (`qou-godb`).
Ref: [garoufalidis-wheeler-modular] Theorems 1.6(a) & 1.7(a). -/
theorem modularQHolonomicMonodromy_invariants (m21 m : Int) :
    unipotentMonodromyDet m21 = 1 ∧
    signedMonodromySquareOffDiag m21 = 0 ∧
    thetaConnectionExponent4x (m + 1) - 2 * thetaConnectionExponent4x m +
      thetaConnectionExponent4x (m - 1) = 2 := by
  dsimp [unipotentMonodromyDet, signedMonodromySquareOffDiag, thetaConnectionExponent4x]
  have h1 : (m + 1) * (m + 1) = m * m + 2 * m + 1 := by
    calc
      (m + 1) * (m + 1) = (m + 1) * m + (m + 1) * 1 := by rw [Int.mul_add]
      _ = m * m + 1 * m + (m * 1 + 1 * 1) := by rw [Int.add_mul, Int.add_mul]
      _ = m * m + 2 * m + 1 := by omega
  have h2 : (m - 1) * (m - 1) = m * m - 2 * m + 1 := by
    calc
      (m - 1) * (m - 1) = (m - 1) * m - (m - 1) * 1 := by rw [Int.mul_sub]
      _ = m * m - 1 * m - (m * 1 - 1 * 1) := by rw [Int.sub_mul, Int.sub_mul]
      _ = m * m - 2 * m + 1 := by omega
  rw [h1, h2]
  omega

/-!
# Section 2: Higher-Order `q`-Borel Kernel Slope and Stokes Multiplier (`qou-hnuw`)

Ref: [morita2014] T. Morita, "The Stokes phenomenon for the Ramanujan's q-difference equation and
its higher order extension", arXiv:1404.2541v1 (2014):
For the `k`-th order extension of the single-slope `q`-difference equation, the `m`-th series
coefficient carries quadratic `q`-exponent `k * m(m - 1) / 2`, requiring `k` successive `q`-Borel
transforms of level `1` (or a single level-`k` `q`-Borel kernel `θ_{q^k}`) to regularize the
divergent formal solution and compute the Stokes connection formula.
-/

/-- Scaled (`× 2`) quadratic `q`-Borel exponent `k * m * (m - 1)` for the `m`-th coefficient of
the `k`-th order extension (`qou-hnuw`).
Ref: [morita2014] §2 & §3. -/
def higherOrderQBorelExponent2x (kOrder m : Int) : Int :=
  kOrder * (m * (m - 1))

/-- Applying `r` successive unit-level `q`-Borel transforms subtracts `r * m * (m - 1)` from the
scaled quadratic exponent (`qou-hnuw`).
Ref: [morita2014] §3. -/
def qBorelRegularizedExponent2x (kOrder rTransforms m : Int) : Int :=
  higherOrderQBorelExponent2x kOrder m - higherOrderQBorelExponent2x rTransforms m

/-- First-difference slope `higherOrderQBorelExponent2x k (m + 1) - higherOrderQBorelExponent2x k m = 2 k m`,
and exact regularization (`= 0`) when the number of unit-level `q`-Borel transforms matches the
order `r = k` (`qou-hnuw`).
Ref: [morita2014] §§2-3. -/
theorem higherOrderQBorel_slope_and_regularization (kOrder m : Int) :
    higherOrderQBorelExponent2x kOrder (m + 1) -
      higherOrderQBorelExponent2x kOrder m = 2 * kOrder * m ∧
    qBorelRegularizedExponent2x kOrder kOrder m = 0 := by
  dsimp [higherOrderQBorelExponent2x, qBorelRegularizedExponent2x]
  have hstep : (m + 1) * (m + 1 - 1) - m * (m - 1) = 2 * m := by
    have h1 : m + 1 - 1 = m := by omega
    have h2 : (m + 1) * m = m * m + m := by
      rw [Int.add_mul, Int.one_mul]
    have h3 : m * (m - 1) = m * m - m := by
      rw [Int.mul_sub, Int.mul_one]
    rw [h1, h2, h3]
    omega
  have hmul :
      kOrder * ((m + 1) * (m + 1 - 1)) - kOrder * (m * (m - 1)) =
        kOrder * ((m + 1) * (m + 1 - 1) - m * (m - 1)) :=
    (Int.mul_sub kOrder ((m + 1) * (m + 1 - 1)) (m * (m - 1))).symm
  have hcomm : kOrder * (2 * m) = 2 * kOrder * m := by
    have hc1 : kOrder * (2 * m) = (kOrder * 2) * m := (Int.mul_assoc kOrder 2 m).symm
    have hc2 : kOrder * 2 = 2 * kOrder := Int.mul_comm kOrder 2
    rw [hc1, hc2]
  rw [hmul, hstep, hcomm]
  omega

end QOU.QBeta
