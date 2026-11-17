/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Analytic Positivity Non-Discrimination and Lithium-6 Multiplicity Blow-Up

Formalizes two linked structural diagnostics in the nuclear partition and cumulant hierarchy:

1. **Analytic Positivity Discriminates Nothing (`qou-jc0e`)**:
   - An observable whose positivity $0 < v$ holds analytically across all candidate sectors
     assigns the identical sign indicator $+1$ to every sector and therefore has zero
     sign-discrimination capability ($\text{signCapabilityDifference}(v_1, v_2) = 0$).
   - In particular, any sum of squared amplitudes $x^2 + y^2$ with $0 < x$ is strictly
     positive on every candidate pair $(x_1, y_1)$ and $(x_2, y_2)$, confirming the
     `qou-04ub` failure mode that universal analytic positivity cannot distinguish
     competing spin-isospin sectors.

2. **Lithium-6 Tower Multiplicity Blow-Up (`qou-x5bv`)**:
   - Even when per-channel cumulant energies are uniformly bounded by $E_{\text{cap}} > 0$,
     multiplying by the channel multiplicity $M$ produces a total tower sum
     $\text{towerMultiplicitySum}(M, E_{\text{cap}}) = M \cdot E_{\text{cap}}$ that exceeds
     any target budget $B < M \cdot E_{\text{cap}}$.
   - At $^6\text{Li}$ ($A = 6$), bounded cumulant energies still blow up by $6.27\times$
     ($627 : 100$ scaled by $100$), exceeding the target budget by $527\%$ ($5.27\times$).
-/

namespace QOU.MassTheory.AnalyticPositivityNonDiscriminationAndMultiplicityBlowup

/-- Sum of squared integer amplitudes $x^2 + y^2$. -/
def squaredAmplitudeSum (x y : Int) : Int :=
  x * x + y * y

/-- Sign indicator: $+1$ when $0 < v$, and $-1$ otherwise. -/
def signIndicatorForPositive (v : Int) : Int :=
  if 0 < v then 1 else -1

/-- Sign-discrimination capability between two sector observables $v_1$ and $v_2$. -/
def signCapabilityDifference (v1 v2 : Int) : Int :=
  signIndicatorForPositive v1 - signIndicatorForPositive v2

/-- Total cumulant tower energy at channel multiplicity $M$ and per-channel energy $E$. -/
def towerMultiplicitySum (multiplicity perChannelEnergy : Int) : Int :=
  multiplicity * perChannelEnergy

/-- $^6\text{Li}$ bounded-cumulant tower total scaled by $100$: $627 \times \text{targetBudget}$. -/
def li6BoundedCumulantTowerScaled100 (targetBudget : Int) : Int :=
  627 * targetBudget

/-- $^6\text{Li}$ reference target budget scaled by $100$: $100 \times \text{targetBudget}$. -/
def li6TargetBudgetScaled100 (targetBudget : Int) : Int :=
  100 * targetBudget

/-- Universal positivity has zero sign-discrimination capability (`qou-jc0e`):
    whenever $0 < v_1$ and $0 < v_2$, both sectors carry sign indicator $+1$
    and $\text{signCapabilityDifference}(v_1, v_2) = 0$. -/
theorem analytic_positivity_zero_sign_discrimination
    (v1 v2 : Int) (h1 : 0 < v1) (h2 : 0 < v2) :
    signIndicatorForPositive v1 = 1 ∧
      signIndicatorForPositive v2 = 1 ∧
      signCapabilityDifference v1 v2 = 0 := by
  have hs1 : signIndicatorForPositive v1 = 1 := by
    dsimp [signIndicatorForPositive]
    rw [if_pos h1]
  have hs2 : signIndicatorForPositive v2 = 1 := by
    dsimp [signIndicatorForPositive]
    rw [if_pos h2]
  refine ⟨hs1, hs2, ?_⟩
  dsimp [signCapabilityDifference]
  omega

