/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization of:
1. qou-pha4: Cumulative swap operators and elementary symmetric centrality in the 3-strand
   quadratic generator representation.
2. qou-mhx0: Base-tabloid to diagonal-eigenbasis transition matrix and eigenvalue diagonalization
   for the two-row 3-box module.
3. qou-68e1: Consolidated cell-length and content-shift polynomial product identities for two-row
   and single-row 3-box shapes.
4. qou-zwzd: Additive multiplicity-weighted sum and multiplicative product formulas connecting
   shape cell products to the third quantum factorial polynomial.
5. qou-xyxc: Curl-difference trace factorization and uniqueness of the two-component quantum
   dimension at quadratic framing.
-/

namespace QOU.Foundations.CumulativeSwapCentralityTabloidTransitionCellProductFactorialCurlTrace

/-!
### Part 1 (`qou-pha4`): Cumulative Swap Operators and Elementary Symmetric Centrality

We represent $2 \times 2$ integer matrices over a parameter $q \in \mathbb{Z}$ as a 4-tuple of entries
$(a_{11}, a_{12}, a_{21}, a_{22})$. On the 2-dimensional standard reflection module for $n = 3$,
the adjacent quadratic generators act by
$$G_1(q) = \begin{pmatrix} q & 1 \\ 0 & -1 \end{pmatrix}, \qquad
  G_2(q) = \begin{pmatrix} -1 & 0 \\ q & q \end{pmatrix}.$$
The scaled cumulative swap elements are
$$L_2(q) = q G_1(q) = \begin{pmatrix} q^2 & q \\ 0 & -q \end{pmatrix}, \qquad
  L_3(q) = G_2(q) G_1(q) G_2(q) + q G_2(q) = \begin{pmatrix} -q & -q \\ 0 & q^2 \end{pmatrix}.$$
We prove that $G_1(q), G_2(q)$ satisfy the cubic braid-type relation $G_1 G_2 G_1 = G_2 G_1 G_2$,
that $L_2(q)$ and $L_3(q)$ commute, and that their elementary symmetric combinations
$e_1(L_2, L_3) = L_2 + L_3 = (q^2 - q) I_2$ and $e_2(L_2, L_3) = L_2 L_3 = -q^3 I_2$ commute with
both generators $G_1(q)$ and $G_2(q)$.
-/

/-- A $2 \times 2$ matrix with integer entries stored in row-major order. -/
structure Mat2 where
  /-- Top-left entry $(1,1)$. -/
  a11 : Int
  /-- Top-right entry $(1,2)$. -/
  a12 : Int
  /-- Bottom-left entry $(2,1)$. -/
  a21 : Int
  /-- Bottom-right entry $(2,2)$. -/
  a22 : Int
  deriving DecidableEq, Repr

/-- Matrix addition on $2 \times 2$ integer matrices. -/
def mat2Add (A B : Mat2) : Mat2 :=
  { a11 := A.a11 + B.a11
    a12 := A.a12 + B.a12
    a21 := A.a21 + B.a21
    a22 := A.a22 + B.a22 }

/-- Matrix multiplication on $2 \times 2$ integer matrices. -/
def mat2Mul (A B : Mat2) : Mat2 :=
  { a11 := A.a11 * B.a11 + A.a12 * B.a21
    a12 := A.a11 * B.a12 + A.a12 * B.a22
    a21 := A.a21 * B.a11 + A.a22 * B.a21
    a22 := A.a21 * B.a12 + A.a22 * B.a22 }

/-- Scalar multiple of the $2 \times 2$ identity matrix $\text{diag}(s, s)$. -/
def mat2Scalar (s : Int) : Mat2 :=
  { a11 := s, a12 := 0, a21 := 0, a22 := s }

/-- First adjacent generator $G_1(q) = \begin{pmatrix} q & 1 \\ 0 & -1 \end{pmatrix}$. -/
def adjGen1 (q : Int) : Mat2 :=
  { a11 := q, a12 := 1, a21 := 0, a22 := -1 }

