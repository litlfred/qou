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
**Convention (agreed 2026-11-27 with the per-fermion braid words thread, PR #9811):** matter is
the EVEN part `Λ^even K⁵ = Λ⁰ ⊕ Λ² ⊕ Λ⁴ = 1 ⊕ 10 ⊕ 5̄`, one Standard Model generation plus a
singlet (the Spin(10) `16`).  The odd part `Λ¹ ⊕ Λ³ ⊕ Λ⁵ = 5 ⊕ 10̄ ⊕ 1` is its conjugate.  Which
half is matter is notation; deriving the chirality is open (bean `qou-qvpl`).

Both halves are anomaly-free for a traceless charge: `evenExterior_linear` / `evenExterior_cubic`
for matter, `oddExterior_linear` / `oddExterior_cubic` for the conjugate.  The sum over all 32
states has cubic `p₁ (4 p₁² + 12 p₂)`, so the even cubic is `p₁ (2 p₁² + 6 p₂)` as well.  The mixed anomalies are the `2 + 3` specialisation,
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

/-- The even subsets of `Fin 5`: the basis of `Λ^even K⁵ = 1 ⊕ 10 ⊕ 5̄` (matter). -/
def evenSubsets : Finset (Finset (Fin 5)) :=
  (univ : Finset (Fin 5)).powerset.filter (fun S => Even S.card)

theorem evenSubsets_eq : evenSubsets =
    {∅, {0,1}, {0,2}, {0,3}, {0,4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4},
     {0,1,2,3}, {0,1,2,4}, {0,1,3,4}, {0,2,3,4}, {1,2,3,4}} := by
  decide +kernel

/-- `∑_{|S| even} f(y_S)`, written out over the sixteen states. -/
theorem sum_evenSubsets (y : Fin 5 → K) (f : K → K) :
    ∑ S ∈ evenSubsets, f (stateCharge y S) =
      f 0 + f (y 0 + y 1) + f (y 0 + y 2) + f (y 0 + y 3) + f (y 0 + y 4)
      + f (y 1 + y 2) + f (y 1 + y 3) + f (y 1 + y 4) + f (y 2 + y 3) + f (y 2 + y 4)
      + f (y 3 + y 4) + f (y 0 + y 1 + y 2 + y 3) + f (y 0 + y 1 + y 2 + y 4)
      + f (y 0 + y 1 + y 3 + y 4) + f (y 0 + y 2 + y 3 + y 4) + f (y 1 + y 2 + y 3 + y 4) := by
  rw [evenSubsets_eq]
  simp (disch := decide) only [Finset.sum_insert, Finset.sum_singleton, stateCharge,
    Finset.sum_empty]
  simp only [add_assoc]

theorem evenExterior_linear_eq (y : Fin 5 → K) :
    ∑ S ∈ evenSubsets, stateCharge y S = 8 * ∑ i, y i := by
  have := sum_evenSubsets y id
  simp only [id] at this
  rw [this, Fin.sum_univ_five]; ring

/-- **Gravitational anomaly of matter `Λ^even`** vanishes for a traceless charge. -/
theorem evenExterior_linear (y : Fin 5 → K) (htr : ∑ i, y i = 0) :
    ∑ S ∈ evenSubsets, stateCharge y S = 0 := by
  rw [evenExterior_linear_eq, htr, mul_zero]

theorem evenExterior_cubic_eq (y : Fin 5 → K) :
    ∑ S ∈ evenSubsets, stateCharge y S ^ 3 =
      (∑ i, y i) * (2 * (∑ i, y i) ^ 2 + 6 * ∑ i, y i ^ 2) := by
  rw [sum_evenSubsets y (· ^ 3), Fin.sum_univ_five, Fin.sum_univ_five]; ring

/-- **Cubic anomaly of matter `Λ^even`** vanishes for a traceless charge. -/
theorem evenExterior_cubic (y : Fin 5 → K) (htr : ∑ i, y i = 0) :
    ∑ S ∈ evenSubsets, stateCharge y S ^ 3 = 0 := by
  rw [evenExterior_cubic_eq, htr, zero_mul]

/-! ## Complementation: the even part is the conjugate of the odd part

The even subsets are the basis of `Λ^even K⁵ = Λ⁰ ⊕ Λ² ⊕ Λ⁴`.  Complementation `S ↦ Sᶜ` swaps
the even and odd parts (five is odd) and, for a traceless charge, negates the charge.  So the
even part is the charge conjugate of the odd part, state by state: with colour first this is
`1 ⊕ 10 ⊕ 5̄`, one Standard Model generation plus a singlet, and the odd part is its conjugate.
Which of the two is "matter" is one `ℤ/2` sign (the chirality); it is **not** derived here
(bean `qou-h0zz`).  Neither part contains both a `Λ¹` and a `Λ⁴` state, so neither contains a
vector-like `5 ⊕ 5̄`. -/

theorem card_evenSubsets : evenSubsets.card = 16 := by decide +kernel

/-- By degree, the even part is `1 + 10 + 5` and has no degree-`1` state. -/
theorem evenSubsets_by_degree :
    (evenSubsets.filter fun S => S.card = 0).card = 1 ∧
    (evenSubsets.filter fun S => S.card = 2).card = 10 ∧
    (evenSubsets.filter fun S => S.card = 4).card = 5 ∧
    (evenSubsets.filter fun S => S.card = 1).card = 0 := by decide +kernel

/-- By degree, the odd part is `5 + 10 + 1` and has no degree-`4` state. -/
theorem oddSubsets_by_degree :
    (oddSubsets.filter fun S => S.card = 1).card = 5 ∧
    (oddSubsets.filter fun S => S.card = 3).card = 10 ∧
    (oddSubsets.filter fun S => S.card = 5).card = 1 ∧
    (oddSubsets.filter fun S => S.card = 4).card = 0 := by decide +kernel

/-- Complementation swaps the even and odd parts. -/
theorem mem_evenSubsets_iff_compl_mem_odd (S : Finset (Fin 5)) :
    S ∈ evenSubsets ↔ Sᶜ ∈ oddSubsets := by
  revert S; decide +kernel

theorem evenSubsets_image_compl : evenSubsets.image (fun S => Sᶜ) = oddSubsets := by
  decide +kernel

/-- For a traceless charge, the complementary state carries the opposite charge. -/
theorem stateCharge_compl (y : Fin 5 → K) (htr : ∑ i, y i = 0) (S : Finset (Fin 5)) :
    stateCharge y Sᶜ = -stateCharge y S := by
  unfold stateCharge
  have h := Finset.sum_add_sum_compl S y
  rw [htr] at h
  linear_combination h

/-- The degree-`4` state missing `j` carries `-y j`: `Λ⁴` is the conjugate of `Λ¹`. -/
theorem stateCharge_compl_singleton (y : Fin 5 → K) (htr : ∑ i, y i = 0) (j : Fin 5) :
    stateCharge y ({j} : Finset (Fin 5))ᶜ = -y j := by
  rw [stateCharge_compl y htr]; simp [stateCharge]

/-- Any sum over the even part is the sum over the odd part of the conjugate charges. -/
theorem sum_evenSubsets_eq_neg_odd (y : Fin 5 → K) (htr : ∑ i, y i = 0) (f : K → K) :
    ∑ S ∈ evenSubsets, f (stateCharge y S) =
      ∑ S ∈ oddSubsets, f (-stateCharge y S) := by
  rw [← evenSubsets_image_compl, Finset.sum_image (fun a _ b _ h => compl_injective h)]
  refine Finset.sum_congr rfl fun S _ => ?_
  rw [stateCharge_compl y htr, neg_neg]

end QOU.StandardModel.OddExterior
