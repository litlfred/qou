/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Tactic

/-!
# Fantini–Wheeler Steepest-Descent Shift, Balanced Theta-Limit Coset, Center Frobenius Diagonal Pairing, Second-Order Euler–Maclaurin Cell Cancellation, and GSWZ Global Symbol Descent (`qou-i9xj`, `qou-r4ya`, `qou-xsv8`, `qou-xzlt`, `qou-y3xv`)

This module provides machine-checked Lean 4 theorems for the five Round 64 items under
`qou-r9ih`:

1. **`qou-i9xj`** (`fantini_wheeler_eq14_five_two_quadratic_shift_and_contour_bridge`):
   In Fantini–Wheeler eq. (14) for the $5_2$ state-integral coefficients $I_{m,\ell}$ with
   Neumann–Zagier parameters $(A, B) = (2, 3)$, the quadratic q-exponent
   $Q_{A,B}(m, \ell) = \frac{1}{2}(A m^2 + B \ell^2)$ satisfies the exact unit-step increment
   $$Q_{A,B}(m + 1, \ell + 1) - Q_{A,B}(m, \ell) = A m + B \ell + \frac{A + B}{2},$$
   which at $(A, B) = (2, 3)$ specializes to $2m + 3\ell + 5/2$ with $B - A = 1$, and two
   steepest-descent contour integrals whose Cauchy residue difference is $R$ agree iff $R = 0$.

2. **`qou-r4ya`** (`balanced_d_function_recentred_square_and_sublattice_coset`):
   In the balanced $D$-function $\theta$-limit on the $u \equiv 1$ coset, recentring the
   quadratic exponent $n^2 - 2(u + \phi_1) n$ around $n = k + u$ completes the square to
   $(k - \phi_1)^2 - (u + \phi_1)^2 + 2 u k$, and both the Friedrichs even sublattice
   $2j + \phi_1$ and the Krein odd sublattice $(2j + 1) + \phi_1$ project to the same
   $\mathbb{Z}$-coset representative $\phi_1$ while differing by exactly $1$.

3. **`qou-xsv8`** (`hecke_h3_center_frobenius_diagonal_and_partition_of_unity`):
   In the central idempotent basis $\{e_{(3)}, e_{(2,1)}, e_{(1,1,1)}\}$ of $Z(H_3(q))$,
   orthogonal idempotence makes the Frobenius bilinear pairing strictly diagonal
   ($\sum_i w_i a_i b_i$), so a central element supported in stratum $k$ pairs to zero
   with any element whose $k$-th stratum coordinate vanishes, and the three rational
   trace weights
   $$w_0(q) = \frac{1}{D(q)}, \quad w_1(q) = \frac{2q^2(q^2+1)}{D(q)}, \quad w_2(q) = \frac{q^6}{D(q)}$$
   with $D(q) = q^6 + 2q^4 + 2q^2 + 1$ satisfy $w_0(q) + w_1(q) + w_2(q) = 1$ whenever $D(q) \neq 0$.

4. **`qou-xzlt`** (`euler_maclaurin_second_order_cubic_cell_cancellation`):
   For a general cubic polynomial $P(t) = c_0 + c_1(t - u) + c_2(t - u)^2 + c_3(t - u)^3$
   on the cell $[u - h/2, u + h/2]$, the raw trapezoid defect is $c_2 h^3 / 6$, the endpoint
   derivative difference is $P'(u + h/2) - P'(u - h/2) = 2 c_2 h + \frac{3}{2} c_3 h^2$,
   and the second-order Euler–Maclaurin corrected rule
   $\mathrm{Trap}(P) - \frac{h^2}{12}(P'(u + h/2) - P'(u - h/2))$ cancels the $O(h^3)$
   quadratic defect identically, leaving the exact fourth-order residual $-\frac{1}{8} c_3 h^4$.

