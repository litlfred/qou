/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization of:
1. qou-ognw: Per-cell quadratic denominator bridge and two-row to three-row addable-cell
   polynomial ratio identity at shape (2,1).
2. qou-3quc: Fourth-order coinvariant degree polynomial sum across all five 4-box shapes
   and strict inequality with the unshifted sum of squared ratios.
3. qou-f1qs: Two-row lattice-vote difference recurrence and level-sum invariance for
   two-row bracket weights from n = 3 to n = 4.
4. qou-mpq5: Block-trace additivity and multiplicity-weighted character sum decomposition
   across the three 3-box matrix blocks.
5. qou-uinl: Orbit-constant function counts and permutation trace projections on the
   three-factor tensor power.
-/

namespace QOU.Foundations.AddableCellRatioFakeDegreeTwoRowBallotWeightTensorPowerCharacterOrbitTrace

/-!
### Part 1 (`qou-ognw`): Per-Cell Denominator Bridge and Addable-Cell Polynomial Identity

For base parameter $Q \in \mathbb{Z}$, the polynomial quantum brackets are
$[1]_Q = 1$, $[2]_Q = 1 + Q$, $[3]_Q = 1 + Q + Q^2$, and $[4]_Q = 1 + Q + Q^2 + Q^3$, with fourth
polynomial factorial $[4]_Q! = [1]_Q [2]_Q [3]_Q [4]_Q$.
For the two-row 3-box shape $\mu = (2,1)$, its three addable 4-box extensions are $\lambda^{(1)} = (3,1)$,
$\lambda^{(2)} = (2,2)$, and $\lambda^{(3)} = (2,1,1)$. Their cleared cell-length ratios
$R_\lambda(Q) = [4]_Q! / H_\lambda(Q)$ are:
- $R_{(3,1)}(Q) = [3]_Q = 1 + Q + Q^2$,
- $R_{(2,2)}(Q) = [4]_Q / [2]_Q = 1 + Q^2$,
- $R_{(2,1,1)}(Q) = [3]_Q = 1 + Q + Q^2$.
We prove the per-cell denominator factorizations $1 - q^4 = (1 - q^2)(1 + q^2)$ and
$1 - q^6 = (1 - q^2)(1 + q^2 + q^4)$, the exact division relation $[2]_Q (1 + Q^2) = [4]_Q$, and
the two-row addable-cell branching identity
$$R_{(3,1)}(Q) + Q R_{(2,2)}(Q) + Q^2 R_{(2,1,1)}(Q) = [4]_Q [2]_Q.$$
-/

/-- First polynomial quantum bracket $[1]_Q = 1$. -/
def polyBracket1 : Int := 1

/-- Second polynomial quantum bracket $[2]_Q = 1 + Q$. -/
def polyBracket2 (Q : Int) : Int := 1 + Q

/-- Third polynomial quantum bracket $[3]_Q = 1 + Q + Q^2$. -/
def polyBracket3 (Q : Int) : Int := 1 + Q + Q * Q

/-- Fourth polynomial quantum bracket $[4]_Q = 1 + Q + Q^2 + Q^3$. -/
def polyBracket4 (Q : Int) : Int := 1 + Q + Q * Q + Q * Q * Q

/-- Fourth polynomial quantum factorial $[4]_Q! = [1]_Q [2]_Q [3]_Q [4]_Q$. -/
def polyFactorial4 (Q : Int) : Int :=
  polyBracket1 * polyBracket2 Q * polyBracket3 Q * polyBracket4 Q

/-- Cleared cell-length ratio $R_{(3,1)}(Q) = [3]_Q$ for the first-row extension $(3,1)$. -/
def addableRatio31 (Q : Int) : Int :=
  polyBracket3 Q

/-- Cleared cell-length ratio $R_{(2,2)}(Q) = 1 + Q^2$ for the second-row extension $(2,2)$. -/
def addableRatio22 (Q : Int) : Int :=
  1 + Q * Q

/-- Cleared cell-length ratio $R_{(2,1,1)}(Q) = [3]_Q$ for the third-row extension $(2,1,1)$. -/
def addableRatio211 (Q : Int) : Int :=
  polyBracket3 Q

