/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization of:
1. qou-7crn: Cleared projector branching recursion and sandwich absorption identity at step n = 2 -> 3.
2. qou-7gei: Deterministic corner deletion on 3-row partitions of size >= 4 preserving >= 3 non-empty rows.
3. qou-qua1: Equivalence of the bracket non-vanishing criterion and the 3-box shape cell-product criterion.
4. qou-s7z2: Degenerate 3-block trace product vs. non-degenerate 2-block quotient determinant factor.
5. qou-tqab: Diagonal matrix-unit trace closure and multiplicity-weighted squared-content sum at n = 3.
-/

namespace QOU.Foundations.ProjectorBranchingThreeRowCornerDeletionGenerictyEquivalenceQuotientPairingDiagonalTrace

/-!
### Part 1 (`qou-7crn`): Cleared Projector Branching Recursion at Step $n = 2 \to 3$

Let $t \in \mathbb{Z}$ denote the loop parameter $t = [2]_q$, so $[3]_q = t^2 - 1$. On the
2-dimensional sandwich subspace, the cleared step-2 projector $B_2(t)$ and sandwich operator
$K_2(t)$ are represented by diagonal $2 \times 2$ matrices
$$B_2(t) = \begin{pmatrix} t & 0 \\ 0 & t \end{pmatrix}, \qquad
  K_2(t) = \begin{pmatrix} t^2 - 1 & 0 \\ 0 & 0 \end{pmatrix}.$$
The cleared step-3 branching recursion defines
$$B_3(t) = (t^2 - 1) B_2(t) - t K_2(t) = \begin{pmatrix} 0 & 0 \\ 0 & t(t^2 - 1) \end{pmatrix}.$$
We prove the absorption relation $K_2(t)^2 = (t^2 - 1) K_2(t)$, orthogonality
$B_3(t) K_2(t) = 0$, and the scaled idempotence relation $B_3(t)^2 = t(t^2 - 1) B_3(t)$.
-/

/-- Diagonal $2 \times 2$ integer matrix $\text{diag}(d_1, d_2)$. -/
structure DiagMat2 where
  /-- First diagonal entry. -/
  d1 : Int
  /-- Second diagonal entry. -/
  d2 : Int
  deriving DecidableEq, Repr

/-- Componentwise multiplication of diagonal $2 \times 2$ integer matrices. -/
def diagMat2Mul (A B : DiagMat2) : DiagMat2 :=
  { d1 := A.d1 * B.d1
    d2 := A.d2 * B.d2 }

/-- Componentwise subtraction of diagonal $2 \times 2$ integer matrices. -/
def diagMat2Sub (A B : DiagMat2) : DiagMat2 :=
  { d1 := A.d1 - B.d1
    d2 := A.d2 - B.d2 }

/-- Scalar multiplication of a diagonal $2 \times 2$ integer matrix. -/
def diagMat2Scale (s : Int) (A : DiagMat2) : DiagMat2 :=
  { d1 := s * A.d1
    d2 := s * A.d2 }

/-- Cleared step-2 projector $B_2(t) = \text{diag}(t, t)$. -/
def clearedProj2 (t : Int) : DiagMat2 :=
  { d1 := t, d2 := t }

/-- Sandwich operator $K_2(t) = \text{diag}(t^2 - 1, 0)$ on the step-2 image. -/
def sandwichOp2 (t : Int) : DiagMat2 :=
  { d1 := t * t - 1, d2 := 0 }

/-- Cleared step-3 branching projector $B_3(t) = (t^2 - 1) B_2(t) - t K_2(t)$. -/
def clearedBranchProj3 (t : Int) : DiagMat2 :=
  diagMat2Sub (diagMat2Scale (t * t - 1) (clearedProj2 t)) (diagMat2Scale t (sandwichOp2 t))