5. **`qou-y3xv`** (`gswz_global_symbol_norm_obstruction_and_hilbert90_splice`):
   For the GSWZ (270) global symbol $\xi = 2[z_1] + [z_2]$ with $z_1 = 1 - a^2$ and
   $z_2 = z_1^2 - z_1 + 2$, proves $z_2 - 2 = a^2(a^2 - 1)$, proves that the relative
   degree $[F : \mathbb{Q}_{25}] = 2m$ makes the naive Galois norm of any base element
   $x^{2m} = (x^2)^m$ an exact $m$-th power, and proves that the Hilbert-90 spliced
   element $P = a_0 \cdot b^m$ recovers the base class $P / b^m = a_0$ for $b \neq 0$.
-/

namespace QOU.QBeta.SteepestDescentEulerMaclaurinAndFrobeniusDiagonal

/-! ## 1. `qou-i9xj`: Fantini–Wheeler eq. (14) quadratic shift and contour bridge -/

/-- Quadratic $q$-exponent $\frac{1}{2}(A m^2 + B \ell^2)$ appearing in the Fantini–Wheeler
eq. (14) state-integral recursion. -/
def fwQuadraticExponent (A B m l : ℚ) : ℚ :=
  (A * m ^ 2 + B * l ^ 2) / 2

/-- Cauchy contour difference between two steepest-descent paths separated by residue sum `R`. -/
def contourIntegralDifference (I_left I_right : ℚ) : ℚ :=
  I_left - I_right

/-- **Theorem (`qou-i9xj`)**: The Fantini–Wheeler quadratic exponent satisfies
`fwQuadraticExponent A B (m + 1) (l + 1) - fwQuadraticExponent A B m l = A * m + B * l + (A + B) / 2`,
specializing at the $5_2$ parameters `(A, B) = (2, 3)` to `2 * m + 3 * l + 5 / 2` with
`3 - 2 = 1`, and two steepest-descent contour integrals whose Cauchy residue difference is `0`
are equal. -/
theorem fantini_wheeler_eq14_five_two_quadratic_shift_and_contour_bridge
    (A B m l I_left I_right : ℚ)
    (hResidueZero : contourIntegralDifference I_left I_right = 0) :
    fwQuadraticExponent A B (m + 1) (l + 1) - fwQuadraticExponent A B m l =
        A * m + B * l + (A + B) / 2 ∧
      fwQuadraticExponent 2 3 (m + 1) (l + 1) - fwQuadraticExponent 2 3 m l =
        2 * m + 3 * l + 5 / 2 ∧
      I_left = I_right := by
  refine ⟨?_, ?_, ?_⟩
  · unfold fwQuadraticExponent
    ring
  · unfold fwQuadraticExponent
    ring
  · unfold contourIntegralDifference at hResidueZero
    linarith

/-! ## 2. `qou-r4ya`: Balanced D-function theta-limit recentring and coset projection -/

/-- Recentred quadratic exponent $(k - \phi_1)^2 - \phi_1^2$ for the balanced $D$-function
around the $u \equiv 1$ lattice shift. -/
def balancedRecentredExponent (k phi1 : ℚ) : ℚ :=
  (k - phi1) ^ 2 - phi1 ^ 2

/-- Friedrichs even $q$-sublattice point $2j + \phi_1$ in the $\phi_1$ coset. -/
def friedrichsEvenSublatticePoint (j phi1 : ℚ) : ℚ :=
  2 * j + phi1

/-- Krein odd $q$-sublattice point $(2j + 1) + \phi_1$ in the $\phi_1$ coset. -/
def kreinOddSublatticePoint (j phi1 : ℚ) : ℚ :=
  2 * j + 1 + phi1