/-- Second adjacent generator $G_2(q) = \begin{pmatrix} -1 & 0 \\ q & q \end{pmatrix}$. -/
def adjGen2 (q : Int) : Mat2 :=
  { a11 := -1, a12 := 0, a21 := q, a22 := q }

/-- Second cumulative swap operator $L_2(q) = \begin{pmatrix} q^2 & q \\ 0 & -q \end{pmatrix}$. -/
def cumSwap2 (q : Int) : Mat2 :=
  { a11 := q * q, a12 := q, a21 := 0, a22 := -q }

/-- Third cumulative swap operator $L_3(q) = \begin{pmatrix} -q & -q \\ 0 & q^2 \end{pmatrix}$. -/
def cumSwap3 (q : Int) : Mat2 :=
  { a11 := -q, a12 := -q, a21 := 0, a22 := q * q }

/-- First elementary symmetric sum $e_1(L_2(q), L_3(q)) = L_2(q) + L_3(q)$. -/
def cumSwapElemSym1 (q : Int) : Mat2 :=
  mat2Add (cumSwap2 q) (cumSwap3 q)

/-- Second elementary symmetric product $e_2(L_2(q), L_3(q)) = L_2(q) L_3(q)$. -/
def cumSwapElemSym2 (q : Int) : Mat2 :=
  mat2Mul (cumSwap2 q) (cumSwap3 q)

/-- Any scalar diagonal matrix $\text{diag}(s, s)$ commutes with an arbitrary $2 \times 2$ matrix. -/
theorem mat2Scalar_mul_comm (s : Int) (A : Mat2) (hs : s ≠ 0) :
    mat2Mul (mat2Scalar s) A = mat2Mul A (mat2Scalar s) ∧
    (mat2Scalar s).a11 ≠ 0 := by
  dsimp only [mat2Mul, mat2Scalar]
  refine ⟨?_, hs⟩
  congr 1
  · rw [Int.mul_comm s A.a11]
    omega
  · rw [Int.mul_comm s A.a12]
    omega
  · rw [Int.mul_comm s A.a21]
    omega
  · rw [Int.mul_comm s A.a22]
    omega