/-- `qou-7crn`: The sandwich operator $K_2(t)$ satisfies the quadratic absorption relation
$K_2(t)^2 = (t^2 - 1) K_2(t)$, the step-3 branching projector $B_3(t)$ annihilates $K_2(t)$, and
$B_3(t)$ satisfies the scaled idempotence relation $B_3(t)^2 = t(t^2 - 1) B_3(t)$. -/
theorem cleared_projector_branching_recursion_step3 (t : Int) (ht : t ≥ 2) :
    diagMat2Mul (sandwichOp2 t) (sandwichOp2 t) =
      diagMat2Scale (t * t - 1) (sandwichOp2 t) ∧
    diagMat2Mul (clearedBranchProj3 t) (sandwichOp2 t) = { d1 := 0, d2 := 0 } ∧
    diagMat2Mul (clearedBranchProj3 t) (clearedBranchProj3 t) =
      diagMat2Scale ((t * t - 1) * t) (clearedBranchProj3 t) ∧
    (clearedBranchProj3 t).d2 > 0 := by
  have hD1Zero : (t * t - 1) * t - t * (t * t - 1) = 0 := by
    rw [Int.mul_comm (t * t - 1) t]
    omega
  dsimp only [clearedBranchProj3, clearedProj2, sandwichOp2,
    diagMat2Mul, diagMat2Sub, diagMat2Scale]
  refine ⟨?_, ?_, ?_, ?_⟩
  · congr 1
    omega
  · congr 1
    · rw [hD1Zero]
      omega
    · omega
  · congr 1
    · rw [hD1Zero]
      omega
    · rw [Int.mul_zero, Int.sub_zero]
  · have ht2 : t * t ≥ 4 := by
      have hSub : t - 2 ≥ 0 := by omega
      have hProd : (t - 2) * (t + 2) ≥ 0 := Int.mul_nonneg hSub (by omega)
      rw [Int.sub_mul, Int.mul_add, Int.mul_add] at hProd
      omega
    have hPos1 : t * t - 1 > 0 := by omega
    have hPos2 : t > 0 := by omega
    have hProdPos : (t * t - 1) * t > 0 := Int.mul_pos hPos1 hPos2
    omega

/-!
### Part 2 (`qou-7gei`): Deterministic Corner Deletion on Three-Row Partitions of Size $\ge 4$

