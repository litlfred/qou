/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

namespace QOU.MassTheory.FullTowerEnergyScaleDenominatorIdentity

/-!
# Binding $E_0$ Full-Tower Denominator Identity & Bond-Content Double-Counting Pruning (`qou-v8ct`)

This module formalizes the exact algebraic identities underlying the `qou-v8ct`
audit of candidate binding energy scales $E_0$:

1. **Full-Tower Geometric Series Denominator Identity ($E_{0,\mathrm{full}}$ vs $E_{0,N_0}$):**
   - For $E_{0,N_0} = \frac{m_e}{q(q-1)}$ and $\hbar_q = \frac{q-1}{q}$, the full-tower
     geometric factor is
     $$1 - \hbar_q^2 = 1 - \frac{(q-1)^2}{q^2} = \frac{q^2 - (q-1)^2}{q^2} = \frac{2q - 1}{q^2},$$
     yielding $E_{0,\mathrm{full}} = \frac{E_{0,N_0}}{1 - \hbar_q^2} = \frac{m_e q}{(q-1)(2q-1)}$.
   - Furthermore, the cleared numerator minus denominator of the scale enhancement ratio
     $\frac{E_{0,\mathrm{full}}}{E_{0,N_0}} = \frac{q^2}{2q - 1}$ is
     $$q^2 - (2q - 1) = (q - 1)^2,$$
     which is strictly positive for any rational $q = P / Q$ with $P \neq Q$.

2. **Bond-Content Double-Counting Pruning ($b_{pp} b_{nn} = 1 / [2]_q^2$):**
   - For rational $q = P / Q$, the quantum integer $[2]_q = q + q^{-1} = \frac{P^2 + Q^2}{P Q}$
     and the single-crossing Markov bond factors
     $b_{pp} = \frac{q^2}{[2]_q} = \frac{P^3}{Q(P^2 + Q^2)}$ and
     $b_{nn} = \frac{q^{-2}}{[2]_q} = \frac{Q^3}{P(P^2 + Q^2)}$ satisfy the exact
     cross-multiplied identity
     $$\mathrm{num}(b_{pp})\,\mathrm{num}(b_{nn})\,(P^2 + Q^2)^2
       = \mathrm{den}(b_{pp})\,\mathrm{den}(b_{nn})\,P^2 Q^2,$$
     showing $b_{pp} b_{nn} = \left(\frac{P Q}{P^2 + Q^2}\right)^2 = \frac{1}{[2]_q^2}$ and
     hence $L_{pp} + L_{nn} = -\ln(b_{pp} b_{nn}) = 2 \ln [2]_q$ is already carried inside
     the bond sum $S$.
-/

private theorem int_sq_eq_mul_self (x : Int) : x ^ 2 = x * x := by
  show (1 * x) * x = x * x
  rw [Int.one_mul]

/-- Cleared numerator of $1 - \hbar_q^2 = \frac{P^2 - (P - Q)^2}{P^2}$ for $q = P / Q$ (`qou-v8ct`). -/
def oneMinusHbarSqClearedNum (P Q : Int) : Int :=
  P ^ 2 - (P - Q) ^ 2

/-- Factored linear-in-$P$ form $Q (2 P - Q)$ of $P^2 - (P - Q)^2$ (`qou-v8ct`). -/
def oneMinusHbarSqFactoredNum (P Q : Int) : Int :=
  Q * (2 * P - Q)

/-- Exact identity $P^2 - (P - Q)^2 = Q (2 P - Q)$ (`qou-v8ct`), proving that
$E_{0,\mathrm{full}} = \frac{E_{0,N_0}}{1 - \hbar_q^2} = \frac{m_e q}{(q-1)(2q-1)}$. -/
theorem oneMinusHbarSqClearedNum_eq_factored (P Q : Int) :
    oneMinusHbarSqClearedNum P Q = oneMinusHbarSqFactoredNum P Q := by
  dsimp [oneMinusHbarSqClearedNum, oneMinusHbarSqFactoredNum]
  rw [int_sq_eq_mul_self P, int_sq_eq_mul_self (P - Q)]
  rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_sub]
  rw [Int.mul_left_comm Q 2 P, Int.mul_comm Q P]
  omega