/-- `qou-pha4`: The adjacent generators $G_1(q)$ and $G_2(q)$ satisfy the triple relation
$G_1(q) G_2(q) G_1(q) = G_2(q) G_1(q) G_2(q)$, the cumulative swap operators $L_2(q)$ and $L_3(q)$
commute, and both elementary symmetric combinations $e_1(L_2, L_3)$ and $e_2(L_2, L_3)$ equal scalar
multiples of the identity matrix and commute with $G_1(q)$ and $G_2(q)$. -/
theorem cumulative_swap_elementary_symmetric_central (q : Int) (hq : q ≠ 0) :
    mat2Mul (mat2Mul (adjGen1 q) (adjGen2 q)) (adjGen1 q) =
      mat2Mul (mat2Mul (adjGen2 q) (adjGen1 q)) (adjGen2 q) ∧
    cumSwapElemSym1 q = mat2Scalar (q * q - q) ∧
    cumSwapElemSym2 q = mat2Scalar (-(q * q * q)) ∧
    mat2Mul (cumSwap2 q) (cumSwap3 q) = mat2Mul (cumSwap3 q) (cumSwap2 q) ∧
    mat2Mul (cumSwapElemSym1 q) (adjGen1 q) = mat2Mul (adjGen1 q) (cumSwapElemSym1 q) ∧
    mat2Mul (cumSwapElemSym1 q) (adjGen2 q) = mat2Mul (adjGen2 q) (cumSwapElemSym1 q) ∧
    mat2Mul (cumSwapElemSym2 q) (adjGen1 q) = mat2Mul (adjGen1 q) (cumSwapElemSym2 q) ∧
    mat2Mul (cumSwapElemSym2 q) (adjGen2 q) = mat2Mul (adjGen2 q) (cumSwapElemSym2 q) ∧
    (adjGen1 q).a11 ≠ 0 := by
  have hElem1 : cumSwapElemSym1 q = mat2Scalar (q * q - q) := by
    dsimp only [cumSwapElemSym1, cumSwap2, cumSwap3, mat2Add, mat2Scalar]
    congr 1 <;> omega
  have hCancelCube : q * q * -q + q * (q * q) = 0 := by
    rw [Int.mul_neg, Int.mul_assoc]
    omega
  have hElem2 : cumSwapElemSym2 q = mat2Scalar (-(q * q * q)) := by
    dsimp only [cumSwapElemSym2, cumSwap2, cumSwap3, mat2Mul, mat2Scalar]
    have h11 : q * q * -q + q * 0 = -(q * q * q) := by
      rw [Int.mul_neg]
      omega
    have h21 : 0 * -q + -q * 0 = 0 := by omega
    have h22 : 0 * -q + -q * (q * q) = -(q * q * q) := by
      rw [Int.zero_mul, Int.zero_add, Int.neg_mul, ← Int.mul_assoc]
    rw [h11, hCancelCube, h21, h22]
  have hSwapComm : mat2Mul (cumSwap2 q) (cumSwap3 q) = mat2Mul (cumSwap3 q) (cumSwap2 q) := by
    have hRev : mat2Mul (cumSwap3 q) (cumSwap2 q) = mat2Scalar (-(q * q * q)) := by
      dsimp only [cumSwap2, cumSwap3, mat2Mul, mat2Scalar]
      have r11 : -q * (q * q) + -q * 0 = -(q * q * q) := by
        rw [Int.neg_mul, ← Int.mul_assoc]
        omega
      have r12 : -q * q + -q * -q = 0 := by
        rw [Int.neg_mul, Int.neg_mul, Int.mul_neg]
        omega
      have r21 : 0 * (q * q) + q * q * 0 = 0 := by omega
      have r22 : 0 * q + q * q * -q = -(q * q * q) := by
        rw [Int.zero_mul, Int.zero_add, Int.mul_neg]
      rw [r11, r12, r21, r22]
    exact hElem2.trans hRev.symm
  have hTriple :
      mat2Mul (mat2Mul (adjGen1 q) (adjGen2 q)) (adjGen1 q) =
        mat2Mul (mat2Mul (adjGen2 q) (adjGen1 q)) (adjGen2 q) := by
    dsimp only [adjGen1, adjGen2, mat2Mul]
    congr 1
    · omega
    · omega
    · have hL : (0 * -1 + -1 * q) * q + (0 * 0 + -1 * q) * 0 = -(q * q) := by
        rw [Int.zero_mul, Int.zero_add, Int.neg_mul, Int.one_mul, Int.neg_mul]
        omega
      have hR : (q * q + q * 0) * -1 + (q * 1 + q * -1) * q = -(q * q) := by
        have hSub : q * 1 + q * -1 = 0 := by omega
        rw [hSub, Int.zero_mul]
        omega
      rw [hL, hR]
    · omega
  refine ⟨hTriple, hElem1, hElem2, hSwapComm, ?_, ?_, ?_, ?_, ?_⟩
  · rw [hElem1]
    dsimp only [mat2Scalar, adjGen1, mat2Mul]
    congr 1
    · rw [Int.mul_comm (q * q - q) q]
      omega
    · omega
    · omega
    · omega
  · rw [hElem1]
    dsimp only [mat2Scalar, adjGen2, mat2Mul]
    congr 1
    · omega
    · omega
    · rw [Int.mul_comm (q * q - q) q]
      omega
    · rw [Int.mul_comm (q * q - q) q]
      omega
  · rw [hElem2]
    dsimp only [mat2Scalar, adjGen1, mat2Mul]
    congr 1
    · rw [Int.mul_comm (-(q * q * q)) q]
      omega
    · omega
    · omega
    · omega
  · rw [hElem2]
    dsimp only [mat2Scalar, adjGen2, mat2Mul]
    congr 1
    · omega
    · omega
    · rw [Int.mul_comm (-(q * q * q)) q]
      omega
    · rw [Int.mul_comm (-(q * q * q)) q]
      omega
  · dsimp only [adjGen1]
    exact hq

