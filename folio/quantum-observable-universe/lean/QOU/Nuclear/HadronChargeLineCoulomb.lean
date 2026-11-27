import QOU.Nuclear.WeylSymmetricPairNotCoulomb
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# Charge lines on whole hadrons give the Coulomb pair term

Audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §31. Owner ruling 2026-11-22 ("Both"):
the U(1)_em grading enters as an explicit, labelled structural input, while its derivation
(Weinberg angle, Z scale) stays open.

`ChargePhaseYangBaxterObstruction` shows the charge phase cannot sit on the strands of the Hecke
braiding. Here it sits on the hadron: each nucleon block is tensored with one U(1) line `L_Q`,
`Q = n − 1` (`n` = number of `u` strands, `blockCharge_eq`). Distinct charges are distinct simple
objects, and two lines braid by `t^{Q Q'}` times the swap.

* `lineBraid_ybe`: the line braiding satisfies Yang–Baxter for every `t` (both sides carry the
  phase `t^{Q₁Q₂ + Q₁Q₃ + Q₂Q₃}`).
* `monodromy`: passing block `A` once round block `B` multiplies by `t^{2 Q_A Q_B}`.
* `log_monodromy`: over `ℝ`, `t > 0`, its log is `2 log t · Q_A Q_B`: a charge–charge term with
  `κ = 2 log t`, zero whenever a neutron is involved (`em_coulombOnNucleons`).
* `total_pp_sub_nn`: added to any isospin-symmetric flavour readout (pp = nn, e.g.
  `QCasimirPairGenericQ.pairDE_pp_eq_nn_of_blockData`), the pair split is pp − nn = κ, nonzero iff
  `t ≠ 1`.

The coupling `t` is not fixed here and is not fitted: it is to come from the corpus α_EM, which is
open. The charges themselves are the Gell-Mann–Nishijima input `Q = T₃ + B/2`, labelled as an input.
No empirical number enters.
-/

namespace QOU.QBeta.HadronChargeLineCoulomb

open QOU.QBeta.GaudinPair

section Generic

variable {K : Type*} [Field K]

/-- Phase of the U(1) line braiding between charges `Q`, `Q'`. -/
def linePhase (t : K) (Q Q' : ℤ) : K := t ^ (Q * Q')

/-- Yang–Baxter for three hadron lines: both orders give the same total phase. -/
theorem lineBraid_ybe (t : K) (Q₁ Q₂ Q₃ : ℤ) :
    linePhase t Q₁ Q₂ * linePhase t Q₁ Q₃ * linePhase t Q₂ Q₃
      = linePhase t Q₂ Q₃ * linePhase t Q₁ Q₃ * linePhase t Q₁ Q₂ := by
  unfold linePhase; ring

/-- Double braiding (monodromy) of two hadron lines. -/
def monodromy (t : K) (Q Q' : ℤ) : K := linePhase t Q Q' * linePhase t Q' Q

theorem monodromy_eq (t : K) (ht : t ≠ 0) (Q Q' : ℤ) :
    monodromy t Q Q' = t ^ (2 * Q * Q') := by
  unfold monodromy linePhase
  rw [← zpow_add₀ ht]; ring_nf

end Generic

/-- Block charge from the number of `u` strands. -/
def chargeOf (n : ℕ) : ℤ := (n : ℤ) - 1

/-- The em pair energy (log of the monodromy) in the sector with `nA`, `nB` up-strands. -/
noncomputable def emEnergy (t : ℝ) (nA nB : ℕ) : ℝ :=
  Real.log (monodromy t (chargeOf nA) (chargeOf nB))

theorem log_monodromy (t : ℝ) (ht : 0 < t) (nA nB : ℕ) :
    emEnergy t nA nB = (2 * Real.log t) * ((chargeOf nA : ℝ) * (chargeOf nB : ℝ)) := by
  unfold emEnergy
  rw [monodromy_eq t ht.ne', Real.log_zpow]
  push_cast; ring

/-- The em term is exactly the Coulomb shape on nucleons, with `c = 0`, `κ = 2 log t`. -/
theorem em_coulombOnNucleons (t : ℝ) (ht : 0 < t) :
    CoulombOnNucleons (emEnergy t) 0 (2 * Real.log t) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> rw [log_monodromy t ht] <;> simp [chargeOf]

/-- Flavour (isospin) readout plus the hadron-line em term: the pp − nn split is `κ = 2 log t`. -/
theorem total_pp_sub_nn (Ef : ℕ → ℕ → ℝ) (hiso : Ef 2 2 = Ef 1 1) (t : ℝ) (ht : 0 < t) :
    (Ef 2 2 + emEnergy t 2 2) - (Ef 1 1 + emEnergy t 1 1) = 2 * Real.log t := by
  rw [log_monodromy t ht, log_monodromy t ht, hiso]; simp [chargeOf]

/-- The split vanishes iff the coupling is trivial. -/
theorem split_ne_zero_iff (t : ℝ) (ht : 0 < t) : 2 * Real.log t ≠ 0 ↔ t ≠ 1 := by
  constructor
  · intro h h1; exact h (by rw [h1, Real.log_one, mul_zero])
  · intro h h0
    have : Real.log t = 0 := by linarith
    rcases Real.log_eq_zero.mp this with h' | h' | h'
    · linarith
    · exact h h'
    · linarith

end QOU.QBeta.HadronChargeLineCoulomb
