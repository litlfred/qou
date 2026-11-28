import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The Gibbs map: free energy, internal energy and entropy of the nucleon split

Thread "Derive the neutron-proton mass split", 2026-11-27 (beans `qou-myts`, `qou-99qc`).
Pre-registration: `computations/probes/nucleon_split_gibbs_energy/PREREGISTRATION.md`.
Audit: `docs/audits/2026-11-27-nucleon-split-gibbs-energy.md`.

## Setting

`SpectatorEnergyMap` reads the nucleon value `ε_N = K_N·t(q)/D(q)` (K-weight `q` on the
proton weight space, `q⁻¹` on the neutron one; `t` the common weight-space trace,
`HeckeWeightSpaceSymmetry`) as a partition function, and the map `m = −kT·log ε` as a
mass. That is the Helmholtz free energy `F = −log Z/β`. The internal energy is
`U = −∂ log Z/∂β` and `F = U − TS`.

## Where the parts live

This module holds the algebraic internal-energy split `uSplitUnit` and its closed forms
(`uNat_eq_unit`, `uNat_neg_unit`, `uT_eq_unit`, `uTower_eq_unit`) over any strict ordered
commutative ring with `Kˣ` units (§7c base-ring discipline; zero field binders or division
tactics). The real division wrapper `uSplit` and the `Real.log` / calculus comparisons live
behind the transcendental boundary in `QOU.Transcendental.Nuclear.NucleonSplitGibbsEnergyAnalytic`
(same namespace). No measured value appears in this file.
-/

namespace QOU.QBeta.NucleonSplitGibbsEnergy

section Algebraic

variable {K : Type*} [CommRing K]

/-- Internal-energy split `ΔU = 2 · q⁻¹ · (b')⁻¹` over a commutative ring for invertible `b', q : Kˣ`. -/
def uSplitUnit (b' q : Kˣ) : K := 2 * (↑q⁻¹ : K) * (↑b'⁻¹ : K)

/-- Natural units, `β_q = q/(q−1)` (`b' · (q − 1)² = −1`): `ΔU = −2(q−1)² · q⁻¹`. -/
theorem uNat_eq_unit (bNat q : Kˣ) (hbNat : (bNat : K) * ((q : K) - 1) ^ 2 = -1) :
    uSplitUnit bNat q = -2 * ((q : K) - 1) ^ 2 * (↑q⁻¹ : K) := by
  unfold uSplitUnit
  have hm : (bNat : K) * (↑bNat⁻¹ : K) = 1 := Units.mul_inv bNat
  have hinv : (↑bNat⁻¹ : K) = -((q : K) - 1) ^ 2 := by
    linear_combination -((q : K) - 1) ^ 2 * hm + (↑bNat⁻¹ : K) * hbNat
  rw [hinv]
  ring

/-- CAL-1 units, order zero (`b' = 2q − 1`): `ΔU = 2 · q⁻¹ · (2q − 1)⁻¹`. -/
theorem uT_eq_unit (bT q : Kˣ) :
    uSplitUnit bT q = 2 * ((↑q⁻¹ : K) * (↑bT⁻¹ : K)) := by
  unfold uSplitUnit
  ring

/-- CAL-1 units, tower (`b' · q² = 2q² − 1`): `ΔU = 2q · (2q² − 1)⁻¹`. -/
theorem uTower_eq_unit (bTow u2q2 q : Kˣ)
    (hbTow : (bTow : K) * (q : K) ^ 2 = (u2q2 : K)) :
    uSplitUnit bTow q = 2 * (q : K) * (↑u2q2⁻¹ : K) := by
  unfold uSplitUnit
  have hq : (q : K) * (↑q⁻¹ : K) = 1 := Units.mul_inv q
  have hb : (bTow : K) * (↑bTow⁻¹ : K) = 1 := Units.mul_inv bTow
  have hu : (u2q2 : K) * (↑u2q2⁻¹ : K) = 1 := Units.mul_inv u2q2
  have hinv : (↑bTow⁻¹ : K) = (q : K) ^ 2 * (↑u2q2⁻¹ : K) := by
    linear_combination
      ((q : K) ^ 2 * (↑u2q2⁻¹ : K)) * hb -
        ((↑bTow⁻¹ : K) * (↑u2q2⁻¹ : K)) * hbTow -
        (↑bTow⁻¹ : K) * hu
  rw [hinv]
  linear_combination 2 * ((q : K) * (↑u2q2⁻¹ : K)) * hq

end Algebraic

section Ordered

variable {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]

theorem unit_inv_pos (u : Kˣ) (hu : 0 < (u : K)) : 0 < (↑u⁻¹ : K) := by
  by_contra h
  push_neg at h
  have hmul : (u : K) * (↑u⁻¹ : K) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hu.le h
  rw [Units.mul_inv u] at hmul
  linarith [zero_lt_one (α := K)]

theorem uNat_neg_unit (bNat q : Kˣ) (hq : 1 < (q : K))
    (hbNat : (bNat : K) * ((q : K) - 1) ^ 2 = -1) :
    uSplitUnit bNat q < 0 := by
  rw [uNat_eq_unit bNat q hbNat]
  have h1 : 0 < (q : K) - 1 := by linarith
  have h0 : 0 < (q : K) := by linarith
  have hinv : 0 < (↑q⁻¹ : K) := unit_inv_pos q h0
  have hpos : 0 < 2 * ((q : K) - 1) ^ 2 * (↑q⁻¹ : K) :=
    mul_pos (mul_pos (by norm_num) (sq_pos_of_pos h1)) hinv
  linarith [show -2 * ((q : K) - 1) ^ 2 * (↑q⁻¹ : K) =
      -(2 * ((q : K) - 1) ^ 2 * (↑q⁻¹ : K)) by ring]

end Ordered

end QOU.QBeta.NucleonSplitGibbsEnergy