/-!
### Part 2 (`qou-mhx0`): Base-Tabloid to Diagonal-Eigenbasis Transition

In the 2-dimensional two-row tabloid basis $\{e_0, e_1\}$, the base tabloid vector is
$v_0 = (1, 0)^T$ and the upper-triangular orthogonalized second vector is
$v_1(q) = (-1, q + 1)^T$. We prove that $v_0$ is a joint eigenvector of $(L_2(q), L_3(q))$ with
eigenvalues $(q^2, -q)$, that $v_1(q)$ is a joint eigenvector of $(L_2(q), L_3(q))$ with
transposed eigenvalues $(-q, q^2)$, and that the transition matrix $P(q) = [v_0 \mid v_1(q)]$ has
determinant $q + 1 = [2]_q$.
-/

/-- A 2-component column vector over $\mathbb{Z}$. -/
structure Vec2 where
  /-- First coordinate. -/
  x1 : Int
  /-- Second coordinate. -/
  x2 : Int
  deriving DecidableEq, Repr

/-- Action of a $2 \times 2$ matrix on a 2-component column vector. -/
def mat2Act (A : Mat2) (v : Vec2) : Vec2 :=
  { x1 := A.a11 * v.x1 + A.a12 * v.x2
    x2 := A.a21 * v.x1 + A.a22 * v.x2 }

/-- Scalar multiplication on a 2-component column vector. -/
def vec2Scale (s : Int) (v : Vec2) : Vec2 :=
  { x1 := s * v.x1
    x2 := s * v.x2 }

/-- Primary base-tabloid vector $v_0 = (1, 0)^T$. -/
def baseTabloidVec0 : Vec2 :=
  { x1 := 1, x2 := 0 }

/-- Secondary triangular-shifted vector $v_1(q) = (-1, q + 1)^T$. -/
def baseTabloidVec1 (q : Int) : Vec2 :=
  { x1 := -1, x2 := q + 1 }

/-- Determinant of the $2 \times 2$ transition matrix whose columns are $u$ and $v$. -/
def transitionDet2 (u v : Vec2) : Int :=
  u.x1 * v.x2 - u.x2 * v.x1

/-- `qou-mhx0`: The base-tabloid vector $v_0 = (1, 0)^T$ and the triangular-shifted vector
$v_1(q) = (-1, q + 1)^T$ simultaneously diagonalize the cumulative swap operators $L_2(q)$ and
$L_3(q)$ with eigenvalues $(q^2, -q)$ and $(-q, q^2)$ respectively, and their transition
determinant equals $q + 1$. -/
theorem base_tabloid_eigenbasis_transition (q : Int) (hq : q + 1 ≠ 0) :
    mat2Act (cumSwap2 q) baseTabloidVec0 = vec2Scale (q * q) baseTabloidVec0 ∧
    mat2Act (cumSwap3 q) baseTabloidVec0 = vec2Scale (-q) baseTabloidVec0 ∧
    mat2Act (cumSwap2 q) (baseTabloidVec1 q) = vec2Scale (-q) (baseTabloidVec1 q) ∧
    mat2Act (cumSwap3 q) (baseTabloidVec1 q) = vec2Scale (q * q) (baseTabloidVec1 q) ∧
    transitionDet2 baseTabloidVec0 (baseTabloidVec1 q) = q + 1 ∧
    transitionDet2 baseTabloidVec0 (baseTabloidVec1 q) ≠ 0 := by
  dsimp only [mat2Act, vec2Scale, cumSwap2, cumSwap3,
    baseTabloidVec0, baseTabloidVec1, transitionDet2]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · congr 1 <;> omega
  · congr 1 <;> omega
  · congr 1
    · rw [Int.mul_add, Int.mul_neg, Int.mul_one]
      omega
    · omega
  · congr 1
    · rw [Int.mul_add, Int.neg_mul, Int.neg_mul, Int.mul_neg, Int.mul_one]
      omega
    · omega
  · omega
  · have hDet : 1 * (q + 1) - 0 * -1 = q + 1 := by omega
    rw [hDet]
    exact hq