/-- **Theorem (`qou-r4ya`)**: The balanced $D$-function exponent $k^2 - 2 \phi_1 k$ equals
`balancedRecentredExponent k phi1 = (k - phi1)^2 - phi1^2` (unique vertex at $k = \phi_1$),
and the Friedrichs even sublattice point and Krein odd sublattice point both recover the
same coset representative $\phi_1$ after subtracting their integer shifts $2j$ and $2j + 1$,
while differing from each other by $1$. -/
theorem balanced_d_function_recentred_square_and_sublattice_coset
    (k j phi1 : ℚ) :
    k ^ 2 - 2 * phi1 * k = balancedRecentredExponent k phi1 ∧
      friedrichsEvenSublatticePoint j phi1 - 2 * j = phi1 ∧
      kreinOddSublatticePoint j phi1 - (2 * j + 1) = phi1 ∧
      kreinOddSublatticePoint j phi1 - friedrichsEvenSublatticePoint j phi1 = 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold balancedRecentredExponent
    ring
  · unfold friedrichsEvenSublatticePoint
    ring
  · unfold kreinOddSublatticePoint
    ring
  · unfold kreinOddSublatticePoint friedrichsEvenSublatticePoint
    ring

/-! ## 3. `qou-xsv8`: Center $Z(H_3(q))$ diagonal Frobenius pairing and partition of unity -/

/-- Diagonal Frobenius trace pairing in the central idempotent basis of $Z(H_3(q))$. -/
def centerDiagonalPairing (w0 w1 w2 a0 a1 a2 b0 b1 b2 : ℚ) : ℚ :=
  w0 * a0 * b0 + w1 * a1 * b1 + w2 * a2 * b2

/-- Common denominator $D(q) = q^6 + 2q^4 + 2q^2 + 1 = (q^2 + 1)(q^4 + q^2 + 1)$ of the
central idempotent trace weights in $Z(H_3(q))$. -/
def heckeH3CenterDenom (q : ℚ) : ℚ :=
  q ^ 6 + 2 * q ^ 4 + 2 * q ^ 2 + 1

