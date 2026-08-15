import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Thermo — the `β = ln q` dictionary (partition-function unification, R1)

The QOU Frobenius/Markov trace is `tr_M = ∑_{λ⊢n} y_λ(q) χ_λ`, a weighted
sum over Young diagrams (Wedderburn blocks).  Read as a statistical-
mechanics partition function `Z = ∑_states e^{-β E}`, the Wedderburn
blocks are the microstates and the **inverse temperature is `β = ln q`**:
the positive Frobenius weight `y_λ(q)` is the Boltzmann weight of block
`λ`, whose energy is read off as `E_λ = -ln y_λ / ln q`.

This file proves that dictionary is well posed and physically meaningful:

* `boltzmann_energyOf` — the read-off energy reproduces the weight
  (`e^{-β E_λ} = y_λ`); derive-then-check, not asserted.
* `energyOf_unique` — the energy is the *unique* solution (Boltzmann map
  is injective).
* `energyOf_le_iff` — **the correspondence is order-reversing**: a larger
  Frobenius weight is a *lower* energy, so the dominant Wedderburn block
  is the ground state.  This is the falsifiable physical content.
* `partition_sum_eq` — the stat-mech partition function written in energy
  variables equals the Frobenius weighted sum: `∑ d_λ e^{-β E_λ} = ∑ d_λ y_λ`.
* `logPos_of_one_lt` — for the substrate regime `q > 1`, `β = ln q > 0`.

Base ring `ℝ`: genuinely archimedean (`Real.exp`, `Real.log`, ordering),
correct per §7c.

LaTeX label: `prop:beta-eq-ln-q-dictionary`
-/

namespace QOU.Thermo

open scoped BigOperators

/-- Boltzmann weight `e^{-β E}` at inverse temperature `β`. -/
noncomputable def boltzmann (β E : ℝ) : ℝ := Real.exp (-β * E)

/-- Energy read off from a positive weight: `E = -ln y / β`. -/
noncomputable def energyOf (β y : ℝ) : ℝ := -Real.log y / β

/-- For the substrate regime `q > 1`, the inverse temperature `β = ln q`
is positive. -/
theorem logPos_of_one_lt {q : ℝ} (hq : 1 < q) : 0 < Real.log q :=
  Real.log_pos hq

/-- **Read-off is correct**: the energy `E_λ = -ln y/β` reproduces the
Boltzmann weight `y` (for `β ≠ 0`, `y > 0`). -/
theorem boltzmann_energyOf {β y : ℝ} (hβ : β ≠ 0) (hy : 0 < y) :
    boltzmann β (energyOf β y) = y := by
  unfold boltzmann energyOf
  rw [show -β * (-Real.log y / β) = Real.log y by field_simp]
  exact Real.exp_log hy

/-- **Uniqueness**: any energy whose Boltzmann weight is `y` equals the
read-off energy (the Boltzmann map is injective). -/
theorem energyOf_unique {β y E : ℝ} (hβ : β ≠ 0) (_hy : 0 < y)
    (h : boltzmann β E = y) : E = energyOf β y := by
  unfold boltzmann at h
  have hlog : -β * E = Real.log y := by
    rw [← h, Real.log_exp]
  unfold energyOf
  field_simp
  linarith [hlog]

/-- **Order-reversing**: at positive inverse temperature, a larger
Frobenius weight is a *lower* energy — the dominant Wedderburn block is
the ground state. -/
theorem energyOf_le_iff {β y₁ y₂ : ℝ} (hβ : 0 < β) (h1 : 0 < y₁) (h2 : 0 < y₂) :
    energyOf β y₁ ≤ energyOf β y₂ ↔ y₂ ≤ y₁ := by
  unfold energyOf
  rw [div_le_div_iff_of_pos_right hβ, neg_le_neg_iff, Real.log_le_log_iff h2 h1]

/-- **Partition function = Frobenius sum**: summing the Boltzmann weights
of the read-off energies over the Wedderburn blocks (with degeneracies
`d`) recovers the Frobenius weighted sum `∑ d_λ y_λ`. -/
theorem partition_sum_eq {ι : Type*} (s : Finset ι) (β : ℝ) (hβ : β ≠ 0)
    (d y : ι → ℝ) (hy : ∀ i ∈ s, 0 < y i) :
    ∑ i ∈ s, d i * boltzmann β (energyOf β (y i)) = ∑ i ∈ s, d i * y i := by
  refine Finset.sum_congr rfl (fun i hi => ?_)
  rw [boltzmann_energyOf hβ (hy i hi)]

end QOU.Thermo