/-!
### Part 3 (`qou-68e1`): Consolidated Cell-Length and Content-Shift Polynomial Products

For $n = 3$ and base variable $Q \in \mathbb{Z}$, we define the polynomial quantum brackets
$[1]_Q = 1$, $[2]_Q = 1 + Q$, $[3]_Q = 1 + Q + Q^2$, the cell-length products for the single-row
shape $(3)$, the two-row shape $(2,1)$, and the three-row shape $(1,1,1)$, together with the
consolidated denominator relation $(1 - Q^h) = (1 - Q) [h]_Q$.
-/

/-- First polynomial quantum bracket $[1]_Q = 1$. -/
def qPolyBracket1 : Int := 1

/-- Second polynomial quantum bracket $[2]_Q = 1 + Q$. -/
def qPolyBracket2 (Q : Int) : Int := 1 + Q

/-- Third polynomial quantum bracket $[3]_Q = 1 + Q + Q^2$. -/
def qPolyBracket3 (Q : Int) : Int := 1 + Q + Q * Q

/-- Cell-length product for the single-row 3-box shape: $[3]_Q [2]_Q [1]_Q$. -/
def cellProductRow3 (Q : Int) : Int :=
  qPolyBracket3 Q * qPolyBracket2 Q * qPolyBracket1

/-- Cell-length product for the two-row 3-box shape $(2,1)$: $[3]_Q [1]_Q [1]_Q$. -/
def cellProductTwoRow21 (Q : Int) : Int :=
  qPolyBracket3 Q * qPolyBracket1 * qPolyBracket1

/-- Cell-length product for the three-row 3-box shape $(1,1,1)$: $[3]_Q [2]_Q [1]_Q$. -/
def cellProductCol111 (Q : Int) : Int :=
  qPolyBracket3 Q * qPolyBracket2 Q * qPolyBracket1

/-- Unnormalized polynomial denominator $(1 - Q^3)(1 - Q)^2$ for the two-row shape $(2,1)$. -/
def unnormalizedDenomTwoRow21 (Q : Int) : Int :=
  (1 - Q * Q * Q) * (1 - Q) * (1 - Q)

/-- `qou-68e1`: The unnormalized denominator $(1 - Q^3)(1 - Q)^2$ of the two-row 3-box shape
factors exactly as $(1 - Q)^3$ times its consolidated cell-length product $[3]_Q [1]_Q^2$, and
multiplying the two-row cell-length product by $[2]_Q$ recovers the single-row cell-length product. -/
theorem consolidated_cell_length_product_identities (Q : Int) (hQ : Q ≠ 1) :
    1 - Q * Q * Q = (1 - Q) * qPolyBracket3 Q ∧
    unnormalizedDenomTwoRow21 Q =
      (1 - Q) * (1 - Q) * (1 - Q) * cellProductTwoRow21 Q ∧
    qPolyBracket2 Q * cellProductTwoRow21 Q = cellProductRow3 Q ∧
    cellProductRow3 Q = 1 + 2 * Q + 2 * (Q * Q) + Q * Q * Q ∧
    1 - Q ≠ 0 := by
  have hCube : 1 - Q * Q * Q = (1 - Q) * (1 + Q + Q * Q) := by
    rw [Int.sub_mul, Int.one_mul, Int.mul_add, Int.mul_add, Int.mul_one, ← Int.mul_assoc]
    omega
  dsimp only [unnormalizedDenomTwoRow21, cellProductTwoRow21, cellProductRow3,
    qPolyBracket1, qPolyBracket2, qPolyBracket3]
  refine ⟨hCube, ?_, ?_, ?_, ?_⟩
  · rw [hCube, Int.mul_one, Int.mul_one]
    rw [Int.mul_assoc ((1 - Q) * (1 + Q + Q * Q)) (1 - Q) (1 - Q)]
    rw [Int.mul_assoc (1 - Q) (1 + Q + Q * Q) ((1 - Q) * (1 - Q))]
    rw [Int.mul_comm (1 + Q + Q * Q) ((1 - Q) * (1 - Q))]
    rw [← Int.mul_assoc (1 - Q) ((1 - Q) * (1 - Q)) (1 + Q + Q * Q)]
    rw [← Int.mul_assoc (1 - Q) (1 - Q) (1 - Q)]
  · rw [Int.mul_one, Int.mul_one, Int.mul_one, Int.mul_comm (1 + Q) (1 + Q + Q * Q)]
  · rw [Int.mul_one, Int.mul_add, Int.mul_one, Int.add_mul, Int.add_mul, Int.one_mul]
    omega
  · omega