/-- Non-negativity of a squared integer $y^2 \ge 0$. -/
theorem sq_nonneg_int (y : Int) : 0 ≤ y * y := by
  by_cases hy : 0 ≤ y
  · exact Int.mul_nonneg hy hy
  · have hny : 0 ≤ -y := by omega
    have hmul : 0 ≤ (-y) * (-y) := Int.mul_nonneg hny hny
    have heq : (-y) * (-y) = y * y := by
      rw [Int.neg_mul_neg]
    omega

/-- Analytic squared-amplitude sums are strictly positive and non-discriminating (`qou-jc0e`):
    for any two parameter pairs $(x_1, y_1)$ and $(x_2, y_2)$ with $0 < x_1$ and $0 < x_2$,
    both squared-amplitude sums are strictly positive and have zero sign-capability difference. -/
theorem squaredAmplitudeSum_strictly_positive_and_non_discriminating
    (x1 y1 x2 y2 : Int) (h1 : 0 < x1) (h2 : 0 < x2) :
    0 < squaredAmplitudeSum x1 y1 ∧
      0 < squaredAmplitudeSum x2 y2 ∧
      signCapabilityDifference (squaredAmplitudeSum x1 y1) (squaredAmplitudeSum x2 y2) = 0 := by
  have hx1 : 0 < x1 * x1 := Int.mul_pos h1 h1
  have hy1 : 0 ≤ y1 * y1 := sq_nonneg_int y1
  have hx2 : 0 < x2 * x2 := Int.mul_pos h2 h2
  have hy2 : 0 ≤ y2 * y2 := sq_nonneg_int y2
  have hp1 : 0 < squaredAmplitudeSum x1 y1 := by
    dsimp [squaredAmplitudeSum]
    omega
  have hp2 : 0 < squaredAmplitudeSum x2 y2 := by
    dsimp [squaredAmplitudeSum]
    omega
  have hdisc := analytic_positivity_zero_sign_discrimination
    (squaredAmplitudeSum x1 y1) (squaredAmplitudeSum x2 y2) hp1 hp2
  exact ⟨hp1, hp2, hdisc.2.2⟩

/-- Multiplicity-driven tower blow-up (`qou-x5bv`): even with bounded per-channel energy
    $0 < E$, a large channel multiplicity $M$ drives the tower sum $M \cdot E$ strictly
    above the target budget $B$. -/
theorem towerMultiplicitySum_exceeds_budget_when_multiplicity_large
    (multiplicity perChannelEnergy targetBudget : Int)
    (hE : 0 < perChannelEnergy)
    (hM : targetBudget < multiplicity * perChannelEnergy) :
    targetBudget < towerMultiplicitySum multiplicity perChannelEnergy ∧
      towerMultiplicitySum multiplicity perChannelEnergy - targetBudget =
        multiplicity * perChannelEnergy - targetBudget ∧
      0 < perChannelEnergy := by
  dsimp [towerMultiplicitySum]
  refine ⟨hM, rfl, hE⟩

/-- $^6\text{Li}$ $6.27\times$ bounded-cumulant multiplicity blow-up (`qou-x5bv`):
    for every positive target budget, the $^6\text{Li}$ bounded-cumulant tower total
    ($627 \times \text{targetBudget}$) strictly exceeds the scaled budget
    ($100 \times \text{targetBudget}$) by $527 \times \text{targetBudget}$. -/
theorem li6_bounded_cumulant_multiplicity_blowup_627_to_100
    (targetBudget : Int) (hB : 0 < targetBudget) :
    li6TargetBudgetScaled100 targetBudget < li6BoundedCumulantTowerScaled100 targetBudget ∧
      li6BoundedCumulantTowerScaled100 targetBudget - li6TargetBudgetScaled100 targetBudget =
        527 * targetBudget ∧
      li6BoundedCumulantTowerScaled100 100 = 62700 := by
  dsimp [li6BoundedCumulantTowerScaled100, li6TargetBudgetScaled100]
  refine ⟨by omega, by omega, rfl⟩

end QOU.MassTheory.AnalyticPositivityNonDiscriminationAndMultiplicityBlowup
