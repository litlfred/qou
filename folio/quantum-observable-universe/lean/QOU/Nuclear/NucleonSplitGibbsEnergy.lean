import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

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

## What is proved

1. `logZ_split`: `log Z_n − log Z_p = −2·log q` for **every** positive common factor `s(q)`
   (trace, normalisation, tower factor, spectator strands): all orders in `q`.
2. `logZ_split_hasDerivAt`: its `q`-derivative is `−2/q`, again for every `s`.
3. So the split depends on the temperature only through the parametrisation `β = b(q)`.
   With `b' ≠ 0` the chain rule gives `ΔF = 2·log q / b(q)` and `ΔU = 2/(q·b'(q))`
   (`fSplit`, `uSplit`). Four corpus parametrisations, each with its derivative checked:
   * dictionary `b = log q` (`prop:beta-eq-ln-q-dictionary`): `ΔU = ΔF = 2`, `TΔS = 0`;
   * natural units `b = q/(q−1)` (`def:quantum-temperature`): `ΔU = −2(q−1)²/q`;
   * CAL-1 units, order-zero `b = 1/E₀ = q(q−1)`: `ΔU = 2/(q(2q−1))`;
   * CAL-1 units, tower `b = 1/E₀^tower = (q−1)(2q−1)/q`: `ΔU = 2q/(2q²−1)`.
4. `uT_lt_fT`, `uTower_lt_fTower`, `uNat_neg`: for every `q > 1` the two CAL-1 internal-energy
   splits lie strictly below their free-energy splits (`TΔS = ΔU − ΔF < 0`: the neutron sector
   carries less entropy than the proton one in these units), and the natural-unit one is
   negative.

## Where the parts live

This module holds the internal-energy split `uSplit` and its closed forms (`uNat_eq`, `uT_eq`,
`uTower_eq`, `uNat_neg`) over any ordered field: they are rational in `q`. The partition
functions `log Z`, the free-energy split `fSplit`, the derivatives of the four parametrisations
and the comparisons with `log q` (`logZ_split`, `logZ_split_hasDerivAt`, `dictionary_U_eq_F`,
`uT_lt_fT`, `uTower_lt_fTower`) use `Real.log` and calculus, and live behind the transcendental
boundary in `QOU.Transcendental.Nuclear.NucleonSplitGibbsEnergyAnalytic` (same namespace).

## What is NOT claimed

* Which of `F` and `U` is a mass. That is the reading, recorded as a fork in the audit.
* Which parametrisation is the temperature. `F` is the same in all of them (in each one's own
  unit); `U` is not, because the energy unit of the dictionary and of natural units moves with
  `q`. No measured value appears in this file.
-/

namespace QOU.QBeta.NucleonSplitGibbsEnergy

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Internal-energy split `ΔU = −d(log Z_n − log Z_p)/dβ = −(−2/q)/b'(q)` (chain rule). -/
def uSplit (b' q : K) : K := -(-2 / q) / b'

/-! ## Internal-energy splits of the corpus temperatures

`b'` is the derivative of the parametrisation `β = b(q)`; the derivatives themselves are checked
in `QOU.Transcendental.Nuclear.NucleonSplitGibbsEnergyAnalytic`. -/

/-- Natural units, `β_q = q/(q−1)`: `ΔU = −2(q−1)²/q`. -/
theorem uNat_eq (q : K) (hq : 1 < q) :
    uSplit (-1 / (q - 1) ^ 2) q = -2 * (q - 1) ^ 2 / q := by
  have h1 : q - 1 ≠ 0 := by linarith
  have h0 : q ≠ 0 := by linarith
  unfold uSplit; field_simp

theorem uNat_neg (q : K) (hq : 1 < q) : uSplit (-1 / (q - 1) ^ 2) q < 0 := by
  rw [uNat_eq q hq]
  have h1 : 0 < q - 1 := by linarith
  have h0 : 0 < q := by linarith
  have : 0 < 2 * (q - 1) ^ 2 / q := div_pos (by positivity) h0
  linarith [show -2 * (q - 1) ^ 2 / q = -(2 * (q - 1) ^ 2 / q) by ring]

/-- CAL-1 units, order zero (`β = 1/E₀ = q(q−1)`): `ΔF = 2 log q/(q(q−1))`, `ΔU = 2/(q(2q−1))`. -/
theorem uT_eq (q : K) (hq : 1 < q) : uSplit (2 * q - 1) q = 2 / (q * (2 * q - 1)) := by
  have h0 : q ≠ 0 := by linarith
  have h2 : 2 * q - 1 ≠ 0 := by linarith
  unfold uSplit; field_simp

/-- CAL-1 units, tower (`β = 1/E₀^tower = (q−1)(2q−1)/q`): `ΔU = 2q/(2q²−1)`. -/
theorem uTower_eq (q : K) (hq : 1 < q) :
    uSplit ((2 * q ^ 2 - 1) / q ^ 2) q = 2 * q / (2 * q ^ 2 - 1) := by
  have h0 : q ≠ 0 := by linarith
  have h2 : 2 * q ^ 2 - 1 ≠ 0 := by nlinarith
  unfold uSplit; field_simp

end Ordered

end QOU.QBeta.NucleonSplitGibbsEnergy