/-!
### Part 4 (`qou-zwzd`): Additive and Multiplicative Shape-Product Formulas to $[3]_Q!$

We define the third polynomial quantum factorial $[3]_Q! = [1]_Q [2]_Q [3]_Q$ and the
partition-weighted dimension contributions for the three shapes of $n = 3$:
- $(3)$: weight $1 \cdot Q^0 = 1$,
- $(2,1)$: multiplicity $2$ times $Q^1 [2]_Q = 2 Q (1 + Q)$,
- $(1,1,1)$: weight $1 \cdot Q^3 = Q^3$.
We prove both the additive sum decomposition $1 + 2 Q (1 + Q) + Q^3 = [3]_Q!$ and the
multiplicative product identity $[2]_Q \cdot H_{(3)}(Q) H_{(2,1)}(Q) H_{(1,1,1)}(Q) = ([3]_Q!)^3$.
-/

/-- The third polynomial quantum factorial $[3]_Q! = [1]_Q [2]_Q [3]_Q$. -/
def qPolyFactorial3 (Q : Int) : Int :=
  qPolyBracket1 * qPolyBracket2 Q * qPolyBracket3 Q

/-- Additive multiplicity-weighted sum over the three 3-box shapes:
$1 + 2 Q [2]_Q + Q^3$. -/
def shapeWeightedFactorialSum3 (Q : Int) : Int :=
  1 + 2 * Q * qPolyBracket2 Q + Q * Q * Q

/-- `qou-zwzd`: The multiplicity-weighted sum over all three 3-box shapes equals $[3]_Q!$, and the
product of the three cell-length polynomials scaled by $[2]_Q$ equals $([3]_Q!)^3$. -/
theorem shape_product_and_sum_q_factorial_connection (Q : Int) (hQ : Q > 0) :
    shapeWeightedFactorialSum3 Q = qPolyFactorial3 Q ∧
    cellProductRow3 Q * (qPolyBracket2 Q * cellProductTwoRow21 Q) * cellProductCol111 Q =
      qPolyFactorial3 Q * qPolyFactorial3 Q * qPolyFactorial3 Q ∧
    qPolyFactorial3 Q > 0 := by
  have hRowEqFact : cellProductRow3 Q = qPolyFactorial3 Q := by
    dsimp only [cellProductRow3, qPolyFactorial3, qPolyBracket1, qPolyBracket2, qPolyBracket3]
    rw [Int.mul_one, Int.one_mul, Int.mul_comm (1 + Q + Q * Q) (1 + Q)]
  have hColEqFact : cellProductCol111 Q = qPolyFactorial3 Q := by
    dsimp only [cellProductCol111, qPolyFactorial3, qPolyBracket1, qPolyBracket2, qPolyBracket3]
    rw [Int.mul_one, Int.one_mul, Int.mul_comm (1 + Q + Q * Q) (1 + Q)]
  have hTwoRowScale : qPolyBracket2 Q * cellProductTwoRow21 Q = qPolyFactorial3 Q := by
    dsimp only [cellProductTwoRow21, qPolyFactorial3, qPolyBracket1, qPolyBracket2, qPolyBracket3]
    rw [Int.mul_one, Int.mul_one, Int.one_mul]
  have hFactExpand : qPolyFactorial3 Q = 1 + 2 * Q + 2 * (Q * Q) + Q * Q * Q := by
    dsimp only [qPolyFactorial3, qPolyBracket1, qPolyBracket2, qPolyBracket3]
    rw [Int.one_mul, Int.add_mul, Int.one_mul, Int.mul_add, Int.mul_add, Int.mul_one]
    rw [← Int.mul_assoc Q Q Q]
    omega
  refine ⟨?_, ?_, ?_⟩
  · rw [hFactExpand]
    dsimp only [shapeWeightedFactorialSum3, qPolyBracket2]
    rw [Int.mul_add, Int.mul_one, Int.mul_assoc 2 Q Q]
    omega
  · rw [hRowEqFact, hTwoRowScale, hColEqFact]
  · rw [hFactExpand]
    have hQ2 : Q * Q > 0 := Int.mul_pos hQ hQ
    have hQ3 : Q * Q * Q > 0 := Int.mul_pos hQ2 hQ
    omega

