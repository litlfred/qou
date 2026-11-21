import QOU.BraidsAndKnots.NucleonWeightSpaceTraces
import Mathlib.GroupTheory.Perm.Fin

/-!
# The count 12 as an `S_3` fixed-point count on the nucleon sectors

A candidate source for the `−12` in the proton identity
`m_p/m_e = 2((m_μ/m_e) F_Bor − 6)`, recorded with what it does and does not show.

The `S_3` fixed-point (Burnside) sum `Σ_{σ ∈ S_3} #Fix(σ)` on the flavour labellings
`Fin 3 → Bool` of the three strands:

* on the proton sector (two `u`, one `d`): `6`;
* on the neutron sector: `6`;
* on both nucleon sectors: `12`;
* on all of `V^{⊗3}` (all eight labellings): `24`.

At `q = 1` the Jimbo matrices on `W_p` become permutation matrices, and the sum of their traces
over the six elements of `S_3` is the same `6` (`own_sector_count_q1`).

So if the constant is a classical `S_3` count on `V^{⊗3}`, it equals `2 · 6` only when it is
taken on a nucleon sector (`2 ×` the own sector, or `1 ×` both nucleon sectors). The whole
space gives `24`. This links the count to a sector restriction. It does not decide between the
two sector readings, and it does not show the constant *is* such a count: that is open (#8809).
No measured value enters.
-/

namespace QOU.MassTheory.NucleonSectorBurnsideCount

open Matrix QOU.BraidsAndKnots.NucleonWeightSpaceTraces

/-- Number of `u` (= `true`) labels. -/
def ups (l : Fin 3 → Bool) : ℕ := (Finset.univ.filter fun i => l i = true).card

/-- Burnside sum: over `σ ∈ S_3`, the number of labellings with `k` up-labels fixed by `σ`. -/
def burnside (P : (Fin 3 → Bool) → Prop) [DecidablePred P] : ℕ :=
  ∑ σ : Equiv.Perm (Fin 3), (Finset.univ.filter fun l : Fin 3 → Bool => P l ∧ l ∘ σ = l).card

theorem burnside_proton : burnside (fun l => ups l = 2) = 6 := by decide
theorem burnside_neutron : burnside (fun l => ups l = 1) = 6 := by decide
theorem burnside_nucleons : burnside (fun l => ups l = 1 ∨ ups l = 2) = 12 := by decide
theorem burnside_whole : burnside (fun _ => True) = 24 := by decide

/-- At `q = 1` the summed traces of the six `S_3` elements on `W_p` give the same count `6`. -/
theorem own_sector_count_q1 :
    trace (1 : Matrix (Fin 3) (Fin 3) ℚ) + trace (A₁ (1 : ℚ)) + trace (A₂ (1 : ℚ))
      + trace (A₁ (1 : ℚ) * A₂ 1) + trace (A₂ (1 : ℚ) * A₁ 1)
      + trace (A₁ (1 : ℚ) * A₂ 1 * A₁ 1) = 6 := by
  simp [A₁, A₂, Matrix.trace_fin_three]
  norm_num

/-- For general `q` the same sum is not constant: the count is a `q = 1` statement. -/
theorem own_sector_sum_q {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    trace (1 : Matrix (Fin 3) (Fin 3) R) + trace (A₁ q) + trace (A₂ q)
      + trace (A₁ q * A₂ q) + trace (A₂ q * A₁ q) + trace (A₁ q * A₂ q * A₁ q)
      = 1 + 4 * q - 2 * q⁻¹ + 2 * q ^ 2 + q ^ 3 := by
  simp [A₁, A₂, Matrix.trace_fin_three]
  field_simp
  ring

end QOU.MassTheory.NucleonSectorBurnsideCount

/-!
## The labelled-closure count is `6` on each nucleon sector for every `q`

A labelled closure keeps each closed component's `u/d` label, so on the permutation braid
`T_σ` a labelling contributes its diagonal entry only if it is constant on the cycles of `σ`.
On `W_p = (uud, udu, duu)` the consistent labellings are: all three for `e`; `uud` for `σ₁`;
`duu` for `σ₂`; `udu` for `σ₁σ₂σ₁`; none for the two 3-cycles. With the closure weight
`q^{c(σ) − 3}` (`c` = number of closure components) the count is `6` for every `q`, and the
same holds on `W_n`. On `uuu` it is `5 + q²` (probe `mn_labelled_closure_probe.py`).

Disclosure: the weight `q^{c − n}` was found by inspecting the proton-sector entries. The
neutron result and the `uuu`/`ddd` failure were not used to choose it.
-/

namespace QOU.MassTheory.NucleonSectorBurnsideCount

open Matrix QOU.BraidsAndKnots.NucleonWeightSpaceTraces

variable {R : Type*} [Field R]

/-- Labelled-closure count on the proton sector: `6` for every `q ≠ 0`. -/
theorem labelled_count_proton (q : R) (hq : q ≠ 0) :
    3 + q⁻¹ * A₁ q 0 0 + q⁻¹ * A₂ q 2 2 + q⁻¹ * (A₁ q * A₂ q * A₁ q) 1 1 = 6 := by
  simp [A₁, A₂, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

/-- Labelled-closure count on the neutron sector `(udd, dud, ddu)`: also `6`. -/
theorem labelled_count_neutron (q : R) (hq : q ≠ 0) :
    3 + q⁻¹ * B₁ q 2 2 + q⁻¹ * B₂ q 0 0 + q⁻¹ * (B₁ q * B₂ q * B₁ q) 1 1 = 6 := by
  simp [B₁, B₂, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

/-- On `uuu` every crossing acts by `q`; the same weighted count is `5 + q²`, which is not
constant (it equals `6` only at `q² = 1`). -/
theorem labelled_count_uuu (q : R) (hq : q ≠ 0) :
    1 + q⁻¹ * q + q⁻¹ * q + q⁻¹ * q ^ 3 + q⁻¹ ^ 2 * q ^ 2 + q⁻¹ ^ 2 * q ^ 2 = 5 + q ^ 2 := by
  field_simp
  ring

end QOU.MassTheory.NucleonSectorBurnsideCount