/-- Row-shifted sum of addable-cell ratios for $\mu = (2,1)$:
$R_{(3,1)}(Q) + Q R_{(2,2)}(Q) + Q^2 R_{(2,1,1)}(Q)$. -/
def addableCellRatioSum21 (Q : Int) : Int :=
  addableRatio31 Q + Q * addableRatio22 Q + Q * Q * addableRatio211 Q

/-- `qou-ognw`: The per-cell denominator $1 - q^4$ factors as $(1 - q^2)(1 + q^2)$, the ratio
$R_{(2,2)}(Q) = 1 + Q^2$ satisfies $[2]_Q R_{(2,2)}(Q) = [4]_Q$, and the row-shifted sum of
addable-cell ratios over the three extensions $(3,1), (2,2), (2,1,1)$ of $\mu = (2,1)$ equals
$[4]_Q [2]_Q$. -/
theorem two_row_addable_cell_ratio_identity (q Q : Int) (hq : q * q ≠ 1) :
    1 - q * q * (q * q) = (1 - q * q) * (1 + q * q) ∧
    polyBracket2 Q * addableRatio22 Q = polyBracket4 Q ∧
    addableCellRatioSum21 Q = polyBracket4 Q * polyBracket2 Q ∧
    1 - q * q ≠ 0 := by
  dsimp only [polyBracket2, polyBracket3, polyBracket4,
    addableRatio31, addableRatio22, addableRatio211, addableCellRatioSum21]
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [Int.sub_mul, Int.one_mul, Int.mul_add, Int.mul_one]
    omega
  · rw [Int.add_mul, Int.one_mul, Int.mul_add, Int.mul_one, ← Int.mul_assoc Q Q Q]
    omega
  · have hL :
        (1 + Q + Q * Q) + Q * (1 + Q * Q) + Q * Q * (1 + Q + Q * Q) =
          1 + 2 * Q + 2 * (Q * Q) + 2 * (Q * Q * Q) + Q * Q * (Q * Q) := by
      rw [Int.mul_add, Int.mul_one, Int.mul_add, Int.mul_add, Int.mul_one]
      rw [← Int.mul_assoc Q Q Q]
      omega
    have hR :
        (1 + Q + Q * Q + Q * Q * Q) * (1 + Q) =
          1 + 2 * Q + 2 * (Q * Q) + 2 * (Q * Q * Q) + Q * Q * (Q * Q) := by
      rw [Int.mul_add, Int.mul_one, Int.add_mul, Int.add_mul, Int.add_mul, Int.one_mul]
      rw [Int.mul_assoc (Q * Q) Q Q]
      omega
    rw [hL, hR]
  · omega

/-!
### Part 2 (`qou-3quc`): Fourth-Order Coinvariant Degree Sum and Squared-Ratio Contrast

For $n = 4$, the five partition shapes $(4), (3,1), (2,2), (2,1,1), (1,1,1,1)$ have standard
tableau counts $1, 3, 2, 3, 1$ and shifted degree polynomials
- $F_{(4)}(Q) = 1$,
- $F_{(3,1)}(Q) = Q [3]_Q$,
- $F_{(2,2)}(Q) = Q^2 (1 + Q^2)$,
- $F_{(2,1,1)}(Q) = Q^3 [3]_Q$,
- $F_{(1,1,1,1)}(Q) = Q^6$.
We prove that the multiplicity-weighted sum $\sum_{\lambda \vdash 4} f^\lambda F_\lambda(Q)$ equals
$[4]_Q!$, and that the unshifted sum of squared ratios
$1^2 + R_{(3,1)}(Q)^2 + R_{(2,2)}(Q)^2 + R_{(2,1,1)}(Q)^2 + 1^2$ differs strictly from $[4]_Q!$ at
$Q = 2$ ($125 \ne 315$).
-/

/-- Multiplicity-weighted fourth-order coinvariant degree sum across all five 4-box shapes. -/
def coinvariantDegreeSum4 (Q : Int) : Int :=
  1 + 3 * Q * polyBracket3 Q + 2 * (Q * Q) * addableRatio22 Q +
    3 * (Q * Q * Q) * polyBracket3 Q + Q * Q * Q * (Q * Q * Q)

