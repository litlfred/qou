import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination

/-!
# Normalisation of the lepton strands (issue #8833, front 1)

The ruled D1 nucleon rule divides the quantum trace by `[2]^3` on three strands whose closure
has three components. Extending it to a process word with lepton strands needs a normalisation.
This file records the two algebraic facts that decide it, given the premises stated in
`computations/probes/qbeta_lepton_normalisation/PREREGISTRATION.md`:

* (N1) agreement with D1 on the nucleon (`n = c = 3`);
* (N2) a split idle unknot strand leaves the value unchanged;
* (N3) Markov stabilisation (one more strand, same components, framing corrected) leaves the
  value unchanged.

Within normalisations `[2]^(-(α n + β c))`, (N1) and (N3) force `α = 0`, `β = 1`, and (N2)
then holds (`normExponent_forced`, `spectator_of_forced`). A lepton strand restricted to one
weight sector contributes `q^{±1}/[2]`, never `1` (`sector_idle_ne_one`, `sector_idle_inv_ne_one`),
so a restricted lepton sector cannot satisfy (N2); summing the sectors gives `(q + q⁻¹)/[2] = 1`
(`summed_idle_eq_one`).

All statements are over a generic field; no ordering or real number is used.
-/

namespace QOU.QBeta.LeptonStrandNormalisation

/-- The exponent of `[2]` in a normalisation `[2]^(-(α n + β c))`. -/
def normExponent (α β : ℤ) (n c : ℤ) : ℤ := α * n + β * c

/-- (N1) and (N3) force the per-component normalisation: `α = 0`, `β = 1`. -/
theorem normExponent_forced (α β : ℤ)
    (hN1 : normExponent α β 3 3 = 3)
    (hN3 : ∀ n c : ℤ, normExponent α β (n + 1) c = normExponent α β n c) :
    α = 0 ∧ β = 1 := by
  have h := hN3 0 0
  simp only [normExponent] at h hN1
  constructor <;> omega

/-- With `α = 0`, `β = 1`, adding one strand that is one more component (an idle unknot)
raises the exponent by exactly one, matching the factor `[2]` its summed trace contributes. -/
theorem spectator_of_forced (n c : ℤ) :
    normExponent 0 1 (n + 1) (c + 1) = normExponent 0 1 n c + 1 := by
  simp only [normExponent]; ring

variable {R : Type*} [Field R]

/-- Summed over both weights, an idle strand contributes `(q + q⁻¹)/[2] = 1`. -/
theorem summed_idle_eq_one (q : R) (h2 : q + q⁻¹ ≠ 0) :
    (q + q⁻¹) / (q + q⁻¹) = 1 := div_self h2

/-- Restricted to the weight-`q` sector, an idle strand contributes `q/[2] ≠ 1`. -/
theorem sector_idle_ne_one (q : R) (hq : q ≠ 0) (h2 : q + q⁻¹ ≠ 0) :
    q / (q + q⁻¹) ≠ 1 := by
  intro h
  rw [div_eq_one_iff_eq h2] at h
  have : q⁻¹ = 0 := by linear_combination -h
  exact hq (inv_eq_zero.mp this)

/-- Restricted to the weight-`q⁻¹` sector, an idle strand contributes `q⁻¹/[2] ≠ 1`. -/
theorem sector_idle_inv_ne_one (q : R) (hq : q ≠ 0) (h2 : q + q⁻¹ ≠ 0) :
    q⁻¹ / (q + q⁻¹) ≠ 1 := by
  intro h
  rw [div_eq_one_iff_eq h2] at h
  have : q = 0 := by linear_combination -h
  exact hq this

end QOU.QBeta.LeptonStrandNormalisation