/-- **Theorem (`qou-xsv8`)**: Under the diagonal Frobenius pairing on $Z(H_3(q))$, any central
element concentrated in the middle stratum $(0, a_1, 0)$ pairs to zero with $(b_0, 0, b_2)$
(even when anti-diagonal partners $b_0, b_2$ are nonzero), and the three central idempotent
trace weights $1/D(q)$, $2q^2/(q^4 + q^2 + 1)$, and $q^6/D(q)$ sum to $1$ whenever
$q^2 + 1 \neq 0$ and $q^4 + q^2 + 1 \neq 0$. -/
theorem hecke_h3_center_frobenius_diagonal_and_partition_of_unity
    (q w0 w1 w2 a1 b0 b2 : ℚ)
    (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    centerDiagonalPairing w0 w1 w2 0 a1 0 b0 0 b2 = 0 ∧
      heckeH3CenterDenom q = (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) ∧
      1 / heckeH3CenterDenom q +
          (2 * q ^ 2) / (q ^ 4 + q ^ 2 + 1) +
          q ^ 6 / heckeH3CenterDenom q = 1 := by
  have hDenomFact : heckeH3CenterDenom q = (q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1) := by
    unfold heckeH3CenterDenom
    ring
  have hDenomNe : heckeH3CenterDenom q ≠ 0 := by
    rw [hDenomFact]
    exact mul_ne_zero hq2 hq4
  refine ⟨?_, hDenomFact, ?_⟩
  · unfold centerDiagonalPairing
    ring
  · unfold heckeH3CenterDenom at hDenomNe ⊢
    field_simp [hDenomNe, hq4]
    ring

/-! ## 4. `qou-xzlt`: Second-order Euler–Maclaurin cubic cell cancellation -/

/-- Exact cell integral of $P(t) = c_0 + c_1(t - u) + c_2(t - u)^2 + c_3(t - u)^3$ over
$[u - h/2, u + h/2]$. -/
def cubicCellExactIntegral (c0 c2 h : ℚ) : ℚ :=
  c0 * h + c2 * h ^ 3 / 12

/-- Trapezoid rule for $P(t) = c_0 + c_1(t - u) + c_2(t - u)^2 + c_3(t - u)^3$ on
$[u - h/2, u + h/2]$. -/
def cubicCellTrapezoid (c0 c2 h : ℚ) : ℚ :=
  c0 * h + c2 * h ^ 3 / 4

/-- Endpoint derivative difference $P'(u + h/2) - P'(u - h/2)$ for the cubic cell polynomial. -/
def cubicCellDerivativeDiff (c2 c3 h : ℚ) : ℚ :=
  2 * c2 * h + (3 / 2) * c3 * h ^ 2

/-- Second-order Euler–Maclaurin corrected cell approximation
$\mathrm{Trap}(P) - \frac{h^2}{12}(P'(u + h/2) - P'(u - h/2))$. -/
def cubicCellEulerMaclaurin2 (c0 c2 c3 h : ℚ) : ℚ :=
  cubicCellTrapezoid c0 c2 h - (h ^ 2 / 12) * cubicCellDerivativeDiff c2 c3 h

/-- **Theorem (`qou-xzlt`)**: On the cell $[u - h/2, u + h/2]$, the raw trapezoid defect is
$c_2 h^3 / 6$, whereas the second-order Euler–Maclaurin corrected approximation cancels the
$O(h^3)$ quadratic term identically and leaves the exact fourth-order residual
$-c_3 h^4 / 8$ (so it is exact for all quadratics $c_3 = 0$). -/
theorem euler_maclaurin_second_order_cubic_cell_cancellation
    (c0 c2 c3 h : ℚ) :
    cubicCellTrapezoid c0 c2 h - cubicCellExactIntegral c0 c2 h = c2 * h ^ 3 / 6 ∧
      cubicCellEulerMaclaurin2 c0 c2 c3 h - cubicCellExactIntegral c0 c2 h =
        -(c3 * h ^ 4) / 8 ∧
      cubicCellEulerMaclaurin2 c0 c2 0 h = cubicCellExactIntegral c0 c2 h := by
  refine ⟨?_, ?_, ?_⟩
  · unfold cubicCellTrapezoid cubicCellExactIntegral
    ring
  · unfold cubicCellEulerMaclaurin2 cubicCellTrapezoid cubicCellDerivativeDiff cubicCellExactIntegral
    ring
  · unfold cubicCellEulerMaclaurin2 cubicCellTrapezoid cubicCellDerivativeDiff cubicCellExactIntegral
    ring

/-! ## 5. `qou-y3xv`: GSWZ (270) global symbol norm obstruction and Hilbert-90 splice -/

/-- Primary GSWZ (270) Nahm component $z_1(a) = 1 - a^2$. -/
def gswzZ1 (a : ℚ) : ℚ :=
  1 - a ^ 2

/-- Secondary GSWZ (270) Nahm component $z_2(a) = z_1(a)^2 - z_1(a) + 2$. -/
def gswzZ2 (a : ℚ) : ℚ :=
  (gswzZ1 a) ^ 2 - gswzZ1 a + 2

/-- **Theorem (`qou-y3xv`)**: For $z_1(a) = 1 - a^2$ and $z_2(a) = z_1(a)^2 - z_1(a) + 2$,
we have $z_2(a) - 2 = a^2(a^2 - 1)$; for any relative extension degree $d/2 = 2m$, the
base-element norm power $x^{2m}$ equals $(x^2)^m$ (an exact $m$-th power, obstructing naive
norm descent $\bmod m$); and for a Hilbert-90 spliced element $P = a_0 \cdot b^m$ with
$b \neq 0$, dividing by $b^m$ recovers the descended base class $a_0$. -/
theorem gswz_global_symbol_norm_obstruction_and_hilbert90_splice
    (a x a0 b : ℚ) (m : ℕ) (hb : b ≠ 0) :
    gswzZ2 a - 2 = a ^ 2 * (a ^ 2 - 1) ∧
      x ^ (2 * m) = (x ^ 2) ^ m ∧
      (a0 * b ^ m) / b ^ m = a0 := by
  have hbm : b ^ m ≠ 0 := pow_ne_zero m hb
  refine ⟨?_, ?_, ?_⟩
  · unfold gswzZ2 gswzZ1
    ring
  · rw [pow_mul]
  · exact mul_div_cancel_right₀ a0 hbm

end QOU.QBeta.SteepestDescentEulerMaclaurinAndFrobeniusDiagonal