/-- Excess of the full-tower scale numerator $P^2$ over the cleared denominator
$Q(2P - Q)$ equals the perfect square $(P - Q)^2$, and is strictly positive
whenever $P > Q$ (`qou-v8ct`). -/
theorem e0Full_over_e0N0_excess_eq_sq_and_pos (P Q : Int) (hgt : P > Q) :
    P ^ 2 - oneMinusHbarSqFactoredNum P Q = (P - Q) ^ 2 ∧
      P ^ 2 - oneMinusHbarSqFactoredNum P Q > 0 := by
  have hEq : oneMinusHbarSqClearedNum P Q = oneMinusHbarSqFactoredNum P Q :=
    oneMinusHbarSqClearedNum_eq_factored P Q
  have hDiff : P ^ 2 - oneMinusHbarSqFactoredNum P Q = (P - Q) ^ 2 := by
    rw [← hEq]
    dsimp [oneMinusHbarSqClearedNum]
    omega
  refine ⟨hDiff, ?_⟩
  rw [hDiff, int_sq_eq_mul_self (P - Q)]
  have hpos : P - Q > 0 := by omega
  exact Int.mul_pos hpos hpos

/-- Cleared numerator $P^3$ of $b_{pp} = \frac{q^2}{[2]_q} = \frac{P^3}{Q(P^2+Q^2)}$ at $q = P/Q$. -/
def bPPNum (P : Int) : Int := P ^ 3

/-- Cleared denominator $Q(P^2 + Q^2)$ of $b_{pp}$ at $q = P/Q$. -/
def bPPDen (P Q : Int) : Int := Q * (P ^ 2 + Q ^ 2)

/-- Cleared numerator $Q^3$ of $b_{nn} = \frac{q^{-2}}{[2]_q} = \frac{Q^3}{P(P^2+Q^2)}$ at $q = P/Q$. -/
def bNNNum (Q : Int) : Int := Q ^ 3

/-- Cleared denominator $P(P^2 + Q^2)$ of $b_{nn}$ at $q = P/Q$. -/
def bNNDen (P Q : Int) : Int := P * (P ^ 2 + Q ^ 2)

/-- Exact cross-multiplied identity (`qou-v8ct`):
$\mathrm{num}(b_{pp})\,\mathrm{num}(b_{nn}) = P^2 Q^2 \cdot (P Q)$ and
$\mathrm{den}(b_{pp})\,\mathrm{den}(b_{nn}) = (P^2 + Q^2)^2 \cdot (P Q)$,
confirming $b_{pp} b_{nn} = \left(\frac{P Q}{P^2 + Q^2}\right)^2 = \frac{1}{[2]_q^2}$. -/
theorem bPP_mul_bNN_cleared_eq_inv_twoQ_sq (P Q : Int) :
    bPPNum P * bNNNum Q = (P ^ 2 * Q ^ 2) * (P * Q) ∧
      bPPDen P Q * bNNDen P Q = (P ^ 2 + Q ^ 2) ^ 2 * (P * Q) := by
  refine ⟨?_, ?_⟩
  · dsimp [bPPNum, bNNNum]
    show (((1 * P) * P) * P) * (((1 * Q) * Q) * Q) =
      (((1 * P) * P) * ((1 * Q) * Q)) * (P * Q)
    simp [Int.mul_left_comm, Int.mul_comm]
  · dsimp [bPPDen, bNNDen]
    rw [int_sq_eq_mul_self (P ^ 2 + Q ^ 2)]
    simp [Int.mul_assoc, Int.mul_left_comm, Int.mul_comm]

end QOU.MassTheory.FullTowerEnergyScaleDenominatorIdentity