A 3-row partition $\lambda = (\ell_1, \ell_2, \ell_3)$ has $\ell_1 \ge \ell_2 \ge \ell_3 \ge 1$ and size
$|\lambda| = \ell_1 + \ell_2 + \ell_3$. We define `deleteThreeRowCorner` by:
- decrementing $\ell_3$ if $\ell_3 \ge 2$,
- else decrementing $\ell_1$ if $\ell_1 > \ell_2$,
- else decrementing $\ell_2$.
We prove that whenever $|\lambda| \ge 4$, the resulting triple $(\ell_1', \ell_2', \ell_3')$ still
satisfies $\ell_1' \ge \ell_2' \ge \ell_3' \ge 1$ and has size $|\lambda| - 1$, whereas at
$|\lambda| = 3$ no 3-row partition of size $2$ exists.
-/

/-- A 3-tuple of row lengths $(\ell_1, \ell_2, \ell_3)$. -/
structure RowTriple where
  /-- First row length $\ell_1$. -/
  l1 : Int
  /-- Second row length $\ell_2$. -/
  l2 : Int
  /-- Third row length $\ell_3$. -/
  l3 : Int
  deriving DecidableEq, Repr

/-- Total box count $\ell_1 + \ell_2 + \ell_3$ of a 3-row tuple. -/
def rowTripleSize (r : RowTriple) : Int :=
  r.l1 + r.l2 + r.l3

/-- Validity predicate $\ell_1 \ge \ell_2 \ge \ell_3 \ge 1$ for a 3-row partition. -/
def isValidThreeRow (r : RowTriple) : Prop :=
  r.l1 ≥ r.l2 ∧ r.l2 ≥ r.l3 ∧ r.l3 ≥ 1

/-- Deterministic corner deletion on a 3-row partition leaving 3 non-empty rows when size $\ge 4$. -/
def deleteThreeRowCorner (r : RowTriple) : RowTriple :=
  if r.l3 ≥ 2 then
    { l1 := r.l1, l2 := r.l2, l3 := r.l3 - 1 }
  else if r.l1 > r.l2 then
    { l1 := r.l1 - 1, l2 := r.l2, l3 := r.l3 }
  else
    { l1 := r.l1, l2 := r.l2 - 1, l3 := r.l3 }

/-- `qou-7gei`: For every valid 3-row partition $r = (\ell_1, \ell_2, \ell_3)$ with
$\ell_1 + \ell_2 + \ell_3 \ge 4$, `deleteThreeRowCorner r` is a valid 3-row partition of size
$\ell_1 + \ell_2 + \ell_3 - 1$, whereas no valid 3-row partition can have size $2$. -/
theorem delete_three_row_corner_preserves_three_rows (r : RowTriple)
    (hValid : isValidThreeRow r)
    (hSize : rowTripleSize r ≥ 4) :
    isValidThreeRow (deleteThreeRowCorner r) ∧
    rowTripleSize (deleteThreeRowCorner r) = rowTripleSize r - 1 ∧
    ∀ s : RowTriple, isValidThreeRow s → rowTripleSize s ≠ 2 := by
  rcases hValid with ⟨h12, h23, h31⟩
  dsimp only [rowTripleSize] at hSize
  refine ⟨?_, ?_, ?_⟩
  · dsimp only [deleteThreeRowCorner, isValidThreeRow]
    split
    · dsimp only
      refine ⟨h12, by omega, by omega⟩
    · split
      · dsimp only
        refine ⟨by omega, h23, h31⟩
      · dsimp only
        refine ⟨by omega, by omega, h31⟩
  · dsimp only [deleteThreeRowCorner, rowTripleSize]
    split
    · dsimp only
      omega
    · split
      · dsimp only
        omega
      · dsimp only
        omega
  · intro s hs
    rcases hs with ⟨hs12, hs23, hs31⟩
    dsimp only [rowTripleSize]
    omega

/-!
### Part 3 (`qou-qua1`): Equivalence of Bracket Genericity and Cell-Product Non-Vanishing

At level $n = 3$ and base variable $Q \in \mathbb{Z}$, the polynomial quantum brackets are
$[2]_Q = 1 + Q$ and $[3]_Q = 1 + Q + Q^2$, and the cell-length polynomials of the three 3-box shapes
are $H_{(3)}(Q) = [2]_Q [3]_Q$, $H_{(2,1)}(Q) = [3]_Q$, and $H_{(1,1,1)}(Q) = [2]_Q [3]_Q$.
We prove that $[3]_Q > 0$ for every integer $Q \in \mathbb{Z}$, and that the bracket non-vanishing
condition $([2]_Q \ne 0 \land [3]_Q \ne 0)$ is logically equivalent to the simultaneous
non-vanishing of $H_{(3)}(Q), H_{(2,1)}(Q), H_{(1,1,1)}(Q)$.
-/

/-- Second polynomial bracket $[2]_Q = 1 + Q$. -/
def genBracket2 (Q : Int) : Int := 1 + Q

/-- Third polynomial bracket $[3]_Q = 1 + Q + Q^2$. -/
def genBracket3 (Q : Int) : Int := 1 + Q + Q * Q

/-- Cell-length polynomial $H_{(3)}(Q) = [2]_Q [3]_Q$. -/
def shapeCellProd3 (Q : Int) : Int :=
  genBracket2 Q * genBracket3 Q

/-- Cell-length polynomial $H_{(2,1)}(Q) = [3]_Q$. -/
def shapeCellProd21 (Q : Int) : Int :=
  genBracket3 Q

/-- Cell-length polynomial $H_{(1,1,1)}(Q) = [2]_Q [3]_Q$. -/
def shapeCellProd111 (Q : Int) : Int :=
  genBracket2 Q * genBracket3 Q

/-- Every integer square $x^2$ is non-negative, and strictly positive when $x \ne 0$. -/
theorem int_sq_nonneg (x : Int) :
    x * x ≥ 0 ∧ (x ≠ 0 → x * x > 0) := by
  have hNonneg : x * x ≥ 0 := by
    rcases Int.lt_trichotomy x 0 with hNeg | hZero | hPos
    · have hNegNonneg : -x ≥ 0 := by omega
      have hP : (-x) * (-x) ≥ 0 := Int.mul_nonneg hNegNonneg hNegNonneg
      rw [Int.neg_mul, Int.mul_neg, Int.neg_neg] at hP
      exact hP
    · rw [hZero]
      omega
    · have hPosNonneg : x ≥ 0 := by omega
      exact Int.mul_nonneg hPosNonneg hPosNonneg
  refine ⟨hNonneg, ?_⟩
  intro hx
  rcases Int.lt_trichotomy x 0 with hNeg | hZero | hPos
  · have hNegPos : -x > 0 := by omega
    have hP : (-x) * (-x) > 0 := Int.mul_pos hNegPos hNegPos
    rw [Int.neg_mul, Int.mul_neg, Int.neg_neg] at hP
    exact hP
  · exact absurd hZero hx
  · exact Int.mul_pos hPos hPos

/-- `qou-qua1`: For every integer $Q \in \mathbb{Z}$, the third polynomial bracket satisfies
$2 [3]_Q = (Q + 1)^2 + Q^2 + 1 \ge 2$ (hence $[3]_Q > 0$), and the bracket non-vanishing condition
$([2]_Q \ne 0 \land [3]_Q \ne 0)$ holds if and only if all three shape cell-length polynomials
$H_{(3)}(Q), H_{(2,1)}(Q), H_{(1,1,1)}(Q)$ are non-zero. -/
theorem bracket_genericity_iff_shape_cell_products_nonzero (Q : Int) (hQ : Q ≠ -1) :
    2 * genBracket3 Q = (Q + 1) * (Q + 1) + Q * Q + 1 ∧
    genBracket3 Q > 0 ∧
    ((genBracket2 Q ≠ 0 ∧ genBracket3 Q ≠ 0) ↔
      (shapeCellProd3 Q ≠ 0 ∧ shapeCellProd21 Q ≠ 0 ∧ shapeCellProd111 Q ≠ 0)) ∧
    shapeCellProd3 Q ≠ 0 := by
  have hSos : 2 * genBracket3 Q = (Q + 1) * (Q + 1) + Q * Q + 1 := by
    dsimp only [genBracket3]
    rw [Int.mul_add, Int.mul_add, Int.mul_one]
    rw [Int.add_mul, Int.mul_add, Int.mul_one, Int.one_mul]
    omega
  have hB3Pos : genBracket3 Q > 0 := by
    have hSq1 : (Q + 1) * (Q + 1) ≥ 0 := (int_sq_nonneg (Q + 1)).1
    have hSq2 : Q * Q ≥ 0 := (int_sq_nonneg Q).1
    omega
  have hB2Ne : genBracket2 Q ≠ 0 := by
    dsimp only [genBracket2]
    omega
  have hB3Ne : genBracket3 Q ≠ 0 := by omega
  refine ⟨hSos, hB3Pos, ?_, ?_⟩
  · dsimp only [shapeCellProd3, shapeCellProd21, shapeCellProd111]
    constructor
    · rintro ⟨h2, h3⟩
      have hProd : genBracket2 Q * genBracket3 Q ≠ 0 := by
        intro hZero
        rcases Int.mul_eq_zero.mp hZero with hL | hR
        · exact h2 hL
        · exact h3 hR
      exact ⟨hProd, h3, hProd⟩
    · rintro ⟨hProd, h3, _⟩
      refine ⟨?_, h3⟩
      intro h2
      apply hProd
      rw [h2, Int.zero_mul]
  · dsimp only [shapeCellProd3]
    intro hZero
    rcases Int.mul_eq_zero.mp hZero with hL | hR
    · exact hB2Ne hL
    · exact hB3Ne hR

/-!
### Part 4 (`qou-s7z2`): Degenerate Full-Tower Trace Product vs. Non-Degenerate Quotient Determinant

At convention D with parameter $t = [2]_q \in \mathbb{Z}$, the cleared block trace weights at
$n = 3$ are $w_{(3)}(t) = t^3 - 2t$, $w_{(2,1)}(t) = t$, and $w_{(1,1,1)} = 0$.
The full 6-dimensional 3-block trace determinant factor is
$$G_{\text{full}}(t) = w_{(3)}(t) \cdot w_{(2,1)}(t)^4 \cdot w_{(1,1,1)},$$
whereas on the 5-dimensional two-row quotient (removing the 1-dimensional $(1,1,1)$ radical block),
the 2-block trace determinant factor is
$$G_{\text{quot}}(t) = w_{(3)}(t) \cdot w_{(2,1)}(t)^4 = t^4 (t^3 - 2t) = t^5 (t^2 - 2).$$
We prove that $G_{\text{full}}(t) = 0$ identically, whereas $G_{\text{quot}}(t) > 0$ for every $t \ge 2$.
-/

/-- Cleared trace weight $w_{(3)}(t) = t^3 - 2t$ on the symmetric block. -/
def quotWeight3 (t : Int) : Int :=
  t * t * t - 2 * t

/-- Cleared trace weight $w_{(2,1)}(t) = t$ on the 2-dimensional two-row block. -/
def quotWeight21 (t : Int) : Int := t

/-- Cleared trace weight $w_{(1,1,1)} = 0$ on the annihilated 3-row block. -/
def quotWeight111 : Int := 0

/-- Full 3-block trace determinant factor $w_{(3)}(t) w_{(2,1)}(t)^4 w_{(1,1,1)}$. -/
def fullThreeBlockDetFactor (t : Int) : Int :=
  quotWeight3 t * (quotWeight21 t * quotWeight21 t * (quotWeight21 t * quotWeight21 t)) * quotWeight111

/-- Quotient 2-block trace determinant factor $w_{(3)}(t) w_{(2,1)}(t)^4$. -/
def twoRowQuotientDetFactor (t : Int) : Int :=
  quotWeight3 t * (quotWeight21 t * quotWeight21 t * (quotWeight21 t * quotWeight21 t))

/-- `qou-s7z2`: The full 3-block determinant factor vanishes identically due to the annihilated
$(1,1,1)$ block, whereas the 2-block quotient determinant factor equals $(t^3 - 2t) t^4$ and is
strictly positive for every integer $t \ge 2$. -/
theorem quotient_two_row_det_factor_pos_and_full_zero (t : Int) (ht : t ≥ 2) :
    fullThreeBlockDetFactor t = 0 ∧
    twoRowQuotientDetFactor t = (t * t - 2) * t * (t * t * (t * t)) ∧
    twoRowQuotientDetFactor t > 0 ∧
    twoRowQuotientDetFactor 2 = 64 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · dsimp only [fullThreeBlockDetFactor, quotWeight111]
    rw [Int.mul_zero]
  · dsimp only [twoRowQuotientDetFactor, quotWeight3, quotWeight21]
    rw [Int.sub_mul (t * t) 2 t]
  · dsimp only [twoRowQuotientDetFactor, quotWeight3, quotWeight21]
    have htPos : t > 0 := by omega
    have ht2 : t * t ≥ 4 := by
      have hSub : t - 2 ≥ 0 := by omega
      have hProd : (t - 2) * (t + 2) ≥ 0 := Int.mul_nonneg hSub (by omega)
      rw [Int.sub_mul, Int.mul_add, Int.mul_add] at hProd
      omega
    have hFactorPos : t * t - 2 > 0 := by omega
    have hW3Eq : t * t * t - 2 * t = (t * t - 2) * t := by
      rw [Int.sub_mul (t * t) 2 t]
    have hW3Pos : t * t * t - 2 * t > 0 := by
      rw [hW3Eq]
      exact Int.mul_pos hFactorPos htPos
    have ht2Pos : t * t > 0 := by omega
    have ht4Pos : t * t * (t * t) > 0 := Int.mul_pos ht2Pos ht2Pos
    exact Int.mul_pos hW3Pos ht4Pos
  · decide

/-!
### Part 5 (`qou-tqab`): Diagonal Matrix-Unit Trace Closure and Squared-Content Sum at $n = 3$

On the 2-dimensional two-row block $(2,1)$ in its diagonal eigenbasis, the primitive idempotents are
$E_{00} = \text{diag}(1, 0)$ and $E_{11} = \text{diag}(0, 1)$, and the cumulative swap operators are
$D_2(q) = \text{diag}(q^2, -q)$ and $D_3(q) = \text{diag}(-q, q^2)$.
We prove that the diagonal matrix-unit traces sum to the block character
$\text{tr}(D_2(q) E_{00}) + \text{tr}(D_2(q) E_{11}) = q^2 - q$, and that the multiplicity-weighted
sum of squared content eigenvalues across all three 3-box shapes $(3), (2,1), (1,1,1)$ at $q = 1$
equals $1 \cdot (1^2 + 2^2) + 2 \cdot ((1^2 + (-1)^2) + ((-1)^2 + 1^2)) + 1 \cdot ((-1)^2 + (-2)^2)
= 18 = 3! \cdot \binom{3}{2}$.
-/

/-- Trace of a diagonal $2 \times 2$ integer matrix $d_1 + d_2$. -/
def diagMat2Trace (A : DiagMat2) : Int :=
  A.d1 + A.d2

/-- First primitive diagonal matrix unit $E_{00} = \text{diag}(1, 0)$. -/
def primUnit00 : DiagMat2 :=
  { d1 := 1, d2 := 0 }

/-- Second primitive diagonal matrix unit $E_{11} = \text{diag}(0, 1)$. -/
def primUnit11 : DiagMat2 :=
  { d1 := 0, d2 := 1 }

/-- Diagonal cumulative swap operator $D_2(q) = \text{diag}(q^2, -q)$. -/
def diagCumSwap2 (q : Int) : DiagMat2 :=
  { d1 := q * q, d2 := -q }

/-- Diagonal cumulative swap operator $D_3(q) = \text{diag}(-q, q^2)$. -/
def diagCumSwap3 (q : Int) : DiagMat2 :=
  { d1 := -q, d2 := q * q }

/-- Multiplicity-weighted sum of squared content eigenvalues across $\lambda \vdash 3$ at scale $s$:
$1 \cdot (s^2 + (2s)^2) + 2 \cdot ((s^2 + (-s)^2) + ((-s)^2 + s^2)) + 1 \cdot ((-s)^2 + (-2s)^2)$. -/
def weightedContentSquareSum3 (s : Int) : Int :=
  1 * (s * s + (2 * s) * (2 * s)) +
    2 * ((s * s + (-s) * (-s)) + ((-s) * (-s) + s * s)) +
    1 * ((-s) * (-s) + (-2 * s) * (-2 * s))

/-- `qou-tqab`: The primitive matrix-unit traces of $D_2(q)$ and $D_3(q)$ sum to $q^2 - q$, and the
multiplicity-weighted sum of squared content eigenvalues across all three 3-box shapes equals
$18 s^2$ (giving $18 = 3! \cdot \binom{3}{2}$ at $s = 1$). -/
theorem diagonal_matrix_unit_trace_and_content_square_closure (q s : Int) (hs : s ≠ 0) :
    diagMat2Trace (diagMat2Mul (diagCumSwap2 q) primUnit00) +
      diagMat2Trace (diagMat2Mul (diagCumSwap2 q) primUnit11) = q * q - q ∧
    diagMat2Trace (diagMat2Mul (diagCumSwap3 q) primUnit00) +
      diagMat2Trace (diagMat2Mul (diagCumSwap3 q) primUnit11) = q * q - q ∧
    weightedContentSquareSum3 s = 18 * (s * s) ∧
    weightedContentSquareSum3 1 = 18 ∧
    weightedContentSquareSum3 s > 0 := by
  have hNegSq : (-s) * (-s) = s * s := by
    rw [Int.neg_mul, Int.mul_neg, Int.neg_neg]
  have hTwoSq : (2 * s) * (2 * s) = 4 * (s * s) := by
    rw [← Int.mul_assoc (2 * s) 2 s, Int.mul_assoc 2 s 2, Int.mul_comm s 2,
      ← Int.mul_assoc 2 2 s, Int.mul_assoc (2 * 2) s s]
    omega
  have hNegTwoSq : (-2 * s) * (-2 * s) = 4 * (s * s) := by
    have hNeg2 : -2 * s = -(2 * s) := by omega
    rw [hNeg2, Int.neg_mul, Int.mul_neg, Int.neg_neg, hTwoSq]
  have hSumSq : weightedContentSquareSum3 s = 18 * (s * s) := by
    dsimp only [weightedContentSquareSum3]
    rw [hNegSq, hTwoSq, hNegTwoSq]
    omega
  refine ⟨?_, ?_, hSumSq, ?_, ?_⟩
  · dsimp only [diagMat2Trace, diagMat2Mul, diagCumSwap2, primUnit00, primUnit11]
    omega
  · dsimp only [diagMat2Trace, diagMat2Mul, diagCumSwap3, primUnit00, primUnit11]
    omega
  · decide
  · rw [hSumSq]
    have hs2Pos : s * s > 0 := (int_sq_nonneg s).2 hs
    omega

end QOU.Foundations.ProjectorBranchingThreeRowCornerDeletionGenerictyEquivalenceQuotientPairingDiagonalTrace