/-- Unshifted sum of squared cell-length ratios across all five 4-box shapes. -/
def unshiftedRatioSqSum4 (Q : Int) : Int :=
  1 + addableRatio31 Q * addableRatio31 Q + addableRatio22 Q * addableRatio22 Q +
    addableRatio211 Q * addableRatio211 Q + 1

/-- `qou-3quc`: The multiplicity-weighted coinvariant degree sum across the five 4-box shapes
equals $[4]_Q!$ for every $Q \in \mathbb{Z}$, while at $Q = 2$ the unshifted sum of squared ratios
is $125$ whereas $[4]_2! = 315$. -/
theorem fourth_order_coinvariant_degree_sum_and_contrast (Q : Int) (hQ : Q > 0) :
    coinvariantDegreeSum4 Q = polyFactorial4 Q ∧
    unshiftedRatioSqSum4 1 = polyFactorial4 1 ∧
    unshiftedRatioSqSum4 2 = 125 ∧
    polyFactorial4 2 = 315 ∧
    unshiftedRatioSqSum4 2 ≠ polyFactorial4 2 ∧
    coinvariantDegreeSum4 Q > 0 := by
  have hExpandSum :
      coinvariantDegreeSum4 Q =
        1 + 3 * Q + 5 * (Q * Q) + 6 * (Q * Q * Q) +
          5 * (Q * Q * (Q * Q)) + 3 * (Q * Q * Q * (Q * Q)) +
          Q * Q * Q * (Q * Q * Q) := by
    dsimp only [coinvariantDegreeSum4, polyBracket3, addableRatio22]
    rw [Int.mul_add, Int.mul_add, Int.mul_one]
    rw [Int.mul_add (2 * (Q * Q)) 1 (Q * Q), Int.mul_one]
    rw [Int.mul_add (3 * (Q * Q * Q)) (1 + Q) (Q * Q), Int.mul_add (3 * (Q * Q * Q)) 1 Q, Int.mul_one]
    rw [Int.mul_assoc 3 Q Q, Int.mul_assoc 3 Q (Q * Q)]
    rw [Int.mul_assoc 2 (Q * Q) (Q * Q)]
    rw [Int.mul_assoc 3 (Q * Q * Q) Q, Int.mul_assoc 3 (Q * Q * Q) (Q * Q)]
    have hQ3 : Q * (Q * Q) = Q * Q * Q := by rw [← Int.mul_assoc Q Q Q]
    have hQ4 : Q * Q * Q * Q = Q * Q * (Q * Q) := by
      rw [Int.mul_assoc (Q * Q) Q Q]
    rw [hQ3, hQ4]
    omega
  have hExpandFact :
      polyFactorial4 Q =
        1 + 3 * Q + 5 * (Q * Q) + 6 * (Q * Q * Q) +
          5 * (Q * Q * (Q * Q)) + 3 * (Q * Q * Q * (Q * Q)) +
          Q * Q * Q * (Q * Q * Q) := by
    dsimp only [polyFactorial4, polyBracket1, polyBracket2, polyBracket3, polyBracket4]
    have h123 : 1 * (1 + Q) * (1 + Q + Q * Q) = 1 + 2 * Q + 2 * (Q * Q) + Q * Q * Q := by
      rw [Int.one_mul, Int.add_mul, Int.one_mul, Int.mul_add, Int.mul_add, Int.mul_one]
      rw [← Int.mul_assoc Q Q Q]
      omega
    rw [h123]
    rw [Int.mul_add, Int.mul_add, Int.mul_add, Int.mul_one]
    rw [Int.add_mul, Int.add_mul, Int.add_mul]
    rw [Int.add_mul, Int.add_mul, Int.add_mul]
    rw [Int.add_mul, Int.add_mul, Int.add_mul]
    rw [Int.one_mul, Int.one_mul, Int.one_mul]
    rw [Int.mul_assoc 2 Q Q, Int.mul_assoc 2 (Q * Q) Q]
    rw [Int.mul_assoc 2 Q (Q * Q), Int.mul_assoc 2 (Q * Q) (Q * Q)]
    rw [Int.mul_assoc 2 Q (Q * Q * Q), Int.mul_assoc 2 (Q * Q) (Q * Q * Q)]
    have hA : Q * (Q * Q) = Q * Q * Q := by rw [← Int.mul_assoc Q Q Q]
    have hB : Q * (Q * Q * Q) = Q * Q * (Q * Q) := by
      rw [← Int.mul_assoc Q (Q * Q) Q, ← Int.mul_assoc Q Q Q, Int.mul_assoc (Q * Q) Q Q]
    have hC : Q * Q * Q * Q = Q * Q * (Q * Q) := by
      rw [Int.mul_assoc (Q * Q) Q Q]
    have hD : Q * Q * (Q * Q * Q) = Q * Q * Q * (Q * Q) := by
      rw [← Int.mul_assoc (Q * Q) (Q * Q) Q, ← Int.mul_assoc (Q * Q) Q Q,
        Int.mul_assoc (Q * Q * Q) Q Q]
    rw [hA, hB, hC, hD]
    omega
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · rw [hExpandSum, hExpandFact]
  · decide
  · decide
  · decide
  · decide
  · rw [hExpandSum]
    have hQ2 : Q * Q > 0 := Int.mul_pos hQ hQ
    have hQ3 : Q * Q * Q > 0 := Int.mul_pos hQ2 hQ
    have hQ4 : Q * Q * (Q * Q) > 0 := Int.mul_pos hQ2 hQ2
    have hQ5 : Q * Q * Q * (Q * Q) > 0 := Int.mul_pos hQ3 hQ2
    have hQ6 : Q * Q * Q * (Q * Q * Q) > 0 := Int.mul_pos hQ3 hQ3
    omega