/-!
### Part 5 (`qou-xyxc`): Curl-Difference Trace Factorization and Two-Component Dimension Uniqueness

In cleared-denominator polynomial form (scaled by $q^2$), the positive and negative curl traces at
framing parameter $a = q^2$ are $C_+(q) = q^4$ and $C_- = 1$, the skein difference factor
(scaled by $q$) is $\delta(q) = q^2 - 1$, and the two-component quantum dimension (scaled by $q$)
is $D_2(q) = q^2 + 1$. We prove that $\delta(q) D_2(q) = C_+(q) - C_-$ and that any integer $D$
satisfying $\delta(q) D = C_+(q) - C_-$ when $q^2 \ne 1$ must equal $D_2(q) = q^2 + 1$.
-/

/-- Positive curl trace scaled by $q^2$ at framing $a = q^2$: $C_+(q) = q^4$. -/
def curlTracePosScaled (q : Int) : Int :=
  q * q * (q * q)

/-- Negative curl trace scaled by $q^2$ at framing $a = q^2$: $C_- = 1$. -/
def curlTraceNegScaled : Int := 1

/-- Skein difference factor scaled by $q$: $\delta(q) = q^2 - 1$. -/
def skeinDiffScaled (q : Int) : Int :=
  q * q - 1

/-- Two-component quantum dimension scaled by $q$: $D_2(q) = q^2 + 1$. -/
def qDimTwoScaled (q : Int) : Int :=
  q * q + 1

/-- `qou-xyxc`: The scaled curl trace difference $C_+(q) - C_- = q^4 - 1$ factors as the product
of the skein difference $\delta(q) = q^2 - 1$ and the two-component quantum dimension
$D_2(q) = q^2 + 1$, and when $q^2 \ne 1$, any $D \in \mathbb{Z}$ satisfying
$\delta(q) D = C_+(q) - C_-$ is uniquely forced to equal $D_2(q)$. -/
theorem curl_trace_difference_and_qdim_two_uniqueness (q D : Int)
    (hq : q * q ≠ 1)
    (hCurl : skeinDiffScaled q * D = curlTracePosScaled q - curlTraceNegScaled) :
    skeinDiffScaled q * qDimTwoScaled q = curlTracePosScaled q - curlTraceNegScaled ∧
    D = qDimTwoScaled q := by
  dsimp only [skeinDiffScaled, qDimTwoScaled, curlTracePosScaled, curlTraceNegScaled] at hCurl ⊢
  have hFactor : (q * q - 1) * (q * q + 1) = q * q * (q * q) - 1 := by
    rw [Int.sub_mul, Int.one_mul, Int.mul_add, Int.mul_one]
    omega
  refine ⟨hFactor, ?_⟩
  have hDiffZero : (q * q - 1) * (D - (q * q + 1)) = 0 := by
    rw [Int.mul_sub, hCurl, hFactor]
    omega
  have hqSub : q * q - 1 ≠ 0 := by omega
  rcases Int.mul_eq_zero.mp hDiffZero with hLeft | hRight
  · exact absurd hLeft hqSub
  · omega

end QOU.Foundations.CumulativeSwapCentralityTabloidTransitionCellProductFactorialCurlTrace
