/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under CC BY 4.0 as described in the repository LICENSE.
-/
import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.VecNotation

/-!
# The odd exterior algebra of a traceless charge is anomaly-free

Bean `qou-qvpl` (hypercharge, Open Check A).  `AnomalyFreeHyperchargeUniqueness.lean` shows that
anomaly freedom plus a neutral lepton forces the Standard Model hypercharges, and that the
solution is the `5̄ ⊕ Λ²5` pattern.  This file proves the converse direction one level up:
anomaly freedom is a property of the **odd exterior algebra**, not of the particular charges.

Let `y : Fin 5 → K` be any diagonal charge with `∑ yᵢ = 0`.  A basis state of `Λ^odd K⁵` is an
odd subset `S ⊆ {0,…,4}` and carries the charge `y_S = ∑_{i∈S} yᵢ`.  Then

* `oddExterior_linear` : `∑_{|S| odd} y_S = 0` (gravitational anomaly),
* `oddExterior_cubic`  : `∑_{|S| odd} y_S³ = 0` (cubic anomaly).

Neither uses the `2 + 3` split of `K⁵ = V ⊕ W*`: both hold for every traceless diagonal charge.
So once the matter content is `Λ^odd(V ⊕ W*)` (`Λ¹ ⊕ Λ³ ⊕ Λ⁵ = 5 ⊕ 10̄ ⊕ 1`, the conjugate of one
Standard Model generation plus a singlet) and the hypercharge is traceless, the two `U(1)`-only
anomalies cancel with no further input.  The mixed anomalies are the `2 + 3` specialisation,
already proved in `exterior_su5_anomaly_identities`.

What remains open for Open Check A is therefore the single structural input "matter is
`Λ^odd(V ⊕ W*)`", plus the construction of `W` (bean `qou-j3w6`).

No measured values.
-/

namespace QOU.StandardModel.OddExterior

open Finset

/-- The odd subsets of `Fin 5`: the basis of `Λ^odd K⁵`. -/
def oddSubsets : Finset (Finset (Fin 5)) :=
  (univ : Finset (Fin 5)).powerset.filter (fun S => Odd S.card)

/-- The sixteen odd subsets, listed. -/
theorem oddSubsets_eq : oddSubsets =
    {{0}, {1}, {2}, {3}, {4},
     {0,1,2}, {0,1,3}, {0,1,4}, {0,2,3}, {0,2,4}, {0,3,4},
     {1,2,3}, {1,2,4}, {1,3,4}, {2,3,4}, {0,1,2,3,4}} := by
  decide +kernel

theorem card_oddSubsets : oddSubsets.card = 16 := by
  rw [oddSubsets_eq]; decide +kernel

variable {K : Type*} [CommRing K]

/-- The charge of the basis state `e_S`. -/
def stateCharge (y : Fin 5 → K) (S : Finset (Fin 5)) : K := ∑ i ∈ S, y i

/-- `∑_{|S| odd} f(y_S)`, written out over the sixteen states. -/
theorem sum_oddSubsets (y : Fin 5 → K) (f : K → K) :
    ∑ S ∈ oddSubsets, f (stateCharge y S) =
      f (y 0) + f (y 1) + f (y 2) + f (y 3) + f (y 4)
      + f (y 0 + y 1 + y 2) + f (y 0 + y 1 + y 3) + f (y 0 + y 1 + y 4)
      + f (y 0 + y 2 + y 3) + f (y 0 + y 2 + y 4) + f (y 0 + y 3 + y 4)
      + f (y 1 + y 2 + y 3) + f (y 1 + y 2 + y 4) + f (y 1 + y 3 + y 4)
      + f (y 2 + y 3 + y 4) + f (y 0 + y 1 + y 2 + y 3 + y 4) := by
  rw [oddSubsets_eq]
  simp (disch := decide) only [Finset.sum_insert, Finset.sum_singleton, stateCharge]
  simp only [add_assoc]

/-- **Gravitational anomaly of `Λ^odd`.**  `∑_{|S| odd} y_S = 8 ∑ yᵢ`, so it vanishes when the
charge is traceless. -/
theorem oddExterior_linear_eq (y : Fin 5 → K) :
    ∑ S ∈ oddSubsets, stateCharge y S = 8 * ∑ i, y i := by
  have := sum_oddSubsets y id
  simp only [id] at this
  rw [this, Fin.sum_univ_five]; ring

theorem oddExterior_linear (y : Fin 5 → K) (htr : ∑ i, y i = 0) :
    ∑ S ∈ oddSubsets, stateCharge y S = 0 := by
  rw [oddExterior_linear_eq, htr, mul_zero]

/-- **Cubic anomaly of `Λ^odd`.**  With `p₁ = ∑ yᵢ`, `p₂ = ∑ yᵢ²`, the odd cubic sum is
`p₁ (2 p₁² + 6 p₂)`, a multiple of `p₁`: the `p₃` coefficient `4 − 6 + 2` is zero. -/
theorem oddExterior_cubic_eq (y : Fin 5 → K) :
    ∑ S ∈ oddSubsets, stateCharge y S ^ 3 =
      (∑ i, y i) * (2 * (∑ i, y i) ^ 2 + 6 * ∑ i, y i ^ 2) := by
  rw [sum_oddSubsets y (· ^ 3), Fin.sum_univ_five, Fin.sum_univ_five]; ring

theorem oddExterior_cubic (y : Fin 5 → K) (htr : ∑ i, y i = 0) :
    ∑ S ∈ oddSubsets, stateCharge y S ^ 3 = 0 := by
  rw [oddExterior_cubic_eq, htr, zero_mul]

/-- **The `2 + 3` specialisation.**  On `V ⊕ W*` with charges `(y₂, y₂, y₃, y₃, y₃)` the sixteen
odd states carry exactly the charges `y₂ (×2), y₃ (×3)` of `5`, `2y₂+y₃ (×3), y₂+2y₃ (×6),
3y₃ (×1)` of `Λ³5`, and `2y₂+3y₃` of `Λ⁵5`; under tracelessness these are the negatives of
`L, d^c, e^c, Q, u^c, ν^c` in the `5̄ ⊕ Λ²5 ⊕ 1` pattern (`3y₃ = -2y₂`, `2y₂ + y₃ = -2y₃`). -/
def splitCharge (y2 y3 : K) : Fin 5 → K := ![y2, y2, y3, y3, y3]

theorem splitCharge_traceless (y2 y3 : K) :
    (∑ i, splitCharge y2 y3 i = 0) ↔ 2 * y2 + 3 * y3 = 0 := by
  simp [splitCharge, Fin.sum_univ_five]
  constructor <;> intro h <;> linear_combination h

theorem split_cubic (y2 y3 : K) (htr : 2 * y2 + 3 * y3 = 0) :
    ∑ S ∈ oddSubsets, stateCharge (splitCharge y2 y3) S ^ 3 = 0 :=
  oddExterior_cubic _ ((splitCharge_traceless y2 y3).2 htr)

end QOU.StandardModel.OddExterior