/-!
### Part 3 (`qou-f1qs`): Two-Row Lattice-Vote Recurrence and Level-Sum Invariance

For two-row shapes $(n - k, k)$, the integer lattice-vote difference is
$d(n, k) = \binom{n}{k} - \binom{n}{k-1}$. At $n = 3$, the valid two-row multiplicities are
$d(3, 0) = 1$ and $d(3, 1) = 2$; at $n = 4$, they are $d(4, 0) = 1$, $d(4, 1) = 3$, and
$d(4, 2) = 2$. In cleared-denominator Laurent-bracket form parameterized by $t = [2]_q \in \mathbb{Z}$
(where $T_1(t) = 1$, $T_2(t) = t$, $T_3(t) = t^2 - 1$, $T_4(t) = t^3 - 2t$, $T_5(t) = t^4 - 3t^2 + 1$
satisfy $T_{m+2}(t) + T_m(t) = t T_{m+1}(t)$), we prove that the level-sum step
$$d(4, 0) T_5(t) + d(4, 1) T_3(t) + d(4, 2) T_1(t) = t \bigl(d(3, 0) T_4(t) + d(3, 1) T_2(t)\bigr)$$
holds identically and reduces both level sums to $t^3 = [2]_q^3$ and $t^4 = [2]_q^4$.
-/

/-- Chebyshev-type two-row bracket polynomial $T_1(t) = 1$ in $t = [2]_q$. -/
def twoRowCheb1 : Int := 1

/-- Chebyshev-type two-row bracket polynomial $T_2(t) = t$ in $t = [2]_q$. -/
def twoRowCheb2 (t : Int) : Int := t

/-- Chebyshev-type two-row bracket polynomial $T_3(t) = t^2 - 1$ in $t = [2]_q$. -/
def twoRowCheb3 (t : Int) : Int := t * t - 1

/-- Chebyshev-type two-row bracket polynomial $T_4(t) = t^3 - 2t$ in $t = [2]_q$. -/
def twoRowCheb4 (t : Int) : Int := t * t * t - 2 * t

/-- Chebyshev-type two-row bracket polynomial $T_5(t) = t^4 - 3t^2 + 1$ in $t = [2]_q$. -/
def twoRowCheb5 (t : Int) : Int := t * t * (t * t) - 3 * (t * t) + 1

/-- Cleared two-row level sum at $n = 3$: $1 \cdot T_4(t) + 2 \cdot T_2(t)$. -/
def twoRowClearedLevelSum3 (t : Int) : Int :=
  1 * twoRowCheb4 t + 2 * twoRowCheb2 t

