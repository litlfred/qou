/-
QOU.Mass.ArchimedeanTraceBridge — the archimedean functor is the logarithm: a multiplicative
categorical trace becomes an additive observable free energy, which LIFTS the additive crossing-energy
partition to the mass observable.

Arc context (bk-crossing mass-binding; bean `qou-brng`, residual R2 — the one item the residuals
audit left genuinely open). `QOU.Mass.SelfMutualPartition` proved, at the ADDITIVE crossing-energy
granularity, that mass = self part and binding = −(mutual part). It *assumed* the energy is additive.
The mass observable, however, carries the q-dimension Markov self-trace
`lw = (Σ_{λ⊢c+1} dim_q λ)/(c+1)` — a MULTIPLICATIVE object: the Markov/Jones trace factorises under
connected sum, `J(K₁ # K₂) = J(K₁)·J(K₂)` (Jones). The residual was: how does the multiplicative
trace at the categorical (fibre) level become the additive energy the partition needs?

The bridge is the **archimedean functor τ = logarithm** (the free energy of a partition-function-like
amplitude). This file proves that multiplicativity of the categorical amplitude *forces* additivity of
the observable free energy, so the additive partition `SelfMutualPartition` assumed is DERIVED here
from Jones multiplicativity — and binding is exactly the connected (interaction) free energy, which
vanishes iff the constituents are independent.

What stays a modelling input (stated, not faked): (1) that the substrate assembly amplitude *is* the
Markov trace, multiplicative under the nucleon-assembly connected sum (a citable theorem for the
Jones polynomial, asserted here as the hypothesis `Multiplicative`); (2) the dimensional dressing
`m = m_e · Vol · lw / ℏ_q²` (the CAL-1 scale `m_e`, the geometric `Vol`, the CAL-2 cusp `1/ℏ_q²`) —
calibration and geometry, not derivable from the trace structure. The bridge below is the piece
between them, and it is a theorem.

Ground ring `ℝ` (§7c: archimedean — `Real.log`, positivity). No fit.
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace QOU.Mass.ArchimedeanTraceBridge

open Finset

/-- The archimedean functor on a positive categorical amplitude `T`: the observable free energy
`E = log T`. (Sign convention: `log`; the mass-deficit binding is `−` the interaction free energy.) -/
noncomputable def freeEnergy (T : ℝ) : ℝ := Real.log T

/-- **Multiplicative trace ⟹ additive free energy.** The Markov/Jones trace is multiplicative under
connected sum (`J(K₁#K₂) = J(K₁)·J(K₂)`); its archimedean image `E = log T` is therefore additive.
This is why rest mass is EXTENSIVE (adds over constituents) — the additive-energy model of
`SelfMutualPartition` is the log-image of the multiplicative self-trace, not an independent
assumption. -/
theorem freeEnergy_connectedSum (T₁ T₂ : ℝ) (h₁ : 0 < T₁) (h₂ : 0 < T₂) :
    freeEnergy (T₁ * T₂) = freeEnergy T₁ + freeEnergy T₂ := by
  unfold freeEnergy
  exact Real.log_mul (ne_of_gt h₁) (ne_of_gt h₂)

/-- Extensivity over many constituents: the free energy of a product of positive self-amplitudes is
the sum of the constituent free energies. Rest mass adds over the `A` nucleons. -/
theorem freeEnergy_prod {ι : Type*} (s : Finset ι) (T : ι → ℝ) (hT : ∀ i ∈ s, 0 < T i) :
    freeEnergy (∏ i ∈ s, T i) = ∑ i ∈ s, freeEnergy (T i) := by
  unfold freeEnergy
  exact Real.log_prod s T (fun i hi => ne_of_gt (hT i hi))

/-- The interaction (connected) free energy of an assembly whose amplitude is the product of the
constituent self-amplitudes times an interaction factor `I`. -/
noncomputable def bindingFreeEnergy (I : ℝ) : ℝ := - freeEnergy I

/-- **The self/mutual partition, lifted to the multiplicative trace.** If the assembly amplitude is
`(∏ Tᵢ) · I` (constituent self-traces times the interaction factor), the observable free energy
splits as `Σ Eᵢ + log I`, so the mass-deficit binding `Σ Eᵢ − E_assembly` equals `−log I =
bindingFreeEnergy I`. This is `SelfMutualPartition.binding_eq_neg_mutualEnergy` DERIVED at the
Markov-trace level: the additivity is a consequence of trace multiplicativity, not an assumption. -/
theorem binding_eq_bindingFreeEnergy {ι : Type*} (s : Finset ι) (T : ι → ℝ) (I : ℝ)
    (hT : ∀ i ∈ s, 0 < T i) (hI : 0 < I) :
    (∑ i ∈ s, freeEnergy (T i)) - freeEnergy ((∏ i ∈ s, T i) * I) = bindingFreeEnergy I := by
  unfold bindingFreeEnergy
  rw [freeEnergy_connectedSum (∏ i ∈ s, T i) I (Finset.prod_pos hT) hI, freeEnergy_prod s T hT]
  ring

/-- **Binding vanishes exactly at independence.** For a positive interaction factor, the binding
free energy is zero iff the assembly amplitude factorises (`I = 1`, no interaction). Binding is
purely the connected part — the free-energy form of `binding_indep_of_self`. -/
theorem bindingFreeEnergy_eq_zero_iff (I : ℝ) (hI : 0 < I) :
    bindingFreeEnergy I = 0 ↔ I = 1 := by
  unfold bindingFreeEnergy freeEnergy
  rw [neg_eq_zero, Real.log_eq_zero]
  constructor
  · rintro (h | h | h)
    · exact absurd h (ne_of_gt hI)
    · exact h
    · linarith
  · intro h; right; left; exact h

/-- **A bound state has positive binding iff its interaction factor is below one.** With the
mass-deficit sign convention, `bindingFreeEnergy I > 0 ↔ I < 1`: the assembly amplitude is
*suppressed* relative to independent constituents exactly when the state is bound. -/
theorem bindingFreeEnergy_pos_iff (I : ℝ) (hI : 0 < I) :
    0 < bindingFreeEnergy I ↔ I < 1 := by
  unfold bindingFreeEnergy freeEnergy
  rw [neg_pos]
  exact Real.log_neg_iff hI

end QOU.Mass.ArchimedeanTraceBridge