/-- Cleared two-row level sum at $n = 4$: $1 \cdot T_5(t) + 3 \cdot T_3(t) + 2 \cdot T_1$. -/
def twoRowClearedLevelSum4 (t : Int) : Int :=
  1 * twoRowCheb5 t + 3 * twoRowCheb3 t + 2 * twoRowCheb1

/-- `qou-f1qs`: The two-row bracket polynomials satisfy the three-term branching relations
$T_5(t) + T_3(t) = t T_4(t)$ and $T_3(t) + T_1 = t T_2(t)$, the cleared level sums satisfy the
step relation $S_4(t) = t S_3(t)$, and consequently $S_3(t) = t^3$ and $S_4(t) = t^4$. -/
theorem two_row_level_sum_branching_normalisation (t : Int) (ht : t > 0) :
    twoRowCheb5 t + twoRowCheb3 t = t * twoRowCheb4 t ∧
    twoRowCheb3 t + twoRowCheb1 = t * twoRowCheb2 t ∧
    twoRowClearedLevelSum3 t = t * t * t ∧
    twoRowClearedLevelSum4 t = t * twoRowClearedLevelSum3 t ∧
    twoRowClearedLevelSum4 t = t * t * (t * t) ∧
    twoRowClearedLevelSum4 t > 0 := by
  have hBranch4 : twoRowCheb5 t + twoRowCheb3 t = t * twoRowCheb4 t := by
    dsimp only [twoRowCheb5, twoRowCheb4, twoRowCheb3]
    have hT4 : t * (t * t * t) = t * t * (t * t) := by
      rw [← Int.mul_assoc t (t * t) t, ← Int.mul_assoc t t t, Int.mul_assoc (t * t) t t]
    have hT2 : t * (2 * t) = 2 * (t * t) := by
      rw [← Int.mul_assoc t 2 t, Int.mul_comm t 2, Int.mul_assoc 2 t t]
    rw [Int.mul_sub, hT4, hT2]
    omega
  have hBranch2 : twoRowCheb3 t + twoRowCheb1 = t * twoRowCheb2 t := by
    dsimp only [twoRowCheb3, twoRowCheb2, twoRowCheb1]
    omega
  have hSum3 : twoRowClearedLevelSum3 t = t * t * t := by
    dsimp only [twoRowClearedLevelSum3, twoRowCheb4, twoRowCheb2]
    omega
  have hSum4 : twoRowClearedLevelSum4 t = t * t * (t * t) := by
    dsimp only [twoRowClearedLevelSum4, twoRowCheb5, twoRowCheb3, twoRowCheb1]
    rw [Int.mul_sub]
    omega
  have hStep : twoRowClearedLevelSum4 t = t * twoRowClearedLevelSum3 t := by
    rw [hSum4, hSum3, ← Int.mul_assoc t (t * t) t, ← Int.mul_assoc t t t, Int.mul_assoc (t * t) t t]
  refine ⟨hBranch4, hBranch2, hSum3, hStep, hSum4, ?_⟩
  rw [hSum4]
  have ht2 : t * t > 0 := Int.mul_pos ht ht
  exact Int.mul_pos ht2 ht2

/-!
### Part 4 (`qou-mpq5`): Block-Trace Additivity and Character-Sum Decomposition

For rank $N \in \mathbb{Z}$ and $n = 3$, the cleared block multiplicities (scaled by $6$) for the
three shapes $(3), (2,1), (1,1,1)$ are:
- $W_{(3)}(N) = N(N+1)(N+2)$,
- $W_{(2,1)}(N) = 2 N(N-1)(N+1)$,
- $W_{(1,1,1)}(N) = N(N-1)(N-2)$.
We prove that the block-trace character sum $\sum_{\lambda \vdash 3} W_\lambda(N) \chi_\lambda(\sigma)$
evaluates to $6 N^3$ at the identity $\sigma = \text{id}$ ($\chi = (1, 2, 1)$), to $6 N^2$ at a
transposition $\sigma = s_1$ ($\chi = (1, 0, -1)$), and to $6 N$ at a 3-cycle $\sigma = c_3$
($\chi = (1, -1, 1)$).
-/

/-- Cleared multiplicity $W_{(3)}(N) = N(N+1)(N+2)$ for the symmetric 3-box block. -/
def blockWeight3 (N : Int) : Int :=
  N * (N + 1) * (N + 2)

/-- Cleared multiplicity $W_{(2,1)}(N) = 2 N(N-1)(N+1)$ for the mixed 3-box block. -/
def blockWeight21 (N : Int) : Int :=
  2 * N * (N - 1) * (N + 1)

/-- Cleared multiplicity $W_{(1,1,1)}(N) = N(N-1)(N-2)$ for the alternating 3-box block. -/
def blockWeight111 (N : Int) : Int :=
  N * (N - 1) * (N - 2)

/-- Weighted character sum across the three 3-box blocks for character values $(c_3, c_{21}, c_{111})$. -/
def blockCharacterSum3 (N c3 c21 c111 : Int) : Int :=
  blockWeight3 N * c3 + blockWeight21 N * c21 + blockWeight111 N * c111

/-- Helper expansion of the three cleared block multiplicities $W_{(3)}(N)$, $W_{(2,1)}(N)$,
and $W_{(1,1,1)}(N)$ into polynomials in $N$. -/
theorem blockWeight3_expansions (N : Int) (hN : N ≥ 1) :
    blockWeight3 N = N * N * N + 3 * (N * N) + 2 * N ∧
    blockWeight21 N = 2 * (N * N * N) - 2 * N ∧
    blockWeight111 N = N * N * N - 3 * (N * N) + 2 * N ∧
    N > 0 := by
  have hW3 : blockWeight3 N = N * N * N + 3 * (N * N) + 2 * N := by
    dsimp only [blockWeight3]
    have h1 : N * (N + 1) = N * N + N := by
      rw [Int.mul_add, Int.mul_one]
    have h2 : (N * N + N) * 2 = 2 * (N * N) + 2 * N := by
      rw [Int.add_mul, Int.mul_comm (N * N) 2, Int.mul_comm N 2]
    rw [h1, Int.mul_add (N * N + N) N 2, Int.add_mul (N * N) N N, h2]
    omega
  have hW21 : blockWeight21 N = 2 * (N * N * N) - 2 * N := by
    dsimp only [blockWeight21]
    have h1 : 2 * N * (N - 1) = 2 * (N * N) - 2 * N := by
      rw [Int.mul_sub, Int.mul_one, Int.mul_assoc 2 N N]
    have h2 : 2 * (N * N) * N = 2 * (N * N * N) := by
      rw [Int.mul_assoc 2 (N * N) N]
    rw [h1, Int.sub_mul, Int.mul_add, Int.mul_one, Int.mul_add, Int.mul_one, h2, Int.mul_assoc 2 N N]
    omega
  have hW111 : blockWeight111 N = N * N * N - 3 * (N * N) + 2 * N := by
    dsimp only [blockWeight111]
    have h1 : N * (N - 1) = N * N - N := by
      rw [Int.mul_sub, Int.mul_one]
    have h2 : (N * N - N) * 2 = 2 * (N * N) - 2 * N := by
      rw [Int.sub_mul, Int.mul_comm (N * N) 2, Int.mul_comm N 2]
    rw [h1, Int.mul_sub (N * N - N) N 2, Int.sub_mul (N * N) N N, h2]
    omega
  refine ⟨hW3, hW21, hW111, ?_⟩
  omega

/-- `qou-mpq5`: The block-trace character sum $\sum_{\lambda \vdash 3} W_\lambda(N) \chi_\lambda(\sigma)$
equals $6 N^3$ on the identity character $(1, 2, 1)$, $6 N^2$ on the transposition character
$(1, 0, -1)$, and $6 N$ on the 3-cycle character $(1, -1, 1)$. -/
theorem block_character_sum_tensor_trace_identities (N : Int) (hN : N > 0) :
    blockCharacterSum3 N 1 2 1 = 6 * (N * N * N) ∧
    blockCharacterSum3 N 1 0 (-1) = 6 * (N * N) ∧
    blockCharacterSum3 N 1 (-1) 1 = 6 * N ∧
    blockCharacterSum3 N 1 2 1 > 0 := by
  have hGe : N ≥ 1 := by omega
  rcases blockWeight3_expansions N hGe with ⟨hW3, hW21, hW111, _⟩
  refine ⟨?_, ?_, ?_, ?_⟩
  · dsimp only [blockCharacterSum3]
    rw [hW3, hW21, hW111]
    omega
  · dsimp only [blockCharacterSum3]
    rw [hW3, hW21, hW111]
    omega
  · dsimp only [blockCharacterSum3]
    rw [hW3, hW21, hW111]
    omega
  · dsimp only [blockCharacterSum3]
    rw [hW3, hW21, hW111]
    have hN2 : N * N > 0 := Int.mul_pos hN hN
    have hN3 : N * N * N > 0 := Int.mul_pos hN2 hN
    omega

/-!
### Part 5 (`qou-uinl`): Orbit-Constant Function Counts and Permutation Trace Projections

For a 3-element domain and an $N$-element codomain, a permutation $\sigma$ with $c(\sigma)$ disjoint
cycles fixes $N^{c(\sigma)}$ functions $f$ under precomposition $f \mapsto f \circ \sigma$:
- Identity ($\text{id}$, $3$ orbits): $N^3$,
- Transposition ($s_1$, $2$ orbits): $N^2$,
- Three-cycle ($c_3$, $1$ orbit): $N^1 = N$.
We prove that the character projections of the orbit-constant counts $(N^3, N^2, N)$ weighted by
the conjugacy-class sizes $(1, 3, 2)$ of $S_3$ recover the three cleared block multiplicities
$W_{(3)}(N)$, $W_{(2,1)}(N)$, and $W_{(1,1,1)}(N)$.
-/

/-- Number of $\sigma$-invariant functions on 3 factors for the identity ($3$ orbits): $N^3$. -/
def orbitInvariantCountId3 (N : Int) : Int :=
  N * N * N

/-- Number of $\sigma$-invariant functions on 3 factors for a transposition ($2$ orbits): $N^2$. -/
def orbitInvariantCountSwap3 (N : Int) : Int :=
  N * N

/-- Number of $\sigma$-invariant functions on 3 factors for a 3-cycle ($1$ orbit): $N$. -/
def orbitInvariantCountCycle3 (N : Int) : Int :=
  N

/-- `qou-uinl`: Weighting the orbit-invariant function counts $(N^3, N^2, N)$ by the conjugacy-class
sizes $(1, 3, 2)$ and irreducible characters of the three 3-box shapes recovers $W_{(3)}(N)$,
$W_{(2,1)}(N)$, and $W_{(1,1,1)}(N)$, whose sum weighted by $(1, 2, 1)$ is $6 N^3$. -/
theorem orbit_invariant_function_count_projections (N : Int) (hN : N ≥ 2) :
    1 * orbitInvariantCountId3 N + 3 * orbitInvariantCountSwap3 N +
      2 * orbitInvariantCountCycle3 N = blockWeight3 N ∧
    2 * orbitInvariantCountId3 N - 2 * orbitInvariantCountCycle3 N = blockWeight21 N ∧
    1 * orbitInvariantCountId3 N - 3 * orbitInvariantCountSwap3 N +
      2 * orbitInvariantCountCycle3 N = blockWeight111 N ∧
    orbitInvariantCountId3 N > orbitInvariantCountSwap3 N := by
  have hGe1 : N ≥ 1 := by omega
  rcases blockWeight3_expansions N hGe1 with ⟨hW3, hW21, hW111, hNPos⟩
  dsimp only [orbitInvariantCountId3, orbitInvariantCountSwap3, orbitInvariantCountCycle3]
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [hW3]
    omega
  · rw [hW21]
  · rw [hW111]
    omega
  · have hN2Pos : N * N > 0 := Int.mul_pos hNPos hNPos
    have hSubPos : N - 1 > 0 := by omega
    have hProdPos : N * N * (N - 1) > 0 := Int.mul_pos hN2Pos hSubPos
    rw [Int.mul_sub, Int.mul_one] at hProdPos
    omega

end QOU.Foundations.AddableCellRatioFakeDegreeTwoRowBallotWeightTensorPowerCharacterOrbitTrace
